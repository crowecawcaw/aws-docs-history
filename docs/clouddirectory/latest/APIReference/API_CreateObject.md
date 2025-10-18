Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# CreateObject

Creates an object in a [Directory](API_Directory.md "API_Directory.md"). Additionally attaches the object to
 a parent, if a parent reference and `LinkName` is specified. An object is simply a
 collection of [Facet](API_Facet.md "API_Facet.md") attributes. You can also use this API call to create a
 policy object, if the facet from which you create the object is a policy facet. 


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/object HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "LinkName": "`string`",
   "ObjectAttributeList": [ 
      { 
         "Key": { 
            "FacetName": "`string`",
            "Name": "`string`",
            "SchemaArn": "`string`"
         },
         "Value": { 
            "BinaryValue": `blob`,
            "BooleanValue": `boolean`,
            "DatetimeValue": `number`,
            "NumberValue": "`string`",
            "StringValue": "`string`"
         }
      }
   ],
   "ParentReference": { 
      "Selector": "`string`"
   },
   "SchemaFacets": [ 
      { 
         "FacetName": "`string`",
         "SchemaArn": "`string`"
      }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_CreateObject_RequestSyntax "#API_CreateObject_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the [Directory](API_Directory.md "API_Directory.md")
 in which the object will be created. For more information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[LinkName](#API_CreateObject_RequestSyntax "#API_CreateObject_RequestSyntax")**


The name of link that is used to attach this object to a parent.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[^\/\[\]\(\):\{\}#@!?\s\\;]+`



Required: No




**[ObjectAttributeList](#API_CreateObject_RequestSyntax "#API_CreateObject_RequestSyntax")**


The attribute map whose attribute ARN contains the key and attribute value as the map
 value.


Type: Array of [AttributeKeyAndValue](API_AttributeKeyAndValue.md "API_AttributeKeyAndValue.md") objects


Required: No




**[ParentReference](#API_CreateObject_RequestSyntax "#API_CreateObject_RequestSyntax")**


If specified, the parent reference to which this object will be attached.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: No




**[SchemaFacets](#API_CreateObject_RequestSyntax "#API_CreateObject_RequestSyntax")**


A list of schema facets to be associated with the object. Do not provide minor version components. See [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") for details.


Type: Array of [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") objects


Required: Yes




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





**[ObjectIdentifier](#API_CreateObject_ResponseSyntax "#API_CreateObject_ResponseSyntax")**


The identifier that is associated with the object.


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


This example illustrates one usage of CreateObject.



```
PUT /amazonclouddirectory/2017-01-11/object HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 196
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20170912/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=af5780db69f39c02593f384e0ad70528f9c833e67d47e8e37ac456c10c994aa0
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8
X-Amz-Date: 20170912T184134Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
   "SchemaFacets":[
      {
         "SchemaArn":"arn:aws:clouddirectory:us-west-2:45132example:directory/AXQXDXvdgkOWktRXV4HnRa8/schema/Examplepersonschema/1",
         "FacetName":"Organization_Person"
      }
   ]
}
```

### Example Response


This example illustrates one usage of CreateObject.



```
HTTP/1.1 200 OK
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Date: Thu, 12 Sep 2017 00:35:44 GMT
x-amzn-RequestId: f6f0b320-a3e4-11e7-b86b-239c40918c06
Content-Type: application/json
Content-Length: 521

{
    "ObjectIdentifier": "AQF0Fw173YJDlpLUV1eB50WvP1K49muETy2xCqhXZK2s-A"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/CreateObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/CreateObject")
