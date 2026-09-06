

# Actions, resources, and condition keys for AWS Identity Store
<a name="list_identitystore"></a>

AWS Identity Store (service prefix: `identitystore`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/identitystore/identitystore.json) for this service.

**Topics**
+ [API operations defined by AWS Identity Store](#list_identitystore-operations)
+ [Actions defined by AWS Identity Store](#list_identitystore-actions-as-permissions)
+ [Resource types defined by AWS Identity Store](#list_identitystore-resources-for-iam-policies)
+ [Condition keys for AWS Identity Store](#list_identitystore-policy-keys)

## API operations defined by AWS Identity Store
<a name="list_identitystore-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_identitystore-actions-as-permissions).




- **   CreateGroup  **
  - **IAM action:**  [identitystore:CreateGroup](#list_identitystore-action-CreateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGroupMembership  **
  - **IAM action:**  [identitystore:CreateGroupMembership](#list_identitystore-action-CreateGroupMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:AddMemberToGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [identitystore:CreateUser](#list_identitystore-action-CreateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteGroup  **
  - **IAM action:**  [identitystore:DeleteGroup](#list_identitystore-action-DeleteGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteGroupMembership  **
  - **IAM action:**  [identitystore:DeleteGroupMembership](#list_identitystore-action-DeleteGroupMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:RemoveMemberFromGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [identitystore:DeleteUser](#list_identitystore-action-DeleteUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeGroup  **
  - **IAM action:**  [identitystore:DescribeGroup](#list_identitystore-action-DescribeGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:DescribeGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeGroupMembership  **
  - **IAM action:**  [identitystore:DescribeGroupMembership](#list_identitystore-action-DescribeGroupMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:ListGroupsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:ListGroupsForUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeUser  **
  - **IAM action:**  [identitystore:DescribeUser](#list_identitystore-action-DescribeUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:DescribeUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetGroupId  **
  - **IAM action:**  [identitystore:GetGroupId](#list_identitystore-action-GetGroupId)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetGroupMembershipId  **
  - **IAM action:**  [identitystore:GetGroupMembershipId](#list_identitystore-action-GetGroupMembershipId)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:ListGroupsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:ListGroupsForUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetUserId  **
  - **IAM action:**  [identitystore:GetUserId](#list_identitystore-action-GetUserId)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   IsMemberInGroups  **
  - **IAM action:**  [identitystore:IsMemberInGroups](#list_identitystore-action-IsMemberInGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:IsMemberInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListGroupMemberships  **
  - **IAM action:**  [identitystore:ListGroupMemberships](#list_identitystore-action-ListGroupMemberships)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso-directory:ListMembersInGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListGroupMembershipsForMember  **
  - **IAM action:**  [identitystore:ListGroupMembershipsForMember](#list_identitystore-action-ListGroupMembershipsForMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso-directory:ListGroupsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:ListGroupsForUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListGroups  **
  - **IAM action:**  [identitystore:ListGroups](#list_identitystore-action-ListGroups)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso-directory:ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:SearchGroups](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListUsers  **
  - **IAM action:**  [identitystore:ListUsers](#list_identitystore-action-ListUsers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [sso-directory:ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sso-directory:SearchUsers](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateGroup  **
  - **IAM action:**  [identitystore:UpdateGroup](#list_identitystore-action-UpdateGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:UpdateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:UpdateGroupDisplayName](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [identitystore:UpdateUser](#list_identitystore-action-UpdateUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:UpdateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateUser.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sso-directory:UpdateUserName](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS Identity Store
<a name="list_identitystore-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddRegion](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to add a region to an IdentityStore
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html)  **
  - **Description:** Grants permission to create a group in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore)
  - **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [CreateGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroupMembership.html)  **
  - **Description:** Grants permission to create a member to a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [CreateIdentityStore](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to create a new IdentityStore in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a user in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore)
  - **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:ReservedUserId](#list_identitystore-identitystore_ReservedUserId)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Access level:** Write

- **   [DeleteGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroup.html)  **
  - **Description:** Grants permission to delete a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteGroupMembership.html)  **
  - **Description:** Grants permission to remove a member that is part of a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [GroupMembership\*](#list_identitystore-resource-GroupMembership) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [DeleteIdentityStore](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to delete an IdentityStore
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Access level:** Write

- **   [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html)  **
  - **Description:** Grants permission to retrieve information about a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroupMembership.html)  **
  - **Description:** Grants permission to retrieve information about a member that is part of a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [GroupMembership\*](#list_identitystore-resource-GroupMembership) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeRegion](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to retrieve configuration details for a specific IdentityStore region
  - **Resource types (\*required):** 
  - **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html)  **
  - **Description:** Grants permission to retrieve information about user in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Access level:** Read

- **   [GetGroupId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupId.html)  **
  - **Description:** Grants permission to retrieve ID information about group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [GetGroupMembershipId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetGroupMembershipId.html)  **
  - **Description:** Grants permission to retrieve ID information of a member which is part of a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [GroupMembership\*](#list_identitystore-resource-GroupMembership) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [GetUserId](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GetUserId.html)  **
  - **Description:** Grants permission to retrieves ID information about user in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [IsMemberInGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_IsMemberInGroups.html)  **
  - **Description:** Grants permission to check if a member is a part of groups in the specified IdentityStore
  - **Resource types (\*required):** [AllGroupMemberships\*](#list_identitystore-resource-AllGroupMemberships) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Read

- **   [ListGroupMemberships](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMemberships.html)  **
  - **Description:** Grants permission to retrieve all members that are part of a group in the specified IdentityStore
  - **Resource types (\*required):** [AllGroupMemberships\*](#list_identitystore-resource-AllGroupMemberships) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** List

- **   [ListGroupMembershipsForMember](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroupMembershipsForMember.html)  **
  - **Description:** Grants permission to list groups of the target member in the specified IdentityStore
  - **Resource types (\*required):** [AllGroupMemberships\*](#list_identitystore-resource-AllGroupMemberships) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html)  **
  - **Description:** Grants permission to search for groups within the specified IdentityStore
  - **Resource types (\*required):** [AllGroups\*](#list_identitystore-resource-AllGroups) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** List

- **   [ListRegions](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to list all regions configured for an IdentityStore
  - **Resource types (\*required):** 
  - **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to search for users in the specified IdentityStore
  - **Resource types (\*required):** [AllUsers\*](#list_identitystore-resource-AllUsers) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Access level:** List

- **   [RemoveRegion](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to remove a region from an IdentityStore
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ReserveUser](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to reserve a user by getting a userId
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore)
  - **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [UpdateGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateGroup.html)  **
  - **Description:** Grants permission to update information about a group in the specified IdentityStore
  - **Resource types (\*required):** [Group\*](#list_identitystore-resource-Group) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:GroupExternalIdIssuers](#list_identitystore-identitystore_GroupExternalIdIssuers)<br />[identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)
  - **Access level:** Write

- **   [UpdateIdentityStore](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample)  **
  - **Description:** Grants permission to update the configuration of an IdentityStore
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_UpdateUser.html)  **
  - **Description:** Grants permission to update user information in the specified IdentityStore
  - **Resource types (\*required):** [Identitystore\*](#list_identitystore-resource-Identitystore) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Resource types (\*required):** [User\*](#list_identitystore-resource-User) / **Condition keys:** [identitystore:PrimaryRegion](#list_identitystore-identitystore_PrimaryRegion)<br />[identitystore:UserExternalIdIssuers](#list_identitystore-identitystore_UserExternalIdIssuers)
  - **Access level:** Write



## Resource types defined by AWS Identity Store
<a name="list_identitystore-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AllGroupMemberships](${ActionsDocRoot}API_GroupMembership.html)  | arn:${Partition}:identitystore:::membership/\* |   | 
|  [AllGroups](${ActionsDocRoot}API_Group.html)  | arn:${Partition}:identitystore:::group/\* |   | 
|  [AllUsers](${ActionsDocRoot}API_User.html)  | arn:${Partition}:identitystore:::user/\* |   | 
|  [Group](${ActionsDocRoot}API_Group.html)  | arn:${Partition}:identitystore:::group/${GroupId} |   | 
|  [GroupMembership](${ActionsDocRoot}API_GroupMembership.html)  | arn:${Partition}:identitystore:::membership/${MembershipId} |   | 
|  [Identitystore](${ActionsDocRoot})  | arn:${Partition}:identitystore::${Account}:identitystore/${IdentityStoreId} |   | 
|  [User](${ActionsDocRoot}API_User.html)  | arn:${Partition}:identitystore:::user/${UserId} |   | 

## Condition keys for AWS Identity Store
<a name="list_identitystore-policy-keys"></a>

AWS Identity Store defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [identitystore:GroupExternalIdIssuers](list_awsidentitystore.html#awsidentitystore-policy-keys)  | Filters access by Issuer present in ExternalIds for Group resources | ArrayOfARN | 
|   [identitystore:IdentityStoreArn](https://docs.aws.amazon.com/singlesignon/latest/userguide/condition-context-keys-sts-idc.html#condition-keys-identity-store-arn)  | Filters access by Identity Store ARN | ARN | 
|   [identitystore:PrimaryRegion](list_awsidentitystore.html#awsidentitystore-policy-keys)  | Filters access by Primary Region of Identity Store | String | 
|   [identitystore:ReservedUserId](list_awsidentitystore.html#awsidentitystore-policy-keys)  | Filters access by a previously reserved User ID for CreateUser operation | String | 
|   [identitystore:UserExternalIdIssuers](list_awsidentitystore.html#awsidentitystore-policy-keys)  | Filters access by Issuer present in ExternalIds for User resources | ArrayOfARN | 
|   [identitystore:UserId](https://docs.aws.amazon.com/singlesignon/latest/userguide/condition-context-keys-sts-idc.html#condition-keys-identity-store-user-id)  | Filters access by Identity Store User ID | String | 