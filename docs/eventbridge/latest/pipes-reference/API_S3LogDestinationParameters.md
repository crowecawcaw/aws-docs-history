

# S3LogDestinationParameters
<a name="API_S3LogDestinationParameters"></a>

The Amazon S3 logging configuration settings for the pipe.

## Contents
<a name="API_S3LogDestinationParameters_Contents"></a>

 ** BucketName **   <a name="eventbridge-Type-S3LogDestinationParameters-BucketName"></a>
Specifies the name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Required: Yes

 ** BucketOwner **   <a name="eventbridge-Type-S3LogDestinationParameters-BucketOwner"></a>
Specifies the AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.  
Type: String  
Pattern: `\d{12}`   
Required: Yes

 ** OutputFormat **   <a name="eventbridge-Type-S3LogDestinationParameters-OutputFormat"></a>
How EventBridge should format the log records.  
EventBridge currently only supports `json` formatting.  
Type: String  
Valid Values: `json | plain | w3c`   
Required: No

 ** Prefix **   <a name="eventbridge-Type-S3LogDestinationParameters-Prefix"></a>
Specifies any prefix text with which to begin Amazon S3 log object names.  
You can use prefixes to organize the data that you store in Amazon S3 buckets. A prefix is a string of characters at the beginning of the object key name. A prefix can be any length, subject to the maximum length of the object key name (1,024 bytes). For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## See Also
<a name="API_S3LogDestinationParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/S3LogDestinationParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/S3LogDestinationParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/S3LogDestinationParameters) 