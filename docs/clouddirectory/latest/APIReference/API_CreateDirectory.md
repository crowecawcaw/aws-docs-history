Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# CreateDirectory

Creates a [Directory](API_Directory.md "API_Directory.md") by copying the published schema into the
 directory. A directory cannot be created without a schema.

You can also quickly create a directory using a managed schema, called the
 `QuickStartSchema`. For more information, see [Managed Schema](../developerguide/schemas_managed.md "../developerguide/schemas_managed.md") in the *Amazon Cloud Directory Developer Guide*.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/directory/create HTTP/1.1
x-amz-data-partition: `SchemaArn`
Content-type: application/json

{
   "Name": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[SchemaArn](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**


The Amazon Resource Name (ARN) of the published schema that will be copied into the
 data [Directory](API_Directory.md "API_Directory.md"). For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[Name](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**


The name of the [Directory](API_Directory.md "API_Directory.md"). Should be unique per account, per
 region.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "AppliedSchemaArn": "***string***",
   "DirectoryArn": "***string***",
   "Name": "***string***",
   "ObjectIdentifier": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[AppliedSchemaArn](#API_CreateDirectory_ResponseSyntax "#API_CreateDirectory_ResponseSyntax")**


The ARN of the published schema in the [Directory](API_Directory.md "API_Directory.md"). Once a published
 schema is copied into the directory, it has its own ARN, which is referred to applied schema
 ARN. For more information, see [Arn Examples](arns.md "arns.md").


Type: String




**[DirectoryArn](#API_CreateDirectory_ResponseSyntax "#API_CreateDirectory_ResponseSyntax")**


The ARN that is associated with the [Directory](API_Directory.md "API_Directory.md"). For more information,
 see [Arn Examples](arns.md "arns.md").


Type: String




**[Name](#API_CreateDirectory_ResponseSyntax "#API_CreateDirectory_ResponseSyntax")**


The name of the [Directory](API_Directory.md "API_Directory.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `^[a-zA-Z0-9._-]*$`





**[ObjectIdentifier](#API_CreateDirectory_ResponseSyntax "#API_CreateDirectory_ResponseSyntax")**


The root object node of the created directory.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**DirectoryAlreadyExistsException** 


Indicates that a [Directory](API_Directory.md "API_Directory.md") could not be created due to a naming
 conflict. Choose a different name and try again.


HTTP Status Code: 400




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


HTTP Status Code: 400




**ResourceNotFoundException** 


The specified resource could not be found.


HTTP Status Code: 404




**RetryableConflictException** 


Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.


HTTP Status Code: 409




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of CreateDirectory.



```
PUT /amazonclouddirectory/2017-01-11/directory/create HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 22
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170922/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=f347d3f8d6ceccbfd47738ab11fe0194b5efd329b4e0431f7221ee80c672fd9a
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:schema/published/person/1
X-Amz-Date: 20170922T220642Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"Name": "ExampleCD"
}
```

### Example Response


This example illustrates one usage of CreateDirectory.



```
HTTP/1.1 200 OK
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Date: Thu, 22 Sep 2017 00:35:44 GMT
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Content-Type: application/json
Content-Length: 521

{
	"AppliedSchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI/schema/person/1",
	"DirectoryArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI",
	"Name": "ExampleCD",
	"ObjectIdentifier": "AQHzK-KsptZGU78KjmnwGH6i-4guCM3uQFOTA9_NjeHDrg"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateDirectory")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateDirectory "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateDirectory")
