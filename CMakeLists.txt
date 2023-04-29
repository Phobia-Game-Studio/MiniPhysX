cmake_minimum_required (VERSION 3.13 FATAL_ERROR)

option(PX_CLANG "use clang" ON)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILE_FEATURES cxx_std_14)

set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g -D_DEBUG -DPX_DEBUG -DPX_CHECKED")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

add_definitions(-DPX_PHYSX_STATIC_LIB)

if(PX_CLANG)
    add_definitions(-DPX_CLANG)
endif()

add_library(PhysX STATIC)
include(_source_files.cmake)

if(APPLE)
target_compile_options(PhysX PRIVATE -Wall -Wno-unused-local-typedef -Wno-unused-private-field -Wno-macro-redefined -Wno-float-equal)
else()
target_compile_options(PhysX PRIVATE -Wall -Wno-misleading-indentation -Wno-unused-local-typedef -Wno-unused-private-field -Wno-macro-redefined -Wno-float-equal)
endif()
