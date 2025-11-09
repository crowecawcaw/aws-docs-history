# Supported software within custom test

environments

Device Farm uses host machines that are pre-installed with many of the necessary software libraries to
run test frameworks supported on our service, providing a ready testing environment on launch.
Device Farm supports multiple languages through the use of our software selection mechanism, and will
periodically update the versions of the languages included in the environment.

For any other required software, you can modify the test spec file to install from your test
package, download from the internet, or access private sources within your VPC (see [VPC
ENI](vpc-eni.md "vpc-eni.md") for more information). For more information, see [Test spec examples](custom-test-environment-test-spec.md#custom-test-environment-test-spec-example "custom-test-environment-test-spec.md#custom-test-environment-test-spec-example").

##

Pre-configured software

In order to facilitate device testing on each platform, the following tooling is provided on
the test host:

| Tools                                          | Device Platform(s) |
| ---------------------------------------------- | ------------------ |
| Android SDK Build-Tools                        | Android            |
| Android SDK Platform-Tools<br>(includes `adb`) | Android            |
| Xcode                                          | iOS                |

##

Selectable software

In addition to the pre-configured software on the host, Device Farm offers a way to
select certain versions of supported software via the `devicefarm-cli` tooling.

The following table contains the selectable software and the test hosts that contain them.

| Software / Tool | Hosts that support this software | Command to use in your test spec |
| --------------- | -------------------------------- | -------------------------------- |
| Java 17         | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use java 17`     |
| Java 11         | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use java 11`     |
| Java 8          | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use java 8`      |
| Node.js 20      | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use node 20`     |
| Node.js 18      | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use node 18`     |
| Node.js 16      | amazon_linux_2                   | `devicefarm-cli use node 16`     |
| Python 3.11     | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use python 3.11` |
| Python 3.10     | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use python 3.10` |
| Python 3.9      | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use python 3.9`  |
| Python 3.8      | amazon_linux_2                   | `devicefarm-cli use python 3.8`  |
| Ruby 3.2        | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use ruby 3.2`    |
| Ruby 2.7        | amazon_linux_2                   | `devicefarm-cli use ruby 2.7`    |
| Appium 2        | amazon_linux_2<br>macos_sequoia  | `devicefarm-cli use appium 2`    |
| Appium 1        | amazon_linux_2                   | `devicefarm-cli use appium 1`    |
| Xcode 26        | macos_sequoia                    | `devicefarm-cli use xcode 26`    |
| Xcode 16        | macos_sequoia                    | `devicefarm-cli use xcode 16`    |

The test host also includes commonly used supporting tools for each software version, such
as the `pip` and `npm` package managers (included with Python and
Node.js respectively) and dependencies (such as the Appium UIAutomator2 Driver) for tools like
Appium. This ensures you have the tools needed to work with the supported test frameworks.
