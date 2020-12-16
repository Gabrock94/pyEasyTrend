from setuptools import setup
import os

setup(name='pyEasyTrend',
    version='0.0.0.1',
    description='A Python package to perform trend analysis using a single-line command.',
    long_description="A Python package to perform trend analysis using a single-line command.",
    url='https://github.com/Gabrock94/https://github.com/Gabrock94/pyEasyTrend',
    download_url='https://github.com/Gabrock94/pyEasyTrend/archive/0.0.0.1.tar.gz',
    author='Giulio Gabrieli',
    author_email='gack94@gmail.com',
    license='GPL-3.0',
    packages=['pyeasytrend'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas'
    ],
    keywords = ["Trend Analysis","Linear model",'Full Model','Reduced model'],
    classifiers = [ 
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License (GPL)',
        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        #Operating Systems
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: Linux',
        
        #Topic
        'Topic :: Trend Analysis',
        'Topic :: Social Sciences',
        'Topic :: Psychology :: Cognitive Sciences',

        #Intended Audience
        'Intended Audience :: Physiologists',
        'Intended Audience :: Psychologists :: Neuroscientists',
        'Intended Audience :: Data Scientists',
        'Intended Audience :: Cool people',
        'Intended Audience :: Researchers',
    ],
    zip_safe=False,
    include_package_data=False,
)

