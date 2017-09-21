"""Conan.io recipe for pcap library
"""
import os
from conans import ConanFile, tools


class winpcapConan(ConanFile):
    """Donwload pcap library, build and create package
    """
    name = "winpcap"
    version = "4.1.2"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    url = "http://github.com/uilianries/conan-winpcap"
    author = "Uilian Ries <uilianries@gmail.com>"
    description = "The WinPcap packet capture library."
    license = "https://github.com/the-tcpdump-group/winpcap/blob/master/LICENSE"
    exports = "LICENSE"

    def source(self):
        tools.get("https://www.winpcap.org/install/bin/WpdPack_4_1_2.zip")

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("WinPcap is only supported for Windows.")

    def package(self):
        self.copy("LICENSE", src=".", dst=".")
        self.copy(pattern="*.h", dst="include", src=os.path.join("WpdPack", "Include"))
        if self.settings.arch == "x86_64":
            self.copy(pattern="*.dll", dst="bin", src=os.path.join("WpdPack", "Lib", "x64"), keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=os.path.join("WpdPack", "Lib", "x64"), keep_path=False)
        else:
            self.copy(pattern="wpcap.dll", dst="bin", src=os.path.join("WpdPack", "Lib"), keep_path=False)
            self.copy(pattern="Packet.dll", dst="bin", src=os.path.join("WpdPack", "Lib"), keep_path=False)
            self.copy(pattern="wpcap.lib", dst="lib", src=os.path.join("WpdPack", "Lib"), keep_path=False)
            self.copy(pattern="Packet.lib", dst="lib", src=os.path.join("WpdPack", "Lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
