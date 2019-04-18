import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yalp",
    version="0.0.1",
    author="Tom Gurion",
    author_email="nagasaki45@gmail.com",
    description="Yet another log parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nagasaki45/yalp",
    py_modules=["yalp"]
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
