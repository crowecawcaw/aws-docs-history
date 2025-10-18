Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# GetObjectAttributes

Retrieves attributes within a facet that are associated with an object.


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/object/attributes/get HTTP/1.1
x-amz-data-partition: `DirectoryArn`
x-amz-consistency-level: `ConsistencyLevel`
Content-type: application/json

{
   "AttributeNames": [ "`string`" ],
   "ObjectReference": { 
      "Selector": "`string`"
   },
   "SchemaFacet": { 
      "FacetName": "`string`",
      "SchemaArn": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[ConsistencyLevel](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The consistency level at which to retrieve the attributes on an object.


Valid Values: `SERIALIZABLE | EVENTUAL`





**[DirectoryArn](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md") where the object resides.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[AttributeNames](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


List of attribute names whose values will be retrieved.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**[ObjectReference](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Reference that identifies the object whose attributes will be retrieved.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**[SchemaFacet](#API_GetObjectAttributes_RequestSyntax "#API_GetObjectAttributes_RequestSyntax")**


Identifier for the facet whose attributes will be retrieved. See [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") for details.


Type: [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": [ 
      { 
         "Key": { 
            "FacetName": "***string***",
            "Name": "***string***",
            "SchemaArn": "***string***"
         },
         "Value": { 
            "BinaryValue": ***blob***,
            "BooleanValue": ***boolean***,
            "DatetimeValue": ***number***,
            "NumberValue": "***string***",
            "StringValue": "***string***"
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Attributes](#API_GetObjectAttributes_ResponseSyntax "#API_GetObjectAttributes_ResponseSyntax")**


The attributes that are associated with the object.


Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md "API_AttributeKeyAndValue.md") objects




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




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetObjectAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetObjectAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetObjectAttributes")
