from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
        name='SolarGUI',
        version='0.1.6',
        packages=find_packages(where="src"),
        url='https://github.com/AstrophysicsAndPython/SolarGUI',
        license='MIT',
        author='Astrophysics and Python, Syed Ali Mohsin Bukhari',
        author_email='astrophysicsandpython@gmail.com, syedali.b@outlook.com',
        description='A program which contains information about the solar system '
                    'planets, moon, pluto, Sun, and more.',
        long_description=readme,
        long_description_content_type="text/markdown",
        python_requires=">=3.7.*, <3.10.*",
        install_requires=["astropy>=4.3.1", "numpy>=1.21.6", "setuptools>=59.6.0",
                          "pillow>=9.1.1"],
        include_package_data=True,
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9"
            ],
        # https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way
        # -entry_points-and-scripts/
        entry_points={
            "gui_scripts": [
                "SolarGUI = SolarGUI.solar_gui:Main"
                ]
            }
        )
