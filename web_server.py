from flask import Flask, jsonify, send_from_directory, send_file
from flask_cors import CORS
import json
import os
from pathlib import Path
import glob

app = Flask(__name__)
CORS(app)

# 配置
DATA_DIR = os.getenv("DATA_DIR", "/data")  # JSON文件所在目录
PORT = int(os.getenv("PORT", 8080))
FRONTEND_DIR = Path(__file__).parent / "frontend"

@app.route('/')
def index():
    """返回 Vue 构建的 index.html"""
    index_file = FRONTEND_DIR / "index.html"
    if index_file.exists():
        return send_file(index_file)
    return """
    <!DOCTYPE html>
    <html>
    <head><title>前端未构建</title></head>
    <body>
        <h1>前端资源未找到</h1>
        <p>请确保已构建 Vue 前端项目</p>
        <pre>
cd frontend
npm install
npm run build
        </pre>
    </body>
    </html>
    """, 404

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    """服务前端静态资源"""
    assets_dir = FRONTEND_DIR / "assets"
    if assets_dir.exists():
        return send_from_directory(assets_dir, filename)
    return "Asset not found", 404

@app.route('/api/files')
def get_files():
    """获取所有JSON文件列表"""
    json_files = glob.glob(os.path.join(DATA_DIR, "hot_trends_analysis_*.json"))
    # 按修改时间倒序排列（最新的在前）
    json_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    # 只返回文件名
    filenames = [os.path.basename(f) for f in json_files]
    return jsonify(filenames)

@app.route('/api/data/<filename>')
def get_data(filename):
    """获取指定JSON文件的内容"""
    # 安全检查：防止路径遍历攻击
    if '..' in filename or '/' in filename or '\\' in filename:
        return jsonify({"error": "Invalid filename"}), 400
    
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/latest')
def get_latest():
    """获取最新的分析结果"""
    json_files = glob.glob(os.path.join(DATA_DIR, "hot_trends_analysis_*.json"))
    
    if not json_files:
        return jsonify({"error": "No data files found"}), 404
    
    # 获取最新的文件
    latest_file = max(json_files, key=os.path.getmtime)
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health():
    """健康检查端点"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("   热搜分析可视化服务器 (Vue 3 版本)")
    print("=" * 60)
    print(f"🌐 服务地址: http://localhost:{PORT}")
    print(f"📁 数据目录: {os.path.abspath(DATA_DIR)}")
    print(f"🎨 前端目录: {FRONTEND_DIR.absolute()}")
    print("=" * 60)
    
    # 检查前端文件
    if not FRONTEND_DIR.exists():
        print("\n⚠️  警告：未找到前端构建目录")
        print("   请先构建 Vue 前端项目：")
        print("   cd frontend && npm install && npm run build\n")
    elif not (FRONTEND_DIR / "index.html").exists():
        print("\n⚠️  警告：前端未构建")
        print("   请运行：cd frontend && npm run build\n")
    else:
        print("\n✅ 前端资源已就绪\n")
    
    app.run(host='0.0.0.0', port=PORT, debug=False)