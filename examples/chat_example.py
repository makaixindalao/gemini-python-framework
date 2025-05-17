"""
聊天示例
展示如何使用GeminiClient类进行聊天对话
"""

import os
import sys
import pathlib

# 添加父目录到sys.path，以便能够导入gemini_api模块
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from gemini_api import GeminiClient

# 设置API密钥（也可以在环境变量中设置）
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"  # 替换为您的API密钥

def main():
    # 创建客户端实例
    client = GeminiClient()
    
    print("=" * 50)
    print("示例1: 聊天模式 - 单次对话")
    print("=" * 50)
    messages = [
        {"role": "user", "content": "你好，你能做什么？"},
        {"role": "model", "content": "我是Gemini AI助手，可以回答问题、生成内容等。"},
        {"role": "user", "content": "给我讲个笑话"}
    ]
    response = client.chat(messages)
    print(response)
    
    print("\n" + "=" * 50)
    print("示例2: 聊天模式 - 创建会话")
    print("=" * 50)
    # 创建聊天会话
    chat_session = client.create_chat_session(
        history=[
            {"role": "user", "content": "你好"},
            {"role": "model", "content": "你好！我是Gemini AI助手，有什么可以帮助你的吗？"}
        ]
    )
    
    # 发送消息
    print("用户: 你能做什么？")
    response = chat_session.send_message("你能做什么？")
    print(f"AI: {response}")
    
    print("用户: 给我讲个笑话")
    response = chat_session.send_message("给我讲个笑话")
    print(f"AI: {response}")
    
    # 获取聊天历史
    print("\n聊天历史:")
    history = chat_session.get_history()
    for msg in history:
        print(f"{msg['role']}: {msg['content']}")

if __name__ == "__main__":
    main()