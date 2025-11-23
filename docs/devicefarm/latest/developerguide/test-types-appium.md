# Automatically run Appium tests in Device Farm

###### Note

This page covers running Appium tests in Device Farm's managed **server-side** execution environment. To run Appium tests from your local **client-side** environment during a remote access session, see [client-side Appium testing](appium-endpoint.md "appium-endpoint.md").

This section describes how to configure, package, and upload your Appium tests for running
on Device Farm's managed server-side environment.
Appium is an open source tool for automating native and mobile web applications.
For more information, see [Introduction to Appium](http://appium.io/docs/en/latest/intro "http://appium.io/docs/en/latest/intro") on the Appium website.

For a sample app and links to working tests, see [Device Farm Sample App for Android](https://github.com/aws-samples/aws-device-farm-sample-app-for-android "https://github.com/aws-samples/aws-device-farm-sample-app-for-android") and [Device Farm Sample App for iOS](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios "https://github.com/aws-samples/aws-device-farm-sample-app-for-ios") on GitHub.

For more information about testing in Device Farm and how server-side works, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

## Selecting an Appium version

###### Note

Support for specific Appium versions, Appium drivers, or programming SDKs will depend on the
device and test host selected for the test run.

Device Farm test hosts come pre-installed with Appium in order to enable quicker setup of tests for
more straightforward use cases. However, the use of the test spec file allows you to install
differing versions of Appium if needed.

Device Farm comes pre-configured with different Appium server versions based on the test host.
The host comes with tooling that enables the pre-configured version with the device
platform's default driver (UiAutomator2 for Android, and XCUITest for iOS).

```
phases:
  install:
    commands:
      - export APPIUM_VERSION=`2`
      - devicefarm-cli use appium $APPIUM_VERSION
```

To view a list of supported software, see the topic on [Supported software within custom test
environments](custom-test-environments-hosts-software.md "custom-test-environments-hosts-software.md").

To select a custom version of Appium, use the `npm` command to install it.
The following example shows how to install the latest version of Appium 2.

```
phases:
  install:
    commands:
      - export APPIUM_VERSION=`2`
      - npm install -g appium@$APPIUM_VERSION
```

On the [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host"), you can
choose specific Appium versions with `avm`. For example, to use the `avm`
command to set the Appium server version to `2.1.2`, add these commands to your
test spec YAML file.

```
phases:
  install:
    commands:
      - export APPIUM_VERSION=`2.1.2`
      - avm $APPIUM_VERSION
```

## Selecting a WebDriverAgent version for iOS tests

In order to run Appium tests on iOS devices, the use of WebDriverAgent is required. This
application must be signed in order to be installed on iOS devices. Device Farm provides
pre-signed versions of WebDriverAgent that are available during custom test environment runs.

The following code snippet can be used to select a WebDriverAgent version on Device Farm within your
test spec file that is compatible with your XCTestUI Driver version..

```
phases:
  pre_test:
    commands:
      - |-
        APPIUM_DRIVER_VERSION=$(appium driver list --installed --json | jq -r ".xcuitest.version" | cut -d "." -f 1);
        CORRESPONDING_APPIUM_WDA=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V${APPIUM_DRIVER_VERSION}")
        if [[ ! -z "$APPIUM_DRIVER_VERSION" ]] && [[ ! -z "$CORRESPONDING_APPIUM_WDA" ]]; then
          echo "Using Device Farm's prebuilt WDA version ${APPIUM_DRIVER_VERSION}.x, which corresponds with your driver";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $CORRESPONDING_APPIUM_WDA | cut -d "=" -f2)
        else
          LATEST_SUPPORTED_WDA_VERSION=$(env | grep "DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V" | sort -V -r | head -n 1)
          echo "Unknown driver version $APPIUM_DRIVER_VERSION; falling back to the Device Farm default version of $LATEST_SUPPORTED_WDA_VERSION";
          DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH=$(echo $LATEST_SUPPORTED_WDA_VERSION | cut -d "=" -f2)
        fi;
```

For more information about the WebDriverAgent, see Appium's [documentation](https://appium.github.io/appium-xcuitest-driver/9.10/guides/run-prebuilt-wda/ "https://appium.github.io/appium-xcuitest-driver/9.10/guides/run-prebuilt-wda/").
