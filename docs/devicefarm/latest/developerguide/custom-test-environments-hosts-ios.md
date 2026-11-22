

# Test environment for iOS devices

 For the full list of available test hosts and how to select one, see [Hosts for custom test environments](custom-test-environments-hosts.md). 

 Device Farm utilizes Amazon-managed macOS instances (hosts) that dynamically connect to the iOS device during the test run. Each host is pre-configured with software that enables device testing on various popular test platforms, such as XCTestUI and Appium. 

 The current iteration of the iOS test host has improved upon the testing experience when compared to previous versions, including: 
+  ** Consistent host OS and tooling experience for iOS 15 and greater ** Before, the test host was determined by the device in use, leading to a fragmented software environment when executing on multiple iOS versions. The current experience allows simple host selection to enable a consistent environment across devices. This will enable the same macOS version and tooling (such as Xcode) to be available across each iOS device. 
+  ** Performance improvements ** Using updated infrastructure, test setup time has improved substantially.
+  ** Standardized selectable software versions for supported dependencies ** We now have the `devicefarm-cli` software selection system on both iOS and Android test hosts, enabling you to select your preferred version of our supported dependencies. For supported dependencies (such as Java, Python, Node.js, Ruby, and Appium), versions will be selectable via the test spec. For an idea of how this feature works, please see the topic on [Supported software within custom test environments](custom-test-environments-hosts-software.md).

**Warning**  
 If you test on iOS 18 or below and don't explicitly select a test host, Device Farm runs your tests on a legacy test host as a fallback. Legacy test hosts are not recommended. To move to a supported test host, see [Migrating your custom test environments to the new iOS test hosts](ios-host-migration.md). 

## Legacy iOS test host
<a name="legacy-ios-host"></a>

 For existing tests on iOS 18 and below, Device Farm uses a legacy test host as a fallback when you don't explicitly select a test host for custom test environments. Legacy test hosts are not recommended. We recommend that you select a test host explicitly, or set `ios_test_host` to `default`. Legacy test hosts are not available for iOS 26 and greater; those versions require a supported test host. The following table contains the test host version that is used for each iOS device version. 


| Operating System | Architecture(s) | Default for Devices | 
| --- | --- | --- | 
|  macOS Sonoma (version 14)  |  arm64  |  iOS 18  | 
|  macOS Ventura (version 13) |  arm64  |  iOS 17  | 
|  macOS Monterey (version 12) |  x86\_64  |  iOS 16 and below | 

 In order to select the newer test hosts, see the topic regarding [Migrating your custom test environments to the new iOS test hosts](ios-host-migration.md). 

## Supported software for iOS devices
<a name="ios-host-software-support"></a>

 In order to support iOS device testing, Device Farm test hosts for iOS devices come pre-configured with Xcode and its associated command line tooling. For other available software, please review the topic regarding [Supported software within custom test environments](custom-test-environments-hosts-software.md). 

## Testing on iOS simulators
<a name="ios-simulator-testing"></a>

 iOS simulators on Device Farm run only on the `macos_tahoe` test host. To run on simulators, set `ios_test_host` to `macos_tahoe`. 

### Required Appium capabilities for simulators
<a name="ios-simulator-appium-capabilities"></a>

 For an Appium test run on a simulator, set the `appium:isHeadless` capability to `true`. Without it, session creation fails with the error `Simulator.app does not exist`. 

 You can keep `appium:isHeadless` set to `true` in a test spec that also runs on physical iOS devices. 

 Set the WebDriverAgent capabilities as you do for physical iOS devices. To resolve `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH`, see [Selecting a WebDriverAgent version for iOS tests](test-types-appium.md#test-types-appium-select-wda). 

 The following YAML test spec example sets the Appium default capabilities, including `appium:isHeadless`, for a simulator test run: 

```yaml
phases:
  pre_test:
    commands:
      - |-
        appium --base-path=$APPIUM_BASE_PATH --default-capabilities \
          "{\"appium:udid\": \"$DEVICEFARM_DEVICE_UDID\", \
          \"appium:usePrebuiltWDA\": true, \
          \"appium:derivedDataPath\": \"$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH\", \
          \"appium:isHeadless\": true, \
          \"appium:automationName\": \"XCUITest\"}"
```