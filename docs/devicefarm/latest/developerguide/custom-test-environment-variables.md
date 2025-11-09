# Environment variables for custom test

environments

Device Farm dynamically configures several environment variables for use as part of your custom
test environment run.

###### Topics

- [Common environment variables](#custom-test-environment-variables-common "#custom-test-environment-variables-common")
- [Environment variables for Appium
  tests](#custom-test-environment-variables-appium "#custom-test-environment-variables-appium")
- [Environment variables for
  XCUITest tests](#custom-test-environment-variables-xcuitest "#custom-test-environment-variables-xcuitest")

## Common environment variables

This section describes custom environment variables common to all tests in Device Farm.

**`$DEVICEFARM_DEVICE_NAME`**

The device on which your tests run. It represents the unique device identifier (UDID) of
the device.

**`$DEVICEFARM_DEVICE_UDID`**

The device's unique identifier.

**`$DEVICEFARM_DEVICE_PLATFORM_NAME`**

The device's platform name. It is either `Android` or `iOS`.

**`$DEVICEFARM_DEVICE_OS_VERSION`**

The device's OS version.

**`$DEVICEFARM_APP_PATH`**

_(mobile app tests)_

The path to the mobile app on the host machine where the tests are being executed. This
variable is not available during web tests.

**`$DEVICEFARM_LOG_DIR`**

The path to the default directory where customer logs, artifacts, and other wanted
files will be stored for later retrieval. Using an [example test spec](custom-test-environment-test-spec.md#custom-test-environment-test-spec-example "custom-test-environment-test-spec.md#custom-test-environment-test-spec-example"), files in
this directory are archived in a ZIP file and made available as an artifact after your
test run.

**`$DEVICEFARM_SCREENSHOT_PATH`**

The path to the screenshots, if any, captured during the test run.

**`$ANDROID_HOME`**

_(Android only)_

The path to the Android SDK installation directory.

## Environment variables for Appium

tests

This section describes environment variables used by any Appium test in a custom test
environment in Device Farm.

**`$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR`**

_(Android only)_

The location of a directory which contains the necessary ChromeDriver executables for
use
in Appium web and hybrid tests.

**`$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>`**

_(iOS only)_

The derived data path of a version of WebDriverAgent built to run on Device Farm. The
numbering on the variable will correspond to the major version of the WebDriverAgent. As
an example, `DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V9` will point to the a
WebDriverAgent version of 9.x. For more information, see [Selecting a WebDriverAgent version for iOS tests](test-types-appium.md#test-types-appium-select-wda "test-types-appium.md#test-types-appium-select-wda").

###### Note

The `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>` environment
variables are only present on non-legacy iOS hosts. For more information, see [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host").

**`$DEVICEFARM_WDA_DERIVED_DATA_PATH_V9`**

_(iOS only, deprecated)_

The derived data path of a version of WebDriverAgent built to run on Device Farm.
Refer to `$DEVICEFARM_APPIUM_WDA_DERIVED_DATA_PATH_V<N>` for the
replacement naming scheme.

## Environment variables for

XCUITest tests

This section describes environment variables used by the XCUITest test in a custom test
environment in Device Farm.

**`$DEVICEFARM_XCUITESTRUN_FILE`**

The path to the Device Farm `.xctestun` file. It is generated from your app
and test packages.

**`$DEVICEFARM_DERIVED_DATA_PATH`**

Expected path of Device Farm xcodebuild output.

**`$DEVICEFARM_XCTEST_BUILD_DIRECTORY`**

The path to the unzipped contents of the test package file.
