# Integrating XCTest UI for iOS with Device Farm

Device Farm provides support for the XCTest UI testing framework. Specifically, Device Farm supports XCTest UI tests
written in both Objective-C and [Swift](https://developer.apple.com/swift/ "https://developer.apple.com/swift/").

The XCTest UI framework enables UI testing in iOS development, built on top of XCTest. For more information, see [User Interface Testing](https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html#//apple_ref/doc/uid/TP40014132-CH13-SW1 "https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html#//apple_ref/doc/uid/TP40014132-CH13-SW1") in the iOS Developer Library.

For general information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

Use the following instructions to integrate Device Farm with the XCTest UI testing framework for iOS.

###### Topics

- [Prepare your iOS XCTest UI tests](#test-types-ios-xctest-ui-prepare "#test-types-ios-xctest-ui-prepare")
- [Option 1: Creating an XCTest UI .ipa package](#how-to-use-create-XCTestUI-ipa-package "#how-to-use-create-XCTestUI-ipa-package")
- [Option 2: Creating an XCTest UI .zip package](#how-to-use-create-XCTestUI-zip-package "#how-to-use-create-XCTestUI-zip-package")
- [Upload your iOS XCTest UI tests](#test-types-ios-xctest-ui-upload "#test-types-ios-xctest-ui-upload")

## Prepare your iOS XCTest UI tests

You can either upload an `.ipa` file or a `.zip` file for your XCTEST_UI test package.

An `.ipa` file is an application archive containing the iOS Runner app in bundle format. _Additional files cannot be included inside the `.ipa` file._

If you upload a `.zip` file, it can contain either the iOS Runner app directly or an `.ipa` file. You can also include other files within the `.zip` file if you want to use them during the tests. For example you can include files like `.xctestrun`, `.xcworkspace` or `.xcodeproj` inside `.zip` file to run XCUI Test Plans on device farm. Detailed instructions on how to run Test Plans are available in the default test specification file for the XCUI Test type.

## Option 1: Creating an XCTest UI .ipa package

The *yourAppName*UITest-Runner.app bundle is produced by Xcode when you build your project for testing. It can be found in
the Products directory for your project.

To create an .ipa file:

1. Create a directory called `Payload`.
2. Add your app directory to the Payload directory.
3. Archive the Payload directory into a `.zip` file and then change the file extension to `.ipa`.

The following folder structure shows how an example app named `my-project-nameUITest-Runner.app` would be packaged as an `.ipa` file:

```

.
└── my-project-nameUITest.ipa
    └── Payload (directory)
        └── my-project-nameUITest-Runner.app
```

## Option 2: Creating an XCTest UI .zip package

Device Farm automatically generates a `.xctestrun` file for you for running your full XCTest UI test suite. If you want to use your own `.xctestrun` file on Device Farm, you can compress your `.xctestrun` files and app directory into a `.zip` file. If you already have a `.ipa` file for your test package you can include that here instead of `*-Runner.app`.

```

.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── SampleTestPlan_2.xctestrun
   ├── SampleTestPlan_1.xctestrun
   └── (any other files)
```

If you want to run an Xcode test plan for your XCUI tests on Device Farm, you can create a zip containing your _my-project-nameUITest-Runner.app_ **or** _my-project-nameUITest.ipa_ file and xcode source code files required to run XCTEST_UI with test plans, including either a `.xcworkspace` or `.xcodeproj` file.

Here is a sample zip using a `.xcodeproj` file:

```

.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── (any directory)
   └── `SampleXcodeProject.xcodeproj`
        ├── Testplan_1.xctestplan
        ├── Testplan_2.xctestplan
        └── (any other source code files created by xcode with .xcodeproj)

```

Here is a sample zip using a `.xcworkspace` file:

```

.
└──swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   └── (any directory)
   │   ├── SampleXcodeProject.xcodeproj
   │   ├── Testplan_1.xctestplan
   │   ├── Testplan_2.xctestplan
   |   └── (any other source code files created by xcode with .xcodeproj)
   └── `SampleWorkspace.xcworkspace`
       └── contents.xcworkspacedata

```

###### Note

Please ensure that you do not have a directory named "Payload" inside your XCTest UI .zip package.

## Upload your iOS XCTest UI tests

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose
   **Projects**.
3. In the list of projects, choose the project that you want to upload your tests to.

###### Tip

You can use the search bar to filter the project list by name.

To create a project, follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md") 4. Choose **Create run**. 5. Under **Run settings**, in the **Run type** section,
choose **iOS app**. 6. Under **Select app**, in the **App selection options** section,
select **Upload own app**. Then, select **Choose file** under
**Upload app**. 7. Browse to and choose your iOS app file. The file must be an .ipa file.

###### Note

Make sure that your .ipa file is built for an iOS device and not for a simulator. 8. Under **Configure test**, in the **Select test framework**
section, choose **XCTest UI**. Then, select **Choose
file** under **Upload app**. 9. Browse to and choose the .ipa or .zip file that contains your iOS XCTest UI test runner. 10. Complete the remaining steps in the run creation process. You will select the devices that you
want to test on and optionally specify additional configuration. 11. Choose **Create run**. Device Farm runs your test and shows the results in the console.
