from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gemini-api-framework",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="一个简单易用的Google Gemini API Python框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/makaixindalao/gemini-python-framework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "google-generativeai>=0.3.0",
        "pillow>=9.0.0",
    ],
)