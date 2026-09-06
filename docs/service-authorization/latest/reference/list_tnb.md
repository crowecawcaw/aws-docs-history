

# Actions, resources, and condition keys for AWS Telco Network Builder
<a name="list_tnb"></a>

AWS Telco Network Builder (service prefix: `tnb`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/tnb/latest/ug/how-tnb-works.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/tnb/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/tnb/latest/ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/tnb/tnb.json) for this service.

**Topics**
+ [API operations defined by AWS Telco Network Builder](#list_tnb-operations)
+ [Actions defined by AWS Telco Network Builder](#list_tnb-actions-as-permissions)
+ [Resource types defined by AWS Telco Network Builder](#list_tnb-resources-for-iam-policies)
+ [Condition keys for AWS Telco Network Builder](#list_tnb-policy-keys)

## API operations defined by AWS Telco Network Builder
<a name="list_tnb-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_tnb-actions-as-permissions).




- **   CancelSolNetworkOperation  **
  - **IAM action:**  [tnb:CancelSolNetworkOperation](#list_tnb-action-CancelSolNetworkOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSolFunctionPackage  **
  - **IAM action:**  [tnb:CreateSolFunctionPackage](#list_tnb-action-CreateSolFunctionPackage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSolNetworkInstance  **
  - **IAM action:**  [tnb:CreateSolNetworkInstance](#list_tnb-action-CreateSolNetworkInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSolNetworkPackage  **
  - **IAM action:**  [tnb:CreateSolNetworkPackage](#list_tnb-action-CreateSolNetworkPackage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteSolFunctionPackage  **
  - **IAM action:**  [tnb:DeleteSolFunctionPackage](#list_tnb-action-DeleteSolFunctionPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSolNetworkInstance  **
  - **IAM action:**  [tnb:DeleteSolNetworkInstance](#list_tnb-action-DeleteSolNetworkInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSolNetworkPackage  **
  - **IAM action:**  [tnb:DeleteSolNetworkPackage](#list_tnb-action-DeleteSolNetworkPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSolFunctionInstance  **
  - **IAM action:**  [tnb:GetSolFunctionInstance](#list_tnb-action-GetSolFunctionInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolFunctionPackage  **
  - **IAM action:**  [tnb:GetSolFunctionPackage](#list_tnb-action-GetSolFunctionPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolFunctionPackageContent  **
  - **IAM action:**  [tnb:GetSolFunctionPackageContent](#list_tnb-action-GetSolFunctionPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolFunctionPackageDescriptor  **
  - **IAM action:**  [tnb:GetSolFunctionPackageDescriptor](#list_tnb-action-GetSolFunctionPackageDescriptor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolNetworkInstance  **
  - **IAM action:**  [tnb:GetSolNetworkInstance](#list_tnb-action-GetSolNetworkInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolNetworkOperation  **
  - **IAM action:**  [tnb:GetSolNetworkOperation](#list_tnb-action-GetSolNetworkOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolNetworkPackage  **
  - **IAM action:**  [tnb:GetSolNetworkPackage](#list_tnb-action-GetSolNetworkPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolNetworkPackageContent  **
  - **IAM action:**  [tnb:GetSolNetworkPackageContent](#list_tnb-action-GetSolNetworkPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSolNetworkPackageDescriptor  **
  - **IAM action:**  [tnb:GetSolNetworkPackageDescriptor](#list_tnb-action-GetSolNetworkPackageDescriptor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InstantiateSolNetworkInstance  **
  - **IAM action:**  [tnb:InstantiateSolNetworkInstance](#list_tnb-action-InstantiateSolNetworkInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListSolFunctionInstances  **
  - **IAM action:**  [tnb:ListSolFunctionInstances](#list_tnb-action-ListSolFunctionInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolFunctionPackages  **
  - **IAM action:**  [tnb:ListSolFunctionPackages](#list_tnb-action-ListSolFunctionPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolNetworkInstances  **
  - **IAM action:**  [tnb:ListSolNetworkInstances](#list_tnb-action-ListSolNetworkInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolNetworkOperations  **
  - **IAM action:**  [tnb:ListSolNetworkOperations](#list_tnb-action-ListSolNetworkOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSolNetworkPackages  **
  - **IAM action:**  [tnb:ListSolNetworkPackages](#list_tnb-action-ListSolNetworkPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [tnb:ListTagsForResource](#list_tnb-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutSolFunctionPackageContent  **
  - **IAM action:**  [tnb:PutSolFunctionPackageContent](#list_tnb-action-PutSolFunctionPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSolNetworkPackageContent  **
  - **IAM action:**  [tnb:PutSolNetworkPackageContent](#list_tnb-action-PutSolNetworkPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateSolNetworkInstance  **
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [tnb:TerminateSolNetworkInstance](#list_tnb-action-TerminateSolNetworkInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [tnb:UntagResource](#list_tnb-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateSolFunctionPackage  **
  - **IAM action:**  [tnb:UpdateSolFunctionPackage](#list_tnb-action-UpdateSolFunctionPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSolNetworkInstance  **
  - **IAM action:**  [tnb:TagResource](#list_tnb-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [tnb:UpdateSolNetworkInstance](#list_tnb-action-UpdateSolNetworkInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSolNetworkPackage  **
  - **IAM action:**  [tnb:UpdateSolNetworkPackage](#list_tnb-action-UpdateSolNetworkPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateSolFunctionPackageContent  **
  - **IAM action:**  [tnb:ValidateSolFunctionPackageContent](#list_tnb-action-ValidateSolFunctionPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateSolNetworkPackageContent  **
  - **IAM action:**  [tnb:ValidateSolNetworkPackageContent](#list_tnb-action-ValidateSolNetworkPackageContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Telco Network Builder
<a name="list_tnb-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelSolNetworkOperation](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CancelSolNetworkOperation.html)  **
  - **Description:** Grants permission to cancel a network operation
  - **Resource types (\*required):** [network-operation\*](#list_tnb-resource-network-operation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolFunctionPackage.html)  **
  - **Description:** Grants permission to create a function package
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html)  **
  - **Description:** Grants permission to create a network instance
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkPackage.html)  **
  - **Description:** Grants permission to create a network package
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolFunctionPackage.html)  **
  - **Description:** Grants permission to delete a function package
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkInstance.html)  **
  - **Description:** Grants permission to delete a network instance
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkPackage.html)  **
  - **Description:** Grants permission to delete a network package
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetSolFunctionInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionInstance.html)  **
  - **Description:** Grants permission to get a function instance
  - **Resource types (\*required):** [function-instance\*](#list_tnb-resource-function-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackage.html)  **
  - **Description:** Grants permission to get a function package
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageContent.html)  **
  - **Description:** Grants permission to get a function package contents
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolFunctionPackageDescriptor](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageDescriptor.html)  **
  - **Description:** Grants permission to get a function package descriptor
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkInstance.html)  **
  - **Description:** Grants permission to get a network instance
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolNetworkOperation](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperation.html)  **
  - **Description:** Grants permission to get a network operation
  - **Resource types (\*required):** [network-operation\*](#list_tnb-resource-network-operation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackage.html)  **
  - **Description:** Grants permission to get a network package
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageContent.html)  **
  - **Description:** Grants permission to get a network package contents
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSolNetworkPackageDescriptor](https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageDescriptor.html)  **
  - **Description:** Grants permission to get a network package descriptor
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InstantiateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html)  **
  - **Description:** Grants permission to instantiate a network instance
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [ListSolFunctionInstances](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstances.html)  **
  - **Description:** Grants permission to list function instances
  - **Resource types (\*required):** [function-instance\*](#list_tnb-resource-function-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSolFunctionPackages](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackages.html)  **
  - **Description:** Grants permission to list function packages
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSolNetworkInstances](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkInstances.html)  **
  - **Description:** Grants permission to list network instances
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSolNetworkOperations](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperations.html)  **
  - **Description:** Grants permission to list network operations
  - **Resource types (\*required):** [network-operation\*](#list_tnb-resource-network-operation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSolNetworkPackages](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkPackages.html)  **
  - **Description:** Grants permission to list network packages
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html)  **
  - **Description:** Grants permission to upload function package content
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html)  **
  - **Description:** Grants permission to upload network package content
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified resource
  - **Resource types (\*required):** [function-instance](#list_tnb-resource-function-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [function-package](#list_tnb-resource-function-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-instance](#list_tnb-resource-network-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-operation](#list_tnb-resource-network-operation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-package](#list_tnb-resource-network-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html)  **
  - **Description:** Grants permission to terminate a network instance
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [function-instance](#list_tnb-resource-function-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [function-package](#list_tnb-resource-function-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-instance](#list_tnb-resource-network-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-operation](#list_tnb-resource-network-operation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-package](#list_tnb-resource-network-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html)  **
  - **Description:** Grants permission to update a function package
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkInstance.html)  **
  - **Description:** Grants permission to update a network instance
  - **Resource types (\*required):** [function-instance\*](#list_tnb-resource-function-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Resource types (\*required):** [network-instance\*](#list_tnb-resource-network-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_tnb-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_tnb-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html)  **
  - **Description:** Grants permission to update a network package
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolFunctionPackageContent.html)  **
  - **Description:** Grants permission to validate function package content
  - **Resource types (\*required):** [function-package\*](#list_tnb-resource-function-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolNetworkPackageContent.html)  **
  - **Description:** Grants permission to validate network package content
  - **Resource types (\*required):** [network-package\*](#list_tnb-resource-network-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Telco Network Builder
<a name="list_tnb-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [function-instance](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html)  | arn:${Partition}:tnb:${Region}:${Account}:function-instance/${FunctionInstanceId} | [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_) | 
|  [function-package](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html)  | arn:${Partition}:tnb:${Region}:${Account}:function-package/${FunctionPackageId} | [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_) | 
|  [network-instance](https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html)  | arn:${Partition}:tnb:${Region}:${Account}:network-instance/${NetworkInstanceId} | [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_) | 
|  [network-operation](https://docs.aws.amazon.com/tnb/latest/ug/network-operations.html)  | arn:${Partition}:tnb:${Region}:${Account}:network-operation/${NetworkOperationId} | [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_) | 
|  [network-package](https://docs.aws.amazon.com/tnb/latest/ug/network-packages.html)  | arn:${Partition}:tnb:${Region}:${Account}:network-package/${NetworkPackageId} | [aws:ResourceTag/${TagKey}](#list_tnb-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Telco Network Builder
<a name="list_tnb-policy-keys"></a>

AWS Telco Network Builder defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by checking the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by checking tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of tag keys in the request | ArrayOfString | 