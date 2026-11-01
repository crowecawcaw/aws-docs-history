

# Integrating Android Instrumentation with Device Farm
<a name="test-types-android-instrumentation-integrate"></a>

**Note**  
Use the following instructions to integrate Android instrumentation tests with AWS Device Farm. For more information about using instrumentation tests in Device Farm, see [Instrumentation for Android and AWS Device Farm](test-types-android-instrumentation.md). 

## Configure instrumentation test reports using a custom test environment
<a name="test-types-android-instrumentation-generate-reports"></a>

Any file that your tests write to `$DEVICEFARM_LOG_DIR` in your test spec YAML file is available in your test output artifacts after the run completes. Device Farm can also generate a test report of its own, called test insights, which gives you a per-test breakdown of results, durations, and stack traces for failures. You can view test insights in the console, and through the AWS CLI and APIs. Test insights are in addition to the artifacts that your tests produce, not a replacement for them.

Device Farm generates test insights for instrumentation tests only when you run them in a custom test environment. For more information, see [Test environments in AWS Device Farm](test-environments.md).

1. Run **am instrument** with the `-r` option, and pipe its output through **tee** so that the output appears in your test spec output. Device Farm reads your test spec output to build the report. The default instrumentation test spec already does this:

   ```
   adb -s $DEVICEFARM_DEVICE_UDID shell am instrument -r -w --no-window-animation \
     $DEVICEFARM_TEST_PACKAGE_NAME/$DEVICEFARM_TEST_PACKAGE_RUNNER 2>&1 | tee $DEVICEFARM_LOG_DIR/instrument.log
   ```

   The `-r` option tells **am instrument** to print raw results. **tee** writes those results to a file and also passes them through to your test spec output, which is what Device Farm reads. The results look like the following:

   ```
   INSTRUMENTATION_STATUS: class=com.example.GpsConnectInstrumentedTest
   INSTRUMENTATION_STATUS: current=1
   INSTRUMENTATION_STATUS: id=AndroidJUnitRunner
   INSTRUMENTATION_STATUS: numtests=2
   INSTRUMENTATION_STATUS: test=useAppContext
   ```

   If you redirect this output to a file only, with `>` instead of **tee**, the results never reach your test spec output and Device Farm cannot build a report.

