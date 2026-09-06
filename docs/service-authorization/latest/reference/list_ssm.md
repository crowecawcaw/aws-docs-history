

# Actions, resources, and condition keys for AWS Systems Manager
<a name="list_ssm"></a>

AWS Systems Manager (service prefix: `ssm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/systems-manager/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm/ssm.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager](#list_ssm-operations)
+ [Actions defined by AWS Systems Manager](#list_ssm-actions-as-permissions)
+ [Permission-only actions for AWS Systems Manager](#list_ssm-permission-only-actions)
+ [Resource types defined by AWS Systems Manager](#list_ssm-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager](#list_ssm-policy-keys)

## API operations defined by AWS Systems Manager
<a name="list_ssm-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-actions-as-permissions).




- **   AddTagsToResource  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AssociateOpsItemRelatedItem  **
  - **IAM action:**  [ssm:AssociateOpsItemRelatedItem](#list_ssm-action-AssociateOpsItemRelatedItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelCommand  **
  - **IAM action:**  [ssm:CancelCommand](#list_ssm-action-CancelCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMaintenanceWindowExecution  **
  - **IAM action:**  [ssm:CancelMaintenanceWindowExecution](#list_ssm-action-CancelMaintenanceWindowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateActivation  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateActivation](#list_ssm-action-CreateActivation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   CreateAssociation  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateAssociation](#list_ssm-action-CreateAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   CreateAssociationBatch  **
  - **IAM action:**  [ssm:CreateAssociation](#list_ssm-action-CreateAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm:CreateAssociationBatch](#list_ssm-action-CreateAssociationBatch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   CreateCloudConnector  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateCloudConnector](#list_ssm-action-CreateCloudConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   CreateDocument  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateDocument](#list_ssm-action-CreateDocument)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm:GetDocument](#list_ssm-action-GetDocument)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** justintimeaccess.ssm.amazonaws.com, ssm.amazonaws.com / **Access level:** Write

- **   CreateMaintenanceWindow  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateMaintenanceWindow](#list_ssm-action-CreateMaintenanceWindow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateOpsItem  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateOpsItem](#list_ssm-action-CreateOpsItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateOpsMetadata  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreateOpsMetadata](#list_ssm-action-CreateOpsMetadata)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreatePatchBaseline  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:CreatePatchBaseline](#list_ssm-action-CreatePatchBaseline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateResourceDataSync  **
  - **IAM action:**  [ssm:CreateResourceDataSync](#list_ssm-action-CreateResourceDataSync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteActivation  **
  - **IAM action:**  [ssm:DeleteActivation](#list_ssm-action-DeleteActivation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssociation  **
  - **IAM action:**  [ssm:DeleteAssociation](#list_ssm-action-DeleteAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCloudConnector  **
  - **IAM action:**  [ssm:DeleteCloudConnector](#list_ssm-action-DeleteCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDocument  **
  - **IAM action:**  [ssm:DeleteDocument](#list_ssm-action-DeleteDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInventory  **
  - **IAM action:**  [ssm:DeleteInventory](#list_ssm-action-DeleteInventory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMaintenanceWindow  **
  - **IAM action:**  [ssm:DeleteMaintenanceWindow](#list_ssm-action-DeleteMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOpsItem  **
  - **IAM action:**  [ssm:DeleteOpsItem](#list_ssm-action-DeleteOpsItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOpsMetadata  **
  - **IAM action:**  [ssm:DeleteOpsMetadata](#list_ssm-action-DeleteOpsMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteParameter  **
  - **IAM action:**  [ssm:DeleteParameter](#list_ssm-action-DeleteParameter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteParameters  **
  - **IAM action:**  [ssm:DeleteParameters](#list_ssm-action-DeleteParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePatchBaseline  **
  - **IAM action:**  [ssm:DeletePatchBaseline](#list_ssm-action-DeletePatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceDataSync  **
  - **IAM action:**  [ssm:DeleteResourceDataSync](#list_ssm-action-DeleteResourceDataSync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [ssm:DeleteResourcePolicy](#list_ssm-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeregisterManagedInstance  **
  - **IAM action:**  [ssm:DeregisterManagedInstance](#list_ssm-action-DeregisterManagedInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterPatchBaselineForPatchGroup  **
  - **IAM action:**  [ssm:DeregisterPatchBaselineForPatchGroup](#list_ssm-action-DeregisterPatchBaselineForPatchGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTargetFromMaintenanceWindow  **
  - **IAM action:**  [ssm:DeregisterTargetFromMaintenanceWindow](#list_ssm-action-DeregisterTargetFromMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterTaskFromMaintenanceWindow  **
  - **IAM action:**  [ssm:DeregisterTaskFromMaintenanceWindow](#list_ssm-action-DeregisterTaskFromMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeActivations  **
  - **IAM action:**  [ssm:DescribeActivations](#list_ssm-action-DescribeActivations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssociation  **
  - **IAM action:**  [ssm:DescribeAssociation](#list_ssm-action-DescribeAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssociationExecutionTargets  **
  - **IAM action:**  [ssm:DescribeAssociationExecutionTargets](#list_ssm-action-DescribeAssociationExecutionTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssociationExecutions  **
  - **IAM action:**  [ssm:DescribeAssociationExecutions](#list_ssm-action-DescribeAssociationExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAutomationExecutions  **
  - **IAM action:**  [ssm:DescribeAutomationExecutions](#list_ssm-action-DescribeAutomationExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAutomationStepExecutions  **
  - **IAM action:**  [ssm:DescribeAutomationStepExecutions](#list_ssm-action-DescribeAutomationStepExecutions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   DescribeAvailablePatches  **
  - **IAM action:**  [ssm:DescribeAvailablePatches](#list_ssm-action-DescribeAvailablePatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDocument  **
  - **IAM action:**  [ssm:DescribeDocument](#list_ssm-action-DescribeDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDocumentPermission  **
  - **IAM action:**  [ssm:DescribeDocumentPermission](#list_ssm-action-DescribeDocumentPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEffectiveInstanceAssociations  **
  - **IAM action:**  [ssm:DescribeEffectiveInstanceAssociations](#list_ssm-action-DescribeEffectiveInstanceAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEffectivePatchesForPatchBaseline  **
  - **IAM action:**  [ssm:DescribeEffectivePatchesForPatchBaseline](#list_ssm-action-DescribeEffectivePatchesForPatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceAssociationsStatus  **
  - **IAM action:**  [ssm:DescribeInstanceAssociationsStatus](#list_ssm-action-DescribeInstanceAssociationsStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceInformation  **
  - **IAM action:**  [ssm:DescribeInstanceInformation](#list_ssm-action-DescribeInstanceInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstancePatchStates  **
  - **IAM action:**  [ssm:DescribeInstancePatchStates](#list_ssm-action-DescribeInstancePatchStates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstancePatchStatesForPatchGroup  **
  - **IAM action:**  [ssm:DescribeInstancePatchStatesForPatchGroup](#list_ssm-action-DescribeInstancePatchStatesForPatchGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstancePatches  **
  - **IAM action:**  [ssm:DescribeInstancePatches](#list_ssm-action-DescribeInstancePatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceProperties  **
  - **IAM action:**  [ssm:DescribeInstanceProperties](#list_ssm-action-DescribeInstanceProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInventoryDeletions  **
  - **IAM action:**  [ssm:DescribeInventoryDeletions](#list_ssm-action-DescribeInventoryDeletions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMaintenanceWindowExecutionTaskInvocations  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowExecutionTaskInvocations](#list_ssm-action-DescribeMaintenanceWindowExecutionTaskInvocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowExecutionTasks  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowExecutionTasks](#list_ssm-action-DescribeMaintenanceWindowExecutionTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowExecutions  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowExecutions](#list_ssm-action-DescribeMaintenanceWindowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowSchedule  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowSchedule](#list_ssm-action-DescribeMaintenanceWindowSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowTargets  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowTargets](#list_ssm-action-DescribeMaintenanceWindowTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowTasks  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowTasks](#list_ssm-action-DescribeMaintenanceWindowTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindows  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindows](#list_ssm-action-DescribeMaintenanceWindows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMaintenanceWindowsForTarget  **
  - **IAM action:**  [ssm:DescribeMaintenanceWindowsForTarget](#list_ssm-action-DescribeMaintenanceWindowsForTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeOpsItems  **
  - **IAM action:**  [ssm:DescribeOpsItems](#list_ssm-action-DescribeOpsItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeParameters  **
  - **IAM action:**  [ssm:DescribeParameters](#list_ssm-action-DescribeParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePatchBaselines  **
  - **IAM action:**  [ssm:DescribePatchBaselines](#list_ssm-action-DescribePatchBaselines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePatchGroupState  **
  - **IAM action:**  [ssm:DescribePatchGroupState](#list_ssm-action-DescribePatchGroupState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePatchGroups  **
  - **IAM action:**  [ssm:DescribePatchGroups](#list_ssm-action-DescribePatchGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribePatchProperties  **
  - **IAM action:**  [ssm:DescribePatchProperties](#list_ssm-action-DescribePatchProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeSessions  **
  - **IAM action:**  [ssm:DescribeSessions](#list_ssm-action-DescribeSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DisassociateOpsItemRelatedItem  **
  - **IAM action:**  [ssm:DisassociateOpsItemRelatedItem](#list_ssm-action-DisassociateOpsItemRelatedItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessToken  **
  - **IAM action:**  [ssm:GetAccessToken](#list_ssm-action-GetAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomationExecution  **
  - **IAM action:**  [ssm:GetAutomationExecution](#list_ssm-action-GetAutomationExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   GetCalendarState  **
  - **IAM action:**  [ssm:GetCalendarState](#list_ssm-action-GetCalendarState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCloudConnector  **
  - **IAM action:**  [ssm:GetCloudConnector](#list_ssm-action-GetCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCommandInvocation  **
  - **IAM action:**  [ssm:GetCommandInvocation](#list_ssm-action-GetCommandInvocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnectionStatus  **
  - **IAM action:**  [ssm:GetConnectionStatus](#list_ssm-action-GetConnectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultPatchBaseline  **
  - **IAM action:**  [ssm:GetDefaultPatchBaseline](#list_ssm-action-GetDefaultPatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployablePatchSnapshotForInstance  **
  - **IAM action:**  [ssm:GetDeployablePatchSnapshotForInstance](#list_ssm-action-GetDeployablePatchSnapshotForInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocument  **
  - **IAM action:**  [ssm:GetDocument](#list_ssm-action-GetDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExecutionPreview  **
  - **IAM action:**  [ssm:GetExecutionPreview](#list_ssm-action-GetExecutionPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInventory  **
  - **IAM action:**  [ssm:GetInventory](#list_ssm-action-GetInventory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInventorySchema  **
  - **IAM action:**  [ssm:GetInventorySchema](#list_ssm-action-GetInventorySchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMaintenanceWindow  **
  - **IAM action:**  [ssm:GetMaintenanceWindow](#list_ssm-action-GetMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMaintenanceWindowExecution  **
  - **IAM action:**  [ssm:GetMaintenanceWindowExecution](#list_ssm-action-GetMaintenanceWindowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMaintenanceWindowExecutionTask  **
  - **IAM action:**  [ssm:GetMaintenanceWindowExecutionTask](#list_ssm-action-GetMaintenanceWindowExecutionTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMaintenanceWindowExecutionTaskInvocation  **
  - **IAM action:**  [ssm:GetMaintenanceWindowExecutionTaskInvocation](#list_ssm-action-GetMaintenanceWindowExecutionTaskInvocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMaintenanceWindowTask  **
  - **IAM action:**  [ssm:GetMaintenanceWindowTask](#list_ssm-action-GetMaintenanceWindowTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpsItem  **
  - **IAM action:**  [ssm:GetOpsItem](#list_ssm-action-GetOpsItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpsMetadata  **
  - **IAM action:**  [ssm:GetOpsMetadata](#list_ssm-action-GetOpsMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpsSummary  **
  - **IAM action:**  [ssm:GetOpsSummary](#list_ssm-action-GetOpsSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParameter  **
  - **IAM action:**  [ssm:GetParameter](#list_ssm-action-GetParameter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParameterHistory  **
  - **IAM action:**  [ssm:GetParameterHistory](#list_ssm-action-GetParameterHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParameters  **
  - **IAM action:**  [ssm:GetParameters](#list_ssm-action-GetParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParametersByPath  **
  - **IAM action:**  [ssm:GetParametersByPath](#list_ssm-action-GetParametersByPath) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPatchBaseline  **
  - **IAM action:**  [ssm:GetPatchBaseline](#list_ssm-action-GetPatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPatchBaselineForPatchGroup  **
  - **IAM action:**  [ssm:GetPatchBaselineForPatchGroup](#list_ssm-action-GetPatchBaselineForPatchGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicies  **
  - **IAM action:**  [ssm:GetResourcePolicies](#list_ssm-action-GetResourcePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetServiceSetting  **
  - **IAM action:**  [ssm:GetServiceSetting](#list_ssm-action-GetServiceSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   LabelParameterVersion  **
  - **IAM action:**  [ssm:LabelParameterVersion](#list_ssm-action-LabelParameterVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAssociationVersions  **
  - **IAM action:**  [ssm:ListAssociationVersions](#list_ssm-action-ListAssociationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociations  **
  - **IAM action:**  [ssm:ListAssociations](#list_ssm-action-ListAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCloudConnectors  **
  - **IAM action:**  [ssm:ListCloudConnectors](#list_ssm-action-ListCloudConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCommandInvocations  **
  - **IAM action:**  [ssm:ListCommandInvocations](#list_ssm-action-ListCommandInvocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCommands  **
  - **IAM action:**  [ssm:ListCommands](#list_ssm-action-ListCommands) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComplianceItems  **
  - **IAM action:**  [ssm:ListComplianceItems](#list_ssm-action-ListComplianceItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComplianceSummaries  **
  - **IAM action:**  [ssm:ListComplianceSummaries](#list_ssm-action-ListComplianceSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDocumentMetadataHistory  **
  - **IAM action:**  [ssm:ListDocumentMetadataHistory](#list_ssm-action-ListDocumentMetadataHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDocumentVersions  **
  - **IAM action:**  [ssm:ListDocumentVersions](#list_ssm-action-ListDocumentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDocuments  **
  - **IAM action:**  [ssm:ListDocuments](#list_ssm-action-ListDocuments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInventoryEntries  **
  - **IAM action:**  [ssm:ListInventoryEntries](#list_ssm-action-ListInventoryEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodes  **
  - **IAM action:**  [ssm:ListNodes](#list_ssm-action-ListNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNodesSummary  **
  - **IAM action:**  [ssm:ListNodesSummary](#list_ssm-action-ListNodesSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpsItemEvents  **
  - **IAM action:**  [ssm:ListOpsItemEvents](#list_ssm-action-ListOpsItemEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpsItemRelatedItems  **
  - **IAM action:**  [ssm:ListOpsItemRelatedItems](#list_ssm-action-ListOpsItemRelatedItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpsMetadata  **
  - **IAM action:**  [ssm:ListOpsMetadata](#list_ssm-action-ListOpsMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceComplianceSummaries  **
  - **IAM action:**  [ssm:ListResourceComplianceSummaries](#list_ssm-action-ListResourceComplianceSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceDataSync  **
  - **IAM action:**  [ssm:ListResourceDataSync](#list_ssm-action-ListResourceDataSync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ssm:ListTagsForResource](#list_ssm-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ModifyDocumentPermission  **
  - **IAM action:**  [ssm:ModifyDocumentPermission](#list_ssm-action-ModifyDocumentPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutComplianceItems  **
  - **IAM action:**  [ssm:PutComplianceItems](#list_ssm-action-PutComplianceItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutInventory  **
  - **IAM action:**  [ssm:PutInventory](#list_ssm-action-PutInventory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutParameter  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:PutParameter](#list_ssm-action-PutParameter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [ssm:PutResourcePolicy](#list_ssm-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RegisterDefaultPatchBaseline  **
  - **IAM action:**  [ssm:RegisterDefaultPatchBaseline](#list_ssm-action-RegisterDefaultPatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterPatchBaselineForPatchGroup  **
  - **IAM action:**  [ssm:RegisterPatchBaselineForPatchGroup](#list_ssm-action-RegisterPatchBaselineForPatchGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterTargetWithMaintenanceWindow  **
  - **IAM action:**  [ssm:RegisterTargetWithMaintenanceWindow](#list_ssm-action-RegisterTargetWithMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterTaskWithMaintenanceWindow  **
  - **IAM action:**  [ssm:RegisterTaskWithMaintenanceWindow](#list_ssm-action-RegisterTaskWithMaintenanceWindow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   RemoveTagsFromResource  **
  - **IAM action:**  [ssm:RemoveTagsFromResource](#list_ssm-action-RemoveTagsFromResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ResetServiceSetting  **
  - **IAM action:**  [ssm:ResetServiceSetting](#list_ssm-action-ResetServiceSetting) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeSession  **
  - **IAM action:**  [ssm:ResumeSession](#list_ssm-action-ResumeSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendAutomationSignal  **
  - **IAM action:**  [ssm:SendAutomationSignal](#list_ssm-action-SendAutomationSignal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendCommand  **
  - **IAM action:**  [ssm:SendCommand](#list_ssm-action-SendCommand)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   StartAccessRequest  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:StartAccessRequest](#list_ssm-action-StartAccessRequest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartAssociationsOnce  **
  - **IAM action:**  [ssm:StartAssociationsOnce](#list_ssm-action-StartAssociationsOnce) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutomationExecution  **
  - **IAM action:**  [ssm:AddTagsToResource](#list_ssm-action-AddTagsToResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [ssm:StartAutomationExecution](#list_ssm-action-StartAutomationExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   StartChangeRequestExecution  **
  - **IAM action:**  [ssm:StartChangeRequestExecution](#list_ssm-action-StartChangeRequestExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   StartExecutionPreview  **
  - **IAM action:**  [ssm:StartExecutionPreview](#list_ssm-action-StartExecutionPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartSession  **
  - **IAM action:**  [ssm:StartSession](#list_ssm-action-StartSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAutomationExecution  **
  - **IAM action:**  [ssm:StopAutomationExecution](#list_ssm-action-StopAutomationExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateSession  **
  - **IAM action:**  [ssm:TerminateSession](#list_ssm-action-TerminateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnlabelParameterVersion  **
  - **IAM action:**  [ssm:UnlabelParameterVersion](#list_ssm-action-UnlabelParameterVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssociation  **
  - **IAM action:**  [ssm:UpdateAssociation](#list_ssm-action-UpdateAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   UpdateAssociationStatus  **
  - **IAM action:**  [ssm:UpdateAssociationStatus](#list_ssm-action-UpdateAssociationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCloudConnector  **
  - **IAM action:**  [ssm:UpdateCloudConnector](#list_ssm-action-UpdateCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDocument  **
  - **IAM action:**  [ssm:UpdateDocument](#list_ssm-action-UpdateDocument)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** justintimeaccess.ssm.amazonaws.com, ssm.amazonaws.com / **Access level:** Write

- **   UpdateDocumentDefaultVersion  **
  - **IAM action:**  [ssm:UpdateDocumentDefaultVersion](#list_ssm-action-UpdateDocumentDefaultVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDocumentMetadata  **
  - **IAM action:**  [ssm:UpdateDocumentMetadata](#list_ssm-action-UpdateDocumentMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMaintenanceWindow  **
  - **IAM action:**  [ssm:UpdateMaintenanceWindow](#list_ssm-action-UpdateMaintenanceWindow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMaintenanceWindowTarget  **
  - **IAM action:**  [ssm:UpdateMaintenanceWindowTarget](#list_ssm-action-UpdateMaintenanceWindowTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMaintenanceWindowTask  **
  - **IAM action:**  [ssm:UpdateMaintenanceWindowTask](#list_ssm-action-UpdateMaintenanceWindowTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   UpdateManagedInstanceRole  **
  - **IAM action:**  [ssm:UpdateManagedInstanceRole](#list_ssm-action-UpdateManagedInstanceRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   UpdateOpsItem  **
  - **IAM action:**  [ssm:UpdateOpsItem](#list_ssm-action-UpdateOpsItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOpsMetadata  **
  - **IAM action:**  [ssm:UpdateOpsMetadata](#list_ssm-action-UpdateOpsMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePatchBaseline  **
  - **IAM action:**  [ssm:UpdatePatchBaseline](#list_ssm-action-UpdatePatchBaseline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceDataSync  **
  - **IAM action:**  [ssm:UpdateResourceDataSync](#list_ssm-action-UpdateResourceDataSync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceSetting  **
  - **IAM action:**  [ssm:UpdateServiceSetting](#list_ssm-action-UpdateServiceSetting)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ssm.amazonaws.com / **Access level:** Write

- **   ValidateCloudConnector  **
  - **IAM action:**  [ssm:ValidateCloudConnector](#list_ssm-action-ValidateCloudConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Systems Manager
<a name="list_ssm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToResource](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AddTagsToResource.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for a specified AWS resource
  - **Resource types (\*required):** [association](#list_ssm-resource-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [automation-execution](#list_ssm-resource-automation-execution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [cloud-connector](#list_ssm-resource-cloud-connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [maintenancewindow](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [opsitem](#list_ssm-resource-opsitem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [opsmetadata](#list_ssm-resource-opsmetadata) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [patchbaseline](#list_ssm-resource-patchbaseline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [task](#list_ssm-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [AssociateOpsItemRelatedItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociateOpsItemRelatedItem.html)  **
  - **Description:** Grants permission to associate RelatedItem to an OpsItem
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelCommand](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CancelCommand.html)  **
  - **Description:** Grants permission to cancel a specified Run Command command
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMaintenanceWindowExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CancelMaintenanceWindowExecution.html)  **
  - **Description:** Grants permission to cancel an in-progress maintenance window execution
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [CreateActivation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateActivation.html)  **
  - **Description:** Grants permission to create an activation that is used to register on-premises servers and virtual machines (VMs) with Systems Manager
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html)  **
  - **Description:** Grants permission to associate a specified Systems Manager document with specified instances or other targets
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [CreateAssociationBatch](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociationBatch.html)  **
  - **Description:** Grants permission to combine entries for multiple CreateAssociation operations in a single command
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [CreateCloudConnector](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateCloudConnector.html)  **
  - **Description:** Grants permission to create a cloud connector for managing instances in other cloud environments
  - **Resource types (\*required):** [cloud-connector\*](#list_ssm-resource-cloud-connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateDocument.html)  **
  - **Description:** Grants permission to create a Systems Manager SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateMaintenanceWindow.html)  **
  - **Description:** Grants permission to create a maintenance window
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOpsItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateOpsItem.html)  **
  - **Description:** Grants permission to create an OpsItem in OpsCenter
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOpsMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateOpsMetadata.html)  **
  - **Description:** Grants permission to create an OpsMetadata object for an AWS resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html)  **
  - **Description:** Grants permission to create a patch baseline
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Write

- **   [CreateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateResourceDataSync.html)  **
  - **Description:** Grants permission to create a resource data sync configuration, which regularly collects inventory data from managed instances and updates the data in an Amazon S3 bucket
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:** [ssm:SyncType](#list_ssm-ssm_SyncType)
  - **Access level:** Write

- **   [DeleteActivation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteActivation.html)  **
  - **Description:** Grants permission to delete a specified activation for managed instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteAssociation.html)  **
  - **Description:** Grants permission to disassociate a specified SSM document from a specified instance
  - **Resource types (\*required):** [association](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeleteCloudConnector](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteCloudConnector.html)  **
  - **Description:** Grants permission to delete a specified cloud connector
  - **Resource types (\*required):** [cloud-connector\*](#list_ssm-resource-cloud-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteDocument.html)  **
  - **Description:** Grants permission to delete a specified SSM document and its instance associations
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInventory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteInventory.html)  **
  - **Description:** Grants permission to delete a specified custom inventory type, or the data associated with a custom inventory type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteMaintenanceWindow.html)  **
  - **Description:** Grants permission to delete a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeleteOpsItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteOpsItem.html)  **
  - **Description:** Grants permission to delete an OpsItem
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOpsMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteOpsMetadata.html)  **
  - **Description:** Grants permission to delete an OpsMetadata object
  - **Resource types (\*required):** [opsmetadata\*](#list_ssm-resource-opsmetadata)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameter.html)  **
  - **Description:** Grants permission to delete a specified SSM parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeleteParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteParameters.html)  **
  - **Description:** Grants permission to delete multiple specified SSM parameters
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeletePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeletePatchBaseline.html)  **
  - **Description:** Grants permission to delete a specified patch baseline
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeleteResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourceDataSync.html)  **
  - **Description:** Grants permission to delete a specified resource data sync
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:** [ssm:SyncType](#list_ssm-ssm_SyncType)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a Systems Manager resource policy
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [opsitemgroup](#list_ssm-resource-opsitemgroup) / **Condition keys:**  
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Permissions management, Write

- **   [DeregisterManagedInstance](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterManagedInstance.html)  **
  - **Description:** Grants permission to deregister a specified on-premises server or virtual machine (VM) from Systems Manager
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeregisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterPatchBaselineForPatchGroup.html)  **
  - **Description:** Grants permission to deregister a specified patch baseline from being the default patch baseline for a specified patch group
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeregisterTargetFromMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterTargetFromMaintenanceWindow.html)  **
  - **Description:** Grants permission to deregister a specified target from a maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [windowtarget\*](#list_ssm-resource-windowtarget) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DeregisterTaskFromMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterTaskFromMaintenanceWindow.html)  **
  - **Description:** Grants permission to deregister a specified task from a maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [windowtask\*](#list_ssm-resource-windowtask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [DescribeActivations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeActivations.html)  **
  - **Description:** Grants permission to view details about a specified managed instance activation, such as when it was created and the number of instances registered using the activation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociation.html)  **
  - **Description:** Grants permission to view details about the specified association for a specified instance or target
  - **Resource types (\*required):** [association](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutionTargets.html)  **
  - **Description:** Grants permission to view information about a specified association execution
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAssociationExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAssociationExecutions.html)  **
  - **Description:** Grants permission to view all executions for a specified association
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAutomationExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationExecutions.html)  **
  - **Description:** Grants permission to view details about all active and terminated Automation executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationStepExecutions.html)  **
  - **Description:** Grants permission to view information about all active and terminated step executions in an Automation workflow
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeAvailablePatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAvailablePatches.html)  **
  - **Description:** Grants permission to view all patches eligible to include in a patch baseline
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeDocument.html)  **
  - **Description:** Grants permission to view details about a specified SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDocumentParameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to display information about SSM document parameters in the Systems Manager console (internal Systems Manager action)
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDocumentPermission](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeDocumentPermission.html)  **
  - **Description:** Grants permission to view the permissions for a specified SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEffectiveInstanceAssociations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeEffectiveInstanceAssociations.html)  **
  - **Description:** Grants permission to view all current associations for a specified instance
  - **Resource types (\*required):** [instance\*](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeEffectivePatchesForPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeEffectivePatchesForPatchBaseline.html)  **
  - **Description:** Grants permission to view details about the patches currently associated with the specified patch baseline (Windows only)
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeInstanceAssociationsStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceAssociationsStatus.html)  **
  - **Description:** Grants permission to view the status of the associations for a specified instance
  - **Resource types (\*required):** [instance\*](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceInformation.html)  **
  - **Description:** Grants permission to view details about a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInstancePatchStates](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatchStates.html)  **
  - **Description:** Grants permission to view status details about patches on a specified instance
  - **Resource types (\*required):** [instance\*](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeInstancePatchStatesForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatchStatesForPatchGroup.html)  **
  - **Description:** Grants permission to describe the high-level patch state for the instances in the specified patch group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInstancePatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatches.html)  **
  - **Description:** Grants permission to view general details about the patches on a specified instance
  - **Resource types (\*required):** [instance\*](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [DescribeInstanceProperties](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to user's Amazon EC2 console to render managed instances' nodes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeInventoryDeletions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInventoryDeletions.html)  **
  - **Description:** Grants permission to view details about a specified inventory deletion
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMaintenanceWindowExecutionTaskInvocations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutionTaskInvocations.html)  **
  - **Description:** Grants permission to view details of a specified task execution for a maintenance window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMaintenanceWindowExecutionTasks](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutionTasks.html)  **
  - **Description:** Grants permission to view details about the tasks that ran during a specified maintenance window execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMaintenanceWindowExecutions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutions.html)  **
  - **Description:** Grants permission to view the executions of a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [DescribeMaintenanceWindowSchedule](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowSchedule.html)  **
  - **Description:** Grants permission to view details about upcoming executions of a specified maintenance window
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMaintenanceWindowTargets](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowTargets.html)  **
  - **Description:** Grants permission to view a list of the targets associated with a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [DescribeMaintenanceWindowTasks](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowTasks.html)  **
  - **Description:** Grants permission to view a list of the tasks associated with a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [DescribeMaintenanceWindows](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindows.html)  **
  - **Description:** Grants permission to view information about all or specified maintenance windows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMaintenanceWindowsForTarget](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowsForTarget.html)  **
  - **Description:** Grants permission to view information about the maintenance window targets and tasks associated with a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOpsItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeOpsItems.html)  **
  - **Description:** Grants permission to view details about specified OpsItems
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html)  **
  - **Description:** Grants permission to view details about a specified SSM parameter
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePatchBaselines](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchBaselines.html)  **
  - **Description:** Grants permission to view information about patch baselines that meet the specified criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePatchGroupState](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchGroupState.html)  **
  - **Description:** Grants permission to view aggregated status details for patches for a specified patch group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePatchGroups](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchGroups.html)  **
  - **Description:** Grants permission to view information about the patch baseline for a specified patch group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePatchProperties](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html)  **
  - **Description:** Grants permission to view details of available patches for a specified operating system and patch property
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeSessions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeSessions.html)  **
  - **Description:** Grants permission to view a list of recent Session Manager sessions that meet the specified search criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DisassociateOpsItemRelatedItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DisassociateOpsItemRelatedItem.html)  **
  - **Description:** Grants permission to disassociate RelatedItem from an OpsItem
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecuteAPI](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html#systems-manager-namespace-other-API-operations)  **
  - **Description:** Grants permission to a Systems Manager delegated administrator to view related resource details about OpsItems across multiple AWS accounts in the AWS Management Console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccessToken](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetAccessToken.html)  **
  - **Description:** Grants permission to return a credentials set to be used with just-in-time node access
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecution.html)  **
  - **Description:** Grants permission to view details of a specified Automation execution
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetCalendarState](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCalendarState.html)  **
  - **Description:** Grants permission to view the calendar state for a change calendar or a list of change calendars
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCloudConnector](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCloudConnector.html)  **
  - **Description:** Grants permission to view details about a specified cloud connector
  - **Resource types (\*required):** [cloud-connector\*](#list_ssm-resource-cloud-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCommandInvocation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetCommandInvocation.html)  **
  - **Description:** Grants permission to view details about the command execution of a specified invocation or plugin
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnectionStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetConnectionStatus.html)  **
  - **Description:** Grants permission to view the Session Manager connection status for a specified managed instance
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [task](#list_ssm-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDefaultPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDefaultPatchBaseline.html)  **
  - **Description:** Grants permission to view the current default patch baseline for a specified operating system type
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetDeployablePatchSnapshotForInstance](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDeployablePatchSnapshotForInstance.html)  **
  - **Description:** Grants permission to retrieve the current patch baseline snapshot for a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDocument.html)  **
  - **Description:** Grants permission to view the contents of a specified SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExecutionPreview](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetExecutionPreview.html)  **
  - **Description:** Grants permission to retrieve an existing preview that shows the effects that running a specified Automation runbook would have on the targeted resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInventory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetInventory.html)  **
  - **Description:** Grants permission to view instance inventory details per the specified criteria
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInventorySchema](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetInventorySchema.html)  **
  - **Description:** Grants permission to view a list of inventory types or attribute names for a specified inventory item type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindow.html)  **
  - **Description:** Grants permission to view details about a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetMaintenanceWindowExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecution.html)  **
  - **Description:** Grants permission to view details about a specified maintenance window execution
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMaintenanceWindowExecutionTask](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecutionTask.html)  **
  - **Description:** Grants permission to view details about a specified maintenance window execution task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMaintenanceWindowExecutionTaskInvocation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowExecutionTaskInvocation.html)  **
  - **Description:** Grants permission to view details about a specific maintenance window task running on a specific target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMaintenanceWindowTask](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetMaintenanceWindowTask.html)  **
  - **Description:** Grants permission to view details about tasks registered with a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetOpsItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsItem.html)  **
  - **Description:** Grants permission to view information about a specified OpsItem
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOpsMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsMetadata.html)  **
  - **Description:** Grants permission to retrieve an OpsMetadata object
  - **Resource types (\*required):** [opsmetadata\*](#list_ssm-resource-opsmetadata)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOpsSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsSummary.html)  **
  - **Description:** Grants permission to view summary information about OpsItems based on specified filters and aggregators
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html)  **
  - **Description:** Grants permission to view information about a specified parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameterHistory.html)  **
  - **Description:** Grants permission to view details and changes for a specified parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html)  **
  - **Description:** Grants permission to view information about multiple specified parameters
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetParametersByPath](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParametersByPath.html)  **
  - **Description:** Grants permission to view information about parameters in a specified hierarchy
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:Recursive](#list_ssm-ssm_Recursive)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetPatchBaseline.html)  **
  - **Description:** Grants permission to view information about a specified patch baseline
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Read

- **   [GetPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetPatchBaselineForPatchGroup.html)  **
  - **Description:** Grants permission to view the ID of the current patch baseline for a specified patch group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicies](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetResourcePolicies.html)  **
  - **Description:** Grants permission to retrieve lists of Systems Manager resource policies
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [opsitemgroup](#list_ssm-resource-opsitemgroup) / **Condition keys:**  
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [GetServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetServiceSetting.html)  **
  - **Description:** Grants permission to view the account-level setting for an AWS service
  - **Resource types (\*required):** [servicesetting\*](#list_ssm-resource-servicesetting)
  - **Condition keys:**  
  - **Access level:** Read

- **   [LabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_LabelParameterVersion.html)  **
  - **Description:** Grants permission to apply an identifying label to a specified version of a parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [ListAssociationVersions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociationVersions.html)  **
  - **Description:** Grants permission to list versions of the specified association
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListAssociations.html)  **
  - **Description:** Grants permission to list the associations for a specified SSM document or managed instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCloudConnectors](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCloudConnectors.html)  **
  - **Description:** Grants permission to list cloud connectors in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCommandInvocations](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCommandInvocations.html)  **
  - **Description:** Grants permission to list information about command invocations sent to a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCommands](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListCommands.html)  **
  - **Description:** Grants permission to list the commands sent to a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListComplianceItems.html)  **
  - **Description:** Grants permission to list compliance status for specified resource types on a specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComplianceSummaries](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListComplianceSummaries.html)  **
  - **Description:** Grants permission to list a summary count of compliant and noncompliant resources for a specified compliance type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDocumentMetadataHistory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocumentMetadataHistory.html)  **
  - **Description:** Grants permission to view metadata history about a specified SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** List

- **   [ListDocumentVersions](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocumentVersions.html)  **
  - **Description:** Grants permission to list all versions of a specified document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** List

- **   [ListDocuments](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocuments.html)  **
  - **Description:** Grants permission to view information about a specified SSM document
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstanceAssociations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to check for new State Manager associations (internal Systems Manager call)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [ListInventoryEntries](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListInventoryEntries.html)  **
  - **Description:** Grants permission to view a list of specified inventory types for a specified instance
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodes](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListNodes.html)  **
  - **Description:** Grants permission to view details about managed nodes based on specified filters
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNodesSummary](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListNodesSummary.html)  **
  - **Description:** Grants permission to view summary information about managed nodes based on specified filters and aggregators
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOpsItemEvents](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsItemEvents.html)  **
  - **Description:** Grants permission to view details about OpsItemEvents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOpsItemRelatedItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsItemRelatedItems.html)  **
  - **Description:** Grants permission to view details about OpsItem RelatedItems
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOpsMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListOpsMetadata.html)  **
  - **Description:** Grants permission to view a list of OpsMetadata objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceComplianceSummaries](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceComplianceSummaries.html)  **
  - **Description:** Grants permission to list resource-level summary count
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListResourceDataSync.html)  **
  - **Description:** Grants permission to list information about resource data sync configurations in an account
  - **Resource types (\*required):** 
  - **Condition keys:** [ssm:SyncType](#list_ssm-ssm_SyncType)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view a list of resource tags for a specified resource
  - **Resource types (\*required):** [association](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automation-execution](#list_ssm-resource-automation-execution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [cloud-connector](#list_ssm-resource-cloud-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [maintenancewindow](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [opsitem](#list_ssm-resource-opsitem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [opsmetadata](#list_ssm-resource-opsmetadata) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [patchbaseline](#list_ssm-resource-patchbaseline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** List

- **   [ModifyDocumentPermission](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ModifyDocumentPermission.html)  **
  - **Description:** Grants permission to share a custom SSM document publicly or privately with specified AWS accounts
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutComplianceItems.html)  **
  - **Description:** Grants permission to register a compliance type and other compliance details on a specified resource
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Access level:** Write

- **   [PutInventory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutInventory.html)  **
  - **Description:** Grants permission to add or update inventory items on multiple specified managed instances
  - **Resource types (\*required):** 
  - **Condition keys:** [ssm:InventoryTypeName](#list_ssm-ssm_InventoryTypeName)
  - **Access level:** Write

- **   [PutParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html)  **
  - **Description:** Grants permission to create an SSM parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:Overwrite](#list_ssm-ssm_Overwrite)<br />[ssm:Policies](#list_ssm-ssm_Policies)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update a Systems Manager resource policy
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [opsitemgroup](#list_ssm-resource-opsitemgroup) / **Condition keys:**  
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Permissions management, Write

- **   [RegisterDefaultPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterDefaultPatchBaseline.html)  **
  - **Description:** Grants permission to specify the default patch baseline for an operating system type
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [RegisterManagedInstance](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to register a Systems Manager Agent
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:NodeAccountId](#list_ssm-ssm_NodeAccountId)<br />[ssm:NodeOrgId](#list_ssm-ssm_NodeOrgId)
  - **Access level:** Write

- **   [RegisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterPatchBaselineForPatchGroup.html)  **
  - **Description:** Grants permission to specify the default patch baseline for a specified patch group
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [RegisterTargetWithMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTargetWithMaintenanceWindow.html)  **
  - **Description:** Grants permission to register a target with a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [RegisterTaskWithMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTaskWithMaintenanceWindow.html)  **
  - **Description:** Grants permission to register a task with a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [RemoveTagsFromResource](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RemoveTagsFromResource.html)  **
  - **Description:** Grants permission to remove a specified tag key from a specified resource
  - **Resource types (\*required):** [association](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [automation-execution](#list_ssm-resource-automation-execution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [cloud-connector](#list_ssm-resource-cloud-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [maintenancewindow](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [opsitem](#list_ssm-resource-opsitem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Resource types (\*required):** [opsmetadata](#list_ssm-resource-opsmetadata) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [parameter](#list_ssm-resource-parameter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [patchbaseline](#list_ssm-resource-patchbaseline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [task](#list_ssm-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ResetServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResetServiceSetting.html)  **
  - **Description:** Grants permission to reset the service setting for an AWS account to the default value
  - **Resource types (\*required):** [servicesetting\*](#list_ssm-resource-servicesetting)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResumeSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResumeSession.html)  **
  - **Description:** Grants permission to reconnect a Session Manager session to a managed instance
  - **Resource types (\*required):** [session\*](#list_ssm-resource-session)
  - **Condition keys:** [ssm:resourceTag/aws:ssmmessages:session-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_session-id)<br />[ssm:resourceTag/aws:ssmmessages:target-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_target-id)
  - **Access level:** Write

- **   [SendAutomationSignal](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendAutomationSignal.html)  **
  - **Description:** Grants permission to send a signal to change the current behavior or status of a specified Automation execution
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [SendCommand](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html)  **
  - **Description:** Grants permission to run commands on one or more specified managed instances
  - **Resource types (\*required):** [bucket](#list_ssm-resource-bucket) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [StartAccessRequest](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAccessRequest.html)  **
  - **Description:** Grants permission to start the workflow for just-in-time node access sessions
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [StartAssociationsOnce](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAssociationsOnce.html)  **
  - **Description:** Grants permission to run a specified association manually
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAutomationExecution.html)  **
  - **Description:** Grants permission to initiate the execution of an Automation document
  - **Resource types (\*required):** [automation-definition](#list_ssm-resource-automation-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [StartChangeRequestExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartChangeRequestExecution.html)  **
  - **Description:** Grants permission to initiate the execution of an Automation Change Template document
  - **Resource types (\*required):** [automation-definition](#list_ssm-resource-automation-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:AutoApprove](#list_ssm-ssm_AutoApprove)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:AutoApprove](#list_ssm-ssm_AutoApprove)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-aws_TagKeys)<br />[ssm:AutoApprove](#list_ssm-ssm_AutoApprove)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:DocumentVersion](#list_ssm-ssm_DocumentVersion)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [StartExecutionPreview](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartExecutionPreview.html)  **
  - **Description:** Grants permission to create a preview showing the effects that running a specified Automation runbook would have on the targeted resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html)  **
  - **Description:** Grants permission to initiate a connection to a specified target for a Session Manager session
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:AccessRequestId](#list_ssm-ssm_AccessRequestId)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SessionDocumentAccessCheck](#list_ssm-ssm_SessionDocumentAccessCheck)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:AccessRequestId](#list_ssm-ssm_AccessRequestId)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SessionDocumentAccessCheck](#list_ssm-ssm_SessionDocumentAccessCheck)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:AccessRequestId](#list_ssm-ssm_AccessRequestId)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)<br />[ssm:SessionDocumentAccessCheck](#list_ssm-ssm_SessionDocumentAccessCheck)
  - **Resource types (\*required):** [task](#list_ssm-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:AccessRequestId](#list_ssm-ssm_AccessRequestId)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SessionDocumentAccessCheck](#list_ssm-ssm_SessionDocumentAccessCheck)
  - **Access level:** Write

- **   [StopAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StopAutomationExecution.html)  **
  - **Description:** Grants permission to stop a specified Automation execution that is already in progress
  - **Resource types (\*required):** [automation-execution\*](#list_ssm-resource-automation-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [TerminateSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_TerminateSession.html)  **
  - **Description:** Grants permission to permanently end a Session Manager connection to an instance
  - **Resource types (\*required):** [session\*](#list_ssm-resource-session)
  - **Condition keys:** [ssm:resourceTag/aws:ssmmessages:session-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_session-id)<br />[ssm:resourceTag/aws:ssmmessages:target-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_target-id)
  - **Access level:** Write

- **   [UnlabelParameterVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UnlabelParameterVersion.html)  **
  - **Description:** Grants permission to remove an identifying label from a specified version of a parameter
  - **Resource types (\*required):** [parameter\*](#list_ssm-resource-parameter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociation.html)  **
  - **Description:** Grants permission to update an association and immediately run the association on the specified targets
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateAssociationStatus](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociationStatus.html)  **
  - **Description:** Grants permission to update the status of the SSM document associated with a specified instance
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Access level:** Write

- **   [UpdateCloudConnector](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateCloudConnector.html)  **
  - **Description:** Grants permission to update a specified cloud connector
  - **Resource types (\*required):** [cloud-connector\*](#list_ssm-resource-cloud-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocument.html)  **
  - **Description:** Grants permission to update one or more values for an SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocumentDefaultVersion.html)  **
  - **Description:** Grants permission to change the default version of an SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDocumentMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocumentMetadata.html)  **
  - **Description:** Grants permission to update the metadata of an SSM document
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to send a heartbeat signal to the Systems Manager service in the cloud
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Access level:** Write

- **   [UpdateMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindow.html)  **
  - **Description:** Grants permission to update a specified maintenance window
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateMaintenanceWindowTarget](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindowTarget.html)  **
  - **Description:** Grants permission to update a specified maintenance window target
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [windowtarget\*](#list_ssm-resource-windowtarget) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateMaintenanceWindowTask](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindowTask.html)  **
  - **Description:** Grants permission to update a specified maintenance window task
  - **Resource types (\*required):** [maintenancewindow\*](#list_ssm-resource-maintenancewindow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [windowtask\*](#list_ssm-resource-windowtask) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateManagedInstanceRole](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateManagedInstanceRole.html)  **
  - **Description:** Grants permission to assign or change the IAM role assigned to a specified managed instance
  - **Resource types (\*required):** [iam-role\*](#list_ssm-resource-iam-role) / **Condition keys:** [ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Resource types (\*required):** [managed-instance\*](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateOpsItem](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateOpsItem.html)  **
  - **Description:** Grants permission to edit or change an OpsItem
  - **Resource types (\*required):** [opsitem\*](#list_ssm-resource-opsitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOpsMetadata](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateOpsMetadata.html)  **
  - **Description:** Grants permission to update an OpsMetadata object
  - **Resource types (\*required):** [opsmetadata\*](#list_ssm-resource-opsmetadata)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdatePatchBaseline.html)  **
  - **Description:** Grants permission to update a specified patch baseline
  - **Resource types (\*required):** [patchbaseline\*](#list_ssm-resource-patchbaseline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateResourceDataSync](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateResourceDataSync.html)  **
  - **Description:** Grants permission to update a resource data sync
  - **Resource types (\*required):** [resourcedatasync\*](#list_ssm-resource-resourcedatasync)
  - **Condition keys:** [ssm:SyncType](#list_ssm-ssm_SyncType)
  - **Access level:** Write

- **   [UpdateServiceSetting](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateServiceSetting.html)  **
  - **Description:** Grants permission to update the service setting for an AWS account
  - **Resource types (\*required):** [servicesetting\*](#list_ssm-resource-servicesetting)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ValidateCloudConnector](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ValidateCloudConnector.html)  **
  - **Description:** Grants permission to verify that a specified cloud connector is functioning properly and to retrieve any validation findings or issues detected
  - **Resource types (\*required):** [cloud-connector\*](#list_ssm-resource-cloud-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Permission-only actions for AWS Systems Manager
<a name="list_ssm-permission-only-actions"></a>

The following actions are defined by AWS Systems Manager but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetCalendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-prereqs.html)  **
  - **Description:** Grants permission to view details of a specific calendar
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManifest](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to Systems Manager and SSM Agent to determine package installation requirements for an instance (internal Systems Manager call)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutCalendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-prereqs.html)  **
  - **Description:** Grants permission to create/edit a specific calendar
  - **Resource types (\*required):** [document\*](#list_ssm-resource-document)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Access level:** Write

- **   [PutConfigurePackageResult](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to generate a report of the results of specific agent requests (internal Systems Manager call)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RequestManagedInstanceRoleToken](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to retrieve temporary credentials to access the managed node (internal Systems Manager call)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:NodeAccountId](#list_ssm-ssm_NodeAccountId)<br />[ssm:NodeOrgId](#list_ssm-ssm_NodeOrgId)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:NodeAccountId](#list_ssm-ssm_NodeAccountId)<br />[ssm:NodeOrgId](#list_ssm-ssm_NodeOrgId)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write

- **   [UpdateInstanceAssociationStatus](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to update the status of the association that it is currently running (internal Systems Manager call)
  - **Resource types (\*required):** [association\*](#list_ssm-resource-association) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ec2:SourceInstanceARN](#list_ssm-ec2_SourceInstanceARN)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)<br />[ssm:SourceInstanceARN](#list_ssm-ssm_SourceInstanceARN)
  - **Access level:** Write

- **   [UpdateManagedInstancePublicKey](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  **
  - **Description:** Grants permission to SSM Agent to update the public key of the managed node after rotating the key pair (internal Systems Manager call)
  - **Resource types (\*required):** [instance](#list_ssm-resource-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:NodeAccountId](#list_ssm-ssm_NodeAccountId)<br />[ssm:NodeOrgId](#list_ssm-ssm_NodeOrgId)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_)
  - **Resource types (\*required):** [managed-instance](#list_ssm-resource-managed-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:NodeAccountId](#list_ssm-ssm_NodeAccountId)<br />[ssm:NodeOrgId](#list_ssm-ssm_NodeOrgId)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key)
  - **Access level:** Write



## Resource types defined by AWS Systems Manager
<a name="list_ssm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [association](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:association/${AssociationId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_) | 
|  [automation-definition](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html)  | arn:${Partition}:ssm:${Region}:${Account}:automation-definition/${AutomationDefinitionName}:${VersionId} | [ssm:DocumentType](#list_ssm-ssm_DocumentType) | 
|  [automation-execution](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-simple-automations.html)  | arn:${Partition}:ssm:${Region}:${Account}:automation-execution/${AutomationExecutionId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html)  | arn:${Partition}:s3:::${BucketName} |   | 
|  [cloud-connector](https://docs.aws.amazon.com/systems-manager/latest/userguide/cloud-connectors.html)  | arn:${Partition}:ssm:${Region}:${Account}:cloud-connector/${CloudConnectorId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_) | 
|  [document](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html)  | arn:${Partition}:ssm:${Region}:${Account}:document/${DocumentName} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:DocumentCategories](#list_ssm-ssm_DocumentCategories)<br />[ssm:DocumentType](#list_ssm-ssm_DocumentType)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_) | 
|  [iam-role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)  | arn:${Partition}:iam::${Account}:role/${RoleName} |   | 
|  [instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#EC2_ARN_Format)  | arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_) | 
|  [maintenancewindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html)  | arn:${Partition}:ssm:${Region}:${Account}:maintenancewindow/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [managed-instance](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:managed-instance/${InstanceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [managed-instance-inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html)  | arn:${Partition}:ssm:${Region}:${Account}:managed-instance-inventory/${InstanceId} |   | 
|  [opsitem](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)  | arn:${Partition}:ssm:${Region}:${Account}:opsitem/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_) | 
|  [opsitemgroup](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)  | arn:${Partition}:ssm:${Region}:${Account}:opsitemgroup/default |   | 
|  [opsmetadata](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:opsmetadata/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/${TagKey}](#list_ssm-ssm_resourceTag___TagKey_) | 
|  [parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)  | arn:${Partition}:ssm:${Region}:${Account}:parameter/${ParameterNameWithoutLeadingSlash} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [patchbaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:patchbaseline/${PatchBaselineIdResourceId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [resourcedatasync](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-datasync.html)  | arn:${Partition}:ssm:${Region}:${Account}:resource-data-sync/${SyncName} |   | 
|  [servicesetting](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:servicesetting/${ResourceId} |   | 
|  [session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)  | arn:${Partition}:ssm:${Region}:${Account}:session/${SessionId} | [ssm:resourceTag/aws:ssmmessages:session-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_session-id)<br />[ssm:resourceTag/aws:ssmmessages:target-id](#list_ssm-ssm_resourceTag_aws_ssmmessages_target-id) | 
|  [task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)  | arn:${Partition}:ecs:${Region}:${Account}:task/${TaskId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_) | 
|  [windowtarget](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-targets.html)  | arn:${Partition}:ssm:${Region}:${Account}:windowtarget/${WindowTargetId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 
|  [windowtask](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-tasks.html)  | arn:${Partition}:ssm:${Region}:${Account}:windowtask/${WindowTaskId} | [aws:ResourceTag/${TagKey}](#list_ssm-aws_ResourceTag___TagKey_)<br />[ssm:resourceTag/tag-key](#list_ssm-ssm_resourceTag_tag-key) | 

## Condition keys for AWS Systems Manager
<a name="list_ssm-policy-keys"></a>

AWS Systems Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by 'Create' requests based on the allowed set of values for a specified tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by based on a tag key-value pair assigned to the AWS resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by 'Create' requests based on whether mandatory tags are included in the request | ArrayOfString | 
|   [ec2:SourceInstanceARN](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys)  | Filters access by the ARN of the instance from which the request originated | ARN | 
|   [ssm:AccessRequestId](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user has access to the access request ID specified in the request | String | 
|   [ssm:AutoApprove](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-auto-approval-access.html)  | Filters access by verifying that a user has permission to start Change Manager workflows without a review step (with the exception of change freeze events) | Bool | 
|   [ssm:DocumentCategories](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user has permission to access a document belonging to a specific category enum | ArrayOfString | 
|   [ssm:DocumentType](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user has permission to access a document belonging to a specific document type. Only available in "aws", "aws-cn", and "aws-us-gov" partitions | String | 
|   [ssm:DocumentVersion](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user has permission to access a specific version of a document | ArrayOfString | 
|   [ssm:InventoryTypeName](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user also has access to the InventoryType specified in the request | ArrayOfString | 
|   [ssm:NodeAccountId](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by the AWS account ID associated with the managed node making the request. Available only in VPC endpoint policies and service control policies (SCPs) | String | 
|   [ssm:NodeOrgId](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by the AWS Organizations ID associated with the managed node making the request. Available only in VPC endpoint policies and service control policies (SCPs) | String | 
|   [ssm:Overwrite](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policy-conditions.html#overwrite-condition)  | Filters access by controling whether Systems Manager parameters can be overwritten | String | 
|   [ssm:Policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policy-conditions.html#parameter-policies-condition)  | Filters access by controlling whether an IAM Entity (user or role) can create or update a parameter that includes a parameter policy | String | 
|   [ssm:Recursive](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policy-conditions.html#recursive-condition)  | Filters access by Systems Manager parameters created in a hierarchical structure | String | 
|   [ssm:SessionDocumentAccessCheck](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-sessiondocumentaccesscheck.html)  | Filters access by verifying that a user has permission to access either the default Session Manager configuration document or the custom configuration document specified in a request | Bool | 
|   [ssm:SourceInstanceARN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html#awssystemsmanager-policy-keys)  | Filters access by verifying the Amazon Resource Name (ARN) of the AWS Systems Manager's managed instance from which the request is made. This key is not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile | ARN | 
|   [ssm:SyncType](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by verifying that a user also has access to the ResourceDataSync SyncType specified in the request | String | 
|   [ssm:resourceTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#policy-conditions)  | Filters access by a tag key-value pair assigned to the Systems Manager resource | String | 
|   [ssm:resourceTag/aws:ssmmessages:session-id](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by based on a tag key-value pair assigned to the Systems Manager session resource | String | 
|   [ssm:resourceTag/aws:ssmmessages:target-id](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by based on a tag key-value pair assigned to the Systems Manager session resource | String | 
|   [ssm:resourceTag/tag-key](https://docs.aws.amazon.com/systems-manager/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#policy-conditions)  | Filters access by based on a tag key-value pair assigned to the Systems Manager resource | String | 