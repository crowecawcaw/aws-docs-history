

# Testing on virtual devices in Device Farm

In AWS Device Farm, you can do manual and automated testing on virtual devices, which include Android emulators and iOS simulators.

Virtual devices appear with the physical devices in the public device list. A virtual device's name ends in `Emulator` or `Simulator`, and its **Device type** is **Virtual**. Virtual devices are available in several OS versions. Virtual devices that run the latest OS version are usually ready to use in less than 30 seconds. Virtual devices that run other OS versions usually start in about 1 minute. To select virtual devices, see [Supported devices](devices.md#devices-supported).
+ **Manual testing**: When you start a remote access session, the emulators and simulators appear in the same device list as the physical devices. For more information, see [Remote access](remote-access.md).
+ **Automated testing**: Virtual devices support standard and custom test environments, and the same test types as physical devices on each platform. For the list of test types, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md). In a custom test environment, set the test host and capabilities in your test spec. For more information, see [Testing on iOS simulators](custom-test-environments-hosts-ios.md#ios-simulator-testing) and [Testing on Android emulators](custom-test-environments-hosts-android.md#android-emulator-testing).

Virtual devices don't support VPC endpoint (VPCE) connectivity, and iOS simulators use only the metered billing method.