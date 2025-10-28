# Reviewing coverage data for automated sensitive data discovery

To review and assess coverage by automated sensitive data discovery, you can use the Amazon Macie console or the
Amazon Macie API. Both the console and the API provide data that indicates the current status of the
analyses for your Amazon Simple Storage Service (Amazon S3) general purpose buckets in the current AWS Region. The data
includes information about issues that create gaps in the analyses:

- Buckets that Macie isn't allowed to access. Macie can't analyze any objects in these
  buckets. The buckets' permissions settings prevent Macie from accessing the buckets and the
  buckets' objects.
- Buckets that don't store any classifiable objects. Macie can't analyze any objects in
  these buckets. All the objects use Amazon S3 storage classes that Macie doesn't support, or they
  have file name extensions for file or storage formats that Macie doesn't support.
- Buckets that Macie hasn’t been able to analyze yet due to object-level classification
  errors. Macie attempted to analyze one or more objects in these buckets. However, Macie
  couldn't analyze the objects due to issues with object-level permissions settings, object
  content, or quotas.
  Coverage data is updated as automated sensitive data discovery progresses each day. If you're the Macie administrator for an
  organization, the data includes information for S3 buckets that your member accounts own.

###### Note

Coverage data doesn't explicitly include results for sensitive data discovery jobs that you create and
run. However, remediating coverage issues that affect automated sensitive data discovery is likely to also increase
coverage by jobs that you subsequently run. To assess coverage for a job, [review the job's results](discovery-jobs-manage-results.md "discovery-jobs-manage-results.md"). If a job's log events
or other results indicate coverage issues, [remediation guidance for automated sensitive data discovery](discovery-coverage-remediate.md "discovery-coverage-remediate.md") can help you address some of the issues.

###### To review coverage data for automated sensitive data discovery

To review coverage data for automated sensitive data discovery, you can use the Amazon Macie console or the Amazon Macie
API. On the console, a single page provides a unified view of coverage data for all of your S3
general purpose buckets in the current Region. This includes a rollup of issues that recently
occurred for each bucket. The page also provides options for reviewing groups of data by issue
type. To track your investigation of issues for specific buckets, you can export data from the
page to a comma-separated values (CSV) file.

Console
Follow these steps to review coverage data by using the Amazon Macie console.

###### To review coverage data

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, choose **Resource coverage**.
3. On the **Resource coverage** page, choose the tab for the type of
   coverage data that you want to review:
   - **All** – Lists all the buckets for your account. For each
     bucket, the **Issues** field indicates whether issues prevented Macie
     from analyzing objects in the bucket. If the value for this field is
     **None**, Macie has analyzed at least one of the bucket's objects or
     Macie hasn't attempted to analyze any of the bucket's objects yet. If there are issues,
     this field indicates the nature of the issues and how to remediate them. For object-level
     classification errors, it might also indicate (in parentheses) the number of occurrences
     of the error.
   - **Access denied** – Lists buckets that Macie isn't allowed to
     access. The permissions settings for these buckets prevent Macie from accessing the
     buckets and the buckets' objects. Consequently, Macie can't analyze any objects in the
     buckets.
   - **Classification error** – Lists buckets that Macie hasn’t
     analyzed yet due to object-level classification errors—issues with object-level
     permissions settings, object content, or quotas. For each bucket, the
     **Issues** field indicates the nature of each type of error that
     occurred and prevented Macie from analyzing an object in the bucket. It also indicates how
     to remediate each type of error. Depending on the error, it might also indicate (in
     parentheses) the number of occurrences of the error.
   - **Unclassifiable** – Lists buckets that Macie can't analyze
     because they don't store any classifiable objects. All the objects in these buckets use
     unsupported Amazon S3 storage classes or they have file name extensions for unsupported file or
     storage formats. Consequently, Macie can't analyze any objects in the buckets.

4. To drill down and review the supporting data for a bucket, choose the bucket's name.
   Then refer to the details panel for statistics and other information about the
   bucket.
5. To export the table to a CSV file, choose **Export to CSV** at the top
   of the page. The resulting CSV file contains a subset of metadata for each bucket in the
   table, for up to 50,000 buckets. The file includes a **Coverage issues**
   field. The value for this field indicates whether issues prevented Macie from analyzing
   objects in the bucket and, if so, the nature of the issues.

API
To review coverage data programmatically, specify filter criteria in queries that you
submit using the [DescribeBuckets](../APIReference/datasources-s3.md "../APIReference/datasources-s3.md") operation of the
Amazon Macie API. This operation returns an array of objects. Each object contains statistical
data and other information about an S3 general purpose bucket that matches the filter
criteria.

In the filter criteria, include a condition for the type of coverage data that you want
to review:

- To identify buckets that Macie isn't allowed to access due to the buckets' permissions
  settings, include a condition where the value for the `errorCode` field equals
  `ACCESS_DENIED`.
- To identify buckets that Macie is allowed to access and hasn't analyzed yet, include
  conditions where the value for the `sensitivityScore` field equals
  `50` and the value for the `errorCode` field doesn't equal
  `ACCESS_DENIED`.
- To identify buckets that Macie can't analyze because all the buckets' objects use
  unsupported storage classes or formats, include conditions where the value for the
  `classifiableSizeInBytes` field equals `0` and the value for the
  `sizeInBytes` field is greater than `0`.
- To identify buckets for which Macie has analyzed at least one object, include
  conditions where the value for the `sensitivityScore` field falls within the
  range of 1–99 but is not equal to `50`. To also include buckets where you
  manually assigned the maximum score, the range should be 1–100.
- To identify buckets that Macie hasn’t analyzed yet due to object-level classification
  errors, include a condition where the value for the `sensitivityScore` field
  equals `-1`. To then review a breakdown of the types and number of errors that
  occurred for a particular bucket, use the [GetResourceProfile](../APIReference/resource-profiles.md "../APIReference/resource-profiles.md")
  operation.

If you're using the AWS Command Line Interface (AWS CLI), specify filter criteria in queries that you submit
by running the [describe-buckets](../../../cli/latest/reference/macie2/describe-buckets.md "../../../cli/latest/reference/macie2/describe-buckets.md") command. To
review a breakdown of the types and number of errors that occurred for a particular S3 bucket,
if any, run the [get-resource-profile](../../../cli/latest/reference/macie2/get-resource-profile.md "../../../cli/latest/reference/macie2/get-resource-profile.md")
command.

For example, the following AWS CLI commands use filter criteria to retrieve the details of
all the S3 buckets that Macie isn't allowed to access due to the buckets' permissions
settings.

This example is formatted for Linux, macOS, or Unix:

```
`$` `aws macie2 describe-buckets --criteria '{"errorCode":{"eq":["ACCESS_DENIED"]}}'`
```

This example is formatted for Microsoft Windows:

```
`C:\>` `aws macie2 describe-buckets --criteria={\"errorCode\":{\"eq\":[\"ACCESS_DENIED\"]}}`
```

If your request succeeds, Macie returns a `buckets` array. The array contains
an object for each S3 bucket that’s in the current AWS Region and matches the filter
criteria.

If no S3 buckets match the filter criteria, Macie returns an empty `buckets`
array.

```
`{
 "buckets": []
}`
```

For more information about specifying filter criteria in queries, including examples of
common criteria, see [Filtering your S3 bucket
inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md").

For detailed information that can help you address coverage issues, see [Remediating coverage issues for automated sensitive data discovery](discovery-coverage-remediate.md "discovery-coverage-remediate.md").
