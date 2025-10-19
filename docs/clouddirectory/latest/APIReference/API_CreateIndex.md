Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# CreateIndex

Creates an index object. See [Indexing and search](../developerguide/indexing_search.md "../developerguide/indexing_search.md") for more information.


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/index HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "IsUnique": `boolean`,
   "LinkName": "`string`",
   "OrderedIndexedAttributeList": [ 
      { 
         "FacetName": "`string`",
         "Name": "`string`",
         "SchemaArn": "`string`"
      }
   ],
   "ParentReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_CreateIndex_RequestSyntax "#API_CreateIndex_RequestSyntax")**


The ARN of the directory where the index should be created.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[IsUnique](#API_CreateIndex_RequestSyntax "#API_CreateIndex_RequestSyntax")**


Indicates whether the attribute that is being indexed has unique values or
 not.


Type: Boolean


Required: Yes




**[LinkName](#API_CreateIndex_RequestSyntax "#API_CreateIndex_RequestSyntax")**


The name of the link between the parent object and the index object.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`



Required: No




**[OrderedIndexedAttributeList](#API_CreateIndex_RequestSyntax "#API_CreateIndex_RequestSyntax")**


Specifies the attributes that should be indexed on. Currently only a single attribute
 is supported.


Type: Array of [AttributeKey](API_AttributeKey.md "API_AttributeKey.md") objects


Required: Yes




**[ParentReference](#API_CreateIndex_RequestSyntax "#API_CreateIndex_RequestSyntax")**


A reference to the parent object that contains the index object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "ObjectIdentifier": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ObjectIdentifier](#API_CreateIndex_ResponseSyntax "#API_CreateIndex_ResponseSyntax")**


The `ObjectIdentifier` of the index created by this operation.


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




**UnsupportedIndexTypeException** 


Indicates that the requested index type is not supported.


HTTP Status Code: 400




**ValidationException** 


Indicates that your request is malformed in some manner. See the exception
 message.


HTTP Status Code: 400




## Examples


The following examples are formatted for legibility.


### Example Request


This example illustrates one usage of CreateIndex.



```
PUT /amazonclouddirectory/2017-01-11/index HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 290
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170913/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=dc93fb34cd655e125aa748b8747d99bef78c7c5785e30327cf151d74accbbcf0
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8
X-Amz-Date: 20170913T012153Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
   "ParentReference":{
      "Selector":"/"
   },
   "OrderedIndexedAttributeList":[
      {
         "SchemaArn":"arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8/schema/Examplepersonschema/1",
         "FacetName":"Organization_Person",
         "Name":"manager"
      }
   ],
   "IsUnique":true,
   "LinkName":"Examplelink"
}
```

### Example Response


This example illustrates one usage of CreateIndex.



```
HTTP/1.1 200 OK
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Date: Thu, 13 Sep 2017 00:35:44 GMT
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Content-Type: application/json
Content-Length: 521

{
   "ObjectIdentifier":"AQF0Fw173YJDlpLUV1eB50Wv4vU99HjyQIShCCUeVob2fw"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateIndex")
