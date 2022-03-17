"""A setuptools based setup module.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(

    name='pyparcels',  # Required

    version='1.1.0',  # Required

    description='Helper functions for simplifying parcel fabric workflows with the ArcGIS Python API',  # Optional

    long_description=long_description,  # Optional

    long_description_content_type='text/markdown',  # Optional (see note above)

    url='https://github.com/kgalliher/arcgis-pythonapi/',  # Optional

    author='Ken Galliher',  # Optional

    author_email='kgalliher092@gmail.com',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='arcgis python api, parcels, development',  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={'': 'pyparcels'},  # Optional

    # packages=find_packages(where="pyparcels", include=["pyparcels.utils", "pyparcels.features", "pyparcels.parcels", "pyparcels.versioning"]),  # Required
    packages=["pyparcels.utils", "pyparcels.features", "pyparcels.parcels", "pyparcels.versioning"],

    python_requires='>=3.6, <4',

    # install_requires=['arcgis'],  # Optional

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/kgalliher/arcgis-pythonapi/issues/',
        'Source': 'https://github.com/kgalliher/arcgis-pythonapi/',
    },
)
