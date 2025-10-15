# Use `DeleteBucketReplication` with a CLI

The following code examples show how to use `DeleteBucketReplication`.


CLI


**AWS CLI**

The following command deletes a replication configuration from a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api delete-bucket-replication --bucket `amzn-s3-demo-bucket``

```


* For API details, see
 [DeleteBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-replication.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-replication.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: Deletes the replication configuration associated with the bucket named 'amzn-s3-demo-bucket'. Note that this operation requires permission for the s3:DeleteReplicationConfiguration action. You will be prompted for confirmation before the operation proceeds - to suppress confirmation, use the -Force switch.**



```
Remove-S3BucketReplication -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [DeleteBucketReplication](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: Deletes the replication configuration associated with the bucket named 'amzn-s3-demo-bucket'. Note that this operation requires permission for the s3:DeleteReplicationConfiguration action. You will be prompted for confirmation before the operation proceeds - to suppress confirmation, use the -Force switch.**



```
Remove-S3BucketReplication -BucketName amzn-s3-demo-bucket

```


* For API details, see
 [DeleteBucketReplication](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
