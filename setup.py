from setuptools import setup, find_packages

setup(
    name='my-project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'twine'
    ],
    entry_points={
        'console_scripts': [
            'convert-images = my_project.convert_images:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
)
