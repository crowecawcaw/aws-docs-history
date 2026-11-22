

# Reports in AWS Device Farm

The following sections provide information about Device Farm test reports.

**Topics**
+ [Report retention](#reports-retention)
+ [Report components](#reports-components)
+ [Logs in reports](#reports-logs)
+ [Common tasks for reports](#reports-tasks)

## Report retention
<a name="reports-retention"></a>

Device Farm stores your reports for 400 days. These reports include metadata, logs, and screenshots.

## Report components
<a name="reports-components"></a>

Reports in Device Farm contain pass and fail information, crash reports, test and device logs, and screenshots. The report includes detailed per-device data and high-level results, such as the number of occurrences of a given problem.

### Test Insights
<a name="reports-test-insights"></a>

Device Farm generates a **Test Insights** report by default for each run in a custom test environment that uses one of the following frameworks:
+ Appium Java JUnit
+ Appium Java TestNG
+ Appium Node.js
+ Appium Python
+ Android Instrumentation
+ XCTest UI

This includes Appium web app tests. Appium Ruby tests are not supported. The report includes the following information:
+ Passed, failed, skipped, and errored test counts for each job and for each run
+ Detailed test output with timestamps and stack traces for each test, where applicable
+ Median test execution time for each job, and median and average job execution duration for each run

Test Insights helps you understand your test suite performance at both the job and run level. With Test Insights, you get the detailed test reporting of standard mode combined with the faster execution speed of custom mode. For more information about test environments, see [Test environments in AWS Device Farm](test-environments.md).

To configure your tests for Test Insights, see the test report section for your framework:
+ [Configure Appium test reports using a custom test environment](test-types-appium-integrate.md#test-types-appium-generate-reports)
+ [Configure instrumentation test reports using a custom test environment](test-types-android-instrumentation-integrate.md#test-types-android-instrumentation-generate-reports)
+ [Configure XCTest UI test reports using a custom test environment](test-types-ios-xctest-ui.md#test-types-ios-xctest-ui-generate-reports)

To turn off Test Insights for a run, see [Creating a test run in Device Farm](how-to-create-test-run.md).

#### Per-test video
<a name="reports-test-insights-video"></a>

When a run records video, Test Insights also include per-test video: where each test starts and ends in the job video. On the console, you can play the video from any test in the test report. In the test report JSON, the `videoStartSeconds` and `videoEndSeconds` fields give each test's position in the video.

A job gets per-test video when all of the following are true:
+ The run records video. Video capture is on by default. For more information, see [Creating a test run in Device Farm](how-to-create-test-run.md).
+ Your test framework records a start time for each test. Appium Java TestNG, Android Instrumentation, and XCTest UI tests record start times without any changes. Appium Java JUnit tests record start times if Device Farm finds a test report file. Appium Node.js tests need the WebdriverIO JSON reporter. Appium Python tests need the `conftest.py` code that records start and end times. For more information, see [Configure Appium test reports using a custom test environment](test-types-appium-integrate.md#test-types-appium-generate-reports).
+ The job produces a single video file for its tests.

For instructions on how to play a test's video on the console, see [Watch a test in the job video](#reports-test-insights-video-console).

#### Watch a test in the job video
<a name="reports-test-insights-video-console"></a>

When a job has Test Insights and a video, you can play the video from any test in the job's test report. For information about the requirements, see [Per-test video](#reports-test-insights-video).

1. Open the job. On the job details page, choose the **Test report** tab.

1. In the **Video** column, choose the play button for a test.

   The **Test video** panel opens beside the test report and plays the job video from the start of that test. The following screenshot shows the test report on the left, with the selected test's name in bold. On the right, the panel shows a card for each test, the video, and the seek bar. The panel also has the **This test** and **Whole video** views, and the download and full-screen buttons.  
![The Test video panel beside the test report, with the selected test's card highlighted and This test selected.](https://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-test-insights/console-test-report-video-panel.png)

1. Choose the close button in the top right corner of the panel to close it.

The panel has two views:

**This test**  
Plays only the selected test. The seek bar covers that test, playback stops at its end, and the bar is red if the test failed.

**Whole video**  
Plays the full recording and keeps playing from one test into the next. The seek bar covers the whole video. As playback reaches each test, that test becomes the selected test.

In both views, the selected test's name is bold in the test report and its card is highlighted at the top of the panel. You can go to any test at any time:
+ To play a test, choose its card at the top of the panel or its play button in the test report. The cards list the tests in the order that they ran, with each test's result.
+ To move to the previous or next test, choose the previous or next button.
+ To go to a point in the video, choose it on the seek bar. When the seek bar has keyboard focus, the arrow keys move 5 seconds. Shift with an arrow key moves to the previous or next test. Home and End go to the start and end.
+ To watch in full screen, choose the full-screen button. To save the recording, choose the download button, which opens it in a new browser tab.

While the panel is open, the test report hides some columns so that it fits beside the video. For example, it hides the test class and the start and end times. As the video plays, the test report scrolls to the row of the selected test. If you close the panel, choosing a play button again reopens it without downloading the video again. To watch the whole recording without the test report, use the job's **Video** tab.

## Logs in reports
<a name="reports-logs"></a>

Reports include complete logcat captures for Android tests and complete Device Console logs for iOS tests.

## Common tasks for reports
<a name="reports-tasks"></a>

For more information, see [Viewing test reports in Device Farm](how-to-use-reports.md).