# Exporting your search results

from evidence finder

After you've reviewed your search results, you can generate an assessment report based on
those results. Alternatively, you can export your evidence finder search results in a CSV file.

## Prerequisites

The following procedure assumes that you already followed the steps to [perform a
search](search-for-evidence-in-evidence-finder.md "search-for-evidence-in-evidence-finder.md") and [review your
search results](viewing-search-results-in-evidence-finder.md "viewing-search-results-in-evidence-finder.md") in evidence finder.

## Procedure

###### Contents

- [Generating an assessment report
  from your search results](exporting-search-results-from-evidence-finder.md#generate-one-time-report-from-search-results "exporting-search-results-from-evidence-finder.md#generate-one-time-report-from-search-results")
- [Exporting your search results into a CSV file](exporting-search-results-from-evidence-finder.md#export-search-results "exporting-search-results-from-evidence-finder.md#export-search-results")
  - [Viewing your results after you've exported them](exporting-search-results-from-evidence-finder.md#viewing-results-after-export "exporting-search-results-from-evidence-finder.md#viewing-results-after-export")

### Generating an assessment report

from your search results

After you're satisfied with the search results, you can generate an assessment
report.

###### To generate an assessment report from your search results

1. At the top of the **View results** table, choose **Generate
   assessment report**.
2. Enter a name and a description for your assessment report, and review the assessment
   report details.
3. Choose **Generate assessment report**.

It takes a few minutes for your assessment report to be generated. You can navigate away
from evidence finder while this happens, and a green success notification will confirm when the
report is ready. You can then go to the Audit Manager download center and [download your assessment report](download-center.md#download-a-file "download-center.md#download-a-file").

###### Note

Audit Manager generates a one-time report using only the evidence from the search results. This
report doesn't include any evidence that was manually [added
to a report from the assessment page](generate-assessment-report-include-evidence.md "generate-assessment-report-include-evidence.md").

Limits apply to how much evidence can be included in an assessment report. For more
information, see [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md").

### Exporting your search results into a CSV file

You might need a portable version of your evidence finder search results. If this is the
case, you can export your search results into a CSV file.

After you export your search results, the CSV file is available in the Audit Manager download
center for seven days. A copy of the CSV file is also delivered to your preferred S3 bucket,
which is known as an _export destination_. Your CSV file
remains available in this bucket until you delete that file.

Audit Manager uses [CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") functionality to
export and deliver CSV files from evidence finder. The following factors define how the CSV
export process works:

- All of your search results are included in the CSV file. If you want to include only
  specific search results, we recommend that you [edit your search filters](search-for-evidence-in-evidence-finder.md#editing-a-search "search-for-evidence-in-evidence-finder.md#editing-a-search"). This way, you can narrow down your results to target only
  the evidence that you want to export.
- CSV files are exported in compressed GZIP format. The default CSV file name is
  `queryID/result.csv.gz`, where `queryID` is the ID of your search
  query.
- The maximum file size for a CSV export is 1 TB. If you’re exporting over 1 TB of data,
  your results are split into more than one file. Each CSV file is named
  `result_`number`.csv.gz`. The number of CSV files that
  you get depends on the total size of your search results. For example, exporting 2 TB of data
  provides you with two query result files: `result_1.csv.gz` and
  `result_2.csv.gz`.
- In addition to the CSV file, a JSON sign file is delivered to your S3 bucket. This file
  acts as a checksum to verify that the information within the CSV file is accurate. To learn
  more, see [CloudTrail sign file structure](../../../awscloudtrail/latest/userguide/cloudtrail-results-file-validation-sign-file-structure.md "../../../awscloudtrail/latest/userguide/cloudtrail-results-file-validation-sign-file-structure.md") in the _AWS CloudTrail Developer
  Guide_. To determine whether the query results were modified, deleted, or
  unchanged after they were delivered, you can use the CloudTrail query results integrity validation.
  For instructions, see [Validate saved query results](../../../awscloudtrail/latest/userguide/cloudtrail-query-results-validation-intro.md "../../../awscloudtrail/latest/userguide/cloudtrail-query-results-validation-intro.md") in the _AWS CloudTrail Developer
  Guide_.

###### Note

Manual evidence text responses are not currently included in evidence finder previews or CSV
exports. To see text response data, choose the manual evidence name in your evidence finder
results to open the evidence details page. If you need to view text response data outside of
the Audit Manager console, we recommend that you generate an assessment report from your evidence
finder results. All manual evidence details, including text responses, are included in
assessment reports.

Follow these steps to export your search results for the first time. This procedure
gives you the option to specify a default export destination for all of your future exports.
If you don't want to save a default export destination right now, you can do so later by
[updating your export destination settings](settings-export-destination.md "settings-export-destination.md").

###### Important

Before you start, make sure that you have an S3 bucket available to use as your export
destination. You can use one of your existing S3 buckets, or you can [create a
new bucket in Amazon S3](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). For optimal security and performance, we recommend using an S3
bucket in the same AWS account and region as your assessment. In addition, your S3 bucket
must have the required permissions policy to allow CloudTrail to write the export files to it.
More specifically, the bucket policy must include an `s3:PutObject` action and
the bucket ARN, and list CloudTrail as the service principal. We provide an [example permission policy](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md") that you can use. For instructions
on how to attach this policy to your S3 bucket, see [Adding a bucket policy by using the
Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md").

For more tips, see [Configuration tips for your
export destination](settings-export-destination.md#settings-export-destination-tips "settings-export-destination.md#settings-export-destination-tips"). If you encounter any issues when
exporting a CSV file, see [csv-exports](evidence-finder-issues.md#csv-exports "evidence-finder-issues.md#csv-exports").

###### To export your search results (first-run experience)

1. At the top of the **View results** table, choose **Export
   CSV**.
2. Specify the S3 bucket that you want to export your file to.
   - Choose **Browse S3** to select from your list of buckets.
   - Alternatively, you can enter the bucket URI in this format:
     `s3://bucketname/prefix`

###### Tip

To keep your destination bucket organized, you can create an optional folder for your
CSV exports. To do so, append a slash (`/`) and a prefix to the value
in the **Resource URI** box (for example,
`/evidenceFinderExports`). Audit Manager then includes this prefix when it
adds the CSV file to the bucket, and Amazon S3 generates the path specified by the prefix. For
more information about prefixes in Amazon S3, see [Organizing objects in the Amazon S3
console](../../../AmazonS3/latest/userguide/using-folders.md "../../../AmazonS3/latest/userguide/using-folders.md") in the _Amazon Simple Storage Service_ User Guide. 3. (Optional) If you don't want to save this bucket as your default export destination,
clear the check box that says **Save this bucket as the default export destination
in my evidence finder settings**. 4. Choose **Export**.

After you've saved a default S3 bucket as your default export destination, you can
follow these steps moving forward.

###### To export your search results (after you saved a default export destination)

1. At the top of the **View results** table, choose **Export
   CSV**.
2. In the prompt that appears, review the default S3 bucket where your exported file will
   be saved.
   1. (Optional) To continue using this bucket and hide this message moving forward, check
      the **Don't remind me again** box.
   2. (Optional) To change this bucket, follow the procedure to [update your export destination settings](settings-export-destination.md "settings-export-destination.md").

3. Choose **Confirm**.

Depending on how much data you’re exporting, the export process can take a few minutes to
complete. You can navigate away from evidence finder while the export is in progress. When you
navigate away from evidence finder, your search is stopped and your search results are
discarded in the console. However, the CSV export process continues in the background. The CSV
file will contain the complete set of search results that matched your query.

#### Viewing your results after you've exported them

To find your CSV file and check its status, go to the Audit Manager [Audit Manager download center](download-center.md "download-center.md"). When the exported file is ready,
you can [download your CSV file](download-center.md#download-a-file "download-center.md#download-a-file") from the download center.

You can also find and download the CSV file from your export destination S3 bucket.

###### To find your CSV file and sign file in the Amazon S3 console

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the export destination bucket that you specified when you exported your CSV
   file.
3. Navigate through the object hierarchy until you find the CSV file and the sign file.
   The CSV file has a `.csv.gz` extension and the sign file has a `.json`
   extension.

You will navigate through an object hierarchy that is similar to the following example,
but with a different export destination bucket name, account ID, date, and query ID.

```
All Buckets
    Export_Destination_Bucket_Name
        AWSLogs
            Account_ID;
                CloudTrail-Lake
                    Query
                        YYYY
                            MM
                              DD
                                Query_ID
```

## Additional resources

- [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md")
- [Configuring your default export
  destination for evidence finder](settings-export-destination.md "settings-export-destination.md")
