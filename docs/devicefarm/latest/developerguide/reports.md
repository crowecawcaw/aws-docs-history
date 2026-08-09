# Reports in AWS Device Farm

The following sections provide information about Device Farm test reports.

###### Topics

- [Report retention](#reports-retention "#reports-retention")
- [Report components](#reports-components "#reports-components")
- [Logs in reports](#reports-logs "#reports-logs")
- [Common tasks for reports](#reports-tasks "#reports-tasks")

## Report retention

Device Farm stores your reports for 400 days. These reports include metadata, logs, and
screenshots.

## Report components

Reports in Device Farm contain pass and fail information, crash reports, test and device
logs, and screenshots. The report includes detailed per-device data and high-level
results, such as the number of occurrences of a given problem.

### Test Insights

For supported frameworks such as Appium TestNG, XCUI, and Instrumentation, Device Farm
provides an optional **Test Insights** report. Test Insights include the following
information:

- Passed, failed, skipped, and errored test counts for each job and for each run
- Detailed test output with timestamps and stack traces for each
  test, where applicable
- Median test execution time for each job, and median and average job execution duration for each run

Test Insights helps you understand your test suite performance at both the job and
run level. With Test Insights, you get the detailed test reporting of standard mode
combined with the faster execution speed of custom mode. For more information about
test environments, see [Test environments in AWS Device Farm](test-environments.md "test-environments.md").

To schedule a run with Test Insights, see [Step 3: Create and start a run](getting-started.md#getting-started-create-run "getting-started.md#getting-started-create-run").

## Logs in reports

Reports include complete logcat captures for Android tests and complete Device Console
logs for iOS tests.

## Common tasks for reports

For more information, see [Viewing test reports in Device Farm](how-to-use-reports.md "how-to-use-reports.md").
