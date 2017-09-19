[![Build Status](https://travis-ci.org/uilianries/conan-winpcap.svg?branch=release/4.1.3)](https://travis-ci.org/uilianries/conan-winpcap)  [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Download](https://api.bintray.com/packages/uilianries/conan/winpcap%3Auilianries/images/download.svg?version=4.1.3%3Astable)](https://bintray.com/uilianries/conan/winpcap%3Auilianries/4.1.3%3Astable/link)

## WinPCAP library is an API for capturing network traffic for Windows

![conan-winpcap](conan-winpcap.jpg)

[Conan.io](https://conan.io) package for [winpcap](https://github.com/wireshark/winpcap) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/uilianries/conan/winpcap%3Auilianries).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload winpcap/4.1.3@uilianries/stable --all

## Reuse the packages

### Basic setup

    $ conan install winpcap/4.1.3@uilianries/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    winpcap/4.1.3@uilianries/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[BSD](LICENSE)
