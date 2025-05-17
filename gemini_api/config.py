"""
配置文件，用于存储Gemini API的配置信息
"""

# 可用的模型
MODELS = {
    "gemini-pro": "gemini-pro",
    "gemini-pro-vision": "gemini-pro-vision",
    "gemini-ultra": "gemini-ultra",
    "gemini-flash": "gemini-1.5-flash",
}

# 默认模型
DEFAULT_MODEL = MODELS["gemini-flash"]