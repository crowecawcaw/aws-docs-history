

# Analyzing test results in AWS Device Farm
<a name="analyzing-results"></a>

With AWS Device Farm, you can choose from [two modes of execution](test-environments.md): standard and custom mode. Standard mode was designed to provide granular reporting as a replacement for any test report that you might generate. The report contains test artifacts, such as videos and logs, presented separately for each test. When you choose standard mode, Device Farm does not guarantee that the test execution sequence matches your local execution order. Because it involves post-processing for each test, standard mode typically takes longer to execute compared to your local execution.

In contrast, custom mode generates the same reports you create locally for any framework. It also provides an optional detailed Test Insights report for each job and run when using select frameworks such as Appium TestNG, Instrumentation, and XCUITest. Because it does not involve separating individual test artifacts, this mode maintains parity with local execution in test sequencing and execution time. The generation of Test Insights happens asynchronously after your tests are complete.

Standard mode is not recommended for new test projects. We recommend using custom mode with Test Insights instead because it is flexible and can replicate the reports that standard mode provides for supported frameworks. Test Insights helps you understand your test suite performance at both the job and run level.

Test Insights include the following information:
+ Passed, failed, skipped, and errored test counts for each job and for each run
+ Detailed test output with timestamps and stack traces for each test, where applicable
+ Median test execution time for each job, and median and average job execution duration for each run

Regardless of the mode you choose, Device Farm gathers artifacts you can download after your test run completes. These include device and test logs, test spec output, network TCP dump, and screenshots. This information can help you analyze how your app is behaving on real devices, identify issues or bugs, and diagnose problems.

**Topics**
+ [Viewing test reports in Device Farm](how-to-use-reports.md)
+ [Downloading artifacts in Device Farm](artifacts.md)