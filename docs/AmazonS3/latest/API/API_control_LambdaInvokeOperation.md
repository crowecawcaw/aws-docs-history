# LambdaInvokeOperation

Contains the configuration parameters for a `Lambda Invoke` operation.


## Contents





**FunctionArn** 


The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
 invoke on every object in the manifest.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`



Required: No




**InvocationSchemaVersion** 


Specifies the schema version for the payload that Batch Operations sends when invoking
 an AWS Lambda function. Version `1.0` is the default. Version
 `2.0` is required when you use Batch Operations to invoke AWS Lambda functions that act on directory buckets, or if you need to specify
 `UserArguments`. For more information, see [Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and
 AWS Lambda](https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/ "https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/") in the *AWS Storage Blog*.


###### Important

Ensure that your AWS Lambda function code expects
 `InvocationSchemaVersion`
**2.0** and uses bucket name rather than bucket ARN. If the
 `InvocationSchemaVersion` does not match what your AWS Lambda
 function expects, your function might not work as expected.


###### Note


**Directory buckets** - To initiate AWS Lambda
 function to perform custom actions on objects in directory buckets, you must specify
 `2.0`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Required: No




**UserArguments** 


Key-value pairs that are passed in the payload that Batch Operations sends when invoking
 an AWS Lambda function. You must specify `InvocationSchemaVersion`
**2.0** for `LambdaInvoke` operations that include
 `UserArguments`. For more information, see [Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and
 AWS Lambda](https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/ "https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/") in the *AWS Storage Blog*.


Type: String to string map


Map Entries: Maximum number of 10 items.


Key Length Constraints: Minimum length of 1. Maximum length of 64.


Value Length Constraints: Maximum length of 1024.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LambdaInvokeOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/LambdaInvokeOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LambdaInvokeOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/LambdaInvokeOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LambdaInvokeOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/LambdaInvokeOperation")
