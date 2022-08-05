from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_pds',
    version='1.0.0',
    description='Package to clean folders',
    author='Petrik Dima',
    author_email='petrikdima16@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder_pds.clean:clean']},
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",]
)