Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchWriteOperationResponse

Represents the output of a `BatchWrite` response operation.


## Contents





**AddFacetToObject** 


The result of an add facet to object batch operation.


Type: [BatchAddFacetToObjectResponse](API_BatchAddFacetToObjectResponse.md "API_BatchAddFacetToObjectResponse.md") object


Required: No




**AttachObject** 


Attaches an object to a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchAttachObjectResponse](API_BatchAttachObjectResponse.md "API_BatchAttachObjectResponse.md") object


Required: No




**AttachPolicy** 


Attaches a policy object to a regular object. An object can have a limited number of attached
 policies.


Type: [BatchAttachPolicyResponse](API_BatchAttachPolicyResponse.md "API_BatchAttachPolicyResponse.md") object


Required: No




**AttachToIndex** 


Attaches the specified object to the specified index.


Type: [BatchAttachToIndexResponse](API_BatchAttachToIndexResponse.md "API_BatchAttachToIndexResponse.md") object


Required: No




**AttachTypedLink** 


Attaches a typed link to a specified source and target object. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchAttachTypedLinkResponse](API_BatchAttachTypedLinkResponse.md "API_BatchAttachTypedLinkResponse.md") object


Required: No




**CreateIndex** 


Creates an index object. See [Indexing and search](../developerguide/indexing_search.md "../developerguide/indexing_search.md") for more information.


Type: [BatchCreateIndexResponse](API_BatchCreateIndexResponse.md "API_BatchCreateIndexResponse.md") object


Required: No




**CreateObject** 


Creates an object in a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchCreateObjectResponse](API_BatchCreateObjectResponse.md "API_BatchCreateObjectResponse.md") object


Required: No




**DeleteObject** 


Deletes an object in a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDeleteObjectResponse](API_BatchDeleteObjectResponse.md "API_BatchDeleteObjectResponse.md") object


Required: No




**DetachFromIndex** 


Detaches the specified object from the specified index.


Type: [BatchDetachFromIndexResponse](API_BatchDetachFromIndexResponse.md "API_BatchDetachFromIndexResponse.md") object


Required: No




**DetachObject** 


Detaches an object from a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDetachObjectResponse](API_BatchDetachObjectResponse.md "API_BatchDetachObjectResponse.md") object


Required: No




**DetachPolicy** 


Detaches a policy from a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDetachPolicyResponse](API_BatchDetachPolicyResponse.md "API_BatchDetachPolicyResponse.md") object


Required: No




**DetachTypedLink** 


Detaches a typed link from a specified source and target object. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchDetachTypedLinkResponse](API_BatchDetachTypedLinkResponse.md "API_BatchDetachTypedLinkResponse.md") object


Required: No




**RemoveFacetFromObject** 


The result of a batch remove facet from object operation.


Type: [BatchRemoveFacetFromObjectResponse](API_BatchRemoveFacetFromObjectResponse.md "API_BatchRemoveFacetFromObjectResponse.md") object


Required: No




**UpdateLinkAttributes** 


Represents the output of a `BatchWrite` response operation.


Type: [BatchUpdateLinkAttributesResponse](API_BatchUpdateLinkAttributesResponse.md "API_BatchUpdateLinkAttributesResponse.md") object


Required: No




**UpdateObjectAttributes** 


Updates a given object’s attributes.


Type: [BatchUpdateObjectAttributesResponse](API_BatchUpdateObjectAttributesResponse.md "API_BatchUpdateObjectAttributesResponse.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperationResponse "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperationResponse")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperationResponse "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperationResponse")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperationResponse "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperationResponse")
