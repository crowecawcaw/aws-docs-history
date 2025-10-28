# Integrating Device Farm with XCTest for iOS

With Device Farm, you can use the XCTest framework to test your app on real devices. For more information about
XCTest, see [Testing Basics](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/03-testing_basics.html "https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/03-testing_basics.html") in _Testing with Xcode_.

To run a test, you create the packages for your test run, and you upload these packages to Device Farm.

For more information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md "test-types.md").

###### Topics

- [Create the packages for your XCTest run](#test-types-ios-xctest-create-packages "#test-types-ios-xctest-create-packages")
- [Upload the packages for your XCTest run to Device Farm](#test-types-ios-xctest-upload "#test-types-ios-xctest-upload")

## Create the packages for your XCTest run

To test your app by using the XCTest framework, Device Farm requires the following:

- Your app package as a `.ipa` file.
- Your XCTest package as a `.zip` file.

You create these packages by using the build output that Xcode generates. Complete the following steps to
create the packages so that you can upload them to Device Farm.

###### To generate the build output for your app

1. Open your app project in Xcode.
2. In the scheme dropdown menu in the Xcode toolbar, choose **Generic iOS Device**
   as the destination.
3. In the **Product** menu, choose **Build For**, and then choose
   **Testing**.

###### To create the app package

1. In the project navigator in Xcode, under **Products**, open the contextual menu
   for the file named ``app-project-name`.app`. Then,
choose **Show in Finder**. Finder opens a folder named
`Debug-iphoneos`, which contains the output that Xcode generated for your
test build. This folder includes your `.app` file.
2. In Finder, create a new folder, and name it `Payload`.
3. Copy the ``app-project-name`.app`file, and paste it
in the`Payload` folder.
4. Open the contextual menu for the `Payload` folder and choose **Compress
   "Payload"**. A file named `Payload.zip` is created.
5. Change the file name and extension of `Payload.zip` to
   ``app-project-name`.ipa`.

In a later step, you provide this file to Device Farm. To make the file easier to find, you might want
to move it to another location, such as your desktop. 6. Optionally, you can delete the `Payload` folder and the
`.app` file in it.

###### To create the XCTest package

1. In Finder, in the `Debug-iphoneos` directory, open the contextual menu for the
   ``app-project-name`.app` file. Then, choose
   **Show Package Contents**.
2. In the package contents, open the `Plugins` folder. This folder contains a file
   named ``app-project-name`.xctest`.
3. Open the contextual menu for this file and choose **Compress
   "``app-project-name`.xctest`"**. A
   file named ``app-project-name`.xctest.zip` is
   created.

In a later step, you provide this file to Device Farm. To make the file easier to find, you might want
to move it to another location, such as your desktop.

## Upload the packages for your XCTest run to Device Farm

Use the Device Farm console to upload the packages for your test.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. If you don't have a project already, create one. For the steps to create a project, see [Creating a project in AWS Device Farm](how-to-create-project.md "how-to-create-project.md").

Otherwise, on the Device Farm navigation panel, choose **Mobile Device Testing**, then
choose **Projects**. 3. Choose the project that you want to use to run the test. 4. Choose **Create run**. 5. Under **Run settings**, in the **Run type** section,
choose **iOS app**. 6. Under **Select app**, in the **App selection options** section,
select **Upload own app**. Then, select **Choose file** under
**Upload app**. 7. Browse to the `.ipa` file for your app and upload it.

###### Note

Your `.ipa` package must be built for testing. 8. Under **Configure test**, in the **Select test framework**
section, choose **XCTest**. Then, select **Choose
file** under **Upload app**. 9. Browse to the `.zip` file that contains the XCTest package for your app and
upload it. 10. Complete the remaining steps in the project creation process. You will select the devices that you
want to test on and specify the device state. 11. Choose **Create run**. Device Farm runs your test and shows the results in the console.
