

# Actions, resources, and condition keys for Amazon Elastic MapReduce
<a name="list_emr"></a>

Amazon Elastic MapReduce (service prefix: `elasticmapreduce`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/emr/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticmapreduce/elasticmapreduce.json) for this service.

**Topics**
+ [API operations defined by Amazon Elastic MapReduce](#list_emr-operations)
+ [Actions defined by Amazon Elastic MapReduce](#list_emr-actions-as-permissions)
+ [Permission-only actions for Amazon Elastic MapReduce](#list_emr-permission-only-actions)
+ [Resource types defined by Amazon Elastic MapReduce](#list_emr-resources-for-iam-policies)
+ [Condition keys for Amazon Elastic MapReduce](#list_emr-policy-keys)

## API operations defined by Amazon Elastic MapReduce
<a name="list_emr-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_emr-actions-as-permissions).




- **   AddInstanceFleet  **
  - **IAM action:**  [elasticmapreduce:AddInstanceFleet](#list_emr-action-AddInstanceFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddInstanceGroups  **
  - **IAM action:**  [elasticmapreduce:AddInstanceGroups](#list_emr-action-AddInstanceGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddJobFlowSteps  **
  - **IAM action:**  [elasticmapreduce:AddJobFlowSteps](#list_emr-action-AddJobFlowSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTags  **
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CancelSteps  **
  - **IAM action:**  [elasticmapreduce:CancelSteps](#list_emr-action-CancelSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePersistentAppUI  **
  - **IAM action:**  [elasticmapreduce:AccessAllEventLogs](#list_emr-action-AccessAllEventLogs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticmapreduce:CreatePersistentAppUI](#list_emr-action-CreatePersistentAppUI)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSecurityConfiguration  **
  - **IAM action:**  [elasticmapreduce:CreateSecurityConfiguration](#list_emr-action-CreateSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateStudio  **
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticmapreduce:CreateStudio](#list_emr-action-CreateStudio)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateStudioSessionMapping  **
  - **IAM action:**  [elasticmapreduce:CreateStudioSessionMapping](#list_emr-action-CreateStudioSessionMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityConfiguration  **
  - **IAM action:**  [elasticmapreduce:DeleteSecurityConfiguration](#list_emr-action-DeleteSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStudio  **
  - **IAM action:**  [elasticmapreduce:DeleteStudio](#list_emr-action-DeleteStudio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStudioSessionMapping  **
  - **IAM action:**  [elasticmapreduce:DeleteStudioSessionMapping](#list_emr-action-DeleteStudioSessionMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCluster  **
  - **IAM action:**  [elasticmapreduce:DescribeCluster](#list_emr-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobFlows  **
  - **IAM action:**  [elasticmapreduce:DescribeJobFlows](#list_emr-action-DescribeJobFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotebookExecution  **
  - **IAM action:**  [elasticmapreduce:DescribeNotebookExecution](#list_emr-action-DescribeNotebookExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePersistentAppUI  **
  - **IAM action:**  [elasticmapreduce:DescribePersistentAppUI](#list_emr-action-DescribePersistentAppUI) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReleaseLabel  **
  - **IAM action:**  [elasticmapreduce:DescribeReleaseLabel](#list_emr-action-DescribeReleaseLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSecurityConfiguration  **
  - **IAM action:**  [elasticmapreduce:DescribeSecurityConfiguration](#list_emr-action-DescribeSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStep  **
  - **IAM action:**  [elasticmapreduce:DescribeStep](#list_emr-action-DescribeStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStudio  **
  - **IAM action:**  [elasticmapreduce:DescribeStudio](#list_emr-action-DescribeStudio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutoTerminationPolicy  **
  - **IAM action:**  [elasticmapreduce:GetAutoTerminationPolicy](#list_emr-action-GetAutoTerminationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlockPublicAccessConfiguration  **
  - **IAM action:**  [elasticmapreduce:GetBlockPublicAccessConfiguration](#list_emr-action-GetBlockPublicAccessConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClusterSessionCredentials  **
  - **IAM action:**  [elasticmapreduce:GetClusterSessionCredentials](#list_emr-action-GetClusterSessionCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetManagedScalingPolicy  **
  - **IAM action:**  [elasticmapreduce:GetManagedScalingPolicy](#list_emr-action-GetManagedScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOnClusterAppUIPresignedURL  **
  - **IAM action:**  [elasticmapreduce:GetOnClusterAppUIPresignedURL](#list_emr-action-GetOnClusterAppUIPresignedURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetPersistentAppUIPresignedURL  **
  - **IAM action:**  [elasticmapreduce:GetPersistentAppUIPresignedURL](#list_emr-action-GetPersistentAppUIPresignedURL) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSession  **
  - **IAM action:**  [elasticmapreduce:GetSession](#list_emr-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionEndpoint  **
  - **IAM action:**  [elasticmapreduce:GetSessionEndpoint](#list_emr-action-GetSessionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetStudioSessionMapping  **
  - **IAM action:**  [elasticmapreduce:GetStudioSessionMapping](#list_emr-action-GetStudioSessionMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBootstrapActions  **
  - **IAM action:**  [elasticmapreduce:ListBootstrapActions](#list_emr-action-ListBootstrapActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListClusters  **
  - **IAM action:**  [elasticmapreduce:ListClusters](#list_emr-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceFleets  **
  - **IAM action:**  [elasticmapreduce:ListInstanceFleets](#list_emr-action-ListInstanceFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInstanceGroups  **
  - **IAM action:**  [elasticmapreduce:ListInstanceGroups](#list_emr-action-ListInstanceGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInstances  **
  - **IAM action:**  [elasticmapreduce:ListInstances](#list_emr-action-ListInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNotebookExecutions  **
  - **IAM action:**  [elasticmapreduce:ListNotebookExecutions](#list_emr-action-ListNotebookExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReleaseLabels  **
  - **IAM action:**  [elasticmapreduce:ListReleaseLabels](#list_emr-action-ListReleaseLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSecurityConfigurations  **
  - **IAM action:**  [elasticmapreduce:ListSecurityConfigurations](#list_emr-action-ListSecurityConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **IAM action:**  [elasticmapreduce:ListSessions](#list_emr-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSteps  **
  - **IAM action:**  [elasticmapreduce:ListSteps](#list_emr-action-ListSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStudioSessionMappings  **
  - **IAM action:**  [elasticmapreduce:ListStudioSessionMappings](#list_emr-action-ListStudioSessionMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStudios  **
  - **IAM action:**  [elasticmapreduce:ListStudios](#list_emr-action-ListStudios) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSupportedInstanceTypes  **
  - **IAM action:**  [elasticmapreduce:ListSupportedInstanceTypes](#list_emr-action-ListSupportedInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ModifyCluster  **
  - **IAM action:**  [elasticmapreduce:ModifyCluster](#list_emr-action-ModifyCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyInstanceFleet  **
  - **IAM action:**  [elasticmapreduce:ModifyInstanceFleet](#list_emr-action-ModifyInstanceFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ModifyInstanceGroups  **
  - **IAM action:**  [elasticmapreduce:ModifyInstanceGroups](#list_emr-action-ModifyInstanceGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAutoScalingPolicy  **
  - **IAM action:**  [elasticmapreduce:PutAutoScalingPolicy](#list_emr-action-PutAutoScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAutoTerminationPolicy  **
  - **IAM action:**  [elasticmapreduce:PutAutoTerminationPolicy](#list_emr-action-PutAutoTerminationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutBlockPublicAccessConfiguration  **
  - **IAM action:**  [elasticmapreduce:PutBlockPublicAccessConfiguration](#list_emr-action-PutBlockPublicAccessConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutManagedScalingPolicy  **
  - **IAM action:**  [elasticmapreduce:PutManagedScalingPolicy](#list_emr-action-PutManagedScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveAutoScalingPolicy  **
  - **IAM action:**  [elasticmapreduce:RemoveAutoScalingPolicy](#list_emr-action-RemoveAutoScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveAutoTerminationPolicy  **
  - **IAM action:**  [elasticmapreduce:RemoveAutoTerminationPolicy](#list_emr-action-RemoveAutoTerminationPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveManagedScalingPolicy  **
  - **IAM action:**  [elasticmapreduce:RemoveManagedScalingPolicy](#list_emr-action-RemoveManagedScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [elasticmapreduce:RemoveTags](#list_emr-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RunJobFlow  **
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticmapreduce:RunJobFlow](#list_emr-action-RunJobFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** application-autoscaling.amazonaws.com, ec2.amazonaws.com, elasticmapreduce.amazonaws.com / **Access level:** Write

- **   SetKeepJobFlowAliveWhenNoSteps  **
  - **IAM action:**  [elasticmapreduce:SetKeepJobFlowAliveWhenNoSteps](#list_emr-action-SetKeepJobFlowAliveWhenNoSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTerminationProtection  **
  - **IAM action:**  [elasticmapreduce:SetTerminationProtection](#list_emr-action-SetTerminationProtection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetUnhealthyNodeReplacement  **
  - **IAM action:**  [elasticmapreduce:SetUnhealthyNodeReplacement](#list_emr-action-SetUnhealthyNodeReplacement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetVisibleToAllUsers  **
  - **IAM action:**  [elasticmapreduce:SetVisibleToAllUsers](#list_emr-action-SetVisibleToAllUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNotebookExecution  **
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticmapreduce:StartNotebookExecution](#list_emr-action-StartNotebookExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartSession  **
  - **IAM action:**  [elasticmapreduce:AddTags](#list_emr-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [elasticmapreduce:StartSession](#list_emr-action-StartSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** elasticmapreduce.amazonaws.com / **Access level:** Write

- **   StopNotebookExecution  **
  - **IAM action:**  [elasticmapreduce:StopNotebookExecution](#list_emr-action-StopNotebookExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateJobFlows  **
  - **IAM action:**  [elasticmapreduce:TerminateJobFlows](#list_emr-action-TerminateJobFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateSession  **
  - **IAM action:**  [elasticmapreduce:TerminateSession](#list_emr-action-TerminateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStudio  **
  - **IAM action:**  [elasticmapreduce:UpdateStudio](#list_emr-action-UpdateStudio)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateStudioSessionMapping  **
  - **IAM action:**  [elasticmapreduce:UpdateStudioSessionMapping](#list_emr-action-UpdateStudioSessionMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Elastic MapReduce
<a name="list_emr-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AccessAllEventLogs](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html)  **
  - **Description:** Grants permission to view all event logs in a persistent application history server
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddInstanceFleet](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddInstanceFleet.html)  **
  - **Description:** Grants permission to add an instance fleet to a running cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddInstanceGroups](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddInstanceGroups.html)  **
  - **Description:** Grants permission to add instance groups to a running cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddJobFlowSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddJobFlowSteps.html)  **
  - **Description:** Grants permission to add new steps to a running cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ExecutionRoleArn](#list_emr-elasticmapreduce_ExecutionRoleArn)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add tags to an Amazon EMR resource
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [editor](#list_emr-resource-editor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-execution](#list_emr-resource-notebook-execution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session](#list_emr-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [studio](#list_emr-resource-studio) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [CancelSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_CancelSteps.html)  **
  - **Description:** Grants permission to cancel a pending step or steps in a running cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePersistentAppUI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html)  **
  - **Description:** Grants permission to create a persistent application history server
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSecurityConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_CreateSecurityConfiguration.html)  **
  - **Description:** Grants permission to create a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateStudio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to create an EMR Studio
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)
  - **Access level:** Write

- **   [CreateStudioPresignedUrl](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to launch an EMR Studio using IAM authentication mode
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateStudioSessionMapping](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to create an EMR Studio session mapping
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_DeleteSecurityConfiguration.html)  **
  - **Description:** Grants permission to delete a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteStudio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to delete an EMR Studio
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStudioSessionMapping](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to delete an EMR Studio session mapping
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCluster](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeCluster.html)  **
  - **Description:** Grants permission to get details about a cluster, including status, hardware and software configuration, VPC settings, and so on
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeJobFlows.html)  **
  - **Description:** Grants permission to describe details of clusters (job flows). This API is deprecated and will eventually be removed. We recommend you use ListClusters, DescribeCluster, ListSteps, ListInstanceGroups and ListBootstrapActions instead
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotebookExecution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)  **
  - **Description:** Grants permission to view information about a notebook execution
  - **Resource types (\*required):** [notebook-execution\*](#list_emr-resource-notebook-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePersistentAppUI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html)  **
  - **Description:** Grants permission to describe a persistent application history server
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReleaseLabel](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeReleaseLabel.html)  **
  - **Description:** Grants permission to view information about an EMR release, such as which applications are supported
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSecurityConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeSecurityConfiguration.html)  **
  - **Description:** Grants permission to get details of a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStep](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeStep.html)  **
  - **Description:** Grants permission to get details about a cluster step
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStudio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to view information about an EMR Studio
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutoTerminationPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetAutoTerminationPolicy.html)  **
  - **Description:** Grants permission to retrieve the auto-termination policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlockPublicAccessConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetBlockPublicAccessConfiguration.html)  **
  - **Description:** Grants permission to retrieve the EMR block public access configuration for the AWS account in the Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetClusterSessionCredentials](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-steps-runtime-roles.html)  **
  - **Description:** Grants permission to retrieve HTTP basic credentials associated with a given execution IAM Role for a fine-grained access control enabled EMR Cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ExecutionRoleArn](#list_emr-elasticmapreduce_ExecutionRoleArn)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetManagedScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetManagedScalingPolicy.html)  **
  - **Description:** Grants permission to retrieve the managed scaling policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOnClusterAppUIPresignedURL](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html)  **
  - **Description:** Grants permission to get a presigned URL for an application history server running on the cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetPersistentAppUIPresignedURL](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html)  **
  - **Description:** Grants permission to get a presigned URL for a persistent application history server
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ExecutionRoleArn](#list_emr-elasticmapreduce_ExecutionRoleArn)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetSession](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetSession.html)  **
  - **Description:** Grants permission to get details of a Spark Connect session
  - **Resource types (\*required):** [session\*](#list_emr-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionEndpoint](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetSessionEndpoint.html)  **
  - **Description:** Grants permission to get the endpoint and credentials for a Spark Connect session
  - **Resource types (\*required):** [session\*](#list_emr-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetStudioSessionMapping](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to view information about an EMR Studio session mapping
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBootstrapActions](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListBootstrapActions.html)  **
  - **Description:** Grants permission to get details about the bootstrap actions associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListClusters](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to get the status of accessible clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInstanceFleets](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstanceFleets.html)  **
  - **Description:** Grants permission to get details of instance fleets in a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInstanceGroups](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstanceGroups.html)  **
  - **Description:** Grants permission to get details of instance groups in a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInstances](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstances.html)  **
  - **Description:** Grants permission to get details about the Amazon EC2 instances in a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListNotebookExecutions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)  **
  - **Description:** Grants permission to list summary information for notebook executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReleaseLabels](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListReleaseLabels.html)  **
  - **Description:** Grants permission to list and filter the available EMR releases in the current region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSecurityConfigurations](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSecurityConfigurations.html)  **
  - **Description:** Grants permission to list available security configurations in this account by name, along with creation dates and times
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list Spark Connect sessions on an Amazon EMR cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSteps.html)  **
  - **Description:** Grants permission to list steps associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListStudioSessionMappings](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to list summary information about EMR Studio session mappings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStudios](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to list summary information about EMR Studios
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSupportedInstanceTypes](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSupportedInstanceTypes.html)  **
  - **Description:** Grants permission to list the Amazon EC2 instance types that an Amazon EMR release supports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ModifyCluster](https://docs.aws.amazon.com/emr/latest/APIReference/API_ModifyCluster.html)  **
  - **Description:** Grants permission to change cluster settings such as number of steps that can be executed concurrently for a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyInstanceFleet](https://docs.aws.amazon.com/emr/latest/APIReference/API_ModifyInstanceFleet.html)  **
  - **Description:** Grants permission to change the target On-Demand and target Spot capacities for a instance fleet
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyInstanceGroups](https://docs.aws.amazon.com/emr/latest/APIReference/API_ModifyInstanceGroups.html)  **
  - **Description:** Grants permission to change the number and configuration of EC2 instances for an instance group
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutAutoScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_PutAutoScalingPolicy.html)  **
  - **Description:** Grants permission to create or update an automatic scaling policy for a core instance group or task instance group
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutAutoTerminationPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_PutAutoTerminationPolicy.html)  **
  - **Description:** Grants permission to create or update the auto-termination policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutBlockPublicAccessConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_PutBlockPublicAccessConfiguration.html)  **
  - **Description:** Grants permission to create or update the EMR block public access configuration for the AWS account in the Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [PutManagedScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_PutManagedScalingPolicy.html)  **
  - **Description:** Grants permission to create or update the managed scaling policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveAutoScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_RemoveAutoScalingPolicy.html)  **
  - **Description:** Grants permission to remove an automatic scaling policy from an instance group
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveAutoTerminationPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_RemoveAutoTerminationPolicy.html)  **
  - **Description:** Grants permission to remove the auto-termination policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveManagedScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_RemoveManagedScalingPolicy.html)  **
  - **Description:** Grants permission to remove the managed scaling policy associated with a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/emr/latest/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove tags from an Amazon EMR resource
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [editor](#list_emr-resource-editor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-execution](#list_emr-resource-notebook-execution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session](#list_emr-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [studio](#list_emr-resource-studio) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [RunJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html)  **
  - **Description:** Grants permission to create and launch a cluster (job flow)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)
  - **Access level:** Write

- **   [SetKeepJobFlowAliveWhenNoSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_SetKeepJobFlowAliveWhenNoSteps.html)  **
  - **Description:** Grants permission to add and remove auto terminate after step execution for a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetTerminationProtection](https://docs.aws.amazon.com/emr/latest/APIReference/API_SetTerminationProtection.html)  **
  - **Description:** Grants permission to add and remove termination protection for a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetUnhealthyNodeReplacement](https://docs.aws.amazon.com/emr/latest/APIReference/API_SetUnhealthyNodeReplacement.html)  **
  - **Description:** Grants permission to enable or disable unhealthy node replacement for a cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetVisibleToAllUsers](https://docs.aws.amazon.com/emr/latest/APIReference/API_SetVisibleToAllUsers.html)  **
  - **Description:** Grants permission to set whether all AWS Identity and Access Management (IAM) users in the AWS account can view a cluster. This API is deprecated and your cluster may be visible to all users in your account. To restrict cluster access using an IAM policy, see AWS Identity and Access Management for Amazon EMR (https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html)
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNotebookExecution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)  **
  - **Description:** Grants permission to start an EMR notebook execution
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSession](https://docs.aws.amazon.com/emr/latest/APIReference/API_StartSession.html)  **
  - **Description:** Grants permission to start a Spark Connect session on an Amazon EMR cluster
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:ExecutionRoleArn](#list_emr-elasticmapreduce_ExecutionRoleArn)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopNotebookExecution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)  **
  - **Description:** Grants permission to stop notebook execution
  - **Resource types (\*required):** [notebook-execution\*](#list_emr-resource-notebook-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_TerminateJobFlows.html)  **
  - **Description:** Grants permission to terminate a cluster (job flow)
  - **Resource types (\*required):** [cluster\*](#list_emr-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateSession](https://docs.aws.amazon.com/emr/latest/APIReference/API_TerminateSession.html)  **
  - **Description:** Grants permission to terminate a Spark Connect session on an Amazon EMR cluster
  - **Resource types (\*required):** [session\*](#list_emr-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStudio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to update information about an EMR Studio
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStudioSessionMapping](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  **
  - **Description:** Grants permission to update an EMR Studio session mapping
  - **Resource types (\*required):** [studio\*](#list_emr-resource-studio)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Elastic MapReduce
<a name="list_emr-permission-only-actions"></a>

The following actions are defined by Amazon Elastic MapReduce but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AttachEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to attach an EMR notebook to a compute engine
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-create.html)  **
  - **Description:** Grants permission to create an EMR notebook
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_emr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_emr-aws_TagKeys)<br />[elasticmapreduce:RequestTag/${TagKey}](#list_emr-elasticmapreduce_RequestTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to create an EMR notebook repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-deleting)  **
  - **Description:** Grants permission to delete an EMR notebook
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to delete an EMR notebook repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWorkspaceAccess](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to block an identity from opening a collaborative workspace
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to view information about a notebook, including status, user, role, tags, location, and more
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to describe an EMR notebook repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetachEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to detach an EMR notebook from a compute engine
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LinkRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to link an EMR notebook repository to EMR notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListEditors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to list summary information for accessible EMR notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to list existing EMR notebook repositories
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkspaceAccessIdentities](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to list identities that are granted access to a workspace
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** List

- **   [OpenEditorInConsole](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to launch the Jupyter notebook editor for an EMR notebook from within the console
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutWorkspaceAccess](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to allow an identity to open a collaborative workspace
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [StartEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to start an EMR notebook
  - **Resource types (\*required):** [cluster](#list_emr-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html)  **
  - **Description:** Grants permission to shut down an EMR notebook
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UnlinkRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to unlink an EMR notebook repository from EMR notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html)  **
  - **Description:** Grants permission to update an EMR notebook
  - **Resource types (\*required):** [editor\*](#list_emr-resource-editor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor)  **
  - **Description:** Grants permission to update an EMR notebook repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ViewEventsFromAllClustersInConsole](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticmapreduce.html)  **
  - **Description:** Grants permission to use the EMR console to view events from all clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by Amazon Elastic MapReduce
<a name="list_emr-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html)  | arn:${Partition}:elasticmapreduce:${Region}:${Account}:cluster/${ClusterId} | [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_) | 
|  [editor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html)  | arn:${Partition}:elasticmapreduce:${Region}:${Account}:editor/${EditorId} | [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_) | 
|  [notebook-execution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html)  | arn:${Partition}:elasticmapreduce:${Region}:${Account}:notebook-execution/${NotebookExecutionId} | [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html)  | arn:${Partition}:elasticmapreduce:${Region}:${Account}:cluster/${ClusterId}/session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_) | 
|  [studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html)  | arn:${Partition}:elasticmapreduce:${Region}:${Account}:studio/${StudioId} | [aws:ResourceTag/${TagKey}](#list_emr-aws_ResourceTag___TagKey_)<br />[elasticmapreduce:ResourceTag/${TagKey}](#list_emr-elasticmapreduce_ResourceTag___TagKey_) | 

## Condition keys for Amazon Elastic MapReduce
<a name="list_emr-policy-keys"></a>

Amazon Elastic MapReduce defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-fine-grained-cluster-access)  | Filters access by whether the tag and value pair is provided with the action | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-fine-grained-cluster-access)  | Filters access by the tag and value pair associated with an Amazon EMR resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-fine-grained-cluster-access)  | Filters access by whether the tag keys are provided with the action regardless of tag value | ArrayOfString | 
|   [elasticmapreduce:ExecutionRoleArn](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-security)  | Filters access by whether the execution role ARN is provided with the action | ARN | 
|   [elasticmapreduce:RequestTag/${TagKey}](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-fine-grained-cluster-access)  | Filters access by whether the tag and value pair is provided with the action | String | 
|   [elasticmapreduce:ResourceTag/${TagKey}](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-iam.html#emr-fine-grained-cluster-access)  | Filters access by the tag and value pair associated with an Amazon EMR resource | String | 