"""Environment report used in Lab 1 and in every project README."""
import importlib.metadata
import platform
import sys

PACKAGES = ("numpy", "pandas", "matplotlib", "scikit-learn", "biopython", "pytest")


def package_version(name: str):
    """Return the installed version string of a package, or None if not installed."""
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def check_environment(packages=PACKAGES):
    """Return a dictionary containing Python version, system platform, and requested package versions."""
    return {
        "python": platform.python_version(),
        "platform": platform.system(),
        "packages": {pkg: package_version(pkg) for pkg in packages},
    }


if __name__ == "__main__":
    report = check_environment()
    print("=== Environment Report ===")
    print(f"Python Version : {report['python']}")
    print(f"Platform       : {report['platform']}")
    print("Packages       :")
    for pkg, ver in report["packages"].items():
        print(f"  {pkg}: {ver}")

    sys.exit(0)
