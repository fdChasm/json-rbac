import setuptools

packages = [
    'json_rbac',
]

setuptools.setup(
    name="json-rbac",
    version="0.1",
    packages=packages,
    package_dir={'' : 'src'},
    install_requires=["simple-rbac"],
    author="Chasm",
    author_email="fd.chasm@gmail.com",
    url="https://github.com/fdChasm/json-rbac",
    license="MIT",
    description="Support for loading and reload simple-rbac rules from json config files.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
)
