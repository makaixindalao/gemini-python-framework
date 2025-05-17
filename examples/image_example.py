"""
图像处理示例
展示如何使用GeminiClient类处理图像
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
    print("图像处理示例")
    print("=" * 50)
    
    # 注意：您需要提供一个实际存在的图像文件路径
    image_path = "path/to/your/image.jpg"  # 替换为您的图像文件路径
    
    # 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"错误: 图像文件 '{image_path}' 不存在")
        print("请修改image_path变量为一个实际存在的图像文件路径")
        return
    
    try:
        response = client.generate_with_images(
            "描述这张图片",
            [image_path],
            model=MODELS["gemini-pro-vision"]
        )
        print(response)
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()