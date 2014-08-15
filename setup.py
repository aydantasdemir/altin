from setuptools import setup

setup(
    name = 'altin',
    packages = ['altin'],
    version = '0.0.4',
    description = 'Check last 30 days gold prices with email',
    author='Aydan Tasdemir',
    author_email='aydantasdemir@gmail.com',
    url='https://github.com/aydantasdemir/altin',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'altin = altin.altin:main',
        ],
    },
)
