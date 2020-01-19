from distutils.core import setup
from setuptools import setup
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
		long_description = f.read()


setup(
	long_description=long_description,
	long_description_content_type='text/markdown',
	name = 'pyqueues',         # How you named your package folder (MyLib)
	packages = ['pyqueues'],   # Chose the same as "name"
	version = '1.2',      # Start with a small number and increase it with every change you make
	license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	description = 'A library for Priory-Queues containing Indexed-Priority-Queue and Simple Priority-Queue',   # Give a short description about your library
	author = 'Abdul Salam',                   # Type in your name
	author_email = 'abdulsalamone@gmail.com',      # Type in your E-Mail
	url = 'https://github.com/abecus/Queue',   # Provide either the link to your github or to your website
	download_url = 'https://github.com/abecus/Queue/archive/master.zip',    # I explain this later on
	keywords = ["pyqueues", 'queues', "queue", 'priority queue', 'priority', "pq", "heap"],   # Keywords that define your package best
	install_requires=[],
	classifiers=[
		"Operating System :: OS Independent",
		'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',      # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',   # Again, pick a license
		'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		"Programming Language :: Python :: Implementation :: PyPy"
	],
)