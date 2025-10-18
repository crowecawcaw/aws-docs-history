Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchWriteOperation

Represents the output of a `BatchWrite` operation. 


## Contents





**AddFacetToObject** 


A batch operation that adds a facet to an object.


Type: [BatchAddFacetToObject](API_BatchAddFacetToObject.md "API_BatchAddFacetToObject.md") object


Required: No




**AttachObject** 


Attaches an object to a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchAttachObject](API_BatchAttachObject.md "API_BatchAttachObject.md") object


Required: No




**AttachPolicy** 


Attaches a policy object to a regular object. An object can have a limited number of attached
 policies.


Type: [BatchAttachPolicy](API_BatchAttachPolicy.md "API_BatchAttachPolicy.md") object


Required: No




**AttachToIndex** 


Attaches the specified object to the specified index.


Type: [BatchAttachToIndex](API_BatchAttachToIndex.md "API_BatchAttachToIndex.md") object


Required: No




**AttachTypedLink** 


Attaches a typed link to a specified source and target object. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchAttachTypedLink](API_BatchAttachTypedLink.md "API_BatchAttachTypedLink.md") object


Required: No




**CreateIndex** 


Creates an index object. See [Indexing and search](../developerguide/indexing_search.md "../developerguide/indexing_search.md") for more information.


Type: [BatchCreateIndex](API_BatchCreateIndex.md "API_BatchCreateIndex.md") object


Required: No




**CreateObject** 


Creates an object.


Type: [BatchCreateObject](API_BatchCreateObject.md "API_BatchCreateObject.md") object


Required: No




**DeleteObject** 


Deletes an object in a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDeleteObject](API_BatchDeleteObject.md "API_BatchDeleteObject.md") object


Required: No




**DetachFromIndex** 


Detaches the specified object from the specified index.


Type: [BatchDetachFromIndex](API_BatchDetachFromIndex.md "API_BatchDetachFromIndex.md") object


Required: No




**DetachObject** 


Detaches an object from a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDetachObject](API_BatchDetachObject.md "API_BatchDetachObject.md") object


Required: No




**DetachPolicy** 


Detaches a policy from a [Directory](API_Directory.md "API_Directory.md").


Type: [BatchDetachPolicy](API_BatchDetachPolicy.md "API_BatchDetachPolicy.md") object


Required: No




**DetachTypedLink** 


Detaches a typed link from a specified source and target object. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchDetachTypedLink](API_BatchDetachTypedLink.md "API_BatchDetachTypedLink.md") object


Required: No




**RemoveFacetFromObject** 


A batch operation that removes a facet from an object.


Type: [BatchRemoveFacetFromObject](API_BatchRemoveFacetFromObject.md "API_BatchRemoveFacetFromObject.md") object


Required: No




**UpdateLinkAttributes** 


Updates a given object's attributes.


Type: [BatchUpdateLinkAttributes](API_BatchUpdateLinkAttributes.md "API_BatchUpdateLinkAttributes.md") object


Required: No




**UpdateObjectAttributes** 


Updates a given object's attributes.


Type: [BatchUpdateObjectAttributes](API_BatchUpdateObjectAttributes.md "API_BatchUpdateObjectAttributes.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperation "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchWriteOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchWriteOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchWriteOperation")
