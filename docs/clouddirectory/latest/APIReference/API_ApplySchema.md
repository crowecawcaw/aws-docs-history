Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# ApplySchema

Copies the input published schema, at the specified version, into the [Directory](API_Directory.md "API_Directory.md") with the same
 name and version as that of the published schema.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/schema/apply HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "PublishedSchemaArn": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_ApplySchema_RequestSyntax "#API_ApplySchema_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md")
 into which the schema is copied. For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[PublishedSchemaArn](#API_ApplySchema_RequestSyntax "#API_ApplySchema_RequestSyntax")**


Published schema Amazon Resource Name (ARN) that needs to be copied. For more
 information, see [Arn Examples](arns.md "arns.md").


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "AppliedSchemaArn": "***string***",
   "DirectoryArn": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[AppliedSchemaArn](#API_ApplySchema_ResponseSyntax "#API_ApplySchema_ResponseSyntax")**


The applied schema ARN that is associated with the copied schema in the [Directory](API_Directory.md "API_Directory.md"). You can use this ARN to describe the schema information applied on
 this directory. For more information, see [Arn Examples](arns.md "arns.md").


Type: String




**[DirectoryArn](#API_ApplySchema_ResponseSyntax "#API_ApplySchema_ResponseSyntax")**


The ARN that is associated with the [Directory](API_Directory.md "API_Directory.md"). For more information,
 see [Arn Examples](arns.md "arns.md").


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**InternalServiceException** 


Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/") site to see if there are any operational issues with the service.


HTTP Status Code: 500




**InvalidArnException** 


Indicates that the provided ARN value is not valid.


HTTP Status Code: 400




**InvalidAttachmentException** 


Indicates that an attempt to make an attachment was invalid. For example, attaching two nodes 
 with a link type that is not applicable to the nodes or attempting to apply a schema to a directory a second time.


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


This example illustrates one usage of ApplySchema.



```
PUT /amazonclouddirectory/2017-01-11/schema/apply HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 94
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171003/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=ac58e3d2d25b85cd1869f7a845a0e97cebfce28d15e8f8df34c0ee89a197f042
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI
X-Amz-Date: 20171003T201513Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"PublishedSchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:schema/published/org/1"
}
```

### Example Response


This example illustrates one usage of ApplySchema.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 90d60895-a877-11e7-81c0-7b48a7696e76
Date: Tue, 03 Oct 2017 20:15:13 GMT
x-amzn-RequestId: 90d60895-a877-11e7-81c0-7b48a7696e76
Content-Type: application/json
Content-Length: 212

{
	"AppliedSchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI/schema/org/1",
	"DirectoryArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ApplySchema")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ApplySchema "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ApplySchema")
