

# Actions, resources, and condition keys for AWS Glue
<a name="list_glue"></a>

AWS Glue (service prefix: `glue`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/glue/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/glue/latest/dg/authentication-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/glue/glue.json) for this service.

**Topics**
+ [API operations defined by AWS Glue](#list_glue-operations)
+ [Actions defined by AWS Glue](#list_glue-actions-as-permissions)
+ [Permission-only actions for AWS Glue](#list_glue-permission-only-actions)
+ [Resource types defined by AWS Glue](#list_glue-resources-for-iam-policies)
+ [Condition keys for AWS Glue](#list_glue-policy-keys)

## API operations defined by AWS Glue
<a name="list_glue-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_glue-actions-as-permissions).




- **   BatchDeleteConnection  **
  - **IAM action:**  [glue:BatchDeleteConnection](#list_glue-action-BatchDeleteConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:DeleteConnection](#list_glue-action-DeleteConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchDeleteTableVersion  **
  - **IAM action:**  [glue:BatchDeleteTableVersion](#list_glue-action-BatchDeleteTableVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:DeleteTableVersion](#list_glue-action-DeleteTableVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   BatchGetBlueprints  **
  - **IAM action:**  [glue:BatchGetBlueprints](#list_glue-action-BatchGetBlueprints)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetBlueprint](#list_glue-action-GetBlueprint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetCrawlers  **
  - **IAM action:**  [glue:BatchGetCrawlers](#list_glue-action-BatchGetCrawlers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCustomEntityTypes  **
  - **IAM action:**  [glue:BatchGetCustomEntityTypes](#list_glue-action-BatchGetCustomEntityTypes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetCustomEntityType](#list_glue-action-GetCustomEntityType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetDataQualityResult  **
  - **IAM action:**  [glue:GetDataQualityResult](#list_glue-action-GetDataQualityResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetDevEndpoints  **
  - **IAM action:**  [glue:BatchGetDevEndpoints](#list_glue-action-BatchGetDevEndpoints)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetDevEndpoint](#list_glue-action-GetDevEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetJobs  **
  - **IAM action:**  [glue:BatchGetJobs](#list_glue-action-BatchGetJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetJob](#list_glue-action-GetJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetTableOptimizer  **
  - **IAM action:**  [glue:BatchGetTableOptimizer](#list_glue-action-BatchGetTableOptimizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetTriggers  **
  - **IAM action:**  [glue:BatchGetTriggers](#list_glue-action-BatchGetTriggers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetTrigger](#list_glue-action-GetTrigger)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchGetWorkflows  **
  - **IAM action:**  [glue:BatchGetWorkflows](#list_glue-action-BatchGetWorkflows)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:GetWorkflow](#list_glue-action-GetWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   BatchPutDataQualityStatisticAnnotation  **
  - **IAM action:**  [glue:PutDataQualityStatisticAnnotation](#list_glue-action-PutDataQualityStatisticAnnotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchStopJobRun  **
  - **IAM action:**  [glue:BatchStopJobRun](#list_glue-action-BatchStopJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDataQualityRuleRecommendationRun  **
  - **IAM action:**  [glue:CancelDataQualityRuleRecommendationRun](#list_glue-action-CancelDataQualityRuleRecommendationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDataQualityRulesetEvaluationRun  **
  - **IAM action:**  [glue:CancelDataQualityRulesetEvaluationRun](#list_glue-action-CancelDataQualityRulesetEvaluationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelMLTaskRun  **
  - **IAM action:**  [glue:CancelMLTaskRun](#list_glue-action-CancelMLTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelStatement  **
  - **IAM action:**  [glue:CancelStatement](#list_glue-action-CancelStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckSchemaVersionValidity  **
  - **IAM action:**  [glue:CheckSchemaVersionValidity](#list_glue-action-CheckSchemaVersionValidity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateBlueprint  **
  - **IAM action:**  [glue:CreateBlueprint](#list_glue-action-CreateBlueprint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCatalog  **
  - **IAM action:**  [glue:CreateCatalog](#list_glue-action-CreateCatalog)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateClassifier  **
  - **IAM action:**  [glue:CreateClassifier](#list_glue-action-CreateClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateColumnStatisticsTaskSettings  **
  - **IAM action:**  [glue:CreateColumnStatisticsTaskSettings](#list_glue-action-CreateColumnStatisticsTaskSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateConnection  **
  - **IAM action:**  [glue:CreateConnection](#list_glue-action-CreateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:DescribeConnectionType](#list_glue-action-DescribeConnectionType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateCrawler  **
  - **IAM action:**  [glue:CreateCrawler](#list_glue-action-CreateCrawler)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateCustomEntityType  **
  - **IAM action:**  [glue:CreateCustomEntityType](#list_glue-action-CreateCustomEntityType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataQualityRuleset  **
  - **IAM action:**  [glue:CreateDataQualityRuleset](#list_glue-action-CreateDataQualityRuleset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDatabase  **
  - **IAM action:**  [glue:CreateDatabase](#list_glue-action-CreateDatabase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDevEndpoint  **
  - **IAM action:**  [glue:CreateDevEndpoint](#list_glue-action-CreateDevEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateGlueIdentityCenterConfiguration  **
  - **IAM action:**  [glue:CreateGlueIdentityCenterConfiguration](#list_glue-action-CreateGlueIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIntegration  **
  - **IAM action:**  [glue:CreateIntegration](#list_glue-action-CreateIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIntegrationResourceProperty  **
  - **IAM action:**  [glue:CreateIntegrationResourceProperty](#list_glue-action-CreateIntegrationResourceProperty)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateIntegrationTableProperties  **
  - **IAM action:**  [glue:CreateIntegrationTableProperties](#list_glue-action-CreateIntegrationTableProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateJob  **
  - **IAM action:**  [glue:CreateJob](#list_glue-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:GetUsageProfile](#list_glue-action-GetUsageProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateMLTransform  **
  - **IAM action:**  [glue:CreateMLTransform](#list_glue-action-CreateMLTransform)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreatePartition  **
  - **IAM action:**  [glue:CreatePartition](#list_glue-action-CreatePartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePartitionIndex  **
  - **IAM action:**  [glue:UpdateTable](#list_glue-action-UpdateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRegistry  **
  - **IAM action:**  [glue:CreateRegistry](#list_glue-action-CreateRegistry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSchema  **
  - **IAM action:**  [glue:CreateSchema](#list_glue-action-CreateSchema)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateScript  **
  - **IAM action:**  [glue:CreateScript](#list_glue-action-CreateScript) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSecurityConfiguration  **
  - **IAM action:**  [glue:CreateSecurityConfiguration](#list_glue-action-CreateSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSession  **
  - **IAM action:**  [glue:CreateSession](#list_glue-action-CreateSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:GetUsageProfile](#list_glue-action-GetUsageProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateTable  **
  - **IAM action:**  [glue:CreateTable](#list_glue-action-CreateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateTableOptimizer  **
  - **IAM action:**  [glue:CreateTableOptimizer](#list_glue-action-CreateTableOptimizer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   CreateTrigger  **
  - **IAM action:**  [glue:CreateTrigger](#list_glue-action-CreateTrigger)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUsageProfile  **
  - **IAM action:**  [glue:CreateUsageProfile](#list_glue-action-CreateUsageProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateUserDefinedFunction  **
  - **IAM action:**  [glue:CreateUserDefinedFunction](#list_glue-action-CreateUserDefinedFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkflow  **
  - **IAM action:**  [glue:CreateWorkflow](#list_glue-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBlueprint  **
  - **IAM action:**  [glue:DeleteBlueprint](#list_glue-action-DeleteBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCatalog  **
  - **IAM action:**  [glue:DeleteCatalog](#list_glue-action-DeleteCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClassifier  **
  - **IAM action:**  [glue:DeleteClassifier](#list_glue-action-DeleteClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteColumnStatisticsForPartition  **
  - **IAM action:**  [glue:UpdatePartition](#list_glue-action-UpdatePartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteColumnStatisticsForTable  **
  - **IAM action:**  [glue:UpdateTable](#list_glue-action-UpdateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteColumnStatisticsTaskSettings  **
  - **IAM action:**  [glue:DeleteColumnStatisticsTaskSettings](#list_glue-action-DeleteColumnStatisticsTaskSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnection  **
  - **IAM action:**  [glue:DeleteConnection](#list_glue-action-DeleteConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnectionType  **
  - **IAM action:**  [glue:DeleteConnectionType](#list_glue-action-DeleteConnectionType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCrawler  **
  - **IAM action:**  [glue:DeleteCrawler](#list_glue-action-DeleteCrawler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomEntityType  **
  - **IAM action:**  [glue:DeleteCustomEntityType](#list_glue-action-DeleteCustomEntityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataQualityRuleset  **
  - **IAM action:**  [glue:DeleteDataQualityRuleset](#list_glue-action-DeleteDataQualityRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDatabase  **
  - **IAM action:**  [glue:DeleteDatabase](#list_glue-action-DeleteDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDevEndpoint  **
  - **IAM action:**  [glue:DeleteDevEndpoint](#list_glue-action-DeleteDevEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGlueIdentityCenterConfiguration  **
  - **IAM action:**  [glue:DeleteGlueIdentityCenterConfiguration](#list_glue-action-DeleteGlueIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegration  **
  - **IAM action:**  [glue:DeleteIntegration](#list_glue-action-DeleteIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegrationResourceProperty  **
  - **IAM action:**  [glue:DeleteIntegrationResourceProperty](#list_glue-action-DeleteIntegrationResourceProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntegrationTableProperties  **
  - **IAM action:**  [glue:DeleteIntegrationTableProperties](#list_glue-action-DeleteIntegrationTableProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **IAM action:**  [glue:DeleteJob](#list_glue-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMLTransform  **
  - **IAM action:**  [glue:DeleteMLTransform](#list_glue-action-DeleteMLTransform) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartition  **
  - **IAM action:**  [glue:DeletePartition](#list_glue-action-DeletePartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartitionIndex  **
  - **IAM action:**  [glue:UpdateTable](#list_glue-action-UpdateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistry  **
  - **IAM action:**  [glue:DeleteRegistry](#list_glue-action-DeleteRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchema  **
  - **IAM action:**  [glue:DeleteSchema](#list_glue-action-DeleteSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchemaVersions  **
  - **IAM action:**  [glue:DeleteSchemaVersions](#list_glue-action-DeleteSchemaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityConfiguration  **
  - **IAM action:**  [glue:DeleteSecurityConfiguration](#list_glue-action-DeleteSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSession  **
  - **IAM action:**  [glue:DeleteSession](#list_glue-action-DeleteSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTable  **
  - **IAM action:**  [glue:DeleteTable](#list_glue-action-DeleteTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableOptimizer  **
  - **IAM action:**  [glue:DeleteTableOptimizer](#list_glue-action-DeleteTableOptimizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTableVersion  **
  - **IAM action:**  [glue:DeleteTableVersion](#list_glue-action-DeleteTableVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrigger  **
  - **IAM action:**  [glue:DeleteTrigger](#list_glue-action-DeleteTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUsageProfile  **
  - **IAM action:**  [glue:DeleteUsageProfile](#list_glue-action-DeleteUsageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserDefinedFunction  **
  - **IAM action:**  [glue:DeleteUserDefinedFunction](#list_glue-action-DeleteUserDefinedFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [glue:DeleteWorkflow](#list_glue-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnectionType  **
  - **IAM action:**  [glue:DescribeConnectionType](#list_glue-action-DescribeConnectionType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeEntity  **
  - **IAM action:**  [glue:DescribeEntity](#list_glue-action-DescribeEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DescribeInboundIntegrations  **
  - **IAM action:**  [glue:DescribeInboundIntegrations](#list_glue-action-DescribeInboundIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeIntegrations  **
  - **IAM action:**  [glue:DescribeIntegrations](#list_glue-action-DescribeIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBlueprint  **
  - **IAM action:**  [glue:GetBlueprint](#list_glue-action-GetBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlueprintRun  **
  - **IAM action:**  [glue:GetBlueprintRun](#list_glue-action-GetBlueprintRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlueprintRuns  **
  - **IAM action:**  [glue:GetBlueprintRuns](#list_glue-action-GetBlueprintRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCatalog  **
  - **IAM action:**  [glue:GetCatalog](#list_glue-action-GetCatalog) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCatalogImportStatus  **
  - **IAM action:**  [glue:GetCatalogImportStatus](#list_glue-action-GetCatalogImportStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCatalogs  **
  - **IAM action:**  [glue:GetCatalogs](#list_glue-action-GetCatalogs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [athena:GetCatalogs](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetClassifier  **
  - **IAM action:**  [glue:GetClassifier](#list_glue-action-GetClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClassifiers  **
  - **IAM action:**  [glue:GetClassifiers](#list_glue-action-GetClassifiers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetColumnStatisticsForPartition  **
  - **IAM action:**  [glue:GetPartition](#list_glue-action-GetPartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetColumnStatisticsForTable  **
  - **IAM action:**  [glue:GetTable](#list_glue-action-GetTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetColumnStatisticsTaskRun  **
  - **IAM action:**  [glue:GetColumnStatisticsTaskRun](#list_glue-action-GetColumnStatisticsTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetColumnStatisticsTaskRuns  **
  - **IAM action:**  [glue:GetColumnStatisticsTaskRuns](#list_glue-action-GetColumnStatisticsTaskRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetColumnStatisticsTaskSettings  **
  - **IAM action:**  [glue:GetColumnStatisticsTaskSettings](#list_glue-action-GetColumnStatisticsTaskSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnection  **
  - **IAM action:**  [glue:GetConnection](#list_glue-action-GetConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnections  **
  - **IAM action:**  [glue:GetConnections](#list_glue-action-GetConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCrawler  **
  - **IAM action:**  [glue:GetCrawler](#list_glue-action-GetCrawler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCrawlerMetrics  **
  - **IAM action:**  [glue:GetCrawlerMetrics](#list_glue-action-GetCrawlerMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCrawlers  **
  - **IAM action:**  [glue:GetCrawlers](#list_glue-action-GetCrawlers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomEntityType  **
  - **IAM action:**  [glue:GetCustomEntityType](#list_glue-action-GetCustomEntityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDashboardUrl  **
  - **IAM action:**  [glue:GetDashboardUrl](#list_glue-action-GetDashboardUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataCatalogEncryptionSettings  **
  - **IAM action:**  [glue:GetDataCatalogEncryptionSettings](#list_glue-action-GetDataCatalogEncryptionSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityModel  **
  - **IAM action:**  [glue:GetDataQualityModel](#list_glue-action-GetDataQualityModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityModelResult  **
  - **IAM action:**  [glue:GetDataQualityModelResult](#list_glue-action-GetDataQualityModelResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityResult  **
  - **IAM action:**  [glue:GetDataQualityResult](#list_glue-action-GetDataQualityResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityRuleRecommendationRun  **
  - **IAM action:**  [glue:GetDataQualityRuleRecommendationRun](#list_glue-action-GetDataQualityRuleRecommendationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityRuleset  **
  - **IAM action:**  [glue:GetDataQualityRuleset](#list_glue-action-GetDataQualityRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataQualityRulesetEvaluationRun  **
  - **IAM action:**  [glue:GetDataQualityRulesetEvaluationRun](#list_glue-action-GetDataQualityRulesetEvaluationRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDatabase  **
  - **IAM action:**  [glue:GetDatabase](#list_glue-action-GetDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDatabases  **
  - **IAM action:**  [glue:GetDatabases](#list_glue-action-GetDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataflowGraph  **
  - **IAM action:**  [glue:GetDataflowGraph](#list_glue-action-GetDataflowGraph) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevEndpoint  **
  - **IAM action:**  [glue:GetDevEndpoint](#list_glue-action-GetDevEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDevEndpoints  **
  - **IAM action:**  [glue:GetDevEndpoints](#list_glue-action-GetDevEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEntityRecords  **
  - **IAM action:**  [glue:GetEntityRecords](#list_glue-action-GetEntityRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGlueIdentityCenterConfiguration  **
  - **IAM action:**  [glue:GetGlueIdentityCenterConfiguration](#list_glue-action-GetGlueIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrationResourceProperty  **
  - **IAM action:**  [glue:GetIntegrationResourceProperty](#list_glue-action-GetIntegrationResourceProperty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIntegrationTableProperties  **
  - **IAM action:**  [glue:GetIntegrationTableProperties](#list_glue-action-GetIntegrationTableProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [glue:GetJob](#list_glue-action-GetJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   GetJobBookmark  **
  - **IAM action:**  [glue:GetJobBookmark](#list_glue-action-GetJobBookmark) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobRun  **
  - **IAM action:**  [glue:GetJobRun](#list_glue-action-GetJobRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobRuns  **
  - **IAM action:**  [glue:GetJobRuns](#list_glue-action-GetJobRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobs  **
  - **IAM action:**  [glue:GetJobs](#list_glue-action-GetJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   GetMLTaskRun  **
  - **IAM action:**  [glue:GetMLTaskRun](#list_glue-action-GetMLTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMLTaskRuns  **
  - **IAM action:**  [glue:GetMLTaskRuns](#list_glue-action-GetMLTaskRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMLTransform  **
  - **IAM action:**  [glue:GetMLTransform](#list_glue-action-GetMLTransform) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMLTransforms  **
  - **IAM action:**  [glue:GetMLTransforms](#list_glue-action-GetMLTransforms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetMapping  **
  - **IAM action:**  [glue:GetMapping](#list_glue-action-GetMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPartition  **
  - **IAM action:**  [glue:GetPartition](#list_glue-action-GetPartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPartitions  **
  - **IAM action:**  [glue:GetPartitions](#list_glue-action-GetPartitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlan  **
  - **IAM action:**  [glue:GetPlan](#list_glue-action-GetPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistry  **
  - **IAM action:**  [glue:GetRegistry](#list_glue-action-GetRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchema  **
  - **IAM action:**  [glue:GetSchema](#list_glue-action-GetSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaByDefinition  **
  - **IAM action:**  [glue:GetSchemaByDefinition](#list_glue-action-GetSchemaByDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaVersion  **
  - **IAM action:**  [glue:GetSchemaVersion](#list_glue-action-GetSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSchemaVersionsDiff  **
  - **IAM action:**  [glue:GetSchemaVersionsDiff](#list_glue-action-GetSchemaVersionsDiff) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityConfiguration  **
  - **IAM action:**  [glue:GetSecurityConfiguration](#list_glue-action-GetSecurityConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityConfigurations  **
  - **IAM action:**  [glue:GetSecurityConfigurations](#list_glue-action-GetSecurityConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **IAM action:**  [glue:GetSession](#list_glue-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSessionEndpoint  **
  - **IAM action:**  [glue:GetSessionEndpoint](#list_glue-action-GetSessionEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStatement  **
  - **IAM action:**  [glue:GetStatement](#list_glue-action-GetStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTable  **
  - **IAM action:**  [glue:GetTable](#list_glue-action-GetTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [athena:GetTable](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetTableOptimizer  **
  - **IAM action:**  [glue:GetTableOptimizer](#list_glue-action-GetTableOptimizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableVersion  **
  - **IAM action:**  [glue:GetTableVersion](#list_glue-action-GetTableVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableVersions  **
  - **IAM action:**  [glue:GetTableVersions](#list_glue-action-GetTableVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTables  **
  - **IAM action:**  [glue:GetTables](#list_glue-action-GetTables)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [athena:GetTables](https://docs.aws.amazon.com/athena/latest/ug/connect-with-previous-jdbc.html#jdbc-prev-version-policies)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetTags  **
  - **IAM action:**  [glue:GetTags](#list_glue-action-GetTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrigger  **
  - **IAM action:**  [glue:GetTrigger](#list_glue-action-GetTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTriggers  **
  - **IAM action:**  [glue:GetTriggers](#list_glue-action-GetTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsageProfile  **
  - **IAM action:**  [glue:GetUsageProfile](#list_glue-action-GetUsageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserDefinedFunction  **
  - **IAM action:**  [glue:GetUserDefinedFunction](#list_glue-action-GetUserDefinedFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUserDefinedFunctions  **
  - **IAM action:**  [glue:GetUserDefinedFunctions](#list_glue-action-GetUserDefinedFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [glue:GetWorkflow](#list_glue-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowRun  **
  - **IAM action:**  [glue:GetWorkflowRun](#list_glue-action-GetWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowRunProperties  **
  - **IAM action:**  [glue:GetWorkflowRunProperties](#list_glue-action-GetWorkflowRunProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowRuns  **
  - **IAM action:**  [glue:GetWorkflowRuns](#list_glue-action-GetWorkflowRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCatalogToGlue  **
  - **IAM action:**  [glue:ImportCatalogToGlue](#list_glue-action-ImportCatalogToGlue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListBlueprints  **
  - **IAM action:**  [glue:ListBlueprints](#list_glue-action-ListBlueprints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListColumnStatisticsTaskRuns  **
  - **IAM action:**  [glue:ListColumnStatisticsTaskRuns](#list_glue-action-ListColumnStatisticsTaskRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectionTypes  **
  - **IAM action:**  [glue:ListConnectionTypes](#list_glue-action-ListConnectionTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ListCrawlers  **
  - **IAM action:**  [glue:ListCrawlers](#list_glue-action-ListCrawlers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCrawls  **
  - **IAM action:**  [glue:ListCrawls](#list_glue-action-ListCrawls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomEntityTypes  **
  - **IAM action:**  [glue:ListCustomEntityTypes](#list_glue-action-ListCustomEntityTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityResults  **
  - **IAM action:**  [glue:ListDataQualityResults](#list_glue-action-ListDataQualityResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityRuleRecommendationRuns  **
  - **IAM action:**  [glue:ListDataQualityRuleRecommendationRuns](#list_glue-action-ListDataQualityRuleRecommendationRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityRulesetEvaluationRuns  **
  - **IAM action:**  [glue:ListDataQualityRulesetEvaluationRuns](#list_glue-action-ListDataQualityRulesetEvaluationRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityRulesets  **
  - **IAM action:**  [glue:ListDataQualityRulesets](#list_glue-action-ListDataQualityRulesets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityStatisticAnnotations  **
  - **IAM action:**  [glue:GetDataQualityResult](#list_glue-action-GetDataQualityResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataQualityStatistics  **
  - **IAM action:**  [glue:GetDataQualityResult](#list_glue-action-GetDataQualityResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevEndpoints  **
  - **IAM action:**  [glue:ListDevEndpoints](#list_glue-action-ListDevEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEntities  **
  - **IAM action:**  [glue:ListEntities](#list_glue-action-ListEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ListIntegrationResourceProperties  **
  - **IAM action:**  [glue:ListIntegrationResourceProperties](#list_glue-action-ListIntegrationResourceProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [glue:ListJobs](#list_glue-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMLTransforms  **
  - **IAM action:**  [glue:ListMLTransforms](#list_glue-action-ListMLTransforms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegistries  **
  - **IAM action:**  [glue:ListRegistries](#list_glue-action-ListRegistries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemaVersions  **
  - **IAM action:**  [glue:ListSchemaVersions](#list_glue-action-ListSchemaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemas  **
  - **IAM action:**  [glue:ListSchemas](#list_glue-action-ListSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **IAM action:**  [glue:ListSessions](#list_glue-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStatements  **
  - **IAM action:**  [glue:ListStatements](#list_glue-action-ListStatements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTableOptimizerRuns  **
  - **IAM action:**  [glue:ListTableOptimizerRuns](#list_glue-action-ListTableOptimizerRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTriggers  **
  - **IAM action:**  [glue:ListTriggers](#list_glue-action-ListTriggers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsageProfiles  **
  - **IAM action:**  [glue:ListUsageProfiles](#list_glue-action-ListUsageProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [glue:ListWorkflows](#list_glue-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ModifyIntegration  **
  - **IAM action:**  [glue:ModifyIntegration](#list_glue-action-ModifyIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDataCatalogEncryptionSettings  **
  - **IAM action:**  [glue:PutDataCatalogEncryptionSettings](#list_glue-action-PutDataCatalogEncryptionSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   PutDataQualityProfileAnnotation  **
  - **IAM action:**  [glue:PutDataQualityProfileAnnotation](#list_glue-action-PutDataQualityProfileAnnotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutSchemaVersionMetadata  **
  - **IAM action:**  [glue:PutSchemaVersionMetadata](#list_glue-action-PutSchemaVersionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutWorkflowRunProperties  **
  - **IAM action:**  [glue:PutWorkflowRunProperties](#list_glue-action-PutWorkflowRunProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   QuerySchemaVersionMetadata  **
  - **IAM action:**  [glue:QuerySchemaVersionMetadata](#list_glue-action-QuerySchemaVersionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterConnectionType  **
  - **IAM action:**  [glue:RegisterConnectionType](#list_glue-action-RegisterConnectionType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RegisterSchemaVersion  **
  - **IAM action:**  [glue:RegisterSchemaVersion](#list_glue-action-RegisterSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveSchemaVersionMetadata  **
  - **IAM action:**  [glue:RemoveSchemaVersionMetadata](#list_glue-action-RemoveSchemaVersionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetJobBookmark  **
  - **IAM action:**  [glue:ResetJobBookmark](#list_glue-action-ResetJobBookmark) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResumeWorkflowRun  **
  - **IAM action:**  [glue:ResumeWorkflowRun](#list_glue-action-ResumeWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RunStatement  **
  - **IAM action:**  [glue:RunStatement](#list_glue-action-RunStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchTables  **
  - **IAM action:**  [glue:SearchTables](#list_glue-action-SearchTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartBlueprintRun  **
  - **IAM action:**  [glue:StartBlueprintRun](#list_glue-action-StartBlueprintRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   StartColumnStatisticsTaskRun  **
  - **IAM action:**  [glue:StartColumnStatisticsTaskRun](#list_glue-action-StartColumnStatisticsTaskRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   StartColumnStatisticsTaskRunSchedule  **
  - **IAM action:**  [glue:StartColumnStatisticsTaskRunSchedule](#list_glue-action-StartColumnStatisticsTaskRunSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCrawler  **
  - **IAM action:**  [glue:StartCrawler](#list_glue-action-StartCrawler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCrawlerSchedule  **
  - **IAM action:**  [glue:StartCrawlerSchedule](#list_glue-action-StartCrawlerSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDataQualityRuleRecommendationRun  **
  - **IAM action:**  [glue:StartDataQualityRuleRecommendationRun](#list_glue-action-StartDataQualityRuleRecommendationRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   StartDataQualityRulesetEvaluationRun  **
  - **IAM action:**  [glue:StartDataQualityRulesetEvaluationRun](#list_glue-action-StartDataQualityRulesetEvaluationRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   StartExportLabelsTaskRun  **
  - **IAM action:**  [glue:StartExportLabelsTaskRun](#list_glue-action-StartExportLabelsTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImportLabelsTaskRun  **
  - **IAM action:**  [glue:StartImportLabelsTaskRun](#list_glue-action-StartImportLabelsTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartJobRun  **
  - **IAM action:**  [glue:GetUsageProfile](#list_glue-action-GetUsageProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:StartJobRun](#list_glue-action-StartJobRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartMLEvaluationTaskRun  **
  - **IAM action:**  [glue:StartMLEvaluationTaskRun](#list_glue-action-StartMLEvaluationTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMLLabelingSetGenerationTaskRun  **
  - **IAM action:**  [glue:StartMLLabelingSetGenerationTaskRun](#list_glue-action-StartMLLabelingSetGenerationTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTrigger  **
  - **IAM action:**  [glue:StartTrigger](#list_glue-action-StartTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartWorkflowRun  **
  - **IAM action:**  [glue:StartWorkflowRun](#list_glue-action-StartWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopColumnStatisticsTaskRun  **
  - **IAM action:**  [glue:StopColumnStatisticsTaskRun](#list_glue-action-StopColumnStatisticsTaskRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopColumnStatisticsTaskRunSchedule  **
  - **IAM action:**  [glue:StopColumnStatisticsTaskRunSchedule](#list_glue-action-StopColumnStatisticsTaskRunSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCrawler  **
  - **IAM action:**  [glue:StopCrawler](#list_glue-action-StopCrawler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCrawlerSchedule  **
  - **IAM action:**  [glue:StopCrawlerSchedule](#list_glue-action-StopCrawlerSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSession  **
  - **IAM action:**  [glue:StopSession](#list_glue-action-StopSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTrigger  **
  - **IAM action:**  [glue:StopTrigger](#list_glue-action-StopTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopWorkflowRun  **
  - **IAM action:**  [glue:StopWorkflowRun](#list_glue-action-StopWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [glue:TagResource](#list_glue-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestConnection  **
  - **IAM action:**  [glue:TestConnection](#list_glue-action-TestConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [glue:UntagResource](#list_glue-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBlueprint  **
  - **IAM action:**  [glue:UpdateBlueprint](#list_glue-action-UpdateBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCatalog  **
  - **IAM action:**  [glue:UpdateCatalog](#list_glue-action-UpdateCatalog)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateClassifier  **
  - **IAM action:**  [glue:UpdateClassifier](#list_glue-action-UpdateClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateColumnStatisticsForPartition  **
  - **IAM action:**  [glue:UpdatePartition](#list_glue-action-UpdatePartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateColumnStatisticsForTable  **
  - **IAM action:**  [glue:UpdateTable](#list_glue-action-UpdateTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateColumnStatisticsTaskSettings  **
  - **IAM action:**  [glue:UpdateColumnStatisticsTaskSettings](#list_glue-action-UpdateColumnStatisticsTaskSettings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateConnection  **
  - **IAM action:**  [glue:UpdateConnection](#list_glue-action-UpdateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateCrawler  **
  - **IAM action:**  [glue:UpdateCrawler](#list_glue-action-UpdateCrawler)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateCrawlerSchedule  **
  - **IAM action:**  [glue:UpdateCrawlerSchedule](#list_glue-action-UpdateCrawlerSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataQualityRuleset  **
  - **IAM action:**  [glue:UpdateDataQualityRuleset](#list_glue-action-UpdateDataQualityRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDatabase  **
  - **IAM action:**  [glue:UpdateDatabase](#list_glue-action-UpdateDatabase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDevEndpoint  **
  - **IAM action:**  [glue:UpdateDevEndpoint](#list_glue-action-UpdateDevEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGlueIdentityCenterConfiguration  **
  - **IAM action:**  [glue:UpdateGlueIdentityCenterConfiguration](#list_glue-action-UpdateGlueIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntegrationResourceProperty  **
  - **IAM action:**  [glue:UpdateIntegrationResourceProperty](#list_glue-action-UpdateIntegrationResourceProperty)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateIntegrationTableProperties  **
  - **IAM action:**  [glue:UpdateIntegrationTableProperties](#list_glue-action-UpdateIntegrationTableProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJob  **
  - **IAM action:**  [glue:GetUsageProfile](#list_glue-action-GetUsageProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glue:UpdateJob](#list_glue-action-UpdateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateJobFromSourceControl  **
  - **IAM action:**  [glue:UpdateJobFromSourceControl](#list_glue-action-UpdateJobFromSourceControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMLTransform  **
  - **IAM action:**  [glue:UpdateMLTransform](#list_glue-action-UpdateMLTransform)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdatePartition  **
  - **IAM action:**  [glue:UpdatePartition](#list_glue-action-UpdatePartition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegistry  **
  - **IAM action:**  [glue:UpdateRegistry](#list_glue-action-UpdateRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSchema  **
  - **IAM action:**  [glue:UpdateSchema](#list_glue-action-UpdateSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSourceControlFromJob  **
  - **IAM action:**  [glue:UpdateSourceControlFromJob](#list_glue-action-UpdateSourceControlFromJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTable  **
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:UpdateTable](#list_glue-action-UpdateTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateTableOptimizer  **
  - **IAM action:**  [glue:PassConnection](#list_glue-action-PassConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [glue:UpdateTableOptimizer](#list_glue-action-UpdateTableOptimizer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** glue.amazonaws.com / **Access level:** Write

- **   UpdateTrigger  **
  - **IAM action:**  [glue:UpdateTrigger](#list_glue-action-UpdateTrigger) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUsageProfile  **
  - **IAM action:**  [glue:UpdateUsageProfile](#list_glue-action-UpdateUsageProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserDefinedFunction  **
  - **IAM action:**  [glue:UpdateUserDefinedFunction](#list_glue-action-UpdateUserDefinedFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflow  **
  - **IAM action:**  [glue:UpdateWorkflow](#list_glue-action-UpdateWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Glue
<a name="list_glue-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreatePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-BatchCreatePartition)  **
  - **Description:** Grants permission to create one or more partitions
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [BatchDeleteConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-BatchDeleteConnection)  **
  - **Description:** Grants permission to delete one or more connections
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [BatchDeletePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-BatchDeletePartition)  **
  - **Description:** Grants permission to delete one or more partitions
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [BatchDeleteTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-BatchDeleteTable)  **
  - **Description:** Grants permission to delete one or more tables
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [BatchDeleteTableVersion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-DeleteTableVersion)  **
  - **Description:** Grants permission to delete one or more versions of a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [BatchGetBlueprints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-BatchGetBlueprints)  **
  - **Description:** Grants permission to retrieve one or more blueprints
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCrawlers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-BatchGetCrawlers)  **
  - **Description:** Grants permission to retrieve one or more crawlers
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetCustomEntityTypes](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html#aws-glue-api-sensitive-data-api-BatchGetCustomEntityTypes)  **
  - **Description:** Grants permission to retrieve one or more Custom Entity Types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetDevEndpoints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-BatchGetDevEndpoints)  **
  - **Description:** Grants permission to retrieve one or more development endpoints
  - **Resource types (\*required):** [devendpoint\*](#list_glue-resource-devendpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetJobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-BatchGetJobs)  **
  - **Description:** Grants permission to retrieve one or more jobs
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetPartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-BatchGetPartition)  **
  - **Description:** Grants permission to retrieve one or more partitions
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [BatchGetStageFiles](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to batch get stage files for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [BatchGetTableOptimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-BatchGetTableOptimizer)  **
  - **Description:** Grants permission to return the configuration for the specified table optimizers
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetTriggers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-BatchGetTriggers)  **
  - **Description:** Grants permission to retrieve one or more triggers
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetWorkflows](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-BatchGetWorkflows)  **
  - **Description:** Grants permission to retrieve one or more workflows
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchStopJobRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-runs-BatchStopStartJobRun)  **
  - **Description:** Grants permission to stop one or more job runs for a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdatePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-BatchUpdatePartition)  **
  - **Description:** Grants permission to update one or more partitions
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CancelDataQualityRuleRecommendationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-CancelDataQualityRuleRecommendationRun)  **
  - **Description:** Grants permission to stop a running Data Quality rule recommendation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelDataQualityRulesetEvaluationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-CancelDataQualityRulesetEvaluationRun)  **
  - **Description:** Grants permission to stop a running Data Quality ruleset evaluation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelMLTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-CancelMLTaskRun)  **
  - **Description:** Grants permission to stop a running ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelStatement](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-CancelStatement)  **
  - **Description:** Grants permission to cancel a statement in an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckSchemaVersionValidity](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-CheckSchemaVersionValidity)  **
  - **Description:** Grants permission to retrieve a check the validity of schema version
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateBlueprint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-CreateBlueprint)  **
  - **Description:** Grants permission to create a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCatalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to create a catalog
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateClassifier](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-CreateClassifier)  **
  - **Description:** Grants permission to create a classifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateColumnStatisticsTaskSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-CreateColumnStatisticsTaskSettings)  **
  - **Description:** Grants permission to create settings for a column statistics task
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-CreateConnection)  **
  - **Description:** Grants permission to create a connection
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-CreateCrawler)  **
  - **Description:** Grants permission to create a crawler
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomEntityType](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html#aws-glue-api-sensitive-data-api-CreateCustomEntityType)  **
  - **Description:** Grants permission to create a Custom Entity Type
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-CreateDataQualityRuleset)  **
  - **Description:** Grants permission to create a Data Quality ruleset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatabase](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-CreateDatabase)  **
  - **Description:** Grants permission to create a database
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateDevEndpoint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-CreateDevEndpoint)  **
  - **Description:** Grants permission to create a development endpoint
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGlueIdentityCenterConfiguration](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-getting-started.html#security-trusted-identity-propagation-connecting)  **
  - **Description:** Grants permission to connect Glue with Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIntegration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-CreateIntegration)  **
  - **Description:** Grants permission to create an integration
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [integration\*](#list_glue-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegrationResourceProperty](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-CreateIntegrationResourceProperty)  **
  - **Description:** Grants permission to create integration resource property
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [integrationResourceProperty\*](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegrationTableProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-CreateIntegrationTableProperties)  **
  - **Description:** Grants permission to create integration table properties
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-CreateJob)  **
  - **Description:** Grants permission to create a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:SecurityGroupIds](#list_glue-glue_SecurityGroupIds)<br />[glue:SubnetIds](#list_glue-glue_SubnetIds)<br />[glue:VpcIds](#list_glue-glue_VpcIds)
  - **Access level:** Write

- **   [CreateMLTransform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-CreateMLTransform)  **
  - **Description:** Grants permission to create an ML Transform
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-CreatePartition)  **
  - **Description:** Grants permission to create a partition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreatePartitionIndex](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-CreatePartitionIndex)  **
  - **Description:** Grants permission to create a specified partition index in an existing table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateRegistry](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-CreateRegistry)  **
  - **Description:** Grants permission to create a new schema registry
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchema](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-CreateSchema)  **
  - **Description:** Grants permission to create a new schema container
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScript](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html#aws-glue-api-etl-script-generation-CreateScript)  **
  - **Description:** Grants permission to create a script
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSecurityConfiguration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-CreateSecurityConfiguration)  **
  - **Description:** Grants permission to create a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-api-interactive-sessions-CreateSession)  **
  - **Description:** Grants permission to create an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:SecurityGroupIds](#list_glue-glue_SecurityGroupIds)<br />[glue:SubnetIds](#list_glue-glue_SubnetIds)<br />[glue:VpcIds](#list_glue-glue_VpcIds)
  - **Access level:** Write

- **   [CreateTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-CreateTable)  **
  - **Description:** Grants permission to create a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateTableOptimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-CreateTableOptimizer)  **
  - **Description:** Grants permission to create a new table optimizer for a specific function. Compaction is the only currently supported optimizer type
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-CreateTrigger)  **
  - **Description:** Grants permission to create a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUsageProfile](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html#aws-glue-api-usage-profiles-CreateUsageProfile)  **
  - **Description:** Grants permission to create a usage profile
  - **Resource types (\*required):** [usageProfile\*](#list_glue-resource-usageProfile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUserDefinedFunction](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html#aws-glue-api-catalog-functions-CreateUserDefinedFunction)  **
  - **Description:** Grants permission to create a function definition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [CreateWorkflow](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-CreateWorkflow)  **
  - **Description:** Grants permission to create a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBlueprint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-DeleteBlueprint)  **
  - **Description:** Grants permission to delete a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCatalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to delete a catalog
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteClassifier](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-DeleteClassifier)  **
  - **Description:** Grants permission to delete a classifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteColumnStatisticsForPartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-DeleteColumnStatisticsForPartition)  **
  - **Description:** Grants permission to delete the partition column statistics of a column
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-DeleteColumnStatisticsForTable)  **
  - **Description:** Grants permission to delete the table statistics of columns
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteColumnStatisticsTaskSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-DeleteColumnStatisticsTaskSettings)  **
  - **Description:** Grants permission to delete settings for a column statistics task
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-DeleteConnection)  **
  - **Description:** Grants permission to delete a connection
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteConnectionType](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to delete connection type
  - **Resource types (\*required):** [connectionType\*](#list_glue-resource-connectionType)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-DeleteCrawler)  **
  - **Description:** Grants permission to delete a crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomEntityType](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html#aws-glue-api-sensitive-data-api-DeleteCustomEntityType)  **
  - **Description:** Grants permission to delete a Custom Entity Type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-DeleteDataQualityRuleset)  **
  - **Description:** Grants permission to delete a Data Quality ruleset
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatabase](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-DeleteDatabase)  **
  - **Description:** Grants permission to delete a database
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [userdefinedfunction\*](#list_glue-resource-userdefinedfunction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteDevEndpoint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-DeleteDevEndpoint)  **
  - **Description:** Grants permission to delete a development endpoint
  - **Resource types (\*required):** [devendpoint\*](#list_glue-resource-devendpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGlueIdentityCenterConfiguration](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-getting-started.html#security-trusted-identity-propagation-connecting)  **
  - **Description:** Grants permission to disconnect Glue with Identity Center
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIntegration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-DeleteIntegration)  **
  - **Description:** Grants permission to delete an integration
  - **Resource types (\*required):** [integration\*](#list_glue-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegrationResourceProperty](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-DeleteIntegrationResourceProperty)  **
  - **Description:** Grants permission to delete the integration resource property
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrationResourceProperty\*](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegrationTableProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-DeleteIntegrationTableProperties)  **
  - **Description:** Grants permission to delete integration table properties
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-DeleteJob)  **
  - **Description:** Grants permission to delete a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMLTransform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-DeleteMLTransform)  **
  - **Description:** Grants permission to delete an ML Transform
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-DeletePartition)  **
  - **Description:** Grants permission to delete a partition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeletePartitionIndex](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-DeletePartitionIndex)  **
  - **Description:** Grants permission to delete a specified partition index from an existing table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteRegistry](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-DeleteRegistry)  **
  - **Description:** Grants permission to delete a schema registry
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-DeleteResourcePolicy)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DeleteSchema](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-DeleteSchema)  **
  - **Description:** Grants permission to delete a schema container
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchemaVersions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-DeleteSchemaVersions)  **
  - **Description:** Grants permission to delete a range of schema versions
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityConfiguration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-DeleteSecurityConfiguration)  **
  - **Description:** Grants permission to delete a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSession](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-DeleteSession)  **
  - **Description:** Grants permission to delete an interactive session after stopping the session if not already stopped
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-DeleteTable)  **
  - **Description:** Grants permission to delete a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteTableOptimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-DeleteTableOptimizer)  **
  - **Description:** Grants permission to delete an optimizer and all associated metadata for a table. The optimization will no longer be performed on the table
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTableVersion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-DeleteTableVersion)  **
  - **Description:** Grants permission to delete a version of a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-DeleteTrigger)  **
  - **Description:** Grants permission to delete a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUsageProfile](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html#aws-glue-api-usage-profiles-DeleteUsageProfile)  **
  - **Description:** Grants permission to delete a usage profile
  - **Resource types (\*required):** [usageProfile\*](#list_glue-resource-usageProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserDefinedFunction](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html#aws-glue-api-catalog-functions-DeleteUserDefinedFunction)  **
  - **Description:** Grants permission to delete a function definition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [userdefinedfunction\*](#list_glue-resource-userdefinedfunction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-DeleteWorkflow)  **
  - **Description:** Grants permission to delete a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterDataPreview](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to terminate Glue Studio Notebook session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DescribeConnectionType](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to describe connection type in glue
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DescribeEntity](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to describe entity in glue studio
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DescribeInboundIntegrations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-DescribeInboundIntegrations)  **
  - **Description:** Grants permission to list the inbound integrations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeIntegrations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-DescribeIntegrations)  **
  - **Description:** Grants permission to describe zero-ETL integrations
  - **Resource types (\*required):** [integration\*](#list_glue-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [FederateAuthorization](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to read and write redshift federated resources
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)
  - **Access level:** Write

- **   [GetBlueprint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetBlueprint)  **
  - **Description:** Grants permission to retrieve a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlueprintRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetBlueprintRun)  **
  - **Description:** Grants permission to retrieve a blueprint run
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlueprintRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetBlueprintRuns)  **
  - **Description:** Grants permission to retrieve all runs of a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCatalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to retrieve a catalog
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetCatalogImportStatus](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-migration.html#aws-glue-api-catalog-migration-GetCatalogImportStatus)  **
  - **Description:** Grants permission to retrieve the catalog import status
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog)
  - **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetCatalogs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to retrieve all catalogs
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:EnabledForRedshiftAutoDiscovery](#list_glue-glue_EnabledForRedshiftAutoDiscovery)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetClassifier](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-GetClassifier)  **
  - **Description:** Grants permission to retrieve a classifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetClassifiers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-GetClassifiers)  **
  - **Description:** Grants permission to list all classifiers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetColumnStatisticsForPartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-GetColumnStatisticsForPartition)  **
  - **Description:** Grants permission to retrieve partition statistics of columns
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetColumnStatisticsForTable)  **
  - **Description:** Grants permission to retrieve table statistics of columns
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetColumnStatisticsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRun)  **
  - **Description:** Grants permission to retrieve Column Statistics run information for the table based on run-id
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetColumnStatisticsTaskRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskRuns)  **
  - **Description:** Grants permission to retrieve Column Statistics run information for the table based on run-ids
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetColumnStatisticsTaskSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-GetColumnStatisticsTaskSettings)  **
  - **Description:** Grants permission to retrieve settings for a column statistics task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCompletion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html#)  **
  - **Description:** Grants permission to get generated response for a completion request in Glue from AWS Q
  - **Resource types (\*required):** [completion\*](#list_glue-resource-completion)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-GetConnection)  **
  - **Description:** Grants permission to retrieve a connection
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetConnections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-GetConnections)  **
  - **Description:** Grants permission to retrieve a list of connections
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-GetCrawler)  **
  - **Description:** Grants permission to retrieve a crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCrawlerMetrics](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-GetCrawlerMetrics)  **
  - **Description:** Grants permission to retrieve metrics about crawlers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCrawlers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-GetCrawlers)  **
  - **Description:** Grants permission to retrieve all crawlers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomEntityType](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html#aws-glue-api-sensitive-data-api-GetCustomEntityType)  **
  - **Description:** Grants permission to read a Custom Entity Type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDashboardUrl](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html)  **
  - **Description:** Grants permission to generate presigned url for accessing spark live UI
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataCatalogEncryptionSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-GetDataCatalogEncryptionSettings)  **
  - **Description:** Grants permission to retrieve catalog encryption settings
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataPreviewStatement](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to get Data Preview Statement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetDataQualityModel](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityModel)  **
  - **Description:** Grants permission to retrieve the training status of the prediction model for a statistic
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job\*](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityModelResult](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityModelResult)  **
  - **Description:** Grants permission to retrieve the predictions for a statistic from the latest model
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job\*](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityResult](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityResult)  **
  - **Description:** Grants permission to retrieve a Data Quality result
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityRuleRecommendationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityRuleRecommendationRun)  **
  - **Description:** Grants permission to retrieve a Data Quality rule recommendation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityRuleset)  **
  - **Description:** Grants permission to retrieve a Data Quality ruleset
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataQualityRulesetEvaluationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-GetDataQualityRulesetEvaluationRun)  **
  - **Description:** Grants permission to retrieve a Data Quality rule recommendation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDatabase](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-GetDatabase)  **
  - **Description:** Grants permission to retrieve a database
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetDatabases](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-GetDatabases)  **
  - **Description:** Grants permission to retrieve all databases
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetDataflowGraph](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html#aws-glue-api-etl-script-generation-GetDataflowGraph)  **
  - **Description:** Grants permission to transform a script into a directed acyclic graph (DAG)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDevEndpoint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-GetDevEndpoint)  **
  - **Description:** Grants permission to retrieve a development endpoint
  - **Resource types (\*required):** [devendpoint\*](#list_glue-resource-devendpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDevEndpoints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-GetDevEndpoints)  **
  - **Description:** Grants permission to retrieve all development endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEntityRecords](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to preview entity records in glue
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get environment details for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetExecutors](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get executors for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetExecutorsThreads](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get executor threads for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetGeneratedCode](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html#aws-glue-api-etl-script-generation-GetGeneratedCode)  **
  - **Description:** Transforms a directed acyclic graph (DAG) into code
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGlueIdentityCenterConfiguration](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-getting-started.html#security-trusted-identity-propagation-connecting)  **
  - **Description:** Grants permission to retrieve the managed Idc application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIntegrationResourceProperty](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-GetIntegrationResourceProperty)  **
  - **Description:** Grants permission to retrieve the integration resource property
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrationResourceProperty\*](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegrationTableProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-GetIntegrationTableProperties)  **
  - **Description:** Grants permission to retrieve the integration table properties
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-GetJob)  **
  - **Description:** Grants permission to retrieve a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobBookmark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-job-GetJobBookmark)  **
  - **Description:** Grants permission to retrieve a job bookmark
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJobRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-runs-GetJobRun)  **
  - **Description:** Grants permission to retrieve a job run
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-runs-GetJobRuns)  **
  - **Description:** Grants permission to retrieve all job runs of a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobUpgradeAnalysis](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-upgrade-analysis.html#aws-glue-api-upgrade-analysis-GetJobUpgradeAnalysis)  **
  - **Description:** Grants permission to retrieve an upgrade analysis for a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetJobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-GetJobs)  **
  - **Description:** Grants permission to retrieve all current jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLogParsingStatus](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get log parsing status for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetMLTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-GetMLTaskRun)  **
  - **Description:** Grants permission to retrieve an ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMLTaskRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-GetMLTaskRuns)  **
  - **Description:** Grants permission to retrieve all ML Task Runs
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetMLTransform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-GetMLTransform)  **
  - **Description:** Grants permission to retrieve an ML Transform
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMLTransforms](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-GetMLTransforms)  **
  - **Description:** Grants permission to retrieve all ML Transforms
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetMapping](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html#aws-glue-api-etl-script-generation-GetMapping)  **
  - **Description:** Grants permission to create a mapping
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotebookInstanceStatus](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to retrieve Glue Studio Notebooks session status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetPartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-GetPartition)  **
  - **Description:** Grants permission to retrieve a partition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetPartitionIndexes](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetPartitionIndexes)  **
  - **Description:** Grants permission to retrieve partition indexes for a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetPartitions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-GetPartitions)  **
  - **Description:** Grants permission to retrieve the partitions of a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetPlan](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html#aws-glue-api-etl-script-generation-GetPlan)  **
  - **Description:** Grants permission to retrieve a mapping for a script
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQueries](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get queries for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetQuery](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get a specific query for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetRecipeAction](https://docs.aws.amazon.com/glue/latest/ug/setting-up.html#getting-started-min-privs)  **
  - **Description:** Grants permission to get the result of a Data Preparation Recipe statement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetRegistry](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-GetRegistry)  **
  - **Description:** Grants permission to retrieve a schema registry
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicies](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-GetResourcePolicies)  **
  - **Description:** Grants permission to retrieve resource policies
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-GetResourcePolicy)  **
  - **Description:** Grants permission to retrieve a resource policy
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchema](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-GetSchema)  **
  - **Description:** Grants permission to retrieve a schema container
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaByDefinition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-GetSchemaByDefinition)  **
  - **Description:** Grants permission to retrieve a schema version based on schema definition
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaVersion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-GetSchemaVersion)  **
  - **Description:** Grants permission to retrieve a schema version
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSchemaVersionsDiff](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-GetSchemaVersionsDiff)  **
  - **Description:** Grants permission to compare two schema versions in schema registry
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSecurityConfiguration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-GetSecurityConfiguration)  **
  - **Description:** Grants permission to retrieve a security configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSecurityConfigurations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-GetSecurityConfigurations)  **
  - **Description:** Grants permission to retrieve one or more security configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-GetSession)  **
  - **Description:** Grants permission to retrieve an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSessionEndpoint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-GetSessionEndpoint)  **
  - **Description:** Grants permission to retrieve an interactive session endpoint
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStage](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get a stage for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStageAttempt](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get a stage attempt for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStageAttemptTaskList](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get the task list for a stage attempt for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStageAttemptTaskSummary](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get the task summary for a stage attempt for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStageFiles](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get stage files for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStages](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get stages for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStatement](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-GetStatement)  **
  - **Description:** Grants permission to retrieve result and information about a statement in an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStorage](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get storage details for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetStorageUnit](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to get storage unit details for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetTable)  **
  - **Description:** Grants permission to retrieve a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetTableOptimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-GetTableOptimizer)  **
  - **Description:** Grants permission to return the configuration of all optimizers associated with a specified table
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTableVersion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetTableVersion)  **
  - **Description:** Grants permission to retrieve a version of a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetTableVersions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetTableVersions)  **
  - **Description:** Grants permission to retrieve a list of versions of a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetTables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-GetTables)  **
  - **Description:** Grants permission to retrieve the tables in a database
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetTags](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-tags.html#aws-glue-api-tags-UntagResource)  **
  - **Description:** Grants permission to retrieve all tags associated with a resource
  - **Resource types (\*required):** [blueprint](#list_glue-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [crawler](#list_glue-resource-crawler) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [customEntityType](#list_glue-resource-customEntityType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [devendpoint](#list_glue-resource-devendpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trigger](#list_glue-resource-trigger) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [usageProfile](#list_glue-resource-usageProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow](#list_glue-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-GetTrigger)  **
  - **Description:** Grants permission to retrieve a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTriggers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-GetTriggers)  **
  - **Description:** Grants permission to retrieve the triggers associated with a job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUsageProfile](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html#aws-glue-api-usage-profiles-GetUsageProfile)  **
  - **Description:** Grants permission to retrieve a usage profile
  - **Resource types (\*required):** [usageProfile\*](#list_glue-resource-usageProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUserDefinedFunction](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html#aws-glue-api-catalog-functions-GetUserDefinedFunction)  **
  - **Description:** Grants permission to retrieve a function definition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [userdefinedfunction\*](#list_glue-resource-userdefinedfunction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetUserDefinedFunctions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html#aws-glue-api-catalog-functions-GetUserDefinedFunctions)  **
  - **Description:** Grants permission to retrieve multiple function definitions
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [userdefinedfunction\*](#list_glue-resource-userdefinedfunction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetWorkflow)  **
  - **Description:** Grants permission to retrieve a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetWorkflowRun)  **
  - **Description:** Grants permission to retrieve a workflow run
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowRunProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetWorkflowRunProperties)  **
  - **Description:** Grants permission to retrieve workflow run properties
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-GetWorkflowRuns)  **
  - **Description:** Grants permission to retrieve all runs of a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GlueNotebookAuthorize](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to access Glue Studio Notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GlueNotebookRefreshCredentials](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to refresh Glue Studio Notebooks credentials
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ImportCatalogToGlue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-migration.html#aws-glue-api-catalog-migration-ImportCatalogToGlue)  **
  - **Description:** Grants permission to import an Athena data catalog into AWS Glue
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog)
  - **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [ListBlueprints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-ListBlueprints)  **
  - **Description:** Grants permission to retrieve all blueprints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListColumnStatisticsTaskRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-ListColumnStatisticsTaskRuns)  **
  - **Description:** Grants permission to list all Column Statistics run-ids that have been executed for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConnectionTypes](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to list connection types in glue
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ListCrawlers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-ListCrawlers)  **
  - **Description:** Grants permission to retrieve all crawlers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCrawls](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-ListCrawls)  **
  - **Description:** Grants permission to retrieve crawl run history for a crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomEntityTypes](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html#aws-glue-api-sensitive-data-api-ListGetCustomEntityTypes)  **
  - **Description:** Grants permission to retrieve all Custom Entity Types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataQualityResults](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-ListDataQualityResults)  **
  - **Description:** Grants permission to retrieve all Data Quality results
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataQualityRuleRecommendationRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-ListDataQualityRuleRecommendationRuns)  **
  - **Description:** Grants permission to retrieve all Data Quality rule recommendation runs
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataQualityRulesetEvaluationRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-ListDataQualityRulesetEvaluationRuns)  **
  - **Description:** Grants permission to retrieve all Data Quality rule recommendation runs
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataQualityRulesets](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-ListDataQualityRulesets)  **
  - **Description:** Grants permission to retrieve a list of Data Quality rulesets
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDevEndpoints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-ListDevEndpoints)  **
  - **Description:** Grants permission to retrieve all development endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEntities](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to list entities in glue studio
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ListIntegrationResourceProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-ListIntegrationResourceProperties)  **
  - **Description:** Grants permission to list zero-ETL integration resource properties
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrationResourceProperty\*](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobUpgradeAnalyses](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-upgrade-analysis.html#aws-glue-api-upgrade-analysis-ListJobUpgradeAnalyses)  **
  - **Description:** Grants permission to list upgrade analyses for a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-ListJobs)  **
  - **Description:** Grants permission to retrieve all current jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMLTransforms](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-ListMLTransforms)  **
  - **Description:** Grants permission to retrieve all ML Transforms
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRegistries](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-ListRegistries)  **
  - **Description:** Grants permission to retrieve a list of schema registries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchemaVersions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-ListSchemaVersions)  **
  - **Description:** Grants permission to retrieve a list of schema versions
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSchemas](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-ListSchemas)  **
  - **Description:** Grants permission to retrieve a list of schema containers
  - **Resource types (\*required):** [registry](#list_glue-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-ListSessions)  **
  - **Description:** Grants permission to retrieve a list of interactive session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStatements](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-ListStatements)  **
  - **Description:** Grants permission to retrieve a list of statements in an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTableOptimizerRuns](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-ListTableOptimizerRuns)  **
  - **Description:** Grants permission to list the history of previous optimizer runs for a specific table
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTriggers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-ListTriggers)  **
  - **Description:** Grants permission to retrieve all triggers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsageProfiles](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html#aws-glue-api-usage-profiles-ListUsageProfiles)  **
  - **Description:** Grants permission to retrieve a list of usage profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-ListWorkflows)  **
  - **Description:** Grants permission to retrieve all workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ManagedConnector](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to use Glue managed connectors to query data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ModifyIntegration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-ModifyIntegration)  **
  - **Description:** Grants permission to modify a zero-ETL integration
  - **Resource types (\*required):** [integration\*](#list_glue-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [NotifyEvent](https://docs.aws.amazon.com/glue/latest/dg/starting-workflow-eventbridge.html)  **
  - **Description:** Grants permission to notify an event to the event-driven workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDataCatalogEncryptionSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-PutDataCatalogEncryptionSettings)  **
  - **Description:** Grants permission to update catalog encryption settings
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDataQualityProfileAnnotation](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-PutDataQualityProfileAnnotation)  **
  - **Description:** Grants permission to annotate all datapoints for a profile
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job\*](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDataQualityStatisticAnnotation](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-BatchPutDataQualityStatisticAnnotation)  **
  - **Description:** Grants permission to annotate datapoints over time for a specific data quality statistic
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job\*](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html#aws-glue-api-jobs-security-PutResourcePolicy)  **
  - **Description:** Grants permission to update a resource policy
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutSchemaVersionMetadata](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-PutSchemaVersionMetadata)  **
  - **Description:** Grants permission to add metadata to schema version
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutWorkflowRunProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-PutWorkflowRunProperties)  **
  - **Description:** Grants permission to update workflow run properties
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [QuerySchemaVersionMetadata](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-QuerySchemaVersionMetadata)  **
  - **Description:** Grants permission to fetch metadata for a schema version
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RefreshOAuth2Tokens](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to refresh the oauth2 tokens for connection during job execution
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RegisterConnectionType](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html#connection-type-permissions-operations)  **
  - **Description:** Grants permission to register connection type
  - **Resource types (\*required):** [connectionType\*](#list_glue-resource-connectionType)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)
  - **Access level:** Write

- **   [RegisterSchemaVersion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-RegisterSchemaVersion)  **
  - **Description:** Grants permission to create a new schema version
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveSchemaVersionMetadata](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-RemoveSchemaVersionMetadata)  **
  - **Description:** Grants permission to remove metadata from schema version
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RenameTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-RenameTable)  **
  - **Description:** Grants permission to rename a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [RequestLogParsing](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)  **
  - **Description:** Grants permission to request log parsing for SparkUI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ResetJobBookmark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-runs-ResetJobBookmark)  **
  - **Description:** Grants permission to reset a job bookmark
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ResumeWorkflowRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-ResumeWorkflowRun)  **
  - **Description:** Grants permission to resume a workflow run
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RunDataPreviewStatement](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to run Data Preview Statement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RunStatement](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-RunStatement)  **
  - **Description:** Grants permission to run a code or statement in an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchTables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-SearchTables)  **
  - **Description:** Grants permission to retrieve the tables in the catalog
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Read

- **   [SendFeedback](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html#)  **
  - **Description:** Grants permission to provide feedback about a glue completion experience in AWS Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendRecipeAction](https://docs.aws.amazon.com/glue/latest/ug/setting-up.html#getting-started-min-privs)  **
  - **Description:** Grants permission to execute a Data Preparation Recipe statement in data preview
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartBlueprintRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-StartBlueprintRun)  **
  - **Description:** Grants permission to start running a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartColumnStatisticsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRun)  **
  - **Description:** Grants permission to start a run for generating Column Statistics for the table
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartColumnStatisticsTaskRunSchedule](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-StartColumnStatisticsTaskRunSchedule)  **
  - **Description:** Grants permission to start a column statistics task run schedule
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCompletion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html#)  **
  - **Description:** Grants permission to create a completion request in Glue for AWS Q experience
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-StartCrawler)  **
  - **Description:** Grants permission to start a crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCrawlerSchedule](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-scheduler.html#aws-glue-api-crawler-scheduler-StartCrawlerSchedule)  **
  - **Description:** Grants permission to change the schedule state of a crawler to SCHEDULED
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDataQualityRuleRecommendationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-StartDataQualityRuleRecommendationRun)  **
  - **Description:** Grants permission to start a Data Quality rule recommendation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDataQualityRulesetEvaluationRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-StartDataQualityRulesetEvaluationRun)  **
  - **Description:** Grants permission to start a Data Quality rule recommendation run
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartExportLabelsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-StartExportLabelsTaskRun)  **
  - **Description:** Grants permission to start an Export Labels ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImportLabelsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-StartImportLabelsTaskRun)  **
  - **Description:** Grants permission to start an Import Labels ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJobRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html#aws-glue-api-jobs-runs-StartJobRun)  **
  - **Description:** Grants permission to start running a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartJobUpgradeAnalysis](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-upgrade-analysis.html#aws-glue-api-upgrade-analysis-StartJobUpgradeAnalysis)  **
  - **Description:** Grants permission to start running upgrade analysis for a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMLEvaluationTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-StartMLEvaluationTaskRun)  **
  - **Description:** Grants permission to start an Evaluation ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMLLabelingSetGenerationTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-StartMLLabelingSetGenerationTaskRun)  **
  - **Description:** Grants permission to start a Labeling Set Generation ML Task Run
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNotebook](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to start Glue Studio Notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [StartTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-StartTrigger)  **
  - **Description:** Grants permission to start a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartWorkflowRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-StartWorkflowRun)  **
  - **Description:** Grants permission to start running a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopColumnStatisticsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRun)  **
  - **Description:** Grants permission to stop execution for Column Statistics run
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopColumnStatisticsTaskRunSchedule](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRunSchedule)  **
  - **Description:** Grants permission to stop a column statistics task run schedule
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-StopCrawler)  **
  - **Description:** Grants permission to stop a running crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCrawlerSchedule](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-scheduler.html#aws-glue-api-crawler-scheduler-StopCrawlerSchedule)  **
  - **Description:** Grants permission to set the schedule state of a crawler to NOT\_SCHEDULED
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopJobUpgradeAnalysis](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-upgrade-analysis.html#aws-glue-api-upgrade-analysis-StopJobUpgradeAnalysis)  **
  - **Description:** Grants permission to stop an on-going upgrade analysis for a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSession](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html#aws-glue-interactive-sessions-StopSession)  **
  - **Description:** Grants permission to stop an interactive session
  - **Resource types (\*required):** [session\*](#list_glue-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-StopTrigger)  **
  - **Description:** Grants permission to stop a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopWorkflowRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-StopWorkflowRun)  **
  - **Description:** Grants permission to stop a workflow run
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-tags.html#aws-glue-api-tags-TagResource)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [blueprint](#list_glue-resource-blueprint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [connection](#list_glue-resource-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [crawler](#list_glue-resource-crawler) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [customEntityType](#list_glue-resource-customEntityType) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [dataQualityRuleset](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [devendpoint](#list_glue-resource-devendpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [integration](#list_glue-resource-integration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [integrationResourceProperty](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [job](#list_glue-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [mlTransform](#list_glue-resource-mlTransform) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [session](#list_glue-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [trigger](#list_glue-resource-trigger) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [usageProfile](#list_glue-resource-usageProfile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [workflow](#list_glue-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_glue-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Tagging, Write

- **   [TerminateNotebook](https://docs.aws.amazon.com/glue/latest/ug/notebook-getting-started.html#create-notebook-permissions-operations)  **
  - **Description:** Grants permission to terminate Glue Studio Notebooks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [TestConnection](https://docs.aws.amazon.com/glue/latest/dg/console-test-connections.html)  **
  - **Description:** Grants permission to test connection in Glue Studio
  - **Resource types (\*required):** [connection](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UntagResource](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-tags.html#aws-glue-api-tags-UntagResource)  **
  - **Description:** Grants permission to remove tags associated with a resource
  - **Resource types (\*required):** [blueprint](#list_glue-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [connection](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [crawler](#list_glue-resource-crawler) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [customEntityType](#list_glue-resource-customEntityType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [dataQualityRuleset](#list_glue-resource-dataQualityRuleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [devendpoint](#list_glue-resource-devendpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [integration](#list_glue-resource-integration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [integrationResourceProperty](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [job](#list_glue-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [mlTransform](#list_glue-resource-mlTransform) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [registry](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [schema](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [session](#list_glue-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [trigger](#list_glue-resource-trigger) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [usageProfile](#list_glue-resource-usageProfile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [workflow](#list_glue-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_glue-aws_TagKeys)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Tagging, Write

- **   [UpdateBlueprint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-UpdateBlueprint)  **
  - **Description:** Grants permission to update a blueprint
  - **Resource types (\*required):** [blueprint\*](#list_glue-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCatalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)  **
  - **Description:** Grants permission to update a catalog
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateClassifier](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html#aws-glue-api-crawler-classifiers-UpdateClassifier)  **
  - **Description:** Grants permission to update a classifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateColumnStatisticsForPartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-UpdateColumnStatisticsForPartition)  **
  - **Description:** Grants permission to update partition statistics of columns
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-UpdateColumnStatisticsForTable)  **
  - **Description:** Grants permission to update table statistics of columns
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateColumnStatisticsTaskSettings](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-UpdateColumnStatisticsTaskSettings)  **
  - **Description:** Grants permission to update settings for a column statistics task
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-UpdateConnection)  **
  - **Description:** Grants permission to update a connection
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [connectionType](#list_glue-resource-connectionType) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateCrawler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html#aws-glue-api-crawler-crawling-UpdateCrawler)  **
  - **Description:** Grants permission to update a crawler
  - **Resource types (\*required):** [crawler\*](#list_glue-resource-crawler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCrawlerSchedule](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-scheduler.html#aws-glue-api-crawler-scheduler-UpdateCrawlerSchedule)  **
  - **Description:** Grants permission to update the schedule of a crawler
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html#aws-glue-api-data-quality-api-UpdateDataQualityRuleset)  **
  - **Description:** Grants permission to update a Data Quality ruleset
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDatabase](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html#aws-glue-api-catalog-databases-UpdateDatabase)  **
  - **Description:** Grants permission to update a database
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateDevEndpoint](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html#aws-glue-api-dev-endpoint-UpdateDevEndpoint)  **
  - **Description:** Grants permission to update a development endpoint
  - **Resource types (\*required):** [devendpoint\*](#list_glue-resource-devendpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGlueIdentityCenterConfiguration](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-getting-started.html#security-trusted-identity-propagation-connecting)  **
  - **Description:** Grants permission to update the managed Idc application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIntegrationResourceProperty](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-UpdateIntegrationResourceProperty)  **
  - **Description:** Grants permission to update the integration resource property
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [integrationResourceProperty\*](#list_glue-resource-integrationResourceProperty) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegrationTableProperties](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-UpdateIntegrationTableProperties)  **
  - **Description:** Grants permission to update the integration table properties
  - **Resource types (\*required):** [catalog\*](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-UpdateJob)  **
  - **Description:** Grants permission to update a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:SecurityGroupIds](#list_glue-glue_SecurityGroupIds)<br />[glue:SubnetIds](#list_glue-glue_SubnetIds)<br />[glue:VpcIds](#list_glue-glue_VpcIds)
  - **Access level:** Write

- **   [UpdateJobFromSourceControl](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-UpdateJobFromSourceControl)  **
  - **Description:** Grants permission to update a job from source control provider
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMLTransform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html#aws-glue-api-machine-learning-api-UpdateMLTransform)  **
  - **Description:** Grants permission to update an ML Transform
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePartition](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html#aws-glue-api-catalog-partitions-UpdatePartition)  **
  - **Description:** Grants permission to update a partition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateRegistry](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-UpdateRegistry)  **
  - **Description:** Grants permission to update a schema registry
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSchema](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html#aws-glue-api-schema-registry-api-UpdateSchema)  **
  - **Description:** Grants permission to update a schema container
  - **Resource types (\*required):** [registry\*](#list_glue-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_glue-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSourceControlFromJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-UpdateSourceControlFromJob)  **
  - **Description:** Grants permission to update source control provider from a job
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTable](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-UpdateTable)  **
  - **Description:** Grants permission to update a table
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:FederatedAuthorizationSource](#list_glue-glue_FederatedAuthorizationSource)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateTableOptimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html#aws-glue-api-table-optimizers-UpdateTableOptimizer)  **
  - **Description:** Grants permission to update the configuration for an existing table optimizer
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:**  
  - **Resource types (\*required):** [table\*](#list_glue-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrigger](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-UpdateTrigger)  **
  - **Description:** Grants permission to update a trigger
  - **Resource types (\*required):** [trigger\*](#list_glue-resource-trigger)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUsageProfile](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html#aws-glue-api-usage-profiles-UpdateUsageProfile)  **
  - **Description:** Grants permission to update a usage profile
  - **Resource types (\*required):** [usageProfile\*](#list_glue-resource-usageProfile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserDefinedFunction](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html#aws-glue-api-catalog-functions-UpdateUserDefinedFunction)  **
  - **Description:** Grants permission to update a function definition
  - **Resource types (\*required):** [catalog](#list_glue-resource-catalog) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [database\*](#list_glue-resource-database) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [rootcatalog\*](#list_glue-resource-rootcatalog) / **Condition keys:** [glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Resource types (\*required):** [userdefinedfunction\*](#list_glue-resource-userdefinedfunction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)<br />[glue:LakeFormationPermissions](#list_glue-glue_LakeFormationPermissions)
  - **Access level:** Write

- **   [UpdateWorkflow](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html#aws-glue-api-workflow-UpdateWorkflow)  **
  - **Description:** Grants permission to update a workflow
  - **Resource types (\*required):** [workflow\*](#list_glue-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpgradeJob](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-upgrade-analysis.html#aws-glue-api-upgrade-analysis-UpgradeJob)  **
  - **Description:** Grants permission to upgrade a job to the latest version
  - **Resource types (\*required):** [job\*](#list_glue-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UseGlueStudio](https://docs.aws.amazon.com/glue/latest/ug/setting-up.html#getting-started-min-privs)  **
  - **Description:** Grants permission to use Glue Studio and access its internal APIs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Permission-only actions for AWS Glue
<a name="list_glue-permission-only-actions"></a>

The following actions are defined by AWS Glue but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessDataQualityRuntimeConfiguration](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html)  **
  - **Description:** Grants permission to retrieve runtime configuration for Data Quality features
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [AuthorizeInboundIntegration](aws-glue-api-integrations.html)  **
  - **Description:** Grants permission to Glue to continuously validate that the target Arn can receive data replicated from the source ARN
  - **Resource types (\*required):** [integration\*](#list_glue-resource-integration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInboundIntegration](aws-glue-api-integrations.html)  **
  - **Description:** Grants permission to the source principal to create an inbound integration for data to be replicated from the source into the target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PassConnection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html#aws-glue-api-catalog-connections-CreateConnection)  **
  - **Description:** Grants permission to pass glue connection name in input for APIs that require them
  - **Resource types (\*required):** [connection\*](#list_glue-resource-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishDataQuality](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html)  **
  - **Description:** Grants permission to publish Data Quality results
  - **Resource types (\*required):** [dataQualityRuleset\*](#list_glue-resource-dataQualityRuleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UseMLTransforms](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html)  **
  - **Description:** Grants permission to use an ML Transform from within a Glue ETL Script
  - **Resource types (\*required):** [mlTransform\*](#list_glue-resource-mlTransform)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Glue
<a name="list_glue-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [blueprint](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:blueprint/${BlueprintName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [catalog](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:catalog/${CatalogName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [completion](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:completion/${CompletionId} |   | 
|  [connection](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:connection/${ConnectionName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [connectionType](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:connectionType:${ConnectionTypeName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [crawler](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:crawler/${CrawlerName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [customEntityType](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:customEntityType/${CustomEntityTypeId} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [dataQualityRuleset](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:dataQualityRuleset/${RulesetName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [database](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:database/${DatabaseName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [devendpoint](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:devEndpoint/${DevEndpointName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [integration](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:integration:${IntegrationId} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [integrationResourceProperty](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:integrationresourceproperty/${ResourceType}/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [job](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:job/${JobName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [mlTransform](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:mlTransform/${TransformId} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [registry](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:registry/${RegistryName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [rootcatalog](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:catalog |   | 
|  [schema](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:schema/${SchemaName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:table/${DatabaseName}/${TableName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [tableversion](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:tableVersion/${DatabaseName}/${TableName}/${TableVersionName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [trigger](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:trigger/${TriggerName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [usageProfile](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:usageProfile/${UsageProfileId} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [userdefinedfunction](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:userDefinedFunction/${DatabaseName}/${UserDefinedFunctionName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 
|  [workflow](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html)  | arn:${Partition}:glue:${Region}:${Account}:workflow/${WorkflowName} | [aws:ResourceTag/${TagKey}](#list_glue-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Glue
<a name="list_glue-policy-keys"></a>

AWS Glue defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [glue:CredentialIssuingService](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the service from which the credentials of the request is issued | String | 
|   [glue:EnabledForRedshiftAutoDiscovery](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the presence of the key configured for role's identity-based policy | Bool | 
|   [glue:FederatedAuthorizationSource](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by whether the resource belongs to federated authorization | String | 
|   [glue:LakeFormationPermissions](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by whether Lake Formation permission checks will be performed for a given caller and the Glue resource | String | 
|   [glue:RoleAssumedBy](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the service from which the credentials of the request is obtained by assuming the customer role | String | 
|   [glue:SecurityGroupIds](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the ID of security groups configured for the Glue job | ArrayOfString | 
|   [glue:SubnetIds](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the ID of subnets configured for the Glue job | ArrayOfString | 
|   [glue:VpcIds](https://docs.aws.amazon.com/glue/latest/dg/using-identity-based-policies.html#glue-identity-based-policy-condition-keys)  | Filters access by the ID of the VPC configured for the Glue job | ArrayOfString | 