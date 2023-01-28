import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="ai2api",
    version="0.0.1",
    author="Manjunath Maigur",
    author_email="manjumbmb97@gmail.com",
    description=("Yet another MLOps tool."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manjumaigur/ai2api",
    project_urls={
        "Bug Tracker": "https://github.com/manjumaigur/ai2api",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "ai2api = ai2api.cli:main",
        ]
    },
)
