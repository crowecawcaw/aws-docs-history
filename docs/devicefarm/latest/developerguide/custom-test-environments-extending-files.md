# Adding extra files to your test package in

Device Farm

You may want to use additional files as a part of your tests either as extra configuration files or additional
test data. You can add these additional files to your test package before uploading it to
AWS Device Farm, then access them from the custom environment mode. Fundamentally, all test package
upload formats (ZIP, IPA, APK, JAR, etc.) are package archive formats that support standard ZIP operations.

You can add files to your test archive before uploading it to AWS Device Farm by using the following
command:

```
$ zip zip-with-dependencies.zip extra_file
```

For a directory of extra files:

```
$ zip -r zip-with-dependencies.zip extra_files/
```

These commands work as expected for all test package upload formats except for IPA files. For IPA files,
especially when used with XCUITests, we recommend that you put any extra files in a slightly different location
due to how AWS Device Farm resigns iOS test packages. When building your iOS test, the test application
directory will be located inside of another directory named `Payload`.

For example, this is how one such iOS test directory may look:

```
$ tree
.
└── Payload
    └── ADFiOSReferenceAppUITests-Runner.app
        ├── ADFiOSReferenceAppUITests-Runner
        ├── Frameworks
        │   ├── XCTAutomationSupport.framework
        │   │   ├── Info.plist
        │   │   ├── XCTAutomationSupport
        │   │   ├── _CodeSignature
        │   │   │   └── CodeResources
        │   │   └── version.plist
        │   └── XCTest.framework
        │       ├── Info.plist
        │       ├── XCTest
        │       ├── _CodeSignature
        │       │   └── CodeResources
        │       ├── en.lproj
        │       │   └── InfoPlist.strings
        │       └── version.plist
        ├── Info.plist
        ├── PkgInfo
        ├── PlugIns
        │   ├── ADFiOSReferenceAppUITests.xctest
        │   │   ├── ADFiOSReferenceAppUITests
        │   │   ├── Info.plist
        │   │   └── _CodeSignature
        │   │       └── CodeResources
        │   └── ADFiOSReferenceAppUITests.xctest.dSYM
        │       └── Contents
        │           ├── Info.plist
        │           └── Resources
        │               └── DWARF
        │                   └── ADFiOSReferenceAppUITests
        ├── _CodeSignature
        │   └── CodeResources
        └── embedded.mobileprovision
```

For these XCUITest packages, add any extra files to the directory ending in `.app`
inside of the `Payload` directory. For example, the following commands show how you can
add a file to this test package:

```
$ mv extra_file Payload/*.app/
$ zip -r my_xcui_tests.ipa Payload/
```

When you add a file to your test package, you can expect slightly different interaction behavior in
AWS Device Farm based on its upload format. If the upload used the ZIP file extension,
AWS Device Farm will automatically unzip the upload before your test and leave the unzipped files at the
location with the `$DEVICEFARM_TEST_PACKAGE_PATH` environment variable. (This means that
if you added a file called `extra_file` to the root of the archive as in the first
example, it would be located at `$DEVICEFARM_TEST_PACKAGE_PATH/extra_file` during the
test).

To use a more practical example, if you’re an Appium TestNG user who wants to include a
`testng.xml` file with your test, you can include it in your archive using the
following command:

```
$ zip zip-with-dependencies.zip testng.xml
```

Then, you can change your test command in the custom environment mode to the following:

```
java -D appium.screenshots.dir=$DEVICEFARM_SCREENSHOT_PATH org.testng.TestNG -testjar *-tests.jar -d $DEVICEFARM_LOG_DIR/test-output $DEVICEFARM_TEST_PACKAGE_PATH/testng.xml
```

If your test package upload extension isn't ZIP (e.g., APK, IPA, or JAR file), the uploaded package file
itself is found at `$DEVICEFARM_TEST_PACKAGE_PATH`. Because these are still archive
format files, you can unzip the file in order to access the additional files from within. For example, the
following command will unzip the contents of the test package (for APK, IPA, or JAR files) to the
`/tmp` directory:

```
unzip $DEVICEFARM_TEST_PACKAGE_PATH -d /tmp
```

In the case of an APK or JAR file, you would find your extra files unzipped to the
`/tmp` directory (e.g., `/tmp/extra_file`). In the case of an
IPA file, as explained before, extra files would be in a slightly different location inside the folder ending in
`.app`, which is inside of the `Payload` directory. For
example, based on the IPA example above, the file would be found at the location
`/tmp/Payload/ADFiOSReferenceAppUITests-Runner.app/extra_file` (referenceable as
`/tmp/Payload/*.app/extra_file`).

For more ways to extend your test suite and optimize your tests, see [Extending custom test environments in Device Farm](custom-test-environments-extending.md "custom-test-environments-extending.md").
