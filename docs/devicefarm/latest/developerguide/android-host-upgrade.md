

# Upgrading to the latest Android test host
<a name="android-host-upgrade"></a>

For the full list of available test hosts and how to select one, see [Hosts for custom test environments](custom-test-environments-hosts.md).

Device Farm periodically adds a new Android test host to support newer Android versions and software, and ends support for older test hosts over time. You select the test host with the `android_test_host` field of your test spec file. To upgrade, set the field to the new test host and review the differences listed for that upgrade.

To avoid updating the field each time Device Farm adds a test host, set `android_test_host: default` instead. Device Farm then selects a test host that is compatible with the Android version of the device under test, and routes tests on future Android versions to a supported test host. If your tests require a specific software version, we recommend that you select the test host explicitly, because a newer test host might not offer an older version. With either selection type, select software versions explicitly with [`devicefarm-cli`](custom-test-environments-hosts-software-cli.md) so that a change in default versions doesn't affect your tests. For the mapping of Android versions to test hosts, see [Let Device Farm choose](custom-test-environments-hosts.md#select-default-test-host).

**Topics**
+ [Upgrading from Amazon Linux 2 to Amazon Linux 2023](#android-host-al2-al2023-upgrade)

## Upgrading from Amazon Linux 2 to Amazon Linux 2023
<a name="android-host-al2-al2023-upgrade"></a>

To upgrade existing Android tests from the `amazon_linux_2` (Amazon Linux 2) test host to the recommended `amazon_linux_2023` (Amazon Linux 2023) test host, set `android_test_host: amazon_linux_2023` in your test spec file. The upgrade changes the following:
+ **Supported devices** – Each test host supports a different range of Android versions. For the devices that each test host supports, see [Available test hosts for custom test environments](custom-test-environments-hosts.md#custom-test-environments-hosts-available).
+ **App re-signing** – By default, Device Farm installs your Android app and test package as you uploaded them, instead of re-signing them. For more information, see [Re-signing apps](apps.md#test-runs-app-resigning).
+ **VPC endpoint connectivity** – The `amazon_linux_2023` test host doesn't support VPC endpoint (VPCE) connectivity. If your tests reach private resources through VPCE, switch to VPC-ENI before you change test hosts. For more information, see [VPC-ENI in AWS Device Farm](vpc-eni.md).
+ **ADB** – The `amazon_linux_2023` test host provides a newer release of the Android SDK Platform-Tools, with `adb` version 1.0.41. The `amazon_linux_2` test host provides `adb` version 1.0.39. To print the `adb` version that your test run uses, add `adb version` to a phase of your test spec file. If your tests depend on the behavior of a specific `adb` version, verify them on the `amazon_linux_2023` test host.
+ **Selectable software** – The `amazon_linux_2023` test host offers newer versions of Java, Node.js, and Python, but not every older version that the `amazon_linux_2` test host offers, such as Appium 1. For the versions on each test host, see [Supported software within custom test environments](custom-test-environments-hosts-software.md).

For more information about Amazon Linux 2023, see [What is Amazon Linux 2023?](https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html) and [Comparing AL2 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) in the *Amazon Linux 2023 User Guide*.