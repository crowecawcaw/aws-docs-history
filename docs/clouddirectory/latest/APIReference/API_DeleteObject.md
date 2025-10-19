Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# DeleteObject

Deletes an object and its associated attributes. Only objects with no children and no
 parents can be deleted. The maximum number of attributes that can be deleted during an object deletion is 30. For more information, see [Amazon Cloud Directory Limits](../developerguide/limits.md "../developerguide/limits.md").


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/object/delete HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "ObjectReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md")
 where the object resides. For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ObjectReference](#API_DeleteObject_RequestSyntax "#API_DeleteObject_RequestSyntax")**


A reference that identifies the object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**DirectoryNotEnabledException** 


Operations are only permitted on enabled directories.


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




**ObjectNotDetachedException** 


Indicates that the requested operation cannot be completed because the object has not
 been detached from the tree.


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


This example illustrates one usage of DeleteObject.



```
PUT /amazonclouddirectory/2017-01-11/object/delete HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 84
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171009/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=7b16ec6d1d54f36672cb2d39f1e975925e5222208ff8c6a8cd4e1a63dd17df70
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AfMr4qym1kZTvwqOafAYfqI
X-Amz-Date: 20171009T183947Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"ObjectReference": {
		"Selector": "$AQHzK-KsptZGU78KjmnwGH6i8H-voMZDSNCqfx-fRUcBFg"
	}
}
```

### Example Response


This example illustrates one usage of DeleteObject.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 3b1928f3-ad21-11e7-81c0-7b48a7696e76
Date: Mon, 09 Oct 2017 18:39:48 GMT
x-amzn-RequestId: 3b1928f3-ad21-11e7-81c0-7b48a7696e76
Content-Type: application/json
Content-Length: 2

{}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/DeleteObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/DeleteObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/DeleteObject")
