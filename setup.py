from setuptools import setup

with open('README.rst') as file:
	long_description = file.read()

setup(
	name='rockstar-py',
	version='1.1.3',
	author='Yan Orestes',
	author_email='yan.orestes@alura.com.br',
	packages=['rockstarpy'],
	description='Python transpiler for the esoteric language Rockstar',
	long_description=long_description,
	url='https://github.com/yanorestes/rockstar-py',
	download_url='https://github.com/yanorestes/rockstar-py/archive/1.1.0.zip',
	license='MIT',
	keywords='esoteric rockstar',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: Software Development :: Compilers'
	],
	entry_points={
		'console_scripts':['rockstar-py=rockstarpy.command_line:main']
	}
)