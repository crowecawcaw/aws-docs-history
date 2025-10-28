# WorkSpaces Core bundles management

To perform various actions for Amazon WorkSpaces Core, use the following API operations. To help you
create your workflow, we have provided a recommendation for each API operation. We recommend
partners solutions use as many of these APIs as possible so that admin customers don’t need to
access the WorkSpaces console.

- Deployment and setup
  - [CreateTags](../../../workspaces/latest/api/API_CreateTags.md "../../../workspaces/latest/api/API_CreateTags.md")
  - [DescribeAccount](../../../workspaces/latest/api/API_DescribeAccount.md "../../../workspaces/latest/api/API_DescribeAccount.md")
  - [DescribeAccountModifications](../../../workspaces/latest/api/API_DescribeAccountModifications.md "../../../workspaces/latest/api/API_DescribeAccountModifications.md")
  - [ImportWorkspaceImage](../../../workspaces/latest/api/API_ImportWorkspaceImage.md "../../../workspaces/latest/api/API_ImportWorkspaceImage.md")
  - [ModifyAccount](../../../workspaces/latest/api/API_ModifyAccount.md "../../../workspaces/latest/api/API_ModifyAccount.md")
  - [ListAvailableManagementCidrRanges](../../../workspaces/latest/api/API_ListAvailableManagementCidrRanges.md "../../../workspaces/latest/api/API_ListAvailableManagementCidrRanges.md")
  - [RegisterWorkspaceDirectory](../../../workspaces/latest/api/API_RegisterWorkspaceDirectory.md "../../../workspaces/latest/api/API_RegisterWorkspaceDirectory.md")

- Operations
  - [CopyWorkspaceImage](../../../workspaces/latest/api/API_CopyWorkspaceImage.md "../../../workspaces/latest/api/API_CopyWorkspaceImage.md") – Supports an
    `UpdateWorkspaceBundle` image process and copying from one AWS Region to
    another Region.
  - [CreateWorkspaceImage](../../../workspaces/latest/api/API_CreateWorkspaceImage.md "../../../workspaces/latest/api/API_CreateWorkspaceImage.md") – Supports custom images and
    workflows for day-two operations.
  - [DescribeTags](../../../workspaces/latest/api/API_DescribeTags.md "../../../workspaces/latest/api/API_DescribeTags.md")
  - [DescribeWorkspaceBundles](../../../workspaces/latest/api/API_DescribeWorkspaceBundles.md "../../../workspaces/latest/api/API_DescribeWorkspaceBundles.md")
  - [DescribeWorkspaceDirectories](../../../workspaces/latest/api/API_DescribeWorkspaceDirectories.md "../../../workspaces/latest/api/API_DescribeWorkspaceDirectories.md")
  - [DescribeWorkspaceImagePermissions](../../../workspaces/latest/api/API_DescribeWorkspaceImagePermissions.md "../../../workspaces/latest/api/API_DescribeWorkspaceImagePermissions.md")
  - [DescribeWorkspaceImages](../../../workspaces/latest/api/API_DescribeWorkspaceImages.md "../../../workspaces/latest/api/API_DescribeWorkspaceImages.md")
  - [DescribeWorkspaces](../../../workspaces/latest/api/API_DescribeWorkspaces.md "../../../workspaces/latest/api/API_DescribeWorkspaces.md")
  - [DescribeWorkspaceSnapshots](../../../workspaces/latest/api/API_DescribeWorkspaceSnapshots.md "../../../workspaces/latest/api/API_DescribeWorkspaceSnapshots.md")
  - [MigrateWorkspace](../../../workspaces/latest/api/API_MigrateWorkspace.md "../../../workspaces/latest/api/API_MigrateWorkspace.md")
  - [ModifyWorkspaceCreationProperties](../../../workspaces/latest/api/API_ModifyWorkspaceCreationProperties.md "../../../workspaces/latest/api/API_ModifyWorkspaceCreationProperties.md")
  - [ModifyWorkspaceProperties](../../../workspaces/latest/api/API_ModifyWorkspaceProperties.md "../../../workspaces/latest/api/API_ModifyWorkspaceProperties.md") – Supports modification of
    the following properties:
    - [ComputeTypeName](../../../workspaces/latest/api/API_WorkspaceProperties.md "../../../workspaces/latest/api/API_WorkspaceProperties.md")
    - [RootVolumeSizeGib](../../../workspaces/latest/api/API_WorkspaceProperties.md "../../../workspaces/latest/api/API_WorkspaceProperties.md")
    - [RunningMode](../../../workspaces/latest/api/API_WorkspaceProperties.md "../../../workspaces/latest/api/API_WorkspaceProperties.md") – BYOP must use
      `ALWAYS_ON` or `MANUAL`.
    - [UserVolumeSizeGib](../../../workspaces/latest/api/API_WorkspaceProperties.md "../../../workspaces/latest/api/API_WorkspaceProperties.md")

  - [ModifyWorkspaceState](../../../workspaces/latest/api/API_ModifyWorkspaceState.md "../../../workspaces/latest/api/API_ModifyWorkspaceState.md")
  - [RebootWorkspaces](../../../workspaces/latest/api/API_RebootWorkspaces.md "../../../workspaces/latest/api/API_RebootWorkspaces.md")
  - [RebuildWorkspaces](../../../workspaces/latest/api/API_RebuildWorkspaces.md "../../../workspaces/latest/api/API_RebuildWorkspaces.md")
  - [RestoreWorkspace](../../../workspaces/latest/api/API_RestoreWorkspace.md "../../../workspaces/latest/api/API_RestoreWorkspace.md")
  - [StartWorkspaces](../../../workspaces/latest/api/API_StartWorkspaces.md "../../../workspaces/latest/api/API_StartWorkspaces.md")
  - [StopWorkspaces](../../../workspaces/latest/api/API_StopWorkspaces.md "../../../workspaces/latest/api/API_StopWorkspaces.md")
  - [UpdateWorkspaceBundle](../../../workspaces/latest/api/API_UpdateWorkspaceBundle.md "../../../workspaces/latest/api/API_UpdateWorkspaceBundle.md")
  - [UpdateWorkspaceImagePermission](../../../workspaces/latest/api/API_UpdateWorkspaceImagePermission.md "../../../workspaces/latest/api/API_UpdateWorkspaceImagePermission.md")

- Termination
  - [DeleteTags](../../../workspaces/latest/api/API_DeleteTags.md "../../../workspaces/latest/api/API_DeleteTags.md")
  - [DeleteWorkspaceBundle](../../../workspaces/latest/api/API_DeleteWorkspaceBundle.md "../../../workspaces/latest/api/API_DeleteWorkspaceBundle.md")
  - [DeleteWorkspaceImage](../../../workspaces/latest/api/API_DeleteWorkspaceImage.md "../../../workspaces/latest/api/API_DeleteWorkspaceImage.md")
  - [DeregisterWorkspaceDirectory](../../../workspaces/latest/api/API_DeregisterWorkspaceDirectory.md "../../../workspaces/latest/api/API_DeregisterWorkspaceDirectory.md")
  - [TerminateWorkspaces](../../../workspaces/latest/api/API_TerminateWorkspaces.md "../../../workspaces/latest/api/API_TerminateWorkspaces.md")
