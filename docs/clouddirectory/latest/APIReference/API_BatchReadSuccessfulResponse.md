Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# BatchReadSuccessfulResponse

Represents the output of a `BatchRead` success response operation.


## Contents





**GetLinkAttributes** 


The list of attributes to retrieve from the typed link.


Type: [BatchGetLinkAttributesResponse](API_BatchGetLinkAttributesResponse.md "API_BatchGetLinkAttributesResponse.md") object


Required: No




**GetObjectAttributes** 


Retrieves attributes within a facet that are associated with an object.


Type: [BatchGetObjectAttributesResponse](API_BatchGetObjectAttributesResponse.md "API_BatchGetObjectAttributesResponse.md") object


Required: No




**GetObjectInformation** 


Retrieves metadata about an object.


Type: [BatchGetObjectInformationResponse](API_BatchGetObjectInformationResponse.md "API_BatchGetObjectInformationResponse.md") object


Required: No




**ListAttachedIndices** 


Lists indices attached to an object.


Type: [BatchListAttachedIndicesResponse](API_BatchListAttachedIndicesResponse.md "API_BatchListAttachedIndicesResponse.md") object


Required: No




**ListIncomingTypedLinks** 


Returns a paginated list of all the incoming [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md")
 information for an object. It also supports filtering by typed link facet and identity
 attributes. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchListIncomingTypedLinksResponse](API_BatchListIncomingTypedLinksResponse.md "API_BatchListIncomingTypedLinksResponse.md") object


Required: No




**ListIndex** 


Lists objects attached to the specified index.


Type: [BatchListIndexResponse](API_BatchListIndexResponse.md "API_BatchListIndexResponse.md") object


Required: No




**ListObjectAttributes** 


Lists all attributes that are associated with an object.


Type: [BatchListObjectAttributesResponse](API_BatchListObjectAttributesResponse.md "API_BatchListObjectAttributesResponse.md") object


Required: No




**ListObjectChildren** 


Returns a paginated list of child objects that are associated with a given
 object.


Type: [BatchListObjectChildrenResponse](API_BatchListObjectChildrenResponse.md "API_BatchListObjectChildrenResponse.md") object


Required: No




**ListObjectParentPaths** 


Retrieves all available parent paths for any object type such as node, leaf node,
 policy node, and index node objects. For more information about objects, see [Directory Structure](../developerguide/key_concepts_directorystructure.md "../developerguide/key_concepts_directorystructure.md").


Type: [BatchListObjectParentPathsResponse](API_BatchListObjectParentPathsResponse.md "API_BatchListObjectParentPathsResponse.md") object


Required: No




**ListObjectParents** 


The list of parent objects to retrieve.


Type: [BatchListObjectParentsResponse](API_BatchListObjectParentsResponse.md "API_BatchListObjectParentsResponse.md") object


Required: No




**ListObjectPolicies** 


Returns policies attached to an object in pagination fashion.


Type: [BatchListObjectPoliciesResponse](API_BatchListObjectPoliciesResponse.md "API_BatchListObjectPoliciesResponse.md") object


Required: No




**ListOutgoingTypedLinks** 


Returns a paginated list of all the outgoing [TypedLinkSpecifier](API_TypedLinkSpecifier.md "API_TypedLinkSpecifier.md")
 information for an object. It also supports filtering by typed link facet and identity
 attributes. For more information, see [Typed Links](../developerguide/directory_objects_links.md#directory_objects_links_typedlink "../developerguide/directory_objects_links.md#directory_objects_links_typedlink").


Type: [BatchListOutgoingTypedLinksResponse](API_BatchListOutgoingTypedLinksResponse.md "API_BatchListOutgoingTypedLinksResponse.md") object


Required: No




**ListPolicyAttachments** 


Returns all of the `ObjectIdentifiers` to which a given policy is attached.


Type: [BatchListPolicyAttachmentsResponse](API_BatchListPolicyAttachmentsResponse.md "API_BatchListPolicyAttachmentsResponse.md") object


Required: No




**LookupPolicy** 


Lists all policies from the root of the [Directory](API_Directory.md "API_Directory.md") to the object
 specified. If there are no policies present, an empty list is returned. If policies are
 present, and if some objects don't have the policies attached, it returns the `ObjectIdentifier`
 for such objects. If policies are present, it returns `ObjectIdentifier`, `policyId`, and
 `policyType`. Paths that don't lead to the root from the target object are ignored. For more
 information, see [Policies](../developerguide/key_concepts_directory.md#key_concepts_policies "../developerguide/key_concepts_directory.md#key_concepts_policies").


Type: [BatchLookupPolicyResponse](API_BatchLookupPolicyResponse.md "API_BatchLookupPolicyResponse.md") object


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadSuccessfulResponse "https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/BatchReadSuccessfulResponse")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadSuccessfulResponse "https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/BatchReadSuccessfulResponse")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadSuccessfulResponse "https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/BatchReadSuccessfulResponse")
