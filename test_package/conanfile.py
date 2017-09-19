"""Validation for Pcap library package

"""
from os import getenv
from conans import CMake
from conans import ConanFile


class TestPcapConan(ConanFile):
    """Build test with winpcap package
    """
    author = "Uilian Ries <uilianries@gmail.com>"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    channel = getenv("CONAN_CHANNEL", "testing")
    username = getenv("CONAN_USERNAME", "uilianries")
    requires = "winpcap/4.1.3@%s/%s" % (username, channel)

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")

    def test(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.test()
