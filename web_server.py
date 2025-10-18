from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json
import os
from pathlib import Path
import glob

app = Flask(__name__)
CORS(app)

# 配置
DATA_DIR = "/data"  # JSON文件所在目录
PORT = 8080

@app.route('/')
def index():
    """返回主页面"""
    html_file = Path(__file__).parent / "hot_trends_viewer.html"
    if html_file.exists():
        return send_file(html_file)
    return """
    <!DOCTYPE html>
    <html>
    <head><title>请先创建网页</title></head>
    <body>
        <h1>请将前面生成的HTML保存为 hot_trends_viewer.html</h1>
        <p>并放在与此脚本相同的目录下</p>
    </body>
    </html>
    """

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

if __name__ == '__main__':
    print("=" * 60)
    print("   热搜分析可视化服务器")
    print("=" * 60)
    print(f"🌐 服务地址: http://localhost:{PORT}")
    print(f"📁 数据目录: {os.path.abspath(DATA_DIR)}")
    print("=" * 60)
    
    # 检查是否有HTML文件
    html_file = Path(__file__).parent / "hot_trends_viewer.html"
    if not html_file.exists():
        print("\n⚠️  警告：未找到 hot_trends_viewer.html")
        print("   请将HTML文件保存到当前目录\n")
    
    app.run(host='0.0.0.0', port=PORT, debug=False)