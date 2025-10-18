Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchListObjectAttributes

Represents the output of a [ListObjectAttributes](API_ListObjectAttributes.md "API_ListObjectAttributes.md") operation.


## Contents





**ObjectReference** 


Reference of the object whose attributes need to be listed.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**FacetFilter** 


Used to filter the list of object attributes that are associated with a certain
 facet.


Type: [SchemaFacet](API_SchemaFacet.md "API_SchemaFacet.md") object


Required: No




**MaxResults** 


The maximum number of items to be retrieved in a single call. This is an approximate
 number.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**NextToken** 


The pagination token.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectAttributes "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchListObjectAttributes")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectAttributes "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchListObjectAttributes")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectAttributes "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchListObjectAttributes")
