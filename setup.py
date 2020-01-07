from setuptools import setup

setup(name='hydroutils',
      version='1.1',
      description='Utility classes to build and run hydrological models',
      author='Sopan Patil and Marc Stieglitz',
      license='MIT',
      packages=['hydroutils'],
      install_requires=['numpy', 'scipy'],
      classifiers=[
          'Programming Language :: Python :: 3.7',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering',
          'Intended Audience :: Science/Research'
      ],
      )
