from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dokos_lmdm_edi",
    version="1.0.0",
    description="EDI Integration App for Dokos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Company",
    author_email="your@email.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        # frappe is already installed in the bench environment
    ],
    python_requires=">=3.8",
)
