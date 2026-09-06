

# Actions, resources, and condition keys for Amazon Cloud Directory
<a name="list_clouddirectory"></a>

Amazon Cloud Directory (service prefix: `clouddirectory`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_amazon_cd.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/directoryservice/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_AuthNAccess.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/clouddirectory/clouddirectory.json) for this service.

**Topics**
+ [API operations defined by Amazon Cloud Directory](#list_clouddirectory-operations)
+ [Actions defined by Amazon Cloud Directory](#list_clouddirectory-actions-as-permissions)
+ [Resource types defined by Amazon Cloud Directory](#list_clouddirectory-resources-for-iam-policies)
+ [Condition keys for Amazon Cloud Directory](#list_clouddirectory-policy-keys)

## API operations defined by Amazon Cloud Directory
<a name="list_clouddirectory-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_clouddirectory-actions-as-permissions).




- **   AddFacetToObject  **
  - **IAM action:**  [clouddirectory:AddFacetToObject](#list_clouddirectory-action-AddFacetToObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ApplySchema  **
  - **IAM action:**  [clouddirectory:ApplySchema](#list_clouddirectory-action-ApplySchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachObject  **
  - **IAM action:**  [clouddirectory:AttachObject](#list_clouddirectory-action-AttachObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachPolicy  **
  - **IAM action:**  [clouddirectory:AttachPolicy](#list_clouddirectory-action-AttachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachToIndex  **
  - **IAM action:**  [clouddirectory:AttachToIndex](#list_clouddirectory-action-AttachToIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachTypedLink  **
  - **IAM action:**  [clouddirectory:AttachTypedLink](#list_clouddirectory-action-AttachTypedLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchRead  **
  - **IAM action:**  [clouddirectory:BatchRead](#list_clouddirectory-action-BatchRead)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:GetLinkAttributes](#list_clouddirectory-action-GetLinkAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:GetObjectAttributes](#list_clouddirectory-action-GetObjectAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:GetObjectInformation](#list_clouddirectory-action-GetObjectInformation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListAttachedIndices](#list_clouddirectory-action-ListAttachedIndices)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListIncomingTypedLinks](#list_clouddirectory-action-ListIncomingTypedLinks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListIndex](#list_clouddirectory-action-ListIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListObjectAttributes](#list_clouddirectory-action-ListObjectAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListObjectChildren](#list_clouddirectory-action-ListObjectChildren)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListObjectParentPaths](#list_clouddirectory-action-ListObjectParentPaths)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListObjectParents](#list_clouddirectory-action-ListObjectParents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListObjectPolicies](#list_clouddirectory-action-ListObjectPolicies)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListOutgoingTypedLinks](#list_clouddirectory-action-ListOutgoingTypedLinks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:ListPolicyAttachments](#list_clouddirectory-action-ListPolicyAttachments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [clouddirectory:LookupPolicy](#list_clouddirectory-action-LookupPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchWrite  **
  - **IAM action:**  [clouddirectory:AddFacetToObject](#list_clouddirectory-action-AddFacetToObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:AttachObject](#list_clouddirectory-action-AttachObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:AttachPolicy](#list_clouddirectory-action-AttachPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:AttachToIndex](#list_clouddirectory-action-AttachToIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:AttachTypedLink](#list_clouddirectory-action-AttachTypedLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:BatchWrite](#list_clouddirectory-action-BatchWrite)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:CreateIndex](#list_clouddirectory-action-CreateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:CreateObject](#list_clouddirectory-action-CreateObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:DeleteObject](#list_clouddirectory-action-DeleteObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:DetachFromIndex](#list_clouddirectory-action-DetachFromIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:DetachObject](#list_clouddirectory-action-DetachObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:DetachTypedLink](#list_clouddirectory-action-DetachTypedLink)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:RemoveFacetFromObject](#list_clouddirectory-action-RemoveFacetFromObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:UpdateLinkAttributes](#list_clouddirectory-action-UpdateLinkAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:UpdateObjectAttributes](#list_clouddirectory-action-UpdateObjectAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDirectory  **
  - **IAM action:**  [clouddirectory:CreateDirectory](#list_clouddirectory-action-CreateDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFacet  **
  - **IAM action:**  [clouddirectory:CreateFacet](#list_clouddirectory-action-CreateFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIndex  **
  - **IAM action:**  [clouddirectory:AttachObject](#list_clouddirectory-action-AttachObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:CreateIndex](#list_clouddirectory-action-CreateIndex)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateObject  **
  - **IAM action:**  [clouddirectory:AttachObject](#list_clouddirectory-action-AttachObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [clouddirectory:CreateObject](#list_clouddirectory-action-CreateObject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSchema  **
  - **IAM action:**  [clouddirectory:CreateSchema](#list_clouddirectory-action-CreateSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTypedLinkFacet  **
  - **IAM action:**  [clouddirectory:CreateTypedLinkFacet](#list_clouddirectory-action-CreateTypedLinkFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectory  **
  - **IAM action:**  [clouddirectory:DeleteDirectory](#list_clouddirectory-action-DeleteDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFacet  **
  - **IAM action:**  [clouddirectory:DeleteFacet](#list_clouddirectory-action-DeleteFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteObject  **
  - **IAM action:**  [clouddirectory:DeleteObject](#list_clouddirectory-action-DeleteObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchema  **
  - **IAM action:**  [clouddirectory:DeleteSchema](#list_clouddirectory-action-DeleteSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTypedLinkFacet  **
  - **IAM action:**  [clouddirectory:DeleteTypedLinkFacet](#list_clouddirectory-action-DeleteTypedLinkFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachFromIndex  **
  - **IAM action:**  [clouddirectory:DetachFromIndex](#list_clouddirectory-action-DetachFromIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachObject  **
  - **IAM action:**  [clouddirectory:DetachObject](#list_clouddirectory-action-DetachObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachPolicy  **
  - **IAM action:**  [clouddirectory:DetachPolicy](#list_clouddirectory-action-DetachPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetachTypedLink  **
  - **IAM action:**  [clouddirectory:DetachTypedLink](#list_clouddirectory-action-DetachTypedLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableDirectory  **
  - **IAM action:**  [clouddirectory:DisableDirectory](#list_clouddirectory-action-DisableDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDirectory  **
  - **IAM action:**  [clouddirectory:EnableDirectory](#list_clouddirectory-action-EnableDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAppliedSchemaVersion  **
  - **IAM action:**  [clouddirectory:GetAppliedSchemaVersion](#list_clouddirectory-action-GetAppliedSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDirectory  **
  - **IAM action:**  [clouddirectory:GetDirectory](#list_clouddirectory-action-GetDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFacet  **
  - **IAM action:**  [clouddirectory:GetFacet](#list_clouddirectory-action-GetFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLinkAttributes  **
  - **IAM action:**  [clouddirectory:GetLinkAttributes](#list_clouddirectory-action-GetLinkAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetObjectAttributes  **
  - **IAM action:**  [clouddirectory:GetObjectAttributes](#list_clouddirectory-action-GetObjectAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetObjectInformation  **
  - **IAM action:**  [clouddirectory:GetObjectInformation](#list_clouddirectory-action-GetObjectInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaAsJson  **
  - **IAM action:**  [clouddirectory:GetSchemaAsJson](#list_clouddirectory-action-GetSchemaAsJson) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTypedLinkFacetInformation  **
  - **IAM action:**  [clouddirectory:GetTypedLinkFacetInformation](#list_clouddirectory-action-GetTypedLinkFacetInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAppliedSchemaArns  **
  - **IAM action:**  [clouddirectory:ListAppliedSchemaArns](#list_clouddirectory-action-ListAppliedSchemaArns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAttachedIndices  **
  - **IAM action:**  [clouddirectory:ListAttachedIndices](#list_clouddirectory-action-ListAttachedIndices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevelopmentSchemaArns  **
  - **IAM action:**  [clouddirectory:ListDevelopmentSchemaArns](#list_clouddirectory-action-ListDevelopmentSchemaArns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDirectories  **
  - **IAM action:**  [clouddirectory:ListDirectories](#list_clouddirectory-action-ListDirectories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFacetAttributes  **
  - **IAM action:**  [clouddirectory:ListFacetAttributes](#list_clouddirectory-action-ListFacetAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFacetNames  **
  - **IAM action:**  [clouddirectory:ListFacetNames](#list_clouddirectory-action-ListFacetNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIncomingTypedLinks  **
  - **IAM action:**  [clouddirectory:ListIncomingTypedLinks](#list_clouddirectory-action-ListIncomingTypedLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListIndex  **
  - **IAM action:**  [clouddirectory:ListIndex](#list_clouddirectory-action-ListIndex) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListManagedSchemaArns  **
  - **IAM action:**  [clouddirectory:ListManagedSchemaArns](#list_clouddirectory-action-ListManagedSchemaArns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListObjectAttributes  **
  - **IAM action:**  [clouddirectory:ListObjectAttributes](#list_clouddirectory-action-ListObjectAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListObjectChildren  **
  - **IAM action:**  [clouddirectory:ListObjectChildren](#list_clouddirectory-action-ListObjectChildren) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListObjectParentPaths  **
  - **IAM action:**  [clouddirectory:ListObjectParentPaths](#list_clouddirectory-action-ListObjectParentPaths) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListObjectParents  **
  - **IAM action:**  [clouddirectory:ListObjectParents](#list_clouddirectory-action-ListObjectParents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListObjectPolicies  **
  - **IAM action:**  [clouddirectory:ListObjectPolicies](#list_clouddirectory-action-ListObjectPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOutgoingTypedLinks  **
  - **IAM action:**  [clouddirectory:ListOutgoingTypedLinks](#list_clouddirectory-action-ListOutgoingTypedLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPolicyAttachments  **
  - **IAM action:**  [clouddirectory:ListPolicyAttachments](#list_clouddirectory-action-ListPolicyAttachments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPublishedSchemaArns  **
  - **IAM action:**  [clouddirectory:ListPublishedSchemaArns](#list_clouddirectory-action-ListPublishedSchemaArns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [clouddirectory:ListTagsForResource](#list_clouddirectory-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTypedLinkFacetAttributes  **
  - **IAM action:**  [clouddirectory:ListTypedLinkFacetAttributes](#list_clouddirectory-action-ListTypedLinkFacetAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTypedLinkFacetNames  **
  - **IAM action:**  [clouddirectory:ListTypedLinkFacetNames](#list_clouddirectory-action-ListTypedLinkFacetNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   LookupPolicy  **
  - **IAM action:**  [clouddirectory:LookupPolicy](#list_clouddirectory-action-LookupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PublishSchema  **
  - **IAM action:**  [clouddirectory:PublishSchema](#list_clouddirectory-action-PublishSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSchemaFromJson  **
  - **IAM action:**  [clouddirectory:PutSchemaFromJson](#list_clouddirectory-action-PutSchemaFromJson) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveFacetFromObject  **
  - **IAM action:**  [clouddirectory:RemoveFacetFromObject](#list_clouddirectory-action-RemoveFacetFromObject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [clouddirectory:TagResource](#list_clouddirectory-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [clouddirectory:UntagResource](#list_clouddirectory-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateFacet  **
  - **IAM action:**  [clouddirectory:UpdateFacet](#list_clouddirectory-action-UpdateFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLinkAttributes  **
  - **IAM action:**  [clouddirectory:UpdateLinkAttributes](#list_clouddirectory-action-UpdateLinkAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateObjectAttributes  **
  - **IAM action:**  [clouddirectory:UpdateObjectAttributes](#list_clouddirectory-action-UpdateObjectAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSchema  **
  - **IAM action:**  [clouddirectory:UpdateSchema](#list_clouddirectory-action-UpdateSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTypedLinkFacet  **
  - **IAM action:**  [clouddirectory:UpdateTypedLinkFacet](#list_clouddirectory-action-UpdateTypedLinkFacet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeAppliedSchema  **
  - **IAM action:**  [clouddirectory:UpgradeAppliedSchema](#list_clouddirectory-action-UpgradeAppliedSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradePublishedSchema  **
  - **IAM action:**  [clouddirectory:UpgradePublishedSchema](#list_clouddirectory-action-UpgradePublishedSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Cloud Directory
<a name="list_clouddirectory-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddFacetToObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_AddFacetToObject.html)  **
  - **Description:** Grants permission to add a new Facet to an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ApplySchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ApplySchema.html)  **
  - **Description:** Grants permission to copy input published schema into Directory with same name and version as that of published schema
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [AttachObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_AttachObject.html)  **
  - **Description:** Grants permission to attach an existing object to another existing object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachPolicy](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_AttachPolicy.html)  **
  - **Description:** Grants permission to attach a policy object to any other object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachToIndex](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_AttachToIndex.html)  **
  - **Description:** Grants permission to attach the specified object to the specified index
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AttachTypedLink](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_AttachTypedLink.html)  **
  - **Description:** Grants permission to attach a typed link b/w a source & target object reference
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchRead](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_BatchRead.html)  **
  - **Description:** Grants permission to perform all the read operations in a batch. Each individual operation inside BatchRead needs to be granted permissions explicitly
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchWrite](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_BatchWrite.html)  **
  - **Description:** Grants permission to perform all the write operations in a batch. Each individual operation inside BatchWrite needs to be granted permissions explicitly
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateDirectory.html)  **
  - **Description:** Grants permission to create a Directory by copying the published schema into the directory
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateFacet.html)  **
  - **Description:** Grants permission to create a new Facet in a schema
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateIndex](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateIndex.html)  **
  - **Description:** Grants permission to create an index object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateObject.html)  **
  - **Description:** Grants permission to create an object in a Directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateSchema.html)  **
  - **Description:** Grants permission to create a new schema in a development state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTypedLinkFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_CreateTypedLinkFacet.html)  **
  - **Description:** Grants permission to create a new Typed Link facet in a schema
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DeleteDirectory.html)  **
  - **Description:** Grants permission to delete a directory. Only disabled directories can be deleted
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DeleteFacet.html)  **
  - **Description:** Grants permission to delete a given Facet. All attributes and Rules associated with the facet will be deleted
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DeleteObject.html)  **
  - **Description:** Grants permission to delete an object and its associated attributes
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DeleteSchema.html)  **
  - **Description:** Grants permission to delete a given schema
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTypedLinkFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DeleteTypedLinkFacet.html)  **
  - **Description:** Grants permission to delete a given TypedLink Facet. All attributes and Rules associated with the facet will be deleted
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DetachFromIndex](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DetachFromIndex.html)  **
  - **Description:** Grants permission to detach the specified object from the specified index
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DetachObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DetachObject.html)  **
  - **Description:** Grants permission to detach a given object from the parent object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DetachPolicy](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DetachPolicy.html)  **
  - **Description:** Grants permission to detach a policy from an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DetachTypedLink](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DetachTypedLink.html)  **
  - **Description:** Grants permission to detach a given typed link b/w given source and target object reference
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_DisableDirectory.html)  **
  - **Description:** Grants permission to disable the specified directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_EnableDirectory.html)  **
  - **Description:** Grants permission to enable the specified directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAppliedSchemaVersion](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetAppliedSchemaVersion.html)  **
  - **Description:** Grants permission to return current applied schema version ARN, including the minor version in use
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDirectory](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetDirectory.html)  **
  - **Description:** Grants permission to retrieve metadata about a directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetFacet.html)  **
  - **Description:** Grants permission to get details of the Facet, such as Facet Name, Attributes, Rules, or ObjectType
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [GetLinkAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetLinkAttributes.html)  **
  - **Description:** Grants permission to retrieve attributes that are associated with a typed link
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetObjectAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetObjectAttributes.html)  **
  - **Description:** Grants permission to retrieve attributes within a facet that are associated with an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetObjectInformation](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetObjectInformation.html)  **
  - **Description:** Grants permission to retrieve metadata about an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSchemaAsJson](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetSchemaAsJson.html)  **
  - **Description:** Grants permission to retrieve a JSON representation of the schema
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [GetTypedLinkFacetInformation](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_GetTypedLinkFacetInformation.html)  **
  - **Description:** Grants permission to return identity attributes order information associated with a given typed link facet
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [ListAppliedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListAppliedSchemaArns.html)  **
  - **Description:** Grants permission to list schemas applied to a directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAttachedIndices](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListAttachedIndices.html)  **
  - **Description:** Grants permission to list indices attached to an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDevelopmentSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListDevelopmentSchemaArns.html)  **
  - **Description:** Grants permission to retrieve the ARNs of schemas in the development state
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDirectories](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListDirectories.html)  **
  - **Description:** Grants permission to list directories created within an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFacetAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListFacetAttributes.html)  **
  - **Description:** Grants permission to retrieve attributes attached to the facet
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [ListFacetNames](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListFacetNames.html)  **
  - **Description:** Grants permission to retrieve the names of facets that exist in a schema
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [ListIncomingTypedLinks](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListIncomingTypedLinks.html)  **
  - **Description:** Grants permission to return a paginated list of all incoming TypedLinks for a given object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListIndex](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListIndex.html)  **
  - **Description:** Grants permission to list objects attached to the specified index
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListManagedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListManagedSchemaArns.html)  **
  - **Description:** Grants permission to list the major version families of each managed schema. If a major version ARN is provided as SchemaArn, the minor version revisions in that family are listed instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListObjectAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectAttributes.html)  **
  - **Description:** Grants permission to list all attributes associated with an object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListObjectChildren](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectChildren.html)  **
  - **Description:** Grants permission to return a paginated list of child objects associated with a given object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListObjectParentPaths](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectParentPaths.html)  **
  - **Description:** Grants permission to retrieve all available parent paths for any object type such as node, leaf node, policy node, and index node objects
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListObjectParents](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectParents.html)  **
  - **Description:** Grants permission to list parent objects associated with a given object in pagination fashion
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListObjectPolicies](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListObjectPolicies.html)  **
  - **Description:** Grants permission to return policies attached to an object in pagination fashion
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListOutgoingTypedLinks](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListOutgoingTypedLinks.html)  **
  - **Description:** Grants permission to return a paginated list of all outgoing TypedLinks for a given object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPolicyAttachments](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListPolicyAttachments.html)  **
  - **Description:** Grants permission to return all of the ObjectIdentifiers to which a given policy is attached
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPublishedSchemaArns](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListPublishedSchemaArns.html)  **
  - **Description:** Grants permission to retrieve published schema ARNs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return tags for a resource
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTypedLinkFacetAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTypedLinkFacetAttributes.html)  **
  - **Description:** Grants permission to return a paginated list of attributes associated with typed link facet
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [ListTypedLinkFacetNames](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_ListTypedLinkFacetNames.html)  **
  - **Description:** Grants permission to return a paginated list of typed link facet names that exist in a schema
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Read

- **   [LookupPolicy](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_LookupPolicy.html)  **
  - **Description:** Grants permission to list all policies from the root of the Directory to the object specified
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Read

- **   [PublishSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_PublishSchema.html)  **
  - **Description:** Grants permission to publish a development schema with a version
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutSchemaFromJson](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_PutSchemaFromJson.html)  **
  - **Description:** Grants permission to update a schema using JSON upload. Only available for development schemas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveFacetFromObject](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_RemoveFacetFromObject.html)  **
  - **Description:** Grants permission to remove the specified facet from the specified object
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UpdateFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpdateFacet.html)  **
  - **Description:** Grants permission to add/update/delete existing Attributes, Rules, or ObjectType of a Facet
  - **Resource types (\*required):** [appliedSchema\*](#list_clouddirectory-resource-appliedSchema) / **Condition keys:**  
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateLinkAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpdateLinkAttributes.html)  **
  - **Description:** Grants permission to update a given typed link's attributes. Attributes to be updated must not contribute to the typed link's identity, as defined by its IdentityAttributeOrder
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateObjectAttributes](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpdateObjectAttributes.html)  **
  - **Description:** Grants permission to update a given object's attributes
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpdateSchema.html)  **
  - **Description:** Grants permission to update the schema name with a new name
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateTypedLinkFacet](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpdateTypedLinkFacet.html)  **
  - **Description:** Grants permission to add/update/delete existing Attributes, Rules, identity attribute order of a TypedLink Facet
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpgradeAppliedSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpgradeAppliedSchema.html)  **
  - **Description:** Grants permission to upgrade a single directory in-place using the PublishedSchemaArn with schema updates found in MinorVersion. Backwards-compatible minor version upgrades are instantaneously available for readers on all objects in the directory
  - **Resource types (\*required):** [directory\*](#list_clouddirectory-resource-directory) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Write

- **   [UpgradePublishedSchema](https://docs.aws.amazon.com/directoryservice/latest/APIReference/API_UpgradePublishedSchema.html)  **
  - **Description:** Grants permission to upgrade a published schema under a new minor version revision using the current contents of DevelopmentSchemaArn
  - **Resource types (\*required):** [developmentSchema\*](#list_clouddirectory-resource-developmentSchema) / **Condition keys:**  
  - **Resource types (\*required):** [publishedSchema\*](#list_clouddirectory-resource-publishedSchema) / **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Cloud Directory
<a name="list_clouddirectory-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [appliedSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory)  | arn:${Partition}:clouddirectory:${Region}:${Account}:directory/${DirectoryId}/schema/${SchemaName}/${Version} |   | 
|  [developmentSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory)  | arn:${Partition}:clouddirectory:${Region}:${Account}:schema/development/${SchemaName} |   | 
|  [directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory)  | arn:${Partition}:clouddirectory:${Region}:${Account}:directory/${DirectoryId} |   | 
|  [publishedSchema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#whatisdirectory)  | arn:${Partition}:clouddirectory:${Region}:${Account}:schema/published/${SchemaName}/${Version} |   | 

## Condition keys for Amazon Cloud Directory
<a name="list_clouddirectory-policy-keys"></a>

Amazon Cloud Directory has no service-specific condition keys that can be used in the `Condition` element of policy statements.