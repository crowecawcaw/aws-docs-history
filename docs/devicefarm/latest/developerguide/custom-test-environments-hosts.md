# Hosts for custom test environments

Device Farm supports a set of operating systems with pre-configured software through the use of a test
host environment. During test execution, Device Farm utilizes Amazon-managed instances (hosts)
that dynamically connect to the selected device under test. This instance is fully cleaned up
and not re-used between runs, and is terminated with its generated artifacts after the test run
concludes.

###### Topics

- [Available test hosts for custom
  test environments](#custom-test-environments-hosts-available "#custom-test-environments-hosts-available")
- [Selecting a test host for custom test environments](#test-host-selection "#test-host-selection")
- [Supported software within custom test
  environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md")
- [Test environment for Android devices](custom-test-environments-hosts-android.md "custom-test-environments-hosts-android.md")
- [Test environment for iOS devices](custom-test-environments-hosts-ios.md "custom-test-environments-hosts-ios.md")

## Available test hosts for custom

test environments

The test hosts are fully managed by Device Farm. The following table lists the currently available
and supported Device Farm test hosts for custom test environments.

| Device Platform | Test Host      | Operating System           | Architecture(s) | Supported Devices   |
| --------------- | -------------- | -------------------------- | --------------- | ------------------- |
| Android         | amazon_linux_2 | Amazon Linux 2             | x86_64          | Android 6 and above |
| iOS             | macos_sequoia  | macOS Sequoia (version 15) | arm64           | iOS 15 to 26        |

###### Note

Periodically, Device Farm adds new test hosts for a device platform to support newer device OS
versions and its dependencies. When this occurs, older test hosts for the respective
device platform are subject to end of support.

### Operating system version

Each available test host uses a specific version of the operating system supported on Device Farm
at the time. Although we try to be on the latest OS version, this may might not be the
latest publicly distributed version available. Device Farm will periodically update the operating
system with minor version updates and security patches.

To know the specific version (including the minor version) of the operating system in use
during your test run, you can add the following snippet of code to any of your test spec
file's phases.

###### Example

```
phases:
  install:
    commands:
      # The following example prints the instance's operating system version details
      - |-
        if [[ "Darwin" == "$(uname)" ]]; then
          echo "$(sw_vers --productName) $(sw_vers --productVersion) ($(sw_vers --buildVersion))";
        else
          echo "$(. /etc/os-release && echo $PRETTY_NAME) ($(uname -r))";
        fi
```

##

Selecting a test host for custom test environments

You can specify the Android and iOS test host in the appropriate `android_test_host`
and `ios_test_host` variables of your [test spec file](custom-test-environment-test-spec.md#custom-test-environment-test-spec-syntax "custom-test-environment-test-spec.md#custom-test-environment-test-spec-syntax").

If you do not specify a test host selection for the given device platform, tests will run on
the test host that Device Farm has set as the default for the specified device and test
configuration.

###### Important

When testing on iOS 18 and below, a legacy test host will be used when a host is not
selected. For more information, see the topic on the [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host").

As an example, review the following code snippet:

###### Example

```
version: 0.1
android_test_host: `amazon_linux_2`
ios_test_host: `macos_sequoia`

phases:
  # ...
```
