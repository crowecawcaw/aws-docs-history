

# Actions, resources, and condition keys for Amazon Bedrock
<a name="list_bedrock"></a>

Amazon Bedrock (service prefix: `bedrock`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/bedrock/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bedrock/bedrock.json) for this service.

**Topics**
+ [API operations defined by Amazon Bedrock](#list_bedrock-operations)
+ [Actions defined by Amazon Bedrock](#list_bedrock-actions-as-permissions)
+ [Permission-only actions for Amazon Bedrock](#list_bedrock-permission-only-actions)
+ [Resource types defined by Amazon Bedrock](#list_bedrock-resources-for-iam-policies)
+ [Condition keys for Amazon Bedrock](#list_bedrock-policy-keys)

## API operations defined by Amazon Bedrock
<a name="list_bedrock-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_bedrock-actions-as-permissions).




- **   BatchDeleteAdvancedPromptOptimizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:BatchDeleteAdvancedPromptOptimizationJob](#list_bedrock-action-BatchDeleteAdvancedPromptOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteEvaluationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:BatchDeleteEvaluationJob](#list_bedrock-action-BatchDeleteEvaluationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAutomatedReasoningPolicyBuildWorkflow  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CancelAutomatedReasoningPolicyBuildWorkflow](#list_bedrock-action-CancelAutomatedReasoningPolicyBuildWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAdvancedPromptOptimizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateAdvancedPromptOptimizationJob](#list_bedrock-action-CreateAdvancedPromptOptimizationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAutomatedReasoningPolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateAutomatedReasoningPolicy](#list_bedrock-action-CreateAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAutomatedReasoningPolicyTestCase  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateAutomatedReasoningPolicyTestCase](#list_bedrock-action-CreateAutomatedReasoningPolicyTestCase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAutomatedReasoningPolicyVersion  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateAutomatedReasoningPolicyVersion](#list_bedrock-action-CreateAutomatedReasoningPolicyVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateCustomModel](#list_bedrock-action-CreateCustomModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateCustomModelDeployment  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateCustomModelDeployment](#list_bedrock-action-CreateCustomModelDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEvaluationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateEvaluationJob](#list_bedrock-action-CreateEvaluationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateFoundationModelAgreement  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateFoundationModelAgreement](#list_bedrock-action-CreateFoundationModelAgreement)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateGuardrail  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateGuardrail](#list_bedrock-action-CreateGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGuardrailVersion  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateGuardrailVersion](#list_bedrock-action-CreateGuardrailVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateInferenceProfile  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateInferenceProfile](#list_bedrock-action-CreateInferenceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateMarketplaceModelEndpoint](#list_bedrock-action-CreateMarketplaceModelEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateModelCopyJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateModelCopyJob](#list_bedrock-action-CreateModelCopyJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateModelCustomizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateModelCustomizationJob](#list_bedrock-action-CreateModelCustomizationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateModelImportJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateModelImportJob](#list_bedrock-action-CreateModelImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateModelInvocationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateModelInvocationJob](#list_bedrock-action-CreateModelInvocationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreatePromptRouter  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreatePromptRouter](#list_bedrock-action-CreatePromptRouter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProvisionedModelThroughput  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CreateProvisionedModelThroughput](#list_bedrock-action-CreateProvisionedModelThroughput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAutomatedReasoningPolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteAutomatedReasoningPolicy](#list_bedrock-action-DeleteAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAutomatedReasoningPolicyBuildWorkflow  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteAutomatedReasoningPolicyBuildWorkflow](#list_bedrock-action-DeleteAutomatedReasoningPolicyBuildWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAutomatedReasoningPolicyTestCase  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteAutomatedReasoningPolicyTestCase](#list_bedrock-action-DeleteAutomatedReasoningPolicyTestCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteCustomModel](#list_bedrock-action-DeleteCustomModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteCustomModelDeployment  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteCustomModelDeployment](#list_bedrock-action-DeleteCustomModelDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteEnforcedGuardrailConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteEnforcedGuardrailConfiguration](#list_bedrock-action-DeleteEnforcedGuardrailConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFoundationModelAgreement  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteFoundationModelAgreement](#list_bedrock-action-DeleteFoundationModelAgreement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGuardrail  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteGuardrail](#list_bedrock-action-DeleteGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteImportedModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteImportedModel](#list_bedrock-action-DeleteImportedModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteInferenceProfile  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteInferenceProfile](#list_bedrock-action-DeleteInferenceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteMarketplaceModelEndpoint](#list_bedrock-action-DeleteMarketplaceModelEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteModelInvocationLoggingConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteModelInvocationLoggingConfiguration](#list_bedrock-action-DeleteModelInvocationLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePromptRouter  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeletePromptRouter](#list_bedrock-action-DeletePromptRouter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteProvisionedModelThroughput  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:DeleteProvisionedModelThroughput](#list_bedrock-action-DeleteProvisionedModelThroughput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeleteResourcePolicy](#list_bedrock-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:PutResourcePolicy](#list_bedrock-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeregisterMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:DeregisterMarketplaceModelEndpoint](#list_bedrock-action-DeregisterMarketplaceModelEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportAutomatedReasoningPolicyVersion  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ExportAutomatedReasoningPolicyVersion](#list_bedrock-action-ExportAutomatedReasoningPolicyVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAccountDataRetention  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetAccountDataRetention](#list_bedrock-action-GetAccountDataRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAdvancedPromptOptimizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAdvancedPromptOptimizationJob](#list_bedrock-action-GetAdvancedPromptOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicy](#list_bedrock-action-GetAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAutomatedReasoningPolicyAnnotations  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyAnnotations](#list_bedrock-action-GetAutomatedReasoningPolicyAnnotations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicyBuildWorkflow  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyBuildWorkflow](#list_bedrock-action-GetAutomatedReasoningPolicyBuildWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicyBuildWorkflowResultAssets  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyBuildWorkflowResultAssets](#list_bedrock-action-GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicyNextScenario  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyNextScenario](#list_bedrock-action-GetAutomatedReasoningPolicyNextScenario) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicyTestCase  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyTestCase](#list_bedrock-action-GetAutomatedReasoningPolicyTestCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedReasoningPolicyTestResult  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetAutomatedReasoningPolicyTestResult](#list_bedrock-action-GetAutomatedReasoningPolicyTestResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetCustomModel](#list_bedrock-action-GetCustomModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetCustomModelDeployment  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetCustomModelDeployment](#list_bedrock-action-GetCustomModelDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetEvaluationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetEvaluationJob](#list_bedrock-action-GetEvaluationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFoundationModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetFoundationModel](#list_bedrock-action-GetFoundationModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetFoundationModelAvailability  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetFoundationModelAvailability](#list_bedrock-action-GetFoundationModelAvailability)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetGuardrail  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetGuardrail](#list_bedrock-action-GetGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetImportedModel  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetImportedModel](#list_bedrock-action-GetImportedModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetInferenceProfile  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetInferenceProfile](#list_bedrock-action-GetInferenceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetMarketplaceModelEndpoint](#list_bedrock-action-GetMarketplaceModelEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetModelCopyJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetModelCopyJob](#list_bedrock-action-GetModelCopyJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetModelCustomizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetModelCustomizationJob](#list_bedrock-action-GetModelCustomizationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetModelImportJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetModelImportJob](#list_bedrock-action-GetModelImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetModelInvocationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetModelInvocationJob](#list_bedrock-action-GetModelInvocationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetModelInvocationLoggingConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetModelInvocationLoggingConfiguration](#list_bedrock-action-GetModelInvocationLoggingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetPromptRouter  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetPromptRouter](#list_bedrock-action-GetPromptRouter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetProvisionedModelThroughput  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetProvisionedModelThroughput](#list_bedrock-action-GetProvisionedModelThroughput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:GetResourcePolicy](#list_bedrock-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUseCaseForModelAccess  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetUseCaseForModelAccess](#list_bedrock-action-GetUseCaseForModelAccess)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAdvancedPromptOptimizationJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListAdvancedPromptOptimizationJobs](#list_bedrock-action-ListAdvancedPromptOptimizationJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListAutomatedReasoningPolicies  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListAutomatedReasoningPolicies](#list_bedrock-action-ListAutomatedReasoningPolicies)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListAutomatedReasoningPolicyBuildWorkflows  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListAutomatedReasoningPolicyBuildWorkflows](#list_bedrock-action-ListAutomatedReasoningPolicyBuildWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomatedReasoningPolicyTestCases  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListAutomatedReasoningPolicyTestCases](#list_bedrock-action-ListAutomatedReasoningPolicyTestCases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomatedReasoningPolicyTestResults  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListAutomatedReasoningPolicyTestResults](#list_bedrock-action-ListAutomatedReasoningPolicyTestResults)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListCustomModelDeployments  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListCustomModelDeployments](#list_bedrock-action-ListCustomModelDeployments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListCustomModels  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListCustomModels](#list_bedrock-action-ListCustomModels)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListEnforcedGuardrailsConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListEnforcedGuardrailsConfiguration](#list_bedrock-action-ListEnforcedGuardrailsConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEvaluationJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListEvaluationJobs](#list_bedrock-action-ListEvaluationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFoundationModelAgreementOffers  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListFoundationModelAgreementOffers](#list_bedrock-action-ListFoundationModelAgreementOffers)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListFoundationModels  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListFoundationModels](#list_bedrock-action-ListFoundationModels)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListGuardrails  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListGuardrails](#list_bedrock-action-ListGuardrails)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListImportedModels  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListImportedModels](#list_bedrock-action-ListImportedModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceProfiles  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListInferenceProfiles](#list_bedrock-action-ListInferenceProfiles)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListMarketplaceModelEndpoints  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListMarketplaceModelEndpoints](#list_bedrock-action-ListMarketplaceModelEndpoints)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListModelCopyJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListModelCopyJobs](#list_bedrock-action-ListModelCopyJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListModelCustomizationJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListModelCustomizationJobs](#list_bedrock-action-ListModelCustomizationJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListModelImportJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:ListModelImportJobs](#list_bedrock-action-ListModelImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelInvocationJobs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListModelInvocationJobs](#list_bedrock-action-ListModelInvocationJobs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListPromptRouters  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListPromptRouters](#list_bedrock-action-ListPromptRouters)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListProvisionedModelThroughputs  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListProvisionedModelThroughputs](#list_bedrock-action-ListProvisionedModelThroughputs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListTagsForResource](#list_bedrock-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   PutAccountDataRetention  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:PutAccountDataRetention](#list_bedrock-action-PutAccountDataRetention)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutEnforcedGuardrailConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:PutEnforcedGuardrailConfiguration](#list_bedrock-action-PutEnforcedGuardrailConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutModelInvocationLoggingConfiguration  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:PutModelInvocationLoggingConfiguration](#list_bedrock-action-PutModelInvocationLoggingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:PutResourcePolicy](#list_bedrock-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutUseCaseForModelAccess  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:PutUseCaseForModelAccess](#list_bedrock-action-PutUseCaseForModelAccess)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RegisterMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:RegisterMarketplaceModelEndpoint](#list_bedrock-action-RegisterMarketplaceModelEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutomatedReasoningPolicyBuildWorkflow  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:StartAutomatedReasoningPolicyBuildWorkflow](#list_bedrock-action-StartAutomatedReasoningPolicyBuildWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutomatedReasoningPolicyTestWorkflow  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeAutomatedReasoningPolicy](#list_bedrock-action-InvokeAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:StartAutomatedReasoningPolicyTestWorkflow](#list_bedrock-action-StartAutomatedReasoningPolicyTestWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StopAdvancedPromptOptimizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:StopAdvancedPromptOptimizationJob](#list_bedrock-action-StopAdvancedPromptOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopEvaluationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:StopEvaluationJob](#list_bedrock-action-StopEvaluationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopModelCustomizationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:StopModelCustomizationJob](#list_bedrock-action-StopModelCustomizationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StopModelInvocationJob  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:StopModelInvocationJob](#list_bedrock-action-StopModelInvocationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UntagResource](#list_bedrock-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateAutomatedReasoningPolicy  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UpdateAutomatedReasoningPolicy](#list_bedrock-action-UpdateAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateAutomatedReasoningPolicyAnnotations  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:UpdateAutomatedReasoningPolicyAnnotations](#list_bedrock-action-UpdateAutomatedReasoningPolicyAnnotations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutomatedReasoningPolicyTestCase  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:UpdateAutomatedReasoningPolicyTestCase](#list_bedrock-action-UpdateAutomatedReasoningPolicyTestCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomModelDeployment  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UpdateCustomModelDeployment](#list_bedrock-action-UpdateCustomModelDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateGuardrail  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UpdateGuardrail](#list_bedrock-action-UpdateGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateMarketplaceModelEndpoint  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UpdateMarketplaceModelEndpoint](#list_bedrock-action-UpdateMarketplaceModelEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   UpdateProvisionedModelThroughput  **
  - **SDK client:** bedrock
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UpdateProvisionedModelThroughput](#list_bedrock-action-UpdateProvisionedModelThroughput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AssociateAgentCollaborator  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateAgentCollaborator](#list_bedrock-action-AssociateAgentCollaborator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateAgentKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateAgentKnowledgeBase](#list_bedrock-action-AssociateAgentKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgent  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateAgent](#list_bedrock-action-CreateAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateAgentActionGroup  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateAgentActionGroup](#list_bedrock-action-CreateAgentActionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateAgentAlias](#list_bedrock-action-CreateAgentAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataSource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateDataSource](#list_bedrock-action-CreateDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateFlow  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateFlow](#list_bedrock-action-CreateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreateFlowAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateFlowAlias](#list_bedrock-action-CreateFlowAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFlowVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreateFlowVersion](#list_bedrock-action-CreateFlowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateThirdPartyKnowledgeBase](#list_bedrock-action-AssociateThirdPartyKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:CreateKnowledgeBase](#list_bedrock-action-CreateKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   CreatePrompt  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreatePrompt](#list_bedrock-action-CreatePrompt)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePromptVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CreatePromptVersion](#list_bedrock-action-CreatePromptVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAgent  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteAgent](#list_bedrock-action-DeleteAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentActionGroup  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteAgentActionGroup](#list_bedrock-action-DeleteAgentActionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteAgentAlias](#list_bedrock-action-DeleteAgentAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAgentVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteAgentVersion](#list_bedrock-action-DeleteAgentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteDataSource](#list_bedrock-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlow  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteFlow](#list_bedrock-action-DeleteFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlowAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteFlowAlias](#list_bedrock-action-DeleteFlowAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlowVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteFlowVersion](#list_bedrock-action-DeleteFlowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteKnowledgeBase](#list_bedrock-action-DeleteKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteKnowledgeBaseDocuments  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateThirdPartyKnowledgeBase](#list_bedrock-action-AssociateThirdPartyKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:DeleteKnowledgeBaseDocuments](#list_bedrock-action-DeleteKnowledgeBaseDocuments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:StartIngestionJob](#list_bedrock-action-StartIngestionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeletePrompt  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeletePrompt](#list_bedrock-action-DeletePrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DeleteResourcePolicy](#list_bedrock-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:PutResourcePolicy](#list_bedrock-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DisassociateAgentCollaborator  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DisassociateAgentCollaborator](#list_bedrock-action-DisassociateAgentCollaborator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAgentKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:DisassociateAgentKnowledgeBase](#list_bedrock-action-DisassociateAgentKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAgent  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgent](#list_bedrock-action-GetAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentActionGroup  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgentActionGroup](#list_bedrock-action-GetAgentActionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgentAlias](#list_bedrock-action-GetAgentAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentCollaborator  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgentCollaborator](#list_bedrock-action-GetAgentCollaborator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgentKnowledgeBase](#list_bedrock-action-GetAgentKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetAgentVersion](#list_bedrock-action-GetAgentVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetDataSource](#list_bedrock-action-GetDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFlow  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetFlow](#list_bedrock-action-GetFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFlowAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetFlowAlias](#list_bedrock-action-GetFlowAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFlowVersion  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetFlowVersion](#list_bedrock-action-GetFlowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngestionJob  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetIngestionJob](#list_bedrock-action-GetIngestionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetKnowledgeBase](#list_bedrock-action-GetKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetKnowledgeBaseDocuments  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetKnowledgeBaseDocuments](#list_bedrock-action-GetKnowledgeBaseDocuments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrompt  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetPrompt](#list_bedrock-action-GetPrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:GetResourcePolicy](#list_bedrock-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   IngestKnowledgeBaseDocuments  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateThirdPartyKnowledgeBase](#list_bedrock-action-AssociateThirdPartyKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:IngestKnowledgeBaseDocuments](#list_bedrock-action-IngestKnowledgeBaseDocuments)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:StartIngestionJob](#list_bedrock-action-StartIngestionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListAgentActionGroups  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgentActionGroups](#list_bedrock-action-ListAgentActionGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentAliases  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgentAliases](#list_bedrock-action-ListAgentAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentCollaborators  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgentCollaborators](#list_bedrock-action-ListAgentCollaborators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentKnowledgeBases  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgentKnowledgeBases](#list_bedrock-action-ListAgentKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentVersions  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgentVersions](#list_bedrock-action-ListAgentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgents  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListAgents](#list_bedrock-action-ListAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListDataSources](#list_bedrock-action-ListDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlowAliases  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListFlowAliases](#list_bedrock-action-ListFlowAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlowVersions  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListFlowVersions](#list_bedrock-action-ListFlowVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlows  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListFlows](#list_bedrock-action-ListFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIngestionJobs  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListIngestionJobs](#list_bedrock-action-ListIngestionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKnowledgeBaseDocuments  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListKnowledgeBaseDocuments](#list_bedrock-action-ListKnowledgeBaseDocuments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKnowledgeBases  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListKnowledgeBases](#list_bedrock-action-ListKnowledgeBases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrompts  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ListPrompts](#list_bedrock-action-ListPrompts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListTagsForResource](#list_bedrock-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   PrepareAgent  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:PrepareAgent](#list_bedrock-action-PrepareAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PrepareFlow  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:PrepareFlow](#list_bedrock-action-PrepareFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:PutResourcePolicy](#list_bedrock-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartIngestionJob  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateThirdPartyKnowledgeBase](#list_bedrock-action-AssociateThirdPartyKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:StartIngestionJob](#list_bedrock-action-StartIngestionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StopIngestionJob  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:StopIngestionJob](#list_bedrock-action-StopIngestionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UntagResource](#list_bedrock-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateAgent  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateAgent](#list_bedrock-action-UpdateAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   UpdateAgentActionGroup  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateAgentActionGroup](#list_bedrock-action-UpdateAgentActionGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateAgentAlias](#list_bedrock-action-UpdateAgentAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentCollaborator  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateAgentCollaborator](#list_bedrock-action-UpdateAgentCollaborator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAgentKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateAgentKnowledgeBase](#list_bedrock-action-UpdateAgentKnowledgeBase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateDataSource](#list_bedrock-action-UpdateDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFlow  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateFlow](#list_bedrock-action-UpdateFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   UpdateFlowAlias  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdateFlowAlias](#list_bedrock-action-UpdateFlowAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateKnowledgeBase  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:AssociateThirdPartyKnowledgeBase](#list_bedrock-action-AssociateThirdPartyKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:UpdateKnowledgeBase](#list_bedrock-action-UpdateKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock.amazonaws.com / **Access level:** Write

- **   UpdatePrompt  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:UpdatePrompt](#list_bedrock-action-UpdatePrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateFlowDefinition  **
  - **SDK client:** bedrock-agent
  - **IAM action:**  [bedrock:ValidateFlowDefinition](#list_bedrock-action-ValidateFlowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AgenticRetrieveStream  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:AgenticRetrieveStream](#list_bedrock-action-AgenticRetrieveStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:Retrieve](#list_bedrock-action-Retrieve)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CheckIngestedDocumentAcl  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CheckIngestedDocumentAcl](#list_bedrock-action-CheckIngestedDocumentAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateInvocation  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CreateInvocation](#list_bedrock-action-CreateInvocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSession  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CreateSession](#list_bedrock-action-CreateSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAgentMemory  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:DeleteAgentMemory](#list_bedrock-action-DeleteAgentMemory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSession  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:DeleteSession](#list_bedrock-action-DeleteSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EndSession  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:EndSession](#list_bedrock-action-EndSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateQuery  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GenerateQuery](#list_bedrock-action-GenerateQuery)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetKnowledgeBase](#list_bedrock-action-GetKnowledgeBase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAgentMemory  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetAgentMemory](#list_bedrock-action-GetAgentMemory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentContent  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetDocumentContent](#list_bedrock-action-GetDocumentContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:Retrieve](#list_bedrock-action-Retrieve)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetExecutionFlowSnapshot  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetExecutionFlowSnapshot](#list_bedrock-action-GetExecutionFlowSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFlowExecution  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetFlowExecution](#list_bedrock-action-GetFlowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIngestedDocumentAcl  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetIngestedDocumentAcl](#list_bedrock-action-GetIngestedDocumentAcl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvocationStep  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetInvocationStep](#list_bedrock-action-GetInvocationStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSession  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:GetSession](#list_bedrock-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeAgent  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:InvokeAgent](#list_bedrock-action-InvokeAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeFlow  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:InvokeFlow](#list_bedrock-action-InvokeFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeInlineAgent  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:InvokeInlineAgent](#list_bedrock-action-InvokeInlineAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFlowExecutionEvents  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:ListFlowExecutionEvents](#list_bedrock-action-ListFlowExecutionEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlowExecutions  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:ListFlowExecutions](#list_bedrock-action-ListFlowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvocationSteps  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:ListInvocations](#list_bedrock-action-ListInvocations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [bedrock:ListInvocationSteps](#list_bedrock-action-ListInvocationSteps)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListInvocations  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:ListInvocations](#list_bedrock-action-ListInvocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:ListSessions](#list_bedrock-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListTagsForResource](#list_bedrock-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   OptimizePrompt  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:OptimizePrompt](#list_bedrock-action-OptimizePrompt) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutInvocationStep  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:PutInvocationStep](#list_bedrock-action-PutInvocationStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Rerank  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:Rerank](#list_bedrock-action-Rerank) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Retrieve  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:Retrieve](#list_bedrock-action-Retrieve) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RetrieveAndGenerate  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:RetrieveAndGenerate](#list_bedrock-action-RetrieveAndGenerate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetrieveAndGenerateStream  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:RetrieveAndGenerate](#list_bedrock-action-RetrieveAndGenerate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartFlowExecution  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:StartFlowExecution](#list_bedrock-action-StartFlowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopFlowExecution  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:StopFlowExecution](#list_bedrock-action-StopFlowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UntagResource](#list_bedrock-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateSession  **
  - **SDK client:** bedrock-agent-runtime
  - **IAM action:**  [bedrock:UpdateSession](#list_bedrock-action-UpdateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CopyBlueprintStage  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CopyBlueprintStage](#list_bedrock-action-CopyBlueprintStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBlueprint  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CreateBlueprint](#list_bedrock-action-CreateBlueprint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBlueprintVersion  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CreateBlueprintVersion](#list_bedrock-action-CreateBlueprintVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataAutomationLibrary  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CreateDataAutomationLibrary](#list_bedrock-action-CreateDataAutomationLibrary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataAutomationProject  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CreateDataAutomationProject](#list_bedrock-action-CreateDataAutomationProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBlueprint  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:DeleteBlueprint](#list_bedrock-action-DeleteBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataAutomationLibrary  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:DeleteDataAutomationLibrary](#list_bedrock-action-DeleteDataAutomationLibrary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataAutomationProject  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:DeleteDataAutomationProject](#list_bedrock-action-DeleteDataAutomationProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBlueprint  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetBlueprint](#list_bedrock-action-GetBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBlueprintOptimizationStatus  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetBlueprintOptimizationStatus](#list_bedrock-action-GetBlueprintOptimizationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAutomationLibrary  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetDataAutomationLibrary](#list_bedrock-action-GetDataAutomationLibrary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAutomationLibraryEntity  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetDataAutomationLibraryEntity](#list_bedrock-action-GetDataAutomationLibraryEntity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAutomationLibraryIngestionJob  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetDataAutomationLibraryIngestionJob](#list_bedrock-action-GetDataAutomationLibraryIngestionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataAutomationProject  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:GetDataAutomationProject](#list_bedrock-action-GetDataAutomationProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeBlueprintOptimizationAsync  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:InvokeBlueprintOptimizationAsync](#list_bedrock-action-InvokeBlueprintOptimizationAsync)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   InvokeDataAutomationLibraryIngestionJob  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:InvokeDataAutomationLibraryIngestionJob](#list_bedrock-action-InvokeDataAutomationLibraryIngestionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListBlueprints  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:ListBlueprints](#list_bedrock-action-ListBlueprints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataAutomationLibraries  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:ListDataAutomationLibraries](#list_bedrock-action-ListDataAutomationLibraries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataAutomationLibraryEntities  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:ListDataAutomationLibraryEntities](#list_bedrock-action-ListDataAutomationLibraryEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataAutomationLibraryIngestionJobs  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:ListDataAutomationLibraryIngestionJobs](#list_bedrock-action-ListDataAutomationLibraryIngestionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataAutomationProjects  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:ListDataAutomationProjects](#list_bedrock-action-ListDataAutomationProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListTagsForResource](#list_bedrock-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   TagResource  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UntagResource](#list_bedrock-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateBlueprint  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:UpdateBlueprint](#list_bedrock-action-UpdateBlueprint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataAutomationLibrary  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:UpdateDataAutomationLibrary](#list_bedrock-action-UpdateDataAutomationLibrary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataAutomationProject  **
  - **SDK client:** bedrock-data-automation
  - **IAM action:**  [bedrock:UpdateDataAutomationProject](#list_bedrock-action-UpdateDataAutomationProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDataAutomationStatus  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:GetDataAutomationStatus](#list_bedrock-action-GetDataAutomationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeDataAutomation  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:InvokeDataAutomation](#list_bedrock-action-InvokeDataAutomation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeDataAutomationAsync  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:InvokeDataAutomationAsync](#list_bedrock-action-InvokeDataAutomationAsync)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListTagsForResource  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListTagsForResource](#list_bedrock-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   TagResource  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock-data-automation-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:UntagResource](#list_bedrock-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ApplyGuardrail  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:ApplyGuardrail](#list_bedrock-action-ApplyGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeAutomatedReasoningPolicy](#list_bedrock-action-InvokeAutomatedReasoningPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   Converse  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:ApplyGuardrail](#list_bedrock-action-ApplyGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModel](#list_bedrock-action-InvokeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeTool](#list_bedrock-action-InvokeTool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ConverseStream  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:ApplyGuardrail](#list_bedrock-action-ApplyGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModelWithResponseStream](#list_bedrock-action-InvokeModelWithResponseStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeTool](#list_bedrock-action-InvokeTool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CountTokens  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CountTokens](#list_bedrock-action-CountTokens)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetAsyncInvoke  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:GetAsyncInvoke](#list_bedrock-action-GetAsyncInvoke)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   InvokeGuardrailChecks  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeGuardrailChecks](#list_bedrock-action-InvokeGuardrailChecks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   InvokeModel  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:ApplyGuardrail](#list_bedrock-action-ApplyGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModel](#list_bedrock-action-InvokeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeTool](#list_bedrock-action-InvokeTool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   InvokeModelWithBidirectionalStream  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:InvokeModel](#list_bedrock-action-InvokeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeModelWithResponseStream  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:ApplyGuardrail](#list_bedrock-action-ApplyGuardrail)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModel](#list_bedrock-action-InvokeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModelWithResponseStream](#list_bedrock-action-InvokeModelWithResponseStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeTool](#list_bedrock-action-InvokeTool)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListAsyncInvokes  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:ListAsyncInvokes](#list_bedrock-action-ListAsyncInvokes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   StartAsyncInvoke  **
  - **SDK client:** bedrock-runtime
  - **IAM action:**  [bedrock:CallWithBearerToken](#list_bedrock-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:InvokeModel](#list_bedrock-action-InvokeModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock:TagResource](#list_bedrock-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write



## Actions defined by Amazon Bedrock
<a name="list_bedrock-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AgenticRetrieveStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to perform agentic retrieve with streaming from retrievers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ApplyGuardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to apply a guardrail
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:**  
  - **Access level:** Read

- **   [AssociateAgentCollaborator](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_AssociateAgentCollaborator.html)  **
  - **Description:** Grants permission to associate another existing agent as a collaborator to an existing agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociateAgentKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_AssociateAgentKnowledgeBase.html)  **
  - **Description:** Grants permission to associate a knowledge base with an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteAdvancedPromptOptimizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_BatchDeleteAdvancedPromptOptimizationJob.html)  **
  - **Description:** Grants permission to delete one or more advanced prompt optimization jobs
  - **Resource types (\*required):** [advanced-prompt-optimization-job\*](#list_bedrock-resource-advanced-prompt-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_BatchDeleteEvaluationJob.html)  **
  - **Description:** Grants permission to batch delete list of bedrock evaluation jobs
  - **Resource types (\*required):** [evaluation-job\*](#list_bedrock-resource-evaluation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CallWithBearerToken](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to use bearer token
  - **Resource types (\*required):** 
  - **Condition keys:** [bedrock:BearerTokenType](#list_bedrock-bedrock_BearerTokenType)
  - **Access level:** Read

- **   [CancelAutomatedReasoningPolicyBuildWorkflow](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to cancel a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelInvoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to cancel an in-progress stateful invocation
  - **Resource types (\*required):** [project\*](#list_bedrock-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckIngestedDocumentAcl](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CheckIngestedDocumentAcl.html)  **
  - **Description:** Grants permission to check whether a user has access to a specific document based on access control list ingested in a knowledge base
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CopyBlueprintStage](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Data_Automation_for_Amazon_Bedrock.html)  **
  - **Description:** Grants permission to copy a blueprint from one stage to another
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CountTokens](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_CountTokens.html)  **
  - **Description:** Grants permission to count the number of tokens in an input prompt
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model)
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateAdvancedPromptOptimizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateAdvancedPromptOptimizationJob.html)  **
  - **Description:** Grants permission to create an advanced prompt optimization job
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgent.html)  **
  - **Description:** Grants permission to create a new agent and a test agent alias pointing to the DRAFT agent version
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAgentActionGroup](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentActionGroup.html)  **
  - **Description:** Grants permission to create a new action group in an existing agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateAgentAlias.html)  **
  - **Description:** Grants permission to create a new alias for an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAutomatedReasoningPolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create a new automated reasoning policy
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAutomatedReasoningPolicyTestCase](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create a test case for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAutomatedReasoningPolicyVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create a new automated reasoning policy version
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBlueprint](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_CreateBlueprint.html)  **
  - **Description:** Grants permission to create a blueprint for custom output from data automation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBlueprintVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_CreateBlueprintVersion.html)  **
  - **Description:** Grants permission to create a new version for an existing blueprint
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html)  **
  - **Description:** Grants permission to create a custom model into Bedrock
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html)  **
  - **Description:** Grants permission to create a custom model deployment for custom model
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataAutomationLibrary](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_CreateDataAutomationLibrary.html)  **
  - **Description:** Grants permission to create a Data Automation Library
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataAutomationProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_CreateDataAutomationProject.html)  **
  - **Description:** Grants permission to create a data automation project
  - **Resource types (\*required):** [blueprint](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-library](#list_bedrock-resource-data-automation-library) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html)  **
  - **Description:** Grants permission to create a data source
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataSourceToken](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-3lo-setup.html)  **
  - **Description:** Grants permission to create an authorization token for MANAGED\_OAUTH2 data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateEvaluationJob.html)  **
  - **Description:** Grants permission to create a job for evaluation foundation models or custom models
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [default-prompt-router\*](#list_bedrock-resource-default-prompt-router) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlow.html)  **
  - **Description:** Grants permission to create a prompt flow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFlowAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlowAlias.html)  **
  - **Description:** Grants permission to create an alias of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFlowVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateFlowVersion.html)  **
  - **Description:** Grants permission to create an immutable version of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFoundationModelAgreement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to create a new foundation model agreement
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGuardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create a new guardrail
  - **Resource types (\*required):** [automated-reasoning-policy](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [automated-reasoning-policy-version](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGuardrailVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create a new guardrail version
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateInferenceProfile.html)  **
  - **Description:** Grants permission to create inference profiles
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInvocation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CreateInvocation.html)  **
  - **Description:** Grants permission to create a new invocation in an existing session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateKnowledgeBase.html)  **
  - **Description:** Grants permission to create a knowledge base
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMarketplaceModelEndpoint](API_CreateMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to create a marketplace model endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateModelCopyJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelCopyJob.html)  **
  - **Description:** Grants permission to create a job for copying a custom model across region or across account
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelCustomizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelCustomizationJob.html)  **
  - **Description:** Grants permission to create a job for customizing the model with your custom training data
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelEvaluationJob.html)  **
  - **Description:** Grants permission to create a job for evaluation foundation models or custom models
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelImportJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html)  **
  - **Description:** Grants permission to create a job for importing model into Bedrock
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelInvocationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelInvocationJob.html)  **
  - **Description:** Grants permission to create a new model invocation job
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-invocation-job\*](#list_bedrock-resource-model-invocation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreatePrompt.html)  **
  - **Description:** Grants permission to create a prompt
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePromptRouter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreatePromptRouter.html)  **
  - **Description:** Grants permission to create a custom prompt router
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePromptVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreatePromptVersion.html)  **
  - **Description:** Grants permission to create a version of a prompt
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateProvisionedModelThroughput.html)  **
  - **Description:** Grants permission to create a new provisioned model throughput
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_CreateSession.html)  **
  - **Description:** Grants permission to create a new session
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteAgent.html)  **
  - **Description:** Grants permission to delete an Agent that you created earlier
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentActionGroup](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteAgentActionGroup.html)  **
  - **Description:** Grants permission to delete an actionGroup that you created earlier
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteAgentAlias.html)  **
  - **Description:** Grants permission to delete an AgentAlias that you created earlier
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentMemory](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteAgentMemory.html)  **
  - **Description:** Grants permission to delete existing memory for an alias
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteAgentVersion.html)  **
  - **Description:** Grants permission to delete an Agent Version that you created earlier
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAutomatedReasoningPolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to delete an automated reasoning policy or its version
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version\*](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAutomatedReasoningPolicyBuildWorkflow](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to delete a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAutomatedReasoningPolicyTestCase](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to delete a test case for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBlueprint](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DeleteBlueprint.html)  **
  - **Description:** Grants permission to delete a blueprint for data automation
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html)  **
  - **Description:** Grants permission to delete a custom model that you created earlier
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html)  **
  - **Description:** Grants permission to delete a custom model deployment that you created earlier
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataAutomationLibrary](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DeleteDataAutomationLibrary.html)  **
  - **Description:** Grants permission to delete a Data Automation Library
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataAutomationProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_DeleteDataAutomationProject.html)  **
  - **Description:** Grants permission to delete a data automation project
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete a data source
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnforcedGuardrailConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteEnforcedGuardrailConfiguration.html)  **
  - **Description:** Grants permission to delete account-level enforced guardrail configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteFlow.html)  **
  - **Description:** Grants permission to delete a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFlowAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteFlowAlias.html)  **
  - **Description:** Grants permission to delete an alias of a prompt flow
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFlowVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteFlowVersion.html)  **
  - **Description:** Grants permission to delete a version of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFoundationModelAgreement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to delete a foundation model agreement that you created earlier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteGuardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to delete a guardrail or its version
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImportedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteImportedModel.html)  **
  - **Description:** Grants permission to delete previously created Bedrock imported model
  - **Resource types (\*required):** [imported-model\*](#list_bedrock-resource-imported-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteInferenceProfile.html)  **
  - **Description:** Grants permission to delete inference profiles
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to delete a stored response of a stateful invocation
  - **Resource types (\*required):** [project\*](#list_bedrock-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteKnowledgeBase.html)  **
  - **Description:** Grants permission to delete a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKnowledgeBaseDocuments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeleteKnowledgeBaseDocuments.html)  **
  - **Description:** Grants permission to delete documents from a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMarketplaceModelAgreement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to unsubscribe from a bedrock marketplace enabled AWS marketplace model
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMarketplaceModelEndpoint](API_DeleteMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to delete a marketplace model endpoint
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteModelInvocationLoggingConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteModelInvocationLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete an existing Invocation logging configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DeletePrompt.html)  **
  - **Description:** Grants permission to delete a prompt or its version
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt-version\*](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePromptRouter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeletePromptRouter.html)  **
  - **Description:** Grants permission to delete a custom prompt router
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteProvisionedModelThroughput.html)  **
  - **Description:** Grants permission to delete a provisioned model throughput that you created earlier
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html)  **
  - **Description:** Grants permission to delete a Session that you created earlier
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterMarketplaceModelEndpoint](API_DeregisterMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to deregister a marketplace model endpoint to make it unusable in Bedrock Marketplace
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DetectGeneratedContent](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to detect if the provided content is generated using Amazon Bedrock
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateAgentCollaborator](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentCollaborator.html)  **
  - **Description:** Grants permission to diassociate a collaborator that you associated earlier
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAgentKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DisassociateAgentKnowledgeBase.html)  **
  - **Description:** Grants permission to disassociate a knowledge base from the agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EndSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html)  **
  - **Description:** Grants permission to end a Session that you created earlier
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportAutomatedReasoningPolicyVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve an automated reasoning policy version artifact
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version\*](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GenerateQuery](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to generate queries associated with user input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAccountDataRetention](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetAccountDataRetention.html)  **
  - **Description:** Returns the account-wide data retention mode for Amazon Bedrock
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAdvancedPromptOptimizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetAdvancedPromptOptimizationJob.html)  **
  - **Description:** Grants permission to get information about an advanced prompt optimization job
  - **Resource types (\*required):** [advanced-prompt-optimization-job\*](#list_bedrock-resource-advanced-prompt-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html)  **
  - **Description:** Grants permission to retrieve an existing agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentActionGroup](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html)  **
  - **Description:** Grants permission to retrieve an existing action group
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentAlias.html)  **
  - **Description:** Grants permission to retrieve an existing alias
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentCollaborator](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentCollaborator.html)  **
  - **Description:** Grants permission to retrieve an existing collaborator
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentKnowledgeBase.html)  **
  - **Description:** Grants permission to describe a knowledge base associated with an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentMemory](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetAgentMemory.html)  **
  - **Description:** Grants permission to retrieve existing memory for an alias
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentVersion.html)  **
  - **Description:** Grants permission to retrieve an existing version of an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAsyncInvoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetAsyncInvoke.html)  **
  - **Description:** Grants permission to get the properties associated with an asynchronous invocation that you have submitted
  - **Resource types (\*required):** [async-invoke\*](#list_bedrock-resource-async-invoke)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve an automated reasoning policy or its version
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version\*](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyAnnotations](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve annotations for a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyBuildWorkflow](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyBuildWorkflowResultAssets](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve assets for a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyNextScenario](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve the next unreviewed generated scenario for a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyTestCase](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve a test case for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedReasoningPolicyTestResult](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve result for a test case for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlueprint](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_GetBlueprint.html)  **
  - **Description:** Grants permission to retrieve an existing blueprint for data automation
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBlueprintOptimizationStatus](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Data_Automation_for_Amazon_Bedrock.html)  **
  - **Description:** Grants permission to get the status of a blueprint optimization job
  - **Resource types (\*required):** [blueprint-optimization-invocation\*](#list_bedrock-resource-blueprint-optimization-invocation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html)  **
  - **Description:** Grants permission to get the properties associated with a Bedrock custom model that you have created
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html)  **
  - **Description:** Grants permission to get the properties associated with a custom model deployment. Use this operation to get the status of a custom model deployment
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAutomationLibrary](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_GetDataAutomationLibrary.html)  **
  - **Description:** Grants permission to retrieve an existing Data Automation Library
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAutomationLibraryEntity](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_GetDataAutomationLibraryEntity.html)  **
  - **Description:** Grants permission to get a Data Automation Library entity
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAutomationLibraryIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_GetDataAutomationLibraryIngestionJob.html)  **
  - **Description:** Grants permission to get details about a Data Automation Library ingestion job
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-library-ingestion-job\*](#list_bedrock-resource-data-automation-library-ingestion-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAutomationProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_GetDataAutomationProject.html)  **
  - **Description:** Grants permission to retrieve an existing data automation project
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataAutomationStatus](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_GetDataAutomationStatus.html)  **
  - **Description:** Grants permission to retrieve the status of a data automation invocation job
  - **Resource types (\*required):** [data-automation-invocation-job\*](#list_bedrock-resource-data-automation-invocation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetDataSource.html)  **
  - **Description:** Grants permission to retrieve an existing data source
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataSourceAuthorizationUrl](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-3lo-setup.html)  **
  - **Description:** Grants permission to get the authorization URL for a MANAGED\_OAUTH2 data source
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDocumentContent](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve a document
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetEvaluationJob.html)  **
  - **Description:** Grants permission to get the properties associated with a evaluation job. Use this operation to get the status of a evaluation job
  - **Resource types (\*required):** [evaluation-job\*](#list_bedrock-resource-evaluation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExecutionFlowSnapshot](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetExecutionFlowSnapshot.html)  **
  - **Description:** Grants permission to retrieve the flow definition for a flow execution
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-execution\*](#list_bedrock-resource-flow-execution) / **Condition keys:**  
  - **Access level:** Read

- **   [GetFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html)  **
  - **Description:** Grants permission to retrieve an existing prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFlowAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlowAlias.html)  **
  - **Description:** Grants permission to retrieve an existing alias of a prompt flow
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFlowExecution](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetFlowExecution.html)  **
  - **Description:** Grants permission to retrieve an existing execution of a flow alias
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-execution\*](#list_bedrock-resource-flow-execution) / **Condition keys:**  
  - **Access level:** Read

- **   [GetFlowVersion](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlowVersion.html)  **
  - **Description:** Grants permission to retrieve an existing version of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFoundationModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html)  **
  - **Description:** Grants permission to get the properties associated with a Bedrock foundation model
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFoundationModelAvailability](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to get the availability of a foundation model
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGuardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve a guardrail or its version
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImportedModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetImportedModel.html)  **
  - **Description:** Grants permission to get the properties associated with Bedrock imported model
  - **Resource types (\*required):** [imported-model\*](#list_bedrock-resource-imported-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInferenceProfile](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetInferenceProfile.html)  **
  - **Description:** Grants permission to get the properties associated with an inference profile
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:**  
  - **Access level:** Read

- **   [GetIngestedDocumentAcl](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetIngestedDocumentAcl.html)  **
  - **Description:** Grants permission to fetch the access control list for a specific document ingested in a knowledge base
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetIngestionJob.html)  **
  - **Description:** Grants permission to retrieve an existing ingestion job
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html)  **
  - **Description:** Grants permission to get an invocation step from a session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve a stored response of a stateful invocation
  - **Resource types (\*required):** [project\*](#list_bedrock-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html)  **
  - **Description:** Grants permission to retrieve an existing knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKnowledgeBaseDocuments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBaseDocuments.html)  **
  - **Description:** Grants permission to get details for documents in a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMarketplaceModelEndpoint](API_GetMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to get the properties of a marketplace model endpoint
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetModelCopyJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelCopyJob.html)  **
  - **Description:** Grants permission to get the properties associated with a model-copy job. Use this operation to get the status of a model-copy job
  - **Resource types (\*required):** [model-copy-job\*](#list_bedrock-resource-model-copy-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelCustomizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelCustomizationJob.html)  **
  - **Description:** Grants permission to get the properties associated with a model-customization job. Use this operation to get the status of a model-customization job
  - **Resource types (\*required):** [model-customization-job\*](#list_bedrock-resource-model-customization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelEvaluationJob.html)  **
  - **Description:** Grants permission to get the properties associated with a model-evaluation job. Use this operation to get the status of a model-evaluation job
  - **Resource types (\*required):** [model-evaluation-job\*](#list_bedrock-resource-model-evaluation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelImportJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelImportJob.html)  **
  - **Description:** Grants permission to get the properties associated with a model import job and is used to get the status of a model import job
  - **Resource types (\*required):** [model-import-job\*](#list_bedrock-resource-model-import-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelInvocationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelInvocationJob.html)  **
  - **Description:** Grants permission to retrieve a model invocation job
  - **Resource types (\*required):** [model-invocation-job\*](#list_bedrock-resource-model-invocation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelInvocationLoggingConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetModelInvocationLoggingConfiguration.html)  **
  - **Description:** Grants permission to retrieve an existing Invocation logging configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetPrompt.html)  **
  - **Description:** Grants permission to retrieve an existing prompt or its version
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt-version\*](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPromptRouter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetPromptRouter.html)  **
  - **Description:** Grants permission to get the properties associated with a prompt router
  - **Resource types (\*required):** [default-prompt-router\*](#list_bedrock-resource-default-prompt-router) / **Condition keys:**  
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetProvisionedModelThroughput.html)  **
  - **Description:** Grants permission to retrieve a provisioned model throughput
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html)  **
  - **Description:** Grants permission to retrieve an existing session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUseCaseForModelAccess](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to retrieve a use case for model access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [IngestKnowledgeBaseDocuments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_IngestKnowledgeBaseDocuments.html)  **
  - **Description:** Grants permission to directly ingest documents into a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html)  **
  - **Description:** Grants permission to send user input (text-only) to the alias of an agent for Bedrock
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeBlueprintOptimizationAsync](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Data_Automation_for_Amazon_Bedrock.html)  **
  - **Description:** Grants permission to invoke an async job to perform blueprint optimization
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-profile\*](#list_bedrock-resource-data-automation-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [InvokeDataAutomation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomation.html)  **
  - **Description:** Grants permission to invoke a call to Sync API of Bedrock data automation 
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-profile\*](#list_bedrock-resource-data-automation-profile) / **Condition keys:**  
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeDataAutomationAsync](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html)  **
  - **Description:** Grants permission to invoke a Bedrock data automation job
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-profile\*](#list_bedrock-resource-data-automation-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [InvokeDataAutomationLibraryIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.html)  **
  - **Description:** Grants permission to invoke a Data Automation Library ingestion job
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [InvokeFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeFlow.html)  **
  - **Description:** Grants permission to invoke a prompt flow with user input
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeGuardrailChecks](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke guardrail checks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InvokeInlineAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html)  **
  - **Description:** Grants permission to send user input (text-only) to the inline agent for Bedrock
  - **Resource types (\*required):** 
  - **Condition keys:** [bedrock:InlineAgentName](#list_bedrock-bedrock_InlineAgentName)
  - **Access level:** Read

- **   [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)  **
  - **Description:** Grants permission to invoke the specified Bedrock model to run inference using the input provided in the request body
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [async-invoke\*](#list_bedrock-resource-async-invoke) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [default-prompt-router\*](#list_bedrock-resource-default-prompt-router) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [imported-model\*](#list_bedrock-resource-imported-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [project\*](#list_bedrock-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [system-tool\*](#list_bedrock-resource-system-tool) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:ModelArn](#list_bedrock-bedrock_ModelArn)<br />[bedrock:ProjectArn](#list_bedrock-bedrock_ProjectArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Access level:** Read

- **   [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)  **
  - **Description:** Grants permission to invoke the specified Bedrock model to run inference using the input provided in the request body with streaming response
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint) / **Condition keys:** [bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [default-prompt-router\*](#list_bedrock-resource-default-prompt-router) / **Condition keys:** [bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:** [bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [imported-model\*](#list_bedrock-resource-imported-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [inference-profile\*](#list_bedrock-resource-inference-profile) / **Condition keys:** [bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Resource types (\*required):** [system-tool\*](#list_bedrock-resource-system-tool) / **Condition keys:** [bedrock:GuardrailIdentifier](#list_bedrock-bedrock_GuardrailIdentifier)<br />[bedrock:InferenceProfileArn](#list_bedrock-bedrock_InferenceProfileArn)<br />[bedrock:PromptRouterArn](#list_bedrock-bedrock_PromptRouterArn)<br />[bedrock:ServiceTier](#list_bedrock-bedrock_ServiceTier)
  - **Access level:** Read

- **   [InvokeTool](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeTool.html)  **
  - **Description:** Grants permission to invoke the specified Bedrock tool to run inference
  - **Resource types (\*required):** [system-tool\*](#list_bedrock-resource-system-tool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAdvancedPromptOptimizationJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListAdvancedPromptOptimizationJobs.html)  **
  - **Description:** Grants permission to list the advanced prompt optimization jobs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAgentActionGroups](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html)  **
  - **Description:** Grants permission to list action groups in an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentAliases](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentAliases.html)  **
  - **Description:** Grants permission to list aliases for an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentCollaborators](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentCollaborators.html)  **
  - **Description:** Grants permission to list collaborators for an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentKnowledgeBases](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html)  **
  - **Description:** Grants permission to list knowledge bases associated with an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentVersions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentVersions.html)  **
  - **Description:** Grants permission to list existing versions of an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgents](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgents.html)  **
  - **Description:** Grants permission to list existing agents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAsyncInvokes](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListAsyncInvokes.html)  **
  - **Description:** Grants permission to get a list of asynchronous invocations that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomatedReasoningPolicies](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to list automated reasoning policies or its versions
  - **Resource types (\*required):** [automated-reasoning-policy](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutomatedReasoningPolicyBuildWorkflows](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to list build workflows for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutomatedReasoningPolicyTestCases](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to list test cases for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAutomatedReasoningPolicyTestResults](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to list test result for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBlueprints](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ListBlueprints.html)  **
  - **Description:** Grants permission to list existing blueprints for data automation
  - **Resource types (\*required):** [data-automation-project](#list_bedrock-resource-data-automation-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomModelDeployments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html)  **
  - **Description:** Grants permission to get the list of custom model deployments that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html)  **
  - **Description:** Grants permission to get a list of Bedrock custom models that you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataAutomationLibraries](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ListDataAutomationLibraries.html)  **
  - **Description:** Grants permission to list Data Automation Libraries
  - **Resource types (\*required):** [data-automation-project](#list_bedrock-resource-data-automation-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataAutomationLibraryEntities](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ListDataAutomationLibraryEntities.html)  **
  - **Description:** Grants permission to list Data Automation Library entities
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataAutomationLibraryIngestionJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ListDataAutomationLibraryIngestionJobs.html)  **
  - **Description:** Grants permission to list Data Automation Library ingestion jobs
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataAutomationProjects](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_ListDataAutomationProjects.html)  **
  - **Description:** Grants permission to list existing data automation projects
  - **Resource types (\*required):** [blueprint](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-project](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListDataSources.html)  **
  - **Description:** Grants permission to list existing data sources in an knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnforcedGuardrailsConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListEnforcedGuardrailsConfiguration.html)  **
  - **Description:** Grants permission to list account-level enforced guardrail configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEvaluationJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListEvaluationJobs.html)  **
  - **Description:** Grants permission to get the list of evaluation jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFlowAliases](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlowAliases.html)  **
  - **Description:** Grants permission to list existing aliases of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlowExecutionEvents](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListFlowExecutionEvents.html)  **
  - **Description:** Grants permission to retrieve events for a flow execution
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-execution\*](#list_bedrock-resource-flow-execution) / **Condition keys:**  
  - **Access level:** List

- **   [ListFlowExecutions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListFlowExecutions.html)  **
  - **Description:** Grants permission to list executions of a flow or a flow alias
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlowVersions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlowVersions.html)  **
  - **Description:** Grants permission to list existing versions of a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFlows](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListFlows.html)  **
  - **Description:** Grants permission to list existing prompt flows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFoundationModelAgreementOffers](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to get a list of foundation model agreement offers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFoundationModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html)  **
  - **Description:** Grants permission to list Bedrock foundation models that you can use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGuardrails](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to list guardrails or its versions
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImportedModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListImportedModels.html)  **
  - **Description:** Grants permission to get list of Bedrock imported models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceProfiles](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListInferenceProfiles.html)  **
  - **Description:** Grants permission to list inference profiles that you can use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIngestionJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListIngestionJobs.html)  **
  - **Description:** Grants permission to list ingestion jobs in a data source
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvocationSteps](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocationSteps.html)  **
  - **Description:** Grants permission to get list of invocation step from a session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInvocations](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html)  **
  - **Description:** Grants permission to list invocations in a session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKnowledgeBaseDocuments](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListKnowledgeBaseDocuments.html)  **
  - **Description:** Grants permission to list documents in a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKnowledgeBases](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListKnowledgeBases.html)  **
  - **Description:** Grants permission to list existing knowledge bases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMarketplaceModelEndpoints](API_ListMarketplaceModelEndpoints)  **
  - **Description:** Grants permission to list marketplace model endpoints that you can use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListModelCopyJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelCopyJobs.html)  **
  - **Description:** Grants permission to get the list of model copy jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelCustomizationJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelCustomizationJobs.html)  **
  - **Description:** Grants permission to get the list of model customization jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelEvaluationJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelEvaluationJobs.html)  **
  - **Description:** Grants permission to get the list of model evaluation jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelImportJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelImportJobs.html)  **
  - **Description:** Grants permission to get list of model import jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelInvocationJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListModelInvocationJobs.html)  **
  - **Description:** Grants permission to list model invocation jobs that you created earlier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPromptRouters](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListPromptRouters.html)  **
  - **Description:** Grants permission to list prompt routers that you can use
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrompts](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListPrompts.html)  **
  - **Description:** Grants permission to list existing prompts
  - **Resource types (\*required):** [prompt](#list_bedrock-resource-prompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProvisionedModelThroughputs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListProvisionedModelThroughputs.html)  **
  - **Description:** Grants permission to list provisioned model throughputs that you created earlier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html)  **
  - **Description:** Grants permission to list existing sessions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Bedrock resource
  - **Resource types (\*required):** [advanced-prompt-optimization-job\*](#list_bedrock-resource-advanced-prompt-optimization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [application-inference-profile\*](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [async-invoke\*](#list_bedrock-resource-async-invoke) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version\*](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [blueprint-optimization-invocation\*](#list_bedrock-resource-blueprint-optimization-invocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-invocation-job\*](#list_bedrock-resource-data-automation-invocation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-library-ingestion-job\*](#list_bedrock-resource-data-automation-library-ingestion-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [evaluation-job\*](#list_bedrock-resource-evaluation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imported-model\*](#list_bedrock-resource-imported-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-copy-job\*](#list_bedrock-resource-model-copy-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-customization-job\*](#list_bedrock-resource-model-customization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-evaluation-job\*](#list_bedrock-resource-model-evaluation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-import-job\*](#list_bedrock-resource-model-import-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-invocation-job\*](#list_bedrock-resource-model-invocation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt-router\*](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt-version\*](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [OptimizePrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_OptimizePrompt.html)  **
  - **Description:** Grants permission to optimize a prompt with user input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PrepareAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareAgent.html)  **
  - **Description:** Grants permission to prepare an existing agent to receive runtime requests
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PrepareFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareFlow.html)  **
  - **Description:** Grants permission to apply the latest changes made to a prompt flow, so that they are reflected at runtime
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutAccountDataRetention](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutAccountDataRetention.html)  **
  - **Description:** Sets the account-wide data retention mode for Amazon Bedrock
  - **Resource types (\*required):** 
  - **Condition keys:** [bedrock:DataRetentionMode](#list_bedrock-bedrock_DataRetentionMode)
  - **Access level:** Write

- **   [PutEnforcedGuardrailConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutEnforcedGuardrailConfiguration.html)  **
  - **Description:** Grants permission to set account-level enforced guardrail configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutFoundationModelEntitlement](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to put entitlement to access a serverless foundation model. Do not use to restrict model access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_PutInvocationStep.html)  **
  - **Description:** Grants permission to put an invocation step into an invocation in session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutModelInvocationLoggingConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutModelInvocationLoggingConfiguration.html)  **
  - **Description:** Grants permission to create an existing Invocation logging configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutUseCaseForModelAccess](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html)  **
  - **Description:** Grants permission to put a use case for model access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterMarketplaceModelEndpoint](API_RegisterMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to register a sagemaker endpoint as a marketplace model endpoint
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [Rerank](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to rank documents based on user input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve ingested data from a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to send user input to perform retrieval and generation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAutomatedReasoningPolicyBuildWorkflow](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to start a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAutomatedReasoningPolicyTestWorkflow](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to start a test workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartFlowExecution](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_StartFlowExecution.html)  **
  - **Description:** Grants permission to start an execution of a flow alias
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StartIngestionJob.html)  **
  - **Description:** Grants permission to start an ingestion job
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAdvancedPromptOptimizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StopAdvancedPromptOptimizationJob.html)  **
  - **Description:** Grants permission to stop an advanced prompt optimization job while in progress
  - **Resource types (\*required):** [advanced-prompt-optimization-job\*](#list_bedrock-resource-advanced-prompt-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEvaluationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StopEvaluationJob.html)  **
  - **Description:** Grants permission to stop a evaluation job while in progress
  - **Resource types (\*required):** [evaluation-job\*](#list_bedrock-resource-evaluation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopFlowExecution](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_StopFlowExecution.html)  **
  - **Description:** Grants permission to stop an execution of a flow alias
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-execution\*](#list_bedrock-resource-flow-execution) / **Condition keys:**  
  - **Access level:** Write

- **   [StopIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StopIngestionJob.html)  **
  - **Description:** Grants permission to stop an ingestion job
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopModelCustomizationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StopModelCustomizationJob.html)  **
  - **Description:** Grants permission to stop a Bedrock model customization job while in progress
  - **Resource types (\*required):** [model-customization-job\*](#list_bedrock-resource-model-customization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopModelInvocationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StopModelInvocationJob.html)  **
  - **Description:** Grants permission to stop a model invocation job that you started earlier
  - **Resource types (\*required):** [model-invocation-job\*](#list_bedrock-resource-model-invocation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to Tag a Bedrock resource
  - **Resource types (\*required):** [advanced-prompt-optimization-job](#list_bedrock-resource-advanced-prompt-optimization-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [agent](#list_bedrock-resource-agent) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [agent-alias](#list_bedrock-resource-agent-alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [application-inference-profile](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [async-invoke](#list_bedrock-resource-async-invoke) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [automated-reasoning-policy](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [automated-reasoning-policy-version](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [blueprint](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [blueprint-optimization-invocation](#list_bedrock-resource-blueprint-optimization-invocation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [custom-model](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [custom-model-deployment](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-invocation-job](#list_bedrock-resource-data-automation-invocation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-library](#list_bedrock-resource-data-automation-library) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-library-ingestion-job](#list_bedrock-resource-data-automation-library-ingestion-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-project](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [evaluation-job](#list_bedrock-resource-evaluation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_bedrock-resource-flow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [flow-alias](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [imported-model](#list_bedrock-resource-imported-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-copy-job](#list_bedrock-resource-model-copy-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-customization-job](#list_bedrock-resource-model-customization-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-evaluation-job](#list_bedrock-resource-model-evaluation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-import-job](#list_bedrock-resource-model-import-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-invocation-job](#list_bedrock-resource-model-invocation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt](#list_bedrock-resource-prompt) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt-router](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt-version](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [provisioned-model](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_bedrock-resource-session) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to Untag a Bedrock resource
  - **Resource types (\*required):** [advanced-prompt-optimization-job](#list_bedrock-resource-advanced-prompt-optimization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [agent](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [agent-alias](#list_bedrock-resource-agent-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [application-inference-profile](#list_bedrock-resource-application-inference-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [async-invoke](#list_bedrock-resource-async-invoke) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [automated-reasoning-policy](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [automated-reasoning-policy-version](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [blueprint](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [blueprint-optimization-invocation](#list_bedrock-resource-blueprint-optimization-invocation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [custom-model](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [custom-model-deployment](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-invocation-job](#list_bedrock-resource-data-automation-invocation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-library](#list_bedrock-resource-data-automation-library) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-library-ingestion-job](#list_bedrock-resource-data-automation-library-ingestion-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [data-automation-project](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [evaluation-job](#list_bedrock-resource-evaluation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [flow](#list_bedrock-resource-flow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [flow-alias](#list_bedrock-resource-flow-alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [imported-model](#list_bedrock-resource-imported-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-copy-job](#list_bedrock-resource-model-copy-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-customization-job](#list_bedrock-resource-model-customization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-evaluation-job](#list_bedrock-resource-model-evaluation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-import-job](#list_bedrock-resource-model-import-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [model-invocation-job](#list_bedrock-resource-model-invocation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt](#list_bedrock-resource-prompt) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt-router](#list_bedrock-resource-prompt-router) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [prompt-version](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [provisioned-model](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [session](#list_bedrock-resource-session) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgent.html)  **
  - **Description:** Grants permission to update an existing agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentActionGroup](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentActionGroup.html)  **
  - **Description:** Grants permission to update an existing action group
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentAlias.html)  **
  - **Description:** Grants permission to update an existing alias
  - **Resource types (\*required):** [agent-alias\*](#list_bedrock-resource-agent-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentCollaborator](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentCollaborator.html)  **
  - **Description:** Grants permission to update an existing collaborator
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgentKnowledgeBase.html)  **
  - **Description:** Grants permission to update a knowledge base associated with an agent
  - **Resource types (\*required):** [agent\*](#list_bedrock-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomatedReasoningPolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to update an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomatedReasoningPolicyAnnotations](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to update annotations for a build workflow for an automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomatedReasoningPolicyTestCase](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to update a test case for automated reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBlueprint](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_UpdateBlueprint.html)  **
  - **Description:** Grants permission to update a blueprint for data automation
  - **Resource types (\*required):** [blueprint\*](#list_bedrock-resource-blueprint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomModelDeployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_UpdateCustomModelDeployment.html)  **
  - **Description:** Grants permission to update an existing custom model deployment with a new custom model
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom-model-deployment\*](#list_bedrock-resource-custom-model-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataAutomationLibrary](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationLibrary.html)  **
  - **Description:** Grants permission to update a Data Automation Library
  - **Resource types (\*required):** [data-automation-library\*](#list_bedrock-resource-data-automation-library)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataAutomationProject](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_UpdateDataAutomationProject.html)  **
  - **Description:** Grants permission to update a data automation project
  - **Resource types (\*required):** [blueprint](#list_bedrock-resource-blueprint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-automation-project\*](#list_bedrock-resource-data-automation-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateDataSource.html)  **
  - **Description:** Grants permission to update a data source
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateFlow.html)  **
  - **Description:** Grants permission to update a prompt flow
  - **Resource types (\*required):** [flow\*](#list_bedrock-resource-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlowAlias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateFlowAlias.html)  **
  - **Description:** Grants permission to update the configuration of an alias of a prompt flow
  - **Resource types (\*required):** [flow-alias\*](#list_bedrock-resource-flow-alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGuardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to update a guardrail
  - **Resource types (\*required):** [automated-reasoning-policy](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail\*](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateKnowledgeBase.html)  **
  - **Description:** Grants permission to update a knowledge base
  - **Resource types (\*required):** [knowledge-base\*](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMarketplaceModelEndpoint](API_UpdateMarketplaceModelEndpoint)  **
  - **Description:** Grants permission to update a marketplace model endpoint
  - **Resource types (\*required):** [bedrock-marketplace-model-endpoint\*](#list_bedrock-resource-bedrock-marketplace-model-endpoint)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdatePrompt.html)  **
  - **Description:** Grants permission to update a prompt
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_UpdateProvisionedModelThroughput.html)  **
  - **Description:** Grants permission to update a provisioned model throughput that you created earlier
  - **Resource types (\*required):** [custom-model\*](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [foundation-model\*](#list_bedrock-resource-foundation-model) / **Condition keys:**  
  - **Resource types (\*required):** [provisioned-model\*](#list_bedrock-resource-provisioned-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSession](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_UpdateSession.html)  **
  - **Description:** Grants permission to update an existing session
  - **Resource types (\*required):** [session\*](#list_bedrock-resource-session)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateFlowDefinition](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ValidateFlowDefinition.html)  **
  - **Description:** Grants permission to validate prompt flow definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Permission-only actions for Amazon Bedrock
<a name="list_bedrock-permission-only-actions"></a>

The following actions are defined by Amazon Bedrock but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to configure vended log delivery for a knowledge base
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AssociateThirdPartyKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to use 3rd party platform to store knowledge data
  - **Resource types (\*required):** 
  - **Condition keys:** [bedrock:ThirdPartyKnowledgeBaseCredentialsSecretArn](#list_bedrock-bedrock_ThirdPartyKnowledgeBaseCredentialsSecretArn)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Deletes a previously created Bedrock resource policy
  - **Resource types (\*required):** [custom-model](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:**  
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBlueprintRecommendation](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to retrieve blueprint recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetResourePolicy.html)  **
  - **Description:** Gets the resource policy document for a Bedrock resource
  - **Resource types (\*required):** [custom-model](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:**  
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAutomatedReasoningPolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke an Automated Reasoning policy
  - **Resource types (\*required):** [automated-reasoning-policy\*](#list_bedrock-resource-automated-reasoning-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automated-reasoning-policy-version\*](#list_bedrock-resource-automated-reasoning-policy-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeBlueprintRecommendationAsync](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke blueprint recommendations asynchronously
  - **Resource types (\*required):** [data-automation-profile\*](#list_bedrock-resource-data-automation-profile)
  - **Condition keys:**  
  - **Access level:** Write

- **   [InvokeBuilder](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create-cb.html)  **
  - **Description:** Grants permission to use the conversational builder which aids in building supported bedrock resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Adds a resource policy for a Bedrock resource
  - **Resource types (\*required):** [custom-model](#list_bedrock-resource-custom-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [guardrail](#list_bedrock-resource-guardrail) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [guardrail-profile](#list_bedrock-resource-guardrail-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Resource types (\*required):** [knowledge-base](#list_bedrock-resource-knowledge-base) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-aws_TagKeys)
  - **Access level:** Write

- **   [RenderPrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to render an existing prompt or its version
  - **Resource types (\*required):** [prompt\*](#list_bedrock-resource-prompt) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [prompt-version\*](#list_bedrock-resource-prompt-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Bedrock
<a name="list_bedrock-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [advanced-prompt-optimization-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:advanced-prompt-optimization-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [agent](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:agent/${AgentId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [agent-alias](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:agent-alias/${AgentId}/${AgentAliasId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [application-inference-profile](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:application-inference-profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [async-invoke](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:async-invoke/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [automated-reasoning-policy](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:automated-reasoning-policy/${AutomatedReasoningPolicyId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [automated-reasoning-policy-version](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:automated-reasoning-policy/${AutomatedReasoningPolicyId}:${AutomatedReasoningPolicyVersion} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [bedrock-marketplace-model-endpoint](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:marketplace/model-endpoint/all-access |   | 
|  [blueprint](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:blueprint/${BlueprintId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [blueprint-optimization-invocation](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Data_Automation_for_Amazon_Bedrock.html)  | arn:${Partition}:bedrock:${Region}:${Account}:blueprint-optimization-invocation/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [custom-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:custom-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [custom-model-deployment](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:custom-model-deployment/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [data-automation-invocation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:data-automation-invocation/${JobId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [data-automation-library](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:data-automation-library/${DataAutomationLibraryId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [data-automation-library-ingestion-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:data-automation-library-ingestion-job/${IngestionJobId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [data-automation-profile](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:data-automation-profile/${ProfileId} |   | 
|  [data-automation-project](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:data-automation-project/${ProjectId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [default-prompt-router](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:default-prompt-router/${ResourceId} |   | 
|  [evaluation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:evaluation-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [flow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_FlowSummary.html)  | arn:${Partition}:bedrock:${Region}:${Account}:flow/${FlowId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [flow-alias](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_FlowAliasSummary.html)  | arn:${Partition}:bedrock:${Region}:${Account}:flow/${FlowId}/alias/${FlowAliasId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [flow-execution](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_FlowExecutionSummary.html)  | arn:${Partition}:bedrock:${Region}:${Account}:flow/${FlowId}/alias/${FlowAliasId}/execution/${FlowExecutionId} |   | 
|  [foundation-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}::foundation-model/${ResourceId} |   | 
|  [guardrail](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:guardrail/${GuardrailId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [guardrail-profile](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrail-profiles-permissions.html)  | arn:${Partition}:bedrock:${Region}:${Account}:guardrail-profile/${ResourceId} |   | 
|  [imported-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:imported-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [inference-profile](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:inference-profile/${ResourceId} |   | 
|  [knowledge-base](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:knowledge-base/${KnowledgeBaseId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [model-copy-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:model-copy-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [model-customization-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:model-customization-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [model-evaluation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:model-evaluation-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [model-import-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:model-import-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [model-invocation-job](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:model-invocation-job/${JobIdentifier} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:project/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [prompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptSummary.html)  | arn:${Partition}:bedrock:${Region}:${Account}:prompt/${PromptId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [prompt-router](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:prompt-router/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [prompt-version](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptSummary.html)  | arn:${Partition}:bedrock:${Region}:${Account}:prompt/${PromptId}:${PromptVersion} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [provisioned-model](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:provisioned-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [session](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock:${Region}:${Account}:session/${SessionId} | [aws:ResourceTag/${TagKey}](#list_bedrock-aws_ResourceTag___TagKey_) | 
|  [system-tool](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)  | arn:${Partition}:bedrock::${Account}:system-tool/${ResourceId} |   | 

## Condition keys for Amazon Bedrock
<a name="list_bedrock-policy-keys"></a>

Amazon Bedrock defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the allowed set of values for each of the mandatory tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by having actions based on the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the presence of mandatory tags in the request | ArrayOfString | 
|   [bedrock:BearerTokenType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the Short-term or Long-term bearer tokens | String | 
|   [bedrock:DataRetentionMode](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the specified Data Retention Mode | String | 
|   [bedrock:GuardrailIdentifier](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the GuardrailIdentifier containing the GuardrailArn or the GuardrailArn:NumericVersion | ARN | 
|   [bedrock:InferenceProfileArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the specified inference profile | ARN | 
|   [bedrock:InlineAgentName](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the Inline Agent Names, this will be used in InvokeInlineAgent API names | String | 
|   [bedrock:ModelArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the model that a stateful invocation runs, on the authorization whose resource is the project | ARN | 
|   [bedrock:ProjectArn](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the project that a stateful invocation belongs to, on authorizations whose resource is the inference target it runs | ARN | 
|   [bedrock:PromptRouterArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the specified prompt router | ARN | 
|   [bedrock:ServiceTier](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html#amazonbedrock-policy-keys)  | Filters access by the specified ServiceTier | String | 
|   [bedrock:ThirdPartyKnowledgeBaseCredentialsSecretArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by the secretArn containing the credentials of the third party platform | ARN | 