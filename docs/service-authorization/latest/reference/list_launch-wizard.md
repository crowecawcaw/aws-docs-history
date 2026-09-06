

# Actions, resources, and condition keys for AWS Launch Wizard
<a name="list_launch-wizard"></a>

AWS Launch Wizard (service prefix: `launchwizard`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/launchwizard/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/launchwizard/launchwizard.json) for this service.

**Topics**
+ [API operations defined by AWS Launch Wizard](#list_launch-wizard-operations)
+ [Actions defined by AWS Launch Wizard](#list_launch-wizard-actions-as-permissions)
+ [Permission-only actions for AWS Launch Wizard](#list_launch-wizard-permission-only-actions)
+ [Resource types defined by AWS Launch Wizard](#list_launch-wizard-resources-for-iam-policies)
+ [Condition keys for AWS Launch Wizard](#list_launch-wizard-policy-keys)

## API operations defined by AWS Launch Wizard
<a name="list_launch-wizard-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_launch-wizard-actions-as-permissions).




- **   CreateDeployment  **
  - **IAM action:**  [launchwizard:CreateDeployment](#list_launch-wizard-action-CreateDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [launchwizard:TagResource](#list_launch-wizard-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDeployment  **
  - **IAM action:**  [launchwizard:DeleteDeployment](#list_launch-wizard-action-DeleteDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDeployment  **
  - **IAM action:**  [launchwizard:GetDeployment](#list_launch-wizard-action-GetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeploymentPatternVersion  **
  - **IAM action:**  [launchwizard:GetDeploymentPatternVersion](#list_launch-wizard-action-GetDeploymentPatternVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkload  **
  - **IAM action:**  [launchwizard:GetWorkload](#list_launch-wizard-action-GetWorkload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkloadDeploymentPattern  **
  - **IAM action:**  [launchwizard:GetWorkloadDeploymentPattern](#list_launch-wizard-action-GetWorkloadDeploymentPattern) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeploymentEvents  **
  - **IAM action:**  [launchwizard:ListDeploymentEvents](#list_launch-wizard-action-ListDeploymentEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentPatternVersions  **
  - **IAM action:**  [launchwizard:ListDeploymentPatternVersions](#list_launch-wizard-action-ListDeploymentPatternVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **IAM action:**  [launchwizard:ListDeployments](#list_launch-wizard-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [launchwizard:ListTagsForResource](#list_launch-wizard-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkloadDeploymentPatterns  **
  - **IAM action:**  [launchwizard:ListWorkloadDeploymentPatterns](#list_launch-wizard-action-ListWorkloadDeploymentPatterns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkloads  **
  - **IAM action:**  [launchwizard:ListWorkloads](#list_launch-wizard-action-ListWorkloads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [launchwizard:TagResource](#list_launch-wizard-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [launchwizard:UntagResource](#list_launch-wizard-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDeployment  **
  - **IAM action:**  [launchwizard:UpdateDeployment](#list_launch-wizard-action-UpdateDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Launch Wizard
<a name="list_launch-wizard-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to create a deployment
  - **Resource types (\*required):** [deployment\*](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_launch-wizard-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_launch-wizard-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_DeleteDeployment.html)  **
  - **Description:** Grants permission to delete a deployment
  - **Resource types (\*required):** [deployment\*](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to get a deployment
  - **Resource types (\*required):** [deployment\*](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeploymentPatternVersion](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetDeploymentPatternVersion.html)  **
  - **Description:** Grants permission to get a version of a deployment pattern
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkload](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkload.html)  **
  - **Description:** Grants permission to get a workload
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkloadDeploymentPattern](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html)  **
  - **Description:** Grants permission to get a deployment pattern
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDeploymentEvents](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeploymentEvents.html)  **
  - **Description:** Grants permission to list the events that occured during a deployment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeploymentPatternVersions](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeploymentPatternVersions.html)  **
  - **Description:** Grants permission to list the versions of a deployment pattern
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to list deployments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a LaunchWizard resource
  - **Resource types (\*required):** [deployment](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWorkloadDeploymentPatterns](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html)  **
  - **Description:** Grants permission to list the deployment patterns of a workload
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkloads](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html)  **
  - **Description:** Grants permission to list workloads
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a LaunchWizard resource
  - **Resource types (\*required):** [deployment](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_launch-wizard-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_launch-wizard-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a LaunchWizard resource
  - **Resource types (\*required):** [deployment](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_launch-wizard-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDeployment](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_UpdateDeployment.html)  **
  - **Description:** Grants permission to update a deployment
  - **Resource types (\*required):** [deployment\*](#list_launch-wizard-resource-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Launch Wizard
<a name="list_launch-wizard-permission-only-actions"></a>

The following actions are defined by AWS Launch Wizard but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateAdditionalNode](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to create an additional node |  |   | Write | 
|   [CreateSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to create an application settings set |  |   | Write | 
|   [DeleteAdditionalNode](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to delete an additional node |  |   | Write | 
|   [DeleteApp](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to delete an application |  |   | Write | 
|   [DeleteSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to delete a settings set |  |   | Write | 
|   [DescribeAdditionalNode](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to describe an additional node |  |   | Read | 
|   [DescribeProvisionedApp](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to describe provisioning applications |  |   | Read | 
|   [DescribeProvisioningEvents](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to describe provisioning events |  |   | Read | 
|   [DescribeSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to describe an application settings set |  |   | Read | 
|   [GetInfrastructureSuggestion](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get infrastructure suggestion |  |   | Read | 
|   [GetIpAddress](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get customer's ip address |  |   | Read | 
|   [GetResourceCostEstimate](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get resource cost estimate |  |   | Read | 
|   [GetResourceRecommendation](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get recommendation for a resource |  |   | Read | 
|   [GetSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get a settings set |  |   | Read | 
|   [GetWorkloadAsset](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get a workload's asset |  |   | Read | 
|   [GetWorkloadAssets](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to get workload assets |  |   | Read | 
|   [ListAdditionalNodes](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list additional nodes |  |   | List | 
|   [ListAllowedResources](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list the allowed resources |  |   | List | 
|   [ListProvisionedApps](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list provisioning applications |  |   | List | 
|   [ListResourceCostEstimates](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list the cost estimates of resources |  |   | List | 
|   [ListSettingsSets](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list settings sets |  |   | List | 
|   [ListWorkloadDeploymentOptions](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to list deployment options of a given workload |  |   | List | 
|   [PutSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to create a settings set |  |   | Write | 
|   [StartProvisioning](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to start a provisioning |  |   | Write | 
|   [UpdateSettingsSet](https://docs.aws.amazon.com/launchwizard/)  | Grants permission to update an application settings set |  |   | Write | 

## Resource types defined by AWS Launch Wizard
<a name="list_launch-wizard-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [deployment](https://docs.aws.amazon.com/launchwizard/Resources/Deployment.html)  | arn:${Partition}:launchwizard:${Region}:${Account}:deployment/${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_launch-wizard-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Launch Wizard
<a name="list_launch-wizard-policy-keys"></a>

AWS Launch Wizard defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 