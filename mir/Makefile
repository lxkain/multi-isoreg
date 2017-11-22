all: dummy

dummy:
	python setup.py build_ext --inplace
	rm -rf build

clean:
	rm *.so
	rm *.html
	rm mir.c
	rm -rf build
