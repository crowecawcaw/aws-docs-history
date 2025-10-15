# Use `GetBucketNotification` with a CLI

The following code examples show how to use `GetBucketNotification`.


CLI


**AWS CLI**

The following command retrieves the notification configuration for a bucket named `amzn-s3-demo-bucket`:



```
`aws s3api get-bucket-notification --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "TopicConfiguration": {
        "Topic": "arn:aws:sns:us-west-2:123456789012:my-notification-topic",
        "Id": "YmQzMmEwM2EjZWVlI0NGItNzVtZjI1MC00ZjgyLWZDBiZWNl",
        "Event": "s3:ObjectCreated:*",
        "Events": [
            "s3:ObjectCreated:*"
        ]
    }
}
```


* For API details, see
 [GetBucketNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This example retrieves notification configuration of the given bucket**



```
Get-S3BucketNotification -BucketName amzn-s3-demo-bucket | select -ExpandProperty TopicConfigurations

```

**Output:**



```
Id   Topic
--   -----
mimo arn:aws:sns:eu-west-1:123456789012:topic-1
```


* For API details, see
 [GetBucketNotification](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This example retrieves notification configuration of the given bucket**



```
Get-S3BucketNotification -BucketName amzn-s3-demo-bucket | select -ExpandProperty TopicConfigurations

```

**Output:**



```
Id   Topic
--   -----
mimo arn:aws:sns:eu-west-1:123456789012:topic-1
```


* For API details, see
 [GetBucketNotification](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
