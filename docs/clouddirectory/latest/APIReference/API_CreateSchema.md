Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# CreateSchema

Creates a new schema in a development state. A schema can exist in three
 phases:


* *Development:* This is a mutable phase of the schema. All new
 schemas are in the development phase. Once the schema is finalized, it can be
 published.
* *Published:* Published schemas are immutable and have a version
 associated with them.
* *Applied:* Applied schemas are mutable in a way that allows you
 to add new schema facets. You can also add new, nonrequired attributes to existing schema
 facets. You can apply only published schemas to directories.

## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/schema/create HTTP/1.1
Content-type: application/json

{
   "Name": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[Name](#API_CreateSchema_RequestSyntax "#API_CreateSchema_RequestSyntax")**


The name that is associated with the schema. This is unique to each account and in each
 region.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 32.


Pattern: `^[a-zA-Z0-9._-]*$`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "SchemaArn": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[SchemaArn](#API_CreateSchema_ResponseSyntax "#API_CreateSchema_ResponseSyntax")**


The Amazon Resource Name (ARN) that is associated with the schema. For more
 information, see [Arn Examples](arns.md "arns.md").


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


HTTP Status Code: 400




**RetryableConflictException** 


Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.


HTTP Status Code: 409




**SchemaAlreadyExistsException** 


Indicates that a schema could not be created due to a naming conflict. Please select a
 different name and then try again.


HTTP Status Code: 400




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of CreateSchema.



```
PUT /amazonclouddirectory/2017-01-11/schema/create HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 21
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170927/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-date, Signature=92b2be88dd90f3e789ff651f5ae897b35f601e2f6a4d08addb07993ef8399e29
X-Amz-Date: 20170927T164420Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"Name": "Customers"
}
```

### Example Response


This example illustrates one usage of CreateSchema.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 2c3050f1-a3a3-11e7-bd9d-f9e3493b0666
Date: Wed, 27 Sep 2017 16:44:47 GMT
x-amzn-RequestId: 2c3050f1-a3a3-11e7-bd9d-f9e3493b0666
Content-Type: application/json
Content-Length: 90

{
    "SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:schema/development/Customers"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateSchema")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateSchema "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateSchema")
