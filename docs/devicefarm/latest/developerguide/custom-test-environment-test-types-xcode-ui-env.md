# XCUITest environment variables in

Device Farm

This section describes environment variables used by the XCUITest test in a custom test environment in
Device Farm. For more information about environment variables in Device Farm, see [Environment variables in Device Farm](custom-test-environment-variables.md "custom-test-environment-variables.md").

**`$DEVICEFARM_XCUITESTRUN_FILE`**

Path to the Device Farm `.xctestun` file. It is generated from your app and test
packages.

**`$DEVICEFARM_DERIVED_DATA_PATH`**

Expected path of Device Farm xcodebuild output.

**`$DEVICEFARM_XCTEST_BUILD_DIRECTORY`**

The path to the unzipped contents of the test package file.
