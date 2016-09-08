from conans import ConanFile, CMake

class HelloConan(ConanFile):
    name = "libfixmath"
    version = "20141230"
    url = "https://github.com/sunsided/libfixmath.git"
    license = "MIT"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {"sin_lut": [True, False], "trig_cache": [True, False]}
    default_options = "sin_lut=False", "trig_cache=False"
    exports = "libfixmath/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self.settings)
        sin_lut_definition    = "-DFIXMATH_SIN_LUT=1"  if     self.options.sin_lut else ""
        trig_cache_definition = "-DFIXMATH_NO_CACHE=1" if not self.options.sin_lut else ""

        self.run('cmake %s %s %s %s' % (self.conanfile_directory, cmake.command_line, sin_lut_definition, trig_cache_definition))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="libfixmath")
        self.copy("*.hpp", dst="include", src="libfixmath")
        self.copy("*.c", dst="src", src="libfixmath")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["libfixmath"]