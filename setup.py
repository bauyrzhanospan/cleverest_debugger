from setuptools import find_packages, setup
setup(
    name='cleverest_debugger',
    packages=find_packages(include=['cleverest_debugger']),
    version='1.0.0',
    description='Debugger as decorator for functions and methods',
    author='Bauyrzhan Ospan, CEO "Cleverest Technologies LLP"',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.2.0'],
    test_suite='tests',
)