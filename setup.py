from setuptools import setup, find_packages
from os import path
import urllib.request

pkg_name = "element_deeplabcut"
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), "r") as f:
    long_description = f.read()

with open(path.join(here, pkg_name, "version.py")) as f:
    exec(f.read())

with urllib.request.urlopen(
    "https://github.com/DeepLabCut/DeepLabCut/blob/main/requirements.txt"
) as f:
    dlc_requirements = f.read().decode("UTF-8").split("\n")

dlc_requirements.remove("")
dlc_requirements.append("future")

setup(
    name=pkg_name.replace("_", "-"),
    version=__version__,
    description="DeepLabCut DataJoint Element",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DataJoint",
    author_email="info@datajoint.com",
    license="MIT",
    url=f'https://github.com/datajoint/{pkg_name.replace("_", "-")}',
    keywords="neuroscience behavior pose-estimation science datajoint",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    scripts=[],
    install_requires=[
        "datajoint>=0.13",
        "element-interface>=0.3.0",
        "opencv-python-headless",
        "ipykernel>=6.0.1",
        "pygit2",
    ],
    extras_requires={
        "dlc_requirements": [dlc_requirements],
        # "dlc_default": ["deeplabcut @ git+https://github.com/DeepLabCut/DeepLabCut"]
        "dlc_default": ["deeplabcut[tf]>=2.2.1.1"],
        "dlc_apple_mchips": [
            "'deeplabcut[apple_mchips]'",
            "tables=3.7.0",
            "tensorflow-deps>=2.9.0",
            "keras >=2.12.0",
        ],
        "elements": [
            "element-lab>=0.2.0",
            "element-animal>=0.1.5",
            "element-session>=0.1.2",
            "element-interface>=0.5.0",
        ],
        "tests": ["pytest", "pytest-cov", "shutils"],
    },
)
