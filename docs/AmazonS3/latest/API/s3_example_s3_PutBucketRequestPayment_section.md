# Use `PutBucketRequestPayment` with a CLI

The following code examples show how to use `PutBucketRequestPayment`.


CLI


**AWS CLI**

**Example 1: To enable ``requester pays`` configuration for a bucket**


The following `put-bucket-request-payment` example enables `requester pays` for the specified bucket.



```
`aws s3api put-bucket-request-payment \
 --bucket `amzn-s3-demo-bucket` \
 --request-payment-configuration '`{"Payer":"Requester"}`'`

```

This command produces no output.


**Example 2: To disable ``requester pays`` configuration for a bucket**


The following `put-bucket-request-payment` example disables `requester pays` for the specified bucket.



```
`aws s3api put-bucket-request-payment \
 --bucket `amzn-s3-demo-bucket` \
 --request-payment-configuration '`{"Payer":"BucketOwner"}`'`

```

This command produces no output.



* For API details, see
 [PutBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-request-payment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-request-payment.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: Updates the request payment configuration for the bucket named 'amzn-s3-demo-bucket' so that the person requesting downloads from the bucket will be charged for the download. By default the bucket owner pays for downloads. To set the request payment back to the default use 'BucketOwner' for the RequestPaymentConfiguration\_Payer parameter.**



```
Write-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket -RequestPaymentConfiguration_Payer Requester

```


* For API details, see
 [PutBucketRequestPayment](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: Updates the request payment configuration for the bucket named 'amzn-s3-demo-bucket' so that the person requesting downloads from the bucket will be charged for the download. By default the bucket owner pays for downloads. To set the request payment back to the default use 'BucketOwner' for the RequestPaymentConfiguration\_Payer parameter.**



```
Write-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket -RequestPaymentConfiguration_Payer Requester

```


* For API details, see
 [PutBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
