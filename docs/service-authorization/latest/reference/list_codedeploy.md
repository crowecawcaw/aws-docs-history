

# Actions, resources, and condition keys for AWS CodeDeploy
<a name="list_codedeploy"></a>

AWS CodeDeploy (service prefix: `codedeploy`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codedeploy/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codedeploy/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codedeploy/codedeploy.json) for this service.

**Topics**
+ [API operations defined by AWS CodeDeploy](#list_codedeploy-operations)
+ [Actions defined by AWS CodeDeploy](#list_codedeploy-actions-as-permissions)
+ [Permission-only actions for AWS CodeDeploy](#list_codedeploy-permission-only-actions)
+ [Resource types defined by AWS CodeDeploy](#list_codedeploy-resources-for-iam-policies)
+ [Condition keys for AWS CodeDeploy](#list_codedeploy-policy-keys)

## API operations defined by AWS CodeDeploy
<a name="list_codedeploy-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codedeploy-actions-as-permissions).




- **   AddTagsToOnPremisesInstances  **
  - **IAM action:**  [codedeploy:AddTagsToOnPremisesInstances](#list_codedeploy-action-AddTagsToOnPremisesInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   BatchGetApplicationRevisions  **
  - **IAM action:**  [codedeploy:BatchGetApplicationRevisions](#list_codedeploy-action-BatchGetApplicationRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetApplications  **
  - **IAM action:**  [codedeploy:BatchGetApplications](#list_codedeploy-action-BatchGetApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetDeploymentGroups  **
  - **IAM action:**  [codedeploy:BatchGetDeploymentGroups](#list_codedeploy-action-BatchGetDeploymentGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetDeploymentInstances  **
  - **IAM action:**  [codedeploy:BatchGetDeploymentInstances](#list_codedeploy-action-BatchGetDeploymentInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetDeploymentTargets  **
  - **IAM action:**  [codedeploy:BatchGetDeploymentTargets](#list_codedeploy-action-BatchGetDeploymentTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetDeployments  **
  - **IAM action:**  [codedeploy:BatchGetDeployments](#list_codedeploy-action-BatchGetDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetOnPremisesInstances  **
  - **IAM action:**  [codedeploy:BatchGetOnPremisesInstances](#list_codedeploy-action-BatchGetOnPremisesInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ContinueDeployment  **
  - **IAM action:**  [codedeploy:ContinueDeployment](#list_codedeploy-action-ContinueDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:CreateCloudFormationDeployment](#list_codedeploy-action-CreateCloudFormationDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [codedeploy:CreateApplication](#list_codedeploy-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:TagResource](#list_codedeploy-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDeployment  **
  - **IAM action:**  [codedeploy:CreateDeployment](#list_codedeploy-action-CreateDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:GetApplicationRevision](#list_codedeploy-action-GetApplicationRevision)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codedeploy:GetDeploymentConfig](#list_codedeploy-action-GetDeploymentConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [codedeploy:RegisterApplicationRevision](#list_codedeploy-action-RegisterApplicationRevision)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:UpdateDeploymentGroup](#list_codedeploy-action-UpdateDeploymentGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDeploymentConfig  **
  - **IAM action:**  [codedeploy:CreateDeploymentConfig](#list_codedeploy-action-CreateDeploymentConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDeploymentGroup  **
  - **IAM action:**  [codedeploy:CreateDeploymentGroup](#list_codedeploy-action-CreateDeploymentGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:TagResource](#list_codedeploy-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codedeploy.amazonaws.com / **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [codedeploy:DeleteApplication](#list_codedeploy-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeploymentConfig  **
  - **IAM action:**  [codedeploy:DeleteDeploymentConfig](#list_codedeploy-action-DeleteDeploymentConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeploymentGroup  **
  - **IAM action:**  [codedeploy:DeleteDeploymentGroup](#list_codedeploy-action-DeleteDeploymentGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGitHubAccountToken  **
  - **IAM action:**  [codedeploy:DeleteGitHubAccountToken](#list_codedeploy-action-DeleteGitHubAccountToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcesByExternalId  **
  - **IAM action:**  [codedeploy:DeleteResourcesByExternalId](#list_codedeploy-action-DeleteResourcesByExternalId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterOnPremisesInstance  **
  - **IAM action:**  [codedeploy:DeregisterOnPremisesInstance](#list_codedeploy-action-DeregisterOnPremisesInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [codedeploy:GetApplication](#list_codedeploy-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetApplicationRevision  **
  - **IAM action:**  [codedeploy:GetApplicationRevision](#list_codedeploy-action-GetApplicationRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeployment  **
  - **IAM action:**  [codedeploy:GetDeployment](#list_codedeploy-action-GetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeploymentConfig  **
  - **IAM action:**  [codedeploy:GetDeploymentConfig](#list_codedeploy-action-GetDeploymentConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeploymentGroup  **
  - **IAM action:**  [codedeploy:GetDeploymentGroup](#list_codedeploy-action-GetDeploymentGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeploymentInstance  **
  - **IAM action:**  [codedeploy:GetDeploymentInstance](#list_codedeploy-action-GetDeploymentInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeploymentTarget  **
  - **IAM action:**  [codedeploy:GetDeploymentTarget](#list_codedeploy-action-GetDeploymentTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOnPremisesInstance  **
  - **IAM action:**  [codedeploy:GetOnPremisesInstance](#list_codedeploy-action-GetOnPremisesInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplicationRevisions  **
  - **IAM action:**  [codedeploy:ListApplicationRevisions](#list_codedeploy-action-ListApplicationRevisions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApplications  **
  - **IAM action:**  [codedeploy:ListApplications](#list_codedeploy-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentConfigs  **
  - **IAM action:**  [codedeploy:ListDeploymentConfigs](#list_codedeploy-action-ListDeploymentConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentGroups  **
  - **IAM action:**  [codedeploy:ListDeploymentGroups](#list_codedeploy-action-ListDeploymentGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentInstances  **
  - **IAM action:**  [codedeploy:ListDeploymentInstances](#list_codedeploy-action-ListDeploymentInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentTargets  **
  - **IAM action:**  [codedeploy:ListDeploymentTargets](#list_codedeploy-action-ListDeploymentTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **IAM action:**  [codedeploy:ListDeployments](#list_codedeploy-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGitHubAccountTokenNames  **
  - **IAM action:**  [codedeploy:ListGitHubAccountTokenNames](#list_codedeploy-action-ListGitHubAccountTokenNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOnPremisesInstances  **
  - **IAM action:**  [codedeploy:ListOnPremisesInstances](#list_codedeploy-action-ListOnPremisesInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codedeploy:ListTagsForResource](#list_codedeploy-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutLifecycleEventHookExecutionStatus  **
  - **IAM action:**  [codedeploy:CreateCloudFormationDeployment](#list_codedeploy-action-CreateCloudFormationDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:PutLifecycleEventHookExecutionStatus](#list_codedeploy-action-PutLifecycleEventHookExecutionStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RegisterApplicationRevision  **
  - **IAM action:**  [codedeploy:RegisterApplicationRevision](#list_codedeploy-action-RegisterApplicationRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterOnPremisesInstance  **
  - **IAM action:**  [codedeploy:RegisterOnPremisesInstance](#list_codedeploy-action-RegisterOnPremisesInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromOnPremisesInstances  **
  - **IAM action:**  [codedeploy:RemoveTagsFromOnPremisesInstances](#list_codedeploy-action-RemoveTagsFromOnPremisesInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   SkipWaitTimeForInstanceTermination  **
  - **IAM action:**  [codedeploy:CreateCloudFormationDeployment](#list_codedeploy-action-CreateCloudFormationDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:SkipWaitTimeForInstanceTermination](#list_codedeploy-action-SkipWaitTimeForInstanceTermination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StopDeployment  **
  - **IAM action:**  [codedeploy:CreateCloudFormationDeployment](#list_codedeploy-action-CreateCloudFormationDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codedeploy:StopDeployment](#list_codedeploy-action-StopDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codedeploy:TagResource](#list_codedeploy-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codedeploy:UntagResource](#list_codedeploy-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateApplication  **
  - **IAM action:**  [codedeploy:UpdateApplication](#list_codedeploy-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDeploymentGroup  **
  - **IAM action:**  [codedeploy:UpdateDeploymentGroup](#list_codedeploy-action-UpdateDeploymentGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codedeploy.amazonaws.com / **Access level:** Write



## Actions defined by AWS CodeDeploy
<a name="list_codedeploy-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTagsToOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AddTagsToOnPremisesInstances.html)  **
  - **Description:** Grants permission to add tags to one or more on-premises instances
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [BatchGetApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplicationRevisions.html)  **
  - **Description:** Grants permission to get information about one or more application revisions
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplications.html)  **
  - **Description:** Grants permission to get information about multiple applications associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentGroups.html)  **
  - **Description:** Grants permission to get information about one or more deployment groups
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentInstances.html)  **
  - **Description:** Grants permission to get information about one or more instance that are part of a deployment group
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentTargets.html)  **
  - **Description:** Grants permission to return an array of one or more targets associated with a deployment. This method works with all compute types and should be used instead of the deprecated BatchGetDeploymentInstances. The maximum number of targets that can be returned is 25
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeployments.html)  **
  - **Description:** Grants permission to get information about multiple deployments associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetOnPremisesInstances.html)  **
  - **Description:** Grants permission to get information about one or more on-premises instances
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ContinueDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html)  **
  - **Description:** Grants permission to start the process of rerouting traffic from instances in the original environment to instances in thereplacement environment without waiting for a specified wait time to elapse
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codedeploy-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to create a deployment for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentConfig.html)  **
  - **Description:** Grants permission to create a custom deployment configuration associated with the IAM user
  - **Resource types (\*required):** [deploymentconfig\*](#list_codedeploy-resource-deploymentconfig)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentGroup.html)  **
  - **Description:** Grants permission to create a deployment group for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codedeploy-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentConfig.html)  **
  - **Description:** Grants permission to delete a custom deployment configuration associated with the IAM user
  - **Resource types (\*required):** [deploymentconfig\*](#list_codedeploy-resource-deploymentconfig)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentGroup.html)  **
  - **Description:** Grants permission to delete a deployment group for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGitHubAccountToken](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteGitHubAccountToken.html)  **
  - **Description:** Grants permission to delete a GitHub account connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcesByExternalId](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteResourcesByExternalId.html)  **
  - **Description:** Grants permission to delete resources associated with the given external Id
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeregisterOnPremisesInstance.html)  **
  - **Description:** Grants permission to deregister an on-premises instance
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to get information about a single application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetApplicationRevision](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplicationRevision.html)  **
  - **Description:** Grants permission to get information about a single application revision for an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to get information about a single deployment to a deployment group for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentConfig.html)  **
  - **Description:** Grants permission to get information about a single deployment configuration associated with the IAM user
  - **Resource types (\*required):** [deploymentconfig\*](#list_codedeploy-resource-deploymentconfig)
  - **Condition keys:**  
  - **Access level:** List

- **   [GetDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentGroup.html)  **
  - **Description:** Grants permission to get information about a single deployment group for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDeploymentInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentInstance.html)  **
  - **Description:** Grants permission to get information about a single instance in a deployment associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html)  **
  - **Description:** Grants permission to return information about a deployment target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetOnPremisesInstance.html)  **
  - **Description:** Grants permission to get information about a single on-premises instance
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplicationRevisions.html)  **
  - **Description:** Grants permission to get information about all application revisions for an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to get information about all applications associated with the IAM user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeploymentConfigs](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentConfigs.html)  **
  - **Description:** Grants permission to get information about all deployment configurations associated with the IAM user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentGroups.html)  **
  - **Description:** Grants permission to get information about all deployment groups for an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeploymentInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentInstances.html)  **
  - **Description:** Grants permission to get information about all instances in a deployment associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentTargets.html)  **
  - **Description:** Grants permission to return an array of target IDs that are associated a deployment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to get information about all deployments to a deployment group associated with the IAM user, or to get all deployments associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGitHubAccountTokenNames](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListGitHubAccountTokenNames.html)  **
  - **Description:** Grants permission to list the names of stored connections to GitHub accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListOnPremisesInstances.html)  **
  - **Description:** Grants permission to get a list of one or more on-premises instance names
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for the resource identified by a specified ARN. Tags are used to organize and categorize your CodeDeploy resources
  - **Resource types (\*required):** [application](#list_codedeploy-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deploymentgroup](#list_codedeploy-resource-deploymentgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutLifecycleEventHookExecutionStatus](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_PutLifecycleEventHookExecutionStatus.html)  **
  - **Description:** Grants permission to notify a lifecycle event hook execution status for associated deployment with the IAM user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterApplicationRevision](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterApplicationRevision.html)  **
  - **Description:** Grants permission to register information about an application revision for an application associated with the IAM user
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterOnPremisesInstance](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterOnPremisesInstance.html)  **
  - **Description:** Grants permission to register an on-premises instance
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveTagsFromOnPremisesInstances](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RemoveTagsFromOnPremisesInstances.html)  **
  - **Description:** Grants permission to remove tags from one or more on-premises instances
  - **Resource types (\*required):** [instance\*](#list_codedeploy-resource-instance)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [SkipWaitTimeForInstanceTermination](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_SkipWaitTimeForInstanceTermination.html)  **
  - **Description:** Grants permission to override any specified wait time and starts terminating instances immediately after the traffic routing is complete. This action applies to blue-green deployments only
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_StopDeployment.html)  **
  - **Description:** Grants permission to stop a deployment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to associate the list of tags in the input Tags parameter with the resource identified by the ResourceArn input parameter
  - **Resource types (\*required):** [application](#list_codedeploy-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codedeploy-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Resource types (\*required):** [deploymentgroup](#list_codedeploy-resource-deploymentgroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codedeploy-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to disassociate a resource from a list of tags. The resource is identified by the ResourceArn input parameter. The tags are identfied by the list of keys in the TagKeys input parameter
  - **Resource types (\*required):** [application](#list_codedeploy-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Resource types (\*required):** [deploymentgroup](#list_codedeploy-resource-deploymentgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codedeploy-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application
  - **Resource types (\*required):** [application\*](#list_codedeploy-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateDeploymentGroup.html)  **
  - **Description:** Grants permission to change information about a single deployment group for an application associated with the IAM user
  - **Resource types (\*required):** [deploymentgroup\*](#list_codedeploy-resource-deploymentgroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS CodeDeploy
<a name="list_codedeploy-permission-only-actions"></a>

The following actions are defined by AWS CodeDeploy but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateCloudFormationDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/codedeploy/latest/userguide/deployments-create-ecs-cfn.html)  | Grants permission to create CloudFormation deployment to cooperate ochestration for a CloudFormation stack update |  |   | Write | 

## Resource types defined by AWS CodeDeploy
<a name="list_codedeploy-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html)  | arn:${Partition}:codedeploy:${Region}:${Account}:application:${ApplicationName} | [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_) | 
|  [deploymentconfig](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html)  | arn:${Partition}:codedeploy:${Region}:${Account}:deploymentconfig:${DeploymentConfigurationName} |   | 
|  [deploymentgroup](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html)  | arn:${Partition}:codedeploy:${Region}:${Account}:deploymentgroup:${ApplicationName}/${DeploymentGroupName} | [aws:ResourceTag/${TagKey}](#list_codedeploy-aws_ResourceTag___TagKey_) | 
|  [instance](https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control-permissions-reference.html)  | arn:${Partition}:codedeploy:${Region}:${Account}:instance:${InstanceName} |   | 

## Condition keys for AWS CodeDeploy
<a name="list_codedeploy-policy-keys"></a>

AWS CodeDeploy defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 