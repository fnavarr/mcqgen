from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Fernando Navarro',
    author_email = 'fnavarro@citecs.com.mx',
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages = find_packages()
)