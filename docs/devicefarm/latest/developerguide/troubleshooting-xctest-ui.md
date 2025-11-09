# Troubleshooting XCTest UI tests in AWS Device Farm

The following topic lists error messages that occur during the upload of XCTest UI
tests and recommends workarounds to resolve each error.

###### Note

The instructions below are based on Linux x86_64 and Mac.

## XCTEST_UI_TEST_PACKAGE_UNZIP_FAILED

If you see the following message, follow these steps to fix the issue.

`We could not open your test IPA file. Please verify that the file is valid and try again.`

Make sure that you can unzip the application package without errors. In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

A valid iOS application package should produce output like the following:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- Info.plist
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the Payload directory inside your test package. Please unzip your test package, 
 verify that the Payload directory is inside the package, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find the `Payload` directory inside
the working directory.

```
.
`-- `Payload` (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- Info.plist
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_APP_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the .app directory inside the Payload directory. Please unzip
 your test package and then open the Payload directory, verify that the .app directory is
 inside the directory, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find an `.app`
directory like `swift-sampleUITests-Runner.app` in our example inside the
`Payload` directory.

```
.
`-- Payload (directory)
        `-- `swift-sampleUITests-Runner.app` (directory)
                      |-- Info.plist
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PLUGINS_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the Plugins directory inside the .app directory. Please unzip
 your test package and then open the .app directory, verify that the Plugins directory is
 inside the directory, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find the `Plugins`
directory inside an `.app` directory. In our example, the
directory is called `swift-sampleUITests-Runner.app`.

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- Info.plist
                      |-- `Plugins` (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_XCTEST_DIR_MISSING_IN_PLUGINS_DIR

If you see the following message, follow these steps to fix the issue.

`We could not find the .xctest directory inside the plugins directory. Please
 unzip your test package and then open the plugins directory, verify that the .xctest directory
 is inside the directory, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find an `.xctest`
directory inside the `Plugins` directory. In our example, the
directory is called `swift-sampleUITests.xctest`.

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- Info.plist
                      |-- Plugins (directory)
                      |       ``swift-sampleUITests.xctest` (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .app directory. Please unzip
 your test package and then open the .app directory, verify that the Info.plist file is inside
 the directory, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find the
`Info.plist` file inside
the `.app` directory. In our example below, the directory is
called `swift-sampleUITests-Runner.app`.

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PLIST_FILE_MISSING_IN_XCTEST_DIR

If you see the following message, follow these steps to fix the issue.

`We could not find the Info.plist file inside the .xctest directory. Please unzip
 your test package and then open the .xctest directory, verify that the Info.plist file is
 inside the directory, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you will find the
`Info.plist` file inside
the `.xctest` directory. In our example below, the directory is
called `swift-sampleUITests.xctest`.

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- Info.plist
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- `Info.plist`
                      |                       `-- (any other files)
                      `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_CPU_ARCHITECTURE_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not the CPU architecture value in the Info.plist file. Please unzip your
 test package and then open the Info.plist file inside the .app directory, verify that the key
 "UIRequiredDeviceCapabilities" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the CPU architecture value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['UIRequiredDeviceCapabilities']
```

A valid XCtest UI package should produce output like the following:

```
['armv7']
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PLATFORM_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the platform value in the Info.plist. Please unzip your test
 package and then open the Info.plist file inside the .app directory, verify that the key
 "CFBundleSupportedPlatforms" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the platform value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['CFBundleSupportedPlatforms']
```

A valid XCtest UI package should produce output like the following:

```
['iPhoneOS']
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_WRONG_PLATFORM_DEVICE_VALUE

If you see the following message, follow these steps to fix the issue.

`We found the platform device value was wrong in the Info.plist file. Please unzip
 your test package and then open the Info.plist file inside the .app directory, verify that the
 value of the key "CFBundleSupportedPlatforms" does not contain the keyword "simulator", and
 try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the platform value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['CFBundleSupportedPlatforms']
```

A valid XCtest UI package should produce output like the following:

```
['iPhoneOS']
```

If the XCTest UI package is valid, the value should not contain the keyword `simulator`.

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_FORM_FACTOR_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not the form factor value in the Info.plist. Please unzip your test
 package and then open the Info.plist file inside the .app directory, verify that the key
 "UIDeviceFamily" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the form factor value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['UIDeviceFamily']
```

A valid XCtest UI package should produce output like the following:

```
[1, 2]
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file. Please unzip
 your test package and then open the Info.plist file inside the .app directory, verify that the
 key "CFBundleIdentifier" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the package name value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['CFBundleIdentifier']
```

A valid XCtest UI package should produce output like the following:

```
com.apple.test.swift-sampleUITests-Runner
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file. Please unzip your
 test package and then open the Info.plist file inside the .app directory, verify that the key
 "CFBundleExecutable" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the executable value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Info.plist')
print info_plist['CFBundleExecutable']
```

A valid XCtest UI package should produce output like the following:

```
XCTRunner
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_TEST_PACKAGE_NAME_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the package name value in the Info.plist file inside the
 .xctest directory. Please unzip your test package and then open the Info.plist file inside the
 .xctest directory, verify that the key "CFBundleIdentifier" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the package name value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
print info_plist['CFBundleIdentifier']
```

A valid XCtest UI package should produce output like the following:

```
com.amazon.swift-sampleUITests
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_TEST_EXECUTABLE_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

`We could not find the executable value in the Info.plist file inside the .xctest
 directory. Please unzip your test package and then open the Info.plist file inside the .xctest
 directory, verify that the key "CFBundleExecutable" is specified, and try again.`

In the following
example, the package's name is **swift-sample-UI.ipa**.

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.ipa
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.app` directory like
`swift-sampleUITests-Runner.app` in our example:

```
.
`-- Payload (directory)
        `-- swift-sampleUITests-Runner.app (directory)
                      |-- `Info.plist`
                      |-- Plugins (directory)
                      |       `swift-sampleUITests.xctest (directory)
                      |                       |-- Info.plist
                      |                       `-- (any other files)
                      `-- (any other files)
```

3. To find the executable value, you can open Info.plist using Xcode or Python.

For Python, you can install the biplist module by running the following command:

```
$ pip install biplist
```

4. Next, open Python and run the following command:

```
import biplist
info_plist = biplist.readPlist('Payload/swift-sampleUITests-Runner.app/Plugins/swift-sampleUITests.xctest/Info.plist')
print info_plist['CFBundleExecutable']
```

A valid XCtest UI package should produce output like the following:

```
swift-sampleUITests
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_MULTIPLE_APP_DIRS

If you see the following message, follow these steps to fix the issue.

`We found multiple .app directories inside your test package. Please unzip your test package, verify that only a single .app directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.zip
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you should find only single `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package.

```
.
`--swift-sample-UI.zip--(directory)
    `-- `swift-sampleUITests-Runner.app` (directory)
            |-- Info.plist
            |-- Plugins (directory)
            |       `swift-sampleUITests.xctest (directory)
           |            |-- Info.plist
           |            `-- (any other files)
            `-- (any other files)
    `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_MULTIPLE_IPA_DIRS

If you see the following message, follow these steps to fix the issue.

`We found multiple .ipa directories inside your test package. Please unzip your test package, verify that only a single .ipa directory is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.zip
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you should find only single `.ipa` directory like `sampleUITests.ipa` in our example inside the .zip test package.

```
.
`--swift-sample-UI.zip--(directory)
    `-- `sampleUITests.ipa` (directory)
            `-- Payload (directory)
                `-- swift-sampleUITests-Runner.app (directory)
    `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_BOTH_APP_AND_IPA_DIR_PRESENT

If you see the following message, follow these steps to fix the issue.

`We found both .app and .ipa files inside your test package. Please unzip your test package, verify that only a single .app or .ipa file is present inside the package, then try again.`

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.zip
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you should find either `.ipa` directory like `sampleUITests.ipa` or `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. You can refer to an example of valid XCTEST_UI Test package in our documentation on [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

```
.
`--swift-sample-UI.zip--(directory)
    `-- `sampleUITests.ipa` (directory)
            `-- Payload (directory)
                `-- swift-sampleUITests-Runner.app (directory)
   `-- (any other files)
```

or

```
.
`--swift-sample-UI.zip--(directory)
    `-- `swift-sampleUITests-Runner.app` (directory)
            |-- Info.plist
            |-- Plugins (directory)
            `-- (any other files)
   `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

## XCTEST_UI_TEST_PACKAGE_PAYLOAD_DIR_PRESENT_IN_ZIP

If you see the following message, follow these steps to fix the issue.

`We found a Payload directory inside your .zip test package. Please unzip your test package, ensure that a Payload directory is not present in the package, then try again.`

1. Copy your test package to your working directory, and then run the
   following command:

```
$ unzip swift-sample-UI.zip
```

2. After you successfully unzip the package, you can find the
   working directory tree structure by running the following command:

```
$ tree .
```

If the XCTest UI package is valid, you should not find a Payload Directory inside your test package.

```
.
`--swift-sample-UI.zip--(directory)
    `-- swift-sampleUITests-Runner.app (directory)
            |-- Info.plist
            |-- Plugins (directory)
            `-- (any other files)
   `-- `Payload (directory) [This directory should not be present]`
            |-- (any other files)
   `-- (any other files)
```

For more information, see [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").
