# Creating a Batch Operations job with job tags used for labeling

You can label and control access to your Amazon S3 Batch Operations jobs by adding
 *tags*. Tags can be used to identify who is responsible for a
 Batch Operations job. You can create jobs with tags attached to them, and you can add tags to jobs
 after they are created. For more information, see [Controlling access and labeling jobs using tags](batch-ops-job-tags.md "batch-ops-job-tags.md").

The following AWS CLI example creates an S3 Batch Operations `S3PutObjectCopy` job
 using job tags as labels for the job. 

1. Select the action or `OPERATION` that you want the Batch Operations job
 to perform, and choose your `TargetResource`.



```
read -d '' OPERATION <<EOF
{
  "S3PutObjectCopy": {
    "TargetResource": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
  }
}
EOF
```
2. Identify the job `TAGS` that you want for the job. In this case,
 you apply two tags, `department` and `FiscalYear`,
 with the values `Marketing` and `2020`
 respectively.



```
read -d '' TAGS <<EOF
[
  {
    "Key": "`department`",
    "Value": "`Marketing`"
  },
  {
    "Key": "`FiscalYear`",
    "Value": "`2020`"
  }
]
EOF
```
3. Specify the `MANIFEST` for the Batch Operations job.



```
read -d '' MANIFEST <<EOF
{
  "Spec": {
    "Format": "`EXAMPLE_S3BatchOperations_CSV_20180820`",
    "Fields": [
      "Bucket",
      "Key"
    ]
  },
  "Location": {
    "ObjectArn": "arn:aws:s3:::`amzn-s3-demo-manifest-bucket/example_manifest.csv`",
    "ETag": "`example-5dc7a8bfb90808fc5d546218`"
  }
}
EOF
```
4. Configure the `REPORT` for the Batch Operations job.



```
read -d '' REPORT <<EOF
{
  "Bucket": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`",
  "Format": "`Example_Report_CSV_20180820`",
  "Enabled": true,
  "Prefix": "`reports/copy-with-replace-metadata`",
  "ReportScope": "AllTasks"
}
EOF
```
5. Run the`create-job` action to create your Batch Operations job with inputs set in the preceding steps.



```
aws \
    s3control create-job \
    --account-id `123456789012` \
    --manifest "${MANIFEST//$'\n'}" \
    --operation "${OPERATION//$'\n'/}" \
    --report "${REPORT//$'\n'}" \
    --priority 10 \
    --role-arn arn:aws:iam::`123456789012`:role/`batch-operations-role` \
    --tags "${TAGS//$'\n'/}" \
    --client-request-token "$(uuidgen)" \
    --region `us-west-2` \
    --description "`Copy with Replace Metadata`";
```
To create an S3 Batch Operations job with tags using the AWS SDK for Java, you can use the S3Control client to configure job parameters including manifest location, job operations, reporting settings, and tags for organization and tracking purposes.

For examples of how to create S3 Batch Operations jobs with tags using the AWS SDK for Java, see [Create a batch job to copy objects](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the *Amazon S3 API Reference*.
