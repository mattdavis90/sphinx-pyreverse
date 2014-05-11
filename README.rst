Sphinx-pyreverse
=================

A simple sphinx extension to generate a UML diagram from python modules.

Install
--------

Install with::

	pip install -e git+https://github.com/mattdavis90/sphinx-pyreverse.git#egg=sphinx-pyreverse
	
or::

	git clone https://github.com/mattdavis90/sphinx-pyreverse.git
	cd sphinx-pyreverse
	sudo ./setup.py install

Usage
------

Add "sphinx_pyreverse" to your conf.py (make sure it is in the PYTHONPATH).

Call the directive with path to python module as content::

	.. uml:: {{path to the module}}
        
Requires pyreverse from pylint.
