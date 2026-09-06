

# Actions, resources, and condition keys for AWS CodeBuild
<a name="list_codebuild"></a>

AWS CodeBuild (service prefix: `codebuild`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codebuild/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codebuild/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codebuild/codebuild.json) for this service.

**Topics**
+ [API operations defined by AWS CodeBuild](#list_codebuild-operations)
+ [Actions defined by AWS CodeBuild](#list_codebuild-actions-as-permissions)
+ [Permission-only actions for AWS CodeBuild](#list_codebuild-permission-only-actions)
+ [Resource types defined by AWS CodeBuild](#list_codebuild-resources-for-iam-policies)
+ [Condition keys for AWS CodeBuild](#list_codebuild-policy-keys)

## API operations defined by AWS CodeBuild
<a name="list_codebuild-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codebuild-actions-as-permissions).




- **   BatchDeleteBuilds  **
  - **IAM action:**  [codebuild:BatchDeleteBuilds](#list_codebuild-action-BatchDeleteBuilds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetBuildBatches  **
  - **IAM action:**  [codebuild:BatchGetBuildBatches](#list_codebuild-action-BatchGetBuildBatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetBuilds  **
  - **IAM action:**  [codebuild:BatchGetBuilds](#list_codebuild-action-BatchGetBuilds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCommandExecutions  **
  - **IAM action:**  [codebuild:BatchGetCommandExecutions](#list_codebuild-action-BatchGetCommandExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetFleets  **
  - **IAM action:**  [codebuild:BatchGetFleets](#list_codebuild-action-BatchGetFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetProjects  **
  - **IAM action:**  [codebuild:BatchGetProjects](#list_codebuild-action-BatchGetProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetReportGroups  **
  - **IAM action:**  [codebuild:BatchGetReportGroups](#list_codebuild-action-BatchGetReportGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetReports  **
  - **IAM action:**  [codebuild:BatchGetReports](#list_codebuild-action-BatchGetReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetSandboxes  **
  - **IAM action:**  [codebuild:BatchGetSandboxes](#list_codebuild-action-BatchGetSandboxes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateFleet  **
  - **IAM action:**  [codebuild:CreateFleet](#list_codebuild-action-CreateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [codebuild:CreateProject](#list_codebuild-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codebuild.amazonaws.com / **Access level:** Write

- **   CreateReportGroup  **
  - **IAM action:**  [codebuild:CreateReportGroup](#list_codebuild-action-CreateReportGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWebhook  **
  - **IAM action:**  [codebuild:CreateWebhook](#list_codebuild-action-CreateWebhook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBuildBatch  **
  - **IAM action:**  [codebuild:DeleteBuildBatch](#list_codebuild-action-DeleteBuildBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFleet  **
  - **IAM action:**  [codebuild:DeleteFleet](#list_codebuild-action-DeleteFleet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [codebuild:DeleteProject](#list_codebuild-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReport  **
  - **IAM action:**  [codebuild:DeleteReport](#list_codebuild-action-DeleteReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReportGroup  **
  - **IAM action:**  [codebuild:DeleteReportGroup](#list_codebuild-action-DeleteReportGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [codebuild:DeleteResourcePolicy](#list_codebuild-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteSourceCredentials  **
  - **IAM action:**  [codebuild:DeleteSourceCredentials](#list_codebuild-action-DeleteSourceCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebhook  **
  - **IAM action:**  [codebuild:DeleteWebhook](#list_codebuild-action-DeleteWebhook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCodeCoverages  **
  - **IAM action:**  [codebuild:DescribeCodeCoverages](#list_codebuild-action-DescribeCodeCoverages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTestCases  **
  - **IAM action:**  [codebuild:DescribeTestCases](#list_codebuild-action-DescribeTestCases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReportGroupTrend  **
  - **IAM action:**  [codebuild:GetReportGroupTrend](#list_codebuild-action-GetReportGroupTrend) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [codebuild:GetResourcePolicy](#list_codebuild-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportSourceCredentials  **
  - **IAM action:**  [codebuild:ImportSourceCredentials](#list_codebuild-action-ImportSourceCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvalidateProjectCache  **
  - **IAM action:**  [codebuild:InvalidateProjectCache](#list_codebuild-action-InvalidateProjectCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListBuildBatches  **
  - **IAM action:**  [codebuild:ListBuildBatches](#list_codebuild-action-ListBuildBatches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuildBatchesForProject  **
  - **IAM action:**  [codebuild:ListBuildBatchesForProject](#list_codebuild-action-ListBuildBatchesForProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuilds  **
  - **IAM action:**  [codebuild:ListBuilds](#list_codebuild-action-ListBuilds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuildsForProject  **
  - **IAM action:**  [codebuild:ListBuildsForProject](#list_codebuild-action-ListBuildsForProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCommandExecutionsForSandbox  **
  - **IAM action:**  [codebuild:ListCommandExecutionsForSandbox](#list_codebuild-action-ListCommandExecutionsForSandbox) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCuratedEnvironmentImages  **
  - **IAM action:**  [codebuild:ListCuratedEnvironmentImages](#list_codebuild-action-ListCuratedEnvironmentImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFleets  **
  - **IAM action:**  [codebuild:ListFleets](#list_codebuild-action-ListFleets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjects  **
  - **IAM action:**  [codebuild:ListProjects](#list_codebuild-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReportGroups  **
  - **IAM action:**  [codebuild:ListReportGroups](#list_codebuild-action-ListReportGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReports  **
  - **IAM action:**  [codebuild:ListReports](#list_codebuild-action-ListReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReportsForReportGroup  **
  - **IAM action:**  [codebuild:ListReportsForReportGroup](#list_codebuild-action-ListReportsForReportGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSandboxes  **
  - **IAM action:**  [codebuild:ListSandboxes](#list_codebuild-action-ListSandboxes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSandboxesForProject  **
  - **IAM action:**  [codebuild:ListSandboxesForProject](#list_codebuild-action-ListSandboxesForProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSharedProjects  **
  - **IAM action:**  [codebuild:ListSharedProjects](#list_codebuild-action-ListSharedProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSharedReportGroups  **
  - **IAM action:**  [codebuild:ListSharedReportGroups](#list_codebuild-action-ListSharedReportGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceCredentials  **
  - **IAM action:**  [codebuild:ListSourceCredentials](#list_codebuild-action-ListSourceCredentials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutResourcePolicy  **
  - **IAM action:**  [codebuild:PutResourcePolicy](#list_codebuild-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RetryBuild  **
  - **IAM action:**  [codebuild:RetryBuild](#list_codebuild-action-RetryBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetryBuildBatch  **
  - **IAM action:**  [codebuild:RetryBuildBatch](#list_codebuild-action-RetryBuildBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBuild  **
  - **IAM action:**  [codebuild:StartBuild](#list_codebuild-action-StartBuild)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codebuild.amazonaws.com / **Access level:** Write

- **   StartBuildBatch  **
  - **IAM action:**  [codebuild:StartBuildBatch](#list_codebuild-action-StartBuildBatch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codebuild.amazonaws.com / **Access level:** Write

- **   StartCommandExecution  **
  - **IAM action:**  [codebuild:StartCommandExecution](#list_codebuild-action-StartCommandExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSandbox  **
  - **IAM action:**  [codebuild:StartSandbox](#list_codebuild-action-StartSandbox) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSandboxConnection  **
  - **IAM action:**  [codebuild:StartSandboxConnection](#list_codebuild-action-StartSandboxConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBuild  **
  - **IAM action:**  [codebuild:StopBuild](#list_codebuild-action-StopBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBuildBatch  **
  - **IAM action:**  [codebuild:StopBuildBatch](#list_codebuild-action-StopBuildBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSandbox  **
  - **IAM action:**  [codebuild:StopSandbox](#list_codebuild-action-StopSandbox) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFleet  **
  - **IAM action:**  [codebuild:UpdateFleet](#list_codebuild-action-UpdateFleet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateProject  **
  - **IAM action:**  [codebuild:UpdateProject](#list_codebuild-action-UpdateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codebuild.amazonaws.com / **Access level:** Write

- **   UpdateProjectVisibility  **
  - **IAM action:**  [codebuild:UpdateProjectVisibility](#list_codebuild-action-UpdateProjectVisibility)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** codebuild.amazonaws.com / **Access level:** Write

- **   UpdateReportGroup  **
  - **IAM action:**  [codebuild:UpdateReportGroup](#list_codebuild-action-UpdateReportGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWebhook  **
  - **IAM action:**  [codebuild:UpdateWebhook](#list_codebuild-action-UpdateWebhook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS CodeBuild
<a name="list_codebuild-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDeleteBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchDeleteBuilds.html)  **
  - **Description:** Grants permission to delete one or more builds
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuildBatches.html)  **
  - **Description:** Grants permission to get information about one or more build batches
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuilds.html)  **
  - **Description:** Grants permission to get information about one or more builds
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCommandExecutions](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetCommandExecutions.html)  **
  - **Description:** Grants permission to get information about one or more command executions
  - **Resource types (\*required):** [sandbox\*](#list_codebuild-resource-sandbox)
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetFleets.html)  **
  - **Description:** Grants permission to return an array of the Fleet objects specified by the input parameter
  - **Resource types (\*required):** [fleet\*](#list_codebuild-resource-fleet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetProjects.html)  **
  - **Description:** Grants permission to get information about one or more build projects
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReportGroups.html)  **
  - **Description:** Grants permission to return an array of ReportGroup objects that are specified by the input reportGroupArns parameter
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReports.html)  **
  - **Description:** Grants permission to return an array of the Report objects specified by the input reportArns parameter
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetSandboxes.html)  **
  - **Description:** Grants permission to get information about one or more sandboxes
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateFleet.html)  **
  - **Description:** Grants permission to create a compute fleet
  - **Resource types (\*required):** [fleet\*](#list_codebuild-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:computeConfiguration](#list_codebuild-codebuild_computeConfiguration)<br />[codebuild:computeConfiguration.disk](#list_codebuild-codebuild_computeConfiguration.disk)<br />[codebuild:computeConfiguration.instanceType](#list_codebuild-codebuild_computeConfiguration.instanceType)<br />[codebuild:computeConfiguration.machineType](#list_codebuild-codebuild_computeConfiguration.machineType)<br />[codebuild:computeConfiguration.memory](#list_codebuild-codebuild_computeConfiguration.memory)<br />[codebuild:computeConfiguration.vCpu](#list_codebuild-codebuild_computeConfiguration.vCpu)<br />[codebuild:computeType](#list_codebuild-codebuild_computeType)<br />[codebuild:environmentType](#list_codebuild-codebuild_environmentType)<br />[codebuild:fleetServiceRole](#list_codebuild-codebuild_fleetServiceRole)<br />[codebuild:imageId](#list_codebuild-codebuild_imageId)<br />[codebuild:vpcConfig](#list_codebuild-codebuild_vpcConfig)<br />[codebuild:vpcConfig.securityGroupIds](#list_codebuild-codebuild_vpcConfig.securityGroupIds)<br />[codebuild:vpcConfig.subnets](#list_codebuild-codebuild_vpcConfig.subnets)<br />[codebuild:vpcConfig.vpcId](#list_codebuild-codebuild_vpcConfig.vpcId)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a build project
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:artifacts](#list_codebuild-codebuild_artifacts)<br />[codebuild:artifacts.bucketOwnerAccess](#list_codebuild-codebuild_artifacts.bucketOwnerAccess)<br />[codebuild:artifacts.encryptionDisabled](#list_codebuild-codebuild_artifacts.encryptionDisabled)<br />[codebuild:artifacts.location](#list_codebuild-codebuild_artifacts.location)<br />[codebuild:autoRetryLimit](#list_codebuild-codebuild_autoRetryLimit)<br />[codebuild:buildBatchConfig](#list_codebuild-codebuild_buildBatchConfig)<br />[codebuild:buildBatchConfig.restrictions.computeTypesAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.computeTypesAllowed)<br />[codebuild:buildBatchConfig.restrictions.fleetsAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.fleetsAllowed)<br />[codebuild:buildBatchConfig.serviceRole](#list_codebuild-codebuild_buildBatchConfig.serviceRole)<br />[codebuild:cache](#list_codebuild-codebuild_cache)<br />[codebuild:cache.location](#list_codebuild-codebuild_cache.location)<br />[codebuild:cache.modes](#list_codebuild-codebuild_cache.modes)<br />[codebuild:cache.type](#list_codebuild-codebuild_cache.type)<br />[codebuild:concurrentBuildLimit](#list_codebuild-codebuild_concurrentBuildLimit)<br />[codebuild:encryptionKey](#list_codebuild-codebuild_encryptionKey)<br />[codebuild:environment](#list_codebuild-codebuild_environment)<br />[codebuild:environment.certificate](#list_codebuild-codebuild_environment.certificate)<br />[codebuild:environment.computeConfiguration](#list_codebuild-codebuild_environment.computeConfiguration)<br />[codebuild:environment.computeConfiguration.disk](#list_codebuild-codebuild_environment.computeConfiguration.disk)<br />[codebuild:environment.computeConfiguration.instanceType](#list_codebuild-codebuild_environment.computeConfiguration.instanceType)<br />[codebuild:environment.computeConfiguration.machineType](#list_codebuild-codebuild_environment.computeConfiguration.machineType)<br />[codebuild:environment.computeConfiguration.memory](#list_codebuild-codebuild_environment.computeConfiguration.memory)<br />[codebuild:environment.computeConfiguration.vCpu](#list_codebuild-codebuild_environment.computeConfiguration.vCpu)<br />[codebuild:environment.computeType](#list_codebuild-codebuild_environment.computeType)<br />[codebuild:environment.environmentVariables](#list_codebuild-codebuild_environment.environmentVariables)<br />[codebuild:environment.environmentVariables.name](#list_codebuild-codebuild_environment.environmentVariables.name)<br />[codebuild:environment.environmentVariables.value](#list_codebuild-codebuild_environment.environmentVariables.value)<br />[codebuild:environment.environmentVariables/${name}.value](#list_codebuild-codebuild_environment.environmentVariables___name_.value)<br />[codebuild:environment.fleet.fleetArn](#list_codebuild-codebuild_environment.fleet.fleetArn)<br />[codebuild:environment.image](#list_codebuild-codebuild_environment.image)<br />[codebuild:environment.imagePullCredentialsType](#list_codebuild-codebuild_environment.imagePullCredentialsType)<br />[codebuild:environment.privilegedMode](#list_codebuild-codebuild_environment.privilegedMode)<br />[codebuild:environment.registryCredential](#list_codebuild-codebuild_environment.registryCredential)<br />[codebuild:environment.registryCredential.credential](#list_codebuild-codebuild_environment.registryCredential.credential)<br />[codebuild:environment.registryCredential.credentialProvider](#list_codebuild-codebuild_environment.registryCredential.credentialProvider)<br />[codebuild:environment.type](#list_codebuild-codebuild_environment.type)<br />[codebuild:fileSystemLocations.identifier](#list_codebuild-codebuild_fileSystemLocations.identifier)<br />[codebuild:fileSystemLocations.location](#list_codebuild-codebuild_fileSystemLocations.location)<br />[codebuild:fileSystemLocations.type](#list_codebuild-codebuild_fileSystemLocations.type)<br />[codebuild:fileSystemLocations/${identifier}.location](#list_codebuild-codebuild_fileSystemLocations___identifier_.location)<br />[codebuild:fileSystemLocations/${identifier}.type](#list_codebuild-codebuild_fileSystemLocations___identifier_.type)<br />[codebuild:logsConfig](#list_codebuild-codebuild_logsConfig)<br />[codebuild:logsConfig.s3Logs](#list_codebuild-codebuild_logsConfig.s3Logs)<br />[codebuild:logsConfig.s3Logs.bucketOwnerAccess](#list_codebuild-codebuild_logsConfig.s3Logs.bucketOwnerAccess)<br />[codebuild:logsConfig.s3Logs.encryptionDisabled](#list_codebuild-codebuild_logsConfig.s3Logs.encryptionDisabled)<br />[codebuild:logsConfig.s3Logs.location](#list_codebuild-codebuild_logsConfig.s3Logs.location)<br />[codebuild:logsConfig.s3Logs.status](#list_codebuild-codebuild_logsConfig.s3Logs.status)<br />[codebuild:secondaryArtifacts](#list_codebuild-codebuild_secondaryArtifacts)<br />[codebuild:secondaryArtifacts.artifactIdentifier](#list_codebuild-codebuild_secondaryArtifacts.artifactIdentifier)<br />[codebuild:secondaryArtifacts.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts.encryptionDisabled)<br />[codebuild:secondaryArtifacts.location](#list_codebuild-codebuild_secondaryArtifacts.location)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.encryptionDisabled)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.location](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.location)<br />[codebuild:secondarySources](#list_codebuild-codebuild_secondarySources)<br />[codebuild:secondarySources.auth.resource](#list_codebuild-codebuild_secondarySources.auth.resource)<br />[codebuild:secondarySources.auth.type](#list_codebuild-codebuild_secondarySources.auth.type)<br />[codebuild:secondarySources.buildspec](#list_codebuild-codebuild_secondarySources.buildspec)<br />[codebuild:secondarySources.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources.buildStatusConfig.context)<br />[codebuild:secondarySources.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources.insecureSsl](#list_codebuild-codebuild_secondarySources.insecureSsl)<br />[codebuild:secondarySources.location](#list_codebuild-codebuild_secondarySources.location)<br />[codebuild:secondarySources.sourceIdentifier](#list_codebuild-codebuild_secondarySources.sourceIdentifier)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.resource](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.resource)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.type](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.type)<br />[codebuild:secondarySources/${sourceIdentifier}.buildspec](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildspec)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.context)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources/${sourceIdentifier}.insecureSsl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.insecureSsl)<br />[codebuild:secondarySources/${sourceIdentifier}.location](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.location)<br />[codebuild:serviceRole](#list_codebuild-codebuild_serviceRole)<br />[codebuild:source](#list_codebuild-codebuild_source)<br />[codebuild:source.auth.resource](#list_codebuild-codebuild_source.auth.resource)<br />[codebuild:source.auth.type](#list_codebuild-codebuild_source.auth.type)<br />[codebuild:source.buildspec](#list_codebuild-codebuild_source.buildspec)<br />[codebuild:source.buildStatusConfig.context](#list_codebuild-codebuild_source.buildStatusConfig.context)<br />[codebuild:source.buildStatusConfig.targetUrl](#list_codebuild-codebuild_source.buildStatusConfig.targetUrl)<br />[codebuild:source.insecureSsl](#list_codebuild-codebuild_source.insecureSsl)<br />[codebuild:source.location](#list_codebuild-codebuild_source.location)<br />[codebuild:vpcConfig](#list_codebuild-codebuild_vpcConfig)<br />[codebuild:vpcConfig.securityGroupIds](#list_codebuild-codebuild_vpcConfig.securityGroupIds)<br />[codebuild:vpcConfig.subnets](#list_codebuild-codebuild_vpcConfig.subnets)<br />[codebuild:vpcConfig.vpcId](#list_codebuild-codebuild_vpcConfig.vpcId)
  - **Access level:** Write

- **   [CreateReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateReportGroup.html)  **
  - **Description:** Grants permission to create a report group
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:exportConfig.s3Destination.bucket](#list_codebuild-codebuild_exportConfig.s3Destination.bucket)<br />[codebuild:exportConfig.s3Destination.bucketOwner](#list_codebuild-codebuild_exportConfig.s3Destination.bucketOwner)<br />[codebuild:exportConfig.s3Destination.encryptionDisabled](#list_codebuild-codebuild_exportConfig.s3Destination.encryptionDisabled)<br />[codebuild:exportConfig.s3Destination.encryptionKey](#list_codebuild-codebuild_exportConfig.s3Destination.encryptionKey)<br />[codebuild:exportConfig.s3Destination.path](#list_codebuild-codebuild_exportConfig.s3Destination.path)
  - **Access level:** Write

- **   [CreateWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateWebhook.html)  **
  - **Description:** Grants permission to create webhook. For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, enables AWS CodeBuild to start rebuilding the source code every time a code change is pushed to the repository
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[codebuild:buildType](#list_codebuild-codebuild_buildType)<br />[codebuild:manualCreation](#list_codebuild-codebuild_manualCreation)<br />[codebuild:scopeConfiguration.domain](#list_codebuild-codebuild_scopeConfiguration.domain)<br />[codebuild:scopeConfiguration.name](#list_codebuild-codebuild_scopeConfiguration.name)<br />[codebuild:scopeConfiguration.scope](#list_codebuild-codebuild_scopeConfiguration.scope)
  - **Access level:** Write

- **   [DeleteBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteBuildBatch.html)  **
  - **Description:** Grants permission to delete a build batch
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteFleet.html)  **
  - **Description:** Grants permission to delete a compute fleet
  - **Resource types (\*required):** [fleet\*](#list_codebuild-resource-fleet)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a build project
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReport](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html)  **
  - **Description:** Grants permission to delete a report
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReportGroup.html)  **
  - **Description:** Grants permission to delete a report group
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy for the associated project or report group
  - **Resource types (\*required):** [project](#list_codebuild-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-group](#list_codebuild-resource-report-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteSourceCredentials.html)  **
  - **Description:** Grants permission to delete a set of GitHub, GitHub Enterprise, or Bitbucket source credentials
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteWebhook.html)  **
  - **Description:** Grants permission to delete webhook. For an existing AWS CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops AWS CodeBuild from rebuilding the source code every time a code change is pushed to the repository
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCodeCoverages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeCodeCoverages.html)  **
  - **Description:** Grants permission to return an array of CodeCoverage objects
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTestCases](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeTestCases.html)  **
  - **Description:** Grants permission to return an array of TestCase objects
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReportGroupTrend](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetReportGroupTrend.html)  **
  - **Description:** Grants permission to analyze and accumulate test report values for the test reports in the specified report group
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to return a resource policy for the specified project or report group
  - **Resource types (\*required):** [project](#list_codebuild-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-group](#list_codebuild-resource-report-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ImportSourceCredentials.html)  **
  - **Description:** Grants permission to import the source repository credentials for an AWS CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, or Bitbucket repository
  - **Resource types (\*required):** 
  - **Condition keys:** [codebuild:authType](#list_codebuild-codebuild_authType)<br />[codebuild:serverType](#list_codebuild-codebuild_serverType)<br />[codebuild:shouldOverwrite](#list_codebuild-codebuild_shouldOverwrite)<br />[codebuild:token](#list_codebuild-codebuild_token)<br />[codebuild:username](#list_codebuild-codebuild_username)
  - **Access level:** Write

- **   [InvalidateProjectCache](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_InvalidateProjectCache.html)  **
  - **Description:** Grants permission to reset the cache for a project
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatches.html)  **
  - **Description:** Grants permission to get a list of build batch IDs, with each build batch ID representing a single build batch
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBuildBatchesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatchesForProject.html)  **
  - **Description:** Grants permission to get a list of build batch IDs for the specified build project, with each build batch ID representing a single build batch
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuilds.html)  **
  - **Description:** Grants permission to get a list of build IDs, with each build ID representing a single build
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBuildsForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildsForProject.html)  **
  - **Description:** Grants permission to get a list of build IDs for the specified build project, with each build ID representing a single build
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCommandExecutionsForSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCommandExecutionsForSandbox.html)  **
  - **Description:** Grants permission to get a list of command execution IDs for the specified sandbox, with each command execution ID representing a single command execution
  - **Resource types (\*required):** [sandbox\*](#list_codebuild-resource-sandbox)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCuratedEnvironmentImages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCuratedEnvironmentImages.html)  **
  - **Description:** Grants permission to get information about Docker images that are managed by AWS CodeBuild
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListFleets.html)  **
  - **Description:** Grants permission to get a list of compute fleet ARNs, with each compute fleet ARN representing a single fleet
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to get a list of build project names, with each build project name representing a single build project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportGroups.html)  **
  - **Description:** Grants permission to return a list of report group ARNs. Each report group ARN represents one report group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReports.html)  **
  - **Description:** Grants permission to return a list of report ARNs. Each report ARN representing one report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReportsForReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html)  **
  - **Description:** Grants permission to return a list of report ARNs that belong to the specified report group. Each report ARN represents one report
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxes.html)  **
  - **Description:** Grants permission to get a list of sandbox IDs, with each sandbox ID representing a single sandbox
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSandboxesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxesForProject.html)  **
  - **Description:** Grants permission to get a list of sandbox IDs for the specified sandbox project, with each sandbox ID representing a single sandbox
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSharedProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedProjects.html)  **
  - **Description:** Grants permission to return a list of project ARNs that have been shared with the requester. Each project ARN represents one project
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSharedReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedReportGroups.html)  **
  - **Description:** Grants permission to return a list of report group ARNs that have been shared with the requester. Each report group ARN represents one report group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSourceCredentials.html)  **
  - **Description:** Grants permission to return a list of SourceCredentialsInfo objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create a resource policy for the associated project or report group
  - **Resource types (\*required):** [project](#list_codebuild-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-group](#list_codebuild-resource-report-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RetryBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RetryBuild.html)  **
  - **Description:** Grants permission to retry a build
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetryBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RetryBuildBatch.html)  **
  - **Description:** Grants permission to retry a build batch
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuild.html)  **
  - **Description:** Grants permission to start running a build
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[codebuild:artifacts](#list_codebuild-codebuild_artifacts)<br />[codebuild:artifacts.bucketOwnerAccess](#list_codebuild-codebuild_artifacts.bucketOwnerAccess)<br />[codebuild:artifacts.encryptionDisabled](#list_codebuild-codebuild_artifacts.encryptionDisabled)<br />[codebuild:artifacts.location](#list_codebuild-codebuild_artifacts.location)<br />[codebuild:autoRetryLimit](#list_codebuild-codebuild_autoRetryLimit)<br />[codebuild:cache](#list_codebuild-codebuild_cache)<br />[codebuild:cache.location](#list_codebuild-codebuild_cache.location)<br />[codebuild:cache.modes](#list_codebuild-codebuild_cache.modes)<br />[codebuild:cache.type](#list_codebuild-codebuild_cache.type)<br />[codebuild:encryptionKey](#list_codebuild-codebuild_encryptionKey)<br />[codebuild:environment](#list_codebuild-codebuild_environment)<br />[codebuild:environment.certificate](#list_codebuild-codebuild_environment.certificate)<br />[codebuild:environment.computeType](#list_codebuild-codebuild_environment.computeType)<br />[codebuild:environment.environmentVariables](#list_codebuild-codebuild_environment.environmentVariables)<br />[codebuild:environment.environmentVariables.name](#list_codebuild-codebuild_environment.environmentVariables.name)<br />[codebuild:environment.environmentVariables.value](#list_codebuild-codebuild_environment.environmentVariables.value)<br />[codebuild:environment.environmentVariables/${name}.value](#list_codebuild-codebuild_environment.environmentVariables___name_.value)<br />[codebuild:environment.fleet.fleetArn](#list_codebuild-codebuild_environment.fleet.fleetArn)<br />[codebuild:environment.image](#list_codebuild-codebuild_environment.image)<br />[codebuild:environment.imagePullCredentialsType](#list_codebuild-codebuild_environment.imagePullCredentialsType)<br />[codebuild:environment.privilegedMode](#list_codebuild-codebuild_environment.privilegedMode)<br />[codebuild:environment.registryCredential](#list_codebuild-codebuild_environment.registryCredential)<br />[codebuild:environment.registryCredential.credential](#list_codebuild-codebuild_environment.registryCredential.credential)<br />[codebuild:environment.registryCredential.credentialProvider](#list_codebuild-codebuild_environment.registryCredential.credentialProvider)<br />[codebuild:environment.type](#list_codebuild-codebuild_environment.type)<br />[codebuild:logsConfig](#list_codebuild-codebuild_logsConfig)<br />[codebuild:logsConfig.s3Logs](#list_codebuild-codebuild_logsConfig.s3Logs)<br />[codebuild:logsConfig.s3Logs.bucketOwnerAccess](#list_codebuild-codebuild_logsConfig.s3Logs.bucketOwnerAccess)<br />[codebuild:logsConfig.s3Logs.encryptionDisabled](#list_codebuild-codebuild_logsConfig.s3Logs.encryptionDisabled)<br />[codebuild:logsConfig.s3Logs.location](#list_codebuild-codebuild_logsConfig.s3Logs.location)<br />[codebuild:logsConfig.s3Logs.status](#list_codebuild-codebuild_logsConfig.s3Logs.status)<br />[codebuild:secondaryArtifacts](#list_codebuild-codebuild_secondaryArtifacts)<br />[codebuild:secondaryArtifacts.artifactIdentifier](#list_codebuild-codebuild_secondaryArtifacts.artifactIdentifier)<br />[codebuild:secondaryArtifacts.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts.encryptionDisabled)<br />[codebuild:secondaryArtifacts.location](#list_codebuild-codebuild_secondaryArtifacts.location)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.encryptionDisabled)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.location](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.location)<br />[codebuild:secondarySources](#list_codebuild-codebuild_secondarySources)<br />[codebuild:secondarySources.auth.resource](#list_codebuild-codebuild_secondarySources.auth.resource)<br />[codebuild:secondarySources.auth.type](#list_codebuild-codebuild_secondarySources.auth.type)<br />[codebuild:secondarySources.buildspec](#list_codebuild-codebuild_secondarySources.buildspec)<br />[codebuild:secondarySources.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources.buildStatusConfig.context)<br />[codebuild:secondarySources.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources.insecureSsl](#list_codebuild-codebuild_secondarySources.insecureSsl)<br />[codebuild:secondarySources.location](#list_codebuild-codebuild_secondarySources.location)<br />[codebuild:secondarySources.sourceIdentifier](#list_codebuild-codebuild_secondarySources.sourceIdentifier)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.resource](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.resource)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.type](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.type)<br />[codebuild:secondarySources/${sourceIdentifier}.buildspec](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildspec)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.context)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources/${sourceIdentifier}.insecureSsl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.insecureSsl)<br />[codebuild:secondarySources/${sourceIdentifier}.location](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.location)<br />[codebuild:serviceRole](#list_codebuild-codebuild_serviceRole)<br />[codebuild:source](#list_codebuild-codebuild_source)<br />[codebuild:source.auth.resource](#list_codebuild-codebuild_source.auth.resource)<br />[codebuild:source.auth.type](#list_codebuild-codebuild_source.auth.type)<br />[codebuild:source.buildspec](#list_codebuild-codebuild_source.buildspec)<br />[codebuild:source.buildStatusConfig.context](#list_codebuild-codebuild_source.buildStatusConfig.context)<br />[codebuild:source.buildStatusConfig.targetUrl](#list_codebuild-codebuild_source.buildStatusConfig.targetUrl)<br />[codebuild:source.insecureSsl](#list_codebuild-codebuild_source.insecureSsl)<br />[codebuild:source.location](#list_codebuild-codebuild_source.location)
  - **Access level:** Write

- **   [StartBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartBuildBatch.html)  **
  - **Description:** Grants permission to start running a build batch
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[codebuild:artifacts](#list_codebuild-codebuild_artifacts)<br />[codebuild:artifacts.bucketOwnerAccess](#list_codebuild-codebuild_artifacts.bucketOwnerAccess)<br />[codebuild:artifacts.encryptionDisabled](#list_codebuild-codebuild_artifacts.encryptionDisabled)<br />[codebuild:artifacts.location](#list_codebuild-codebuild_artifacts.location)<br />[codebuild:buildBatchConfig](#list_codebuild-codebuild_buildBatchConfig)<br />[codebuild:buildBatchConfig.restrictions.computeTypesAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.computeTypesAllowed)<br />[codebuild:buildBatchConfig.restrictions.fleetsAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.fleetsAllowed)<br />[codebuild:buildBatchConfig.serviceRole](#list_codebuild-codebuild_buildBatchConfig.serviceRole)<br />[codebuild:cache](#list_codebuild-codebuild_cache)<br />[codebuild:cache.location](#list_codebuild-codebuild_cache.location)<br />[codebuild:cache.modes](#list_codebuild-codebuild_cache.modes)<br />[codebuild:cache.type](#list_codebuild-codebuild_cache.type)<br />[codebuild:encryptionKey](#list_codebuild-codebuild_encryptionKey)<br />[codebuild:environment](#list_codebuild-codebuild_environment)<br />[codebuild:environment.certificate](#list_codebuild-codebuild_environment.certificate)<br />[codebuild:environment.computeType](#list_codebuild-codebuild_environment.computeType)<br />[codebuild:environment.environmentVariables](#list_codebuild-codebuild_environment.environmentVariables)<br />[codebuild:environment.environmentVariables.name](#list_codebuild-codebuild_environment.environmentVariables.name)<br />[codebuild:environment.environmentVariables.value](#list_codebuild-codebuild_environment.environmentVariables.value)<br />[codebuild:environment.environmentVariables/${name}.value](#list_codebuild-codebuild_environment.environmentVariables___name_.value)<br />[codebuild:environment.image](#list_codebuild-codebuild_environment.image)<br />[codebuild:environment.imagePullCredentialsType](#list_codebuild-codebuild_environment.imagePullCredentialsType)<br />[codebuild:environment.privilegedMode](#list_codebuild-codebuild_environment.privilegedMode)<br />[codebuild:environment.registryCredential](#list_codebuild-codebuild_environment.registryCredential)<br />[codebuild:environment.registryCredential.credential](#list_codebuild-codebuild_environment.registryCredential.credential)<br />[codebuild:environment.registryCredential.credentialProvider](#list_codebuild-codebuild_environment.registryCredential.credentialProvider)<br />[codebuild:environment.type](#list_codebuild-codebuild_environment.type)<br />[codebuild:logsConfig](#list_codebuild-codebuild_logsConfig)<br />[codebuild:logsConfig.s3Logs](#list_codebuild-codebuild_logsConfig.s3Logs)<br />[codebuild:logsConfig.s3Logs.bucketOwnerAccess](#list_codebuild-codebuild_logsConfig.s3Logs.bucketOwnerAccess)<br />[codebuild:logsConfig.s3Logs.encryptionDisabled](#list_codebuild-codebuild_logsConfig.s3Logs.encryptionDisabled)<br />[codebuild:logsConfig.s3Logs.location](#list_codebuild-codebuild_logsConfig.s3Logs.location)<br />[codebuild:logsConfig.s3Logs.status](#list_codebuild-codebuild_logsConfig.s3Logs.status)<br />[codebuild:secondaryArtifacts](#list_codebuild-codebuild_secondaryArtifacts)<br />[codebuild:secondaryArtifacts.artifactIdentifier](#list_codebuild-codebuild_secondaryArtifacts.artifactIdentifier)<br />[codebuild:secondaryArtifacts.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts.encryptionDisabled)<br />[codebuild:secondaryArtifacts.location](#list_codebuild-codebuild_secondaryArtifacts.location)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.encryptionDisabled)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.location](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.location)<br />[codebuild:secondarySources](#list_codebuild-codebuild_secondarySources)<br />[codebuild:secondarySources.auth.resource](#list_codebuild-codebuild_secondarySources.auth.resource)<br />[codebuild:secondarySources.auth.type](#list_codebuild-codebuild_secondarySources.auth.type)<br />[codebuild:secondarySources.buildspec](#list_codebuild-codebuild_secondarySources.buildspec)<br />[codebuild:secondarySources.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources.buildStatusConfig.context)<br />[codebuild:secondarySources.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources.insecureSsl](#list_codebuild-codebuild_secondarySources.insecureSsl)<br />[codebuild:secondarySources.location](#list_codebuild-codebuild_secondarySources.location)<br />[codebuild:secondarySources.sourceIdentifier](#list_codebuild-codebuild_secondarySources.sourceIdentifier)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.resource](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.resource)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.type](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.type)<br />[codebuild:secondarySources/${sourceIdentifier}.buildspec](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildspec)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.context)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources/${sourceIdentifier}.insecureSsl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.insecureSsl)<br />[codebuild:secondarySources/${sourceIdentifier}.location](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.location)<br />[codebuild:serviceRole](#list_codebuild-codebuild_serviceRole)<br />[codebuild:source](#list_codebuild-codebuild_source)<br />[codebuild:source.auth.resource](#list_codebuild-codebuild_source.auth.resource)<br />[codebuild:source.auth.type](#list_codebuild-codebuild_source.auth.type)<br />[codebuild:source.buildspec](#list_codebuild-codebuild_source.buildspec)<br />[codebuild:source.insecureSsl](#list_codebuild-codebuild_source.insecureSsl)<br />[codebuild:source.location](#list_codebuild-codebuild_source.location)
  - **Access level:** Write

- **   [StartCommandExecution](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartCommandExecution.html)  **
  - **Description:** Grants permission to start running a command execution
  - **Resource types (\*required):** [sandbox\*](#list_codebuild-resource-sandbox)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartSandbox.html)  **
  - **Description:** Grants permission to start running a sandbox
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSandboxConnection](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StartSandboxConnection.html)  **
  - **Description:** Grants permission to establish a connection to the sandbox
  - **Resource types (\*required):** [sandbox\*](#list_codebuild-resource-sandbox)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopBuild](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopBuild.html)  **
  - **Description:** Grants permission to attempt to stop running a build
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBuildBatch](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopBuildBatch.html)  **
  - **Description:** Grants permission to attempt to stop running a build batch
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_StopSandbox.html)  **
  - **Description:** Grants permission to attempt to stop running a sandbox
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFleet](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateFleet.html)  **
  - **Description:** Grants permission to change the settings of an existing compute fleet
  - **Resource types (\*required):** [fleet\*](#list_codebuild-resource-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:computeConfiguration](#list_codebuild-codebuild_computeConfiguration)<br />[codebuild:computeConfiguration.disk](#list_codebuild-codebuild_computeConfiguration.disk)<br />[codebuild:computeConfiguration.instanceType](#list_codebuild-codebuild_computeConfiguration.instanceType)<br />[codebuild:computeConfiguration.machineType](#list_codebuild-codebuild_computeConfiguration.machineType)<br />[codebuild:computeConfiguration.memory](#list_codebuild-codebuild_computeConfiguration.memory)<br />[codebuild:computeConfiguration.vCpu](#list_codebuild-codebuild_computeConfiguration.vCpu)<br />[codebuild:computeType](#list_codebuild-codebuild_computeType)<br />[codebuild:environmentType](#list_codebuild-codebuild_environmentType)<br />[codebuild:fleetServiceRole](#list_codebuild-codebuild_fleetServiceRole)<br />[codebuild:imageId](#list_codebuild-codebuild_imageId)<br />[codebuild:vpcConfig](#list_codebuild-codebuild_vpcConfig)<br />[codebuild:vpcConfig.securityGroupIds](#list_codebuild-codebuild_vpcConfig.securityGroupIds)<br />[codebuild:vpcConfig.subnets](#list_codebuild-codebuild_vpcConfig.subnets)<br />[codebuild:vpcConfig.vpcId](#list_codebuild-codebuild_vpcConfig.vpcId)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to change the settings of an existing build project
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:artifacts](#list_codebuild-codebuild_artifacts)<br />[codebuild:artifacts.bucketOwnerAccess](#list_codebuild-codebuild_artifacts.bucketOwnerAccess)<br />[codebuild:artifacts.encryptionDisabled](#list_codebuild-codebuild_artifacts.encryptionDisabled)<br />[codebuild:artifacts.location](#list_codebuild-codebuild_artifacts.location)<br />[codebuild:autoRetryLimit](#list_codebuild-codebuild_autoRetryLimit)<br />[codebuild:buildBatchConfig](#list_codebuild-codebuild_buildBatchConfig)<br />[codebuild:buildBatchConfig.restrictions.computeTypesAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.computeTypesAllowed)<br />[codebuild:buildBatchConfig.restrictions.fleetsAllowed](#list_codebuild-codebuild_buildBatchConfig.restrictions.fleetsAllowed)<br />[codebuild:buildBatchConfig.serviceRole](#list_codebuild-codebuild_buildBatchConfig.serviceRole)<br />[codebuild:cache](#list_codebuild-codebuild_cache)<br />[codebuild:cache.location](#list_codebuild-codebuild_cache.location)<br />[codebuild:cache.modes](#list_codebuild-codebuild_cache.modes)<br />[codebuild:cache.type](#list_codebuild-codebuild_cache.type)<br />[codebuild:concurrentBuildLimit](#list_codebuild-codebuild_concurrentBuildLimit)<br />[codebuild:encryptionKey](#list_codebuild-codebuild_encryptionKey)<br />[codebuild:environment](#list_codebuild-codebuild_environment)<br />[codebuild:environment.certificate](#list_codebuild-codebuild_environment.certificate)<br />[codebuild:environment.computeConfiguration](#list_codebuild-codebuild_environment.computeConfiguration)<br />[codebuild:environment.computeConfiguration.disk](#list_codebuild-codebuild_environment.computeConfiguration.disk)<br />[codebuild:environment.computeConfiguration.instanceType](#list_codebuild-codebuild_environment.computeConfiguration.instanceType)<br />[codebuild:environment.computeConfiguration.machineType](#list_codebuild-codebuild_environment.computeConfiguration.machineType)<br />[codebuild:environment.computeConfiguration.memory](#list_codebuild-codebuild_environment.computeConfiguration.memory)<br />[codebuild:environment.computeConfiguration.vCpu](#list_codebuild-codebuild_environment.computeConfiguration.vCpu)<br />[codebuild:environment.computeType](#list_codebuild-codebuild_environment.computeType)<br />[codebuild:environment.environmentVariables](#list_codebuild-codebuild_environment.environmentVariables)<br />[codebuild:environment.environmentVariables.name](#list_codebuild-codebuild_environment.environmentVariables.name)<br />[codebuild:environment.environmentVariables.value](#list_codebuild-codebuild_environment.environmentVariables.value)<br />[codebuild:environment.environmentVariables/${name}.value](#list_codebuild-codebuild_environment.environmentVariables___name_.value)<br />[codebuild:environment.fleet.fleetArn](#list_codebuild-codebuild_environment.fleet.fleetArn)<br />[codebuild:environment.image](#list_codebuild-codebuild_environment.image)<br />[codebuild:environment.imagePullCredentialsType](#list_codebuild-codebuild_environment.imagePullCredentialsType)<br />[codebuild:environment.privilegedMode](#list_codebuild-codebuild_environment.privilegedMode)<br />[codebuild:environment.registryCredential](#list_codebuild-codebuild_environment.registryCredential)<br />[codebuild:environment.registryCredential.credential](#list_codebuild-codebuild_environment.registryCredential.credential)<br />[codebuild:environment.registryCredential.credentialProvider](#list_codebuild-codebuild_environment.registryCredential.credentialProvider)<br />[codebuild:environment.type](#list_codebuild-codebuild_environment.type)<br />[codebuild:fileSystemLocations.identifier](#list_codebuild-codebuild_fileSystemLocations.identifier)<br />[codebuild:fileSystemLocations.location](#list_codebuild-codebuild_fileSystemLocations.location)<br />[codebuild:fileSystemLocations.type](#list_codebuild-codebuild_fileSystemLocations.type)<br />[codebuild:fileSystemLocations/${identifier}.location](#list_codebuild-codebuild_fileSystemLocations___identifier_.location)<br />[codebuild:fileSystemLocations/${identifier}.type](#list_codebuild-codebuild_fileSystemLocations___identifier_.type)<br />[codebuild:logsConfig](#list_codebuild-codebuild_logsConfig)<br />[codebuild:logsConfig.s3Logs](#list_codebuild-codebuild_logsConfig.s3Logs)<br />[codebuild:logsConfig.s3Logs.bucketOwnerAccess](#list_codebuild-codebuild_logsConfig.s3Logs.bucketOwnerAccess)<br />[codebuild:logsConfig.s3Logs.encryptionDisabled](#list_codebuild-codebuild_logsConfig.s3Logs.encryptionDisabled)<br />[codebuild:logsConfig.s3Logs.location](#list_codebuild-codebuild_logsConfig.s3Logs.location)<br />[codebuild:logsConfig.s3Logs.status](#list_codebuild-codebuild_logsConfig.s3Logs.status)<br />[codebuild:secondaryArtifacts](#list_codebuild-codebuild_secondaryArtifacts)<br />[codebuild:secondaryArtifacts.artifactIdentifier](#list_codebuild-codebuild_secondaryArtifacts.artifactIdentifier)<br />[codebuild:secondaryArtifacts.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts.encryptionDisabled)<br />[codebuild:secondaryArtifacts.location](#list_codebuild-codebuild_secondaryArtifacts.location)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.bucketOwnerAccess](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.bucketOwnerAccess)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.encryptionDisabled](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.encryptionDisabled)<br />[codebuild:secondaryArtifacts/${artifactIdentifier}.location](#list_codebuild-codebuild_secondaryArtifacts___artifactIdentifier_.location)<br />[codebuild:secondarySources](#list_codebuild-codebuild_secondarySources)<br />[codebuild:secondarySources.auth.resource](#list_codebuild-codebuild_secondarySources.auth.resource)<br />[codebuild:secondarySources.auth.type](#list_codebuild-codebuild_secondarySources.auth.type)<br />[codebuild:secondarySources.buildspec](#list_codebuild-codebuild_secondarySources.buildspec)<br />[codebuild:secondarySources.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources.buildStatusConfig.context)<br />[codebuild:secondarySources.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources.insecureSsl](#list_codebuild-codebuild_secondarySources.insecureSsl)<br />[codebuild:secondarySources.location](#list_codebuild-codebuild_secondarySources.location)<br />[codebuild:secondarySources.sourceIdentifier](#list_codebuild-codebuild_secondarySources.sourceIdentifier)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.resource](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.resource)<br />[codebuild:secondarySources/${sourceIdentifier}.auth.type](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.auth.type)<br />[codebuild:secondarySources/${sourceIdentifier}.buildspec](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildspec)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.context](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.context)<br />[codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.targetUrl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.buildStatusConfig.targetUrl)<br />[codebuild:secondarySources/${sourceIdentifier}.insecureSsl](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.insecureSsl)<br />[codebuild:secondarySources/${sourceIdentifier}.location](#list_codebuild-codebuild_secondarySources___sourceIdentifier_.location)<br />[codebuild:serviceRole](#list_codebuild-codebuild_serviceRole)<br />[codebuild:source](#list_codebuild-codebuild_source)<br />[codebuild:source.auth.resource](#list_codebuild-codebuild_source.auth.resource)<br />[codebuild:source.auth.type](#list_codebuild-codebuild_source.auth.type)<br />[codebuild:source.buildspec](#list_codebuild-codebuild_source.buildspec)<br />[codebuild:source.buildStatusConfig.context](#list_codebuild-codebuild_source.buildStatusConfig.context)<br />[codebuild:source.buildStatusConfig.targetUrl](#list_codebuild-codebuild_source.buildStatusConfig.targetUrl)<br />[codebuild:source.insecureSsl](#list_codebuild-codebuild_source.insecureSsl)<br />[codebuild:source.location](#list_codebuild-codebuild_source.location)<br />[codebuild:vpcConfig](#list_codebuild-codebuild_vpcConfig)<br />[codebuild:vpcConfig.securityGroupIds](#list_codebuild-codebuild_vpcConfig.securityGroupIds)<br />[codebuild:vpcConfig.subnets](#list_codebuild-codebuild_vpcConfig.subnets)<br />[codebuild:vpcConfig.vpcId](#list_codebuild-codebuild_vpcConfig.vpcId)
  - **Access level:** Write

- **   [UpdateProjectVisibility](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateProjectVisibility.html)  **
  - **Description:** Grants permission to change the public visibility of a project and its builds
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:projectVisibility](#list_codebuild-codebuild_projectVisibility)
  - **Access level:** Write

- **   [UpdateReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateReportGroup.html)  **
  - **Description:** Grants permission to change the settings of an existing report group
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codebuild-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codebuild-aws_TagKeys)<br />[codebuild:exportConfig.s3Destination.bucket](#list_codebuild-codebuild_exportConfig.s3Destination.bucket)<br />[codebuild:exportConfig.s3Destination.bucketOwner](#list_codebuild-codebuild_exportConfig.s3Destination.bucketOwner)<br />[codebuild:exportConfig.s3Destination.encryptionDisabled](#list_codebuild-codebuild_exportConfig.s3Destination.encryptionDisabled)<br />[codebuild:exportConfig.s3Destination.encryptionKey](#list_codebuild-codebuild_exportConfig.s3Destination.encryptionKey)<br />[codebuild:exportConfig.s3Destination.path](#list_codebuild-codebuild_exportConfig.s3Destination.path)
  - **Access level:** Write

- **   [UpdateWebhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateWebhook.html)  **
  - **Description:** Grants permission to update the webhook associated with an AWS CodeBuild build project
  - **Resource types (\*required):** [project\*](#list_codebuild-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)<br />[codebuild:buildType](#list_codebuild-codebuild_buildType)<br />[codebuild:manualCreation](#list_codebuild-codebuild_manualCreation)<br />[codebuild:scopeConfiguration.domain](#list_codebuild-codebuild_scopeConfiguration.domain)<br />[codebuild:scopeConfiguration.name](#list_codebuild-codebuild_scopeConfiguration.name)<br />[codebuild:scopeConfiguration.scope](#list_codebuild-codebuild_scopeConfiguration.scope)
  - **Access level:** Write



## Permission-only actions for AWS CodeBuild
<a name="list_codebuild-permission-only-actions"></a>

The following actions are defined by AWS CodeBuild but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [BatchPutCodeCoverages](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to add or update information about a report
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutTestCases](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to add or update information about a report
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReport](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to create a report. A report is created when tests specified in the buildspec file for a report groups run during the build of a project
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOAuthToken](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to delete an OAuth token from a connected third-party OAuth provider. Only used in the AWS CodeBuild console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListConnectedOAuthAccounts](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to list connected third-party OAuth providers. Only used in the AWS CodeBuild console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to list source code repositories from a connected third-party OAuth provider. Only used in the AWS CodeBuild console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PersistOAuthToken](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to save an OAuth token from a connected third-party OAuth provider. Only used in the AWS CodeBuild console
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateReport](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies)  **
  - **Description:** Grants permission to update information about a report
  - **Resource types (\*required):** [report-group\*](#list_codebuild-resource-report-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CodeBuild
<a name="list_codebuild-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [build](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:build/${BuildId} |   | 
|  [build-batch](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:build-batch/${BuildBatchId} |   | 
|  [fleet](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:fleet/${FleetName}:${FleetId} |   | 
|  [project](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:project/${ProjectName} | [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_) | 
|  [report](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:report/${ReportGroupName}:${ReportId} |   | 
|  [report-group](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:report-group/${ReportGroupName} | [aws:ResourceTag/${TagKey}](#list_codebuild-aws_ResourceTag___TagKey_) | 
|  [sandbox](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-access-control-identity-based.html#arn-formats)  | arn:${Partition}:codebuild:${Region}:${Account}:sandbox/${SandboxId} |   | 

## Condition keys for AWS CodeBuild
<a name="list_codebuild-policy-keys"></a>

AWS CodeBuild defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by actions based on the presence of tag keys in the request | ArrayOfString | 
|   [codebuild:artifacts](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:artifacts.bucketOwnerAccess](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:artifacts.encryptionDisabled](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:artifacts.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:authType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:autoRetryLimit](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:buildArn](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-permissions-reference.html)  | Filters access by the ARN of the AWS CodeBuild build from which the request originated | ARN | 
|   [codebuild:buildBatchConfig](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:buildBatchConfig.restrictions.computeTypesAllowed](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:buildBatchConfig.restrictions.fleetsAllowed](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:buildBatchConfig.serviceRole](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:buildType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:cache](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:cache.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:cache.modes](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:cache.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:computeConfiguration](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:computeConfiguration.disk](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:computeConfiguration.instanceType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:computeConfiguration.machineType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:computeConfiguration.memory](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:computeConfiguration.vCpu](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:computeType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:concurrentBuildLimit](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:encryptionKey](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:environment.certificate](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.computeConfiguration](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:environment.computeConfiguration.disk](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:environment.computeConfiguration.instanceType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.computeConfiguration.machineType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.computeConfiguration.memory](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:environment.computeConfiguration.vCpu](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Numeric | 
|   [codebuild:environment.computeType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.environmentVariables](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:environment.environmentVariables.name](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:environment.environmentVariables.value](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:environment.environmentVariables/${name}.value](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.fleet.fleetArn](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ARN | 
|   [codebuild:environment.image](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.imagePullCredentialsType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.privilegedMode](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:environment.registryCredential](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:environment.registryCredential.credential](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.registryCredential.credentialProvider](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environment.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:environmentType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:exportConfig.s3Destination.bucket](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:exportConfig.s3Destination.bucketOwner](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:exportConfig.s3Destination.encryptionDisabled](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:exportConfig.s3Destination.encryptionKey](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:exportConfig.s3Destination.path](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:fileSystemLocations.identifier](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:fileSystemLocations.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:fileSystemLocations.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:fileSystemLocations/${identifier}.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:fileSystemLocations/${identifier}.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:fleetServiceRole](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:imageId](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:logsConfig](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:logsConfig.s3Logs](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:logsConfig.s3Logs.bucketOwnerAccess](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:logsConfig.s3Logs.encryptionDisabled](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:logsConfig.s3Logs.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:logsConfig.s3Logs.status](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:manualCreation](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:projectArn](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-permissions-reference.html)  | Filters access by the ARN of the AWS CodeBuild project from which the request originated | ARN | 
|   [codebuild:projectVisibility](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:scopeConfiguration.domain](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:scopeConfiguration.name](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:scopeConfiguration.scope](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondaryArtifacts](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondaryArtifacts.artifactIdentifier](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondaryArtifacts.bucketOwnerAccess](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondaryArtifacts.encryptionDisabled](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfBool | 
|   [codebuild:secondaryArtifacts.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondaryArtifacts/${artifactIdentifier}.bucketOwnerAccess](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondaryArtifacts/${artifactIdentifier}.encryptionDisabled](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondaryArtifacts/${artifactIdentifier}.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondarySources](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondarySources.auth.resource](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources.auth.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources.buildStatusConfig.context](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources.buildStatusConfig.targetUrl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources.buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondarySources.insecureSsl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfBool | 
|   [codebuild:secondarySources.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources.sourceIdentifier](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:secondarySources/${sourceIdentifier}.auth.resource](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondarySources/${sourceIdentifier}.auth.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.context](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondarySources/${sourceIdentifier}.buildStatusConfig.targetUrl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:secondarySources/${sourceIdentifier}.buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondarySources/${sourceIdentifier}.insecureSsl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:secondarySources/${sourceIdentifier}.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:serverType](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:serviceRole](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:shouldOverwrite](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:source](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:source.auth.resource](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:source.auth.type](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:source.buildStatusConfig.context](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:source.buildStatusConfig.targetUrl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:source.buildspec](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:source.insecureSsl](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:source.location](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:token](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:username](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 
|   [codebuild:vpcConfig](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | Bool | 
|   [codebuild:vpcConfig.securityGroupIds](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:vpcConfig.subnets](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | ArrayOfString | 
|   [codebuild:vpcConfig.vpcId](https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html)  | Filters access by the API corresponding argument value | String | 