

# Integrating XCTest UI for iOS with Device Farm

Device Farm provides support for the XCTest UI testing framework. Specifically, Device Farm supports XCTest UI tests written in both Objective-C and [Swift](https://developer.apple.com/swift/). 

 The XCTest UI framework enables UI testing in iOS development, built on top of XCTest. For more information, see [User Interface Testing](https://developer.apple.com/library/prerelease/ios/documentation/DeveloperTools/Conceptual/testing_with_xcode/chapters/09-ui_testing.html#//apple_ref/doc/uid/TP40014132-CH13-SW1) in the iOS Developer Library.

For general information about testing in Device Farm, see [Test frameworks and built-in tests in AWS Device Farm](test-types.md).

Use the following instructions to integrate Device Farm with the XCTest UI testing framework for iOS.

**Topics**
+ [Configure XCTest UI test reports using a custom test environment](#test-types-ios-xctest-ui-generate-reports)
+ [Prepare your iOS XCTest UI tests](#test-types-ios-xctest-ui-prepare)
+ [Option 1: Creating an XCTest UI .ipa package](#how-to-use-create-XCTestUI-ipa-package)
+ [Option 2: Creating an XCTest UI .zip package](#how-to-use-create-XCTestUI-zip-package)
+ [Run iOS XCTest UI tests (console)](#test-types-ios-xctest-ui-upload)
+ [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console)
+ [View a test report (AWS CLI)](#test-types-ios-xctest-ui-view-insights-cli)

## Configure XCTest UI test reports using a custom test environment
<a name="test-types-ios-xctest-ui-generate-reports"></a>

Any test report that your tests write to `$DEVICEFARM_LOG_DIR` in your test spec YAML file is available in your test output artifacts after the run completes. By default, Device Farm also generates its own test report, called test insights. Test insights give you a per-test breakdown of results, durations, and stack traces for failures. You can view test insights in the console, and through the AWS CLI and APIs. Test insights are in addition to the artifacts that your tests produce, not a replacement for them.

Before you begin, make sure that your run meets the following requirements:
+ Your run uses a custom test environment. Device Farm does not generate test insights in the standard test environment. For more information, see [Test environments in AWS Device Farm](test-environments.md).
+ Your run uses the `macos_sequoia` test host or a newer host, such as `macos_tahoe`. Device Farm does not generate test insights on older test hosts. To choose the test host, set `ios_test_host` in your test spec file. For more information, see [Selecting a test host for custom test environments](custom-test-environments-hosts.md#test-host-selection).

To configure test reports for your XCTest UI tests:

1. Run **xcodebuild** with `-derivedDataPath` set to `$DEVICEFARM_DERIVED_DATA_PATH`, so that Xcode writes the `.xcresult` bundle to that directory. Device Farm collects your test output artifacts from `$DEVICEFARM_DERIVED_DATA_PATH` and reads the bundle from there to build the report. The default XCTest UI test spec already does this:

   ```bash
   xcodebuild test-without-building \
     -destination id=$DEVICEFARM_DEVICE_UDID \
     -xctestrun $DEVICEFARM_XCUITESTRUN_FILE \
     -derivedDataPath $DEVICEFARM_DERIVED_DATA_PATH
   ```

   If you point `-derivedDataPath` at a different directory, Device Farm does not collect the bundle, so it cannot build a report. You also do not receive screenshots.

1. Schedule the run in a custom test environment. Test insights are on by default. If you don't set the `insightsTypes` field of the `configuration` parameter of your `ScheduleRun` request, Device Farm sets it to `TEST_REPORT`. To turn off test insights for a run, see [Creating a test run in Device Farm](how-to-create-test-run.md).

The result bundle records a start time for each test. When the run records video, you also get per-test video. For more information, see [Per-test video](reports.md#reports-test-insights-video).

To view the report after the run completes, see [View a test report (console)](#test-types-ios-xctest-ui-view-insights-console). If Device Farm does not generate a report, see [Troubleshooting test reports and insights in AWS Device Farm](troubleshooting-test-insights.md).

## Prepare your iOS XCTest UI tests
<a name="test-types-ios-xctest-ui-prepare"></a>

You can either upload an `.ipa` file or a `.zip` file for your XCTEST\_UI test package, for a runner built for physical devices or for iOS simulators alike.

An `.ipa` file is an application archive containing the iOS Runner app in bundle format. *Additional files cannot be included inside the `.ipa` file.*

If you upload a `.zip` file, it can contain either the iOS Runner app directly or an `.ipa` file. You can also include other files within the `.zip` file if you want to use them during the tests. For example, you can include files like `.xctestrun`, `.xcworkspace`, or `.xcodeproj` inside the `.zip` file. Use these files to run XCUI Test Plans on Device Farm. Detailed instructions on how to run Test Plans are available in the default test specification file for the XCUI Test type. 

Build the runner for the type of device that you test on. Each option that follows has steps for physical devices and steps for simulators.

## Option 1: Creating an XCTest UI .ipa package
<a name="how-to-use-create-XCTestUI-ipa-package"></a>

This is the recommended package format. Xcode produces the `{{app-project-name}}UITest-Runner.app` bundle when you build your project for testing, in the Products directory for your project.

 The following folder structure shows how an example app named {{my-project-nameUITest-Runner.app}} would be packaged as an `.ipa` file: 

```
.
└── my-project-nameUITest.ipa
    └── Payload (directory)
        └── my-project-nameUITest-Runner.app
```

### Physical devices
<a name="how-to-use-create-XCTestUI-ipa-package-device"></a>

Build the UI test target for a physical device. In Xcode, choose **Generic iOS Device** as the destination. Then, on the **Product** menu, choose **Build For**, and then choose **Testing**. Xcode writes the runner to `Build/Products/Debug-iphoneos/{{name}}-Runner.app` under the derived data path. Alternatively, run the following command from the directory that contains your project file:

```bash
xcodebuild build-for-testing -project {{MyApp}}.xcodeproj -scheme {{MyApp}} \
    -sdk iphoneos -destination "generic/platform=iOS" -derivedDataPath build
```

Package the runner the same way as a device build of your app, with `{{name}}-Runner.app` inside the `Payload` directory. For the steps, see the [Physical devices](apps.md#test-runs-ios-app-package-device) steps in [Package your app](apps.md#test-runs-ios-app-package).

### Simulators
<a name="how-to-use-create-XCTestUI-ipa-package-simulator"></a>

Build the UI test target for a simulator. In Xcode, choose an iOS Simulator destination. Then, on the **Product** menu, choose **Build For**, and then choose **Testing**. Xcode writes the runner to `Build/Products/Debug-iphonesimulator/{{name}}-Runner.app` under the derived data path. Alternatively, run the following command from the directory that contains your project file:

```bash
xcodebuild build-for-testing -project {{MyApp}}.xcodeproj -scheme {{MyApp}} \
    -sdk iphonesimulator -destination "generic/platform=iOS Simulator" \
    -derivedDataPath build
```

Package the runner the same way as a simulator build of your app, with `{{name}}-Runner.app` inside the `Payload` directory. For the steps, see the [Simulators](apps.md#test-runs-ios-app-package-simulator) steps in [Package your app](apps.md#test-runs-ios-app-package).

## Option 2: Creating an XCTest UI .zip package
<a name="how-to-use-create-XCTestUI-zip-package"></a>

A `.zip` package holds the runner, and can hold other files that your tests use. What the `.zip` file can contain depends on the type of device that you test on.

**Note**  
Make sure that your XCTest UI `.zip` package does not contain a `Payload` directory.

### Physical devices
<a name="how-to-use-create-XCTestUI-zip-package-device"></a>

Device Farm automatically generates a `.xctestrun` file for you for running your full XCTest UI test suite. If you want to use your own `.xctestrun` file on Device Farm, you can compress one or more `.xctestrun` files and your app directory into a `.zip` file. If you already have an `.ipa` file for your test package, you can include it instead of the runner.

```
.
└── swift-sample-UI.zip (directory)
   ├── my-project-nameUITest-Runner.app [OR] my-project-nameUITest.ipa
   ├── SampleTestPlan_2.xctestrun
   ├── SampleTestPlan_1.xctestrun
   └── (any other files)
```

You can also run an Xcode test plan for your XCTest UI tests on Device Farm. Create a `.zip` file that contains your `my-project-nameUITest-Runner.app` or `my-project-nameUITest.ipa` file and the Xcode source files that the test plan needs, including either a `.xcworkspace` or `.xcodeproj` file.

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

### Simulators
<a name="how-to-use-create-XCTestUI-zip-package-simulator"></a>

Build the UI test target for a simulator as described in [Simulators](#how-to-use-create-XCTestUI-ipa-package-simulator) under Option 1, and then zip the runner. The runner must sit at the root of the `.zip` file. Do not nest the runner in a folder, and do not place an `.ipa` file inside the `.zip` file. The following command, run in the `Debug-iphonesimulator` folder, creates the archive with the runner at its root. Replace {{MyAppUITests}} with the name of your UI test target.

```bash
ditto -c -k --sequesterRsrc --keepParent {{MyAppUITests}}-Runner.app {{MyAppUITests}}-Runner.zip
```

The archive has the following layout:

```
.
└── MyAppUITests-Runner.zip
    └── MyAppUITests-Runner.app
```

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

1. Browse to and choose your iOS app file. For the build that your devices need, see [Packaging an iOS app](apps.md#test-runs-ios-app-packaging).

1. Under **Configure test**, in the **Select test framework** section, choose **XCTest UI**. Then, select **Choose file** under **Upload app**.

1. Browse to and choose the .ipa or .zip file that contains your iOS XCTest UI test runner. 

1. To configure run-level properties, update the **Run settings** section.

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

![The first set of columns on the Test report tab for a completed XCTest UI job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-start.png)


![The remaining columns on the Test report tab for a completed XCTest UI job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-column-end.png)


When the run records a video, the **Video** column has a play button for each test that plays the test in the job video. For more information, see [Watch a test in the job video](reports.md#reports-test-insights-video-console).

The following screenshot shows the **Test report** tab with the **Test video** panel open.

![The Test report tab for a completed XCTest UI job, with the Test video panel open on the selected test.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-video-panel.png)


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

![The Test report tab with tests grouped by class, showing each class expanded to its individual tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-xctest-ui-insights-enabled-test-report-grouped.png)


To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-console-without"></a>

If the run used the standard test environment, or if you turned off test insights for the run, the job results show the standard test output and artifacts, such as the **Suites**, **Logs**, and **Screenshots** tabs, but no **Test report** tab. To get a test report, schedule a new run in a custom test environment with **Generate test report** selected.

![The job results for a completed XCTest UI job without test insights enabled, showing the standard tabs and no Test report tab.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/passing.png)


## View a test report (AWS CLI)
<a name="test-types-ios-xctest-ui-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

### Without test insights enabled
<a name="test-types-ios-xctest-ui-view-insights-cli-without"></a>

If the run did not generate test insights, for example because it used the standard test environment or you turned off test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```json
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

If the run generated test insights, the response also includes an `insights` object that contains the test report status, high-level metrics, and a presigned URL to the detailed report:

```json
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

```json
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

`videoStartSeconds`  
Where the test started in the job video, in seconds. See [Per-test video](reports.md#reports-test-insights-video).

`videoEndSeconds`  
Where the test ended in the job video, in seconds.