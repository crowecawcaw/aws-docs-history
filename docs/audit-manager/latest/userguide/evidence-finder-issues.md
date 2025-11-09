# Troubleshooting evidence finder issues

Use the information on this page to resolve common evidence finder issues in
Audit Manager.

###### General evidence finder issues

- [I can't
  enable evidence finder](#cannot-enable-evidence-finder "#cannot-enable-evidence-finder")
- [I enabled
  evidence finder, but I don't see past evidence in my search results](#cannot-see-past-evidence "#cannot-see-past-evidence")
- [I can't
  disable evidence finder](#cannot-disable-evidence-finder "#cannot-disable-evidence-finder")
- [My search query
  fails](#cannot-start-query "#cannot-start-query")
- [I see that a
  control domain is marked as “outdated”. What does this mean?](#outdated-control-domains "#outdated-control-domains")

###### Evidence finder assessment report issues

- [I can’t generate multiple assessment
  reports from my search results](#cannot-generate-multiple-reports-from-search-results "#cannot-generate-multiple-reports-from-search-results")
- [I can't include specific evidence from my
  search results](#cannot-add-individual-evidence "#cannot-add-individual-evidence")
- [Not all of my evidence finder results
  are included in the assessment report](#not-all-results-present-in-report "#not-all-results-present-in-report")
- [I
  want to generate an assessment report from my search results, but my query
  statement is failing](#querystatement-exceptions "#querystatement-exceptions")
- [Additional resources](#evidence-finder-assessment-report-see-also "#evidence-finder-assessment-report-see-also")

###### Evidence finder CSV export

issues

- [My CSV export
  failed](#export-checklist "#export-checklist")
- [I
  can't export specific evidence from my search results](#cannot-include-individual-evidence "#cannot-include-individual-evidence")
- [I can’t export multiple CSV files at
  once](#cannot-export-multiple-files-from-search-results "#cannot-export-multiple-files-from-search-results")

## I can't

enable evidence finder

Common reasons why you can't enable evidence finder include the following
situations:

**You're missing permissions**

If you’re trying to enable evidence finder for the first time, make
sure that you have the [required permissions to enable evidence finder](security_iam_id-based-policy-examples.md#full-administrator-access-enable-evidence-finder "security_iam_id-based-policy-examples.md#full-administrator-access-enable-evidence-finder"). These
permissions allow you to create and manage an event data store in CloudTrail
Lake, which is necessary to support evidence finder search queries. The
permissions also allow you to run search queries in evidence
finder.

If you need help with permissions, contact your AWS administrator.
If you’re an AWS administrator, you can copy the required permission
statement and [attach it to an IAM policy](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

**You're using your Organizations management account**

Keep in mind that you can't use your management account to enable
evidence finder. Sign in as the delegated administrator account, and try
again.

**You previously disabled evidence finder**

Re-enabling evidence finder isn't currently supported. If you
previously disabled evidence finder, you can't enable it again.

## I enabled

evidence finder, but I don't see past evidence in my search results

When you enable evidence finder, it takes up to 7 days for all of your past
evidence data to become available.

During this 7-day period, an event data store is backfilled with your past two
years’ worth of evidence data. This means that if you use evidence finder
immediately after you enable it, not all results are available until the backfill is
complete.

For instructions on how to check the status of the data backfill, see [Confirming the status of evidence
finder](confirm-status-of-evidence-finder.md "confirm-status-of-evidence-finder.md").

## I can't

disable evidence finder

This could be caused by one of the following reasons.

**You're missing permissions**

If you’re trying to disable evidence finder, make sure that you have
the [required permissions to disable evidence finder](security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder "security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder"). These
permissions allow you to update and delete an event data store in CloudTrail
Lake, which is necessary to disable evidence finder.

If you need help with permissions, contact your AWS administrator.
If you’re an AWS administrator, you can copy the required permission
statement and [attach it to an IAM policy](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

**A request to enable evidence finder is still in progress**

When you request to enable evidence finder, we create an event data
store to support evidence finder queries. You can't disable evidence
finder while the event data store is being created.

To proceed, wait until the event data store is created, and try again.
For more information, see [Confirming the status of evidence
finder](confirm-status-of-evidence-finder.md "confirm-status-of-evidence-finder.md").

**You already requested to disable evidence finder**

When you request to disable evidence finder, we delete the event data
store that's used for evidence finder queries. If you try again to
disable evidence finder while the event data store is being deleted, you
get an error message.

In this case, no action is needed. Wait for the event data store to be
deleted. As soon as this is complete, evidence finder is disabled. For
more information, see [Confirming the status of evidence
finder](confirm-status-of-evidence-finder.md "confirm-status-of-evidence-finder.md").

## My search query

fails

A failed search query could be caused by one of the following reasons.

**You're missing permissions**

Verify that the user has the [required permissions to run search queries](security_iam_id-based-policy-examples.md#evidence-finder-query-access "security_iam_id-based-policy-examples.md#evidence-finder-query-access") and access the
search results. Specifically, you need permissions for the following
CloudTrail actions:

- [StartQuery](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md")
- [DescribeQuery](../../../awscloudtrail/latest/APIReference/API_DescribeQuery.md "../../../awscloudtrail/latest/APIReference/API_DescribeQuery.md")
- [CancelQuery](../../../awscloudtrail/latest/APIReference/API_CancelQuery.md "../../../awscloudtrail/latest/APIReference/API_CancelQuery.md")
- [GetQueryResults](../../../awscloudtrail/latest/APIReference/API_GetQueryResults.md "../../../awscloudtrail/latest/APIReference/API_GetQueryResults.md")

If you need help with permissions, contact your AWS administrator.
If you’re an AWS administrator, you can copy the required permission
statement and [attach it to an IAM policy](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

**You're running the maximum number of queries**

You can run up to 5 queries at a time. If you're running the maximum
number of concurrent queries, this results in a
`MaxConcurrentQueriesException` error. If you get this
error message, wait a minute for some queries to finish, and then run
the query again.

**Your query statement has a validation error**

If you're using the API or CLI to perform the CloudTrail Lake [StartQuery](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md") operation, make sure that your
`queryStatement` is valid. If the query statement has
validation errors, incorrect syntax, or unsupported keywords, this
results in an `InvalidQueryStatementException`.

For more information about writing a query, see [Create or edit a query](../../../awscloudtrail/latest/userguide/query-create-edit-query.md "../../../awscloudtrail/latest/userguide/query-create-edit-query.md") in the _AWS CloudTrail User Guide_.

For examples of valid syntax, review the following query statement
examples that can be used to query an Audit Manager event data store.

###### Example 1: Investigate evidence and its compliance status

This example finds evidence with any compliance status across all
assessments in account, within a specified date range.

```
SELECT eventData.evidenceId, eventData.resourceArn, eventData.resourceComplianceCheck FROM $EDS_ID WHERE eventTime > '2022-11-02 00:00:00.000' AND eventTime < '2022-11-03 00:00:00.000'
```

###### Example 2: Determine non-compliant evidence for a control

This example finds all non-compliant evidence in a specified date
range for a specific assessment and control.

```
SELECT * FROM $EDS_ID WHERE eventData.assessmentId = '11aa33bb-55cc-77dd-99ee-ff22gg44hh66' AND eventTime > '2022-10-27 22:05:00.000' AND eventTime < '2022-11-03 22:05:00.000' AND eventData.resourceComplianceCheck IN ('NON_COMPLIANT','FAILED','WARNING') AND eventData.controlId IN ('aa11bb22-cc33-dd44-ee55-ff66gg77hh88')
```

###### Example 3: Count evidence by name

This example lists the total evidence for an assessment in a
specified date range, grouped by name and ordered by evidence count.

```
SELECT eventData.eventName as eventName, COUNT(*) as totalEvidence FROM  $EDS_ID WHERE eventData.assessmentId = '11aa33bb-55cc-77dd-99ee-ff22gg44hh66' AND eventTime > '2022-10-27 22:05:00.000' AND eventTime < '2022-11-03 22:05:00.000' GROUP BY eventData.eventName ORDER BY totalEvidence DESC
```

###### Example 4: Explore evidence by data source and service

This example finds all evidence in a specified date range for a
specific data source and service.

```
SELECT * FROM $EDS_ID WHERE eventTime > '2022-10-27 22:05:00.000' AND eventTime < '2022-11-03 22:05:00.000' AND eventData.service IN ('dynamodb') AND eventData.dataSource IN ('AWS API calls')
```

###### Example 5: Explore compliant evidence by data source and control

domain

This example finds compliant evidence for specific control
domains, where the evidence comes from a data source that isn't AWS
Config.

```
 SELECT * FROM $EDS_ID WHERE eventData.resourceComplianceCheck IN ('PASSED','COMPLIANT') AND eventData.controlDomainName IN ('Logging and monitoring','Data security and privacy') AND eventData.dataSource NOT IN ('AWS Config')
```

**Other API exceptions**

The [StartQuery](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md") API might fail for several other reasons. For a
complete list of possible errors and descriptions, see [StartQuery Errors](../../../awscloudtrail/latest/APIReference/API_StartQuery.md#API_StartQuery_Errors "../../../awscloudtrail/latest/APIReference/API_StartQuery.md#API_StartQuery_Errors") in the _AWS CloudTrail
API Reference._

## I see that a

control domain is marked as “outdated”. What does this mean?

When you apply a control domain filter in evidence finder, you might notice that
some available control domains are described as **Outdated**.

![Screenshot of an outdated control domain filter in evidence finder.](images/troubleshooting-outdated-control-domain-filter-console.png)

As of June 6, 2024, Audit Manager supports a new set of control domains provided by AWS
Control Catalog. To fetch a list of these control domains, see [ListDomains](../../../controlcatalog/latest/APIReference/API_ListDomains.md "../../../controlcatalog/latest/APIReference/API_ListDomains.md") in the _AWS Control Catalog API
Reference_.

If a control domain is marked as **Outdated**, this means that
the control domain you’re viewing isn’t one of the new control domains provided by
AWS Control Catalog. Audit Manager continues to support these outdated control domains so
that you can still use them as criteria when you search for evidence.

Although we continue to support the outdated control domains, we encourage you to
use the new control domains instead. The new control domains are mapped to the
updated standard controls that were launched as part of the common controls library
on June 6, 2024. On this date, we released updated standard controls that can
collect evidence from [AWS
managed sources](concepts.md#aws-managed-source "concepts.md#aws-managed-source"). This means that whenever there’s an update to the
underlying data sources for a common or core control, Audit Manager automatically applies the
same update to all related standard controls.

## I can’t generate multiple assessment

reports from my search results

This error is caused by running too many CloudTrail Lake queries at the same time.

This error can happen if you group your search results and attempt to immediately
generate assessment reports for each line item in your grouped results. When you get
your search results and generate an assessment report, each action invokes a query.
You can only run up to 5 queries at one time. If you’re running the maximum number
of concurrent queries, a `MaxConcurrentQueriesException` error is
returned.

To prevent this error, make sure that you aren’t generating too many assessment
reports at one time. If you’re running the maximum number of concurrent queries, a
`MaxConcurrentQueriesException` error is returned. If you get this
error message, wait a few minutes for your in-progress assessment reports to
complete.

You can check the status of your assessment reports from the download center page
in the Audit Manager console. After your reports are complete, return to your grouped results
in evidence finder. You can then continue to get the results and generate an
assessment report for each line item.

## I can't include specific evidence from my

search results

All of your search results are included in the assessment report. You can't
selectively add individual rows from your set of search results.

If you only want to include specific search results in the assessment report, we
recommend that you [edit your current search filters](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search"). This way, you can narrow down your
results to target only the evidence that you want to include in the report.

## Not all of my evidence finder results

are included in the assessment report

When you generate an assessment report, there are limits for how much evidence you
can add. The limit is based on the AWS Region of your assessment, the Region of
the S3 bucket that's used as your assessment report destination, and whether your
assessment uses a customer managed AWS KMS key.

1. The limit is 22,000 for same-Region reports (where the S3 bucket and
   assessment are in the same AWS Region)
2. The limit is 3,500 for cross-Region reports (where the S3 bucket and
   assessment are in different AWS Regions)
3. The limit is 3,500 if the assessment uses a customer managed
   KMS key

If you exceed this limit, the report is still created. However, Audit Manager adds only the
first 3,500 or 22,000 evidence items to the report.

To prevent this issue, we recommend that you [edit your current search filters](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search"). This way, you can reduce your search
results by targeting a smaller amount of evidence. If needed, you can repeat this
method and generate multiple assessment reports instead of one larger report.

## I

want to generate an assessment report from my search results, but my query
statement is failing

If you're using the [CreateAssessmentReport](../APIReference/API_CreateAssessmentReport.md "../APIReference/API_CreateAssessmentReport.md") API and your query statement returns a
validation exception, check the table below for guidance on how to fix it.

###### Note

Even if a query statement works in CloudTrail, the same query might not be valid for
assessment report generation in Audit Manager. This is because of some differences in
query validation between the two services.

| Clause     | Issue                                                                                                                                                                                                                                                                                                                                                                                                             | Solution                                                                                                                                                                                                                                                                                                                                                                                                                              | Notes                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SELECT`   | The `SELECT` clause contains a column name                                                                                                                                                                                                                                                                                                                                                                        | Remove the `SELECT` clause and replace with<br>`SELECT eventJson`.                                                                                                                                                                                                                                                                                                                                                                    | Only `SELECT eventJson` is supported.<br>This validation is handled by Audit Manager.                                                                                                                                                                                                                                                                              |
| `FROM`     | The `FROM` clause contains an invalid event data<br>store ID<br>or<br>The provided event data store ID doesn’t match the event data<br>store ID in your Audit Manager settings                                                                                                                                                                                                                                    | Remove the `FROM` clause and replace with<br>`FROM `edsID``, where<br>the value of `edsID` matches the event data store ID<br>that's specified in your Audit Manager settings.<br>You can retrieve the ARN of the event data store from your<br>Audit Manager settings. For more information, see [GetSettings](../APIReference/API_GetSettings.md "../APIReference/API_GetSettings.md") in the _AWS Audit Manager<br>API Reference_. | This validation is handled by Audit Manager.                                                                                                                                                                                                                                                                                                                       |
| `GROUP BY` | A `GROUP BY` clause is present in the query                                                                                                                                                                                                                                                                                                                                                                       | Remove the `GROUP BY` clause.                                                                                                                                                                                                                                                                                                                                                                                                         | This validation is handled by Audit Manager.                                                                                                                                                                                                                                                                                                                       |
| `HAVING`   | A `HAVING` clause is present in the query                                                                                                                                                                                                                                                                                                                                                                         | Remove the `HAVING` clause.                                                                                                                                                                                                                                                                                                                                                                                                           | This validation is handled by Audit Manager.                                                                                                                                                                                                                                                                                                                       |
| `LIMIT`    | The `LIMIT` clause contains a value that exceeds<br>the maximum allowed limit                                                                                                                                                                                                                                                                                                                                     | If the `LIMIT` clause exists, ensure that its value<br>is equal to or less than the maximum supported limit:<br>• For same-Region reports, the limit is 22,000<br>• For cross-Region reports, the limit is 3,500<br>• For reports where the related assessment uses a<br>customer managed AWS KMS key, the limit is 3,500                                                                                                             | In the console, there’s no limit to the number of evidence<br>results that can be returned. However, when generating an<br>assessment report, a limit applies to the amount of evidence<br>that you can include.If no `LIMIT` value<br>is provided in your query statement, the default maximum limits<br>are applied.This validation is handled by Audit Manager. |
| `ORDER BY` | The `ORDER BY` clause contains [Aggregate functions](../../../awscloudtrail/latest/userguide/query-limitations.md#query-aggregates-condition-operators "../../../awscloudtrail/latest/userguide/query-limitations.md#query-aggregates-condition-operators") or [Aliases](https://www.w3schools.com/sql/sql_alias.asp "https://www.w3schools.com/sql/sql_alias.asp") that aren’t present in the<br>`SELECT` clause | Ensure that the `ORDER BY` clause doesn’t contain<br>any conditions using [Aggregate functions](../../../awscloudtrail/latest/userguide/query-limitations.md#query-aggregates-condition-operators "../../../awscloudtrail/latest/userguide/query-limitations.md#query-aggregates-condition-operators") or [Aliases](https://www.w3schools.com/sql/sql_alias.asp "https://www.w3schools.com/sql/sql_alias.asp").                       | This validation is handled by the CloudTrail [StartQuery API.](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md")                                                                                                                                                                        |
| `WHERE`    | The `WHERE` clause contains more than one<br>`assessmentId`<br>or<br>The `WHERE` clause contains an<br>`assessmentId` that doesn’t match the<br>`assessmentId` in your<br>`createAssessmentReport` request<br>or<br>The `WHERE` clause contains an unsupported column<br>name                                                                                                                                     | Ensure that only one assessmentID is specified, and that it<br>matches the [assessmentId parameter](../APIReference/API_CreateAssessmentReport.md#auditmanager-CreateAssessmentReport-request-assessmentId "../APIReference/API_CreateAssessmentReport.md#auditmanager-CreateAssessmentReport-request-assessmentId") that you<br>specified in the `createAssessmentReport` API<br>request.<br>Remove any unsupported column names.    | This validation is handled by the CloudTrail [StartQuery API.](../../../awscloudtrail/latest/APIReference/API_StartQuery.md "../../../awscloudtrail/latest/APIReference/API_StartQuery.md")                                                                                                                                                                        |

### Examples

The following examples show how you can use the `queryStatement`
parameter when calling the [CreateAssessmentReport](../APIReference/API_CreateAssessmentReport.md "../APIReference/API_CreateAssessmentReport.md") operation. Before you
use these queries, replace the `placeholder text` with
your own `edsId` and `assessmentId` values.

###### Example 1: Create a report (same-Region limit applies)

This example creates a report that includes results for S3 buckets created
between January 22-23rd, 2022.

```
SELECT eventJson FROM `12345678-abcd-1234-abcd-123456789012` WHERE eventData.assessmentId = '`11aa33bb-55cc-77dd-99ee-ff22gg44hh66`' AND eventTime > '2022-01-22 00:00:00.000' AND eventTime < '2022-01-23 00:00:00.000' AND eventName='CreateBucket' LIMIT 22000
```

###### Example 2: Create a report (cross-Region limit applies)

This example creates a report that includes all results for the specified
event data store and assessment, with no date range specified.

```
SELECT eventJson FROM `12345678-abcd-1234-abcd-123456789012` WHERE eventData.assessmentId = '`11aa33bb-55cc-77dd-99ee-ff22gg44hh66`' LIMIT 7000
```

###### Example 3: Create a report (under the default limit)

This example creates a report that includes all results for the specified
event data store and assessment, with a limit that’s under the default
maximum.

```
SELECT eventJson FROM `12345678-abcd-1234-abcd-123456789012` WHERE eventData.assessmentId = '`11aa33bb-55cc-77dd-99ee-ff22gg44hh66`' LIMIT 2000
```

## Additional resources

The following page contains general troubleshooting guidance about assessment
reports:

- [Troubleshooting assessment report
  issues](assessment-report-issues.md "assessment-report-issues.md")

## My CSV export

failed

Your CSV export might fail for a number of reasons. You can troubleshoot this
issue by checking the most frequent causes.

First, make sure that you meet the prerequisites for using the CSV export
feature:

**You successfully enabled evidence
finder**

If you haven’t [enabled evidence finder](evidence-finder-settings-enable.md "evidence-finder-settings-enable.md"), you can’t run a search query and
export your search results.

**The backfill of your event data store is
complete**

If you use evidence finder immediately after you enable it, and the
[evidence backfill](evidence-finder.md#understanding-evidence-finder "evidence-finder.md#understanding-evidence-finder") is still in progress, there may be some
results that aren't available. To check the backfill status, see [Confirming the status of evidence
finder](confirm-status-of-evidence-finder.md "confirm-status-of-evidence-finder.md").

**Your search query succeeded**

Audit Manager can't export the results of a failed query. To troubleshoot a
failed query, see [My search query
fails](#cannot-start-query "#cannot-start-query").

After you've confirmed that you meet the prerequisites, use the following
checklist to check for potential issues:

1. Check the status of your search query:
   1. **Was the query cancelled?** Evidence
      finder displays partial results that were processed before the query
      was cancelled. However, Audit Manager doesn't export partial results to your
      S3 bucket or the download center.
   2. **Has the query been running for over one
      hour?** Queries that run for longer than one hour might
      time out. Evidence finder displays partial results that were
      processed before the query timed out. However, Audit Manager doesn’t export
      partial results. To avoid a timeout, you can reduce the amount of
      evidence that’s scanned by [Editing search filters](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search") to specify a narrower time
      range.

2. Check the name and the URI of your export destination S3 bucket:
   1. **Does the bucket that you specified
      exist?** If you manually entered a bucket URI, make
      sure that you didn't mistype anything. A typo or an incorrect URI
      can result in a `RESOURCE_NOT_FOUND` error when Audit Manager
      attempts to export the CSV file to Amazon S3.

3. Check the permissions of your export destination S3 bucket:
   1. **Do you have write permissions for the S3
      bucket?** You must have write access for the S3 bucket
      that you're using as the export destination. More specifically, the
      IAM permissions policy must include an `s3:PutObject`
      action and the bucket ARN, and list CloudTrail as the service principal.
      We provide an [example policy](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md") that you can use.

4. Check if any of your AWS Region information doesn't match up:
   1. **Does the AWS Region of your customer managed key
      match the AWS Region of your assessment?** If you
      provided a customer managed key for data encryption, it must be in the same
      AWS Region as your assessment. For instructions on how to change
      the KMS key, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").

5. Check the permissions of your delegated administrator account:
   1. **Does the customer managed key in your Audit Manager settings
      grant permissions to your delegated administrator?** If
      you're using a delegated administrator account and you specified a
      customer managed key for data encryption, make sure the delegated
      administrator has access on that KMS key. For instructions, see
      [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in
      the _AWS Key Management Service Developer Guide._ To
      review and change your encryption settings in Audit Manager, see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").

###### Note

If you change your Audit Manager data encryption settings, these changes apply to new
assessments that you create moving forward. This includes any CSV files that you
export from your new assessments.

The changes don't apply to existing assessments that you created before you
changed your encryption settings. This includes new CSV exports from existing
assessments, in addition to existing CSV exports. Existing assessments—and all
their CSV exports—continue to use the old KMS key. If the IAM identity
that’s exporting the CSV file doesn’t have permissions to use the old KMS key,
you can grant permissions at the key policy level.

## I

can't export specific evidence from my search results

All of your search results are included in the results.

If you want to include only specific evidence in the CSV file, we recommend that
you [edit your current search filters](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search"). This way, you can narrow your results
to target only the evidence that you want to export.

## I can’t export multiple CSV files at

once

This error is caused by running too many CloudTrail Lake queries at the same time.

This can happen if you group your search results and attempt to immediately export
a CSV file for each line item in your grouped results. When you get your search
results and export a CSV file, each of these actions invokes a query. You can run
only up to five queries at one time. If you’re running the maximum number of
concurrent queries, a `MaxConcurrentQueriesException` error is returned.

To prevent this error, make sure that you aren’t exporting too many CSV files at
one time.

To resolve this error, wait for your in-progress CSV exports to complete. Most
exports take a few minutes. However, if you're exporting a very large amount of
data, it might take up to an hour to complete the export. Feel free to navigate away
from evidence finder while the export is in progress.

You can check the export status from the download center in the Audit Manager console.
After your exported files are ready, return to your grouped results in evidence
finder. You can then continue to get the results and export a CSV file for each line
item.
