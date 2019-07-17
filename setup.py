from setuptools import find_packages, setup

required_packages = ["click", "requests", "layeredconfig"]

extras_require = None

setup(
    name="tempo_log",
    version="0.0.3",
    description="logging workload from console",
    author="Łukasz Bołdys",
    author_email="",
    url="https://github.com/utek/tlog",
    packages=find_packages(),
    include_package_data=True,
    test_suite="tests",
    install_requires=required_packages,
    extras_require=extras_require,
    tests_require=["mock", "pytest<5.0", "bunch"],
    entry_points={"console_scripts": ["tlog = tempo.worklog:logwork"]},
)
