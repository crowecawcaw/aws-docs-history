

# WorkSpaces Core bundles management
<a name="lifecyle-management-of-instances"></a>

 To perform various actions for Amazon WorkSpaces Core, use the following API operations. To help you create your workflow, we have provided a recommendation for each API operation. We recommend partners solutions use as many of these APIs as possible so that admin customers don’t need to access the WorkSpaces console.
+ Deployment and setup
  + [CreateTags](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateTags.html)
  + [DescribeAccount](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccount.html)
  + [DescribeAccountModifications](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeAccountModifications.html)
  + [ImportWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_ImportWorkspaceImage.html)
  + [ModifyAccount](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyAccount.html)
  + [ListAvailableManagementCidrRanges](https://docs.aws.amazon.com/workspaces/latest/api/API_ListAvailableManagementCidrRanges.html)
  + [RegisterWorkspaceDirectory](https://docs.aws.amazon.com/workspaces/latest/api/API_RegisterWorkspaceDirectory.html)
+ Operations
  + [CopyWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CopyWorkspaceImage.html) – Supports an `UpdateWorkspaceBundle` image process and copying from one AWS Region to another Region.
  + [CreateWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_CreateWorkspaceImage.html) – Supports custom images and workflows for day-two operations.
  + [DescribeTags](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeTags.html)
  + [DescribeWorkspaceBundles](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceBundles.html)
  + [DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html)
  + [DescribeWorkspaceImagePermissions](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html)
  + [DescribeWorkspaceImages](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html)
  + [DescribeWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html)
  + [DescribeWorkspaceSnapshots](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceSnapshots.html)
  + [MigrateWorkspace](https://docs.aws.amazon.com/workspaces/latest/api/API_MigrateWorkspace.html)
  + [ModifyWorkspaceCreationProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceCreationProperties.html)
  + [ModifyWorkspaceProperties](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceProperties.html) – Supports modification of the following properties:
    + [ComputeTypeName](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
    + [RootVolumeSizeGib](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
    + [RunningMode](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html) – BYOP must use `ALWAYS_ON` or `MANUAL`.
    + [UserVolumeSizeGib](https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html)
  + [ModifyWorkspaceState](https://docs.aws.amazon.com/workspaces/latest/api/API_ModifyWorkspaceState.html)
  + [RebootWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_RebootWorkspaces.html)
  + [RebuildWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_RebuildWorkspaces.html)
  + [RestoreWorkspace](https://docs.aws.amazon.com/workspaces/latest/api/API_RestoreWorkspace.html)
  + [StartWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_StartWorkspaces.html)
  + [StopWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_StopWorkspaces.html)
  + [UpdateWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceBundle.html)
  + [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html)
+ Termination
  + [DeleteTags](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteTags.html)
  + [DeleteWorkspaceBundle](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceBundle.html)
  + [DeleteWorkspaceImage](https://docs.aws.amazon.com/workspaces/latest/api/API_DeleteWorkspaceImage.html)
  + [DeregisterWorkspaceDirectory](https://docs.aws.amazon.com/workspaces/latest/api/API_DeregisterWorkspaceDirectory.html)
  + [TerminateWorkspaces](https://docs.aws.amazon.com/workspaces/latest/api/API_TerminateWorkspaces.html)