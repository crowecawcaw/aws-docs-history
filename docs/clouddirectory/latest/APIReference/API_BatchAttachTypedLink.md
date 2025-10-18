Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchAttachTypedLink

Attaches a typed link to a specified source and target object inside a [BatchRead](API_BatchRead.md "API_BatchRead.md") operation. For more information, see [AttachTypedLink](API_AttachTypedLink.md "API_AttachTypedLink.md") and [BatchRead:Operations](API_BatchRead.md#amazoncds-BatchRead-request-Operations "API_BatchRead.md#amazoncds-BatchRead-request-Operations").


## Contents





**Attributes** 


A set of attributes that are associated with the typed link.


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



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachTypedLink "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchAttachTypedLink")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachTypedLink "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchAttachTypedLink")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachTypedLink "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchAttachTypedLink")
