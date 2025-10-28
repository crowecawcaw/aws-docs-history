# Common environment variables in Device Farm

This section describes environment variables that are common to Android platform tests and to iOS
platform tests in AWS Device Farm. For more information about environment variables in Device Farm, see [Environment variables in Device Farm](custom-test-environment-variables.md "custom-test-environment-variables.md").

## Android tests

This section describes custom environment variables common to Android platform tests supported by
Device Farm.

**`$DEVICEFARM_DEVICE_NAME`**

Name of the device on which your tests run. It represents the unique device identifer
(UDID) of the device.

**`$DEVICEFARM_DEVICE_PLATFORM_NAME`**

The device platform name. It is either Android or iOS.

**`$DEVICEFARM_DEVICE_OS_VERSION`**

The device OS version.

**`$DEVICEFARM_APP_PATH`**

The path to the mobile app on the host machine where the tests are being executed. The
app path is available for mobile apps only.

**`$DEVICEFARM_DEVICE_UDID`**

The unique identifier of the mobile device running the automated test.

**`$DEVICEFARM_LOG_DIR`**

The path to the log files generated during the test run. By default, all files in this
directory are archived in a ZIP file and made available as an artifact after your test
run.

**`$DEVICEFARM_SCREENSHOT_PATH`**

The path to the screenshots, if any, captured during the test run.

**`$DEVICEFARM_CHROMEDRIVER_EXECUTABLE_DIR`**

The location of a directory which contains the necessary Chromedriver executables for
use in Appium web and hybrid tests.

**`$ANDROID_HOME`**

The path to the Android SDK installation directory.

###### Note

The `ANDROID_HOME` environment variable is only available on the Amazon
Linux 2 test host for Android.

## iOS tests

This section describes custom environment variables common to iOS platform tests supported by
Device Farm.

**`$DEVICEFARM_DEVICE_NAME`**

Name of the device on which your tests run. It represents the unique device identifer
(UDID) of the device.

**`$DEVICEFARM_DEVICE_PLATFORM_NAME`**

The device platform name. It is either Android or iOS.

**`$DEVICEFARM_APP_PATH`**

The path to the mobile app on the host machine where the tests are being executed. The
app path is available for mobile apps only.

**`$DEVICEFARM_DEVICE_UDID`**

The unique identifier of the mobile device running the automated test.

**`$DEVICEFARM_LOG_DIR`**

The path to the log files generated during the test run.

**`$DEVICEFARM_SCREENSHOT_PATH`**

The path to the screenshots, if any, captured during the test run.
