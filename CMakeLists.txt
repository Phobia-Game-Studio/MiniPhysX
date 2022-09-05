cmake_minimum_required (VERSION 3.15 FATAL_ERROR)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILE_FEATURES cxx_std_14)

add_library(PhysX STATIC)
include(_source_files.cmake)

target_compile_options(PhysX PRIVATE -Wall -Wno-misleading-indentation -Wno-unused-local-typedef -Wno-unused-private-field)
