Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# AttachObject

Attaches an existing object to another object. An object can be accessed in two
 ways:


1. Using the path
2. Using `ObjectIdentifier`

## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/object/attach HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "ChildReference": { 
      "Selector": "`string`"
   },
   "LinkName": "`string`",
   "ParentReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_AttachObject_RequestSyntax "#API_AttachObject_RequestSyntax")**


Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md")
 where both objects reside. For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ChildReference](#API_AttachObject_RequestSyntax "#API_AttachObject_RequestSyntax")**


The child object reference to be attached to the object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**[LinkName](#API_AttachObject_RequestSyntax "#API_AttachObject_RequestSyntax")**


The link name with which the child object is attached to the parent.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`



Required: Yes




**[ParentReference](#API_AttachObject_RequestSyntax "#API_AttachObject_RequestSyntax")**


The parent object reference.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "AttachedObjectIdentifier": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[AttachedObjectIdentifier](#API_AttachObject_ResponseSyntax "#API_AttachObject_ResponseSyntax")**


The attached `ObjectIdentifier`, which is the child
 `ObjectIdentifier`.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDeniedException** 


Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md "API_ListDirectories.md") and check your permissions.


HTTP Status Code: 403




**DirectoryNotEnabledException** 


Operations are only permitted on enabled directories.


HTTP Status Code: 400




**FacetValidationException** 


The [Facet](API_Facet.md "API_Facet.md") that you provided was not well formed or could not be
 validated with the schema.


HTTP Status Code: 400




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




**LinkNameAlreadyInUseException** 


Indicates that a link could not be created due to a naming conflict. Choose a different
 name and then try again.


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




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of AttachObject.



```
PUT /amazonclouddirectory/2017-01-11/object/attach HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 188
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171003/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=2ce97afc4ac4d1fd4826861fa366d6d8674d1399b1a666e59cc53b8310aacf6a
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171003T195605Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"ParentReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
	},
	"LinkName": "link2",
	"ChildReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
	}
}
```

### Example Response


This example illustrates one usage of AttachObject.



```
HTTP/1.1 200 OK
x-amzn-RequestId: e4be5146-a874-11e7-a169-c5bf0acd39f4
Date: Tue, 03 Oct 2017 19:56:06 GMT
x-amzn-RequestId: e4be5146-a874-11e7-a169-c5bf0acd39f4
Content-Type: application/json
Content-Length: 77

{
	"AttachedObjectIdentifier": "AQGG_ADlfNZBzYHY_JgDt3TWSvfuEnDqTdmeCuTs6YBNUA"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/AttachObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/AttachObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/AttachObject")
