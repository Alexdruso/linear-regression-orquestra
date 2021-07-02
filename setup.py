import setuptools

setuptools.setup(
    name                            = "linear-regression-orquestra",
    version                         = "0.0.0",
    author                          = "Alessandro Sanvito",
    author_email                    = "alessandro1.sanvito@mail.polimi.it",
    packages                        = setuptools.find_packages(),
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        "dimod",
        "dwave-neal",
        "pandas",
        "numpy"
   ],
)
