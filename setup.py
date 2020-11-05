from distutils.core import setup

VERSION = "v1.1"

setup(
    name = "pyfractals",
    packages = ["pyfractals"],
    version = VERSION,
    license = "MIT",
    description = "Python Module which creates fractals design.",
    author = "Abhay Tripathi",
    author_email = "abhay.triipathi@gmail.com",
    url = "https://github.com/AbhayTr/PyFractals",
    download_url = "https://github.com/AbhayTr/PyFractals/archive/" + VERSION + ".tar.gz",
    keywords = ["PyFractals", "Fractal", "PyMandelBrot", "Fractals", "MandelBrot", "Infinity", "MandelBrot Graph"],
    install_requires = [
        "Pillow",
        "consolebar",
        "numpy",
        "matplotlib"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
