

# Actions, resources, and condition keys for Amazon Lex V2
<a name="list_lex-v2"></a>

Amazon Lex V2 (service prefix: `lex`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lexv2/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lexv2/latest/APIReference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lexv2/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lex/lex.json) for this service.

**Topics**
+ [API operations defined by Amazon Lex V2](#list_lex-v2-operations)
+ [Actions defined by Amazon Lex V2](#list_lex-v2-actions-as-permissions)
+ [Permission-only actions for Amazon Lex V2](#list_lex-v2-permission-only-actions)
+ [Resource types defined by Amazon Lex V2](#list_lex-v2-resources-for-iam-policies)
+ [Condition keys for Amazon Lex V2](#list_lex-v2-policy-keys)

## API operations defined by Amazon Lex V2
<a name="list_lex-v2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_lex-v2-actions-as-permissions).




- **   BatchCreateCustomVocabularyItem  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:BatchCreateCustomVocabularyItem](#list_lex-v2-action-BatchCreateCustomVocabularyItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteCustomVocabularyItem  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:BatchDeleteCustomVocabularyItem](#list_lex-v2-action-BatchDeleteCustomVocabularyItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateCustomVocabularyItem  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:BatchUpdateCustomVocabularyItem](#list_lex-v2-action-BatchUpdateCustomVocabularyItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BuildBotLocale  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:BuildBotLocale](#list_lex-v2-action-BuildBotLocale) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBot](#list_lex-v2-action-CreateBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DescribeBotAlias](#list_lex-v2-action-DescribeBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotVersion](#list_lex-v2-action-DescribeBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:TagResource](#list_lex-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lexv2.amazonaws.com / **Access level:** Write

- **   CreateBotAlias  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBotAlias](#list_lex-v2-action-CreateBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:TagResource](#list_lex-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBotLocale  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBotLocale](#list_lex-v2-action-CreateBotLocale) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBotReplica  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBotReplica](#list_lex-v2-action-CreateBotReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBotVersion  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBotVersion](#list_lex-v2-action-CreateBotVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateExport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateExport](#list_lex-v2-action-CreateExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateIntent  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateIntent](#list_lex-v2-action-CreateIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourcePolicy  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateResourcePolicy](#list_lex-v2-action-CreateResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourcePolicyStatement  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateResourcePolicy](#list_lex-v2-action-CreateResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateResourcePolicy](#list_lex-v2-action-UpdateResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSlot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateSlot](#list_lex-v2-action-CreateSlot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSlotType  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateSlotType](#list_lex-v2-action-CreateSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTestSetDiscrepancyReport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateTestSetDiscrepancyReport](#list_lex-v2-action-CreateTestSetDiscrepancyReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateUploadUrl  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateUploadUrl](#list_lex-v2-action-CreateUploadUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBot](#list_lex-v2-action-DeleteBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotAlias](#list_lex-v2-action-DeleteBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotChannel](#list_lex-v2-action-DeleteBotChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotLocale](#list_lex-v2-action-DeleteBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotVersion](#list_lex-v2-action-DeleteBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteCustomVocabulary](#list_lex-v2-action-DeleteCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-v2-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteResourcePolicy](#list_lex-v2-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](#list_lex-v2-action-DeleteSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-v2-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBotAlias  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBotAlias](#list_lex-v2-action-DeleteBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteResourcePolicy](#list_lex-v2-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBotAnalyzerRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBotAnalyzerRecommendation](#list_lex-v2-action-DeleteBotAnalyzerRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBotLocale  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBotLocale](#list_lex-v2-action-DeleteBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteCustomVocabulary](#list_lex-v2-action-DeleteCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-v2-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](#list_lex-v2-action-DeleteSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-v2-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBotReplica  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBotReplica](#list_lex-v2-action-DeleteBotReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBotVersion  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteBotVersion](#list_lex-v2-action-DeleteBotVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomVocabulary  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteCustomVocabulary](#list_lex-v2-action-DeleteCustomVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteExport](#list_lex-v2-action-DeleteExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteImport](#list_lex-v2-action-DeleteImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIntent  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteIntent](#list_lex-v2-action-DeleteIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteResourcePolicy](#list_lex-v2-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicyStatement  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteResourcePolicy](#list_lex-v2-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateResourcePolicy](#list_lex-v2-action-UpdateResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSlot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteSlot](#list_lex-v2-action-DeleteSlot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlotType  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-v2-action-DeleteSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTestSet  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteTestSet](#list_lex-v2-action-DeleteTestSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUtterances  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DeleteUtterances](#list_lex-v2-action-DeleteUtterances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBot](#list_lex-v2-action-DescribeBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotAlias](#list_lex-v2-action-DescribeBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotVersion](#list_lex-v2-action-DescribeBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBotAlias  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotAlias](#list_lex-v2-action-DescribeBotAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotAnalyzerRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotAnalyzerRecommendation](#list_lex-v2-action-DescribeBotAnalyzerRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotLocale  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotLocale](#list_lex-v2-action-DescribeBotLocale) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotRecommendation](#list_lex-v2-action-DescribeBotRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotReplica  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotReplica](#list_lex-v2-action-DescribeBotReplica) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotResourceGeneration  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotResourceGeneration](#list_lex-v2-action-DescribeBotResourceGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeBotVersion  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotAlias](#list_lex-v2-action-DescribeBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotVersion](#list_lex-v2-action-DescribeBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeCustomVocabularyMetadata  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeCustomVocabularyMetadata](#list_lex-v2-action-DescribeCustomVocabularyMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBot](#list_lex-v2-action-DescribeBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotLocale](#list_lex-v2-action-DescribeBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeCustomVocabulary](#list_lex-v2-action-DescribeCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeExport](#list_lex-v2-action-DescribeExport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeIntent](#list_lex-v2-action-DescribeIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeSlot](#list_lex-v2-action-DescribeSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeSlotType](#list_lex-v2-action-DescribeSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeTestSet](#list_lex-v2-action-DescribeTestSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:ListBotLocales](#list_lex-v2-action-ListBotLocales)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lex:ListIntents](#list_lex-v2-action-ListIntents)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lex:ListSlots](#list_lex-v2-action-ListSlots)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [lex:ListSlotTypes](#list_lex-v2-action-ListSlotTypes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeImport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeImport](#list_lex-v2-action-DescribeImport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIntent  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeIntent](#list_lex-v2-action-DescribeIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeResourcePolicy](#list_lex-v2-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSlot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeSlot](#list_lex-v2-action-DescribeSlot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSlotType  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeSlotType](#list_lex-v2-action-DescribeSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTestExecution  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeTestExecution](#list_lex-v2-action-DescribeTestExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTestSet  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeTestSet](#list_lex-v2-action-DescribeTestSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTestSetDiscrepancyReport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeTestSetDiscrepancyReport](#list_lex-v2-action-DescribeTestSetDiscrepancyReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTestSetGeneration  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeTestSetGeneration](#list_lex-v2-action-DescribeTestSetGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GenerateBotElement  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:GenerateBotElement](#list_lex-v2-action-GenerateBotElement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTestExecutionArtifactsUrl  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:GetTestExecutionArtifactsUrl](#list_lex-v2-action-GetTestExecutionArtifactsUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAggregatedUtterances  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListAggregatedUtterances](#list_lex-v2-action-ListAggregatedUtterances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotAliasReplicas  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotAliasReplicas](#list_lex-v2-action-ListBotAliasReplicas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotAliases  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotAliases](#list_lex-v2-action-ListBotAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotLocales  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotLocales](#list_lex-v2-action-ListBotLocales) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotRecommendations  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotRecommendations](#list_lex-v2-action-ListBotRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotReplicas  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotReplicas](#list_lex-v2-action-ListBotReplicas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotResourceGenerations  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotResourceGenerations](#list_lex-v2-action-ListBotResourceGenerations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotVersionReplicas  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotVersionReplicas](#list_lex-v2-action-ListBotVersionReplicas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBotVersions  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBotVersions](#list_lex-v2-action-ListBotVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBots  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBots](#list_lex-v2-action-ListBots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuiltInIntents  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBuiltInIntents](#list_lex-v2-action-ListBuiltInIntents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBuiltInSlotTypes  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListBuiltInSlotTypes](#list_lex-v2-action-ListBuiltInSlotTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomVocabularyItems  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListCustomVocabularyItems](#list_lex-v2-action-ListCustomVocabularyItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExports  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListExports](#list_lex-v2-action-ListExports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImports  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListImports](#list_lex-v2-action-ListImports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntentMetrics  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListIntentMetrics](#list_lex-v2-action-ListIntentMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntentPaths  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListIntentPaths](#list_lex-v2-action-ListIntentPaths) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntentStageMetrics  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListIntentStageMetrics](#list_lex-v2-action-ListIntentStageMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIntents  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListIntents](#list_lex-v2-action-ListIntents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendedIntents  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListRecommendedIntents](#list_lex-v2-action-ListRecommendedIntents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessionAnalyticsData  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListSessionAnalyticsData](#list_lex-v2-action-ListSessionAnalyticsData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessionMetrics  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListSessionMetrics](#list_lex-v2-action-ListSessionMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSlotTypes  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListSlotTypes](#list_lex-v2-action-ListSlotTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSlots  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListSlots](#list_lex-v2-action-ListSlots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListTagsForResource](#list_lex-v2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestExecutionResultItems  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListTestExecutionResultItems](#list_lex-v2-action-ListTestExecutionResultItems)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:ListTestSetRecords](#list_lex-v2-action-ListTestSetRecords)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListTestExecutions  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListTestExecutions](#list_lex-v2-action-ListTestExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTestSetRecords  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListTestSetRecords](#list_lex-v2-action-ListTestSetRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTestSets  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListTestSets](#list_lex-v2-action-ListTestSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUtteranceAnalyticsData  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListAggregatedUtterances](#list_lex-v2-action-ListAggregatedUtterances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUtteranceMetrics  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:ListAggregatedUtterances](#list_lex-v2-action-ListAggregatedUtterances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchAssociatedTranscripts  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:SearchAssociatedTranscripts](#list_lex-v2-action-SearchAssociatedTranscripts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartBotAnalyzer  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StartBotAnalyzer](#list_lex-v2-action-StartBotAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBotRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateIntent](#list_lex-v2-action-CreateIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlot](#list_lex-v2-action-CreateSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlotType](#list_lex-v2-action-CreateSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-v2-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](#list_lex-v2-action-DeleteSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-v2-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:StartBotRecommendation](#list_lex-v2-action-StartBotRecommendation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartBotResourceGeneration  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StartBotResourceGeneration](#list_lex-v2-action-StartBotResourceGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:CreateBot](#list_lex-v2-action-CreateBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateBotLocale](#list_lex-v2-action-CreateBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateCustomVocabulary](#list_lex-v2-action-CreateCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateIntent](#list_lex-v2-action-CreateIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlot](#list_lex-v2-action-CreateSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateSlotType](#list_lex-v2-action-CreateSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:CreateTestSet](#list_lex-v2-action-CreateTestSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteBotLocale](#list_lex-v2-action-DeleteBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteCustomVocabulary](#list_lex-v2-action-DeleteCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteIntent](#list_lex-v2-action-DeleteIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlot](#list_lex-v2-action-DeleteSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:DeleteSlotType](#list_lex-v2-action-DeleteSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:StartImport](#list_lex-v2-action-StartImport)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:TagResource](#list_lex-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [lex:UpdateBot](#list_lex-v2-action-UpdateBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateBotLocale](#list_lex-v2-action-UpdateBotLocale)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateCustomVocabulary](#list_lex-v2-action-UpdateCustomVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateIntent](#list_lex-v2-action-UpdateIntent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateSlot](#list_lex-v2-action-UpdateSlot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateSlotType](#list_lex-v2-action-UpdateSlotType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:UpdateTestSet](#list_lex-v2-action-UpdateTestSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lexv2.amazonaws.com / **Access level:** Write

- **   StartTestExecution  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StartTestExecution](#list_lex-v2-action-StartTestExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTestSetGeneration  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StartTestSetGeneration](#list_lex-v2-action-StartTestSetGeneration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lex:TagResource](#list_lex-v2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lexv2.amazonaws.com / **Access level:** Write

- **   StopBotAnalyzer  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StopBotAnalyzer](#list_lex-v2-action-StopBotAnalyzer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBotRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:StopBotRecommendation](#list_lex-v2-action-StopBotRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:TagResource](#list_lex-v2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UntagResource](#list_lex-v2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:DescribeBotAlias](#list_lex-v2-action-DescribeBotAlias)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:DescribeBotVersion](#list_lex-v2-action-DescribeBotVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lex:UpdateBot](#list_lex-v2-action-UpdateBot)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lexv2.amazonaws.com / **Access level:** Write

- **   UpdateBotAlias  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateBotAlias](#list_lex-v2-action-UpdateBotAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBotLocale  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateBotLocale](#list_lex-v2-action-UpdateBotLocale) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBotRecommendation  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateBotRecommendation](#list_lex-v2-action-UpdateBotRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExport  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateExport](#list_lex-v2-action-UpdateExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIntent  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateIntent](#list_lex-v2-action-UpdateIntent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourcePolicy  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateResourcePolicy](#list_lex-v2-action-UpdateResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSlot  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateSlot](#list_lex-v2-action-UpdateSlot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSlotType  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateSlotType](#list_lex-v2-action-UpdateSlotType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTestSet  **
  - **SDK client:** lexv2-models
  - **IAM action:**  [lex:UpdateTestSet](#list_lex-v2-action-UpdateTestSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSession  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:DeleteSession](#list_lex-v2-action-DeleteSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetSession  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:GetSession](#list_lex-v2-action-GetSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutSession  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:PutSession](#list_lex-v2-action-PutSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecognizeText  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:RecognizeText](#list_lex-v2-action-RecognizeText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecognizeUtterance  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:RecognizeUtterance](#list_lex-v2-action-RecognizeUtterance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartConversation  **
  - **SDK client:** lexv2-runtime
  - **IAM action:**  [lex:StartConversation](#list_lex-v2-action-StartConversation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Lex V2
<a name="list_lex-v2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateCustomVocabularyItem](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BatchCreateCustomVocabularyItem.html)  **
  - **Description:** Grants permission to create new items in an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteCustomVocabularyItem](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BatchDeleteCustomVocabularyItem.html)  **
  - **Description:** Grants permission to delete existing items in an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateCustomVocabularyItem](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BatchUpdateCustomVocabularyItem.html)  **
  - **Description:** Grants permission to update existing items in an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BuildBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BuildBotLocale.html)  **
  - **Description:** Grants permission to build an existing bot locale in a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html)  **
  - **Description:** Grants permission to create a new bot and a test bot alias pointing to the DRAFT bot version
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotAlias.html)  **
  - **Description:** Grants permission to create a new bot alias in a bot
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotLocale.html)  **
  - **Description:** Grants permission to create a new bot locale in an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBotReplica](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotReplica.html)  **
  - **Description:** Grants permission to create bot replica for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBotVersion](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBotVersion.html)  **
  - **Description:** Grants permission to create a new version of an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateExport.html)  **
  - **Description:** Grants permission to create an export for an existing resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html)  **
  - **Description:** Grants permission to create a new intent in an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateResourcePolicy.html)  **
  - **Description:** Grants permission to create a new resource policy for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateResourcePolicyStatement](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateResourcePolicyStatement.html)  **
  - **Description:** Grants permission to create a new resource policy statement for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlot.html)  **
  - **Description:** Grants permission to create a new slot in an intent
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateSlotType.html)  **
  - **Description:** Grants permission to create a new slot type in an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTestSetDiscrepancyReport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateTestSetDiscrepancyReport.html)  **
  - **Description:** Grants permission to create a test set discrepancy report
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUploadUrl](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html)  **
  - **Description:** Grants permission to create an upload url for import file
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html)  **
  - **Description:** Grants permission to delete an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotAlias.html)  **
  - **Description:** Grants permission to delete an existing bot alias in a bot
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotAnalyzerRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotAnalyzerRecommendation.html)  **
  - **Description:** Grants permission to delete a bot analyzer recommendation
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotLocale.html)  **
  - **Description:** Grants permission to delete an existing bot locale in a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotReplica](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotReplica.html)  **
  - **Description:** Grants permission to delete an existing bot replica
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBotVersion](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBotVersion.html)  **
  - **Description:** Grants permission to delete an existing bot version
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteCustomVocabulary.html)  **
  - **Description:** Grants permission to delete an existing custom vocabulary in a bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteExport.html)  **
  - **Description:** Grants permission to delete an existing export
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteImport.html)  **
  - **Description:** Grants permission to delete an existing import
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteIntent.html)  **
  - **Description:** Grants permission to delete an existing intent in a bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete an existing resource policy for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicyStatement](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteResourcePolicyStatement.html)  **
  - **Description:** Grants permission to delete an existing resource policy statement for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSession](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DeleteSession.html)  **
  - **Description:** Grants permission to delete session information for a bot alias and user ID
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteSlot.html)  **
  - **Description:** Grants permission to delete an existing slot in an intent
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteSlotType.html)  **
  - **Description:** Grants permission to delete an existing slot type in a bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTestSet](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteTestSet.html)  **
  - **Description:** Grants permission to delete an existing test set
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUtterances](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteUtterances.html)  **
  - **Description:** Grants permission to delete utterance data for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBot.html)  **
  - **Description:** Grants permission to retrieve an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotAlias.html)  **
  - **Description:** Grants permission to retrieve an existing bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotAnalyzerRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotAnalyzerRecommendation.html)  **
  - **Description:** Grants permission to describe a bot analyzer recommendation
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotLocale.html)  **
  - **Description:** Grants permission to retrieve an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotRecommendation.html)  **
  - **Description:** Grants permission to retrieve metadata information about a bot recommendation
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotReplica](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotReplica.html)  **
  - **Description:** Grants permission to retrieve an existing bot replica
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotResourceGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotResourceGeneration.html)  **
  - **Description:** Grants permission to retrieve metadata information for a bot resource generation
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeBotVersion](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBotVersion.html)  **
  - **Description:** Grants permission to retrieve an existing bot version
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomVocabularyMetadata](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeCustomVocabularyMetadata.html)  **
  - **Description:** Grants permission to retrieve metadata of an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html)  **
  - **Description:** Grants permission to retrieve an existing export
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeImport.html)  **
  - **Description:** Grants permission to retrieve an existing import
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeIntent.html)  **
  - **Description:** Grants permission to retrieve an existing intent
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve an existing resource policy for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeSlot.html)  **
  - **Description:** Grants permission to retrieve an existing slot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeSlotType.html)  **
  - **Description:** Grants permission to retrieve an existing slot type
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTestExecution](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestExecution.html)  **
  - **Description:** Grants permission to retrieve test execution metadata
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTestSet](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSet.html)  **
  - **Description:** Grants permission to retrieve an existing test set
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTestSetDiscrepancyReport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSetDiscrepancyReport.html)  **
  - **Description:** Grants permission to retrieve test set discrepancy report metadata
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTestSetGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSetGeneration.html)  **
  - **Description:** Grants permission to retrieve test set generation metadata
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GenerateBotElement](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GenerateBotElement.html)  **
  - **Description:** Grants permission to generate supported fields or elements for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_GetSession.html)  **
  - **Description:** Grants permission to retrieve session information for a bot alias and user ID
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTestExecutionArtifactsUrl](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_GetTestExecutionArtifactsUrl.html)  **
  - **Description:** Grants permission to retrieve artifacts URL for a test execution
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAggregatedUtterances](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html)  **
  - **Description:** Grants permission to list utterances and statistics for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotAliasReplicas](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotAliasReplicas.html)  **
  - **Description:** Grants permission to list alias replicas in a bot replica
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotAliases](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotAliases.html)  **
  - **Description:** Grants permission to list bot aliases in an bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotAnalyzerRecommendations](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotAnalyzerRecommendations.html)  **
  - **Description:** Grants permission to list bot analyzer recommendations
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotLocales](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotLocales.html)  **
  - **Description:** Grants permission to list bot locales in a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotRecommendations](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotRecommendations.html)  **
  - **Description:** Grants permission to get a list of bot recommendations that meet the specified criteria
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotReplicas](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotReplicas.html)  **
  - **Description:** Grants permission to list replicas of a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotResourceGenerations](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotResourceGenerations.html)  **
  - **Description:** Grants permission to list the resource generations for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotVersionReplicas](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotVersionReplicas.html)  **
  - **Description:** Grants permission to list version replicas in a bot replica
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBotVersions](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBotVersions.html)  **
  - **Description:** Grants permission to list existing bot versions
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBots](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBots.html)  **
  - **Description:** Grants permission to list existing bots
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBuiltInIntents](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBuiltInIntents.html)  **
  - **Description:** Grants permission to list built-in intents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBuiltInSlotTypes](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBuiltInSlotTypes.html)  **
  - **Description:** Grants permission to list built-in slot types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomVocabularyItems](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListCustomVocabularyItems.html)  **
  - **Description:** Grants permission to list items of an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListExports.html)  **
  - **Description:** Grants permission to list existing exports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html)  **
  - **Description:** Grants permission to list existing imports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIntentMetrics](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListIntentMetrics.html)  **
  - **Description:** Grants permission to list intent analytics metrics for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntentPaths](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListIntentPaths.html)  **
  - **Description:** Grants permission to list intent path analytics for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntentStageMetrics](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListIntentStageMetrics.html)  **
  - **Description:** Grants permission to list intentStage analytics metrics for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListIntents](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListIntents.html)  **
  - **Description:** Grants permission to list intents in a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommendedIntents](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListRecommendedIntents.html)  **
  - **Description:** Grants permission to get a list of recommended intents provided by the bot recommendation
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSessionAnalyticsData](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListSessionAnalyticsData.html)  **
  - **Description:** Grants permission to list session analytics data for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSessionMetrics](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListSessionMetrics.html)  **
  - **Description:** Grants permission to list session analytics metrics for a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSlotTypes](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListSlotTypes.html)  **
  - **Description:** Grants permission to list slot types in a bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSlots](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListSlots.html)  **
  - **Description:** Grants permission to list slots in an intent
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tags for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestExecutionResultItems](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestExecutionResultItems.html)  **
  - **Description:** Grants permission to retrieve test results data for a test execution
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestExecutions](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestExecutions.html)  **
  - **Description:** Grants permission to list test executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTestSetRecords](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestSetRecords.html)  **
  - **Description:** Grants permission to retrieve records inside an existing test set
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTestSets](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListTestSets.html)  **
  - **Description:** Grants permission to list test sets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutSession](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_PutSession.html)  **
  - **Description:** Grants permission to create a new session or modify an existing session for a bot alias and user ID
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html)  **
  - **Description:** Grants permission to send user input (text-only) to an bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html)  **
  - **Description:** Grants permission to send user input (text or speech) to an bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchAssociatedTranscripts](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SearchAssociatedTranscripts.html)  **
  - **Description:** Grants permission to search for associated transcripts that meet the specified criteria
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartBotAnalyzer](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotAnalyzer.html)  **
  - **Description:** Grants permission to start a bot analyzer for an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBotRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotRecommendation.html)  **
  - **Description:** Grants permission to start a bot recommendation for an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBotResourceGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartBotResourceGeneration.html)  **
  - **Description:** Grants permission to start a resource generation for an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartConversation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_StartConversation.html)  **
  - **Description:** Grants permission to stream user input (speech/text/DTMF) to a bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartImport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartImport.html)  **
  - **Description:** Grants permission to start a new import with the uploaded import file
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Access level:** Write

