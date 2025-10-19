Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# GetObjectInformation

Retrieves metadata about an object.


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/object/information HTTP/1.1
x-amz-data-partition: `DirectoryArn`
x-amz-consistency-level: `ConsistencyLevel`
Content-type: application/json

{
   "ObjectReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[ConsistencyLevel](#API_GetObjectInformation_RequestSyntax "#API_GetObjectInformation_RequestSyntax")**


The consistency level at which to retrieve the object information.


Valid Values: `SERIALIZABLE | EVENTUAL`





**[DirectoryArn](#API_GetObjectInformation_RequestSyntax "#API_GetObjectInformation_RequestSyntax")**


The ARN of the directory being retrieved.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ObjectReference](#API_GetObjectInformation_RequestSyntax "#API_GetObjectInformation_RequestSyntax")**


A reference to the object.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "ObjectIdentifier": "***string***",
   "SchemaFacets": [ 
      { 
         "FacetName": "***string***",
         "SchemaArn": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[ObjectIdentifier](#API_GetObjectInformation_ResponseSyntax "#API_GetObjectInformation_ResponseSyntax")**


The `ObjectIdentifier` of the specified object.


Type: String




**[SchemaFacets](#API_GetObjectInformation_ResponseSyntax "#API_GetObjectInformation_ResponseSyntax")**


The facets attached to the specified object. Although the response does not include minor version information, the most recently applied minor version of each Facet is in effect. See [GetAppliedSchemaVersion](API_GetAppliedSchemaVersion.md "API_GetAppliedSchemaVersion.md") for details.


Type: Array of [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") objects




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


This example illustrates one usage of GetObjectInformation.



```
POST /amazonclouddirectory/2017-01-11/object/information HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 84
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171005/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=6afad99dfe7c5c8152ec38e7ff206dc0c6c6060ed24624ea5654f24ab1392086
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171005T182528Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"ObjectReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TWmspn1fxfQmSQaaVKSbvEiQ"
	}
}
```

### Example Response


This example illustrates one usage of GetObjectInformation.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 90f2f915-a9fa-11e7-bd9d-f9e3493b0666
Date: Thu, 05 Oct 2017 18:25:29 GMT
x-amzn-RequestId: 90f2f915-a9fa-11e7-bd9d-f9e3493b0666
Content-Type: application/json
Content-Length: 215

{
	"ObjectIdentifier": "AQGG_ADlfNZBzYHY_JgDt3TWmspn1fxfQmSQaaVKSbvEiQ",
	"SchemaFacets": [{
		"FacetName": "node2",
		"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1"
	}]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/GetObjectInformation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetObjectInformation "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/GetObjectInformation")
