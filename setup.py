from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="multivis",
    version="0.1.4",
    description="multivis is a data visualisation package that produces both static and interactive visualisations targeted towards the Omics community.",
    long_description=long_description,
    license="MIT License",
    url="https://github.com/brettChapman/multivis",
    packages=["multivis", "multivis.utils"],
    python_requires=">=3.5",
    install_requires=["numpy>=1.12",
                      "pandas",
		      "matplotlib",
		      "seaborn",
	 	      "networkx",
                      "scipy",
                      "scikit-learn",
		      "tqdm"],
    author="Brett Chapman",
    author_email="brett.chapman@ecu.edu.au, brett.chapman78@gmail.com"
)
