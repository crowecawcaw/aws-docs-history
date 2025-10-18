Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# ListIndex

Lists objects attached to the specified index.


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/index/targets HTTP/1.1
x-amz-data-partition: `DirectoryArn`
x-amz-consistency-level: `ConsistencyLevel`
Content-type: application/json

{
   "IndexReference": { 
      "Selector": "`string`"
   },
   "MaxResults": `number`,
   "NextToken": "`string`",
   "RangesOnIndexedValues": [ 
      { 
         "AttributeKey": { 
            "FacetName": "`string`",
            "Name": "`string`",
            "SchemaArn": "`string`"
         },
         "Range": { 
            "EndMode": "`string`",
            "EndValue": { 
               "BinaryValue": `blob`,
               "BooleanValue": `boolean`,
               "DatetimeValue": `number`,
               "NumberValue": "`string`",
               "StringValue": "`string`"
            },
            "StartMode": "`string`",
            "StartValue": { 
               "BinaryValue": `blob`,
               "BooleanValue": `boolean`,
               "DatetimeValue": `number`,
               "NumberValue": "`string`",
               "StringValue": "`string`"
            }
         }
      }
   ]
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[ConsistencyLevel](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


The consistency level to execute the request at.


Valid Values: `SERIALIZABLE | EVENTUAL`





**[DirectoryArn](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


The ARN of the directory that the index exists in.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[IndexReference](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


The reference to the index to list.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**[MaxResults](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


The maximum number of objects in a single page to retrieve from the index during a request. For more information, see [Amazon Cloud Directory Limits](../developerguide/limits.md "../developerguide/limits.md").


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**[NextToken](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


The pagination token.


Type: String


Required: No




**[RangesOnIndexedValues](#API_ListIndex_RequestSyntax "#API_ListIndex_RequestSyntax")**


Specifies the ranges of indexed values that you want to query.


Type: Array of [ObjectAttributeRange](API_ObjectAttributeRange.md "API_ObjectAttributeRange.md") objects


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "IndexAttachments": [ 
      { 
         "IndexedAttributes": [ 
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
         ],
         "ObjectIdentifier": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[IndexAttachments](#API_ListIndex_ResponseSyntax "#API_ListIndex_ResponseSyntax")**


The objects and indexed values attached to the index.


Type: Array of [IndexAttachment](API_IndexAttachment.md "API_IndexAttachment.md") objects




**[NextToken](#API_ListIndex_ResponseSyntax "#API_ListIndex_ResponseSyntax")**


The pagination token.


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




**InvalidNextTokenException** 


Indicates that the `NextToken` value is not valid.


HTTP Status Code: 400




**LimitExceededException** 


Indicates that limits are exceeded. See [Limits](../developerguide/limits.md "../developerguide/limits.md") for more information.


HTTP Status Code: 400




**NotIndexException** 


Indicates that the requested operation can only operate on index objects.


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


This example illustrates one usage of ListIndex.



```
POST /amazonclouddirectory/2017-01-11/index/targets HTTP/1.1
Host: clouddirectory.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 83
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI7E3BYXS3example/20171017/us-west-2/clouddirectory/aws4_request, SignedHeaders=host;x-amz-data-partition;x-amz-date, Signature=e10557e84c0fb9fd30e6a018a02b51ecbac72a389e2dd20090e516d3023872e4
x-amz-data-partition: arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY
X-Amz-Date: 20171017T221341Z
User-Agent: aws-cli/1.11.150 Python/2.7.9 Windows/8 botocore/1.7.8

{
	"IndexReference": {
		"Selector": "$AQGG_ADlfNZBzYHY_JgDt3TW45F26R1HTY2z-stwKBte_Q"
	}
}
```

### Example Response


This example illustrates one usage of ListIndex.



```
HTTP/1.1 200 OK
x-amzn-RequestId: 2920690c-b38d-11e7-bd9d-f9e3493b0666
Date: Tue, 17 Oct 2017 22:47:31 GMT
x-amzn-RequestId: 2920690c-b38d-11e7-bd9d-f9e3493b0666
Content-Type: application/json
Content-Length: 404

{
	"IndexAttachments": [{
		"IndexedAttributes": [{
			"Key": {
				"FacetName": "Organization",
				"Name": "description",
				"SchemaArn": "arn:aws:clouddirectory:us-west-2:45132example:directory/AYb8AOV81kHNgdj8mAO3dNY/schema/org/1"
			},
			"Value": {
				"BinaryValue": null,
				"BooleanValue": null,
				"DatetimeValue": null,
				"NumberValue": null,
				"StringValue": null
			}
		}],
		"ObjectIdentifier": "AQGG_ADlfNZBzYHY_JgDt3TWcU7IARvOTeaR09zme1sVsw"
	}],
	"NextToken": null
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListIndex")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListIndex "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListIndex")
