# GetTrailStatus

Returns a JSON-formatted list of information about the specified trail. Fields include
 information on delivery errors, Amazon SNS and Amazon S3 errors, and start
 and stop logging times for each trail. This operation returns trail status from a single
 Region. To return trail status from all Regions, you must call the operation on each
 Region.


## Request Syntax



```
{
   "Name": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Name](#API_GetTrailStatus_RequestSyntax "#API_GetTrailStatus_RequestSyntax")**


Specifies the name or the CloudTrail ARN of the trail for which you are
 requesting status. To get the status of a shadow trail (a replication of the trail in
 another Region), you must specify its ARN.



 The following is the format of a trail
 ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



###### Note

If the trail is an organization trail and you are a member account in the organization in AWS Organizations, you must provide the full ARN of that trail, and not just the name.


Type: String


Required: Yes




## Response Syntax



```
{
   "IsLogging": ***boolean***,
   "LatestCloudWatchLogsDeliveryError": "***string***",
   "LatestCloudWatchLogsDeliveryTime": ***number***,
   "LatestDeliveryAttemptSucceeded": "***string***",
   "LatestDeliveryAttemptTime": "***string***",
   "LatestDeliveryError": "***string***",
   "LatestDeliveryTime": ***number***,
   "LatestDigestDeliveryError": "***string***",
   "LatestDigestDeliveryTime": ***number***,
   "LatestNotificationAttemptSucceeded": "***string***",
   "LatestNotificationAttemptTime": "***string***",
   "LatestNotificationError": "***string***",
   "LatestNotificationTime": ***number***,
   "StartLoggingTime": ***number***,
   "StopLoggingTime": ***number***,
   "TimeLoggingStarted": "***string***",
   "TimeLoggingStopped": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[IsLogging](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Whether the CloudTrail trail is currently logging AWS API
 calls.


Type: Boolean




**[LatestCloudWatchLogsDeliveryError](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Displays any CloudWatch Logs error that CloudTrail encountered when attempting
 to deliver logs to CloudWatch Logs.


Type: String




**[LatestCloudWatchLogsDeliveryTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.


Type: Timestamp




**[LatestDeliveryAttemptSucceeded](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




**[LatestDeliveryAttemptTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




**[LatestDeliveryError](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Displays any Amazon S3 error that CloudTrail encountered when attempting
 to deliver log files to the designated bucket. For more information, see [Error
 Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html "https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html") in the Amazon S3 API Reference. 


###### Note

This error occurs only when there is a problem with the destination S3 bucket, and
 does not occur for requests that time out. To resolve the issue, 
 fix the [bucket policy](../userguide/create-s3-bucket-policy-for-cloudtrail.md "../userguide/create-s3-bucket-policy-for-cloudtrail.md") so that CloudTrail 
 can write to the bucket; or create a new bucket and call `UpdateTrail` to specify the new bucket.


Type: String




**[LatestDeliveryTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Specifies the date and time that CloudTrail last delivered log files to an
 account's Amazon S3 bucket.


Type: Timestamp




**[LatestDigestDeliveryError](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Displays any Amazon S3 error that CloudTrail encountered when attempting
 to deliver a digest file to the designated bucket. For more information, see [Error
 Responses](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html "https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html") in the Amazon S3 API Reference. 


###### Note

This error occurs only when there is a problem with the destination S3 bucket, and
 does not occur for requests that time out. To resolve the issue, 
 fix the [bucket policy](../userguide/create-s3-bucket-policy-for-cloudtrail.md "../userguide/create-s3-bucket-policy-for-cloudtrail.md") so that CloudTrail 
 can write to the bucket; or create a new bucket and call `UpdateTrail` to specify the new bucket.


Type: String




**[LatestDigestDeliveryTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Specifies the date and time that CloudTrail last delivered a digest file to an
 account's Amazon S3 bucket.


Type: Timestamp




**[LatestNotificationAttemptSucceeded](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




**[LatestNotificationAttemptTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




**[LatestNotificationError](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Displays any Amazon SNS error that CloudTrail encountered when attempting
 to send a notification. For more information about Amazon SNS errors, see the
 [Amazon SNS
 Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html "https://docs.aws.amazon.com/sns/latest/dg/welcome.html"). 


Type: String




**[LatestNotificationTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Specifies the date and time of the most recent Amazon SNS notification that
 CloudTrail has written a new log file to an account's Amazon S3
 bucket.


Type: Timestamp




**[StartLoggingTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Specifies the most recent date and time when CloudTrail started recording API
 calls for an AWS account.


Type: Timestamp




**[StopLoggingTime](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


Specifies the most recent date and time when CloudTrail stopped recording API
 calls for an AWS account.


Type: Timestamp




**[TimeLoggingStarted](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




**[TimeLoggingStopped](#API_GetTrailStatus_ResponseSyntax "#API_GetTrailStatus_ResponseSyntax")**


This field is no longer in use.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudTrailARNInvalidException** 


This exception is thrown when an operation is called with an ARN that is not valid.


The following is the format of a trail ARN: `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`



The following is the format of an event data store ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE`



The following is the format of a dashboard ARN: `arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash`



The following is the format of a channel ARN:
 `arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890`



HTTP Status Code: 400




**InvalidTrailNameException** 


This exception is thrown when the provided trail name is not valid. Trail names must
 meet the following requirements:



* Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores
 (\_), or dashes (-)
* Start with a letter or number, and end with a letter or number
* Be between 3 and 128 characters
* Have no adjacent periods, underscores or dashes. Names like
 `my-_namespace` and `my--namespace` are not valid.
* Not be in IP address format (for example, 192.168.5.4)

HTTP Status Code: 400




**OperationNotPermittedException** 


This exception is thrown when the requested operation is not permitted.


HTTP Status Code: 400




**TrailNotFoundException** 


This exception is thrown when the trail with the given name is not found.


HTTP Status Code: 400




**UnsupportedOperationException** 


This exception is thrown when the requested operation is not supported.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetTrailStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetTrailStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetTrailStatus")
