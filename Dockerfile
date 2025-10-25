FROM node:18-alpine AS frontend-builder

# 构建前端
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Python 运行环境
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用文件
COPY web_server.py .

# 从构建阶段复制前端构建产物
COPY --from=frontend-builder /frontend/dist ./frontend

# 创建数据目录
RUN mkdir -p /data

# 暴露端口
EXPOSE 8080

# 环境变量
ENV PORT=8080
ENV DATA_DIR=/data

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/health')" || exit 1

# 启动应用
CMD ["python", "web_server.py"]