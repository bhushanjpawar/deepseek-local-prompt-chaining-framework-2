from setuptools import setup, find_packages

setup(
    name="deepseek_prompt_chaining",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "pydantic",
        "python-dotenv"
    ]
)