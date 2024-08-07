from setuptools import setup, find_packages

setup(
    name="pytorchts",
    version="0.6.0",
    description="PyTorch Probabilistic Time Series Modeling framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Lenushka Sablin",
    author_email="1020030829@qq.com",
    url="https://github.com/sablin-39/pytorch-ts",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.6",
    install_requires=[
        "torch>=1.8.0",
        "gluonts>=0.12.8",
        "holidays",
        "numpy",
        "pandas",
        "scipy",
        "tqdm",
        "matplotlib",
        "tensorboard",
    ],
    test_suite="tests",
    tests_require=["flake8", "pytest"],
)
