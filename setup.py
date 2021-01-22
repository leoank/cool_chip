try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open("README.md").read()

setup(
    long_description=readme,
    name="cool_chip",
    version="0.1.0",
    description="Cooling electronic chips",
    python_requires="==3.*,>=3.8.0",
    author="Ankur Kumar",
    author_email="ank@leoank.me",
    license="MIT",
    packages=[
        "cool_chip",
        "cool_chip.geometry",
        "cool_chip.simulation",
        "cool_chip.analysis",
    ],
    package_dir={"": "src"},
    package_data={},
    install_requires=[
        "bibcure ==0.3.*,>=0.3.0",
        "matplotlib==3.*,>=3.3.2",
        "numpy==1.*,>=1.19.2",
        "sympy==1.7.*,>=1.7.1",
    ],
    dependency_links=[],
    extras_require={
        "dev": [
            "black==19.*,>=19.10b0",
            "darglint==1.*,>=1.5.8",
            "flake8==3.*,>=3.8.4",
            "flake8-black==0.*,>=0.2.1",
            "mypy==0.*,>=0.790.0",
            "pre-commit==2.*,>=2.9.3",
            "pytest==6.*,>=6.2.1",
        ]
    },
)