1. Opt in to test insights when you schedule the run. You can do this in the console or with the AWS CLI and APIs:
   + In the console, in the **Run settings** section, under **Test Insights**, choose **Generate test report**. For more information, see [Run Android Instrumentation tests (console)](#test-types-android-instrumentation-upload).
   + With the AWS CLI or the API, set the `insightsTypes` field of the `configuration` parameter of **ScheduleRun** to `TEST_REPORT`:

     ```
     aws devicefarm schedule-run \
       --project-arn {{projectArn}} \
       --device-pool-arn {{devicePoolArn}} \
       --test type=INSTRUMENTATION,testPackageArn={{testPackageArn}},testSpecArn={{testSpecArn}} \
       --configuration '{"insightsTypes":["TEST_REPORT"]}'
     ```

     Device Farm rejects `insightsTypes` if the run does not use a test spec, because test insights require a custom test environment.

     For more information, see [ScheduleRun](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRun.html) and [insightsTypes](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ScheduleRunConfiguration.html#devicefarm-Type-ScheduleRunConfiguration-insightsTypes) in the *Device Farm API Reference*.

To view the report after the run completes, see [View a test report (console)](#test-types-android-instrumentation-view-insights-console). If Device Farm does not generate a report, see [Test insights](troubleshooting-instrumentation-tests.md#troubleshooting-instrumentation-tests-insights).

## Run Android Instrumentation tests (console)
<a name="test-types-android-instrumentation-upload"></a>

Use the Device Farm console to upload your tests.

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. In the list of projects, choose the project that you want to upload your tests to.
**Tip**  
You can use the search bar to filter the project list by name.  
To create a project, follow the instructions in [Creating a project in AWS Device Farm](how-to-create-project.md).

1. Select **Create run**.

1. Under **Select app and run type**, in the **Run type** section, select **Android app**.

1. Under **Select app**, in the **App selection options** section, choose **Select sample app provided by Device Farm** if you do not have an app. If you are bringing your own app, select **Upload own app**, and then choose your APK (.apk file format).

1. Under **Configure test**, in the **Select test framework** section, choose **Instrumentation**, and then choose **Choose File**. Browse to and choose the APK file (.apk file format) that contains your tests.

1. Under **Choose your execution environment**, select either **Run your test in a custom environment** or **Run your test in our standard environment**. For more information, see [Test environments in AWS Device Farm](test-environments.md).

1. If you chose the custom environment, you can use the default test spec that is populated for instrumentation tests, or choose **Upload own test spec** to provide your own.

1. Under **Select devices**, choose a device selection method. Select **Use Device Pool** to choose from a curated collection of devices or a custom device pool you created. Select **Manually select devices** to pick individual devices to run your tests against. The **Device compatibility** section shows how many devices in the selected pool are compatible with your app. For more information, see [Device support in AWS Device Farm](devices.md).

1. To configure run-level properties, update the **Run settings** section.

   (Optional) To have Device Farm generate a test report after your run completes, in the **Run settings** section, under **Test Insights**, choose **Generate test report**. This option is available in a custom test environment only. For the prerequisites, see [Configure instrumentation test reports using a custom test environment](#test-types-android-instrumentation-generate-reports).

1. Complete the remaining steps, and then start the run.

## View a test report (console)
<a name="test-types-android-instrumentation-view-insights-console"></a>

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Projects**.

1. Choose the project that contains the run you want to inspect.

1. Choose the completed run to open its details.

1. Choose one of the completed jobs to open the results for that device.

### With test insights enabled
<a name="test-types-android-instrumentation-view-insights-console-with"></a>

The job results include a **Test report** tab. Choose it to see a per-test breakdown. The following screenshots show the **Test report** tab with all columns visible.

![The first set of columns on the Test report tab for a completed instrumentation job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-column-start.png)


![The remaining columns on the Test report tab for a completed instrumentation job.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-column-end.png)


The tab shows the following fields for each test:

`testName`  
The name of the test method.

`testClass`  
The name of the test class.

`result`  
The Device Farm result for the test.

`frameworkResult`  
The result that the instrumentation framework reported. Device Farm maps this value to the normalized `result` field.

`durationSeconds`  
The duration of the test, in seconds.

`startTimestamp`  
The time when the test started.

`endTimestamp`  
The time when the test ended.

`current`  
The position of the test in the run.

`numTests`  
The total number of tests in the run.

`statusCode`  
The instrumentation status code that the test reported.

`stream`  
A human-readable version of the instrumentation output for the test.

`stackTrace`  
For a failed test, the stack trace of the failure.

To download the full test report as a JSON file, choose **Download full summary** at the top of the job details.

To choose which columns appear, choose the gear icon. In the settings, you can select the columns to display and turn **Group by class** on or off. **Group by class** is on by default, which groups the tests by their test class. Turn it off to see a flat list of all tests, as shown in the following screenshot.

![The Test report tab with Group by class turned off, showing a flat list of tests.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-enabled-test-report-without-grouping.png)


### Without test insights enabled
<a name="test-types-android-instrumentation-view-insights-console-without"></a>

The job results show the standard test output and artifacts, but no **Test report** tab. To generate a test report, schedule a new run with test insights enabled.

![The job results for a completed instrumentation job without test insights enabled.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-instrumentation-insights-disabled-test-report.png)


## View a test report (AWS CLI)
<a name="test-types-android-instrumentation-view-insights-cli"></a>

Run **get-job** and specify the job ARN:

```
aws devicefarm get-job --arn {{arn:aws:devicefarm:us-west-2:123456789012:job:PROJECT_ID/RUN_ID/00000}}
```

### Without test insights enabled
<a name="test-types-android-instrumentation-view-insights-cli-without"></a>

If you did not enable test insights, the response contains the standard job fields, such as the job status, result, counters, and device:

```
{
    "job": {
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
        "name": "Example Android Phone",
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
            "name": "Example Android Phone",
            "platform": "ANDROID",
            "os": "16",
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
<a name="test-types-android-instrumentation-view-insights-cli-with"></a>

If you enabled test insights, the response also includes an `insights` object. This object contains the test report status, high-level metrics, and a presigned URL to the detailed report:

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
                "message": "Results: 2 Executed | 2 passed, Median test duration: 28.926 seconds.",
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

The following is an example test report for an instrumentation job:

```
{
  "version": "1.0",
  "jobArn": "arn:aws:devicefarm:us-west-2:123456789012:job:EXAMPLE-PROJECT/EXAMPLE-RUN/00000",
  "metrics": {
    "testsTotal": 3,
    "testsPassed": 2,
    "testsFailed": 1,
    "testsSkipped": 0,
    "testsErrored": 0,
    "testsOther": 0,
    "testsPassedPercentage": 66.67,
    "totalTestExecutionDurationSeconds": 26.004,
    "medianTestExecutionDurationSeconds": 1.598
  },
  "testDetails": [
    {
      "testName": "testConnect",
      "testClass": "com.example.myapp.GpsConnectInstrumentedTest",
      "frameworkResult": "PASSED",
      "result": "PASSED",
      "durationSeconds": 24.399,
      "startTimestamp": "2026-08-05T20:38:30.131514Z",
      "endTimestamp": "2026-08-05T20:38:54.530369Z",
      "statusCode": 0,
      "current": 1,
      "numTests": 3
    },
    {
      "testName": "testHistoryOff",
      "testClass": "com.example.myapp.NotificationHistoryInstrumentedTest",
      "frameworkResult": "PASSED",
      "result": "PASSED",
      "durationSeconds": 1.598,
      "startTimestamp": "2026-08-05T20:38:54.531765Z",
      "endTimestamp": "2026-08-05T20:38:56.130032Z",
      "statusCode": 0,
      "current": 2,
      "numTests": 3
    },
    {
      "testName": "testConnect",
      "testClass": "com.example.myapp.WifiConnectInstrumentedTest",
      "frameworkResult": "FAILED",
      "result": "FAILED",
      "durationSeconds": 0.002,
      "startTimestamp": "2026-08-05T20:38:56.131857Z",
      "endTimestamp": "2026-08-05T20:38:56.133770Z",
      "stackTrace": "java.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\tat com.example.myapp.WifiConnectInstrumentedTest.testConnect(WifiConnectInstrumentedTest.java:93)\n\t...",
      "stream": "\nError in testConnect(com.example.myapp.WifiConnectInstrumentedTest):\njava.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\t...",
      "statusCode": -2,
      "current": 3,
      "numTests": 3
    }
  ],
  "errorMessage": "There was 1 failure:\n1) testConnect(com.example.myapp.WifiConnectInstrumentedTest)\njava.lang.NullPointerException: Attempt to invoke virtual method 'boolean androidx.test.uiautomator.UiDevice.pressHome()' on a null object reference\n\t...\nFAILURES!!!\nTests run: 3,  Failures: 1",
  "instrumentationCode": -1
}
```

The report contains the following top-level fields:

`version`  
The report schema version.

`jobArn`  
The ARN of the job.

`metrics`  
Aggregate results for the job. The `metrics` object contains the following fields:    
`testsTotal`  
The total number of tests in the job.  
`testsPassed`  
The number of tests that passed.  
`testsFailed`  
The number of tests that failed.  
`testsSkipped`  
The number of tests that were skipped.  
`testsErrored`  
The number of tests that errored.  
`testsOther`  
The number of tests with another result.  
`testsPassedPercentage`  
The percentage of tests that passed.  
`totalTestExecutionDurationSeconds`  
The total duration of all tests, in seconds.  
`medianTestExecutionDurationSeconds`  
The median duration of a test, in seconds.

`errorMessage`  
If the run had failures, an error message that summarizes them.

`instrumentationCode`  
The overall instrumentation exit code for the job.

`testDetails`  
A list of per-test results. Each entry in `testDetails` contains the following fields:    
`testName`  
The name of the test method.  
`testClass`  
The name of the test class.  
`result`  
The Device Farm result for the test.  
`frameworkResult`  
The result that the instrumentation framework reported. Device Farm maps this value to the normalized `result` field.  
`durationSeconds`  
The duration of the test, in seconds.  
`startTimestamp`  
The time when the test started.  
`endTimestamp`  
The time when the test ended.  
`current`  
The position of the test in the run.  
`numTests`  
The total number of tests in the run.  
`statusCode`  
The instrumentation status code that the test reported.  
`stream`  
A human-readable version of the instrumentation output for the test.  
`stackTrace`  
For a failed test, the stack trace of the failure.

## (Optional) Take screenshots in Android instrumentation tests
<a name="test-types-android-instrumentation-screenshots"></a>

You can take screenshots as part of your Android Instrumentation tests.

To take screenshots, call one of the following methods:
+ For Robotium, call the `takeScreenShot` method (for example, `solo.takeScreenShot();`).
+ For Spoon, call the `screenshot` method, for example:

  ```
  Spoon.screenshot(activity, "initial_state");
  /* Normal test code... */
  Spoon.screenshot(activity, "after_login");
  ```

During a test run, Device Farm gets screenshots from the following locations on the devices, if they exist, and then adds them to the test reports:
+ `/sdcard/robotium-screenshots`
+ `/sdcard/test-screenshots`
+ `/sdcard/Download/spoon-screenshots/{{test-class-name}}/{{test-method-name}}`
+ `/data/data/{{application-package-name}}/app_spoon-screenshots/{{test-class-name}}/{{test-method-name}}`