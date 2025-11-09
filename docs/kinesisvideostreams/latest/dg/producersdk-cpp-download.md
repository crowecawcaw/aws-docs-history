# Download and configure the C++ producer

library code

For information about how to download and configure the C++ producer library, see [Amazon Kinesis Video Streams CPP Producer, GStreamer Plugin and JNI](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp").

For prerequisites and more information about this example, see [Use the C++ producer library](producer-sdk-cpp.md "producer-sdk-cpp.md").

## CMake arguments

Below is a reference table for the C++ Producer SDK-specific CMake arguments. You can also pass the [standard CMake options](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html "https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html") to CMake as well.

###### Important

These are all optional.

**Flags for including or excluding certain
features**

| CMake argument            | Type    | Default              | Explanation                                                                                                                                                                                                                                                       |
| ------------------------- | ------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BUILD_DEPENDENCIES`      | Boolean | ON                   | Build dependencies from source. Otherwise, use the dependencies<br>that are already installed on the system. If the one of the required<br>dependencies couldn't be found, an error will be returned.                                                             |
| `BUILD_GSTREAMER_PLUGIN`  | Boolean | OFF                  | Builds the `kvssink` GStreamer plugin.                                                                                                                                                                                                                            |
| `BUILD_JNI`               | Boolean | OFF                  | Builds the Java Native Interface (JNI) to be able to call this<br>code from a Java runtime environment.                                                                                                                                                           |
| `ALIGNED_MEMORY_MODEL`    | Boolean | OFF                  | If memory allocations should be aligned to 8-byte boundaries.<br>Some architectures don't allow for unaligned memory access.                                                                                                                                      |
| `CONSTRAINED_DEVICE`      | Boolean | OFF                  | \*_Non-Windows only._<br>• When ON, sets<br>the thread stack size to `0.5 MiB`. Needed for [Alpine Linux](https://wiki.alpinelinux.org/wiki/Main_Page "https://wiki.alpinelinux.org/wiki/Main_Page") builds. Otherwise, the operating system default is<br>used.  |
| `BUILD_STATIC`            | Boolean | OFF                  | Build libraries and executables as [shared](https://en.wikipedia.org/wiki/Shared_library "https://en.wikipedia.org/wiki/Shared_library") (OFF), or [static](https://en.wikipedia.org/wiki/Static_library "https://en.wikipedia.org/wiki/Static_library")<br>(ON). |
| `ADD_MUCLIBC`             | Boolean | OFF                  | Link to [uClibc](https://en.wikipedia.org/wiki/UClibc "https://en.wikipedia.org/wiki/UClibc") instead of the standard C library, which is a<br>smaller C standard library designed for embedded systems.                                                          |
| `OPEN_SRC_INSTALL_PREFIX` | String  | ../open-source/local | Location to install the open-source dependencies, if building<br>from source.                                                                                                                                                                                     |

**Flags for cross-compilation**

###### Important

Set these if your target and host machine CPU architectures are different.

| CMake argument           | Type   | Default | Explanation                                                                                                                                                      |
| ------------------------ | ------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BUILD_LOG4CPLUS_HOST`   | String | ""      | Build the `log4cplus` dependency for the specified CPU<br>architecture. If not set, `log4cplus` will auto-detect<br>and use the host machine's CPU architecture. |
| `BUILD_OPENSSL_PLATFORM` | String | ""      | Build the `OpenSSL` dependency for the specified CPU<br>architecture. If not set, `OpenSSL` will auto-detect and<br>use the host machine's CPU architecture.     |

**Flags related to testing**

| CMake argument                 | Type    | Default | Explanation                                                                                                                                                                                                |
| ------------------------------ | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BUILD_TEST`                   | Boolean | OFF     | Build the unit and integration tests. To run all the tests, run<br>`./tst/producerTest` from the build directory. AWS<br>Credentials are needed to run the tests.                                          |
| `CODE_COVERAGE`                | Boolean | OFF     | Only available for GNU/Clang compilers. Enable code coverage<br>collection with [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html "https://gcc.gnu.org/onlinedocs/gcc/Gcov.html") and report generation. |
| `COMPILER_WARNINGS`            | Boolean | OFF     | Only available for GNU/Clang compilers. Enable all compiler<br>warnings.                                                                                                                                   |
| `ADDRESS_SANITIZER`            | Boolean | OFF     | Only available for GNU/Clang compilers. Build with<br>[AddressSanitizer](https://compiler-rt.llvm.org/ "https://compiler-rt.llvm.org/").                                                                   |
| `MEMORY_SANITIZER`             | Boolean | OFF     | Only available for GNU/Clang compilers. Build with<br>[MemorySanitizer](https://compiler-rt.llvm.org/ "https://compiler-rt.llvm.org/").                                                                    |
| `THREAD_SANITIZER`             | Boolean | OFF     | Only available for GNU/Clang compilers. Build with<br>[ThreadSanitizer](https://compiler-rt.llvm.org/ "https://compiler-rt.llvm.org/").                                                                    |
| `UNDEFINED_BEHAVIOR_SANITIZER` | Boolean | OFF     | Only available for GNU/Clang compilers. Build with<br>[UndefinedBehaviorSanitizer](https://compiler-rt.llvm.org/ "https://compiler-rt.llvm.org/").                                                         |

To use these CMake arguments, pass them as a space-separated list of
`-D`key`=`value`` pairs following the`cmake ..` command. For example:

```
cmake .. -DBUILD_GSTREAMER_PLUGIN=ON -DBUILD_DEPENDENCIES=OFF -DALIGNED_MEMORY_MODEL=ON
```

CMake will look for the compiler toolchain by following the `$PATH`
variable. Before running CMake, set the `CC` and `CXX`
environment variables to explicitly set the toolchain to use for cross
compiling.
