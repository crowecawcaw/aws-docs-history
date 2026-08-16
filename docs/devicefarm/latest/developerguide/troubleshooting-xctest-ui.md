# Troubleshooting XCTest UI tests in AWS Device Farm

The following topic lists error messages that occur during the upload of XCTest UI
tests and recommends workarounds to resolve each error.

## Upload errors

The following errors can occur when you upload your XCTest UI tests.

### XCTEST\_UI\_TEST\_PACKAGE\_UNZIP\_FAILED

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

### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_APP\_DIR\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_PLUGINS\_DIR\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_XCTEST\_DIR\_MISSING\_IN\_PLUGINS\_DIR

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

### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_PLIST\_FILE\_MISSING\_IN\_XCTEST\_DIR

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

### XCTEST\_UI\_TEST\_PACKAGE\_CPU\_ARCHITECTURE\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_PLATFORM\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_WRONG\_PLATFORM\_DEVICE\_VALUE

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

### XCTEST\_UI\_TEST\_PACKAGE\_FORM\_FACTOR\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_PACKAGE\_NAME\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_EXECUTABLE\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_PACKAGE\_NAME\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_TEST\_EXECUTABLE\_VALUE\_MISSING

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

### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_APP\_DIRS

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

### XCTEST\_UI\_TEST\_PACKAGE\_MULTIPLE\_IPA\_DIRS

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

### XCTEST\_UI\_TEST\_PACKAGE\_BOTH\_APP\_AND\_IPA\_DIR\_PRESENT

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

If the XCTest UI package is valid, you should find either `.ipa` directory like `sampleUITests.ipa` or `.app` directory like `swift-sampleUITests-Runner.app` in our example inside the .zip test package. You can refer to an example of valid XCTEST\_UI Test package in our documentation on [Integrating XCTest UI for iOS with Device Farm](test-types-ios-xctest-ui.md "test-types-ios-xctest-ui.md").

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

### XCTEST\_UI\_TEST\_PACKAGE\_PAYLOAD\_DIR\_PRESENT\_IN\_ZIP

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

## Test insights

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the
service cannot generate the report, the insights report status is `SKIPPED` or
`ERRORED`, and the report message explains why. The following messages can occur
when generating insights for XCTest UI tests.

### The job did not run to completion

`Unable to generate test insights because the job was
 `status`.`

The job ended in a non-successful state (where
`status` is `STOPPED`, `ERRORED`, or
`SKIPPED`), so there was no result to summarize. A run that ends in a failed
state still receives insights.

To resolve this issue, investigate why the job did not run to completion.
In many cases, the `message` field of the job itself might explain why the job didn't complete.

### The results contained no test cases

`Test insights could not be generated. The xcresult_summary.json file was
 parsed successfully but contained no test cases.`

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and
that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

### The test output exceeds the maximum supported size

`Unable to generate test insights: test output "xcresult bundle" exceeds
 the maximum supported size of 1GB.`

The xcresult bundle is larger than 1 GB.

To resolve this issue, reduce the xcresult bundle size to below 1 GB by trimming logs or
attachments.

### The xcresult bundle was not found

`Unable to generate test insights. The xctestresult bundle file
 (.xcresult) was not found in the output artifacts.`

Device Farm could not find an `.xcresult` bundle for this job, so there
were no results to summarize.

Device Farm looks for the bundle anywhere under
`$DEVICEFARM_DERIVED_DATA_PATH`. The default XCTest UI test spec produces it
there automatically, so this message usually indicates that a customized test spec did not
write results to that location.

To confirm whether a bundle was produced, download the customer artifacts for the job
and look for an `.xcresult` directory under the derived data
folder.

### The xcresult test results could not be processed

`Test insights could not be generated because of an error while processing the
 .xcresult test results.`

Device Farm found an `.xcresult` bundle but could not read the test results
from it.

To resolve this issue, ensure that your test run produces a valid
`.xcresult` bundle. Verify that your test spec does not modify,
truncate, or archive the bundle before the run finishes, and that the
**xcodebuild** command completes rather than being interrupted by a
timeout.
