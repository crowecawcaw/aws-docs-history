# Exporting your recommendations

This section provides you with instructions on how to export your AWS Compute Optimizer recommendations. Recommendations are exported in a CSV file, and its metadata
in a JSON file.

## Prerequisites

- The following procedures assumes that you have already completed the [Specifying an existing S3 bucket for your recommendations export](create-s3-bucket-policy-for-compute-optimizer.md "create-s3-bucket-policy-for-compute-optimizer.md") procedure.
- Make sure that you understand the following restrictions that apply to exporting Compute Optimizer recommendations.
  - You can't export recommendations from multiple AWS Regions into a single Amazon S3 bucket. To export recommendations from multiple AWS Regions, you must create separate Amazon S3 buckets for your recommendations in each AWS Region.
  - You can have only one recommendations export job in progress for each resource type,
    and for each AWS Region. Before creating a new export job, confirm that all previous
    export jobs are complete. For more information about viewing your export jobs, including
    those that are in progress, see [Viewing your export jobs](viewing-your-exports.md "viewing-your-exports.md").
  - Recommendations for each resource type and in each are exported in separate CSV
    files. You can't export recommendations from multiple resource types and Regions into a
    single file.
  - Large export jobs can take up to a few hours to complete. To lower your wait time,
    consider limiting the recommendation columns that you include in your export job.
    Additionally, if your account is the management account of an organization, consider
    limiting the number of member accounts to include in your export job.

## Procedure

###### To export your recommendations

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose a resource type in the navigation pane. For example, choose **EC2
   instances**, **Auto Scaling groups**, **EBS
   volume**, **Lambda function**, or
   **ECS services on Fargate**.
3. On the **Recommendations** page, choose the
   **Action** dropdown menu, and choose **Export
   Recommendations**.
4. On the **Export Recommendations** page, under **Export
   destination settings**, specify the following:
   1. For **Region**, specify an AWS Region for your export.
   2. For **Destination S3 bucket name**, specify the name of an
      existing S3 bucket in the specific Region.
   3. (Optional) Choose **Add Region** to export the recommendations
      for another AWS Region.
   4. (Optional) Choose **Remove** next to a specific Region and S3
      bucket name to remove the destination from the export job.
   5. (Optional) For **Object prefix**, specify a prefix to use in the
      destination S3 bucket for all of the export files. The prefix is an optional addition
      to the S3 object key that organizes your export files in your S3 bucket. You can
      specify a date prefix (for example, `2020/april`), a resource type prefix
      (for example, `ec2-instances`), or a combination of both (for example,
      `2020/april/ec2-instances`).

5. Under **Export filters**, specify the following:
   1. For **Resource type**, choose the resource type to include in
      your recommendations export.
   2. For **Accounts**, choose if you want to include recommendations
      for all member accounts of the organization. This option is available only if your
      account is the management account of an organization.
   3. For **CPU architecture preference**, choose **Graviton
      (`aws-arm64`)** to export recommendations that are based on
      the 64-bit ARM architecture (AWS Graviton). Otherwise, choose
      **Current** to export recommendations that are based on the CPU
      architecture of your current instances.

6. Under **Columns to include**, choose the recommendations data to
   include in your recommendations export. For more information about the columns to include,
   see [Exported files](exported-files.md "exported-files.md").
7. After confirming that the export job is configured correctly, choose
   **Export**. Or, to return to the **Recommendations**
   page without creating the export job, choose **Cancel**. If you cancel
   the export job configuration, the configuration is deleted.

###### Note

If you export recommendations for multiple AWS Regions at one time, they're
treated as separate export jobs. Compute Optimizer tries to start all of them at once. If an export
job fails to start, the **Export Recommendations** page displays an
error. Export jobs that successfully start continue to process. But, before trying to
start them again, you must resolve the errors for the failed jobs.

Your recommendations export job might take up to a few hours to complete. Check the status
of your export jobs by viewing the **Exports** page. For more information,
see [Viewing your export jobs](viewing-your-exports.md "viewing-your-exports.md"). Your
recommendations export file and its associated metadata file are saved to the specified S3
bucket when the export job is complete. The following are examples of the full Amazon S3 object key
for the export file and its associated metadata file. The account ID in the object keys is the
account of the requester of the export job. For more information, see [Exported files](exported-files.md "exported-files.md").

```
s3://`amzn-s3-demo-bucket`/`OptionalPrefix`/compute-optimizer/`AccountId`/`AWSRegion`-`CreatedTimestamp`-`UniqueJobID`.csv
```

```
s3://`amzn-s3-demo-bucket`/`OptionalPrefix`/compute-optimizer/`AccountId`/`AWSRegion`-`CreatedTimestamp`-`UniqueJobID`-metadata.json
```

**Example:**

```
s3://`compute-optimizer-exports`/`ec2-instance-recommendations`/compute-optimizer/`111122223333`/`us-west-2`-`2020-03-03T133027`-`3e496c549301c8a4dfcsdX`.csv
```

```
s3://`compute-optimizer-exports`/`ec2-instance-recommendations`/compute-optimizer/`111122223333`/`us-west-2`-`2020-03-03T133027`-`3e496c549301c8a4dfcsdX`-metadata.json
```

## Next steps

For instructions on how to view the export jobs that you created, see [Viewing your export jobs](viewing-your-exports.md "viewing-your-exports.md").

## Additional resources

- Troubleshooting — [Troubleshooting failed export jobs](troubleshooting-account-opt-in.md#troubleshooting-exports "troubleshooting-account-opt-in.md#troubleshooting-exports")
- [Exported files](exported-files.md "exported-files.md")
- [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").
