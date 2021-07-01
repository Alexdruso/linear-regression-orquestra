import setuptools

setuptools.setup(
    name="linear-regression-orquestra",
    author="Alessandro Sanvito",
    author_email="alessandro1.sanvito@mail.polimi.it",
    description="Quantum linear regression on Orquestra.",
    url="https://github.com/zapatacomputing/z-quantum-qubo",
    packages=setuptools.find_namespace_packages(
        include=["zquantum.*"], where="src/python"
    ),
    package_dir={"": "src/python"},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "z-quantum-core",
        "z-quantum-qubo",
        "dimod",
        "dwave-neal",
        "pandas",
        "numpy"
    ],
)