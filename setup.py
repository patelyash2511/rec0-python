from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memorylayer-py",
    version="0.1.1",
    author="rec0",
    author_email="support@rec0.vercel.app",
    description="Privacy-first memory API for LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patelyash2511/rec0-python",
    project_urls={
        "Homepage": "https://rec0.vercel.app",
        "Documentation": "https://rec0.vercel.app/docs",
        "Bug Tracker": "https://github.com/patelyash2511/rec0-python/issues",
        "Repository": "https://github.com/patelyash2511/rec0-python",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
        "httpx>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
        ]
    },
)
