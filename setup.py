from setuptools import setup, find_packages
from pathlib import Path

readme = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name='semanticanalyser-py',
    version='0.1.0',
    description='A package for semantic analysis using the BODC API',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(exclude=('tests', 'test*', 'examples', 'docs')),
    install_requires=[
        'requests>=2.25.0',
    ],
    include_package_data=True,
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: GPL-3.0 license',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.8',
    project_urls={
        'Homepage': 'https://github.com/ESSI-Lab/semanticanalyser-py',
        'Source': 'https://github.com/ESSI-Lab/semanticanalyser-py',
        'Tracker': 'https://github.com/ESSI-Lab/semanticanalyser-py/issues',
    },
)