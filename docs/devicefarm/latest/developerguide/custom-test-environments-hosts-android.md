

# Test environment for Android devices
<a name="custom-test-environments-hosts-android"></a>

For the full list of available test hosts and how to select one, see [Hosts for custom test environments](custom-test-environments-hosts.md). 

AWS Device Farm utilizes Amazon Elastic Compute Cloud (EC2) host machines running Amazon Linux to execute Android tests. When you schedule a test run, Device Farm allocates a dedicated host for each device to independently run tests. The host machines terminate after the test run along with any generated artifacts. 

For Android devices, use the `android_test_host` field of your test spec file to select the `amazon_linux_2023` or `amazon_linux_2` test host, or `default`. The field is required for Android test runs. The recommended test host is `amazon_linux_2023`. To upgrade existing tests, see [Upgrading to the latest Android test host](android-host-upgrade.md).

**Topics**
+ [Supported software for Android devices](#android-host-software-support)
+ [Upgrading to the latest Android test host](android-host-upgrade.md)

## Supported software for Android devices
<a name="android-host-software-support"></a>

To support Android device testing, Device Farm test hosts for Android devices come pre-configured with the Android SDK Build-Tools and Platform-Tools, which include the Android Debug Bridge (`adb`). For other available software, see [Supported software within custom test environments](custom-test-environments-hosts-software.md).