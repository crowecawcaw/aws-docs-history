

# Actions, resources, and condition keys for AWS Elastic Disaster Recovery
<a name="list_drs"></a>

AWS Elastic Disaster Recovery (service prefix: `drs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/drs/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/drs/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/drs/latest/userguide/security_iam_authentication.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/drs/drs.json) for this service.

**Topics**
+ [API operations defined by AWS Elastic Disaster Recovery](#list_drs-operations)
+ [Actions defined by AWS Elastic Disaster Recovery](#list_drs-actions-as-permissions)
+ [Permission-only actions for AWS Elastic Disaster Recovery](#list_drs-permission-only-actions)
+ [Resource types defined by AWS Elastic Disaster Recovery](#list_drs-resources-for-iam-policies)
+ [Condition keys for AWS Elastic Disaster Recovery](#list_drs-policy-keys)

## API operations defined by AWS Elastic Disaster Recovery
<a name="list_drs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_drs-actions-as-permissions).




- **   AssociateSourceNetworkStack  **
  - **IAM action:**  [drs:AssociateSourceNetworkStack](#list_drs-action-AssociateSourceNetworkStack) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateExtendedSourceServer  **
  - **IAM action:**  [drs:CreateExtendedSourceServer](#list_drs-action-CreateExtendedSourceServer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLaunchConfigurationTemplate  **
  - **IAM action:**  [drs:CreateLaunchConfigurationTemplate](#list_drs-action-CreateLaunchConfigurationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecoveryPlan  **
  - **IAM action:**  [drs:CreateRecoveryPlan](#list_drs-action-CreateRecoveryPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecoveryPlanStep  **
  - **IAM action:**  [drs:CreateRecoveryPlanStep](#list_drs-action-CreateRecoveryPlanStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateReplicationConfigurationTemplate  **
  - **IAM action:**  [drs:CreateReplicationConfigurationTemplate](#list_drs-action-CreateReplicationConfigurationTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSourceNetwork  **
  - **IAM action:**  [drs:CreateSourceNetwork](#list_drs-action-CreateSourceNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteJob  **
  - **IAM action:**  [drs:DeleteJob](#list_drs-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLaunchAction  **
  - **IAM action:**  [drs:DeleteLaunchAction](#list_drs-action-DeleteLaunchAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLaunchConfigurationTemplate  **
  - **IAM action:**  [drs:DeleteLaunchConfigurationTemplate](#list_drs-action-DeleteLaunchConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecoveryInstance  **
  - **IAM action:**  [drs:DeleteRecoveryInstance](#list_drs-action-DeleteRecoveryInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecoveryPlan  **
  - **IAM action:**  [drs:DeleteRecoveryPlan](#list_drs-action-DeleteRecoveryPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecoveryPlanStep  **
  - **IAM action:**  [drs:DeleteRecoveryPlanStep](#list_drs-action-DeleteRecoveryPlanStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReplicationConfigurationTemplate  **
  - **IAM action:**  [drs:DeleteReplicationConfigurationTemplate](#list_drs-action-DeleteReplicationConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSourceNetwork  **
  - **IAM action:**  [drs:DeleteSourceNetwork](#list_drs-action-DeleteSourceNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSourceServer  **
  - **IAM action:**  [drs:DeleteSourceServer](#list_drs-action-DeleteSourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeJobLogItems  **
  - **IAM action:**  [drs:DescribeJobLogItems](#list_drs-action-DescribeJobLogItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobs  **
  - **IAM action:**  [drs:DescribeJobs](#list_drs-action-DescribeJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLaunchConfigurationTemplates  **
  - **IAM action:**  [drs:DescribeLaunchConfigurationTemplates](#list_drs-action-DescribeLaunchConfigurationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecoveryInstances  **
  - **IAM action:**  [drs:DescribeRecoveryInstances](#list_drs-action-DescribeRecoveryInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecoverySnapshots  **
  - **IAM action:**  [drs:DescribeRecoverySnapshots](#list_drs-action-DescribeRecoverySnapshots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReplicationConfigurationTemplates  **
  - **IAM action:**  [drs:DescribeReplicationConfigurationTemplates](#list_drs-action-DescribeReplicationConfigurationTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSourceNetworks  **
  - **IAM action:**  [drs:DescribeSourceNetworks](#list_drs-action-DescribeSourceNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSourceServers  **
  - **IAM action:**  [drs:DescribeSourceServers](#list_drs-action-DescribeSourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisconnectRecoveryInstance  **
  - **IAM action:**  [drs:DisconnectRecoveryInstance](#list_drs-action-DisconnectRecoveryInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisconnectSourceServer  **
  - **IAM action:**  [drs:DisconnectSourceServer](#list_drs-action-DisconnectSourceServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportSourceNetworkCfnTemplate  **
  - **IAM action:**  [drs:ExportSourceNetworkCfnTemplate](#list_drs-action-ExportSourceNetworkCfnTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetFailbackReplicationConfiguration  **
  - **IAM action:**  [drs:GetFailbackReplicationConfiguration](#list_drs-action-GetFailbackReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLaunchConfiguration  **
  - **IAM action:**  [drs:GetLaunchConfiguration](#list_drs-action-GetLaunchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPlan  **
  - **IAM action:**  [drs:GetRecoveryPlan](#list_drs-action-GetRecoveryPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPlanExecution  **
  - **IAM action:**  [drs:GetRecoveryPlanExecution](#list_drs-action-GetRecoveryPlanExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecoveryPlanStep  **
  - **IAM action:**  [drs:GetRecoveryPlanStep](#list_drs-action-GetRecoveryPlanStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReplicationConfiguration  **
  - **IAM action:**  [drs:GetReplicationConfiguration](#list_drs-action-GetReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitializeService  **
  - **IAM action:**  [drs:InitializeService](#list_drs-action-InitializeService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListExtensibleSourceServers  **
  - **IAM action:**  [drs:ListExtensibleSourceServers](#list_drs-action-ListExtensibleSourceServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLaunchActions  **
  - **IAM action:**  [drs:ListLaunchActions](#list_drs-action-ListLaunchActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecoveryPlanExecutions  **
  - **IAM action:**  [drs:ListRecoveryPlanExecutions](#list_drs-action-ListRecoveryPlanExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecoveryPlanSteps  **
  - **IAM action:**  [drs:ListRecoveryPlanSteps](#list_drs-action-ListRecoveryPlanSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecoveryPlans  **
  - **IAM action:**  [drs:ListRecoveryPlans](#list_drs-action-ListRecoveryPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStagingAccounts  **
  - **IAM action:**  [drs:ListStagingAccounts](#list_drs-action-ListStagingAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [drs:ListTagsForResource](#list_drs-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutLaunchAction  **
  - **IAM action:**  [drs:PutLaunchAction](#list_drs-action-PutLaunchAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReorderRecoveryPlanSteps  **
  - **IAM action:**  [drs:ReorderRecoveryPlanSteps](#list_drs-action-ReorderRecoveryPlanSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetryDataReplication  **
  - **IAM action:**  [drs:RetryDataReplication](#list_drs-action-RetryDataReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReverseReplication  **
  - **IAM action:**  [drs:ReverseReplication](#list_drs-action-ReverseReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRecovery  **
  - **IAM action:**  [drs:StartRecovery](#list_drs-action-StartRecovery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartReplication  **
  - **IAM action:**  [drs:StartReplication](#list_drs-action-StartReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSourceNetworkRecovery  **
  - **IAM action:**  [drs:StartSourceNetworkRecovery](#list_drs-action-StartSourceNetworkRecovery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartSourceNetworkReplication  **
  - **IAM action:**  [drs:StartSourceNetworkReplication](#list_drs-action-StartSourceNetworkReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFailback  **
  - **IAM action:**  [drs:StopFailback](#list_drs-action-StopFailback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopReplication  **
  - **IAM action:**  [drs:StopReplication](#list_drs-action-StopReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSourceNetworkReplication  **
  - **IAM action:**  [drs:StopSourceNetworkReplication](#list_drs-action-StopSourceNetworkReplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [drs:TagResource](#list_drs-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateRecoveryInstances  **
  - **IAM action:**  [drs:TerminateRecoveryInstances](#list_drs-action-TerminateRecoveryInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [drs:UntagResource](#list_drs-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateFailbackReplicationConfiguration  **
  - **IAM action:**  [drs:UpdateFailbackReplicationConfiguration](#list_drs-action-UpdateFailbackReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLaunchConfiguration  **
  - **IAM action:**  [drs:UpdateLaunchConfiguration](#list_drs-action-UpdateLaunchConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLaunchConfigurationTemplate  **
  - **IAM action:**  [drs:UpdateLaunchConfigurationTemplate](#list_drs-action-UpdateLaunchConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecoveryPlan  **
  - **IAM action:**  [drs:UpdateRecoveryPlan](#list_drs-action-UpdateRecoveryPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecoveryPlanStep  **
  - **IAM action:**  [drs:UpdateRecoveryPlanStep](#list_drs-action-UpdateRecoveryPlanStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationConfiguration  **
  - **IAM action:**  [drs:UpdateReplicationConfiguration](#list_drs-action-UpdateReplicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateReplicationConfigurationTemplate  **
  - **IAM action:**  [drs:UpdateReplicationConfigurationTemplate](#list_drs-action-UpdateReplicationConfigurationTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Elastic Disaster Recovery
<a name="list_drs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateSourceNetworkStack](https://docs.aws.amazon.com/drs/latest/APIReference/API_AssociateSourceNetworkStack.html)  **
  - **Description:** Grants permission to associate CloudFormation stack with source network
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CancelRecoveryPlanExecution](https://docs.aws.amazon.com/drs/latest/APIReference/API_CancelRecoveryPlanExecution.html)  **
  - **Description:** Grants permission to cancel a recovery plan execution
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateExtendedSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateExtendedSourceServer.html)  **
  - **Description:** Grants permission to extend a source server
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to create launch configuration template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecoveryPlan](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateRecoveryPlan.html)  **
  - **Description:** Grants permission to create a recovery plan
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecoveryPlanStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateRecoveryPlanStep.html)  **
  - **Description:** Grants permission to create a step in a recovery plan
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to create replication configuration template
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSourceNetwork](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateSourceNetwork.html)  **
  - **Description:** Grants permission to create a source network
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteJob.html)  **
  - **Description:** Grants permission to delete a job
  - **Resource types (\*required):** [JobResource\*](#list_drs-resource-JobResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLaunchAction](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteLaunchAction.html)  **
  - **Description:** Grants permission to delete a launch action
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_drs-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SourceServerResource](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to delete launch configuration template
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_drs-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecoveryInstance](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteRecoveryInstance.html)  **
  - **Description:** Grants permission to delete recovery instance
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [DeleteRecoveryPlan](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteRecoveryPlan.html)  **
  - **Description:** Grants permission to delete a recovery plan
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecoveryPlanExecution](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteRecoveryPlanExecution.html)  **
  - **Description:** Grants permission to delete a recovery plan execution
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecoveryPlanStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteRecoveryPlanStep.html)  **
  - **Description:** Grants permission to delete a recovery plan step
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to delete replication configuration template
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource\*](#list_drs-resource-ReplicationConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSourceNetwork](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteSourceNetwork.html)  **
  - **Description:** Grants permission to delete source network
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteSourceServer.html)  **
  - **Description:** Grants permission to delete source server
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeJobLogItems](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobLogItems.html)  **
  - **Description:** Grants permission to describe job log items
  - **Resource types (\*required):** [JobResource\*](#list_drs-resource-JobResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobs](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobs.html)  **
  - **Description:** Grants permission to describe jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLaunchConfigurationTemplates](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeLaunchConfigurationTemplates.html)  **
  - **Description:** Grants permission to describe launch configuration template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecoveryInstances](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoveryInstances.html)  **
  - **Description:** Grants permission to describe recovery instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeRecoverySnapshots](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoverySnapshots.html)  **
  - **Description:** Grants permission to describe recovery snapshots
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReplicationConfigurationTemplates](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeReplicationConfigurationTemplates.html)  **
  - **Description:** Grants permission to describe replication configuration template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSourceNetworks](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceNetworks.html)  **
  - **Description:** Grants permission to describe source networks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSourceServers](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceServers.html)  **
  - **Description:** Grants permission to describe source servers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisconnectRecoveryInstance](https://docs.aws.amazon.com/drs/latest/APIReference/API_DisconnectRecoveryInstance.html)  **
  - **Description:** Grants permission to disconnect recovery instance
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [DisconnectSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_DisconnectSourceServer.html)  **
  - **Description:** Grants permission to disconnect source server
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportSourceNetworkCfnTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_ExportSourceNetworkCfnTemplate.html)  **
  - **Description:** Grants permission to export CloudFormation template which contains source network resources
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [GetFailbackReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetFailbackReplicationConfiguration.html)  **
  - **Description:** Grants permission to get failback replication configuration
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Read

- **   [GetLaunchConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetLaunchConfiguration.html)  **
  - **Description:** Grants permission to get launch configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPlan](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetRecoveryPlan.html)  **
  - **Description:** Grants permission to get a recovery plan
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPlanExecution](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetRecoveryPlanExecution.html)  **
  - **Description:** Grants permission to get a recovery plan execution
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPlanExecutionStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetRecoveryPlanExecutionStep.html)  **
  - **Description:** Grants permission to get a recovery plan execution step
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecoveryPlanStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetRecoveryPlanStep.html)  **
  - **Description:** Grants permission to get a recovery plan step
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetReplicationConfiguration.html)  **
  - **Description:** Grants permission to get replication configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitializeService](https://docs.aws.amazon.com/drs/latest/APIReference/API_InitializeService.html)  **
  - **Description:** Grants permission to initialize service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListExtensibleSourceServers](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListExtensibleSourceServers.html)  **
  - **Description:** Grants permission to list extensible source servers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLaunchActions](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListLaunchActions.html)  **
  - **Description:** Grants permission to list launch actions
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_drs-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SourceServerResource](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRecoveryPlanExecutionSteps](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListRecoveryPlanExecutionSteps.html)  **
  - **Description:** Grants permission to list recovery plan execution steps
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRecoveryPlanExecutions](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListRecoveryPlanExecutions.html)  **
  - **Description:** Grants permission to list recovery plan executions
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRecoveryPlanSteps](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListRecoveryPlanSteps.html)  **
  - **Description:** Grants permission to list recovery plan steps
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRecoveryPlans](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListRecoveryPlans.html)  **
  - **Description:** Grants permission to list recovery plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListStagingAccounts](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListStagingAccounts.html)  **
  - **Description:** Grants permission to list staging accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutLaunchAction](https://docs.aws.amazon.com/drs/latest/APIReference/API_PutLaunchAction.html)  **
  - **Description:** Grants permission to put a launch action
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_drs-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [SourceServerResource](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReorderRecoveryPlanSteps](https://docs.aws.amazon.com/drs/latest/APIReference/API_ReorderRecoveryPlanSteps.html)  **
  - **Description:** Grants permission to reorder steps in a recovery plan
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetryDataReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_RetryDataReplication.html)  **
  - **Description:** Grants permission to retry data replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetryRecoveryPlanExecutionStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_RetryRecoveryPlanExecutionStep.html)  **
  - **Description:** Grants permission to retry a recovery plan execution step
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReverseReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_ReverseReplication.html)  **
  - **Description:** Grants permission to reverse replication
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [StartFailbackLaunch](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartFailbackLaunch.html)  **
  - **Description:** Grants permission to start failback launch
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [StartRecovery](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecovery.html)  **
  - **Description:** Grants permission to start recovery
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [StartRecoveryPlanExecution](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecoveryPlanExecution.html)  **
  - **Description:** Grants permission to start a recovery plan execution
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [StartReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartReplication.html)  **
  - **Description:** Grants permission to start replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSourceNetworkRecovery](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkRecovery.html)  **
  - **Description:** Grants permission to start network recovery
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [StartSourceNetworkReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkReplication.html)  **
  - **Description:** Grants permission to start network replication
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopFailback](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopFailback.html)  **
  - **Description:** Grants permission to stop failback
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [StopReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopReplication.html)  **
  - **Description:** Grants permission to stop replication
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSourceNetworkReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopSourceNetworkReplication.html)  **
  - **Description:** Grants permission to stop network replication
  - **Resource types (\*required):** [SourceNetworkResource\*](#list_drs-resource-SourceNetworkResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to assign a resource tag
  - **Resource types (\*required):** [JobResource](#list_drs-resource-JobResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_drs-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [RecoveryInstanceResource](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [RecoveryPlanExecutionResource](#list_drs-resource-RecoveryPlanExecutionResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [RecoveryPlanResource](#list_drs-resource-RecoveryPlanResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource](#list_drs-resource-ReplicationConfigurationTemplateResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [SourceNetworkResource](#list_drs-resource-SourceNetworkResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Resource types (\*required):** [SourceServerResource](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:CreateAction](#list_drs-drs_CreateAction)
  - **Access level:** Tagging, Write

- **   [TerminateRecoveryInstances](https://docs.aws.amazon.com/drs/latest/APIReference/API_TerminateRecoveryInstances.html)  **
  - **Description:** Grants permission to terminate recovery instances
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [JobResource](#list_drs-resource-JobResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource](#list_drs-resource-LaunchConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [RecoveryInstanceResource](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [RecoveryPlanExecutionResource](#list_drs-resource-RecoveryPlanExecutionResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [RecoveryPlanResource](#list_drs-resource-RecoveryPlanResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource](#list_drs-resource-ReplicationConfigurationTemplateResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [SourceNetworkResource](#list_drs-resource-SourceNetworkResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Resource types (\*required):** [SourceServerResource](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateFailbackReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateFailbackReplicationConfiguration.html)  **
  - **Description:** Grants permission to update failback replication configuration
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [UpdateLaunchConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfiguration.html)  **
  - **Description:** Grants permission to update launch configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfigurationTemplate.html)  **
  - **Description:** Grants permission to update launch configuration
  - **Resource types (\*required):** [LaunchConfigurationTemplateResource\*](#list_drs-resource-LaunchConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecoveryPlan](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateRecoveryPlan.html)  **
  - **Description:** Grants permission to update a recovery plan
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecoveryPlanExecutionStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateRecoveryPlanExecutionStep.html)  **
  - **Description:** Grants permission to update a recovery plan execution step
  - **Resource types (\*required):** [RecoveryPlanExecutionResource\*](#list_drs-resource-RecoveryPlanExecutionResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecoveryPlanStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateRecoveryPlanStep.html)  **
  - **Description:** Grants permission to update a recovery plan step
  - **Resource types (\*required):** [RecoveryPlanResource\*](#list_drs-resource-RecoveryPlanResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateReplicationConfiguration.html)  **
  - **Description:** Grants permission to update replication configuration
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateReplicationConfigurationTemplate.html)  **
  - **Description:** Grants permission to update replication configuration template
  - **Resource types (\*required):** [ReplicationConfigurationTemplateResource\*](#list_drs-resource-ReplicationConfigurationTemplateResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Elastic Disaster Recovery
<a name="list_drs-permission-only-actions"></a>

The following actions are defined by AWS Elastic Disaster Recovery but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateFailbackClientToRecoveryInstanceForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get associate failback client to recovery instance
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [BatchCreateVolumeSnapshotGroupForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to batch create volume snapshot group
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteSnapshotRequestForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to batch delete snapshot request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateConvertedSnapshotForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to create converted snapshot
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecoveryInstanceForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to create recovery instance
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSourceServerForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to create a source server
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_drs-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_drs-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeReplicationServerAssociationsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to describe replication server associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSnapshotRequestsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to describe snapshot requests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentCommandForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent command
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentConfirmedResumeInfoForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent confirmed resume info
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentInstallationAssetsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent installation assets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentReplicationInfoForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent replication info
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRuntimeConfigurationForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent runtime configuration
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentSnapshotCreditsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get agent snapshot credits
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChannelCommandsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get channel commands
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFailbackCommandForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get failback command
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Read

- **   [GetFailbackLaunchRequestedForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get failback launch requested
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Read

- **   [GetSuggestedFailbackClientDeviceMappingForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to get suggested failback client device mapping
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Read

- **   [IssueAgentCertificateForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to issue an agent certificate
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentAuthenticationForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify agent authentication
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentConnectedForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify agent is connected
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentDisconnectedForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify agent is disconnected
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyAgentReplicationProgressForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify agent replication progress
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyConsistencyAttainedForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify consistency attained
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [NotifyReplicationServerAuthenticationForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify replication server authentication
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [NotifyVolumeEventForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to notify replicator volume events
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendAgentLogsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send agent logs
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendAgentMetricsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send agent metrics
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendChannelCommandResultForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send channel command result
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendClientLogsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send client logs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendClientMetricsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send client metrics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendVolumeStatsForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to send volume throughput statistics
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentBacklogForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update agent backlog
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentConversionInfoForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update agent conversion info
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentReplicationInfoForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update agent replication info
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentReplicationProcessStateForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update agent replication process state
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentSourcePropertiesForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update agent source properties
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Resource types (\*required):** [SourceServerResource\*](#list_drs-resource-SourceServerResource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFailbackClientDeviceMappingForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update failback client device mapping
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [UpdateFailbackClientLastSeenForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update failback client last seen
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write

- **   [UpdateReplicationCertificateForDrs](https://docs.aws.amazon.com/drs/latest/userguide/drs-apis.html)  **
  - **Description:** Grants permission to update a replication certificate
  - **Resource types (\*required):** [RecoveryInstanceResource\*](#list_drs-resource-RecoveryInstanceResource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN)
  - **Access level:** Write



## Resource types defined by AWS Elastic Disaster Recovery
<a name="list_drs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [JobResource](https://docs.aws.amazon.com/drs/latest/userguide/failback-overview.html)  | arn:${Partition}:drs:${Region}:${Account}:job/${JobID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [LaunchConfigurationTemplateResource](https://docs.aws.amazon.com/drs/latest/userguide/default-drs-launch-settings.html)  | arn:${Partition}:drs:${Region}:${Account}:launch-configuration-template/${LaunchConfigurationTemplateID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [RecoveryInstanceResource](https://docs.aws.amazon.com/drs/latest/userguide/recovery-instances.html)  | arn:${Partition}:drs:${Region}:${Account}:recovery-instance/${RecoveryInstanceID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_)<br />[drs:EC2InstanceARN](#list_drs-drs_EC2InstanceARN) | 
|  [RecoveryPlanExecutionResource](https://docs.aws.amazon.com/drs/latest/userguide/recovery-plan-execution.html)  | arn:${Partition}:drs:${Region}:${Account}:recovery-plan-execution/${RecoveryPlanExecutionID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [RecoveryPlanResource](https://docs.aws.amazon.com/drs/latest/userguide/recovery-plan.html)  | arn:${Partition}:drs:${Region}:${Account}:recovery-plan/${RecoveryPlanID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [ReplicationConfigurationTemplateResource](https://docs.aws.amazon.com/drs/latest/userguide/replication-settings-template.html)  | arn:${Partition}:drs:${Region}:${Account}:replication-configuration-template/${ReplicationConfigurationTemplateID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [SourceNetworkResource](https://docs.aws.amazon.com/drs/latest/userguide/source-networks.html)  | arn:${Partition}:drs:${Region}:${Account}:source-network/${SourceNetworkID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 
|  [SourceServerResource](https://docs.aws.amazon.com/drs/latest/userguide/source-servers.html)  | arn:${Partition}:drs:${Region}:${Account}:source-server/${SourceServerID} | [aws:ResourceTag/${TagKey}](#list_drs-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elastic Disaster Recovery
<a name="list_drs-policy-keys"></a>

AWS Elastic Disaster Recovery defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [drs:CreateAction](https://docs.aws.amazon.com/drs/latest/userguide/supported-iam-actions-tagging.html)  | Filters access by the name of a resource-creating API action | String | 
|   [drs:EC2InstanceARN](https://docs.aws.amazon.com/drs/latest/userguide/security_iam_authentication.html)  | Filters access by the EC2 instance the request originated from | ARN | 