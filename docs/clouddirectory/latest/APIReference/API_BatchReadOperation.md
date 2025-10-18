Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchReadOperation

Represents the output of a `BatchRead` operation.


## Contents





**GetLinkAttributes** 


Retrieves attributes that are associated with a typed link.


Type: [BatchGetLinkAttributes](API_BatchGetLinkAttributes.md "API_BatchGetLinkAttributes.md") object


Required: No




**GetObjectAttributes** 


Retrieves attributes within a facet that are associated with an object.


Type: [BatchGetObjectAttributes](API_BatchGetObjectAttributes.md "API_BatchGetObjectAttributes.md") object


Required: No




**GetObjectInformation** 


Retrieves metadata about an object.


Type: [BatchGetObjectInformation](API_BatchGetObjectInformation.md "API_BatchGetObjectInformation.md") object


Required: No




**ListAttachedIndices** 


Lists indices attached to an object.


Type: [BatchListAttachedIndices](API_BatchListAttachedIndices.md "API_BatchListAttachedIndices.md") object


Required: No




**ListIncomingTypedLinks** 


Returns a paginated list of all the incoming [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md")
 information for an object. It also supports filtering by typed link facet and identity
 attributes. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchListIncomingTypedLinks](API_BatchListIncomingTypedLinks.md "API_BatchListIncomingTypedLinks.md") object


Required: No




**ListIndex** 


Lists objects attached to the specified index.


Type: [BatchListIndex](API_BatchListIndex.md "API_BatchListIndex.md") object


Required: No




**ListObjectAttributes** 


Lists all attributes that are associated with an object.


Type: [BatchListObjectAttributes](API_BatchListObjectAttributes.md "API_BatchListObjectAttributes.md") object


Required: No




**ListObjectChildren** 


Returns a paginated list of child objects that are associated with a given
 object.


Type: [BatchListObjectChildren](API_BatchListObjectChildren.md "API_BatchListObjectChildren.md") object


Required: No




**ListObjectParentPaths** 


Retrieves all available parent paths for any object type such as node, leaf node,
 policy node, and index node objects. For more information about objects, see [Directory Structure](../developerguide/key_concepts_directorystructure.md "../developerguide/key_concepts_directorystructure.md").


Type: [BatchListObjectParentPaths](API_BatchListObjectParentPaths.md "API_BatchListObjectParentPaths.md") object


Required: No




**ListObjectParents** 


Lists parent objects that are associated with a given object in pagination
 fashion.


Type: [BatchListObjectParents](API_BatchListObjectParents.md "API_BatchListObjectParents.md") object


Required: No




**ListObjectPolicies** 


Returns policies attached to an object in pagination fashion.


Type: [BatchListObjectPolicies](API_BatchListObjectPolicies.md "API_BatchListObjectPolicies.md") object


Required: No




**ListOutgoingTypedLinks** 


Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md")
 information for an object. It also supports filtering by typed link facet and identity
 attributes. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchListOutgoingTypedLinks](API_BatchListOutgoingTypedLinks.md "API_BatchListOutgoingTypedLinks.md") object


Required: No




**ListPolicyAttachments** 


Returns all of the `ObjectIdentifiers` to which a given policy is attached.


Type: [BatchListPolicyAttachments](API_BatchListPolicyAttachments.md "API_BatchListPolicyAttachments.md") object


Required: No




**LookupPolicy** 


Lists all policies from the root of the [Directory](API_Directory.md "API_Directory.md") to the object
 specified. If there are no policies present, an empty list is returned. If policies are
 present, and if some objects don't have the policies attached, it returns the `ObjectIdentifier`
 for such objects. If policies are present, it returns `ObjectIdentifier`, `policyId`, and
 `policyType`. Paths that don't lead to the root from the target object are ignored. For more
 information, see [Policies](../developerguide/key_concepts_directory.md#key_concepts_policies "../developerguide/key_concepts_directory.md#key_concepts_policies").


Type: [BatchLookupPolicy](API_BatchLookupPolicy.md "API_BatchLookupPolicy.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadOperation "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadOperation")
