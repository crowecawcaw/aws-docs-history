

# Actions, resources, and condition keys for Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client"></a>

Amazon WorkSpaces Thin Client (service prefix: `thinclient`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/thinclient/thinclient.json) for this service.

**Topics**
+ [API operations defined by Amazon WorkSpaces Thin Client](#list_workspaces-thin-client-operations)
+ [Actions defined by Amazon WorkSpaces Thin Client](#list_workspaces-thin-client-actions-as-permissions)
+ [Permission-only actions for Amazon WorkSpaces Thin Client](#list_workspaces-thin-client-permission-only-actions)
+ [Resource types defined by Amazon WorkSpaces Thin Client](#list_workspaces-thin-client-resources-for-iam-policies)
+ [Condition keys for Amazon WorkSpaces Thin Client](#list_workspaces-thin-client-policy-keys)

## API operations defined by Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_workspaces-thin-client-actions-as-permissions).




- **   CreateEnvironment  **
  - **IAM action:**  [thinclient:CreateEnvironment](#list_workspaces-thin-client-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [thinclient:TagResource](#list_workspaces-thin-client-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDevice  **
  - **IAM action:**  [thinclient:DeleteDevice](#list_workspaces-thin-client-action-DeleteDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **IAM action:**  [thinclient:DeleteEnvironment](#list_workspaces-thin-client-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterDevice  **
  - **IAM action:**  [thinclient:DeregisterDevice](#list_workspaces-thin-client-action-DeregisterDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDevice  **
  - **IAM action:**  [thinclient:GetDevice](#list_workspaces-thin-client-action-GetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **IAM action:**  [thinclient:GetEnvironment](#list_workspaces-thin-client-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSoftwareSet  **
  - **IAM action:**  [thinclient:GetSoftwareSet](#list_workspaces-thin-client-action-GetSoftwareSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevices  **
  - **IAM action:**  [thinclient:ListDevices](#list_workspaces-thin-client-action-ListDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **IAM action:**  [thinclient:ListEnvironments](#list_workspaces-thin-client-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSoftwareSets  **
  - **IAM action:**  [thinclient:ListSoftwareSets](#list_workspaces-thin-client-action-ListSoftwareSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [thinclient:ListTagsForResource](#list_workspaces-thin-client-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [thinclient:TagResource](#list_workspaces-thin-client-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [thinclient:UntagResource](#list_workspaces-thin-client-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDevice  **
  - **IAM action:**  [thinclient:UpdateDevice](#list_workspaces-thin-client-action-UpdateDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironment  **
  - **IAM action:**  [thinclient:TagResource](#list_workspaces-thin-client-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [thinclient:UpdateEnvironment](#list_workspaces-thin-client-action-UpdateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSoftwareSet  **
  - **IAM action:**  [thinclient:UpdateSoftwareSet](#list_workspaces-thin-client-action-UpdateSoftwareSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateEnvironment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create environments
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-thin-client-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDevice](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_DeleteDevice.html)  **
  - **Description:** Grants permission to delete devices
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete environments
  - **Resource types (\*required):** [environment\*](#list_workspaces-thin-client-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterDevice](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_DeregisterDevice.html)  **
  - **Description:** Grants permission to deregister devices
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDevice](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_GetDevice.html)  **
  - **Description:** Grants permission to get devices
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_GetEnvironment.html)  **
  - **Description:** Grants permission to get details of environments
  - **Resource types (\*required):** [environment\*](#list_workspaces-thin-client-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSoftwareSet](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_GetSoftwareSet.html)  **
  - **Description:** Grants permission to get details of software sets
  - **Resource types (\*required):** [softwareset\*](#list_workspaces-thin-client-resource-softwareset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDevices](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_ListDevices.html)  **
  - **Description:** Grants permission to list devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSoftwareSets](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_ListSoftwareSets.html)  **
  - **Description:** Grants permission to list software sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [device](#list_workspaces-thin-client-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment](#list_workspaces-thin-client-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [softwareset](#list_workspaces-thin-client-resource-softwareset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [device](#list_workspaces-thin-client-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-thin-client-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_workspaces-thin-client-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-thin-client-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Resource types (\*required):** [softwareset](#list_workspaces-thin-client-resource-softwareset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-thin-client-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [device](#list_workspaces-thin-client-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_workspaces-thin-client-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Resource types (\*required):** [softwareset](#list_workspaces-thin-client-resource-softwareset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-thin-client-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDevice](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateDevice.html)  **
  - **Description:** Grants permission to update devices
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update environments
  - **Resource types (\*required):** [environment\*](#list_workspaces-thin-client-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSoftwareSet](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateSoftwareSet.html)  **
  - **Description:** Grants permission to update software set
  - **Resource types (\*required):** [softwareset\*](#list_workspaces-thin-client-resource-softwareset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client-permission-only-actions"></a>

The following actions are defined by Amazon WorkSpaces Thin Client but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetDeviceDetails](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get details of devices
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeviceSessions](${APIReferenceDocPage})  **
  - **Description:** Grants permission to list device sessions
  - **Resource types (\*required):** [device\*](#list_workspaces-thin-client-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_)
  - **Access level:** List



## Resource types defined by Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [device](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Device.html)  | arn:${Partition}:thinclient:${Region}:${Account}:device/${DeviceId} | [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_) | 
|  [environment](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_Environment.html)  | arn:${Partition}:thinclient:${Region}:${Account}:environment/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_) | 
|  [softwareset](https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_SoftwareSet.html)  | arn:${Partition}:thinclient:${Region}:${Account}:softwareset/${SoftwareSetId} | [aws:ResourceTag/${TagKey}](#list_workspaces-thin-client-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon WorkSpaces Thin Client
<a name="list_workspaces-thin-client-policy-keys"></a>

Amazon WorkSpaces Thin Client defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 