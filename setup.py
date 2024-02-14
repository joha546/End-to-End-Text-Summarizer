import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.1.0"
REPO_NAME = "End-to-End Text Summarization"
AUHORT_NAME = "joha546"
SRC_REPO = "end-to-end-text-summmarizer"
AUTHOR_EMAIL = "joh60483@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUHORT_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A Python library for NLP application",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{AUHORT_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker": "https://github.com/joha546/end-to-end-text-summmarizer/issues",
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")
)