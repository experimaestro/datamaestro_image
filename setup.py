import sys
try:
    from setuptools import setup, find_namespace_packages
except ImportError:
    print("Please upgrade pip: find_namesspace_packages not found")
    sys.exit(1)

setup(
    name='datamaestro_image',
    version='0.1',
    description='Image related datasets',
    author='Benjamin Piwowarski',
    author_email='benjamin@piwowarski.fr',
    url='https://github.com/bpiwowar/datamaestro_image',
    license='MIT',
    python_requires='>=3.5',
    packages=find_namespace_packages(include="datamaestro_image.*"),
    package_data={
        '': [ '*.yaml' ]
    },
    install_requires=[
        'datamaestro'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'datamaestro.repositories': [
            'image = datamaestro_image:Repository'
        ]

    }
)
