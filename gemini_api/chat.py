"""
聊天会话模块
提供了与Gemini API进行多轮对话的功能
"""

from typing import Dict, List, Any


class ChatSession:
    """聊天会话类，用于管理与Gemini API的对话"""
    
    def __init__(self, chat_session: Any):
        """
        初始化聊天会话
        
        Args:
            chat_session: Gemini API的聊天会话对象
        """
        self.session = chat_session
    
    def send_message(self, message: str) -> str:
        """
        发送消息
        
        Args:
            message: 消息内容
            
        Returns:
            模型的回复
        """
        response = self.session.send_message(message=message)
        return response.text
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        获取聊天历史
        
        Returns:
            聊天历史列表
        """
        # 在新版API中，Chat对象没有直接的history属性
        # 返回一个简单的提示信息
        return [
            {"role": "system", "content": "聊天历史功能在当前API版本中暂不可用"},
            {"role": "system", "content": "请使用send_message方法继续对话"}
        ]