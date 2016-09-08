cmake_minimum_required(VERSION 3.6)
project(libfixmath)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(CMAKE_DEBUG_POSTFIX d)

if(FIXMATH_SIN_LUT)
    message(STATUS "Enabling sin lookup table.")
    add_definitions(-DFIXMATH_SIN_LUT=1)
else()
    message(STATUS "Disabling sin lookup table.")
endif()

if(FIXMATH_NO_CACHE)
    message(STATUS "Disabling trigonometry cache.")
    add_definitions(-DFIXMATH_NO_CACHE=1)
else()
    message(STATUS "Enabling trigonometry cache.")
endif()

SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY         ${CMAKE_CURRENT_BINARY_DIR}/lib)
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG   ${CMAKE_ARCHIVE_OUTPUT_DIRECTORY})

set(SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/libfixmath)
set(SOURCE_FILES
    ${SOURCES}/fix16.hpp
    ${SOURCES}/fix16.h
    ${SOURCES}/fix16.c
    ${SOURCES}/fix16_exp.c
    ${SOURCES}/fix16_sqrt.c
    ${SOURCES}/fix16_str.c
    ${SOURCES}/fixmath.h
    ${SOURCES}/fract32.h
    ${SOURCES}/fract32.c
    ${SOURCES}/int64.h
    ${SOURCES}/uint32.h
    ${SOURCES}/uint32.c)

set(SOURCE_FILES
    ${SOURCE_FILES}
    ${SOURCES}/fix16_trig.c
    ${SOURCES}/fix16_trig_sin_lut.h)

add_library(libfixmath STATIC ${SOURCE_FILES})