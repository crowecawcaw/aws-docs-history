

# Actions, resources, and condition keys for AWS Directory Service Data
<a name="list_ds-data"></a>

AWS Directory Service Data (service prefix: `ds-data`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_AuthNAccess.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ds-data/ds-data.json) for this service.

**Topics**
+ [API operations defined by AWS Directory Service Data](#list_ds-data-operations)
+ [Actions defined by AWS Directory Service Data](#list_ds-data-actions-as-permissions)
+ [Resource types defined by AWS Directory Service Data](#list_ds-data-resources-for-iam-policies)
+ [Condition keys for AWS Directory Service Data](#list_ds-data-policy-keys)

## API operations defined by AWS Directory Service Data
<a name="list_ds-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ds-data-actions-as-permissions).




- **   AddGroupMember  **
  - **IAM action:**  [ds-data:AddGroupMember](#list_ds-data-action-AddGroupMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateGroup  **
  - **IAM action:**  [ds-data:CreateGroup](#list_ds-data-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateUser  **
  - **IAM action:**  [ds-data:CreateUser](#list_ds-data-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DeleteGroup  **
  - **IAM action:**  [ds-data:DeleteGroup](#list_ds-data-action-DeleteGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DeleteUser  **
  - **IAM action:**  [ds-data:DeleteUser](#list_ds-data-action-DeleteUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DescribeGroup  **
  - **IAM action:**  [ds-data:DescribeGroup](#list_ds-data-action-DescribeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DescribeUser  **
  - **IAM action:**  [ds-data:DescribeUser](#list_ds-data-action-DescribeUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   DisableUser  **
  - **IAM action:**  [ds-data:DisableUser](#list_ds-data-action-DisableUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   ListGroupMembers  **
  - **IAM action:**  [ds-data:ListGroupMembers](#list_ds-data-action-ListGroupMembers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   ListGroups  **
  - **IAM action:**  [ds-data:ListGroups](#list_ds-data-action-ListGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   ListGroupsForMember  **
  - **IAM action:**  [ds-data:ListGroupsForMember](#list_ds-data-action-ListGroupsForMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   ListUsers  **
  - **IAM action:**  [ds-data:ListUsers](#list_ds-data-action-ListUsers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   RemoveGroupMember  **
  - **IAM action:**  [ds-data:RemoveGroupMember](#list_ds-data-action-RemoveGroupMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   SearchGroups  **
  - **IAM action:**  [ds-data:DescribeGroup](#list_ds-data-action-DescribeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds-data:SearchGroups](#list_ds-data-action-SearchGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   SearchUsers  **
  - **IAM action:**  [ds-data:DescribeUser](#list_ds-data-action-DescribeUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds-data:SearchUsers](#list_ds-data-action-SearchUsers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateGroup  **
  - **IAM action:**  [ds-data:UpdateGroup](#list_ds-data-action-UpdateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   UpdateUser  **
  - **IAM action:**  [ds-data:UpdateUser](#list_ds-data-action-UpdateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ds:AccessDSData](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write



## Actions defined by AWS Directory Service Data
<a name="list_ds-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AddGroupMember.html)  **
  - **Description:** Grants permission to add a member to a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:MemberName](#list_ds-data-ds-data_MemberName)<br />[ds-data:MemberRealm](#list_ds-data-ds-data_MemberRealm)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a user on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [DescribeGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeGroup.html)  **
  - **Description:** Grants permission to describe a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Read

- **   [DescribeUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeUser.html)  **
  - **Description:** Grants permission to describe a user on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Read

- **   [DisableUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DisableUser.html)  **
  - **Description:** Grants permission to disable a user on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [ListGroupMembers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupMembers.html)  **
  - **Description:** Grants permission to list members in a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:MemberRealm](#list_ds-data-ds-data_MemberRealm)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to list groups on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)
  - **Access level:** List

- **   [ListGroupsForMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupsForMember.html)  **
  - **Description:** Grants permission to list the groups that a member is in on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:MemberRealm](#list_ds-data-ds-data_MemberRealm)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to list users on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)
  - **Access level:** List

- **   [RemoveGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_RemoveGroupMember.html)  **
  - **Description:** Grants permission to remove a member from a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:MemberName](#list_ds-data-ds-data_MemberName)<br />[ds-data:MemberRealm](#list_ds-data-ds-data_MemberRealm)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [SearchGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchGroups.html)  **
  - **Description:** Grants permission to search for groups on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)
  - **Access level:** Read

- **   [SearchUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchUsers.html)  **
  - **Description:** Grants permission to search for users on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)
  - **Access level:** Read

- **   [UpdateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update a group on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateUser.html)  **
  - **Description:** Grants permission to update a user on a directory
  - **Resource types (\*required):** [directory\*](#list_ds-data-resource-directory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_)<br />[ds-data:Identifier](#list_ds-data-ds-data_Identifier)<br />[ds-data:Realm](#list_ds-data-ds-data_Realm)<br />[ds-data:SAMAccountName](#list_ds-data-ds-data_SAMAccountName)
  - **Access level:** Write



## Resource types defined by AWS Directory Service Data
<a name="list_ds-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/IAM_Auth_Access_Overview.html)  | arn:${Partition}:ds:${Region}:${Account}:directory/${DirectoryId} | [aws:ResourceTag/${TagKey}](#list_ds-data-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Directory Service Data
<a name="list_ds-data-policy-keys"></a>

AWS Directory Service Data defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the AWS DS Resource being acted upon | String | 
|   [ds-data:Identifier](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html#dsdata_condition-Identifier)  | Filters access by the type of identifier provided in the request (i.e. SAM Account Name) | String | 
|   [ds-data:MemberName](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html#dsdata_condition-MemberName)  | Filters access by the directory SAM Account Name included in the MemberName input of the request | String | 
|   [ds-data:MemberRealm](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html#dsdata_condition-MemberRealm)  | Filters access by the directory realm name included in the MemberRealm input of the request | String | 
|   [ds-data:Realm](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html#dsdata_condition-Realm)  | Filters access by the directory realm name for the request | String | 
|   [ds-data:SAMAccountName](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html#dsdata_condition-SAMAccountName)  | Filters access by the directory SAM Account Name included in the SAMAccountName input of the request | String | 