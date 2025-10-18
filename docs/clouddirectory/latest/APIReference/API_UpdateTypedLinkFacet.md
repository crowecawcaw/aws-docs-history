Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# UpdateTypedLinkFacet

Updates a [TypedLinkFacet](API_TypedLinkFacet.md "API_TypedLinkFacet.md"). For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


## Request Syntax



```
PUT /amazonclouddirectory/2017-01-11/typedlink/facet HTTP/1.1
x-amz-data-partition: `SchemaArn`
Content-type: application/json

{
   "AttributeUpdates": [ 
      { 
         "Action": "`string`",
         "Attribute": { 
            "DefaultValue": { 
               "BinaryValue": `blob`,
               "BooleanValue": `boolean`,
               "DatetimeValue": `number`,
               "NumberValue": "`string`",
               "StringValue": "`string`"
            },
            "IsImmutable": `boolean`,
            "Name": "`string`",
            "RequiredBehavior": "`string`",
            "Rules": { 
               "`string`" : { 
                  "Parameters": { 
                     "`string`" : "`string`" 
                  },
                  "Type": "`string`"
               }
            },
            "Type": "`string`"
         }
      }
   ],
   "IdentityAttributeOrder": [ "`string`" ],
   "Name": "`string`"
}
```

## URI Request Parameters


The request uses the following URI parameters.





**[SchemaArn](#API_UpdateTypedLinkFacet_RequestSyntax "#API_UpdateTypedLinkFacet_RequestSyntax")**


The Amazon Resource Name (ARN) that is associated with the schema. For more
 information, see [Arn Examples](arns.md "arns.md").


Required: Yes




## Request Body


The request accepts the following data in JSON format.





**[AttributeUpdates](#API_UpdateTypedLinkFacet_RequestSyntax "#API_UpdateTypedLinkFacet_RequestSyntax")**


Attributes update structure.


Type: Array of [TypedLinkFacetAttributeUpdate](API_TypedLinkFacetAttributeUpdate.md "API_TypedLinkFacetAttributeUpdate.md") objects


Required: Yes




**[IdentityAttributeOrder](#API_UpdateTypedLinkFacet_RequestSyntax "#API_UpdateTypedLinkFacet_RequestSyntax")**


The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed
 links considers the order that the attributes are defined on the typed link facet. When
 providing ranges to a typed link selection, any inexact ranges must be specified at the end.
 Any attributes that do not have a range specified are presumed to match the entire range.
 Filters are interpreted in the order of the attributes on the typed link facet, not the order
 in which they are supplied to any API calls. For more information about identity attributes, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 230.


Pattern: `^[a-zA-Z0-9._:-]*$`



Required: Yes




**[Name](#API_UpdateTypedLinkFacet_RequestSyntax "#API_UpdateTypedLinkFacet_RequestSyntax")**


The unique name of the typed link facet.


Type: String


Pattern: `^[a-zA-Z0-9._-]*$`



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




**FacetNotFoundException** 


The specified [Facet](API_Facet.md "API_Facet.md") could not be found.


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




**InvalidFacetUpdateException** 


An attempt to modify a [Facet](API_Facet.md "API_Facet.md") resulted in an invalid schema
 exception.


HTTP Status Code: 400




**InvalidRuleException** 


Occurs when any of the rule parameter keys or values are invalid.


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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/DotNetSDKV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/UpdateTypedLinkFacet")
