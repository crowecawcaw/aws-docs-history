

# Troubleshooting Appium Node.js tests in AWS Device Farm
<a name="troubleshooting-appium-node"></a>

## Test insights
<a name="troubleshooting-appium-node-insights"></a>

When you opt in to test insights, Device Farm generates a summarized report for your run and each job under it. If the service cannot generate the report, the insights report status is `SKIPPED` or `ERRORED`, and the report message explains why. The following messages can occur when generating insights for Appium Node.js tests.

### The job did not run to completion
<a name="ti-appium-node-job-not-complete"></a>

`Unable to generate test insights because the job was {{status}}.`

The job ended in a non-successful state (where {{status}} is `STOPPED`, `ERRORED`, or `SKIPPED`), so there was no result to summarize. A run that ends in a failed state still receives insights.

To resolve this issue, investigate why the job did not run to completion. In many cases, the `message` field of the job itself might explain why the job didn't complete.

### No supported WebdriverIO test report was found
<a name="ti-appium-node-no-supported-report"></a>

`Unable to generate test insights. No supported WebdriverIO test report was found in the artifact directory. Refer to our documentation to find the supported test report outputs and the steps to generate them.`

Device Farm searched your test output artifacts and found no report that it can read.

To resolve this issue, check the following:
+ Your `wdio.conf.js` file enables either [@wdio/json-reporter](https://webdriver.io/docs/json-reporter/) or [@wdio/junit-reporter](https://webdriver.io/docs/junit-reporter/). The `spec` reporter writes to the console only, so it produces no file to read.
+ The reporter's `outputDir` is a directory under `$DEVICEFARM_LOG_DIR`.
+ The report file name ends in `.json` for the JSON reporter, or `.xml` or `.log` for the JUnit reporter. If you set `outputFileFormat`, keep one of these extensions; Device Farm does not open files with any other extension.

### The test report could not be processed
<a name="ti-appium-node-report-error"></a>

`Unable to generate test insights. An error occurred while processing the test report in your output artifacts. To resolve the error, ensure that your WebdriverIO reporter generated a valid report. Refer to our documentation for the prerequisites to generate test insights.`

Device Farm found a report but could not read it. The usual cause is a truncated file, which happens when the test process is killed before the reporter finishes writing.

To resolve this issue, verify that your tests run to completion within your job timeout, and that your test spec does not move, rewrite, or compress the report after the reporter writes it.

### The results contained no test cases
<a name="ti-appium-node-no-test-cases"></a>

`Test insights could not be generated. The WebdriverIO JSON report was parsed successfully but contained no test cases. Verify that your test suite includes at least one test case and that the WebdriverIO JSON report is stored correctly in the output artifacts directory.`

The report parsed successfully but contained zero test cases. The message names the WebdriverIO JUnit report instead when Device Farm read a JUnit report.

To resolve this issue, verify that your spec files match your `specs` pattern in `wdio.conf.js`, and that at least one test ran. A job in which every spec file failed to load produces a report with no test cases.

### The test report exceeds the maximum supported size
<a name="ti-appium-node-report-too-large"></a>

`Unable to generate test insights: "WebdriverIO JSON report" exceeds the maximum supported size of 250MB.`

The size of a single report file in your test output artifacts is larger than 250 MB. The message names the WebdriverIO JUnit report instead when the oversized file is a JUnit report.

To resolve this issue, reduce the size of the report. A very high test count and long stack traces are the usual causes. Splitting your suite across more spec files also helps, because each WebdriverIO runner writes its own report file.

### The test output archive exceeds the maximum supported size
<a name="ti-appium-node-archive-too-large"></a>

`Unable to generate test insights: "test output archive" exceeds the maximum supported size of 1GB.`

The size of the archive (zip file) that contains your test output artifacts is larger than 1 GB, so Device Farm could not download it to search for a report. Your test artifacts are still available in the console and through the API.

To resolve this issue, reduce what your tests write to `$DEVICEFARM_LOG_DIR`. Screenshots and full browser logs for every test are the usual cause.

### The test output archive is not a valid zip file
<a name="ti-appium-node-invalid-archive"></a>

`Unable to generate test insights: the test output archive could not be processed because it is not a valid zip file.`

The archive (zip file) that contains your test output artifacts could not be opened.

To resolve this issue, retry the run. If the error persists, contact AWS Support.

### A service error occurred
<a name="ti-appium-node-service-error"></a>

`Test insights could not be generated due to a service error.`

Device Farm could not collect the artifacts it needs to summarize the job.

To resolve this issue, retry the run. If the error persists, contact AWS Support.