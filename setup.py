from setuptools import setup

if __name__ == "__main__":

    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        long_description = open('README.md').read()

    __version__ = "0.7.1"
    base_url = "https://github.com/pdpiech/prefpy_experiments"

    setup(name="prefpy-experiments",
          version=__version__,
          description="Rank aggregation algorithms",
          long_description=long_description,
          classifiers=[
              "Development Status :: 3 - Alpha",
              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
              "Programming Language :: Python :: 3.4",
              "Programming Language :: Python :: 3.5",
              "Intended Audience :: Science/Research",
              "Topic :: Scientific/Engineering"
          ],
          url=base_url,
          download_url="{0}/archive/prefpy_experiments-{1}.tar.gz".format(base_url, __version__),
          author="Peter Piech",
          license="GPL-3",
          packages=["prefpy_experiments"],
          install_requires=["prefpy"],
          zip_safe=False)
