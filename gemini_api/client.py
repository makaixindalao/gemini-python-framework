"""
Gemini API客户端
提供了一个简单的接口来调用Gemini API
"""

import os
from typing import Dict, List, Optional, Any, Union
import PIL.Image

from google import genai
from google.genai import types

from .config import DEFAULT_MODEL
from .chat import ChatSession


class GeminiClient:
    """Gemini API客户端类"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_MODEL):
        """
        初始化Gemini客户端
        
        Args:
            api_key: Gemini API密钥，如果为None，则使用环境变量GEMINI_API_KEY
            model: 使用的模型名称
        """
        # 获取API密钥（优先级：参数 > 环境变量）
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API密钥未设置，请通过参数传入或设置环境变量GEMINI_API_KEY")
        
        # 初始化客户端
        self.client = genai.Client(api_key=self.api_key)
        
        # 设置默认模型
        self.model = model
    
    def generate_text(self, prompt: str, model: Optional[str] = None) -> str:
        """
        生成文本
        
        Args:
            prompt: 提示文本
            model: 模型名称，如果为None则使用默认模型
        
        Returns:
            生成的文本
        """
        model_name = model or self.model
        
        # 调用API
        response = self.client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        
        return response.text
    
    def generate_with_images(self, prompt: str, images: List[Union[str, PIL.Image.Image]], model: Optional[str] = None) -> str:
        """
        使用图像和文本生成内容
        
        Args:
            prompt: 提示文本
            images: 图像列表，可以是文件路径或PIL.Image对象
            model: 模型名称，如果为None则使用默认模型
        
        Returns:
            生成的文本
        """
        model_name = model or self.model
        
        # 准备内容
        contents = [prompt]
        
        # 添加图像
        for img in images:
            if isinstance(img, str):
                # 如果是文件路径，加载图像
                image = PIL.Image.open(img)
                contents.append(image)
            else:
                # 如果已经是PIL.Image对象，直接使用
                contents.append(img)
        
        # 调用API
        response = self.client.models.generate_content(
            model=model_name,
            contents=contents
        )
        
        return response.text
    
    def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None) -> str:
        """
        聊天模式
        
        Args:
            messages: 消息列表，格式为[{"role": "user", "content": "你好"}, {"role": "model", "content": "你好！"}]
            model: 模型名称，如果为None则使用默认模型
        
        Returns:
            生成的回复
        """
        model_name = model or self.model
        
        # 转换消息格式
        history = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            history.append(types.Content(role=role, parts=[types.Part(text=content)]))
        
        # 创建聊天会话
        chat = self.client.chats.create(
            model=model_name,
            history=history[:-1] if len(history) > 1 else []
        )
        
        # 发送最后一条消息
        last_message = history[-1].parts[0].text if history else ""
        response = chat.send_message(message=last_message)
        
        return response.text
    
    def create_chat_session(self, history: Optional[List[Dict[str, str]]] = None, model: Optional[str] = None) -> ChatSession:
        """
        创建聊天会话
        
        Args:
            history: 历史消息列表，格式为[{"role": "user", "content": "你好"}, {"role": "model", "content": "你好！"}]
            model: 模型名称，如果为None则使用默认模型
            
        Returns:
            聊天会话对象
        """
        model_name = model or self.model
        
        # 转换消息格式
        chat_history = []
        if history:
            for msg in history:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                chat_history.append(types.Content(role=role, parts=[types.Part(text=content)]))
        
        # 创建聊天会话
        chat = self.client.chats.create(
            model=model_name,
            history=chat_history
        )
        
        return ChatSession(chat)
    
    def upload_file(self, file_path: str) -> Any:
        """
        上传文件到Gemini API
        
        Args:
            file_path: 文件路径
            
        Returns:
            上传的文件对象
        """
        return self.client.files.upload(file=file_path)