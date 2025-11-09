# Troubleshooting XCTest tests in AWS Device Farm

The following topic lists error messages that occur during the upload of XCTest tests and recommends workarounds
to resolve each error.

###### Note

The instructions below assume you are using MacOS.

## XCTEST_TEST_PACKAGE_UNZIP_FAILED

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not open your test ZIP file. Please verify that the file is valid and try again.

Make sure that you can unzip the application package without errors. In the following example, the package's
name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip swiftExampleTests.xctest-1.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

A valid XCTest package should produce output like the following:

```
.
`-- swiftExampleTests.xctest (directory)
              |-- Info.plist
              `-- (any other files)
```

For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md "test-types-ios-xctest.md").

## XCTEST_TEST_PACKAGE_XCTEST_DIR_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the .xctest directory inside your test package. Please unzip your test package, verify
that the .xctest directory is inside the package, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip swiftExampleTests.xctest-1.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the XCTest package is valid, you will find a directory with a name similar to
`swiftExampleTests.xctest` inside the working directory. The name should end with
`.xctest`.

```
.
`-- `swiftExampleTests.xctest` (directory)
              |-- Info.plist
              `-- (any other files)
```

For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md "test-types-ios-xctest.md").

## XCTEST_TEST_PACKAGE_PLIST_FILE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the Info.plist file inside the .xctest directory. Please unzip your test package and then
open the .xctest directory, verify that the Info.plist file is inside the directory, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip swiftExampleTests.xctest-1.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

If the XCTest package is valid, you will find the `Info.plist` file inside the
`.xctest` directory. In our example below, the directory is called
`swiftExampleTests.xctest`.

```
.
`-- swiftExampleTests.xctest (directory)
              |-- `Info.plist`
              `-- (any other files)
```

For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md "test-types-ios-xctest.md").

## XCTEST_TEST_PACKAGE_PACKAGE_NAME_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the package name value in the Info.plist file. Please unzip your test package and then
open Info.plist file, verify that the key "CFBundleIdentifier" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip swiftExampleTests.xctest-1.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.xctest` directory like `swiftExampleTests.xctest` in our
example:

```
.
`-- swiftExampleTests.xctest (directory)
              |-- `Info.plist`
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
info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
print info_plist['CFBundleIdentifier']
```

A valid XCtest application package should produce output like the following:

```
com.amazon.kanapka.swiftExampleTests
```

For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md "test-types-ios-xctest.md").

## XCTEST_TEST_PACKAGE_EXECUTABLE_VALUE_MISSING

If you see the following message, follow these steps to fix the issue.

###### Warning

We could not find the executable value in the Info.plist file. Please unzip your test package and then open
Info.plist file, verify that the key "CFBundleExecutable" is specified, and try again.

In the following example, the package's name is **swiftExampleTests.xctest-1.zip**.

1. Copy your test package to your working directory, and then run the following command:

```
$ unzip swiftExampleTests.xctest-1.zip
```

2. After you successfully unzip the package, you can find the working directory tree structure by running the
   following command:

```
$ tree .
```

You should find the `Info.plist` file inside an
`.xctest` directory like `swiftExampleTests.xctest` in our
example:

```
.
`-- swiftExampleTests.xctest (directory)
              |-- `Info.plist`
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
info_plist = biplist.readPlist('swiftExampleTests.xctest/Info.plist')
print info_plist['CFBundleExecutable']
```

A valid XCtest application package should produce output like the following:

```
swiftExampleTests
```

For more information, see [Integrating Device Farm with XCTest for iOS](test-types-ios-xctest.md "test-types-ios-xctest.md").
