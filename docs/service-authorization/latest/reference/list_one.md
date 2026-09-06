

# Actions, resources, and condition keys for Amazon One Enterprise
<a name="list_one"></a>

Amazon One Enterprise (service prefix: `one`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/one-enterprise/latest/userguide/one-enterprise-getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/one-enterprise/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/one-enterprise/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/one/one.json) for this service.

**Topics**
+ [Actions defined by Amazon One Enterprise](#list_one-actions-as-permissions)
+ [Resource types defined by Amazon One Enterprise](#list_one-resources-for-iam-policies)
+ [Condition keys for Amazon One Enterprise](#list_one-policy-keys)

## Actions defined by Amazon One Enterprise
<a name="list_one-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDeviceActivationQrCode](https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html)  **
  - **Description:** Grants permission to create a QR code for a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDeviceConfigurationTemplate](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  **
  - **Description:** Grants permission to create a Device Configuration Template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeviceInstance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to create a Device Instance
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeviceInstanceConfiguration](https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html)  **
  - **Description:** Grants permission to create a Device Instance Configuration
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSite](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to create a Site
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAssociatedDevice](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to disassociate Device from a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceConfigurationTemplate](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  **
  - **Description:** Grants permission to delete a Device Configuration Template
  - **Resource types (\*required):** [device-configuration-template\*](#list_one-resource-device-configuration-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceInstance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to delete a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSite](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to delete a Site
  - **Resource types (\*required):** [site\*](#list_one-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserV1](https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.htmll)  **
  - **Description:** Grants permission to delete a User
  - **Resource types (\*required):** [user\*](#list_one-resource-user)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetDeviceConfigurationTemplate](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  **
  - **Description:** Grants permission to view a Device Configuration Template
  - **Resource types (\*required):** [device-configuration-template\*](#list_one-resource-device-configuration-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceInstance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to view a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceInstanceConfiguration](https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html)  **
  - **Description:** Grants permission to view a Device Instance Configuration
  - **Resource types (\*required):** [configuration\*](#list_one-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSite](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to view a Site
  - **Resource types (\*required):** [site\*](#list_one-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSiteAddress](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to view address of a Site
  - **Resource types (\*required):** [site\*](#list_one-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeviceConfigurationTemplates](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  **
  - **Description:** Grants permission to retrieve list of Device Configuration Templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeviceInstances](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to retrieve list of Device Instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSites](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to view list of Sites
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/one-enterprise/latest/userguide/actions-resources-contextkeys.html)  **
  - **Description:** Grants permission to list tags for an Amazon One Enterprise resource
  - **Resource types (\*required):** [device-configuration-template](#list_one-resource-device-configuration-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device-instance](#list_one-resource-device-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [site](#list_one-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUsers](https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.html)  **
  - **Description:** Grants permission to view list of Users
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsersV1](https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.html)  **
  - **Description:** Grants permission to view list of Users
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RebootDevice](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to reboot Device associated with a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/one-enterprise/latest/userguide/actions-resources-contextkeys.html)  **
  - **Description:** Grants permission to add tags to an Amazon One Enterprise resource
  - **Resource types (\*required):** [device-configuration-template](#list_one-resource-device-configuration-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Resource types (\*required):** [device-instance](#list_one-resource-device-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_one-resource-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_one-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/one-enterprise/latest/userguide/actions-resources-contextkeys.html)  **
  - **Description:** Grants permission to remove tags from an Amazon One Enterprise resource
  - **Resource types (\*required):** [device-configuration-template](#list_one-resource-device-configuration-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Resource types (\*required):** [device-instance](#list_one-resource-device-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_one-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_one-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDeviceConfigurationTemplate](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  **
  - **Description:** Grants permission to update a Device Configuration Template
  - **Resource types (\*required):** [device-configuration-template\*](#list_one-resource-device-configuration-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeviceInstance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  **
  - **Description:** Grants permission to update a Device Instance
  - **Resource types (\*required):** [device-instance\*](#list_one-resource-device-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSite](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to update a Site
  - **Resource types (\*required):** [site\*](#list_one-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSiteAddress](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  **
  - **Description:** Grants permission to update address of a Site
  - **Resource types (\*required):** [site\*](#list_one-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon One Enterprise
<a name="list_one-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [configuration](https://docs.aws.amazon.com/one-enterprise/latest/userguide/configure-instance.html)  | arn:${Partition}:one:${Region}:${Account}:device-instance/${DeviceInstanceId}/configuration/${Version} |   | 
|  [device-configuration-template](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-config-template.html)  | arn:${Partition}:one:${Region}:${Account}:device-configuration-template/${TemplateId} | [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_) | 
|  [device-instance](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-device-instance.html)  | arn:${Partition}:one:${Region}:${Account}:device-instance/${DeviceInstanceId} | [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_) | 
|  [site](https://docs.aws.amazon.com/one-enterprise/latest/userguide/create-sites.html)  | arn:${Partition}:one:${Region}:${Account}:site/${SiteId} | [aws:ResourceTag/${TagKey}](#list_one-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/one-enterprise/latest/userguide/enrollment-entry.html)  | arn:${Partition}:one:${Region}:${Account}:user/${UserId} |   | 

## Condition keys for Amazon One Enterprise
<a name="list_one-policy-keys"></a>

Amazon One Enterprise defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by using tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by using tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 