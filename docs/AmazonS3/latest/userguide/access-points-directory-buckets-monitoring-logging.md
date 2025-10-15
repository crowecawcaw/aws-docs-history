# Monitoring and logging access points for directory buckets

You can log requests made through access points and requests made to the APIs that
 manage access points, such as `CreateAccessPoint` and
 `GetAccessPointPolicy,` by using AWS CloudTrail. CloudTrail log entries for requests made through access points include the access point ARN (which includes the access point name) in the
 `resources` section of the log.

For example, suppose you have the following configuration: 


* A bucket named
 ``amzn-s3-demo-bucket`--`zone-id`--x-s3`
 in Region `region` that contains an
 object named `my-image.jpg`.
* An access point named `my-bucket-ap--zoneID--xa-s3` that is
 associated with
 ``amzn-s3-demo-bucket`--`zone-id`--x-s3`
* An AWS account ID of
 `123456789012`
The following example shows the `resources` section of a CloudTrail log entry
 for the preceding configuration:


```
"resources": [
        {"type": "AWS::S3Express::Object",
        
            "ARN": "arn:aws:s3express-region:123456789012:bucket/`amzn-s3-demo-bucket`--`zone-id`--x-s3/my-image.jpg"
        },
        {"accountId": "c",
            "type": "AWS::S3Express::DirectoryBucket",
            "ARN": "arn:aws::s3express:region:123456789012:bucket/`amzn-s3-demo-bucket`--`zone-id`--x-s3"
        },
        {"accountId": "123456789012",
            "type": "AWS::S3::AccessPoint",
            "ARN": "arn:aws:s3express:region:123456789012:accesspoint/my-bucket-ap--zoneID--xa-s3"
        }
    ]        
```
For more information about AWS CloudTrail, see [What is
 AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html") in the *AWS CloudTrail User Guide*.
