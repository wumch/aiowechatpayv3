from setuptools import setup


with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

setup(
    name="aiowechatpayv3",
    version="1.3.10",
    author="minibear",
    description="微信支付 API v3 Python SDK async(python sdk for wechatpay v3)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="python sdk wechatpay async api v3 微信支付",
    url="https://github.com/minibear2021/wechatpayv3",
    packages=["aiowechatpayv3"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["requests>=2.21.0", "httpx>=0.23.0", "cryptography>=35.0.0"],
)
