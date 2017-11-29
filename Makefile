all: dummy

dummy:
	python setup.py build_ext --inplace
	rm -rf build

clean:
	rm mir/*.so
	rm mir/*.html
	rm mir/mir.c
	rm -rf build
