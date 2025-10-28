# Prerequisites

Before you set up the C++ producer SDK, ensure that you have the following prerequisites:

- **Credentials:** In the sample code, you
  provide credentials by specifying a profile that you set up in your AWS
  credentials profile file. If you haven't already done so, first set up your
  credentials profile.

For more information, see [Set up AWS Credentials and Region for Development](../../../sdk-for-java/v1/developer-guide/setup-credentials.md "../../../sdk-for-java/v1/developer-guide/setup-credentials.md").

- **Certificate store integration:** The Kinesis Video Streams
  producer library must establish trust with the service it calls. This is
  done through validating the certificate authorities (CAs) in the public
  certificate store. On Linux-based models, this store is located in the
  `/etc/ssl`/ directory.

Download the certificate from the following location to your certificate
store:

[https://www.amazontrust.com/repository/SFSRootCAG2.pem](https://www.amazontrust.com/repository/SFSRootCAG2.pem "https://www.amazontrust.com/repository/SFSRootCAG2.pem")

- Install the following build dependencies for macOS:
  - [Autoconf 2.69](http://www.gnu.org/software/autoconf/autoconf.html "http://www.gnu.org/software/autoconf/autoconf.html") (License GPLv3+/Autoconf: GNU GPL version
    3 or later)
  - [CMake 3.7 or 3.8](https://cmake.org/ "https://cmake.org/")
  - [Pkg-Config](https://www.freedesktop.org/wiki/Software/pkg-config/ "https://www.freedesktop.org/wiki/Software/pkg-config/")
  - xCode (macOS) / clang / gcc (xcode-select version 2347)
  - Java Development Kit (JDK) (for Java JNI compilation)
  - [Lib-Pkg](https://github.com/freebsd/pkg/tree/master/libpkg "https://github.com/freebsd/pkg/tree/master/libpkg")

- Install the following build dependencies for Ubuntu:
  - Git: `sudo apt install git`
  - [CMake](http://kitware.com/cmake "http://kitware.com/cmake"): `sudo
apt install cmake`
  - G++: `sudo apt install g++`
  - pkg-config: `sudo apt install pkg-config`
  - OpenJDK: `sudo apt install openjdk-8-jdk`

  ###### Note

  This is only required if you’re building Java Native Interface (JNI).
  - Set the `JAVA_HOME` environment variable: `export
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/`
