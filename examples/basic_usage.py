"""
基本使用示例
展示如何使用GeminiClient类进行基本的API调用
"""

import os
import sys
import pathlib

# 添加父目录到sys.path，以便能够导入gemini_api模块
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from gemini_api import GeminiClient, MODELS

# 设置API密钥（也可以在环境变量中设置）
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"  # 替换为您的API密钥

def main():
    # 创建客户端实例
    client = GeminiClient()
    
    print("=" * 50)
    print("示例1: 基本文本生成")
    print("=" * 50)
    response = client.generate_text("为什么天空是蓝色的？")
    print(response)
    
    print("\n" + "=" * 50)
    print("示例2: 使用不同模型")
    print("=" * 50)
    try:
        response = client.generate_text(
            "解释量子力学的基本原理",
            model=MODELS["gemini-pro"]
        )
        print(response)
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()