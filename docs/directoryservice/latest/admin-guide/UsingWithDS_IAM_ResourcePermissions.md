

# Directory Service API permissions: Actions, resources, and conditions reference
<a name="UsingWithDS_IAM_ResourcePermissions"></a>

When you are setting up [Access control](iam_auth_access.md#access_control) and writing permissions policies that you can attach to an IAM identity (identity-based policies), you can use the [Directory Service API permissions: Actions, resources, and conditions reference](#UsingWithDS_IAM_ResourcePermissions) table as a reference. Each API entry in the table includes the following:
+ The name of each API operation
+ Each API operation's corresponding action or actions in which you can grant permissions to perform the action
+ The AWS resource in which you can grant the permissions

 You specify the actions in the policy's `Action` field and the resource value in the policy's `Resource` field. To specify an action, use the `ds:` prefix followed by the API operation name (for example, `ds:CreateDirectory`). Some AWS applications may require use of nonpublic Directory Service API operations such as `ds:AuthorizeApplication`, `ds:CheckAlias`, `ds:CreateIdentityPoolDirectory`, `ds:GetAuthorizedApplicationDetails`, `ds:UpdateAuthorizedApplication`, and `ds:UnauthorizeApplication` in their policies. 

Some Directory Service APIs can only be called through the AWS Management Console. They are not public APIs, in the sense they cannot be called programmatically, and they are not provided by any SDK. They accept user credentials. These API operations include `ds:DisableRoleAccess`, `ds:EnableRoleAccess`, and `ds:UpdateDirectory`.

 You can use AWS global condition keys in your Directory Service and Directory Service Data policies to express conditions. For a complete list of AWS keys, see [Available Global Condition Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys) in the *IAM User Guide*. 

## Directory Service API and required permissions for actions
<a name="actions-related-to-objects-table"></a>


| Directory Service API Operations | Required Permissions (API Actions) | Resources | 
| --- | --- | --- | 
| [AcceptSharedDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AcceptSharedDirectory.html)  | ds:AcceptSharedDirectory | \* | 
| [AddIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AddIpRoutes.html)  | `ds:AddIpRoutes`<br />`ec2:DescribeSecurityGroup`<br />`ec2:AuthorizeSecurityGroupIngress`<br />`ec2:AuthorizeSecurityGroupEgress` | \* | 
| [AddTagsToResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_AddTagsToResource.html)  | ds:AddTagsToResource`ec2:CreateTags` | \* | 
| [CancelSchemaExtension](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CancelSchemaExtension.html)  | ds:CancelSchemaExtension | \* | 
|  [ConnectDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ConnectDirectory.html)  | `ds:ConnectDirectory`<br />`ec2:DescribeSubnets`<br />`ec2:DescribeVpcs`<br />`ec2:CreateSecurityGroup`<br />`ec2:CreateNetworkInterface`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:AuthorizeSecurityGroupIngress`<br />`ec2:AuthorizeSecurityGroupEgress`<br />`ec2:CreateTags` | \* | 
|  [CreateAlias](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateAlias.html)  | `ds:CreateAlias` | \* | 
|  [CreateComputer](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateComputer.html)  | `ds:CreateComputer` | \* | 
|  [CreateConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateConditionalForwarder.html)  | `ds:CreateConditionalForwarder` | \* | 
|  [CreateDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html)  | `ds:CreateDirectory`<br />`ec2:DescribeSubnets`<br />`ec2:DescribeVpcs`<br />`ec2:CreateSecurityGroup`<br />`ec2:CreateNetworkInterface`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:AuthorizeSecurityGroupIngress`<br />`ec2:AuthorizeSecurityGroupEgress`<br />`ec2:CreateTags` | \* | 
| [CreateLogSubscription](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateLogSubscription.html)  | ds:CreateLogSubscription | \* | 
|  [CreateMicrosoftAD](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html)  | `ds:CreateMicrosoftAD`<br />`ec2:DescribeSubnets`<br />`ec2:DescribeVpcs`<br />`ec2:CreateSecurityGroup`<br />`ec2:CreateNetworkInterface`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:AuthorizeSecurityGroupIngress`<br />`ec2:AuthorizeSecurityGroupEgress`<br />`ec2:RevokeSecurityGroupEgress`<br />`ec2:CreateTags` | \* | 
|  [CreateSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateSnapshot.html)  | `ds:CreateSnapshot` | \* | 
|  [CreateTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateTrust.html)  | `ds:CreateTrust` | \* | 
|  [DeleteConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteConditionalForwarder.html)  | `ds:DeleteConditionalForwarder` | \* | 
|  [DeleteDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteDirectory.html)  | `ds:DeleteDirectory`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:DeleteSecurityGroup`<br />`ec2:DeleteNetworkInterface`<br />`ec2:RevokeSecurityGroupIngress`<br />`ec2:RevokeSecurityGroupEgress`<br />`ec2:DeleteTags` | \* | 
| [DeleteLogSubscription](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteLogSubscription.html)  | ds:DeleteLogSubscription | \* | 
|  [DeleteSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteSnapshot.html)  | `ds:DeleteSnapshot` | \* | 
|  [DeleteTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeleteTrust.html)  | `ds:DeleteTrust` | \* | 
|  [DeregisterEventTopic](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DeregisterEventTopic.html)  | `ds:DeregisterEventTopic` | \* | 
|  [DescribeConditionalForwarders](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeConditionalForwarders.html)  | `ds:DescribeConditionalForwarders` | \* | 
|  [DescribeDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDirectories.html)  | `ds:DescribeDirectories` | \* | 
| [DescribeDomainControllers](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeDomainControllers.html)  | ds:DescribeDomainControllers | \* | 
|  [DescribeEventTopics](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeEventTopics.html)  | `ds:DescribeEventTopics` | \* | 
| [DescribeSharedDirectories](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSharedDirectories.html)  | ds:DescribeSharedDirectories | \* | 
|  [DescribeSnapshots](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeSnapshots.html)  | `ds:DescribeSnapshots` | \* | 
|  [DescribeTrusts](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DescribeTrusts.html)  | `ds:DescribeTrusts` | \* | 
|  [DisableRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableRadius.html)  | `ds:DisableRadius` | \* | 
|  [DisableSso](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DisableSso.html)  | `ds:DisableSso` | \* | 
|  [EnableRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableRadius.html)  | `ds:EnableRadius` | \* | 
|  [EnableSso](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_EnableSso.html)  | `ds:EnableSso` | \* | 
|  [GetDirectoryLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetDirectoryLimits.html)  | `ds:GetDirectoryLimits` | \* | 
|  [GetSnapshotLimits](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_GetSnapshotLimits.html)  | `ds:GetSnapshotLimits` | \* | 
| [ListIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListIpRoutes.html) | `ds:ListIpRoutes` | \* | 
| [ListLogSubscriptions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListLogSubscriptions.html)  | ds:ListLogSubscriptions | \* | 
| [ListSchemaExtensions](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListSchemaExtensions.html) | `ds:ListSchemaExtensions` | \* | 
| [ListTagsForResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ListTagsForResource.html) | `ds:ListTagsForResource` | \* | 
|  [RegisterEventTopic](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RegisterEventTopic.html)  | `ds:RegisterEventTopic`<br />`sns:GetTopicAttributes` | \* | 
| [RejectSharedDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RejectSharedDirectory.html)  | ds:RejectSharedDirectory | \* | 
| [RemoveIpRoutes](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RemoveIpRoutes.html) | `ds:RemoveIpRoutes` | \* | 
| [RemoveTagsFromResource](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RemoveTagsFromResource.html) | `ds:RemoveTagsFromResource`<br />`ec2:DeleteTags` | \* | 
| [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html)  | ds:ResetUserPassword | \* | 
|  [RestoreFromSnapshot](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_RestoreFromSnapshot.html)  | `ds:RestoreFromSnapshot` | \* | 
| [ShareDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ShareDirectory.html)  | `ds:ShareDirectory`<br />`organizations:DescribeAccount`<br />`organizations:DescribeOrganization`<br />`organizations:ListAWSServiceAccessForOrganization` | \* | 
| [StartSchemaExtension](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_StartSchemaExtension.html) | `ds:StartSchemaExtension` | \* | 
| [UnshareDirectory](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UnshareDirectory.html)  | ds:UnshareDirectory | \* | 
|  [UpdateConditionalForwarder](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateConditionalForwarder.html)  | `ds:UpdateConditionalForwarder` | \* | 
| [UpdateNumberOfDomainControllers](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateNumberOfDomainControllers.html)  | `ds:UpdateNumberOfDomainControllers`<br />`ec2:DescribeSubnets`<br />`ec2:DescribeVpcs`<br />`ec2:CreateNetworkInterface`<br />`ec2:DescribeNetworkInterfaces`<br />`ec2:DeleteNetworkInterface` | \* | 
|  [UpdateRadius](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateRadius.html)  | `ds:UpdateRadius` | \* | 
| [UpdateTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_UpdateTrust.html)  | ds:UpdateTrust | \* | 
|  [VerifyTrust](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_VerifyTrust.html)  | `ds:VerifyTrust` | \* | 

## AWS Directory Service Data API and required permissions for actions
<a name="DSData_ResourcePermissions"></a>

**Note**  
 To specify an action, use the `ds-data:` prefix followed by the name of the API operation (for example, `ds-data:AddGroupMember`). 


| Directory Service Data API Operations | Required Permissions (API Actions) | Resources | 
| --- | --- | --- | 
|  [AddGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AddGroupMember.html)  | `ds-data:AddGroupMember` | \* | 
|  [CreateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateGroup.html)  | `ds-data:CreateGroup` | \* | 
|  [CreateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_CreateUser.html)  | `ds-data:CreateUser` | \* | 
|  [DeleteGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DeleteGroup.html)  | `ds-data:DeleteGroup` | \* | 
|  [DeleteUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/DeleteUser.html)  | `ds-data:DeleteUser` | \* | 
|  [DescribeGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeGroup.html)  | `ds-data:DescribeGroup` | \* | 
|  [DescribeUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DescribeUser.html)  | `ds-data:DescribeUser` | \* | 
|  [DisableUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_DisableUser.html)  | `ds-data:DisableUser` | \* | 
|  [ListGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroups.html)  | `ds-data:ListGroups` | \* | 
|  [ListGroupMembers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupMembers.html)  | `ds-data:ListGroupMembers` | \* | 
|  [ListGroupsForMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListGroupsForMember.html)  | `ds-data:ListGroupsForMember` | \* | 
|  [ListUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_ListUsers.html)  | `ds-data:ListUsers` | \* | 
|  [RemoveGroupMember](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_RemoveGroupMember.html)  | `ds-data:RemoveGroupMember` | \* | 
|  [SearchGroups](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchGroups.html)  | `ds-data:DescribeGroup`<br />`ds-data:SearchGroups` | \* | 
| [SearchUsers](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_SearchUsers.html) | `ds-data:DescribeUser`<br />`ds-data:SearchUsers` | \* | 
| [UpdateGroup](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateGroup.html) | `ds-data:UpdateGroup` | \* | 
| [UpdateUser](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UpdateUser.html) | `ds-data:UpdateUser` | \* | 

## Related Topics
<a name="iam2_related"></a>
+ [Access control](iam_auth_access.md#access_control)