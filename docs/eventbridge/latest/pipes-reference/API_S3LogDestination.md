

# S3LogDestination
<a name="API_S3LogDestination"></a>

The Amazon S3 logging configuration settings for the pipe.

## Contents
<a name="API_S3LogDestination_Contents"></a>

 ** BucketName **   <a name="eventbridge-Type-S3LogDestination-BucketName"></a>
The name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.  
Type: String  
Required: No

 ** BucketOwner **   <a name="eventbridge-Type-S3LogDestination-BucketOwner"></a>
The AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.  
Type: String  
Required: No

 ** OutputFormat **   <a name="eventbridge-Type-S3LogDestination-OutputFormat"></a>
The format EventBridge uses for the log records.  
EventBridge currently only supports `json` formatting.  
Type: String  
Valid Values: `json | plain | w3c`   
Required: No

 ** Prefix **   <a name="eventbridge-Type-S3LogDestination-Prefix"></a>
The prefix text with which to begin Amazon S3 log object names.  
For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.  
Type: String  
Required: No

## See Also
<a name="API_S3LogDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/S3LogDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/S3LogDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/S3LogDestination) 