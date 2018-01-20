#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools


class winpcapConan(ConanFile):
    """Donwload pcap library, build and create package
    """
    name = "winpcap"
    version = "4.1.3"
    settings = "os", "arch", "compiler"
    url = "http://github.com/uilianries/conan-winpcap"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "The WinPcap packet capture library."
    license = "https://github.com/the-tcpdump-group/winpcap/blob/master/LICENSE"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"

    def source(self):
        url = "https://www.winpcap.org/install/bin/WpcapSrc_4_1_3.zip"
        md5 = "3a47076c5a437c023e76a58b77cfa890"
        tools.get(url=url, md5=md5)
        os.rename(self.name, self.source_subfolder)

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("WinPcap is only supported for Windows.")

    def build(self):
        os.environ["WPDPACKDESTDIR"] = self.package_folder
        self.run(os.path.join(self.source_subfolder, "create_include.bat")

    def package(self):
        self.copy("LICENSE", dst="license", src=os.path.join(self.source_subfolder, "wpcap", "libpcap"))
        os.rename(os.path.join(self.package_folder, "Include"), os.path.join(self.package_folder, "include"))
        self.copy(pattern="*.h", dst="include", src=os.path.join(self.name, "Include"))
        if self.settings.compiler == "gcc":

        else:
            if self.settings.arch == "x86_64":
                self.copy(pattern="*.dll", dst="bin", src=os.path.join(self.name, "Lib", "x64"), keep_path=False)
                self.copy(pattern="*.lib", dst="lib", src=os.path.join(self.name, "Lib", "x64"), keep_path=False)
            else:
                self.copy(pattern="wpcap.dll", dst="bin", src=os.path.join(self.name, "Lib"), keep_path=False)
                self.copy(pattern="Packet.dll", dst="bin", src=os.path.join(self.name, "Lib"), keep_path=False)
                self.copy(pattern="wpcap.lib", dst="lib", src=os.path.join(self.name, "Lib"), keep_path=False)
                self.copy(pattern="Packet.lib", dst="lib", src=os.path.join(self.name, "Lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
