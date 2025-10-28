# Automatically merge individual build reports

In fanout batch builds, AWS CodeBuild supports automatic merging of individual build reports into a consolidated batch-level report. This feature provides
a comprehensive view of test results and code coverage across all builds within a batch.

## How it works

When executing `fanout` batch builds, each individual build generates [test reports](test-reporting.md "test-reporting.md"). CodeBuild then automatically
consolidates identical reports from different builds into a unified report, which is attached to the batch build. These consolidated reports are readily
accessible through the [BatchGetBuildBatches](../APIReference/API_BatchGetBuildBatches.md#CodeBuild-BatchGetBuildBatches-response-buildBatches "../APIReference/API_BatchGetBuildBatches.md#CodeBuild-BatchGetBuildBatches-response-buildBatches") API's `reportArns` field, and can also be viewed in the **Reports** tab of the console. This merging
capability extends to auto-discovered reports as well.

Consolidated reports are created under [report groups](test-report-group.md "test-report-group.md") that are either specified in the buildspec or auto-discovered by CodeBuild. You can analyze
trends of the merged reports directly under these report groups, providing valuable insights into the overall build performance and quality metrics across
historical builds of the same build-batch project.

For each individual build within the batch, CodeBuild automatically creates separate report groups. These follow a specific naming convention, combining the
batch build report group name with a suffix of `BuildFanoutShard<shard_number>`, where the `shard_number` represents the number of the shard in which the report
group is created. This organization allows you to track and analyze trends at both the consolidated and individual build levels, providing flexibility in
how you monitor and evaluate their build processes.

The batch-build report follows the same structure as [individual build reports](../APIReference/API_Report.md "../APIReference/API_Report.md").
The following key fields in the **Report** tab are specific to batch-build reports:

**Batch build report status**

The status of batch build reports follows specific rules depending on the report type:

- Test reports:
  - Succeeded: Status is set to succeeded when all individual build reports have succeeded.
  - Failed: Status is set to failed if any individual build report has failed.
  - Incomplete: Status is marked as incomplete if any individual build report is missing or has an incomplete status.

- Code coverage reports:
  - Complete: Status is set to complete when all individual build reports are complete.
  - Failed: Status is set to failed if any individual build report has failed.
  - Incomplete: Status is marked as incomplete if any individual build report is missing or has an incomplete status.

**Test summary**

The merged test report consolidates the following fields from all individual build reports:

- duration-in-nano-seconds: Maximum test duration time in nanoseconds among all individual build reports.
- total: The combined count of all test cases, summing the total number of tests from each build.
- status-counts: Provides a consolidated view of test statuses such as passed, failed, or skipped, calculated by
  aggregating the count of each status type across all individual builds.

**Code coverage summary**

The merged code coverage report combines fields from all individual builds using the following calculations:

- branches-covered: Sum of all covered branches from individual reports.
- branches-missed: Sum of all missed branches from individual reports.
- branch-coverage-percentage: `(Total covered branches / Total branches) * 100`
- lines-covered: Sum of all covered lines from individual reports.
- lines-missed: Sum of all missed lines from individual reports.
- lines-coverage-percentage: `(Total covered lines / Total lines) * 100`

**Execution ID**

The batch build ARN.

**Test cases**

The merged report contains a consolidated list of all test cases from individual builds, accessible through both the
[DescribeTestCases](../APIReference/API_DescribeTestCases.md "../APIReference/API_DescribeTestCases.md") API
and the batch build report in the console.

**Code coverages**

The merged code coverage report provides consolidated line and branch coverage information for each file across all individual builds,
accessible through both the [DescribeCodeCoverages](../APIReference/API_DescribeCodeCoverages.md "../APIReference/API_DescribeCodeCoverages.md")
API and the batch build report in the console. Note: For files covered by multiple test files distributed across different shards, the merged report
uses the following selection criteria:

1. Primary selection is based on the highest line coverage among shards.
2. If line coverage is equal across multiple shards, the shard with the highest branch coverage is selected.
