import setuptools

with open("README.md","r") as file:
	long_description = file.read()

setuptools.setup(
	name = "preprocessing_yaswanth", #this should be unique
	version = "0.0.2",
	author = "Yaswanth Babu",
	author_email = "sunnyyashu178@gmail.com",
	description = "This is preprocessing package",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	package = setuptools.find_packages(),
	classifiers = ["Programming Language :: Python :: 3",
	"License :: OSI Aproved :: MIT License",
	"Operating System :: OS Independent"],
	python_requires = ">=3.5"
	)
