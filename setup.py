import setuptools

setuptools.setup(
    name="linear-regression-orquestra",
    author="Alessandro Sanvito",
    author_email="alessandro1.sanvito@mail.polimi.it",
    description="Quantum linear regression on Orquestra.",
    url="https://github.com/zapatacomputing/z-quantum-qubo",
    package_dir={"": "src/python"},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "dimod",
        "dwave-neal",
        "pandas",
        "numpy"
    ],
)
