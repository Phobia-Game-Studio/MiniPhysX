cmake_minimum_required (VERSION 3.13 FATAL_ERROR)

option(PX_MINGW "use MinGW/MSYS2" OFF)
option(PX_REDEFINE_WINDOWS "mark this ON if you link this library statically and include windows on your own" OFF)
option(PX_SUPPORT_PVD "support PhysX Visual Debugger" ON)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_COMPILE_FEATURES cxx_std_14)

set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g -D_DEBUG -DPX_DEBUG -DPX_CHECKED")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")

add_definitions(-DPX_PHYSX_STATIC_LIB)
if (PX_SUPPORT_PVD)
    add_definitions(-DPX_SUPPORT_PVD=1)
endif()

add_library(PhysX STATIC)
include(_source_files.cmake)

if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(PX_GCC ON)
    set(PX_CLANG OFF)
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(PX_CLANG ON)
    set(PX_GCC OFF)
endif()

target_compile_definitions(PhysX PRIVATE PX_MINGW=$<BOOL:${PX_MINGW}>
        PX_REDEFINE_WINDOWS=$<BOOL:${PX_REDEFINE_WINDOWS}>)

if(APPLE)
    target_compile_options(PhysX PRIVATE -Wall -Wno-unused-local-typedef -Wno-unused-private-field -Wno-macro-redefined
            -Wno-float-equal -Wno-bitwise-instead-of-logical -Wno-unused-but-set-variable)
else()
    if (PX_GCC)
        target_compile_options(PhysX PRIVATE -Wall
                -Wno-misleading-indentation -Wno-float-equal -Wno-unused-but-set-variable -Wno-maybe-uninitialized
                -Wno-invalid-offsetof  -Wno-uninitialized -Wno-unknown-pragmas -Wno-restrict -Wno-class-memaccess
                -Wno-nonnull -Wno-mismatched-new-delete -Wno-sign-compare -Wno-reorder -Wno-array-bounds
                -Wno-stringop-overflow -Wno-strict-aliasing -fno-strict-aliasing)
    else()
        target_compile_options(PhysX PRIVATE -Wall -Wno-misleading-indentation -Wno-unused-local-typedef
                -Wno-unused-private-field -Wno-macro-redefined -Wno-float-equal -Wno-bitwise-instead-of-logical
                -Wno-unused-but-set-variable)
    endif()
endif()
