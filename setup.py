from pathlib import Path

from setuptools import find_packages, setup


def get_long_description() -> str:
    return Path("README.md").read_text(encoding="utf8")


setup(
    name="rhymes-with",
    use_scm_version=True,
    url="https://github.com/eivindjahren/rhymes-with",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["pronouncing"],
    entry_points={
        "console_scripts": [
            "rhymes_with=rhymes_with.__main__:main",
        ],
    },
    license="GPL-3.0",
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    setup_requires=["setuptools_scm"],
    include_package_data=True,
)
