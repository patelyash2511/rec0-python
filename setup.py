from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memorylayer-py",
    version="1.0.0",
    author="Yash Patel",
    author_email="ycpatel1029@gmail.com",
    description="Official Python SDK for rec0 - Memory API for AI apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patelyash2511/rec0-python",
    project_urls={
        "Homepage": "https://rec0.vercel.app",
        "Documentation": "https://rec0.vercel.app/docs",
        "Bug Tracker": "https://github.com/patelyash2511/rec0-python/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
    ],
)
