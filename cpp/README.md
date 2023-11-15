# Description

The folders libs, pure-data and libpd_wrapper are required to compile every project compiled inside the samples directory. Each project will have its own Makefile to compile the code, these files will look for the binaries, classes and header files from the mentioned folders (libs, pure-data and lib_wrapper).

Each sample project will also contain the respective patch used in the application. Some classes (such as PdObject) should be copied from the samples in the original libpd repo in order to make it work.
