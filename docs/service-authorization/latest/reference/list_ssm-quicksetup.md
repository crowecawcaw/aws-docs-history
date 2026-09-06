

# Actions, resources, and condition keys for AWS Systems Manager Quick Setup
<a name="list_ssm-quicksetup"></a>

AWS Systems Manager Quick Setup (service prefix: `ssm-quicksetup`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/quick-setup/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm-quicksetup/ssm-quicksetup.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager Quick Setup](#list_ssm-quicksetup-operations)
+ [Actions defined by AWS Systems Manager Quick Setup](#list_ssm-quicksetup-actions-as-permissions)
+ [Resource types defined by AWS Systems Manager Quick Setup](#list_ssm-quicksetup-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager Quick Setup](#list_ssm-quicksetup-policy-keys)

## API operations defined by AWS Systems Manager Quick Setup
<a name="list_ssm-quicksetup-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-quicksetup-actions-as-permissions).




- **   CreateConfigurationManager  **
  - **IAM action:**  [ssm-quicksetup:CreateConfigurationManager](#list_ssm-quicksetup-action-CreateConfigurationManager)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-quicksetup:TagResource](#list_ssm-quicksetup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, ssm-quicksetup.amazonaws.com / **Access level:** Write

- **   DeleteConfigurationManager  **
  - **IAM action:**  [ssm-quicksetup:DeleteConfigurationManager](#list_ssm-quicksetup-action-DeleteConfigurationManager)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, ssm-quicksetup.amazonaws.com / **Access level:** Write

- **   GetConfiguration  **
  - **IAM action:**  [ssm-quicksetup:GetConfiguration](#list_ssm-quicksetup-action-GetConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationManager  **
  - **IAM action:**  [ssm-quicksetup:GetConfigurationManager](#list_ssm-quicksetup-action-GetConfigurationManager) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceSettings  **
  - **IAM action:**  [ssm-quicksetup:GetServiceSettings](#list_ssm-quicksetup-action-GetServiceSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConfigurationManagers  **
  - **IAM action:**  [ssm-quicksetup:ListConfigurationManagers](#list_ssm-quicksetup-action-ListConfigurationManagers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurations  **
  - **IAM action:**  [ssm-quicksetup:ListConfigurations](#list_ssm-quicksetup-action-ListConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuickSetupTypes  **
  - **IAM action:**  [ssm-quicksetup:ListQuickSetupTypes](#list_ssm-quicksetup-action-ListQuickSetupTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [ssm-quicksetup:ListTagsForResource](#list_ssm-quicksetup-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [ssm-quicksetup:TagResource](#list_ssm-quicksetup-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, ssm-quicksetup.amazonaws.com / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [ssm-quicksetup:UntagResource](#list_ssm-quicksetup-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, ssm-quicksetup.amazonaws.com / **Access level:** Write

- **   UpdateConfigurationDefinition  **
  - **IAM action:**  [ssm-quicksetup:UpdateConfigurationDefinition](#list_ssm-quicksetup-action-UpdateConfigurationDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, ssm-quicksetup.amazonaws.com / **Access level:** Write

- **   UpdateConfigurationManager  **
  - **IAM action:**  [ssm-quicksetup:UpdateConfigurationManager](#list_ssm-quicksetup-action-UpdateConfigurationManager) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceSettings  **
  - **IAM action:**  [ssm-quicksetup:UpdateServiceSettings](#list_ssm-quicksetup-action-UpdateServiceSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm-quicksetup.amazonaws.com / **Access level:** Write



## Actions defined by AWS Systems Manager Quick Setup
<a name="list_ssm-quicksetup-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_CreateConfigurationManager.html)  **
  - **Description:** Grants permission to create a Quick Setup configuration manager resource
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-quicksetup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-quicksetup-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_DeleteConfigurationManager.html)  **
  - **Description:** Grants permission to delete a configuration manager
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetConfiguration](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfiguration.html)  **
  - **Description:** Grants permission to get Quick Setup configuration
  - **Resource types (\*required):** [configuration-manager](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetConfigurationManager.html)  **
  - **Description:** Grants permission to get a configuration manager
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceSettings](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_GetServiceSettings.html)  **
  - **Description:** Grants permission to get settings configured for Quick Setup in the requesting AWS account and AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConfigurationManagers](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurationManagers.html)  **
  - **Description:** Grants permission to list Quick Setup configuration managers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurations](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListConfigurations.html)  **
  - **Description:** Grants permission to list Quick Setup configurations
  - **Resource types (\*required):** [configuration-manager](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQuickSetupTypes](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListQuickSetupTypes.html)  **
  - **Description:** Grants permission to list the available Quick Setup types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags assigned to the resource
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to Assign key-value pairs of metadata to AWS resources
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-quicksetup-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-quicksetup-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-quicksetup-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConfigurationDefinition](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateConfigurationDefinition.html)  **
  - **Description:** Grants permission to update a Quick Setup configuration definition
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfigurationManager](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateConfigurationManager.html)  **
  - **Description:** Grants permission to update a Quick Setup configuration manager
  - **Resource types (\*required):** [configuration-manager\*](#list_ssm-quicksetup-resource-configuration-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceSettings](https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateServiceSettings.html)  **
  - **Description:** Grants permission to update settings configured for Quick Setup
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Systems Manager Quick Setup
<a name="list_ssm-quicksetup-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration-manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)  | arn:${Partition}:ssm-quicksetup:${Region}:${Account}:configuration-manager/${ConfigurationManagerId} | [aws:ResourceTag/${TagKey}](#list_ssm-quicksetup-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Systems Manager Quick Setup
<a name="list_ssm-quicksetup-policy-keys"></a>

AWS Systems Manager Quick Setup defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 