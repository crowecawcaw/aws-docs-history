

# Hosts for custom test environments
<a name="custom-test-environments-hosts"></a>

 Device Farm supports a set of operating systems with pre-configured software through the use of a test host environment. During test execution, Device Farm utilizes Amazon-managed instances (hosts) that dynamically connect to the selected device under test. This instance is fully cleaned up and not re-used between runs, and is terminated with its generated artifacts after the test run concludes. 

**Topics**
+ [Available test hosts for custom test environments](#custom-test-environments-hosts-available)
+ [Selecting a test host for custom test environments](#test-host-selection)
+ [Operating system version](#test-host-os)
+ [Supported software within custom test environments](custom-test-environments-hosts-software.md)
+ [Test environment for Android devices](custom-test-environments-hosts-android.md)
+ [Test environment for iOS devices](custom-test-environments-hosts-ios.md)

## Available test hosts for custom test environments
<a name="custom-test-environments-hosts-available"></a>

 The test hosts are fully managed by Device Farm. The following table lists the currently available and supported Device Farm test hosts for custom test environments. 


| Device Platform | Test Host | Operating System | Architecture(s) | Supported Devices | 
| --- | --- | --- | --- | --- | 
|  Android  |  amazon\_linux\_2  |  Amazon Linux 2  |  x86\_64  | Android 6 and above | 
|  iOS  |  macos\_tahoe  | macOS Tahoe (version 26) |  arm64  | iOS 17 to 27 | 
|  iOS  |  macos\_sequoia  | macOS Sequoia (version 15) |  arm64  | iOS 15 to 26 | 

**Note**  
Periodically, Device Farm adds new test hosts for a device platform to support newer device OS versions and its dependencies. When this occurs, older test hosts for the respective device platform are subject to end of support.

## Selecting a test host for custom test environments
<a name="test-host-selection"></a>

To select your desired test host, specify the Android and iOS test host in the appropriate `android_test_host` and `ios_test_host` variables of your [test spec file](custom-test-environment-test-spec.md#custom-test-environment-test-spec-syntax).

You can select a test host in one of the following ways:

1. **Select a specific host** – You name the exact test host you want to use.

1. **Let Device Farm choose** – You set the test host to `default`, and Device Farm picks the host based on the device's OS version.

1. **Use the fallback host** – You omit the field, and Device Farm assigns a legacy test host as a fallback. ***This option is not recommended.*** For more information, see the [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host).

Managing test hosts is a shared responsibility between Device Farm and you. Your responsibilities vary depending on the selection type you choose. This is summarized in the following table for the recommended selection types.


| Selection type | Device Farm's responsibility | Customer's responsibility | 
| --- | --- | --- | 
| [Select a specific host](#select-specific-test-host) | Run your tests on the exact host you name, with a consistent set of software versions on every run. | Specify the host that provides the software versions your tests require (for example, macos\_sequoia or amazon\_linux\_2). Update your test spec to a newer host for each major device OS version, because Device Farm ends support for older hosts over time. | 
| [Let Device Farm choose](#select-default-ios-test-host) | Select a host that is compatible with the device's OS version, and route your tests on future OS versions to a supported host. | Set the test host value to `default`. If your tests require a specific software version, specify the host explicitly instead, because in rare cases an older version of a dependency might not be available on a newer host. | 

For more information about shared responsibility with AWS, see the [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) on the AWS website.

### Option 1: Select a specific host
<a name="select-specific-test-host"></a>

When you create your test spec file, provide the exact test host value in the corresponding `android_test_host` or `ios_test_host` field.

**Example**  

```
version: 0.1
android_test_host: {{amazon_linux_2}}
ios_test_host: {{macos_tahoe}}

phases:
  # ...
```

### Option 2: Let Device Farm choose
<a name="select-default-ios-test-host"></a>

You can set the test host to the value `default` to have Device Farm select a host based on the OS version of the device under test.

**Note**  
For the time being, `default` applies to `ios_test_host` only. Support for `android_test_host` is planned for a future release.

The following table shows the default host mapping by device OS version.


| Platform | Device OS version | Assigned test host | 
| --- | --- | --- | 
| iOS | 17 to 27 | macos\_tahoe | 
| iOS | 15 to 16 | macos\_sequoia | 

**Example**  

```
version: 0.1
ios_test_host: default

phases:
  # ...
```

## Operating system version
<a name="test-host-os"></a>

 Each available test host uses a specific version of the operating system supported on Device Farm at the time. Device Farm periodically updates the operating system with minor version updates and security patches. 

 You can find the exact OS version used during your test run, including the minor version. To do this, add the following snippet to any phase of your test spec file: 

**Example**  

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