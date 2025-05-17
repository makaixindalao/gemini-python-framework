"""
Gemini API Python框架
提供了一个简单易用的接口来调用Google Gemini API
"""

from .client import GeminiClient
from .chat import ChatSession
from .config import MODELS, DEFAULT_MODEL

__version__ = '0.1.0'