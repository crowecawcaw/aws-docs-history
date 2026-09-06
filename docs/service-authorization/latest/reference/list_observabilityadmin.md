

# Actions, resources, and condition keys for Amazon CloudWatch Observability Admin Service
<a name="list_observabilityadmin"></a>

Amazon CloudWatch Observability Admin Service (service prefix: `observabilityadmin`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/observabilityadmin/observabilityadmin.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudWatch Observability Admin Service](#list_observabilityadmin-operations)
+ [Actions defined by Amazon CloudWatch Observability Admin Service](#list_observabilityadmin-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Observability Admin Service](#list_observabilityadmin-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Observability Admin Service](#list_observabilityadmin-policy-keys)

## API operations defined by Amazon CloudWatch Observability Admin Service
<a name="list_observabilityadmin-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_observabilityadmin-actions-as-permissions).




- **   CreateCentralizationRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:CreateCentralizationRuleForOrganization](#list_observabilityadmin-action-CreateCentralizationRuleForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateS3TableIntegration  **
  - **IAM action:**  [observabilityadmin:CreateS3TableIntegration](#list_observabilityadmin-action-CreateS3TableIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com, test.logs.amazonaws.com / **Access level:** Write

- **   CreateTelemetryPipeline  **
  - **IAM action:**  [observabilityadmin:CreateTelemetryPipeline](#list_observabilityadmin-action-CreateTelemetryPipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cloudwatch:PutPipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com, telemetry-pipelines.observabilityadmin.amazonaws.com / **Access level:** Write

- **   CreateTelemetryRule  **
  - **IAM action:**  [observabilityadmin:CreateTelemetryRule](#list_observabilityadmin-action-CreateTelemetryRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTelemetryRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:CreateTelemetryRuleForOrganization](#list_observabilityadmin-action-CreateTelemetryRuleForOrganization)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCentralizationRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:DeleteCentralizationRuleForOrganization](#list_observabilityadmin-action-DeleteCentralizationRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteS3TableIntegration  **
  - **IAM action:**  [observabilityadmin:DeleteS3TableIntegration](#list_observabilityadmin-action-DeleteS3TableIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTelemetryPipeline  **
  - **IAM action:**  [observabilityadmin:DeleteTelemetryPipeline](#list_observabilityadmin-action-DeleteTelemetryPipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:DeletePipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteTelemetryRule  **
  - **IAM action:**  [observabilityadmin:DeleteTelemetryRule](#list_observabilityadmin-action-DeleteTelemetryRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTelemetryRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:DeleteTelemetryRuleForOrganization](#list_observabilityadmin-action-DeleteTelemetryRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCentralizationRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:GetCentralizationRuleForOrganization](#list_observabilityadmin-action-GetCentralizationRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetS3TableIntegration  **
  - **IAM action:**  [observabilityadmin:GetS3TableIntegration](#list_observabilityadmin-action-GetS3TableIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryEnrichmentStatus  **
  - **IAM action:**  [observabilityadmin:GetTelemetryEnrichmentStatus](#list_observabilityadmin-action-GetTelemetryEnrichmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryEvaluationStatus  **
  - **IAM action:**  [observabilityadmin:GetTelemetryEvaluationStatus](#list_observabilityadmin-action-GetTelemetryEvaluationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryEvaluationStatusForOrganization  **
  - **IAM action:**  [observabilityadmin:GetTelemetryEvaluationStatusForOrganization](#list_observabilityadmin-action-GetTelemetryEvaluationStatusForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryPipeline  **
  - **IAM action:**  [observabilityadmin:GetTelemetryPipeline](#list_observabilityadmin-action-GetTelemetryPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryRule  **
  - **IAM action:**  [observabilityadmin:GetTelemetryRule](#list_observabilityadmin-action-GetTelemetryRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:GetTelemetryRuleForOrganization](#list_observabilityadmin-action-GetTelemetryRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCentralizationRulesForOrganization  **
  - **IAM action:**  [observabilityadmin:ListCentralizationRulesForOrganization](#list_observabilityadmin-action-ListCentralizationRulesForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceTelemetry  **
  - **IAM action:**  [observabilityadmin:ListResourceTelemetry](#list_observabilityadmin-action-ListResourceTelemetry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListResourceTelemetryForOrganization  **
  - **IAM action:**  [observabilityadmin:ListResourceTelemetryForOrganization](#list_observabilityadmin-action-ListResourceTelemetryForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListS3TableIntegrations  **
  - **IAM action:**  [observabilityadmin:ListS3TableIntegrations](#list_observabilityadmin-action-ListS3TableIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [observabilityadmin:ListTagsForResource](#list_observabilityadmin-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTelemetryPipelines  **
  - **IAM action:**  [observabilityadmin:ListTelemetryPipelines](#list_observabilityadmin-action-ListTelemetryPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTelemetryRules  **
  - **IAM action:**  [observabilityadmin:ListTelemetryRules](#list_observabilityadmin-action-ListTelemetryRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTelemetryRulesForOrganization  **
  - **IAM action:**  [observabilityadmin:ListTelemetryRulesForOrganization](#list_observabilityadmin-action-ListTelemetryRulesForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartTelemetryEnrichment  **
  - **IAM action:**  [observabilityadmin:StartTelemetryEnrichment](#list_observabilityadmin-action-StartTelemetryEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTelemetryEvaluation  **
  - **IAM action:**  [observabilityadmin:StartTelemetryEvaluation](#list_observabilityadmin-action-StartTelemetryEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTelemetryEvaluationForOrganization  **
  - **IAM action:**  [observabilityadmin:StartTelemetryEvaluationForOrganization](#list_observabilityadmin-action-StartTelemetryEvaluationForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTelemetryEnrichment  **
  - **IAM action:**  [observabilityadmin:StopTelemetryEnrichment](#list_observabilityadmin-action-StopTelemetryEnrichment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTelemetryEvaluation  **
  - **IAM action:**  [observabilityadmin:StopTelemetryEvaluation](#list_observabilityadmin-action-StopTelemetryEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTelemetryEvaluationForOrganization  **
  - **IAM action:**  [observabilityadmin:StopTelemetryEvaluationForOrganization](#list_observabilityadmin-action-StopTelemetryEvaluationForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [observabilityadmin:TagResource](#list_observabilityadmin-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestTelemetryPipeline  **
  - **IAM action:**  [observabilityadmin:TestTelemetryPipeline](#list_observabilityadmin-action-TestTelemetryPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagResource  **
  - **IAM action:**  [observabilityadmin:UntagResource](#list_observabilityadmin-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCentralizationRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:UpdateCentralizationRuleForOrganization](#list_observabilityadmin-action-UpdateCentralizationRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTelemetryPipeline  **
  - **IAM action:**  [observabilityadmin:UpdateTelemetryPipeline](#list_observabilityadmin-action-UpdateTelemetryPipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cloudwatch:PutPipelineRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** logs.amazonaws.com, telemetry-pipelines.observabilityadmin.amazonaws.com / **Access level:** Write

- **   UpdateTelemetryRule  **
  - **IAM action:**  [observabilityadmin:UpdateTelemetryRule](#list_observabilityadmin-action-UpdateTelemetryRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTelemetryRuleForOrganization  **
  - **IAM action:**  [observabilityadmin:UpdateTelemetryRuleForOrganization](#list_observabilityadmin-action-UpdateTelemetryRuleForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateTelemetryPipelineConfiguration  **
  - **IAM action:**  [observabilityadmin:ValidateTelemetryPipelineConfiguration](#list_observabilityadmin-action-ValidateTelemetryPipelineConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon CloudWatch Observability Admin Service
<a name="list_observabilityadmin-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateCentralizationRuleForOrganization.html)  **
  - **Description:** Grants permission to create a new organization centralization rule with the specified name for the organization
  - **Resource types (\*required):** [organization-centralization-rule\*](#list_observabilityadmin-resource-organization-centralization-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)<br />[observabilityadmin:CentralizationBackupRegion](#list_observabilityadmin-observabilityadmin_CentralizationBackupRegion)<br />[observabilityadmin:CentralizationDestinationAccount](#list_observabilityadmin-observabilityadmin_CentralizationDestinationAccount)<br />[observabilityadmin:CentralizationDestinationRegion](#list_observabilityadmin-observabilityadmin_CentralizationDestinationRegion)<br />[observabilityadmin:CentralizationRuleName](#list_observabilityadmin-observabilityadmin_CentralizationRuleName)<br />[observabilityadmin:CentralizationSourceId](#list_observabilityadmin-observabilityadmin_CentralizationSourceId)<br />[observabilityadmin:CentralizationSourceRegions](#list_observabilityadmin-observabilityadmin_CentralizationSourceRegions)
  - **Access level:** Write

- **   [CreateS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateS3TableIntegration.html)  **
  - **Description:** Grants permission to create a new s3 table integration with the specified configuration
  - **Resource types (\*required):** [s3tableintegration\*](#list_observabilityadmin-resource-s3tableintegration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryPipeline.html)  **
  - **Description:** Grants permission to create a new telemetry pipeline with the specified name and configuration
  - **Resource types (\*required):** [telemetry-pipeline\*](#list_observabilityadmin-resource-telemetry-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)<br />[observabilityadmin:SourceType](#list_observabilityadmin-observabilityadmin_SourceType)
  - **Access level:** Write

- **   [CreateTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryRule.html)  **
  - **Description:** Grants permission to create a new telemetry rule with the specified name for the account
  - **Resource types (\*required):** [telemetry-rule\*](#list_observabilityadmin-resource-telemetry-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)<br />[observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [CreateTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryRuleForOrganization.html)  **
  - **Description:** Grants permission to create a new organization telemetry rule with the specified name for the organization
  - **Resource types (\*required):** [organization-telemetry-rule\*](#list_observabilityadmin-resource-organization-telemetry-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)<br />[observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [DeleteCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteCentralizationRuleForOrganization.html)  **
  - **Description:** Grants permission to delete an organization centralization rule with the specified name for the organization
  - **Resource types (\*required):** [organization-centralization-rule\*](#list_observabilityadmin-resource-organization-centralization-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[observabilityadmin:CentralizationRuleName](#list_observabilityadmin-observabilityadmin_CentralizationRuleName)
  - **Access level:** Write

- **   [DeleteS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteS3TableIntegration.html)  **
  - **Description:** Grants permission to delete the s3 table integration with the specified arn
  - **Resource types (\*required):** [s3tableintegration\*](#list_observabilityadmin-resource-s3tableintegration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryPipeline.html)  **
  - **Description:** Grants permission to delete the telemetry pipeline with the specified arn
  - **Resource types (\*required):** [telemetry-pipeline\*](#list_observabilityadmin-resource-telemetry-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryRule.html)  **
  - **Description:** Grants permission to delete a telemetry rule with the specified name for the account
  - **Resource types (\*required):** [telemetry-rule\*](#list_observabilityadmin-resource-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_DeleteTelemetryRuleForOrganization.html)  **
  - **Description:** Grants permission to delete an organization telemetry rule with the specified name for the organization
  - **Resource types (\*required):** [organization-telemetry-rule\*](#list_observabilityadmin-resource-organization-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetCentralizationRuleForOrganization.html)  **
  - **Description:** Grants permission to retrieve the specified organization centralization rule for the organization
  - **Resource types (\*required):** [organization-centralization-rule\*](#list_observabilityadmin-resource-organization-centralization-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[observabilityadmin:CentralizationRuleName](#list_observabilityadmin-observabilityadmin_CentralizationRuleName)
  - **Access level:** Read

- **   [GetS3TableIntegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetS3TableIntegration.html)  **
  - **Description:** Grants permission to retrieve the specified s3 table integration for the account
  - **Resource types (\*required):** [s3tableintegration\*](#list_observabilityadmin-resource-s3tableintegration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTelemetryEnrichmentStatus](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEnrichmentStatus.html)  **
  - **Description:** Grants permission to retrieve the status of the Resource tags for telemetry feature for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTelemetryEvaluationStatus](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatus.html)  **
  - **Description:** Grants permission to retrieve the Telemetry Config feature status for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTelemetryEvaluationStatusForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryEvaluationStatusForOrganization.html)  **
  - **Description:** Grants permission to retrieve the Telemetry Config feature status for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryPipeline.html)  **
  - **Description:** Grants permission to Get the telemetry pipeline with the specified name or arn
  - **Resource types (\*required):** [telemetry-pipeline\*](#list_observabilityadmin-resource-telemetry-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryRule.html)  **
  - **Description:** Grants permission to retrieve the specified telemetry rule for the account
  - **Resource types (\*required):** [telemetry-rule\*](#list_observabilityadmin-resource-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_GetTelemetryRuleForOrganization.html)  **
  - **Description:** Grants permission to retrieve the specified organization telemetry rule for the organization
  - **Resource types (\*required):** [organization-telemetry-rule\*](#list_observabilityadmin-resource-organization-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCentralizationRulesForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListCentralizationRulesForOrganization.html)  **
  - **Description:** Grants permission to list the centralization rules for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceTelemetry](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetry.html)  **
  - **Description:** Grants permission to retrieve telemetry configurations for resources associated with the account
  - **Resource types (\*required):** 
  - **Condition keys:** [observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Read

- **   [ListResourceTelemetryForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListResourceTelemetryForOrganization.html)  **
  - **Description:** Grants permission to retrieve telemetry configurations for resources associated with accounts in the organization
  - **Resource types (\*required):** 
  - **Condition keys:** [observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Read

- **   [ListS3TableIntegrations](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListS3TableIntegrations.html)  **
  - **Description:** Grants permission to list s3 table integrations for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** [organization-centralization-rule](#list_observabilityadmin-resource-organization-centralization-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [organization-telemetry-rule](#list_observabilityadmin-resource-organization-telemetry-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [s3tableintegration](#list_observabilityadmin-resource-s3tableintegration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [telemetry-pipeline](#list_observabilityadmin-resource-telemetry-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [telemetry-rule](#list_observabilityadmin-resource-telemetry-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTelemetryPipelines](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryPipelines.html)  **
  - **Description:** Grants permission to List telemetry pipelines for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTelemetryRules](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryRules.html)  **
  - **Description:** Grants permission to list the telemetry rules for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTelemetryRulesForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ListTelemetryRulesForOrganization.html)  **
  - **Description:** Grants permission to list the telemetry rules for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartTelemetryEnrichment](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEnrichment.html)  **
  - **Description:** Grants permission to enable the Resource tags for telemetry feature for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluation.html)  **
  - **Description:** Grants permission to start the Telemetry Config feature for the account
  - **Resource types (\*required):** 
  - **Condition keys:** [observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [StartTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StartTelemetryEvaluationForOrganization.html)  **
  - **Description:** Grants permission to start the Telemetry Config feature for the organization
  - **Resource types (\*required):** 
  - **Condition keys:** [observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [StopTelemetryEnrichment](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEnrichment.html)  **
  - **Description:** Grants permission to disable the Resource tags for telemetry feature for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopTelemetryEvaluation](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluation.html)  **
  - **Description:** Grants permission to stop the Telemetry Config feature for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopTelemetryEvaluationForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_StopTelemetryEvaluationForOrganization.html)  **
  - **Description:** Grants permission to stop the Telemetry Config feature for the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TagResource.html)  **
  - **Description:** Grants permission to add or update the specified tags for the specified resource
  - **Resource types (\*required):** [organization-centralization-rule](#list_observabilityadmin-resource-organization-centralization-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [organization-telemetry-rule](#list_observabilityadmin-resource-organization-telemetry-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [s3tableintegration](#list_observabilityadmin-resource-s3tableintegration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [telemetry-pipeline](#list_observabilityadmin-resource-telemetry-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [telemetry-rule](#list_observabilityadmin-resource-telemetry-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_observabilityadmin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TestTelemetryPipeline.html)  **
  - **Description:** Grants permission to Test a telemetry pipeline configuration with sample data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [organization-centralization-rule](#list_observabilityadmin-resource-organization-centralization-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [organization-telemetry-rule](#list_observabilityadmin-resource-organization-telemetry-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [s3tableintegration](#list_observabilityadmin-resource-s3tableintegration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [telemetry-pipeline](#list_observabilityadmin-resource-telemetry-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Resource types (\*required):** [telemetry-rule](#list_observabilityadmin-resource-telemetry-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_observabilityadmin-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCentralizationRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateCentralizationRuleForOrganization.html)  **
  - **Description:** Grants permission to update the specified centralization rule for the organization
  - **Resource types (\*required):** [organization-centralization-rule\*](#list_observabilityadmin-resource-organization-centralization-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[observabilityadmin:CentralizationBackupRegion](#list_observabilityadmin-observabilityadmin_CentralizationBackupRegion)<br />[observabilityadmin:CentralizationDestinationAccount](#list_observabilityadmin-observabilityadmin_CentralizationDestinationAccount)<br />[observabilityadmin:CentralizationDestinationRegion](#list_observabilityadmin-observabilityadmin_CentralizationDestinationRegion)<br />[observabilityadmin:CentralizationRuleName](#list_observabilityadmin-observabilityadmin_CentralizationRuleName)<br />[observabilityadmin:CentralizationSourceId](#list_observabilityadmin-observabilityadmin_CentralizationSourceId)<br />[observabilityadmin:CentralizationSourceRegions](#list_observabilityadmin-observabilityadmin_CentralizationSourceRegions)
  - **Access level:** Write

- **   [UpdateTelemetryPipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryPipeline.html)  **
  - **Description:** Grants permission to Update the telemetry pipeline with the specified arn
  - **Resource types (\*required):** [telemetry-pipeline\*](#list_observabilityadmin-resource-telemetry-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTelemetryRule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryRule.html)  **
  - **Description:** Grants permission to update the specified telemetry rule for the account
  - **Resource types (\*required):** [telemetry-rule\*](#list_observabilityadmin-resource-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [UpdateTelemetryRuleForOrganization](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_UpdateTelemetryRuleForOrganization.html)  **
  - **Description:** Grants permission to update the specified telemetry rule for the organization
  - **Resource types (\*required):** [organization-telemetry-rule\*](#list_observabilityadmin-resource-organization-telemetry-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_)<br />[observabilityadmin:TargetRegions](#list_observabilityadmin-observabilityadmin_TargetRegions)
  - **Access level:** Write

- **   [ValidateTelemetryPipelineConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ValidateTelemetryPipelineConfiguration.html)  **
  - **Description:** Grants permission to Validate a telemetry pipeline configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon CloudWatch Observability Admin Service
<a name="list_observabilityadmin-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [organization-centralization-rule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CentralizationRule.html)  | arn:${Partition}:observabilityadmin:${Region}:${Account}:organization-centralization-rule/${CentralizationRuleName} | [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_) | 
|  [organization-telemetry-rule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryRule.html)  | arn:${Partition}:observabilityadmin:${Region}:${Account}:organization-telemetry-rule/${TelemetryRuleName} | [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_) | 
|  [s3tableintegration](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_S3TableIntegration.html)  | arn:${Partition}:observabilityadmin:${Region}:${Account}:s3tableintegration/${S3TableIntegrationIdentifier} | [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_) | 
|  [telemetry-pipeline](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryPipeline.html)  | arn:${Partition}:observabilityadmin:${Region}:${Account}:telemetry-pipeline/${TelemetryPipelineIdentifier} | [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_) | 
|  [telemetry-rule](https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_TelemetryRule.html)  | arn:${Partition}:observabilityadmin:${Region}:${Account}:telemetry-rule/${TelemetryRuleName} | [aws:ResourceTag/${TagKey}](#list_observabilityadmin-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Observability Admin Service
<a name="list_observabilityadmin-policy-keys"></a>

Amazon CloudWatch Observability Admin Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [observabilityadmin:CentralizationBackupRegion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationbackupregion)  | Filters access by the backup region that is passed in the request | String | 
|   [observabilityadmin:CentralizationDestinationAccount](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationdestinationaccount)  | Filters access by the destination account that is passed in the request | String | 
|   [observabilityadmin:CentralizationDestinationRegion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationdestinationregion)  | Filters access by the destination region that is passed in the request | String | 
|   [observabilityadmin:CentralizationRuleName](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationrulename)  | Filters access by the name of the centralization rule that is passed in the request | String | 
|   [observabilityadmin:CentralizationSourceId](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationsourceid)  | Filters access by the source account, organizational unit, or organization IDs that is passed in the request | ArrayOfString | 
|   [observabilityadmin:CentralizationSourceRegions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-centralizationsourceregions)  | Filters access by the source regions that are passed in the request | ArrayOfString | 
|   [observabilityadmin:SourceType](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-sourcetype)  | Filters access by the source type that is passed in the request | String | 
|   [observabilityadmin:TargetRegions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/reference_policies_condition-keys.htmlcondition-keys-observabilityadmin.html#condition-keys-targetregions)  | Filters access by the regions that are targetted by the request | String | 