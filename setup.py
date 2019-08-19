from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['genmsg'],
    package_dir={'': 'src'},
    setup_requires=['catkin_pkg'],
)

setup(**d)
