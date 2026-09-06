

# Actions, resources, and condition keys for Amazon CodeWhisperer
<a name="list_codewhisperer"></a>

Amazon CodeWhisperer (service prefix: `codewhisperer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codewhisperer/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_id-based-policy-examples.html#permissions-required-console/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codewhisperer/codewhisperer.json) for this service.

**Topics**
+ [Actions defined by Amazon CodeWhisperer](#list_codewhisperer-actions-as-permissions)
+ [Permission-only actions for Amazon CodeWhisperer](#list_codewhisperer-permission-only-actions)
+ [Resource types defined by Amazon CodeWhisperer](#list_codewhisperer-resources-for-iam-policies)
+ [Condition keys for Amazon CodeWhisperer](#list_codewhisperer-policy-keys)

## Actions defined by Amazon CodeWhisperer
<a name="list_codewhisperer-actions-as-permissions"></a>

Amazon CodeWhisperer has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Amazon CodeWhisperer
<a name="list_codewhisperer-permission-only-actions"></a>

The following actions are defined by Amazon CodeWhisperer but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/codewhisperer/latest/userguide/monitoring-overview.html)  **
  - **Description:** Grants permission to configure vended log delivery for CodeWhisperer customization resource
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AssociateCustomizationPermission](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke AssociateCustomizationPermission on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCustomization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke CreateCustomization on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codewhisperer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke CreateProfile on CodeWhisperer
  - **Resource types (\*required):** [profile\*](#list_codewhisperer-resource-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codewhisperer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCustomization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke DeleteCustomization on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke DeleteProfile on CodeWhisperer
  - **Resource types (\*required):** [profile\*](#list_codewhisperer-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateCustomizationPermission](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke DisassociateCustomizationPermission on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateRecommendations](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke GenerateRecommendations on CodeWhisperer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke GetCustomization on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCustomizationPermissions](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke ListCustomizationPermissions on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomizationVersions](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke ListCustomizationVersions on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomizations](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke ListCustomizations on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke ListProfiles on CodeWhisperer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke ListTagsForResource on CodeWhisperer
  - **Resource types (\*required):** [customization](#list_codewhisperer-resource-customization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [profile](#list_codewhisperer-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke TagResource on CodeWhisperer
  - **Resource types (\*required):** [customization](#list_codewhisperer-resource-customization) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codewhisperer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_codewhisperer-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codewhisperer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke UntagResource on CodeWhisperer
  - **Resource types (\*required):** [customization](#list_codewhisperer-resource-customization) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_codewhisperer-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codewhisperer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCustomization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke UpdateCustomization on CodeWhisperer
  - **Resource types (\*required):** [customization\*](#list_codewhisperer-resource-customization)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security_iam_service-with-iam.html)  **
  - **Description:** Grants permission to invoke UpdateProfile on CodeWhisperer
  - **Resource types (\*required):** [profile\*](#list_codewhisperer-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon CodeWhisperer
<a name="list_codewhisperer-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [customization](https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-customizations)  | arn:${Partition}:codewhisperer:${Region}:${Account}:customization/${Identifier} | [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/codewhisperer/latest/userguide/as-whisper-admin.html#about-profiles)  | arn:${Partition}:codewhisperer:${Region}:${Account}:profile/${Identifier} | [aws:ResourceTag/${TagKey}](#list_codewhisperer-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CodeWhisperer
<a name="list_codewhisperer-policy-keys"></a>

Amazon CodeWhisperer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/codewhisperer/latest/userguide/codewhisperer-setup-enterprise-admin.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/codewhisperer/latest/userguide/codewhisperer-setup-enterprise-admin.html)  | Filters access by the tags associated with CodeWhisperer resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/codewhisperer/latest/userguide/codewhisperer-setup-enterprise-admin.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 