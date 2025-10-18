Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchListOutgoingTypedLinks

Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md") information for an object inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [ListOutgoingTypedLinks](API_ListOutgoingTypedLinks.md "API_ListOutgoingTypedLinks.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**ObjectReference** 


The reference that identifies the object whose attributes will be listed.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**FilterAttributeRanges** 


Provides range filters for multiple attributes. When providing ranges to typed link
 selection, any inexact ranges must be specified at the end. Any attributes that do not have a
 range specified are presumed to match the entire range.


Type: Array of [TypedLinkAttributeRange](API_TypedLinkAttributeRange.md "API_TypedLinkAttributeRange.md") objects


Required: No




**FilterTypedLink** 


Filters are interpreted in the order of the attributes defined on the typed link facet,
 not the order they are supplied to any API calls.


Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md "API_TypedLinkSchemaAndFacetName.md") object


Required: No




**MaxResults** 


The maximum number of results to retrieve.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**NextToken** 


The pagination token.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListOutgoingTypedLinks")
