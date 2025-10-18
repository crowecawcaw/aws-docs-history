# Trail

The settings for a trail.


## Contents





**CloudWatchLogsLogGroupArn** 


Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log
 group to which CloudTrail logs will be delivered.


Type: String


Required: No




**CloudWatchLogsRoleArn** 


Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's
 log group.


Type: String


Required: No




**HasCustomEventSelectors** 


Specifies if the trail has custom event selectors.


Type: Boolean


Required: No




**HasInsightSelectors** 


Specifies whether a trail has insight types specified in an `InsightSelector`
 list.


Type: Boolean


Required: No




**HomeRegion** 


The Region in which the trail was created.


Type: String


Required: No




**IncludeGlobalServiceEvents** 


Set to **True** to include AWS API calls
 from AWS global services such as IAM. Otherwise, **False**.


Type: Boolean


Required: No




**IsMultiRegionTrail** 


Specifies whether the trail exists only in one Region or exists in all Regions.


Type: Boolean


Required: No




**IsOrganizationTrail** 


Specifies whether the trail is an organization trail.


Type: Boolean


Required: No




**KmsKeyId** 


Specifies the AWS KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a AWS KMS key in the
 following format.



`arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`



Type: String


Required: No




**LogFileValidationEnabled** 


Specifies whether log file validation is enabled.


Type: Boolean


Required: No




**Name** 


Name of the trail set by calling [CreateTrail](API_CreateTrail.md "API_CreateTrail.md"). The maximum length is
 128 characters.


Type: String


Required: No




**S3BucketName** 


Name of the Amazon S3 bucket into which CloudTrail delivers your trail
 files. See [Amazon S3
 Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html").


Type: String


Required: No




**S3KeyPrefix** 


Specifies the Amazon S3 key prefix that comes after the name of the bucket you
 have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](../userguide/get-and-view-cloudtrail-log-files.md#cloudtrail-find-log-files "../userguide/get-and-view-cloudtrail-log-files.md#cloudtrail-find-log-files"). The maximum length is 200
 characters.


Type: String


Required: No




**SnsTopicARN** 


Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send
 notifications when log files are delivered. The following is the format of a topic
 ARN.



`arn:aws:sns:us-east-2:123456789012:MyTopic`



Type: String


Required: No




**SnsTopicName** 



*This member has been deprecated.*



This field is no longer in use. Use `SnsTopicARN`.


Type: String


Required: No




**TrailARN** 


Specifies the ARN of the trail. The following is the format of a trail ARN.



`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Trail "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Trail")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Trail "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Trail")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Trail "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Trail")
