import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='timer.py',
    version='2.5.0',
    author='Randy Cahya Wihandika',
    author_email='rendicahya@gmail.com',
    description='Easy and accurate timer for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rendicahya/timer.py',
    packages=setuptools.find_packages(),
    install_requires=['print-color'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
