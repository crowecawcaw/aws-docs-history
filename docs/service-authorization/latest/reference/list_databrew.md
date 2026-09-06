

# Actions, resources, and condition keys for AWS Glue DataBrew
<a name="list_databrew"></a>

AWS Glue DataBrew (service prefix: `databrew`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/databrew/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/databrew/latest/dg/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/databrew/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/databrew/databrew.json) for this service.

**Topics**
+ [API operations defined by AWS Glue DataBrew](#list_databrew-operations)
+ [Actions defined by AWS Glue DataBrew](#list_databrew-actions-as-permissions)
+ [Resource types defined by AWS Glue DataBrew](#list_databrew-resources-for-iam-policies)
+ [Condition keys for AWS Glue DataBrew](#list_databrew-policy-keys)

## API operations defined by AWS Glue DataBrew
<a name="list_databrew-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_databrew-actions-as-permissions).




- **   BatchDeleteRecipeVersion  **
  - **IAM action:**  [databrew:BatchDeleteRecipeVersion](#list_databrew-action-BatchDeleteRecipeVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataset  **
  - **IAM action:**  [databrew:CreateDataset](#list_databrew-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProfileJob  **
  - **IAM action:**  [databrew:CreateProfileJob](#list_databrew-action-CreateProfileJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [databrew:CreateProject](#list_databrew-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   CreateRecipe  **
  - **IAM action:**  [databrew:CreateRecipe](#list_databrew-action-CreateRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRecipeJob  **
  - **IAM action:**  [databrew:CreateRecipeJob](#list_databrew-action-CreateRecipeJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   CreateRuleset  **
  - **IAM action:**  [databrew:CreateRuleset](#list_databrew-action-CreateRuleset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSchedule  **
  - **IAM action:**  [databrew:CreateSchedule](#list_databrew-action-CreateSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDataset  **
  - **IAM action:**  [databrew:DeleteDataset](#list_databrew-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **IAM action:**  [databrew:DeleteJob](#list_databrew-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [databrew:DeleteProject](#list_databrew-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecipeVersion  **
  - **IAM action:**  [databrew:DeleteRecipeVersion](#list_databrew-action-DeleteRecipeVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRuleset  **
  - **IAM action:**  [databrew:DeleteRuleset](#list_databrew-action-DeleteRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchedule  **
  - **IAM action:**  [databrew:DeleteSchedule](#list_databrew-action-DeleteSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataset  **
  - **IAM action:**  [databrew:DescribeDataset](#list_databrew-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJob  **
  - **IAM action:**  [databrew:DescribeJob](#list_databrew-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobRun  **
  - **IAM action:**  [databrew:DescribeJobRun](#list_databrew-action-DescribeJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProject  **
  - **IAM action:**  [databrew:DescribeProject](#list_databrew-action-DescribeProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRecipe  **
  - **IAM action:**  [databrew:DescribeRecipe](#list_databrew-action-DescribeRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRuleset  **
  - **IAM action:**  [databrew:DescribeRuleset](#list_databrew-action-DescribeRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchedule  **
  - **IAM action:**  [databrew:DescribeSchedule](#list_databrew-action-DescribeSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasets  **
  - **IAM action:**  [databrew:ListDatasets](#list_databrew-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListJobRuns  **
  - **IAM action:**  [databrew:ListJobRuns](#list_databrew-action-ListJobRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListJobs  **
  - **IAM action:**  [databrew:ListJobs](#list_databrew-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProjects  **
  - **IAM action:**  [databrew:ListProjects](#list_databrew-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecipeVersions  **
  - **IAM action:**  [databrew:ListRecipeVersions](#list_databrew-action-ListRecipeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecipes  **
  - **IAM action:**  [databrew:ListRecipes](#list_databrew-action-ListRecipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRulesets  **
  - **IAM action:**  [databrew:ListRulesets](#list_databrew-action-ListRulesets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSchedules  **
  - **IAM action:**  [databrew:ListSchedules](#list_databrew-action-ListSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [databrew:ListTagsForResource](#list_databrew-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PublishRecipe  **
  - **IAM action:**  [databrew:PublishRecipe](#list_databrew-action-PublishRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendProjectSessionAction  **
  - **IAM action:**  [databrew:SendProjectSessionAction](#list_databrew-action-SendProjectSessionAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartJobRun  **
  - **IAM action:**  [databrew:StartJobRun](#list_databrew-action-StartJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartProjectSession  **
  - **IAM action:**  [databrew:StartProjectSession](#list_databrew-action-StartProjectSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopJobRun  **
  - **IAM action:**  [databrew:StopJobRun](#list_databrew-action-StopJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [databrew:TagResource](#list_databrew-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [databrew:UntagResource](#list_databrew-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataset  **
  - **IAM action:**  [databrew:UpdateDataset](#list_databrew-action-UpdateDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfileJob  **
  - **IAM action:**  [databrew:UpdateProfileJob](#list_databrew-action-UpdateProfileJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   UpdateProject  **
  - **IAM action:**  [databrew:UpdateProject](#list_databrew-action-UpdateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   UpdateRecipe  **
  - **IAM action:**  [databrew:UpdateRecipe](#list_databrew-action-UpdateRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRecipeJob  **
  - **IAM action:**  [databrew:UpdateRecipeJob](#list_databrew-action-UpdateRecipeJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** databrew.amazonaws.com / **Access level:** Write

- **   UpdateRuleset  **
  - **IAM action:**  [databrew:UpdateRuleset](#list_databrew-action-UpdateRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSchedule  **
  - **IAM action:**  [databrew:UpdateSchedule](#list_databrew-action-UpdateSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Glue DataBrew
<a name="list_databrew-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDeleteRecipeVersion](https://docs.aws.amazon.com/databrew/latest/dg/API_BatchDeleteRecipeVersion.html)  **
  - **Description:** Grants permission to delete one or more recipe versions
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfileJob](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateProfileJob.html)  **
  - **Description:** Grants permission to create a profile job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecipe](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateRecipe.html)  **
  - **Description:** Grants permission to create a recipe
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRecipeJob](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateRecipeJob.html)  **
  - **Description:** Grants permission to create a recipe job
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRuleset](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateRuleset.html)  **
  - **Description:** Grants permission to create a ruleset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchedule](https://docs.aws.amazon.com/databrew/latest/dg/API_CreateSchedule.html)  **
  - **Description:** Grants permission to create a schedule
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [Dataset\*](#list_databrew-resource-Dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteJob.html)  **
  - **Description:** Grants permission to delete a job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [Project\*](#list_databrew-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecipeVersion](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteRecipeVersion.html)  **
  - **Description:** Grants permission to delete a recipe version
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRuleset](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteRuleset.html)  **
  - **Description:** Grants permission to delete a ruleset
  - **Resource types (\*required):** [Ruleset\*](#list_databrew-resource-Ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchedule](https://docs.aws.amazon.com/databrew/latest/dg/API_DeleteSchedule.html)  **
  - **Description:** Grants permission to delete a schedule
  - **Resource types (\*required):** [Schedule\*](#list_databrew-resource-Schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDataset](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeDataset.html)  **
  - **Description:** Grants permission to view details about a dataset
  - **Resource types (\*required):** [Dataset\*](#list_databrew-resource-Dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJob](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeJob.html)  **
  - **Description:** Grants permission to view details about a job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobRun](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeJobRun.html)  **
  - **Description:** Grants permission to view details about job run for a given job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProject](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeProject.html)  **
  - **Description:** Grants permission to view details about a project
  - **Resource types (\*required):** [Project\*](#list_databrew-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRecipe](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeRecipe.html)  **
  - **Description:** Grants permission to view details about a recipe
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRuleset](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeRuleset.html)  **
  - **Description:** Grants permission to view details about a ruleset
  - **Resource types (\*required):** [Ruleset\*](#list_databrew-resource-Ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSchedule](https://docs.aws.amazon.com/databrew/latest/dg/API_DescribeSchedule.html)  **
  - **Description:** Grants permission to view details about a schedule
  - **Resource types (\*required):** [Schedule\*](#list_databrew-resource-Schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDatasets](https://docs.aws.amazon.com/databrew/latest/dg/API_ListDatasets.html)  **
  - **Description:** Grants permission to list datasets in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListJobRuns](https://docs.aws.amazon.com/databrew/latest/dg/API_ListJobRuns.html)  **
  - **Description:** Grants permission to list job runs for a given job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListJobs](https://docs.aws.amazon.com/databrew/latest/dg/API_ListJobs.html)  **
  - **Description:** Grants permission to list jobs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListProjects](https://docs.aws.amazon.com/databrew/latest/dg/API_ListProjects.html)  **
  - **Description:** Grants permission to list projects in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRecipeVersions](https://docs.aws.amazon.com/databrew/latest/dg/API_ListRecipeVersions.html)  **
  - **Description:** Grants permission to list versions in your recipe
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRecipes](https://docs.aws.amazon.com/databrew/latest/dg/API_ListRecipes.html)  **
  - **Description:** Grants permission to list recipes in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRulesets](https://docs.aws.amazon.com/databrew/latest/dg/API_ListRulesets.html)  **
  - **Description:** Grants permission to list rulesets in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSchedules](https://docs.aws.amazon.com/databrew/latest/dg/API_ListSchedules.html)  **
  - **Description:** Grants permission to list schedules in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/databrew/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve tags associated with a resource
  - **Resource types (\*required):** [Dataset](#list_databrew-resource-Dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Job](#list_databrew-resource-Job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Project](#list_databrew-resource-Project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Recipe](#list_databrew-resource-Recipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Ruleset](#list_databrew-resource-Ruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Schedule](#list_databrew-resource-Schedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PublishRecipe](https://docs.aws.amazon.com/databrew/latest/dg/API_PublishRecipe.html)  **
  - **Description:** Grants permission to publish a major verison of a recipe
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendProjectSessionAction](https://docs.aws.amazon.com/databrew/latest/dg/API_SendProjectSessionAction.html)  **
  - **Description:** Grants permission to submit an action to the interactive session for a project
  - **Resource types (\*required):** [Project\*](#list_databrew-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJobRun](https://docs.aws.amazon.com/databrew/latest/dg/API_StartJobRun.html)  **
  - **Description:** Grants permission to start running a job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartProjectSession](https://docs.aws.amazon.com/databrew/latest/dg/API_StartProjectSession.html)  **
  - **Description:** Grants permission to start an interactive session for a project
  - **Resource types (\*required):** [Project\*](#list_databrew-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopJobRun](https://docs.aws.amazon.com/databrew/latest/dg/API_StopJobRun.html)  **
  - **Description:** Grants permission to stop a job run for a job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/databrew/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [Dataset](#list_databrew-resource-Dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Job](#list_databrew-resource-Job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Project](#list_databrew-resource-Project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Recipe](#list_databrew-resource-Recipe) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Ruleset](#list_databrew-resource-Ruleset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Schedule](#list_databrew-resource-Schedule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_databrew-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/databrew/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags associated with a resource
  - **Resource types (\*required):** [Dataset](#list_databrew-resource-Dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Job](#list_databrew-resource-Job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Project](#list_databrew-resource-Project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Recipe](#list_databrew-resource-Recipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Ruleset](#list_databrew-resource-Ruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Resource types (\*required):** [Schedule](#list_databrew-resource-Schedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_databrew-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataset](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateDataset.html)  **
  - **Description:** Grants permission to modify a dataset
  - **Resource types (\*required):** [Dataset\*](#list_databrew-resource-Dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfileJob](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateProfileJob.html)  **
  - **Description:** Grants permission to modify a profile job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateProject.html)  **
  - **Description:** Grants permission to modify a project
  - **Resource types (\*required):** [Project\*](#list_databrew-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecipe](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateRecipe.html)  **
  - **Description:** Grants permission to modify a recipe
  - **Resource types (\*required):** [Recipe\*](#list_databrew-resource-Recipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecipeJob](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateRecipeJob.html)  **
  - **Description:** Grants permission to modify a recipe job
  - **Resource types (\*required):** [Job\*](#list_databrew-resource-Job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleset](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateRuleset.html)  **
  - **Description:** Grants permission to modify a ruleset
  - **Resource types (\*required):** [Ruleset\*](#list_databrew-resource-Ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSchedule](https://docs.aws.amazon.com/databrew/latest/dg/API_UpdateSchedule.html)  **
  - **Description:** Grants permission to modify a schedule
  - **Resource types (\*required):** [Schedule\*](#list_databrew-resource-Schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Glue DataBrew
<a name="list_databrew-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Dataset](https://docs.aws.amazon.com/databrew/latest/dg/datasets.html)  | arn:${Partition}:databrew:${Region}:${Account}:dataset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 
|  [Job](https://docs.aws.amazon.com/databrew/latest/dg/jobs.html)  | arn:${Partition}:databrew:${Region}:${Account}:job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 
|  [Project](https://docs.aws.amazon.com/databrew/latest/dg/projects.html)  | arn:${Partition}:databrew:${Region}:${Account}:project/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 
|  [Recipe](https://docs.aws.amazon.com/databrew/latest/dg/recipes.html)  | arn:${Partition}:databrew:${Region}:${Account}:recipe/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 
|  [Ruleset](https://docs.aws.amazon.com/databrew/latest/dg/rulesets.html)  | arn:${Partition}:databrew:${Region}:${Account}:ruleset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 
|  [Schedule](https://docs.aws.amazon.com/databrew/latest/dg/jobs.html#jobs.scheduling)  | arn:${Partition}:databrew:${Region}:${Account}:schedule/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_databrew-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Glue DataBrew
<a name="list_databrew-policy-keys"></a>

AWS Glue DataBrew defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 