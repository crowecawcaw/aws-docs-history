

# Actions, resources, and condition keys for AWS CloudFormation
<a name="list_cloudformation"></a>

AWS CloudFormation (service prefix: `cloudformation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudformation/cloudformation.json) for this service.

**Topics**
+ [API operations defined by AWS CloudFormation](#list_cloudformation-operations)
+ [Actions defined by AWS CloudFormation](#list_cloudformation-actions-as-permissions)
+ [Permission-only actions for AWS CloudFormation](#list_cloudformation-permission-only-actions)
+ [Resource types defined by AWS CloudFormation](#list_cloudformation-resources-for-iam-policies)
+ [Condition keys for AWS CloudFormation](#list_cloudformation-policy-keys)

## API operations defined by AWS CloudFormation
<a name="list_cloudformation-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudformation-actions-as-permissions).




- **   ActivateOrganizationsAccess  **
  - **IAM action:**  [cloudformation:ActivateOrganizationsAccess](#list_cloudformation-action-ActivateOrganizationsAccess)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ActivateType  **
  - **IAM action:**  [cloudformation:ActivateType](#list_cloudformation-action-ActivateType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resources.cloudformation.amazonaws.com / **Access level:** Write

- **   BatchDescribeTypeConfigurations  **
  - **IAM action:**  [cloudformation:BatchDescribeTypeConfigurations](#list_cloudformation-action-BatchDescribeTypeConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelUpdateStack  **
  - **IAM action:**  [cloudformation:CancelUpdateStack](#list_cloudformation-action-CancelUpdateStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ContinueUpdateRollback  **
  - **IAM action:**  [cloudformation:ContinueUpdateRollback](#list_cloudformation-action-ContinueUpdateRollback)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   CreateChangeSet  **
  - **IAM action:**  [cloudformation:CreateChangeSet](#list_cloudformation-action-CreateChangeSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UntagResource](#list_cloudformation-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   CreateGeneratedTemplate  **
  - **IAM action:**  [cloudformation:CreateGeneratedTemplate](#list_cloudformation-action-CreateGeneratedTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStack  **
  - **IAM action:**  [cloudformation:CreateStack](#list_cloudformation-action-CreateStack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   CreateStackInstances  **
  - **IAM action:**  [cloudformation:CreateStackInstances](#list_cloudformation-action-CreateStackInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStackRefactor  **
  - **IAM action:**  [cloudformation:CreateStackRefactor](#list_cloudformation-action-CreateStackRefactor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStackSet  **
  - **IAM action:**  [cloudformation:CreateStackSet](#list_cloudformation-action-CreateStackSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   DeactivateOrganizationsAccess  **
  - **IAM action:**  [cloudformation:DeactivateOrganizationsAccess](#list_cloudformation-action-DeactivateOrganizationsAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeactivateType  **
  - **IAM action:**  [cloudformation:DeactivateType](#list_cloudformation-action-DeactivateType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteChangeSet  **
  - **IAM action:**  [cloudformation:DeleteChangeSet](#list_cloudformation-action-DeleteChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGeneratedTemplate  **
  - **IAM action:**  [cloudformation:DeleteGeneratedTemplate](#list_cloudformation-action-DeleteGeneratedTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStack  **
  - **IAM action:**  [cloudformation:DeleteStack](#list_cloudformation-action-DeleteStack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   DeleteStackInstances  **
  - **IAM action:**  [cloudformation:DeleteStackInstances](#list_cloudformation-action-DeleteStackInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStackSet  **
  - **IAM action:**  [cloudformation:DeleteStackSet](#list_cloudformation-action-DeleteStackSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterType  **
  - **IAM action:**  [cloudformation:DeregisterType](#list_cloudformation-action-DeregisterType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAccountLimits  **
  - **IAM action:**  [cloudformation:DescribeAccountLimits](#list_cloudformation-action-DescribeAccountLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChangeSet  **
  - **IAM action:**  [cloudformation:DescribeChangeSet](#list_cloudformation-action-DescribeChangeSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeChangeSetHooks  **
  - **IAM action:**  [cloudformation:DescribeChangeSetHooks](#list_cloudformation-action-DescribeChangeSetHooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEvents  **
  - **IAM action:**  [cloudformation:DescribeEvents](#list_cloudformation-action-DescribeEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeGeneratedTemplate  **
  - **IAM action:**  [cloudformation:DescribeGeneratedTemplate](#list_cloudformation-action-DescribeGeneratedTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationsAccess  **
  - **IAM action:**  [cloudformation:DescribeOrganizationsAccess](#list_cloudformation-action-DescribeOrganizationsAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePublisher  **
  - **IAM action:**  [cloudformation:DescribePublisher](#list_cloudformation-action-DescribePublisher) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourceScan  **
  - **IAM action:**  [cloudformation:DescribeResourceScan](#list_cloudformation-action-DescribeResourceScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackDriftDetectionStatus  **
  - **IAM action:**  [cloudformation:DescribeStackDriftDetectionStatus](#list_cloudformation-action-DescribeStackDriftDetectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackEvents  **
  - **IAM action:**  [cloudformation:DescribeStackEvents](#list_cloudformation-action-DescribeStackEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackInstance  **
  - **IAM action:**  [cloudformation:DescribeStackInstance](#list_cloudformation-action-DescribeStackInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackRefactor  **
  - **IAM action:**  [cloudformation:DescribeStackRefactor](#list_cloudformation-action-DescribeStackRefactor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackResource  **
  - **IAM action:**  [cloudformation:DescribeStackResource](#list_cloudformation-action-DescribeStackResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackResourceDrifts  **
  - **IAM action:**  [cloudformation:DescribeStackResourceDrifts](#list_cloudformation-action-DescribeStackResourceDrifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackResources  **
  - **IAM action:**  [cloudformation:DescribeStackResources](#list_cloudformation-action-DescribeStackResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackSet  **
  - **IAM action:**  [cloudformation:DescribeStackSet](#list_cloudformation-action-DescribeStackSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStackSetOperation  **
  - **IAM action:**  [cloudformation:DescribeStackSetOperation](#list_cloudformation-action-DescribeStackSetOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStacks  **
  - **IAM action:**  [cloudformation:DescribeStacks](#list_cloudformation-action-DescribeStacks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [cloudformation:ListStacks](#list_cloudformation-action-ListStacks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeType  **
  - **IAM action:**  [cloudformation:DescribeType](#list_cloudformation-action-DescribeType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTypeRegistration  **
  - **IAM action:**  [cloudformation:DescribeTypeRegistration](#list_cloudformation-action-DescribeTypeRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectStackDrift  **
  - **IAM action:**  [cloudformation:DetectStackDrift](#list_cloudformation-action-DetectStackDrift)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cloudformation:DetectStackResourceDrift](#list_cloudformation-action-DetectStackResourceDrift)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DetectStackResourceDrift  **
  - **IAM action:**  [cloudformation:DetectStackResourceDrift](#list_cloudformation-action-DetectStackResourceDrift) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectStackSetDrift  **
  - **IAM action:**  [cloudformation:DetectStackSetDrift](#list_cloudformation-action-DetectStackSetDrift) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   EstimateTemplateCost  **
  - **IAM action:**  [cloudformation:EstimateTemplateCost](#list_cloudformation-action-EstimateTemplateCost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExecuteChangeSet  **
  - **IAM action:**  [cloudformation:ExecuteChangeSet](#list_cloudformation-action-ExecuteChangeSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UntagResource](#list_cloudformation-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ExecuteStackRefactor  **
  - **IAM action:**  [cloudformation:ExecuteStackRefactor](#list_cloudformation-action-ExecuteStackRefactor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetGeneratedTemplate  **
  - **IAM action:**  [cloudformation:GetGeneratedTemplate](#list_cloudformation-action-GetGeneratedTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHookResult  **
  - **IAM action:**  [cloudformation:GetHookResult](#list_cloudformation-action-GetHookResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStackPolicy  **
  - **IAM action:**  [cloudformation:GetStackPolicy](#list_cloudformation-action-GetStackPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplate  **
  - **IAM action:**  [cloudformation:GetTemplate](#list_cloudformation-action-GetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateSummary  **
  - **IAM action:**  [cloudformation:GetTemplateSummary](#list_cloudformation-action-GetTemplateSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportStacksToStackSet  **
  - **IAM action:**  [cloudformation:ImportStacksToStackSet](#list_cloudformation-action-ImportStacksToStackSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListChangeSets  **
  - **IAM action:**  [cloudformation:ListChangeSets](#list_cloudformation-action-ListChangeSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExports  **
  - **IAM action:**  [cloudformation:ListExports](#list_cloudformation-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGeneratedTemplates  **
  - **IAM action:**  [cloudformation:ListGeneratedTemplates](#list_cloudformation-action-ListGeneratedTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHookResults  **
  - **IAM action:**  [cloudformation:ListAllHookResults](#list_cloudformation-action-ListAllHookResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [cloudformation:ListHookResults](#list_cloudformation-action-ListHookResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListImports  **
  - **IAM action:**  [cloudformation:ListImports](#list_cloudformation-action-ListImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceScanRelatedResources  **
  - **IAM action:**  [cloudformation:ListResourceScanRelatedResources](#list_cloudformation-action-ListResourceScanRelatedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceScanResources  **
  - **IAM action:**  [cloudformation:ListResourceScanResources](#list_cloudformation-action-ListResourceScanResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceScans  **
  - **IAM action:**  [cloudformation:ListResourceScans](#list_cloudformation-action-ListResourceScans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackInstanceResourceDrifts  **
  - **IAM action:**  [cloudformation:ListStackInstanceResourceDrifts](#list_cloudformation-action-ListStackInstanceResourceDrifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackInstances  **
  - **IAM action:**  [cloudformation:ListStackInstances](#list_cloudformation-action-ListStackInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackRefactorActions  **
  - **IAM action:**  [cloudformation:ListStackRefactorActions](#list_cloudformation-action-ListStackRefactorActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackRefactors  **
  - **IAM action:**  [cloudformation:ListStackRefactors](#list_cloudformation-action-ListStackRefactors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackResources  **
  - **IAM action:**  [cloudformation:ListStackResources](#list_cloudformation-action-ListStackResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackSetAutoDeploymentTargets  **
  - **IAM action:**  [cloudformation:ListStackSetAutoDeploymentTargets](#list_cloudformation-action-ListStackSetAutoDeploymentTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackSetOperationResults  **
  - **IAM action:**  [cloudformation:ListStackSetOperationResults](#list_cloudformation-action-ListStackSetOperationResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackSetOperations  **
  - **IAM action:**  [cloudformation:ListStackSetOperations](#list_cloudformation-action-ListStackSetOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStackSets  **
  - **IAM action:**  [cloudformation:ListStackSets](#list_cloudformation-action-ListStackSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStacks  **
  - **IAM action:**  [cloudformation:ListStacks](#list_cloudformation-action-ListStacks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTypeRegistrations  **
  - **IAM action:**  [cloudformation:ListTypeRegistrations](#list_cloudformation-action-ListTypeRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTypeVersions  **
  - **IAM action:**  [cloudformation:ListTypeVersions](#list_cloudformation-action-ListTypeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTypes  **
  - **IAM action:**  [cloudformation:ListTypes](#list_cloudformation-action-ListTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishType  **
  - **IAM action:**  [cloudformation:PublishType](#list_cloudformation-action-PublishType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecordHandlerProgress  **
  - **IAM action:**  [cloudformation:RecordHandlerProgress](#list_cloudformation-action-RecordHandlerProgress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterPublisher  **
  - **IAM action:**  [cloudformation:RegisterPublisher](#list_cloudformation-action-RegisterPublisher) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterType  **
  - **IAM action:**  [cloudformation:RegisterType](#list_cloudformation-action-RegisterType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** resources.cloudformation.amazonaws.com / **Access level:** Write

- **   RollbackStack  **
  - **IAM action:**  [cloudformation:RollbackStack](#list_cloudformation-action-RollbackStack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   SetStackPolicy  **
  - **IAM action:**  [cloudformation:SetStackPolicy](#list_cloudformation-action-SetStackPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetTypeConfiguration  **
  - **IAM action:**  [cloudformation:SetTypeConfiguration](#list_cloudformation-action-SetTypeConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTypeDefaultVersion  **
  - **IAM action:**  [cloudformation:SetTypeDefaultVersion](#list_cloudformation-action-SetTypeDefaultVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SignalResource  **
  - **IAM action:**  [cloudformation:SignalResource](#list_cloudformation-action-SignalResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartResourceScan  **
  - **IAM action:**  [cloudformation:StartResourceScan](#list_cloudformation-action-StartResourceScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopStackSetOperation  **
  - **IAM action:**  [cloudformation:StopStackSetOperation](#list_cloudformation-action-StopStackSetOperation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestType  **
  - **IAM action:**  [cloudformation:TestType](#list_cloudformation-action-TestType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGeneratedTemplate  **
  - **IAM action:**  [cloudformation:UpdateGeneratedTemplate](#list_cloudformation-action-UpdateGeneratedTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStack  **
  - **IAM action:**  [cloudformation:SetStackPolicy](#list_cloudformation-action-SetStackPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UntagResource](#list_cloudformation-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UpdateStack](#list_cloudformation-action-UpdateStack)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   UpdateStackInstances  **
  - **IAM action:**  [cloudformation:UpdateStackInstances](#list_cloudformation-action-UpdateStackInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStackSet  **
  - **IAM action:**  [cloudformation:TagResource](#list_cloudformation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UntagResource](#list_cloudformation-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudformation:UpdateStackSet](#list_cloudformation-action-UpdateStackSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com / **Access level:** Write

- **   UpdateTerminationProtection  **
  - **IAM action:**  [cloudformation:UpdateTerminationProtection](#list_cloudformation-action-UpdateTerminationProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateTemplate  **
  - **IAM action:**  [cloudformation:ValidateTemplate](#list_cloudformation-action-ValidateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS CloudFormation
<a name="list_cloudformation-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivateOrganizationsAccess](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateOrganizationsAccess.html)  **
  - **Description:** Grants permission to activate trusted access between StackSets and Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ActivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html)  **
  - **Description:** Grants permission to activate a public third-party extension, making it available for use in stack templates
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDescribeTypeConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_BatchDescribeTypeConfigurations.html)  **
  - **Description:** Grants permission to return configuration data for the specified CloudFormation extensions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CancelUpdateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html)  **
  - **Description:** Grants permission to cancel an update on the specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ContinueUpdateRollback](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ContinueUpdateRollback.html)  **
  - **Description:** Grants permission to continue rolling back a stack that is in the UPDATE\_ROLLBACK\_FAILED state to the UPDATE\_ROLLBACK\_COMPLETE state
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)
  - **Access level:** Write

- **   [CreateChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html)  **
  - **Description:** Grants permission to create a list of changes for a stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)<br />[cloudformation:ImportResourceTypes](#list_cloudformation-cloudformation_ImportResourceTypes)<br />[cloudformation:ResourceTypes](#list_cloudformation-cloudformation_ResourceTypes)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:StackPolicyUrl](#list_cloudformation-cloudformation_StackPolicyUrl)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Write

- **   [CreateGeneratedTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateGeneratedTemplate.html)  **
  - **Description:** Grants permission to create a template from existing resources that are not already managed with CloudFormation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html)  **
  - **Description:** Grants permission to create a stack as specified in the template
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:ResourceTypes](#list_cloudformation-cloudformation_ResourceTypes)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:StackPolicyUrl](#list_cloudformation-cloudformation_StackPolicyUrl)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Write

- **   [CreateStackInstances](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html)  **
  - **Description:** Grants permission to create stack instances for the specified accounts, within the specified regions
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [stackset-target](#list_cloudformation-resource-stackset-target) / **Condition keys:** [aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [type](#list_cloudformation-resource-type) / **Condition keys:** [aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Access level:** Write

- **   [CreateStackRefactor](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackRefactor.html)  **
  - **Description:** Grants permission to create a stack refactor
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackSet.html)  **
  - **Description:** Grants permission to create a stackset as specified in the template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Write

- **   [DeactivateOrganizationsAccess](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeactivateOrganizationsAccess.html)  **
  - **Description:** Grants permission to deactivate trusted access between StackSets and Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeactivateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeactivateType.html)  **
  - **Description:** Grants permission to deactivate a public extension that was previously activated in this account and region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeleteChangeSet.html)  **
  - **Description:** Grants permission to delete the specified change set. Deleting change sets ensures that no one executes the wrong change set
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)
  - **Access level:** Write

- **   [DeleteGeneratedTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeleteGeneratedTemplate.html)  **
  - **Description:** Grants permission to delete a generated template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeleteStack.html)  **
  - **Description:** Grants permission to delete a specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)
  - **Access level:** Write

- **   [DeleteStackInstances](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeleteStackInstances.html)  **
  - **Description:** Grants permission to delete stack instances for the specified accounts, in the specified regions
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [stackset-target](#list_cloudformation-resource-stackset-target) / **Condition keys:** [cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [type](#list_cloudformation-resource-type) / **Condition keys:** [cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Access level:** Write

- **   [DeleteStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeleteStackSet.html)  **
  - **Description:** Grants permission to delete a specified stackset
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html)  **
  - **Description:** Grants permission to deregister an existing CloudFormation type or type version
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccountLimits](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeAccountLimits.html)  **
  - **Description:** Grants permission to retrieve your account's AWS CloudFormation limits
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeChangeSet.html)  **
  - **Description:** Grants permission to return the description for the specified change set
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)
  - **Access level:** Read

- **   [DescribeChangeSetHooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeChangeSetHooks.html)  **
  - **Description:** Grants permission to return the Hook invocation information for the specified change set
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)
  - **Access level:** Read

- **   [DescribeEvents](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeEvents.html)  **
  - **Description:** Grants permission to return all related events for a specified operation
  - **Resource types (\*required):** [changeset](#list_cloudformation-resource-changeset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeGeneratedTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeGeneratedTemplate.html)  **
  - **Description:** Grants permission to describe a generated template. The output includes details about the progress of the creation of a generated template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationsAccess](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeOrganizationsAccess.html)  **
  - **Description:** Grants permission to return information about the account's OrganizationAccess status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePublisher](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribePublisher.html)  **
  - **Description:** Grants permission to return information about a CloudFormation extension publisher
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeResourceScan](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeResourceScan.html)  **
  - **Description:** Grants permission to describe details of a resource scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStackDriftDetectionStatus](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackDriftDetectionStatus.html)  **
  - **Description:** Grants permission to return information about a stack drift detection operation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStackEvents](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackEvents.html)  **
  - **Description:** Grants permission to return all stack related events for a specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackInstance.html)  **
  - **Description:** Grants permission to return the stack instance that's associated with the specified stack set, AWS account, and region
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackRefactor](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackRefactor.html)  **
  - **Description:** Grants permission to return the description for the specified stack refactor
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackResource.html)  **
  - **Description:** Grants permission to return a description of the specified resource in the specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackResourceDrifts](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackResourceDrifts.html)  **
  - **Description:** Grants permission to return drift information for the resources that have been checked for drift in the specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackResources](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackResources.html)  **
  - **Description:** Grants permission to return AWS resource descriptions for running and deleted stacks
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackSet.html)  **
  - **Description:** Grants permission to return the description of the specified stack set
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStackSetOperation](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackSetOperation.html)  **
  - **Description:** Grants permission to return the description of the specified stack set operation
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStacks.html)  **
  - **Description:** Grants permission to return the description for the specified stack, and to all stacks when used in combination with the ListStacks action
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html)  **
  - **Description:** Grants permission to return information about the CloudFormation type requested
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeTypeRegistration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeTypeRegistration.html)  **
  - **Description:** Grants permission to return information about the registration process for a CloudFormation type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectStackDrift](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DetectStackDrift.html)  **
  - **Description:** Grants permission to detects whether a stack's actual configuration differs, or has drifted, from it's expected configuration, as defined in the stack template and any values specified as template parameters
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectStackResourceDrift](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DetectStackResourceDrift.html)  **
  - **Description:** Grants permission to return information about whether a resource's actual configuration differs, or has drifted, from it's expected configuration, as defined in the stack template and any values specified as template parameters
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectStackSetDrift](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DetectStackSetDrift.html)  **
  - **Description:** Grants permission to enable users to detect drift on a stack set and the stack instances that belong to that stack set
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [EstimateTemplateCost](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_EstimateTemplateCost.html)  **
  - **Description:** Grants permission to return the estimated monthly cost of a template
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Read

- **   [ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html)  **
  - **Description:** Grants permission to update a stack using the input information that was provided when the specified change set was created
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)
  - **Access level:** Write

- **   [ExecuteStackRefactor](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteStackRefactor.html)  **
  - **Description:** Grants permission to execute a stack refactor using the input information that was provided when the specified stack refactor was created
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetGeneratedTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetGeneratedTemplate.html)  **
  - **Description:** Grants permission to retrieve a generated template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetHookResult](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetHookResult.html)  **
  - **Description:** Grants permission to return detailed information about a specific hook invocation result
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudformation:TypeArn](#list_cloudformation-cloudformation_TypeArn)
  - **Access level:** Read

- **   [GetStackPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetStackPolicy.html)  **
  - **Description:** Grants permission to return the stack policy for a specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetTemplate.html)  **
  - **Description:** Grants permission to return the template body for a specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplateSummary](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetTemplateSummary.html)  **
  - **Description:** Grants permission to return information about a new or existing template
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Resource types (\*required):** [stackset](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Read

- **   [ImportStacksToStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ImportStacksToStackSet.html)  **
  - **Description:** Grants permission to enable users to import existing stacks to a new or existing stackset
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAllHookResults](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListHookResults.html)  **
  - **Description:** Grants permission to return Hook invocations result information for a specified Hook, a combination of Hook and status, or all Hooks
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudformation:TypeArn](#list_cloudformation-cloudformation_TypeArn)
  - **Access level:** List

- **   [ListChangeSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListChangeSets.html)  **
  - **Description:** Grants permission to return the ID and status of each active change set for a stack. For example, AWS CloudFormation lists change sets that are in the CREATE\_IN\_PROGRESS or CREATE\_PENDING state
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListExports.html)  **
  - **Description:** Grants permission to list all exported output values in the account and region in which you call this action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGeneratedTemplates](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListGeneratedTemplates.html)  **
  - **Description:** Grants permission to list your generated templates in this Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHookResults](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListHookResults.html)  **
  - **Description:** Grants permission to return Hook invocations result information for the specified target
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:ChangeSetName](#list_cloudformation-cloudformation_ChangeSetName)
  - **Access level:** List

- **   [ListImports](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListImports.html)  **
  - **Description:** Grants permission to list all stacks that are importing an exported output value
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceScanRelatedResources](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListResourceScanRelatedResources.html)  **
  - **Description:** Grants permission to list the related resources for a list of resources from a resource scan. The response indicates whether each returned resource is already managed by CloudFormation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceScanResources](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListResourceScanResources.html)  **
  - **Description:** Grants permission to list the resources from a resource scan. The results can be filtered by resource identifier, resource type prefix, tag key, and tag value
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceScans](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListResourceScans.html)  **
  - **Description:** Grants permission to list the resource scans from newest to oldest. By default it will return up to 10 resource scans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStackInstanceResourceDrifts](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackInstanceResourceDrifts.html)  **
  - **Description:** Grants permission to return drift information for the resources that have been checked for drift in the specified stack instance
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackInstances](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSets.html)  **
  - **Description:** Grants permission to return summary information about stack instances that are associated with the specified stack set
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackRefactorActions](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackRefactorActions.html)  **
  - **Description:** Grants permission to return the list of actions of the specified stack refactor
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackRefactors](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackRefactors.html)  **
  - **Description:** Grants permission to return the ID and status of each active stack refactor
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackResources](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackResources.html)  **
  - **Description:** Grants permission to return descriptions of all resources of the specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackSetAutoDeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetAutoDeploymentTargets.html)  **
  - **Description:** Grants permission to return summary information about StackSet Auto Deployment Targets
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackSetOperationResults](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetOperationResults.html)  **
  - **Description:** Grants permission to return summary information about the results of a stack set operation
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackSetOperations](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetOperations.html)  **
  - **Description:** Grants permission to return summary information about operations performed on a stack set
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSets.html)  **
  - **Description:** Grants permission to return summary information about stack sets that are associated with the user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStacks.html)  **
  - **Description:** Grants permission to return the summary information for stacks whose status matches the specified StackStatusFilter. In combination with the DescribeStacks action, grants permission to list descriptions for stacks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTypeRegistrations](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypeRegistrations.html)  **
  - **Description:** Grants permission to list CloudFormation type registration attempts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTypeVersions](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypeVersions.html)  **
  - **Description:** Grants permission to list versions of a particular CloudFormation type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypes.html)  **
  - **Description:** Grants permission to list available CloudFormation types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PublishType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_PublishType.html)  **
  - **Description:** Grants permission to publish the specified extension to the CloudFormation registry as a public extension in this region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RecordHandlerProgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RecordHandlerProgress.html)  **
  - **Description:** Grants permission to record the handler progress
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterPublisher](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html)  **
  - **Description:** Grants permission to register account as a publisher of public extensions in the CloudFormation registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html)  **
  - **Description:** Grants permission to register a new CloudFormation type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RollbackStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RollbackStack.html)  **
  - **Description:** Grants permission to rollback the stack to the last stable state
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)
  - **Access level:** Write

- **   [SetStackPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetStackPolicy.html)  **
  - **Description:** Grants permission to set a stack policy for a specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:StackPolicyUrl](#list_cloudformation-cloudformation_StackPolicyUrl)
  - **Access level:** Permissions management, Write

- **   [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html)  **
  - **Description:** Grants permission to set the configuration data for a registered CloudFormation extension, in the given account and region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetTypeDefaultVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeDefaultVersion.html)  **
  - **Description:** Grants permission to set which version of a CloudFormation type applies to CloudFormation operations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SignalResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SignalResource.html)  **
  - **Description:** Grants permission to send a signal to the specified resource with a success or failure status
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartResourceScan](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StartResourceScan.html)  **
  - **Description:** Grants permission to start a scan of the resources in this account in this Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopStackSetOperation](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StopStackSetOperation.html)  **
  - **Description:** Grants permission to stop an in-progress operation on a stack set and its associated stack instances
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag cloudformation resources
  - **Resource types (\*required):** [changeset](#list_cloudformation-resource-changeset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Resource types (\*required):** [stackset](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Access level:** Tagging, Write

- **   [TestType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_TestType.html)  **
  - **Description:** Grants permission to test a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag cloudformation resources
  - **Resource types (\*required):** [changeset](#list_cloudformation-resource-changeset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Resource types (\*required):** [stack](#list_cloudformation-resource-stack) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Resource types (\*required):** [stackset](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:CreateAction](#list_cloudformation-cloudformation_CreateAction)
  - **Access level:** Tagging, Write

- **   [UpdateGeneratedTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateGeneratedTemplate.html)  **
  - **Description:** Grants permission to update a generated template. This can be used to change the name, add and remove resources, refresh resources, and change the DeletionPolicy and UpdateReplacePolicy settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStack](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html)  **
  - **Description:** Grants permission to update a stack as specified in the template
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:ResourceTypes](#list_cloudformation-cloudformation_ResourceTypes)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:StackPolicyUrl](#list_cloudformation-cloudformation_StackPolicyUrl)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Write

- **   [UpdateStackInstances](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackInstances.html)  **
  - **Description:** Grants permission to update the parameter values for stack instances for the specified accounts, within the specified regions
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [stackset-target](#list_cloudformation-resource-stackset-target) / **Condition keys:** [cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Resource types (\*required):** [type](#list_cloudformation-resource-type) / **Condition keys:** [cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)
  - **Access level:** Write

- **   [UpdateStackSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html)  **
  - **Description:** Grants permission to update a stackset as specified in the template
  - **Resource types (\*required):** [stackset\*](#list_cloudformation-resource-stackset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Resource types (\*required):** [stackset-target](#list_cloudformation-resource-stackset-target) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Resource types (\*required):** [type](#list_cloudformation-resource-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cloudformation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cloudformation-aws_TagKeys)<br />[cloudformation:RoleArn](#list_cloudformation-cloudformation_RoleArn)<br />[cloudformation:TargetRegion](#list_cloudformation-cloudformation_TargetRegion)<br />[cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Write

- **   [UpdateTerminationProtection](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateTerminationProtection.html)  **
  - **Description:** Grants permission to update termination protection for the specified stack
  - **Resource types (\*required):** [stack\*](#list_cloudformation-resource-stack)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ValidateTemplate.html)  **
  - **Description:** Grants permission to validate a specified template
  - **Resource types (\*required):** 
  - **Condition keys:** [cloudformation:TemplateUrl](#list_cloudformation-cloudformation_TemplateUrl)
  - **Access level:** Read



## Permission-only actions for AWS CloudFormation
<a name="list_cloudformation-permission-only-actions"></a>

The following actions are defined by AWS CloudFormation but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateUploadBucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)  | Grants permission to upload templates to Amazon S3 buckets. Used only by the AWS CloudFormation console and is not documented in the API reference |  |   | Write | 

## Resource types defined by AWS CloudFormation
<a name="list_cloudformation-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [changeset](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15c11)  | arn:${Partition}:cloudformation:${Region}:${Account}:changeSet/${ChangeSetName}/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_) | 
|  [generatedtemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)  | arn:${Partition}:cloudformation:${Region}:${Account}:generatedTemplate/${Id} |   | 
|  [resourcescan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)  | arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id} |   | 
|  [stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html#w2ab1b5c15b9)  | arn:${Partition}:cloudformation:${Region}:${Account}:stack/${StackName}/${Id} | [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_) | 
|  [stackset](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stacksets-concepts-stackset)  | arn:${Partition}:cloudformation:${Region}:${Account}:stackset/${StackSetName}:${Id} | [aws:ResourceTag/${TagKey}](#list_cloudformation-aws_ResourceTag___TagKey_) | 
|  [stackset-target](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)  | arn:${Partition}:cloudformation:${Region}:${Account}:stackset-target/${StackSetTarget} |   | 
|  [type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)  | arn:${Partition}:cloudformation:${Region}:${Account}:type/resource/${Type} |   | 
|  [typeHook](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)  | arn:${Partition}:cloudformation:${Region}:${Account}:type/hook/${Type} |   | 

## Condition keys for AWS CloudFormation
<a name="list_cloudformation-policy-keys"></a>

AWS CloudFormation defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [cloudformation:ChangeSetName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by an AWS CloudFormation change set name. Use to control which change sets IAM users can execute or delete | String | 
|   [cloudformation:CreateAction](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the name of a resource-mutating API action. Use to control which APIs IAM users can use to add or remove tags on a stack or stack set | String | 
|   [cloudformation:ImportResourceTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the template resource types, such as AWS::EC2::Instance. Use to control which resource types IAM users can work with when they want to import a resource into a stack | String | 
|   [cloudformation:ResourceTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the template resource types, such as AWS::EC2::Instance. Use to control which resource types IAM users can work with when they create or update a stack | ArrayOfString | 
|   [cloudformation:RoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the ARN of an IAM service role. Use to control which service role IAM users can use to work with stacks or change sets | ARN | 
|   [cloudformation:StackPolicyUrl](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by an Amazon S3 stack policy URL. Use to control which stack policies IAM users can associate with a stack during a create or update stack action | String | 
|   [cloudformation:TargetRegion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by stack set target region. Use to control which regions IAM users can use when they create or update stack sets | ArrayOfString | 
|   [cloudformation:TemplateUrl](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by an Amazon S3 template URL. Use to control which templates IAM users can use when they create or update stacks | String | 
|   [cloudformation:TypeArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-template-conditions)  | Filters access by the ARN of a CloudFormation extension | ARN | 