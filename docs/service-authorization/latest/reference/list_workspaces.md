

# Actions, resources, and condition keys for Amazon WorkSpaces
<a name="list_workspaces"></a>

Amazon WorkSpaces (service prefix: `workspaces`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/workspaces/latest/api/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/workspaces/workspaces.json) for this service.

**Topics**
+ [API operations defined by Amazon WorkSpaces](#list_workspaces-operations)
+ [Actions defined by Amazon WorkSpaces](#list_workspaces-actions-as-permissions)
+ [Permission-only actions for Amazon WorkSpaces](#list_workspaces-permission-only-actions)
+ [Resource types defined by Amazon WorkSpaces](#list_workspaces-resources-for-iam-policies)
+ [Condition keys for Amazon WorkSpaces](#list_workspaces-policy-keys)

## API operations defined by Amazon WorkSpaces
<a name="list_workspaces-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_workspaces-actions-as-permissions).




- **   AcceptAccountLinkInvitation  **
  - **IAM action:**  [workspaces:AcceptAccountLinkInvitation](#list_workspaces-action-AcceptAccountLinkInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateConnectionAlias  **
  - **IAM action:**  [workspaces:AssociateConnectionAlias](#list_workspaces-action-AssociateConnectionAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateIpGroups  **
  - **IAM action:**  [workspaces:AssociateIpGroups](#list_workspaces-action-AssociateIpGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateWorkspaceApplication  **
  - **IAM action:**  [workspaces:AssociateWorkspaceApplication](#list_workspaces-action-AssociateWorkspaceApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AuthorizeIpRules  **
  - **IAM action:**  [workspaces:AuthorizeIpRules](#list_workspaces-action-AuthorizeIpRules)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:UpdateRulesOfIpGroup](#list_workspaces-action-UpdateRulesOfIpGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CopyWorkspaceImage  **
  - **IAM action:**  [workspaces:CopyWorkspaceImage](#list_workspaces-action-CopyWorkspaceImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:DescribeWorkspaceImages](#list_workspaces-action-DescribeWorkspaceImages)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   CreateAccountLinkInvitation  **
  - **IAM action:**  [workspaces:CreateAccountLinkInvitation](#list_workspaces-action-CreateAccountLinkInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectClientAddIn  **
  - **IAM action:**  [workspaces:CreateConnectClientAddIn](#list_workspaces-action-CreateConnectClientAddIn) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateConnectionAlias  **
  - **IAM action:**  [workspaces:CreateConnectionAlias](#list_workspaces-action-CreateConnectionAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIpGroup  **
  - **IAM action:**  [workspaces:CreateIpGroup](#list_workspaces-action-CreateIpGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStandbyWorkspaces  **
  - **IAM action:**  [workspaces:CreateStandbyWorkspaces](#list_workspaces-action-CreateStandbyWorkspaces)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:DescribeWorkspaces](#list_workspaces-action-DescribeWorkspaces)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   CreateTags  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CreateUpdatedWorkspaceImage  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:CreateUpdatedWorkspaceImage](#list_workspaces-action-CreateUpdatedWorkspaceImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateWorkspaceBundle  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:CreateWorkspaceBundle](#list_workspaces-action-CreateWorkspaceBundle)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateWorkspaceImage  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:CreateWorkspaceImage](#list_workspaces-action-CreateWorkspaceImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateWorkspaces  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:CreateWorkspaces](#list_workspaces-action-CreateWorkspaces)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateWorkspacesPool  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:CreateWorkspacesPool](#list_workspaces-action-CreateWorkspacesPool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAccountLinkInvitation  **
  - **IAM action:**  [workspaces:DeleteAccountLinkInvitation](#list_workspaces-action-DeleteAccountLinkInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClientBranding  **
  - **IAM action:**  [workspaces:DeleteClientBranding](#list_workspaces-action-DeleteClientBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectClientAddIn  **
  - **IAM action:**  [workspaces:DeleteConnectClientAddIn](#list_workspaces-action-DeleteConnectClientAddIn) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectionAlias  **
  - **IAM action:**  [workspaces:DeleteConnectionAlias](#list_workspaces-action-DeleteConnectionAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIpGroup  **
  - **IAM action:**  [workspaces:DeleteIpGroup](#list_workspaces-action-DeleteIpGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **IAM action:**  [workspaces:DeleteTags](#list_workspaces-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteWorkspaceBundle  **
  - **IAM action:**  [workspaces:DeleteWorkspaceBundle](#list_workspaces-action-DeleteWorkspaceBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkspaceImage  **
  - **IAM action:**  [workspaces:DeleteWorkspaceImage](#list_workspaces-action-DeleteWorkspaceImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeployWorkspaceApplications  **
  - **IAM action:**  [workspaces:DeployWorkspaceApplications](#list_workspaces-action-DeployWorkspaceApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterWorkspaceDirectory  **
  - **IAM action:**  [workspaces:DeregisterWorkspaceDirectory](#list_workspaces-action-DeregisterWorkspaceDirectory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccount  **
  - **IAM action:**  [workspaces:DescribeAccount](#list_workspaces-action-DescribeAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAccountModifications  **
  - **IAM action:**  [workspaces:DescribeAccountModifications](#list_workspaces-action-DescribeAccountModifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApplicationAssociations  **
  - **IAM action:**  [workspaces:DescribeApplicationAssociations](#list_workspaces-action-DescribeApplicationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeApplications  **
  - **IAM action:**  [workspaces:DescribeApplications](#list_workspaces-action-DescribeApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeBundleAssociations  **
  - **IAM action:**  [workspaces:DescribeBundleAssociations](#list_workspaces-action-DescribeBundleAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeClientBranding  **
  - **IAM action:**  [workspaces:DescribeClientBranding](#list_workspaces-action-DescribeClientBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClientProperties  **
  - **IAM action:**  [workspaces:DescribeClientProperties](#list_workspaces-action-DescribeClientProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeConnectClientAddIns  **
  - **IAM action:**  [workspaces:DescribeConnectClientAddIns](#list_workspaces-action-DescribeConnectClientAddIns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeConnectionAliasPermissions  **
  - **IAM action:**  [workspaces:DescribeConnectionAliasPermissions](#list_workspaces-action-DescribeConnectionAliasPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectionAliases  **
  - **IAM action:**  [workspaces:DescribeConnectionAliases](#list_workspaces-action-DescribeConnectionAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCustomWorkspaceImageImport  **
  - **IAM action:**  [workspaces:DescribeCustomWorkspaceImageImport](#list_workspaces-action-DescribeCustomWorkspaceImageImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImageAssociations  **
  - **IAM action:**  [workspaces:DescribeImageAssociations](#list_workspaces-action-DescribeImageAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeIpGroups  **
  - **IAM action:**  [workspaces:DescribeIpGroups](#list_workspaces-action-DescribeIpGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTags  **
  - **IAM action:**  [workspaces:DescribeTags](#list_workspaces-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceAssociations  **
  - **IAM action:**  [workspaces:DescribeWorkspaceAssociations](#list_workspaces-action-DescribeWorkspaceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspaceBundles  **
  - **IAM action:**  [workspaces:DescribeWorkspaceBundles](#list_workspaces-action-DescribeWorkspaceBundles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspaceDirectories  **
  - **IAM action:**  [workspaces:DescribeWorkspaceDirectories](#list_workspaces-action-DescribeWorkspaceDirectories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceImagePermissions  **
  - **IAM action:**  [workspaces:DescribeWorkspaceImagePermissions](#list_workspaces-action-DescribeWorkspaceImagePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspaceImages  **
  - **IAM action:**  [workspaces:DescribeWorkspaceImages](#list_workspaces-action-DescribeWorkspaceImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspaceSnapshots  **
  - **IAM action:**  [workspaces:DescribeWorkspaceSnapshots](#list_workspaces-action-DescribeWorkspaceSnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspaces  **
  - **IAM action:**  [workspaces:DescribeWorkspaces](#list_workspaces-action-DescribeWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspacesConnectionStatus  **
  - **IAM action:**  [workspaces:DescribeWorkspacesConnectionStatus](#list_workspaces-action-DescribeWorkspacesConnectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkspacesPoolSessions  **
  - **IAM action:**  [workspaces:DescribeWorkspacesPoolSessions](#list_workspaces-action-DescribeWorkspacesPoolSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeWorkspacesPools  **
  - **IAM action:**  [workspaces:DescribeWorkspacesPools](#list_workspaces-action-DescribeWorkspacesPools) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateConnectionAlias  **
  - **IAM action:**  [workspaces:DisassociateConnectionAlias](#list_workspaces-action-DisassociateConnectionAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateIpGroups  **
  - **IAM action:**  [workspaces:DisassociateIpGroups](#list_workspaces-action-DisassociateIpGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWorkspaceApplication  **
  - **IAM action:**  [workspaces:DisassociateWorkspaceApplication](#list_workspaces-action-DisassociateWorkspaceApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountLink  **
  - **IAM action:**  [workspaces:GetAccountLink](#list_workspaces-action-GetAccountLink) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportClientBranding  **
  - **IAM action:**  [workspaces:ImportClientBranding](#list_workspaces-action-ImportClientBranding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ImportCustomWorkspaceImage  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:ImportCustomWorkspaceImage](#list_workspaces-action-ImportCustomWorkspaceImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ImportWorkspaceImage  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:ImportWorkspaceImage](#list_workspaces-action-ImportWorkspaceImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListAccountLinks  **
  - **IAM action:**  [workspaces:ListAccountLinks](#list_workspaces-action-ListAccountLinks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAvailableManagementCidrRanges  **
  - **IAM action:**  [workspaces:ListAvailableManagementCidrRanges](#list_workspaces-action-ListAvailableManagementCidrRanges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   MigrateWorkspace  **
  - **IAM action:**  [workspaces:MigrateWorkspace](#list_workspaces-action-MigrateWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyAccount  **
  - **IAM action:**  [workspaces:ModifyAccount](#list_workspaces-action-ModifyAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyCertificateBasedAuthProperties  **
  - **IAM action:**  [workspaces:ModifyCertificateBasedAuthProperties](#list_workspaces-action-ModifyCertificateBasedAuthProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyClientProperties  **
  - **IAM action:**  [workspaces:ModifyClientProperties](#list_workspaces-action-ModifyClientProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyEndpointEncryptionMode  **
  - **IAM action:**  [workspaces:ModifyEndpointEncryptionMode](#list_workspaces-action-ModifyEndpointEncryptionMode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifySamlProperties  **
  - **IAM action:**  [workspaces:ModifySamlProperties](#list_workspaces-action-ModifySamlProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifySelfservicePermissions  **
  - **IAM action:**  [workspaces:ModifySelfservicePermissions](#list_workspaces-action-ModifySelfservicePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ModifyStreamingProperties  **
  - **IAM action:**  [workspaces:ModifyStreamingProperties](#list_workspaces-action-ModifyStreamingProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyWorkspaceAccessProperties  **
  - **IAM action:**  [workspaces:ModifyWorkspaceAccessProperties](#list_workspaces-action-ModifyWorkspaceAccessProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyWorkspaceCreationProperties  **
  - **IAM action:**  [workspaces:ModifyWorkspaceCreationProperties](#list_workspaces-action-ModifyWorkspaceCreationProperties)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** workspaces.amazonaws.com / **Access level:** Write

- **   ModifyWorkspaceProperties  **
  - **IAM action:**  [workspaces:ModifyWorkspaceProperties](#list_workspaces-action-ModifyWorkspaceProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyWorkspaceState  **
  - **IAM action:**  [workspaces:ModifyWorkspaceState](#list_workspaces-action-ModifyWorkspaceState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebootWorkspaces  **
  - **IAM action:**  [workspaces:RebootWorkspaces](#list_workspaces-action-RebootWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RebuildWorkspaces  **
  - **IAM action:**  [workspaces:RebuildWorkspaces](#list_workspaces-action-RebuildWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterWorkspaceDirectory  **
  - **IAM action:**  [workspaces:CreateTags](#list_workspaces-action-CreateTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [workspaces:RegisterWorkspaceDirectory](#list_workspaces-action-RegisterWorkspaceDirectory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RejectAccountLinkInvitation  **
  - **IAM action:**  [workspaces:RejectAccountLinkInvitation](#list_workspaces-action-RejectAccountLinkInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RestoreWorkspace  **
  - **IAM action:**  [workspaces:RestoreWorkspace](#list_workspaces-action-RestoreWorkspace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeIpRules  **
  - **IAM action:**  [workspaces:RevokeIpRules](#list_workspaces-action-RevokeIpRules)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:UpdateRulesOfIpGroup](#list_workspaces-action-UpdateRulesOfIpGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartWorkspaces  **
  - **IAM action:**  [workspaces:StartWorkspaces](#list_workspaces-action-StartWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartWorkspacesPool  **
  - **IAM action:**  [workspaces:StartWorkspacesPool](#list_workspaces-action-StartWorkspacesPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopWorkspaces  **
  - **IAM action:**  [workspaces:StopWorkspaces](#list_workspaces-action-StopWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopWorkspacesPool  **
  - **IAM action:**  [workspaces:StopWorkspacesPool](#list_workspaces-action-StopWorkspacesPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateWorkspaces  **
  - **IAM action:**  [workspaces:TerminateWorkspaces](#list_workspaces-action-TerminateWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateWorkspacesPool  **
  - **IAM action:**  [workspaces:TerminateWorkspacesPool](#list_workspaces-action-TerminateWorkspacesPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateWorkspacesPoolSession  **
  - **IAM action:**  [workspaces:TerminateWorkspacesPoolSession](#list_workspaces-action-TerminateWorkspacesPoolSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectClientAddIn  **
  - **IAM action:**  [workspaces:UpdateConnectClientAddIn](#list_workspaces-action-UpdateConnectClientAddIn) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectionAliasPermission  **
  - **IAM action:**  [workspaces:UpdateConnectionAliasPermission](#list_workspaces-action-UpdateConnectionAliasPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateRulesOfIpGroup  **
  - **IAM action:**  [workspaces:AuthorizeIpRules](#list_workspaces-action-AuthorizeIpRules)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:RevokeIpRules](#list_workspaces-action-RevokeIpRules)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [workspaces:UpdateRulesOfIpGroup](#list_workspaces-action-UpdateRulesOfIpGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateWorkspaceBundle  **
  - **IAM action:**  [workspaces:UpdateWorkspaceBundle](#list_workspaces-action-UpdateWorkspaceBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkspaceImagePermission  **
  - **IAM action:**  [workspaces:UpdateWorkspaceImagePermission](#list_workspaces-action-UpdateWorkspaceImagePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   UpdateWorkspacesPool  **
  - **IAM action:**  [workspaces:UpdateWorkspacesPool](#list_workspaces-action-UpdateWorkspacesPool) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon WorkSpaces
<a name="list_workspaces-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_AcceptAccountLinkInvitation.html)  **
  - **Description:** Grants permission to accept invitations from other AWS accounts to share the same configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateConnectionAlias](https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateConnectionAlias.html)  **
  - **Description:** Grants permission to associate connection aliases with directories
  - **Resource types (\*required):** [connectionalias\*](#list_workspaces-resource-connectionalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateIpGroups](https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateIpGroups.html)  **
  - **Description:** Grants permission to associate IP access control groups with directories
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateWorkspaceApplication](https://docs.aws.amazon.com/workspaces/latest/api/API_AssociateWorkspaceApplication.html)  **
  - **Description:** Grants permission to associate a workspace application with a WorkSpace
  - **Resource types (\*required):** [workspaceapplication\*](#list_workspaces-resource-workspaceapplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AuthorizeIpRules](https://docs.aws.amazon.com/workspaces/latest/api/API_AuthorizeIpRules.html)  **
  - **Description:** Grants permission to add rules to IP access control groups
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CopyWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CopyWorkspaceImage.html)  **
  - **Description:** Grants permission to copy a WorkSpace image
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateAccountLinkInvitation.html)  **
  - **Description:** Grants permission to invite other AWS accounts to share the same configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConnectClientAddIn](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateConnectClientAddIn.html)  **
  - **Description:** Grants permission to create an Amazon Connect client add-in within a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConnectionAlias](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateConnectionAlias.html)  **
  - **Description:** Grants permission to create connection aliases for use with cross-Region redirection
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIpGroup](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateIpGroup.html)  **
  - **Description:** Grants permission to create IP access control groups
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStandbyWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateStandbyWorkspaces.html)  **
  - **Description:** Grants permission to create one or more Standby WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTags](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateTags.html)  **
  - **Description:** Grants permission to create tags for WorkSpaces resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [CreateUpdatedWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateUpdatedWorkspaceImage.html)  **
  - **Description:** Grants permission to create an updated WorkSpace image
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceBundle.html)  **
  - **Description:** Grants permission to create a WorkSpace bundle
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html)  **
  - **Description:** Grants permission to create a new WorkSpace image
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaces.html)  **
  - **Description:** Grants permission to create one or more WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkspacesPool](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspacesPool.html)  **
  - **Description:** Grants permission to create a WorkSpaces Pool
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteAccountLinkInvitation.html)  **
  - **Description:** Grants permission to delete invitations to other AWS accounts to share the same configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteClientBranding](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteClientBranding.html)  **
  - **Description:** Grants permission to delete AWS WorkSpaces Client branding data within a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectClientAddIn](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteConnectClientAddIn.html)  **
  - **Description:** Grants permission to delete an Amazon Connect client add-in that is configured within a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnectionAlias](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteConnectionAlias.html)  **
  - **Description:** Grants permission to delete connection aliases
  - **Resource types (\*required):** [connectionalias\*](#list_workspaces-resource-connectionalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIpGroup](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteIpGroup.html)  **
  - **Description:** Grants permission to delete IP access control groups
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteTags.html)  **
  - **Description:** Grants permission to delete tags from WorkSpaces resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [DeleteWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceBundle.html)  **
  - **Description:** Grants permission to delete WorkSpace bundles
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceImage.html)  **
  - **Description:** Grants permission to delete WorkSpace images
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeployWorkspaceApplications](https://docs.aws.amazon.com/workspaces/latest/api/API_DeployWorkspaceApplications.html)  **
  - **Description:** Grants permission to deploy all pending workspace applications on a WorkSpace
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterWorkspaceDirectory](https://docs.aws.amazon.com/workspaces/latest/api/API_DeregisterWorkspaceDirectory.html)  **
  - **Description:** Grants permission to deregister directories from use with Amazon WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAccount](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccount.html)  **
  - **Description:** Grants permission to retrieve the configuration of Bring Your Own License (BYOL) for WorkSpaces accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAccountModifications](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html)  **
  - **Description:** Grants permission to retrieve modifications to the configuration of Bring Your Own License (BYOL) for WorkSpaces accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeApplicationAssociations](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeApplicationAssociations.html)  **
  - **Description:** Grants permission to retrieve information about resources associated with a WorkSpace application
  - **Resource types (\*required):** [workspaceapplication\*](#list_workspaces-resource-workspaceapplication)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeApplications](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeApplications.html)  **
  - **Description:** Grants permission to obtain information about WorkSpace applications
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeBundleAssociations](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeBundleAssociations.html)  **
  - **Description:** Grants permission to retrieve information about resources associated with a WorkSpace bundle
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeClientBranding](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeClientBranding.html)  **
  - **Description:** Grants permission to retrieve AWS WorkSpaces Client branding data within a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClientProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeClientProperties.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpaces clients
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeConnectClientAddIns](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectClientAddIns.html)  **
  - **Description:** Grants permission to retrieve a list of Amazon Connect client add-ins that have been created
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeConnectionAliasPermissions](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliasPermissions.html)  **
  - **Description:** Grants permission to retrieve the permissions that the owners of connection aliases have granted to other AWS accounts for connection aliases
  - **Resource types (\*required):** [connectionalias\*](#list_workspaces-resource-connectionalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnectionAliases](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html)  **
  - **Description:** Grants permission to retrieve a list that describes the connection aliases used for cross-Region redirection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeCustomWorkspaceImageImport](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeCustomWorkspaceImageImport.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpace BYOL image import task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeImageAssociations](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeImageAssociations.html)  **
  - **Description:** Grants permission to retrieve information about resources associated with a WorkSpace image
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeIpGroups](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeIpGroups.html)  **
  - **Description:** Grants permission to retrieve information about IP access control groups
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTags](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeTags.html)  **
  - **Description:** Grants permission to describe the tags for WorkSpaces resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeWorkspaceAssociations](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceAssociations.html)  **
  - **Description:** Grants permission to retrieve information about resources associated with a WorkSpace
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeWorkspaceBundles](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceBundles.html)  **
  - **Description:** Grants permission to obtain information about WorkSpace bundles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html)  **
  - **Description:** Grants permission to retrieve information about directories that are registered with WorkSpaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeWorkspaceImagePermissions](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpace image permissions
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkspaceImages](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpace images
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeWorkspaceSnapshots](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceSnapshots.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpace snapshots
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html)  **
  - **Description:** Grants permission to obtain information about WorkSpaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeWorkspacesConnectionStatus](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesConnectionStatus.html)  **
  - **Description:** Grants permission to obtain the connection status of WorkSpaces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeWorkspacesPoolSessions](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesPoolSessions.html)  **
  - **Description:** Grants permission to retrieve information about the sessions of a WorkSpaces Pool
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeWorkspacesPools](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspacesPools.html)  **
  - **Description:** Grants permission to retrieve information about WorkSpaces Pools
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisassociateConnectionAlias](https://docs.aws.amazon.com/workspaces/latest/api/API_DisassociateConnectionAlias.html)  **
  - **Description:** Grants permission to disassociate connection aliases from directories
  - **Resource types (\*required):** [connectionalias\*](#list_workspaces-resource-connectionalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateIpGroups](https://docs.aws.amazon.com/workspaces/latest/api/API_DisassociateIpGroups.html)  **
  - **Description:** Grants permission to disassociate IP access control groups from directories
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWorkspaceApplication](https://docs.aws.amazon.com/workspaces/latest/api/API_DisassociateWorkspaceApplication.html)  **
  - **Description:** Grants permission to disassociate a workspace application from a WorkSpace
  - **Resource types (\*required):** [workspaceapplication\*](#list_workspaces-resource-workspaceapplication) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountLink](https://docs.aws.amazon.com/workspaces/latest/api/API_GetAccountLink.html)  **
  - **Description:** Grants permission to retrieve a link with another AWS Account for sharing configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportClientBranding](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportClientBranding.html)  **
  - **Description:** Grants permission to import AWS WorkSpaces Client branding data within a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ImportCustomWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportCustomWorkspaceImage.html)  **
  - **Description:** Grants permission to import Bring Your Own License (BYOL) images into Amazon WorkSpaces
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [ImportWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html)  **
  - **Description:** Grants permission to import Bring Your Own License (BYOL) images into Amazon WorkSpaces
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [ListAccountLinks](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAccountLinks.html)  **
  - **Description:** Grants permission to retrieve links with the AWS Account(s) that share your configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAvailableManagementCidrRanges](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html)  **
  - **Description:** Grants permission to list the available CIDR ranges for enabling Bring Your Own License (BYOL) for WorkSpaces accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [MigrateWorkspace](https://docs.aws.amazon.com/workspaces/latest/api/API_MigrateWorkspace.html)  **
  - **Description:** Grants permission to migrate WorkSpaces
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyAccount](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html)  **
  - **Description:** Grants permission to modify the configuration of Bring Your Own License (BYOL) for WorkSpaces accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ModifyCertificateBasedAuthProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyCertificateBasedAuthProperties.html)  **
  - **Description:** Grants permission to modify the certificate-based authorization properties of a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyClientProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyClientProperties.html)  **
  - **Description:** Grants permission to modify the properties of WorkSpaces clients
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyEndpointEncryptionMode](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyEndpointEncryptionMode.html)  **
  - **Description:** Grants permission to configure the specified directory between Standard TLS and FIPS 140-2 validated mode
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifySamlProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifySamlProperties.html)  **
  - **Description:** Grants permission to modify the SAML properties of a directory
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifySelfservicePermissions](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifySelfservicePermissions.html)  **
  - **Description:** Grants permission to modify the self-service WorkSpace management capabilities for your users
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ModifyStreamingProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyStreamingProperties.html)  **
  - **Description:** Grants permission to modify the streaming properties
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyWorkspaceAccessProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceAccessProperties.html)  **
  - **Description:** Grants permission to specify which devices and operating systems users can use to access their WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyWorkspaceCreationProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceCreationProperties.html)  **
  - **Description:** Grants permission to modify the default properties used to create WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyWorkspaceProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceProperties.html)  **
  - **Description:** Grants permission to modify WorkSpace properties, including the running mode and the AutoStop period
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyWorkspaceState](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceState.html)  **
  - **Description:** Grants permission to modify the state of WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebootWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_RebootWorkspaces.html)  **
  - **Description:** Grants permission to reboot WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RebuildWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_RebuildWorkspaces.html)  **
  - **Description:** Grants permission to rebuild WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html)  **
  - **Description:** Grants permission to register directories for use with Amazon WorkSpaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_workspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_workspaces-aws_TagKeys)
  - **Access level:** Write

- **   [RejectAccountLinkInvitation](https://docs.aws.amazon.com/workspaces/latest/api/API_RejectAccountLinkInvitation.html)  **
  - **Description:** Grants permission to reject invitations from other AWS accounts to share the same configuration for WorkSpaces BYOL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RestoreWorkspace](https://docs.aws.amazon.com/workspaces/latest/api/API_RestoreWorkspace.html)  **
  - **Description:** Grants permission to restore WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeIpRules](https://docs.aws.amazon.com/workspaces/latest/api/API_RevokeIpRules.html)  **
  - **Description:** Grants permission to remove rules from IP access control groups
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspaces.html)  **
  - **Description:** Grants permission to start AutoStop WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartWorkspacesPool](https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspacesPool.html)  **
  - **Description:** Grants permission to start a WorkSpaces Pool
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspaces.html)  **
  - **Description:** Grants permission to stop AutoStop WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopWorkspacesPool](https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspacesPool.html)  **
  - **Description:** Grants permission to stop a WorkSpaces Pool
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Stream](https://docs.aws.amazon.com/workspaces/latest/api/API_Stream.html)  **
  - **Description:** Grants permission to federated users to sign in by using their existing credentials and stream their workspace
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)<br />[workspaces:userId](#list_workspaces-workspaces_userId)
  - **Access level:** Write

- **   [TerminateWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspaces.html)  **
  - **Description:** Grants permission to terminate WorkSpaces
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateWorkspacesPool](https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspacesPool.html)  **
  - **Description:** Grants permission to terminate a WorkSpaces Pool
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateWorkspacesPoolSession](https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspacesPoolSession.html)  **
  - **Description:** Grants permission to terminate a WorkSpaces Pool session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnectClientAddIn](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateConnectClientAddIn.html)  **
  - **Description:** Grants permission to update an Amazon Connect client add-in. Use this action to update the name and endpoint URL of an Amazon Connect client add-in
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnectionAliasPermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateConnectionAliasPermission.html)  **
  - **Description:** Grants permission to share or unshare connection aliases with other accounts
  - **Resource types (\*required):** [connectionalias\*](#list_workspaces-resource-connectionalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateRulesOfIpGroup](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateRulesOfIpGroup.html)  **
  - **Description:** Grants permission to replace rules for IP access control groups
  - **Resource types (\*required):** [workspaceipgroup\*](#list_workspaces-resource-workspaceipgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html)  **
  - **Description:** Grants permission to update the WorkSpace images used in WorkSpace bundles
  - **Resource types (\*required):** [workspacebundle\*](#list_workspaces-resource-workspacebundle) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html)  **
  - **Description:** Grants permission to share or unshare WorkSpace images with other accounts by specifying whether other accounts have permission to copy the image
  - **Resource types (\*required):** [workspaceimage\*](#list_workspaces-resource-workspaceimage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateWorkspacesPool](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspacesPool.html)  **
  - **Description:** Grants permission to update the WorkSpaces pool
  - **Resource types (\*required):** [workspacespool\*](#list_workspaces-resource-workspacespool)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon WorkSpaces
<a name="list_workspaces-permission-only-actions"></a>

The following actions are defined by Amazon WorkSpaces but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateRootClientCertificate](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to create a root client certificate
  - **Resource types (\*required):** [certificateid\*](#list_workspaces-resource-certificateid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRootClientCertificate](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to delete root client certificate
  - **Resource types (\*required):** [certificateid\*](#list_workspaces-resource-certificateid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeConsent](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to retrieve information about consent agreement to BYOL minimum requirements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DirectoryAccessManagement](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to directory management actions while managing and provisioning workspaces
  - **Resource types (\*required):** [directoryid\*](#list_workspaces-resource-directoryid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetTroubleshootingRecommendation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-advisor.html)  **
  - **Description:** Grants permission to get troubleshooting recommendations
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeOnboardingAgent](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to use WorkSpaces Advisor for WorkSpace onboarding
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [InvokeTroubleshootingInvestigation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-advisor.html)  **
  - **Description:** Grants permission to invoke troubleshooting investigation
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTroubleshootingRecommendations](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-advisor.html)  **
  - **Description:** Grants permission to list troubleshooting recommendations
  - **Resource types (\*required):** [workspaceid\*](#list_workspaces-resource-workspaceid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Personalization](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to manage features that enable personalization of the WorkSpaces console experience
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConsent](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to update the consent agreement to BYOL minimum requirements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRootClientCertificate](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html)  **
  - **Description:** Grants permission to update a root client certificate
  - **Resource types (\*required):** [certificateid\*](#list_workspaces-resource-certificateid)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon WorkSpaces
<a name="list_workspaces-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [certificateid](https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspacecertificate/${CertificateId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [connectionalias](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html)  | arn:${Partition}:workspaces:${Region}:${Account}:connectionalias/${ConnectionAliasId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [directoryid](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html)  | arn:${Partition}:workspaces:${Region}:${Account}:directory/${DirectoryId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspaceapplication](https://docs.aws.amazon.com/workspaces/latest/adminguide/application-bundle-management.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspaceapplication/${WorkSpaceApplicationId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspacebundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspacebundle/${BundleId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspaceid](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp_workspace_management.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspace/${WorkspaceId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspaceimage](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundles.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspaceimage/${ImageId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspaceipgroup](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspaceipgroup/${GroupId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 
|  [workspacespool](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-pools.html)  | arn:${Partition}:workspaces:${Region}:${Account}:workspacespool/${PoolId} | [aws:ResourceTag/${TagKey}](#list_workspaces-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon WorkSpaces
<a name="list_workspaces-policy-keys"></a>

Amazon WorkSpaces defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 
|   [workspaces:userId](https://docs.aws.amazon.com/workspaces/latest/adminguide/external-identity-providers-setting-up-saml.html#external-identity-providers-embed-inline-policy-for-IAM-role)  | Filters access by the ID of the Workspaces user | String | 