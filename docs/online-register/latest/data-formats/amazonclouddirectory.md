

# Data retrieval APIs for Amazon Cloud Directory
<a name="amazonclouddirectory"></a>

Amazon Cloud Directory provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="clouddirectory-BatchRead"></a>[BatchRead](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_BatchRead.html) | Perform all the read operations in a batch. Each individual operation inside BatchRead needs to be granted permissions explicitly | Read | 
| <a name="clouddirectory-GetAppliedSchemaVersion"></a>[GetAppliedSchemaVersion](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetAppliedSchemaVersion.html) | Return current applied schema version ARN, including the minor version in use | Read | 
| <a name="clouddirectory-GetDirectory"></a>[GetDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetDirectory.html) | Retrieve metadata about a directory | Read | 
| <a name="clouddirectory-GetFacet"></a>[GetFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetFacet.html) | Get details of the Facet, such as Facet Name, Attributes, Rules, or ObjectType | Read | 
| <a name="clouddirectory-GetLinkAttributes"></a>[GetLinkAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetLinkAttributes.html) | Retrieve attributes that are associated with a typed link | Read | 
| <a name="clouddirectory-GetObjectAttributes"></a>[GetObjectAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetObjectAttributes.html) | Retrieve attributes within a facet that are associated with an object | Read | 
| <a name="clouddirectory-GetObjectInformation"></a>[GetObjectInformation](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetObjectInformation.html) | Retrieve metadata about an object | Read | 
| <a name="clouddirectory-GetSchemaAsJson"></a>[GetSchemaAsJson](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetSchemaAsJson.html) | Retrieve a JSON representation of the schema | Read | 
| <a name="clouddirectory-GetTypedLinkFacetInformation"></a>[GetTypedLinkFacetInformation](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetTypedLinkFacetInformation.html) | Return identity attributes order information associated with a given typed link facet | Read | 
| <a name="clouddirectory-ListAppliedSchemaArns"></a>[ListAppliedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListAppliedSchemaArns.html) | List schemas applied to a directory | List | 
| <a name="clouddirectory-ListAttachedIndices"></a>[ListAttachedIndices](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListAttachedIndices.html) | List indices attached to an object | Read | 
| <a name="clouddirectory-ListDevelopmentSchemaArns"></a>[ListDevelopmentSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListDevelopmentSchemaArns.html) | Retrieve the ARNs of schemas in the development state | List | 
| <a name="clouddirectory-ListDirectories"></a>[ListDirectories](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListDirectories.html) | List directories created within an account | List | 
| <a name="clouddirectory-ListFacetAttributes"></a>[ListFacetAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListFacetAttributes.html) | Retrieve attributes attached to the facet | Read | 
| <a name="clouddirectory-ListFacetNames"></a>[ListFacetNames](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListFacetNames.html) | Retrieve the names of facets that exist in a schema | Read | 
| <a name="clouddirectory-ListIncomingTypedLinks"></a>[ListIncomingTypedLinks](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListIncomingTypedLinks.html) | Return a paginated list of all incoming TypedLinks for a given object | Read | 
| <a name="clouddirectory-ListIndex"></a>[ListIndex](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListIndex.html) | List objects attached to the specified index | Read | 
| <a name="clouddirectory-ListManagedSchemaArns"></a>[ListManagedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListManagedSchemaArns.html) | List the major version families of each managed schema. If a major version ARN is provided as SchemaArn, the minor version revisions in that family are listed instead | List | 
| <a name="clouddirectory-ListObjectAttributes"></a>[ListObjectAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectAttributes.html) | List all attributes associated with an object | Read | 
| <a name="clouddirectory-ListObjectChildren"></a>[ListObjectChildren](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectChildren.html) | Return a paginated list of child objects associated with a given object | Read | 
| <a name="clouddirectory-ListObjectParentPaths"></a>[ListObjectParentPaths](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectParentPaths.html) | Retrieve all available parent paths for any object type such as node, leaf node, policy node, and index node objects | Read | 
| <a name="clouddirectory-ListObjectParents"></a>[ListObjectParents](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectParents.html) | List parent objects associated with a given object in pagination fashion | Read | 
| <a name="clouddirectory-ListObjectPolicies"></a>[ListObjectPolicies](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectPolicies.html) | Return policies attached to an object in pagination fashion | Read | 
| <a name="clouddirectory-ListOutgoingTypedLinks"></a>[ListOutgoingTypedLinks](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListOutgoingTypedLinks.html) | Return a paginated list of all outgoing TypedLinks for a given object | Read | 
| <a name="clouddirectory-ListPolicyAttachments"></a>[ListPolicyAttachments](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListPolicyAttachments.html) | Return all of the ObjectIdentifiers to which a given policy is attached | Read | 
| <a name="clouddirectory-ListPublishedSchemaArns"></a>[ListPublishedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListPublishedSchemaArns.html) | Retrieve published schema ARNs | List | 
| <a name="clouddirectory-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTagsForResource.html) | Return tags for a resource | Read | 
| <a name="clouddirectory-ListTypedLinkFacetAttributes"></a>[ListTypedLinkFacetAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTypedLinkFacetAttributes.html) | Return a paginated list of attributes associated with typed link facet | Read | 
| <a name="clouddirectory-ListTypedLinkFacetNames"></a>[ListTypedLinkFacetNames](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTypedLinkFacetNames.html) | Return a paginated list of typed link facet names that exist in a schema | Read | 
| <a name="clouddirectory-LookupPolicy"></a>[LookupPolicy](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_LookupPolicy.html) | List all policies from the root of the Directory to the object specified | Read | 