all: dummy

dummy:
	python setup.py build_ext --inplace
	@rm -rf build

clean:
	@rm -f *.so
	@rm -f *.html
	@rm -f mir.c
	@rm -rf build
