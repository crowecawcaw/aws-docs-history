Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# TypedLinkSpecifier

Contains all the information that is used to uniquely identify a typed link. The
 parameters discussed in this topic are used to uniquely specify the typed link being operated
 on. The [AttachTypedLink](API_AttachTypedLink.md "API_AttachTypedLink.md") API returns a typed link specifier while the [DetachTypedLink](API_DetachTypedLink.md "API_DetachTypedLink.md") API accepts one as input. Similarly, the [ListIncomingTypedLinks](API_ListIncomingTypedLinks.md "API_ListIncomingTypedLinks.md") and [ListOutgoingTypedLinks](API_ListOutgoingTypedLinks.md "API_ListOutgoingTypedLinks.md") API
 operations provide typed link specifiers as output. You can also construct a typed link
 specifier from scratch.


## Contents





**IdentityAttributeValues** 


Identifies the attribute value to update.


Type: Array of [AttributeNameAndValue](API_AttributeNameAndValue.md "API_AttributeNameAndValue.md") objects


Required: Yes




**SourceObjectReference** 


Identifies the source object that the typed link will attach to.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**TargetObjectReference** 


Identifies the target object that the typed link will attach to.


Type: [ObjectReference](API_ObjectReference.md "API_ObjectReference.md") object


Required: Yes




**TypedLinkFacet** 


Identifies the typed link facet that is associated with the typed link.


Type: [TypedLinkSchemaAndFacetName](API_TypedLinkSchemaAndFacetName.md "API_TypedLinkSchemaAndFacetName.md") object


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkSpecifier "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/TypedLinkSpecifier")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkSpecifier "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/TypedLinkSpecifier")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkSpecifier "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/TypedLinkSpecifier")
