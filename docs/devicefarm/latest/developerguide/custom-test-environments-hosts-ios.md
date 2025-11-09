#

Test environment for iOS devices

Device Farm utilizes Amazon-managed macOS instances (hosts) that dynamically connect to the iOS device
during the test run. Each host is pre-configured with software that enables device testing on
various popular test platforms, such as XCTestUI and Appium.

The current iteration of the iOS test host has improved upon the testing experience when
compared to previous versions, including:

- Consistent host OS and tooling experience for iOS 15 to iOS 26

Before, the test host was determined by the device in use, leading to a fragmented software
environment when executing on multiple iOS versions. The current experience allows simple
host selection to enable a consistent environment across devices. This will enable the same
macOS version and tooling (such as Xcode) to be available across each iOS device.

- Performance improvements for iOS 15 and 16 tests Using
  updated infrastructure, setup time has improved substantially for iOS 15 and 16 tests.
- Standardized selectable software versions for supported dependencies
  We now have the `devicefarm-cli` software selection system on both iOS and Android
  test hosts, enabling you to select your preferred version of our supported dependencies. For
  supported dependencies (such as Java, Python, Node.js, Ruby, and Appium), versions will be
  selectable via the test spec. For an idea of how this feature works, please see the topic on [Supported software within custom test
  environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").

###### Important

If executing on iOS 18 and below, your tests will execute on legacy test hosts by default. See
the topic below on how to migrate away from legacy hosts.

## Legacy iOS test host

For existing tests on iOS 18 and below, the legacy test hosts are selected by default for
custom test environments. The following table contains the test host version that is executed
with by the iOS device version.

| Operating System            | Architecture(s) | Default for Devices |
| --------------------------- | --------------- | ------------------- |
| macOS Sonoma (version 14)   | arm64           | iOS 18              |
| macOS Ventura (version 13)  | arm64           | iOS 17              |
| macOS Monterey (version 12) | x86_64          | iOS 16 and below    |

In order to select the newer test hosts, see the topic regarding [Migrating your custom test environments to the new iOS test
hosts](ios-host-migration.md "ios-host-migration.md").

##

Supported software for iOS devices

In order to support iOS device testing, Device Farm test hosts for iOS devices come
pre-configured with Xcode and its associated command line tooling. For other available
software, please review the topic regarding [Supported software within custom test
environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").
