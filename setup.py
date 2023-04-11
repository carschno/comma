from setuptools import find_packages, setup


INSTALL_REQUIRES = ['pandas', 'matplotlib']
EXTRA_REQUIRES = ['pytest', 'jupyter']


setup(
    name="mhm",
    version='0.1.0',
    description="An agent-based simulation model to study mental health outcomes during covid-19 lockdowns.",
    url="https://github.com/covid19ABM/mhm",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Eva Viviani, Ji Qi",
    packages=find_packages(exclude=["tests", ".github"]),
    python_requires='>=3.6', 
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": EXTRA_REQUIRES},
)