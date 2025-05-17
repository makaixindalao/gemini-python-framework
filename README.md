# Gemini API Python框架

这是一个用于调用Google Gemini API的简单Python框架，提供了一个易于使用的接口来与Gemini模型进行交互。

## 功能特点

- 简单易用的API接口
- 支持文本生成
- 支持图像处理
- 支持聊天模式
- 支持多种Gemini模型

## 安装

### 从GitHub安装

```bash
git clone https://github.com/makaixindalao/gemini-python-framework.git
cd gemini-python-framework
pip install -e .
```

### 使用pip安装

```bash
pip install gemini-api-framework
```

## 配置

在使用前，您需要设置Gemini API密钥。有两种方式：

1. 设置环境变量`GEMINI_API_KEY`
2. 在创建`GeminiClient`实例时传入API密钥

## 使用示例

### 基本文本生成

```python
from gemini_api import GeminiClient

# 方法1：通过环境变量设置API密钥
import os
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"
client = GeminiClient()

# 方法2：直接传入API密钥
client = GeminiClient(api_key="YOUR_API_KEY_HERE")

# 生成文本
response = client.generate_text("为什么天空是蓝色的？")
print(response)
```

### 使用不同模型

```python
from gemini_api import GeminiClient, MODELS

client = GeminiClient()
response = client.generate_text(
    "解释量子力学的基本原理",
    model=MODELS["gemini-pro"]
)
print(response)
```

### 聊天模式 - 单次对话

```python
messages = [
    {"role": "user", "content": "你好，你能做什么？"},
    {"role": "model", "content": "我是Gemini AI助手，可以回答问题、生成内容等。"},
    {"role": "user", "content": "给我讲个笑话"}
]
response = client.chat(messages)
print(response)
```

### 聊天模式 - 创建会话

```python
# 创建聊天会话
chat_session = client.create_chat_session(
    history=[
        {"role": "user", "content": "你好"},
        {"role": "model", "content": "你好！我是Gemini AI助手，有什么可以帮助你的吗？"}
    ]
)

# 发送消息
response = chat_session.send_message("你能做什么？")
print(f"AI: {response}")

response = chat_session.send_message("给我讲个笑话")
print(f"AI: {response}")
```

### 图像处理

```python
response = client.generate_with_images(
    "描述这张图片",
    ["path/to/image.jpg"],
    model=MODELS["gemini-pro-vision"]
)
print(response)
```

## 更多示例

查看`examples`目录获取更多使用示例：

- `basic_usage.py`: 基本文本生成示例
- `chat_example.py`: 聊天对话示例
- `image_example.py`: 图像处理示例

## 依赖

- Python 3.9+
- google-generativeai>=0.3.0
- pillow>=9.0.0

## 许可证

MIT