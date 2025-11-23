# Environment variables for custom test

environments

Device Farm dynamically configures several environment variables for use as part of your custom
test environment run.

###### Topics

- [Custom environment variables](#custom-test-environment-variables-custom "#custom-test-environment-variables-custom")
- [Common environment variables](#custom-test-environment-variables-common "#custom-test-environment-variables-common")
- [Environment variables for Appium
  tests](#custom-test-environment-variables-appium "#custom-test-environment-variables-appium")
- [Environment variables for
  XCUITest tests](#custom-test-environment-variables-xcuitest "#custom-test-environment-variables-xcuitest")

## Custom environment variables

Device Farm supports the configuration of key-value pairs that are applied as environment variables on the test host. These may be configured on a Device Farm project or during run creation;
any variables configured on a run will supersede any that may be configured on its parent project.
The following restrictions apply:

- Custom environment variables are not supported on legacy iOS test hosts. For more information, see [Legacy iOS test host](custom-test-environments-hosts-ios.md#legacy-ios-host "custom-test-environments-hosts-ios.md#legacy-ios-host").
- Variable names beginning with `$DEVICEFARM_` are reserved for internal service use.
- Custom environment variables may not be used to configure test host compute selection in your test spec.

## Common environment variables

This section describes environment variables common to all tests in Device Farm.

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

**`$DEVICEFARM_PROJECT_ARN`**

The ARN of the job's parent project.

**`$DEVICEFARM_RUN_ARN`**

The ARN of the job's parent run.

**`$DEVICEFARM_DEVICE_ARN`**

The ARN of the device under test.

**`$DEVICEFARM_TOTAL_JOBS`**

The total number of jobs associated with its parent Device Farm run.

**`$DEVICEFARM_JOB_NUMBER`**

This job's number within `$DEVICEFARM_TOTAL_JOBS`. For example, a run may contain 5 jobs, and each will have a unique `$DEVICEFARM_JOB_NUMBER` ranging from 0 to 4.

**`$AWS_REGION`**

The AWS region. The service will set this to match the region in which the device under test is located. It can be overridden by a custom environment variable if needed.

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
