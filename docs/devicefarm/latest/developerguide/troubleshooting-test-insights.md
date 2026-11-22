

# Troubleshooting test reports and insights in AWS Device Farm

When test insights are enabled, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating test insights.

Web app tests use the same reports as mobile app tests, so the same messages can occur.

**Topics**
+ [The job did not run to completion](#ti-job-not-complete)
+ [The results contained no test cases](#ti-no-test-cases)
+ [The test output exceeds the maximum supported size](#ti-output-too-large)
+ [The test results were not found](#ti-results-not-found)
+ [The test report could not be processed](#ti-report-error)
+ [The test output archive is not a valid zip file](#ti-invalid-archive)
+ [A service error occurred](#ti-service-error)

## The job did not run to completion
<a name="ti-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

## The results contained no test cases
<a name="ti-no-test-cases"></a>

`Test insights could not be generated. The {{results}} was parsed successfully but contained no test cases.`

For some test types, the message continues: `Verify that your test suite includes at least one test case and that the {{results}} is stored correctly in the output artifacts directory.`

The value of {{results}} depends on the test type.


| Test type | {{results}} | 
| --- | --- | 
| Appium Java JUnit | JUnit XML | 
| Appium Java TestNG | testng-results.xml file | 
| Appium Python | pytest JUnit XML | 
| Appium Node.js | WebdriverIO JSON report, or WebdriverIO JUnit report when Device Farm read a JUnit report | 
| Instrumentation | test spec output file | 
| XCTest UI | xcresult\_summary.json file | 

The results artifact parsed successfully but contained zero test cases.

To resolve this issue, verify that your test suite includes at least one test case and that results are stored correctly under `$DEVICEFARM_LOG_DIR`.

### JUnit XML report (Appium Java JUnit)
<a name="ti-appium-java-junit-no-test-cases"></a>

This happens most often when the selector you passed to the JUnit Platform matched no tests, for example a package or tag that none of your tests carries.

To resolve this issue, verify that your selector matches at least one test and that the reports are under `$DEVICEFARM_LOG_DIR`.

### pytest JUnit XML report (Appium Python)
<a name="ti-appium-python-no-test-cases"></a>

To resolve this issue, verify that pytest collects at least one test from the paths in your test spec. A `-k` or `-m` expression that matches no test produces a report with no test cases.

### WebdriverIO report (Appium Node.js)
<a name="ti-appium-node-no-test-cases"></a>

To resolve this issue, verify that your spec files match your `specs` pattern in `wdio.conf.js`, and that at least one test ran. A job in which every spec file failed to load produces a report with no test cases.

## The test output exceeds the maximum supported size
<a name="ti-output-too-large"></a>

`Unable to generate test insights: {{output}} exceeds the maximum supported size of {{size}}.`

The values of {{output}} and {{size}} depend on the test type.


| Test type | {{output}} | {{size}} | 
| --- | --- | --- | 
| Appium Java JUnit | "JUnit XML" | 1GB | 
| Appium Java TestNG | test output "testng-results.xml" | 1GB | 
| Appium Python | "pytest JUnit XML" | 250MB | 
| Appium Node.js (report) | "WebdriverIO JSON report", or "WebdriverIO JUnit report" when the oversized file is a JUnit report | 250MB | 
| Appium Node.js (archive) | "test output archive" | 1GB | 
| Instrumentation | test output "test spec output" | 1GB | 
| XCTest UI | test output "xcresult bundle" | 1GB | 

### JUnit XML report (Appium Java JUnit)
<a name="ti-appium-java-junit-output-too-large"></a>

The collected JUnit XML reports are larger than 1 GB in total.

To resolve this issue, reduce the report size to less than 1 GB. To reduce the size, write less output to `system-out` and `system-err`. The JUnit XML format embeds that output in the report.

### `testng-results.xml` (Appium Java TestNG)
<a name="ti-appium-java-testng-output-too-large"></a>

The testng-results.xml is larger than 1 GB.

To resolve this issue, reduce the testng-results.xml size to below 1 GB by trimming logs or attachments.

### pytest JUnit XML report (Appium Python)
<a name="ti-appium-python-report-too-large"></a>

The only report that Device Farm found in your test output artifacts is larger than 250 MB, so it could not be read. If the archive holds another readable report, Device Farm uses that report and ignores the oversized one, and this message does not appear.

To resolve this issue, reduce the size of the report. Captured output and long tracebacks are the usual causes. Remove the `junit_logging` setting if you set it, and consider the `--tb=short` option.

### WebdriverIO report (Appium Node.js)
<a name="ti-appium-node-report-too-large"></a>

The size of a single report file in your test output artifacts is larger than 250 MB.

To resolve this issue, reduce the size of the report. A very high test count and long stack traces are the usual causes. Splitting your suite across more spec files also helps, because each WebdriverIO runner writes its own report file.

### Test output archive (Appium Node.js)
<a name="ti-appium-node-archive-too-large"></a>

The size of the archive (zip file) that contains your test output artifacts is larger than 1 GB, so Device Farm could not download it to search for a report. Your test artifacts are still available in the console and through the API.

To resolve this issue, reduce what your tests write to `$DEVICEFARM_LOG_DIR`. Screenshots and full browser logs for every test are the usual cause.

### Test spec output (instrumentation)
<a name="ti-instrumentation-output-too-large"></a>

The test spec output is larger than 1 GB.

To resolve this issue, investigate commands that are generating large numbers of lines in your test spec output. Then, remove or modify them.

### `.xcresult` bundle (XCTest UI)
<a name="ti-xctest-ui-output-too-large"></a>

The xcresult bundle is larger than 1 GB.

To resolve this issue, reduce the xcresult bundle size to below 1 GB by trimming logs or attachments.

## The test results were not found
<a name="ti-results-not-found"></a>

Device Farm could not find test results to summarize. The message depends on the test type.

### JUnit XML report (Appium Java JUnit)
<a name="ti-appium-java-junit-report-not-found"></a>

`Unable to generate test insights. The JUnit XML test results file was not found in the output artifacts. Ensure your test framework is configured to produce JUnit XML reports and that the results are written to the artifacts directory.`

`$DEVICEFARM_LOG_DIR` contained no JUnit XML report. JUnit doesn't use a standard report file name, so Device Farm looks for every JUnit XML report under `$DEVICEFARM_LOG_DIR`. A run that prints its results to the console only, without writing a report file, or that writes the report somewhere else, produces nothing to summarize.

To resolve this issue, configure your run to write a report under `$DEVICEFARM_LOG_DIR`. Pass `--reports-dir` on a Console Launcher command, or copy the build tool's own report directory into `$DEVICEFARM_LOG_DIR` in the `post_test` phase of your test spec file. For the options, see [Configure Appium test reports using a custom test environment](test-types-appium-integrate.md#test-types-appium-generate-reports).

### `testng-results.xml` (Appium Java TestNG)
<a name="ti-appium-java-testng-testng-xml-not-found"></a>

`Unable to generate test insights. The test results file (testng-results.xml) was not found.`

No `testng-results.xml` file (and no XML entry with the TestNG root signature) was found.

To resolve this issue, configure your framework to emit TestNG XML into the artifacts directory (`$DEVICEFARM_LOG_DIR`).

### pytest JUnit XML report (Appium Python)
<a name="ti-appium-python-no-report"></a>

`Unable to generate test insights. No JUnit XML test results file was found in the output artifacts. Run pytest with --junit-xml and write the report under $DEVICEFARM_LOG_DIR, for example --junit-xml $DEVICEFARM_LOG_DIR/junitreport.xml. Any filename works.`

Device Farm searched your test output artifacts and found no pytest report.

To resolve this issue, check the following:
+ Your test spec runs pytest with the `--junit-xml` option.
+ The report path is under `$DEVICEFARM_LOG_DIR`, and the file name ends in `.xml`.
+ The test session ran to the end. pytest writes the report when the session finishes, so a session that stops early, for example at the job timeout, writes no report. A `conftest.py` that fails to import stops the session before any test runs.

### WebdriverIO report (Appium Node.js)
<a name="ti-appium-node-no-supported-report"></a>

`Unable to generate test insights. No supported WebdriverIO test report was found in the artifact directory. Refer to our documentation to find the supported test report outputs and the steps to generate them.`

Device Farm searched your test output artifacts and found no report that it can read.

To resolve this issue, check the following:
+ Your `wdio.conf.js` file enables either [@wdio/json-reporter](https://webdriver.io/docs/json-reporter/) or [@wdio/junit-reporter](https://webdriver.io/docs/junit-reporter/). The `spec` reporter writes to the console only, so it produces no file to read.
+ The reporter's `outputDir` is a directory under `$DEVICEFARM_LOG_DIR`.
+ The report file name ends in `.json` for the JSON reporter, or `.xml` or `.log` for the JUnit reporter. If you set `outputFileFormat`, keep one of these extensions; Device Farm does not open files with any other extension.

### Test spec output (instrumentation)
<a name="ti-instrumentation-no-instrumentation-output"></a>

`Unable to generate test insights. No instrumentation test output was found in the test spec output file.`

The test spec output file was present but contained no instrumentation output lines.

To resolve this issue, ensure that your framework emits instrumentation output to `stdout` in the test spec file.

### `.xcresult` bundle (XCTest UI)
<a name="ti-xctest-ui-xcresult-not-found"></a>

`Unable to generate test insights. The xctestresult bundle file (.xcresult) was not found in the output artifacts.`

Device Farm could not find an `.xcresult` bundle for this job, so there were no results to summarize.

Device Farm looks for the bundle anywhere under `$DEVICEFARM_DERIVED_DATA_PATH`. The default XCTest UI test spec produces it there automatically, so this message usually indicates that a customized test spec did not write results to that location.

To confirm whether a bundle was produced, download the customer artifacts for the job and look for an `.xcresult` directory under the derived data folder.

## The test report could not be processed
<a name="ti-report-error"></a>

The message depends on the test type:
+ Appium Java JUnit and Appium Python:

  `Test insights could not be generated due to an error while processing the {{report}} report. Ensure the file is well-formed XML in the standard JUnit report format.`

  Where {{report}} is `JUnit XML` (Appium Java JUnit) or `pytest JUnit XML` (Appium Python).
+ Appium Java TestNG and XCTest UI:

  `Test insights could not be generated because of an error while processing {{results}}.`

  Where {{results}} is `testng-results.xml` (Appium Java TestNG) or `the .xcresult test results` (XCTest UI).
+ Appium Node.js:

  `Unable to generate test insights. An error occurred while processing the test report in your output artifacts. To resolve the error, ensure that your WebdriverIO reporter generated a valid report. Refer to our documentation for the prerequisites to generate test insights.`

### JUnit XML report (Appium Java JUnit)
<a name="ti-appium-java-junit-report-error"></a>

The report was malformed or could not be parsed. If a run stops partway through, the report can be truncated.

To resolve this issue, verify that the file is well-formed XML in the standard JUnit report format. If your run writes several reports and only one is malformed, Device Farm reports the tests from the others, so this message means that no report could be read.

### `testng-results.xml` (Appium Java TestNG)
<a name="ti-appium-java-testng-testng-xml-error"></a>

The XML file was malformed or could not be parsed.

To resolve this issue, ensure that the file is a well-formed XML in the standard TestNG report format.

### pytest JUnit XML report (Appium Python)
<a name="ti-appium-python-report-error"></a>

Device Farm found one or more reports but could not read any of them. If some reports can be read, Device Farm uses those and skips the rest, so this message means that none could be read. The usual cause is a report that was truncated or rewritten after pytest wrote it.

To resolve this issue, verify that your test spec does not move, rewrite, or compress the report after pytest writes it.

### WebdriverIO report (Appium Node.js)
<a name="ti-appium-node-report-error"></a>

Device Farm found a report but could not read it. The usual cause is a truncated file, which happens when the test process is killed before the reporter finishes writing.

To resolve this issue, verify that your tests run to completion within your job timeout, and that your test spec does not move, rewrite, or compress the report after the reporter writes it.

### `.xcresult` bundle (XCTest UI)
<a name="ti-xctest-ui-xcresult-error"></a>

Device Farm found an `.xcresult` bundle but could not read the test results from it.

To resolve this issue, ensure that your test run produces a valid `.xcresult` bundle. Verify that your test spec does not modify, truncate, or archive the bundle before the run finishes, and that the **xcodebuild** command completes rather than being interrupted by a timeout.

## The test output archive is not a valid zip file
<a name="ti-invalid-archive"></a>

`Unable to generate test insights: the test output archive could not be processed because it is not a valid zip file.`

The archive (zip file) that contains your test output artifacts could not be opened.

To resolve this issue, retry the run. If the error persists, contact AWS Support.

## A service error occurred
<a name="ti-service-error"></a>

`Test insights could not be generated due to a service error.`

Device Farm could not collect the artifacts it needs to summarize the job.

To resolve this issue, retry the run. If the error persists, contact AWS Support.

### Test output archive (Appium Python)
<a name="ti-appium-python-service-error"></a>

This message also appears when the archive (zip file) that contains your test output artifacts is larger than 1 GB.

To resolve this issue, reduce what your tests write to `$DEVICEFARM_LOG_DIR`, and retry the run. If the error persists, contact AWS Support.