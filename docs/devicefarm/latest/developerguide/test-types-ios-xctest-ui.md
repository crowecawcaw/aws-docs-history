

# Integrating XCTest UI for iOS with Device Farm
<a name="test-types-ios-xctest-ui"></a>

Device Farm provides support for the XCTest UI testing framework. Specifically, Device Farm supports XCTest UI tests written in both Objective-C and [Swift](https://developer.apple.com/swift/). 

 The XCTest UI framework enables UI testing in iOS development, built on top of XCTest. For more information, see [User Interface Testing](https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html#//apple_ref/doc/uid/TP40014132-CH13-SW1) in the iOS Developer Library.

For general information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md).

Use the following instructions to integrate Device Farm with the XCTest UI testing framework for iOS.

**Topics**
+ [Prepare your iOS XCTest UI tests](#test-types-ios-xctest-ui-prepare)
+ [Option 1: Creating an XCTest UI .ipa package](#how-to-use-create-XCTestUI-ipa-package)
+ [Option 2: Creating an XCTest UI .zip package](#how-to-use-create-XCTestUI-zip-package)
+ [Run iOS XCTest UI tests (console)](#test-types-ios-xctest-ui-upload)
+ [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console)
+ [View a test report (AWS CLI)](#test-types-ios-xctest-ui-view-insights-cli)

## Prepare your iOS XCTest UI tests
<a name="test-types-ios-xctest-ui-prepare"></a>

You can either upload an `.ipa` file or a `.zip` file for your XCTEST\_UI test package.

An `.ipa` file is an application archive containing the iOS Runner app in bundle format. *Additional files cannot be included inside the `.ipa` file.*

If you upload a `.zip` file, it can contain either the iOS Runner app directly or an `.ipa` file. You can also include other files within the `.zip` file if you want to use them during the tests. For example you can include files like `.xctestrun`, `.xcworkspace` or `.xcodeproj` inside `.zip` file to run XCUI Test Plans on device farm. Detailed instructions on how to run Test Plans are available in the default test specification file for the XCUI Test type. 

## Option 1: Creating an XCTest UI .ipa package
<a name="how-to-use-create-XCTestUI-ipa-package"></a>

The *yourAppName*UITest-Runner.app bundle is produced by Xcode when you build your project for testing. It can be found in the Products directory for your project.

To create an .ipa file:

1. Create a directory called {{Payload}}.

1. Add your app directory to the Payload directory.

1. Archive the Payload directory into a `.zip` file and then change the file extension to `.ipa`.

 The following folder structure shows how an example app named {{my-project-nameUITest-Runner.app}} would be packaged as an `.ipa` file: 

```
.
└── my-project-nameUITest.ipa
    └── Payload (directory)
        └── my-project-nameUITest-Runner.app
```

## Option 2: Creating an XCTest UI .zip package
<a name="how-to-use-create-XCTestUI-zip-package"></a>

Device Farm automatically generates a `.xctestrun` file for you for running your full XCTest UI test suite. If you want to use your own `.xctestrun` file on Device Farm, you can compress your `.xctestrun` files and app directory into a `.zip` file. If you already have a `.ipa` file for your test package you can include that here instead of {{\*-Runner.app}}.

```
.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── SampleTestPlan_2.xctestrun
   ├── SampleTestPlan_1.xctestrun
   └── (any other files)
```

 If you want to run an Xcode test plan for your XCUI tests on Device Farm, you can create a zip containing your *my-project-nameUITest-Runner.app* **or** *my-project-nameUITest.ipa* file and xcode source code files required to run XCTEST\_UI with test plans, including either a `.xcworkspace` or `.xcodeproj` file.

Here is a sample zip using a `.xcodeproj` file: 

```
.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── (any directory)
   └── {{SampleXcodeProject.xcodeproj}}
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
   └── {{SampleWorkspace.xcworkspace}}
       └── contents.xcworkspacedata
```

**Note**  
Please ensure that you do not have a directory named "Payload" inside your XCTest UI .zip package. 

## Run iOS XCTest UI tests (console)
<a name="test-types-ios-xctest-ui-upload"></a>

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. In the list of projects, choose the project that you want to upload your tests to.
**Tip**  
You can use the search bar to filter the project list by name.  
To create a project, follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md)

1. Choose **Create run**.

1. Under **Select app and run type**, in the **Run type** section, choose **iOS app**.

1. In the **Select app** section, in **App selection options**, select **Upload own app**. Then, select **Choose file** under **Upload app**.

1. Browse to and choose your iOS app file. The file must be an .ipa file.
**Note**  
Make sure that your .ipa file is built for an iOS device and not for a simulator.

1. Under **Configure test**, in the **Select test framework** section, choose **XCTest UI**. Then, select **Choose file** under **Upload app**.

1. Browse to and choose the .ipa or .zip file that contains your iOS XCTest UI test runner. 

1. (Optional) To configure run-level properties, update the **Run settings** section:

   1. To have Device Farm generate a Test Insights report after your run completes, enable **Generate test report**. This option is available in a custom test environment only.

      The following prerequisites apply:

      1. Your tests must generate an Xcode `.xcresult` bundle and write it to `$DEVICEFARM_DERIVED_DATA_PATH`. For example, pass `-derivedDataPath $DEVICEFARM_DERIVED_DATA_PATH` to `xcodebuild`. The default XCTest UI test spec produces and stores this bundle automatically if you keep the default configuration.

      For more information about viewing your report, see [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console).

1. Complete the remaining steps in the run creation process. Select the devices that you want to test on and optionally specify additional configuration.

1. Choose **Create run**. Device Farm runs your test and shows the results in the console.

## View a test report (console)
<a name="test-types-ios-xctest-ui-view-insights-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

### With test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-console-with"></a>

The job results include a **Test report** tab. Choose it to see a summary of the test results, including the total number of tests, how many passed and failed, the total test execution time, and the median test execution time. Below the summary, the **Tests** table shows a per-test breakdown.

![The first set of columns on the Test report tab for a completed XCTest UI job.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-start.png)


![The remaining columns on the Test report tab for a completed XCTest UI job.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-end.png)


Each row in the **Tests** table includes the following columns:
+ **Result** – whether the test passed, failed, or was skipped.
+ **Test class** – the class that the test belongs to.
+ **Test name** – the name of the test method.
+ **Stack trace** – for a failed test, a link to the stack trace of the failure.
+ **Duration** – how long the test took to run.
+ **Start time** and **End time** – when the test started and ended.
+ **Framework result** – the result string that the XCTest framework reported for the test.
+ **Test bundle** – the test bundle that the test belongs to.
+ **Node identifier** – the xcresult node identifier for the test case.

You can search for a test by name, class, or status. To choose which columns appear, choose the **Settings** icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Expand a class to see its individual tests, as shown in the following screenshot.

![The Test report tab with tests grouped by class, showing each class expanded to its individual tests.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-grouped.png)


To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-console-without"></a>

The job results show the standard test output and artifacts, such as the **Suites**, **Logs**, and **Screenshots** tabs, but no **Test report** tab. To generate a test report, schedule a new run with test insights enabled.

![The job results for a completed XCTest UI job without test insights enabled, showing the standard tabs and no Test report tab.](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/passing.png)


## View a test report (AWS CLI)
<a name="test-types-ios-xctest-ui-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-cli-without"></a>

If you did not enable test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Apple iPhone",
        "created": "2026-08-05T14:26:56.959000-07:00",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": {
            "total": 3,
            "passed": 3,
            "failed": 0,
            "warned": 0,
            "errored": 0,
            "stopped": 0,
            "skipped": 0
        },
        "message": "Successful test lifecycle of Setup Test",
        "device": {
            "arn": "arn:aws:devicefarm:us-west-2::device:EXAMPLEDEVICEID",
            "name": "Example Apple iPhone",
            "platform": "IOS",
            "os": "18",
            "formFactor": "PHONE",
            "fleetType": "PUBLIC"
        },
        "deviceMinutes": {
            "total": 1.38,
            "metered": 0.0,
            "unmetered": 1.13
        },
        "videoCapture": true
    }
}
```

### With test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-cli-with"></a>

If you enabled test insights, the response also includes an `insights` object that contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "status": "COMPLETED",
        "result": "PASSED",
        "counters": { ... },
        "device": { ... },
        "deviceMinutes": { ... },
        "videoCapture": true,
        "insights": {
            "status": "COMPLETED",
            "testReport": {
                "message": "Results: 2 Executed | 2 passed, Median test duration: 3.214 seconds.",
                "metrics": {
                    "testsTotal": 2,
                    "testsPassed": 2,
                    "testsFailed": 0,
                    "testsSkipped": 0,
                    "testsErrored": 0,
                    "testsOther": 0,
                    "testsPassedPercentage": 100.0
                },
                "testDetailsUrl": "https://EXAMPLE-PRESIGNED-URL"
            }
        }
    }
}
```

The `testDetailsUrl` field is a presigned URL to the full test report JSON. Download it to get the per-test breakdown:

```
curl -o test-report.json "{{PRESIGNED_URL}}"
```

The following is an example test report for an XCTest UI job:

```
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:5e01a8c7-c861-4c0a-b1d5-12345EXAMPLE/a1b2c3d4-e5f6-4a7b-8c9d-67890EXAMPLE/00000",
  "deviceName": "Apple iPhone 15",
  "deviceArn": "arn:aws:devicefarm:us-west-2::device:A1B2C3D4E5F60718293A4B5C6D7E8F90",
  "deviceOsVersion": "17.5",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 2,
    "testsFailed": 1,
    "testsSkipped": 0,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 66.67,
    "totalTestExecutionDurationSeconds": 6.914,
    "medianTestExecutionDurationSeconds": 2.062
  },
  "testDetails": [
    {
      "testName": "test_execute()",
      "testClass": "AlertsTest",
      "frameworkResult": "Passed",
      "result": "PASSED",
      "durationSeconds": 2.062,
      "startTimestamp": "2026-07-31T16:58:26.646000Z",
      "endTimestamp": "2026-07-31T16:58:28.708000Z",
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "AlertsTest/test_execute()"
    },
    {
      "testName": "test_login()",
      "testClass": "LoginTest",
      "frameworkResult": "Failed",
      "result": "FAILED",
      "durationSeconds": 3.541,
      "startTimestamp": "2026-07-31T16:58:29.000000Z",
      "endTimestamp": "2026-07-31T16:58:32.541000Z",
      "stackTrace": "LoginTest.swift:88: XCTAssertEqual failed: (\"Welcome\") is not equal to (\"Error\")\nLoginTest.swift:91: XCTAssertTrue failed",
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "LoginTest/test_login()"
    },
    {
      "testName": "test_themeRendering()",
      "testClass": "ThemeTest",
      "frameworkResult": "Passed",
      "result": "PASSED",
      "durationSeconds": 1.311,
      "testBundle": "AWSDeviceFarmiOSReferenceAppSwiftUITests",
      "nodeIdentifier": "ThemeTest/test_themeRendering()",
      "testArguments": "Dark Appearance, Portrait"
    }
  ]
}
```

The report contains the following top-level fields:

`version`, `jobArn`  
The report schema version and the ARN of the job.

`deviceName`, `deviceArn`, `deviceOsVersion`  
The name and ARN of the device that ran the job, and its operating system version.

`metrics`  
Aggregate results for the job: the total number of tests (`testsTotal`) and how many passed (`testsPassed`), failed (`testsFailed`), were skipped (`testsSkipped`), errored (`testsErrored`), or had another result (`testsOther`), along with the pass rate (`testsPassedPercentage`), the total test duration (`totalTestExecutionDurationSeconds`), and the median test duration (`medianTestExecutionDurationSeconds`).

Each entry in `testDetails` contains the following fields:

`testName`, `testClass`  
The name of the test method and its test class.

`result`, `frameworkResult`  
The Device Farm result for the test, and the result string that the XCTest framework reported. Device Farm maps `frameworkResult` to the normalized `result` field.

`durationSeconds`, `startTimestamp`, `endTimestamp`  
The duration of the test in seconds, and the times when it started and ended.

`testBundle`, `nodeIdentifier`  
The test bundle that the test belongs to, and the xcresult node identifier for the test case.

`testArguments`  
For a parameterized test invocation, the argument label for the invocation.

`stackTrace`  
For a failed test, the stack trace of the failure.