- **   [StartTestExecution](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartTestExecution.html)  **
  - **Description:** Grants permission to start a test execution using a test set
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTestSetGeneration](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartTestSetGeneration.html)  **
  - **Description:** Grants permission to generate a test set
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBotAnalyzer](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StopBotAnalyzer.html)  **
  - **Description:** Grants permission to stop a bot analyzer for an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBotRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StopBotRecommendation.html)  **
  - **Description:** Grants permission to stop a bot recommendation for an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite tags of a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Resource types (\*required):** [test set](#list_lex-v2-resource-testset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lex-v2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lex-v2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBot.html)  **
  - **Description:** Grants permission to update an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html)  **
  - **Description:** Grants permission to update an existing bot alias
  - **Resource types (\*required):** [bot alias\*](#list_lex-v2-resource-botalias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBotLocale](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotLocale.html)  **
  - **Description:** Grants permission to update an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBotRecommendation](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotRecommendation.html)  **
  - **Description:** Grants permission to update an existing bot recommendation request
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExport](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateExport.html)  **
  - **Description:** Grants permission to update an existing export
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntent](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateIntent.html)  **
  - **Description:** Grants permission to update an existing intent
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResourcePolicy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateResourcePolicy.html)  **
  - **Description:** Grants permission to update an existing resource policy for a Lex resource
  - **Resource types (\*required):** [bot](#list_lex-v2-resource-bot) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [bot alias](#list_lex-v2-resource-botalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSlot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlot.html)  **
  - **Description:** Grants permission to update an existing slot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSlotType](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateSlotType.html)  **
  - **Description:** Grants permission to update an existing slot type
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTestSet](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateTestSet.html)  **
  - **Description:** Grants permission to update an existing test set
  - **Resource types (\*required):** [test set\*](#list_lex-v2-resource-testset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Lex V2
<a name="list_lex-v2-permission-only-actions"></a>

The following actions are defined by Amazon Lex V2 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CreateBotChannel](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)  **
  - **Description:** Grants permission to create a bot channel in an existing bot
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html)  **
  - **Description:** Grants permission to create a new custom vocabulary in an existing bot locale
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTestSet](https://docs.aws.amazon.com/lexv2/latest/dg/create-test-set-from-CSV.html)  **
  - **Description:** Grants permission to import a new test-set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBotChannel](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)  **
  - **Description:** Grants permission to delete an existing bot channel
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBotChannel](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)  **
  - **Description:** Grants permission to retrieve an existing bot channel
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html)  **
  - **Description:** Grants permission to retrieve an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBotChannels](https://docs.aws.amazon.com/lexv2/latest/dg/deploying-messaging-platform.html)  **
  - **Description:** Grants permission to list bot channels
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [UpdateCustomVocabulary](https://docs.aws.amazon.com/lexv2/latest/dg/vocab.html)  **
  - **Description:** Grants permission to update an existing custom vocabulary
  - **Resource types (\*required):** [bot\*](#list_lex-v2-resource-bot)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Lex V2
<a name="list_lex-v2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bot](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html)  | arn:${Partition}:lex:${Region}:${Account}:bot/${BotId}, arn:${Partition}:lex:${Region}:${Account}:bot:${BotName} | [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_) | 
|  [bot alias](https://docs.aws.amazon.com/lexv2/latest/dg/how-it-works.html)  | arn:${Partition}:lex:${Region}:${Account}:bot-alias/${BotId}/${BotAliasId}, arn:${Partition}:lex:${Region}:${Account}:bot:${BotName}:${BotAlias} | [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_) | 
|  [test set](https://docs.aws.amazon.com/lexv2/latest/dg/test-workbench.html)  | arn:${Partition}:lex:${Region}:${Account}:test-set/${TestSetId} | [aws:ResourceTag/${TagKey}](#list_lex-v2-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Lex V2
<a name="list_lex-v2-policy-keys"></a>

Amazon Lex V2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags attached to a Lex resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the set of tag keys in the request | ArrayOfString | 