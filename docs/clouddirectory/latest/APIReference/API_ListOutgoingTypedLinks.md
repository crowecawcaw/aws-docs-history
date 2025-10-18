Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# ListOutgoingTypedLinks

Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md")
 information for an object. It also supports filtering by typed link facet and identity
 attributes. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


## Request Syntax



```
POST /amazonclouddirectory/2017-01-11/typedlink/outgoing HTTP/1.1
x-amz-data-partition: `DirectoryArn`
Content-type: application/json

{
   "ConsistencyLevel": "`string`",
   "FilterAttributeRanges": [ 
      { 
         "AttributeName": "`string`",
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
   ],
   "FilterTypedLink": { 
      "SchemaArn": "`string`",
      "TypedLinkName": "`string`"
   },
   "MaxResults": `number`,
   "NextToken": "`string`",
   "ObjectReference": { 
      "Selector": "`string`"
   }
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[DirectoryArn](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


The Amazon Resource Name (ARN) of the directory where you want to list the typed
 links.


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[ConsistencyLevel](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


The consistency level to execute the request at.


Type: String


Valid Values: `SERIALIZABLE | EVENTUAL`



Required: No




**[FilterAttributeRanges](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


Provides range filters for multiple attributes. When providing ranges to typed link
 selection, any inexact ranges must be specified at the end. Any attributes that do not have a
 range specified are presumed to match the entire range.


Type: Array of [TypedLinkAttributeRange](API_TypedLinkAttributeRange.md "API_TypedLinkAttributeRange.md") objects


Required: No




**[FilterTypedLink](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


Filters are interpreted in the order of the attributes defined on the typed link facet,
 not the order they are supplied to any API calls.


Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md "API_TypedLinkSchemaAndFacetName.md") object


Required: No




**[MaxResults](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


The maximum number of results to retrieve.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**[NextToken](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


The pagination token.


Type: String


Required: No




**[ObjectReference](#API_ListOutgoingTypedLinks_RequestSyntax "#API_ListOutgoingTypedLinks_RequestSyntax")**


A reference that identifies the object whose attributes will be listed.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "TypedLinkSpecifiers": [ 
      { 
         "IdentityAttributeValues": [ 
            { 
               "AttributeName": "***string***",
               "Value": { 
                  "BinaryValue": ***blob***,
                  "BooleanValue": ***boolean***,
                  "DatetimeValue": ***number***,
                  "NumberValue": "***string***",
                  "StringValue": "***string***"
               }
            }
         ],
         "SourceObjectReference": { 
            "Selector": "***string***"
         },
         "TargetObjectReference": { 
            "Selector": "***string***"
         },
         "TypedLinkFacet": { 
            "SchemaArn": "***string***",
            "TypedLinkName": "***string***"
         }
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_ListOutgoingTypedLinks_ResponseSyntax "#API_ListOutgoingTypedLinks_ResponseSyntax")**


The pagination token.


Type: String




**[TypedLinkSpecifiers](#API_ListOutgoingTypedLinks_ResponseSyntax "#API_ListOutgoingTypedLinks_ResponseSyntax")**


Returns a typed link specifier as output.


Type: Array of [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md") objects




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListOutgoingTypedLinks")
