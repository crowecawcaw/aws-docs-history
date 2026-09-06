

# Actions, resources, and condition keys for Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore"></a>

Amazon Bedrock Agentcore (service prefix: `bedrock-agentcore`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/bedrock-agentcore/bedrock-agentcore.json) for this service.

**Topics**
+ [API operations defined by Amazon Bedrock Agentcore](#list_bedrock-agentcore-operations)
+ [Actions defined by Amazon Bedrock Agentcore](#list_bedrock-agentcore-actions-as-permissions)
+ [Permission-only actions for Amazon Bedrock Agentcore](#list_bedrock-agentcore-permission-only-actions)
+ [Resource types defined by Amazon Bedrock Agentcore](#list_bedrock-agentcore-resources-for-iam-policies)
+ [Condition keys for Amazon Bedrock Agentcore](#list_bedrock-agentcore-policy-keys)

## API operations defined by Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_bedrock-agentcore-actions-as-permissions).




- **   BatchCreateMemoryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:BatchCreateMemoryRecords](#list_bedrock-agentcore-action-BatchCreateMemoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteMemoryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:BatchDeleteMemoryRecords](#list_bedrock-agentcore-action-BatchDeleteMemoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchUpdateMemoryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:BatchUpdateMemoryRecords](#list_bedrock-agentcore-action-BatchUpdateMemoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteResourceTokenAuth  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:CompleteResourceTokenAuth](#list_bedrock-agentcore-action-CompleteResourceTokenAuth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateABTest  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:CreateABTest](#list_bedrock-agentcore-action-CreateABTest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateEvent  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:CreateEvent](#list_bedrock-agentcore-action-CreateEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePaymentInstrument  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:CreatePaymentInstrument](#list_bedrock-agentcore-action-CreatePaymentInstrument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePaymentSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:CreatePaymentSession](#list_bedrock-agentcore-action-CreatePaymentSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteABTest  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteABTest](#list_bedrock-agentcore-action-DeleteABTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBatchEvaluation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteBatchEvaluation](#list_bedrock-agentcore-action-DeleteBatchEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCapacityProviderSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteCapacityProviderSession](#list_bedrock-agentcore-action-DeleteCapacityProviderSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEvent  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteEvent](#list_bedrock-agentcore-action-DeleteEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMemoryRecord  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteMemoryRecord](#list_bedrock-agentcore-action-DeleteMemoryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePaymentInstrument  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeletePaymentInstrument](#list_bedrock-agentcore-action-DeletePaymentInstrument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePaymentSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeletePaymentSession](#list_bedrock-agentcore-action-DeletePaymentSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRecommendation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:DeleteRecommendation](#list_bedrock-agentcore-action-DeleteRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Evaluate  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:Evaluate](#list_bedrock-agentcore-action-Evaluate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetABTest  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetABTest](#list_bedrock-agentcore-action-GetABTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentCard  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetAgentCard](#list_bedrock-agentcore-action-GetAgentCard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBatchEvaluation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetBatchEvaluation](#list_bedrock-agentcore-action-GetBatchEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBrowserSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetBrowserSession](#list_bedrock-agentcore-action-GetBrowserSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeInterpreterSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetCodeInterpreterSession](#list_bedrock-agentcore-action-GetCodeInterpreterSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvent  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetEvent](#list_bedrock-agentcore-action-GetEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMemoryRecord  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetMemoryRecord](#list_bedrock-agentcore-action-GetMemoryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentInstrument  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetPaymentInstrument](#list_bedrock-agentcore-action-GetPaymentInstrument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentInstrumentBalance  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetPaymentInstrumentBalance](#list_bedrock-agentcore-action-GetPaymentInstrumentBalance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetPaymentSession](#list_bedrock-agentcore-action-GetPaymentSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetRecommendation](#list_bedrock-agentcore-action-GetRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceApiKey  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetResourceApiKey](#list_bedrock-agentcore-action-GetResourceApiKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceOauth2Token  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetResourceOauth2Token](#list_bedrock-agentcore-action-GetResourceOauth2Token) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePaymentToken  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetResourcePaymentToken](#list_bedrock-agentcore-action-GetResourcePaymentToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkloadAccessToken  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetWorkloadAccessToken](#list_bedrock-agentcore-action-GetWorkloadAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWorkloadAccessTokenForJWT  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetWorkloadAccessTokenForJWT](#list_bedrock-agentcore-action-GetWorkloadAccessTokenForJWT) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWorkloadAccessTokenForUserId  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:GetWorkloadAccessTokenForUserId](#list_bedrock-agentcore-action-GetWorkloadAccessTokenForUserId) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeAgentRuntime  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:InvokeAgentRuntime](#list_bedrock-agentcore-action-InvokeAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:InvokeAgentRuntimeForUser](#list_bedrock-agentcore-action-InvokeAgentRuntimeForUser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   InvokeAgentRuntimeCommand  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:InvokeAgentRuntimeCommand](#list_bedrock-agentcore-action-InvokeAgentRuntimeCommand) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeCodeInterpreter  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:InvokeCodeInterpreter](#list_bedrock-agentcore-action-InvokeCodeInterpreter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:StartCodeInterpreterSession](#list_bedrock-agentcore-action-StartCodeInterpreterSession)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   InvokeHarness  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:InvokeAgentRuntime](#list_bedrock-agentcore-action-InvokeAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:InvokeHarness](#list_bedrock-agentcore-action-InvokeHarness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListABTests  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListABTests](#list_bedrock-agentcore-action-ListABTests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListActors  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListActors](#list_bedrock-agentcore-action-ListActors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBatchEvaluations  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListBatchEvaluations](#list_bedrock-agentcore-action-ListBatchEvaluations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBrowserSessions  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListBrowserSessions](#list_bedrock-agentcore-action-ListBrowserSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeInterpreterSessions  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListCodeInterpreterSessions](#list_bedrock-agentcore-action-ListCodeInterpreterSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEvents  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListEvents](#list_bedrock-agentcore-action-ListEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemoryExtractionJobs  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListMemoryExtractionJobs](#list_bedrock-agentcore-action-ListMemoryExtractionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemoryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListMemoryRecords](#list_bedrock-agentcore-action-ListMemoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPaymentInstruments  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListPaymentInstruments](#list_bedrock-agentcore-action-ListPaymentInstruments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPaymentSessions  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListPaymentSessions](#list_bedrock-agentcore-action-ListPaymentSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendations  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListRecommendations](#list_bedrock-agentcore-action-ListRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSessions  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ListSessions](#list_bedrock-agentcore-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ProcessPayment  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:ProcessPayment](#list_bedrock-agentcore-action-ProcessPayment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetrieveMemoryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:RetrieveMemoryRecords](#list_bedrock-agentcore-action-RetrieveMemoryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SaveBrowserSessionProfile  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:SaveBrowserSessionProfile](#list_bedrock-agentcore-action-SaveBrowserSessionProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchRegistryRecords  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:SearchRegistryRecords](#list_bedrock-agentcore-action-SearchRegistryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartBatchEvaluation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StartBatchEvaluation](#list_bedrock-agentcore-action-StartBatchEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartBrowserSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StartBrowserSession](#list_bedrock-agentcore-action-StartBrowserSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCodeInterpreterSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StartCodeInterpreterSession](#list_bedrock-agentcore-action-StartCodeInterpreterSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMemoryExtractionJob  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StartMemoryExtractionJob](#list_bedrock-agentcore-action-StartMemoryExtractionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRecommendation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StartRecommendation](#list_bedrock-agentcore-action-StartRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBatchEvaluation  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StopBatchEvaluation](#list_bedrock-agentcore-action-StopBatchEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopBrowserSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StopBrowserSession](#list_bedrock-agentcore-action-StopBrowserSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCodeInterpreterSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StopCodeInterpreterSession](#list_bedrock-agentcore-action-StopCodeInterpreterSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRuntimeSession  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:StopRuntimeSession](#list_bedrock-agentcore-action-StopRuntimeSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateABTest  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:UpdateABTest](#list_bedrock-agentcore-action-UpdateABTest)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateBrowserStream  **
  - **SDK client:** bedrock-agentcore
  - **IAM action:**  [bedrock-agentcore:UpdateBrowserStream](#list_bedrock-agentcore-action-UpdateBrowserStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddDatasetExamples  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:AddDatasetExamples](#list_bedrock-agentcore-action-AddDatasetExamples) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchPutGatewayRateLimits  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:BatchPutGatewayRateLimits](#list_bedrock-agentcore-action-BatchPutGatewayRateLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgentRuntime  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateAgentRuntime](#list_bedrock-agentcore-action-CreateAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:CreateAgentRuntimeEndpoint](#list_bedrock-agentcore-action-CreateAgentRuntimeEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:PassCapacityProvider](#list_bedrock-agentcore-action-PassCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateAgentRuntimeEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateAgentRuntimeEndpoint](#list_bedrock-agentcore-action-CreateAgentRuntimeEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateApiKeyCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateApiKeyCredentialProvider](#list_bedrock-agentcore-action-CreateApiKeyCredentialProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateBrowser  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateBrowser](#list_bedrock-agentcore-action-CreateBrowser)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateBrowserProfile  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateBrowserProfile](#list_bedrock-agentcore-action-CreateBrowserProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCapacityProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateCapacityProvider](#list_bedrock-agentcore-action-CreateCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com, ec2.amazonaws.com / **Access level:** Write

- **   CreateCodeInterpreter  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateCodeInterpreter](#list_bedrock-agentcore-action-CreateCodeInterpreter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateConfigurationBundle  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateConfigurationBundle](#list_bedrock-agentcore-action-CreateConfigurationBundle)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConsentPortal  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateDataset  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateDataset](#list_bedrock-agentcore-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDatasetVersion  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateDatasetVersion](#list_bedrock-agentcore-action-CreateDatasetVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEvaluator  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateEvaluator](#list_bedrock-agentcore-action-CreateEvaluator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGateway  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateGateway](#list_bedrock-agentcore-action-CreateGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:SynchronizeGatewayTargets](#list_bedrock-agentcore-action-SynchronizeGatewayTargets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateGatewayRateLimit  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateGatewayRateLimit](#list_bedrock-agentcore-action-CreateGatewayRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGatewayRule  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateGatewayRule](#list_bedrock-agentcore-action-CreateGatewayRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGatewayTarget  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateGatewayTarget](#list_bedrock-agentcore-action-CreateGatewayTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:SynchronizeGatewayTargets](#list_bedrock-agentcore-action-SynchronizeGatewayTargets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   CreateHarness  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateAgentRuntime](#list_bedrock-agentcore-action-CreateAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:CreateHarness](#list_bedrock-agentcore-action-CreateHarness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:CreateMemory](#list_bedrock-agentcore-action-CreateMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:GetMemory](#list_bedrock-agentcore-action-GetMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateHarnessEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateHarnessEndpoint](#list_bedrock-agentcore-action-CreateHarnessEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMemory  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateMemory](#list_bedrock-agentcore-action-CreateMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateOauth2CredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateOauth2CredentialProvider](#list_bedrock-agentcore-action-CreateOauth2CredentialProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateOnlineEvaluationConfig  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateOnlineEvaluationConfig](#list_bedrock-agentcore-action-CreateOnlineEvaluationConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreatePaymentConnector  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreatePaymentConnector](#list_bedrock-agentcore-action-CreatePaymentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePaymentCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreatePaymentCredentialProvider](#list_bedrock-agentcore-action-CreatePaymentCredentialProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePaymentManager  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreatePaymentManager](#list_bedrock-agentcore-action-CreatePaymentManager)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreatePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreatePolicy](#list_bedrock-agentcore-action-CreatePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePolicyEngine  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreatePolicyEngine](#list_bedrock-agentcore-action-CreatePolicyEngine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRegistry  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateRegistry](#list_bedrock-agentcore-action-CreateRegistry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistryRecord  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateRegistryRecord](#list_bedrock-agentcore-action-CreateRegistryRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   CreateWorkloadIdentity  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:CreateWorkloadIdentity](#list_bedrock-agentcore-action-CreateWorkloadIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAgentRuntime  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteAgentRuntime](#list_bedrock-agentcore-action-DeleteAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:DeleteAgentRuntimeEndpoint](#list_bedrock-agentcore-action-DeleteAgentRuntimeEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:DeleteWorkloadIdentity](#list_bedrock-agentcore-action-DeleteWorkloadIdentity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAgentRuntimeEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteAgentRuntimeEndpoint](#list_bedrock-agentcore-action-DeleteAgentRuntimeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApiKeyCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteApiKeyCredentialProvider](#list_bedrock-agentcore-action-DeleteApiKeyCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBrowser  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteBrowser](#list_bedrock-agentcore-action-DeleteBrowser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBrowserProfile  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteBrowserProfile](#list_bedrock-agentcore-action-DeleteBrowserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCapacityProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteCapacityProvider](#list_bedrock-agentcore-action-DeleteCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCodeInterpreter  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteCodeInterpreter](#list_bedrock-agentcore-action-DeleteCodeInterpreter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationBundle  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteConfigurationBundle](#list_bedrock-agentcore-action-DeleteConfigurationBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteDataset](#list_bedrock-agentcore-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDatasetExamples  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteDatasetExamples](#list_bedrock-agentcore-action-DeleteDatasetExamples) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEvaluator  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteEvaluator](#list_bedrock-agentcore-action-DeleteEvaluator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGateway  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteGateway](#list_bedrock-agentcore-action-DeleteGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGatewayRateLimit  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteGatewayRateLimit](#list_bedrock-agentcore-action-DeleteGatewayRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGatewayRule  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteGatewayRule](#list_bedrock-agentcore-action-DeleteGatewayRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGatewayTarget  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteGatewayTarget](#list_bedrock-agentcore-action-DeleteGatewayTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHarness  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteAgentRuntime](#list_bedrock-agentcore-action-DeleteAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:DeleteHarness](#list_bedrock-agentcore-action-DeleteHarness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteHarnessEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteHarnessEndpoint](#list_bedrock-agentcore-action-DeleteHarnessEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMemory  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteMemory](#list_bedrock-agentcore-action-DeleteMemory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOauth2CredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteOauth2CredentialProvider](#list_bedrock-agentcore-action-DeleteOauth2CredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOnlineEvaluationConfig  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteOnlineEvaluationConfig](#list_bedrock-agentcore-action-DeleteOnlineEvaluationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePaymentConnector  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeletePaymentConnector](#list_bedrock-agentcore-action-DeletePaymentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePaymentCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeletePaymentCredentialProvider](#list_bedrock-agentcore-action-DeletePaymentCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePaymentManager  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeletePaymentManager](#list_bedrock-agentcore-action-DeletePaymentManager) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeletePolicy](#list_bedrock-agentcore-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicyEngine  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeletePolicyEngine](#list_bedrock-agentcore-action-DeletePolicyEngine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistry  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteRegistry](#list_bedrock-agentcore-action-DeleteRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistryRecord  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteRegistryRecord](#list_bedrock-agentcore-action-DeleteRegistryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteResourcePolicy](#list_bedrock-agentcore-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkloadIdentity  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:DeleteWorkloadIdentity](#list_bedrock-agentcore-action-DeleteWorkloadIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAgentRuntime  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetAgentRuntime](#list_bedrock-agentcore-action-GetAgentRuntime) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAgentRuntimeEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetAgentRuntimeEndpoint](#list_bedrock-agentcore-action-GetAgentRuntimeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApiKeyCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetApiKeyCredentialProvider](#list_bedrock-agentcore-action-GetApiKeyCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBrowser  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetBrowser](#list_bedrock-agentcore-action-GetBrowser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBrowserProfile  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetBrowserProfile](#list_bedrock-agentcore-action-GetBrowserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCapacityProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetCapacityProvider](#list_bedrock-agentcore-action-GetCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeInterpreter  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetCodeInterpreter](#list_bedrock-agentcore-action-GetCodeInterpreter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationBundle  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetConfigurationBundle](#list_bedrock-agentcore-action-GetConfigurationBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationBundleVersion  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetConfigurationBundleVersion](#list_bedrock-agentcore-action-GetConfigurationBundleVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataset  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetDataset](#list_bedrock-agentcore-action-GetDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvaluator  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetEvaluator](#list_bedrock-agentcore-action-GetEvaluator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGateway  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetGateway](#list_bedrock-agentcore-action-GetGateway) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGatewayRateLimit  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetGatewayRateLimit](#list_bedrock-agentcore-action-GetGatewayRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGatewayRule  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetGatewayRule](#list_bedrock-agentcore-action-GetGatewayRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGatewayTarget  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetGatewayTarget](#list_bedrock-agentcore-action-GetGatewayTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHarness  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetHarness](#list_bedrock-agentcore-action-GetHarness) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHarnessEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetHarnessEndpoint](#list_bedrock-agentcore-action-GetHarnessEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMemory  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetMemory](#list_bedrock-agentcore-action-GetMemory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOauth2CredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetOauth2CredentialProvider](#list_bedrock-agentcore-action-GetOauth2CredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOnlineEvaluationConfig  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetOnlineEvaluationConfig](#list_bedrock-agentcore-action-GetOnlineEvaluationConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentConnector  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPaymentConnector](#list_bedrock-agentcore-action-GetPaymentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPaymentCredentialProvider](#list_bedrock-agentcore-action-GetPaymentCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPaymentManager  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPaymentManager](#list_bedrock-agentcore-action-GetPaymentManager) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicy](#list_bedrock-agentcore-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyEngine  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicyEngine](#list_bedrock-agentcore-action-GetPolicyEngine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyEngineSummary  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicyEngineSummary](#list_bedrock-agentcore-action-GetPolicyEngineSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyGeneration  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicyGeneration](#list_bedrock-agentcore-action-GetPolicyGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicyGenerationSummary  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicyGenerationSummary](#list_bedrock-agentcore-action-GetPolicyGenerationSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicySummary  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetPolicySummary](#list_bedrock-agentcore-action-GetPolicySummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistry  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetRegistry](#list_bedrock-agentcore-action-GetRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegistryRecord  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetRegistryRecord](#list_bedrock-agentcore-action-GetRegistryRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetResourcePolicy](#list_bedrock-agentcore-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTokenVault  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetTokenVault](#list_bedrock-agentcore-action-GetTokenVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkloadIdentity  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetWorkloadIdentity](#list_bedrock-agentcore-action-GetWorkloadIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentRuntimeEndpoints  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListAgentRuntimeEndpoints](#list_bedrock-agentcore-action-ListAgentRuntimeEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentRuntimeVersions  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListAgentRuntimeVersions](#list_bedrock-agentcore-action-ListAgentRuntimeVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentRuntimeVersionsByCapacityProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListAgentRuntimeVersionsByCapacityProvider](#list_bedrock-agentcore-action-ListAgentRuntimeVersionsByCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAgentRuntimes  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListAgentRuntimes](#list_bedrock-agentcore-action-ListAgentRuntimes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApiKeyCredentialProviders  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListApiKeyCredentialProviders](#list_bedrock-agentcore-action-ListApiKeyCredentialProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBrowserProfiles  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListBrowserProfiles](#list_bedrock-agentcore-action-ListBrowserProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBrowsers  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListBrowsers](#list_bedrock-agentcore-action-ListBrowsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCapacityProviders  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListCapacityProviders](#list_bedrock-agentcore-action-ListCapacityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeInterpreters  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListCodeInterpreters](#list_bedrock-agentcore-action-ListCodeInterpreters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationBundleVersions  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListConfigurationBundleVersions](#list_bedrock-agentcore-action-ListConfigurationBundleVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationBundles  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListConfigurationBundles](#list_bedrock-agentcore-action-ListConfigurationBundles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetExamples  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListDatasetExamples](#list_bedrock-agentcore-action-ListDatasetExamples) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasetVersions  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListDatasetVersions](#list_bedrock-agentcore-action-ListDatasetVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasets  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListDatasets](#list_bedrock-agentcore-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEvaluators  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListEvaluators](#list_bedrock-agentcore-action-ListEvaluators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGatewayRateLimits  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListGatewayRateLimits](#list_bedrock-agentcore-action-ListGatewayRateLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGatewayRules  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListGatewayRules](#list_bedrock-agentcore-action-ListGatewayRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGatewayTargets  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListGatewayTargets](#list_bedrock-agentcore-action-ListGatewayTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListGateways  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListGateways](#list_bedrock-agentcore-action-ListGateways) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHarnessEndpoints  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListHarnessEndpoints](#list_bedrock-agentcore-action-ListHarnessEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHarnessVersions  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListHarnessVersions](#list_bedrock-agentcore-action-ListHarnessVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHarnesses  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListHarnesses](#list_bedrock-agentcore-action-ListHarnesses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemories  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListMemories](#list_bedrock-agentcore-action-ListMemories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOauth2CredentialProviders  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListOauth2CredentialProviders](#list_bedrock-agentcore-action-ListOauth2CredentialProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListOnlineEvaluationConfigs  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListOnlineEvaluationConfigs](#list_bedrock-agentcore-action-ListOnlineEvaluationConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPaymentConnectors  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPaymentConnectors](#list_bedrock-agentcore-action-ListPaymentConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPaymentCredentialProviders  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPaymentCredentialProviders](#list_bedrock-agentcore-action-ListPaymentCredentialProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPaymentManagers  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPaymentManagers](#list_bedrock-agentcore-action-ListPaymentManagers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicies](#list_bedrock-agentcore-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyEngineSummaries  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicyEngineSummaries](#list_bedrock-agentcore-action-ListPolicyEngineSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyEngines  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicyEngines](#list_bedrock-agentcore-action-ListPolicyEngines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyGenerationAssets  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicyGenerationAssets](#list_bedrock-agentcore-action-ListPolicyGenerationAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyGenerationSummaries  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicyGenerationSummaries](#list_bedrock-agentcore-action-ListPolicyGenerationSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicyGenerations  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicyGenerations](#list_bedrock-agentcore-action-ListPolicyGenerations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicySummaries  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListPolicySummaries](#list_bedrock-agentcore-action-ListPolicySummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegistries  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListRegistries](#list_bedrock-agentcore-action-ListRegistries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegistryRecords  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListRegistryRecords](#list_bedrock-agentcore-action-ListRegistryRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListTagsForResource](#list_bedrock-agentcore-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkloadIdentities  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:ListWorkloadIdentities](#list_bedrock-agentcore-action-ListWorkloadIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:PutResourcePolicy](#list_bedrock-agentcore-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTokenVaultCMK  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:SetTokenVaultCMK](#list_bedrock-agentcore-action-SetTokenVaultCMK) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPolicyGeneration  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:StartPolicyGeneration](#list_bedrock-agentcore-action-StartPolicyGeneration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubmitRegistryRecordForApproval  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:SubmitRegistryRecordForApproval](#list_bedrock-agentcore-action-SubmitRegistryRecordForApproval) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SynchronizeGatewayTargets  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:SynchronizeGatewayTargets](#list_bedrock-agentcore-action-SynchronizeGatewayTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   TagResource  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:TagResource](#list_bedrock-agentcore-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UntagResource](#list_bedrock-agentcore-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgentRuntime  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:PassCapacityProvider](#list_bedrock-agentcore-action-PassCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:UpdateAgentRuntime](#list_bedrock-agentcore-action-UpdateAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateAgentRuntimeEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateAgentRuntimeEndpoint](#list_bedrock-agentcore-action-UpdateAgentRuntimeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApiKeyCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateApiKeyCredentialProvider](#list_bedrock-agentcore-action-UpdateApiKeyCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCapacityProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateCapacityProvider](#list_bedrock-agentcore-action-UpdateCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationBundle  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateConfigurationBundle](#list_bedrock-agentcore-action-UpdateConfigurationBundle) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataset  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateDataset](#list_bedrock-agentcore-action-UpdateDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDatasetExamples  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateDatasetExamples](#list_bedrock-agentcore-action-UpdateDatasetExamples) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEvaluator  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateEvaluator](#list_bedrock-agentcore-action-UpdateEvaluator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGateway  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateGateway](#list_bedrock-agentcore-action-UpdateGateway)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateGatewayRateLimit  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateGatewayRateLimit](#list_bedrock-agentcore-action-UpdateGatewayRateLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewayRule  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateGatewayRule](#list_bedrock-agentcore-action-UpdateGatewayRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGatewayTarget  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:SynchronizeGatewayTargets](#list_bedrock-agentcore-action-SynchronizeGatewayTargets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [bedrock-agentcore:UpdateGatewayTarget](#list_bedrock-agentcore-action-UpdateGatewayTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateHarness  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:GetMemory](#list_bedrock-agentcore-action-GetMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [bedrock-agentcore:UpdateAgentRuntime](#list_bedrock-agentcore-action-UpdateAgentRuntime)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:UpdateHarness](#list_bedrock-agentcore-action-UpdateHarness)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [bedrock-agentcore:UpdateMemory](#list_bedrock-agentcore-action-UpdateMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateHarnessEndpoint  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateHarnessEndpoint](#list_bedrock-agentcore-action-UpdateHarnessEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMemory  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateMemory](#list_bedrock-agentcore-action-UpdateMemory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateOauth2CredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateOauth2CredentialProvider](#list_bedrock-agentcore-action-UpdateOauth2CredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOnlineEvaluationConfig  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateOnlineEvaluationConfig](#list_bedrock-agentcore-action-UpdateOnlineEvaluationConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdatePaymentConnector  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdatePaymentConnector](#list_bedrock-agentcore-action-UpdatePaymentConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePaymentCredentialProvider  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdatePaymentCredentialProvider](#list_bedrock-agentcore-action-UpdatePaymentCredentialProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePaymentManager  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdatePaymentManager](#list_bedrock-agentcore-action-UpdatePaymentManager)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdatePolicy  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdatePolicy](#list_bedrock-agentcore-action-UpdatePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePolicyEngine  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdatePolicyEngine](#list_bedrock-agentcore-action-UpdatePolicyEngine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegistry  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateRegistry](#list_bedrock-agentcore-action-UpdateRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegistryRecord  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateRegistryRecord](#list_bedrock-agentcore-action-UpdateRegistryRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** bedrock-agentcore.amazonaws.com / **Access level:** Write

- **   UpdateRegistryRecordStatus  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateRegistryRecordStatus](#list_bedrock-agentcore-action-UpdateRegistryRecordStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkloadIdentity  **
  - **SDK client:** bedrock-agentcore-control
  - **IAM action:**  [bedrock-agentcore:UpdateWorkloadIdentity](#list_bedrock-agentcore-action-UpdateWorkloadIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddDatasetExamples](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_AddDatasetExamples.html)  **
  - **Description:** Grants permission to add examples to a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchCreateMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchCreateMemoryRecords.html)  **
  - **Description:** Grants permission to create one or more memory records
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:namespace](#list_bedrock-agentcore-bedrock-agentcore_namespace)
  - **Access level:** Write

- **   [BatchDeleteMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchDeleteMemoryRecords.html)  **
  - **Description:** Grants permission to delete one or more memory records
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchPutGatewayRateLimits](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_BatchPutGatewayRateLimits.html)  **
  - **Description:** Grants permission to batch put rate limits on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchUpdateMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_BatchUpdateMemoryRecords.html)  **
  - **Description:** Grants permission to update one or more memory records
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:namespace](#list_bedrock-agentcore-bedrock-agentcore_namespace)
  - **Access level:** Write

- **   [CompleteResourceTokenAuth](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CompleteResourceTokenAuth.html)  **
  - **Description:** Grants permission to retrieve access token with OAuth2 for 3LO flow to access external resource
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Access level:** Read

- **   [ConnectBrowserAutomationStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ConnectBrowserAutomationStream.html)  **
  - **Description:** Grants permission to connect to a browser automation stream
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ConnectBrowserLiveViewStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ConnectBrowserLiveViewStream.html)  **
  - **Description:** Grants permission to connect to a browser live view stream
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateABTest](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateABTest.html)  **
  - **Description:** Grants permission to create an A/B test
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.html)  **
  - **Description:** Grants permission to create a new agent runtime
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)<br />[bedrock-agentcore:RuntimeAuthorizerType](#list_bedrock-agentcore-bedrock-agentcore_RuntimeAuthorizerType)<br />[bedrock-agentcore:securityGroups](#list_bedrock-agentcore-bedrock-agentcore_securityGroups)<br />[bedrock-agentcore:subnets](#list_bedrock-agentcore-bedrock-agentcore_subnets)
  - **Access level:** Write

- **   [CreateAgentRuntimeEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntimeEndpoint.html)  **
  - **Description:** Grants permission to create a new agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApiKeyCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateApiKeyCredentialProvider.html)  **
  - **Description:** Grants permission to create a new API Key Credential Provider
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBrowser](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateBrowser.html)  **
  - **Description:** Grants permission to create a new custom browser
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)<br />[bedrock-agentcore:securityGroups](#list_bedrock-agentcore-bedrock-agentcore_securityGroups)<br />[bedrock-agentcore:subnets](#list_bedrock-agentcore-bedrock-agentcore_subnets)
  - **Access level:** Write

- **   [CreateBrowserProfile](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateBrowserProfile.html)  **
  - **Description:** Grants permission to create a new browser profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateCapacityProvider.html)  **
  - **Description:** Grants permission to create a new capacity provider
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateCodeInterpreter.html)  **
  - **Description:** Grants permission to create a new custom code interpreter
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)<br />[bedrock-agentcore:securityGroups](#list_bedrock-agentcore-bedrock-agentcore_securityGroups)<br />[bedrock-agentcore:subnets](#list_bedrock-agentcore-bedrock-agentcore_subnets)
  - **Access level:** Write

- **   [CreateConfigurationBundle](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateConfigurationBundle.html)  **
  - **Description:** Grants permission to create a new configuration bundle
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a new dataset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDatasetVersion](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateDatasetVersion.html)  **
  - **Description:** Grants permission to create a new version of a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEvaluator](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateEvaluator.html)  **
  - **Description:** Grants permission to create a new evaluator
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html)  **
  - **Description:** Grants permission to create an Event
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)<br />[bedrock-agentcore:sessionId](#list_bedrock-agentcore-bedrock-agentcore_sessionId)
  - **Access level:** Write

- **   [CreateGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGateway.html)  **
  - **Description:** Grants permission to create a new gateway
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGatewayRateLimit](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayRateLimit.html)  **
  - **Description:** Grants permission to create a rate limit on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGatewayRule](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayRule.html)  **
  - **Description:** Grants permission to create a new rule in an existing gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.html)  **
  - **Description:** Grants permission to create a new target in an existing gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateHarness](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateHarness.html)  **
  - **Description:** Grants permission to create a new harness
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHarnessEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateHarnessEndpoint.html)  **
  - **Description:** Grants permission to create a new harness endpoint
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateMemory.html)  **
  - **Description:** Grants permission to create a Memory resource
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)<br />[bedrock-agentcore:KmsKeyArn](#list_bedrock-agentcore-bedrock-agentcore_KmsKeyArn)
  - **Access level:** Write

- **   [CreateOauth2CredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateOauth2CredentialProvider.html)  **
  - **Description:** Grants permission to create a new Credential Provider to access external resources with OAuth2 protocol
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateOnlineEvaluationConfig](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateOnlineEvaluationConfig.html)  **
  - **Description:** Grants permission to create a new online evaluation configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePaymentConnector](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePaymentConnector.html)  **
  - **Description:** Grants permission to create a new payment connector under a payment manager
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePaymentCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePaymentCredentialProvider.html)  **
  - **Description:** Grants permission to create a new Payment Credential Provider
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePaymentInstrument](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePaymentInstrument.html)  **
  - **Description:** Grants permission to create a new payment instrument
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePaymentManager](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePaymentManager.html)  **
  - **Description:** Grants permission to create a new payment manager
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)<br />[bedrock-agentcore:DiscoveryUrl](#list_bedrock-agentcore-bedrock-agentcore_DiscoveryUrl)
  - **Access level:** Write

- **   [CreatePaymentSession](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePaymentSession.html)  **
  - **Description:** Grants permission to create a new payment session
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePolicy.html)  **
  - **Description:** Grants permission to create a new policy within a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreatePolicyEngine.html)  **
  - **Description:** Grants permission to create a new policy engine
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistry](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateRegistry.html)  **
  - **Description:** Grants permission to create a new registry
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRegistryRecord](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateRegistryRecord.html)  **
  - **Description:** Grants permission to create a new registry record
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkloadIdentity](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateWorkloadIdentity.html)  **
  - **Description:** Grants permission to create a new Workload Identity
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteABTest](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteABTest.html)  **
  - **Description:** Grants permission to delete an A/B test
  - **Resource types (\*required):** [ab-test\*](#list_bedrock-agentcore-resource-ab-test)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntime.html)  **
  - **Description:** Grants permission to delete an agent runtime
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentRuntimeEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntimeEndpoint.html)  **
  - **Description:** Grants permission to delete an agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApiKeyCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteApiKeyCredentialProvider.html)  **
  - **Description:** Grants permission to delete a registered API Key Credential Provider
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteBatchEvaluation.html)  **
  - **Description:** Grants permission to delete a batch evaluation
  - **Resource types (\*required):** [batch-evaluate\*](#list_bedrock-agentcore-resource-batch-evaluate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBrowser](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteBrowser.html)  **
  - **Description:** Grants permission to delete a custom browser
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBrowserProfile](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteBrowserProfile.html)  **
  - **Description:** Grants permission to delete a browser profile
  - **Resource types (\*required):** [browser-profile\*](#list_bedrock-agentcore-resource-browser-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteCapacityProvider.html)  **
  - **Description:** Grants permission to delete a capacity provider
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCapacityProviderSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteCapacityProviderSession.html)  **
  - **Description:** Grants permission to delete a capacity provider session
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteCodeInterpreter.html)  **
  - **Description:** Grants permission to delete a custom code interpreter
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigurationBundle](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteConfigurationBundle.html)  **
  - **Description:** Grants permission to delete a configuration bundle
  - **Resource types (\*required):** [configuration-bundle\*](#list_bedrock-agentcore-resource-configuration-bundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDatasetExamples](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteDatasetExamples.html)  **
  - **Description:** Grants permission to delete examples from a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEvaluator](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteEvaluator.html)  **
  - **Description:** Grants permission to delete an evaluator
  - **Resource types (\*required):** [evaluator\*](#list_bedrock-agentcore-resource-evaluator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteEvent.html)  **
  - **Description:** Grants permission to delete an Event
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)<br />[bedrock-agentcore:sessionId](#list_bedrock-agentcore-bedrock-agentcore_sessionId)
  - **Access level:** Write

- **   [DeleteGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteGateway.html)  **
  - **Description:** Grants permission to delete an existing gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGatewayRateLimit](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteGatewayRateLimit.html)  **
  - **Description:** Grants permission to delete a rate limit on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGatewayRule](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteGatewayRule.html)  **
  - **Description:** Grants permission to delete an existing gateway rule
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteGatewayTarget.html)  **
  - **Description:** Grants permission to delete an existing gateway target
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHarness](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteHarness.html)  **
  - **Description:** Grants permission to delete a harness
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHarnessEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteHarnessEndpoint.html)  **
  - **Description:** Grants permission to delete a harness endpoint
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harness-endpoint\*](#list_bedrock-agentcore-resource-harness-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteMemory.html)  **
  - **Description:** Grants permission to delete a Memory resource
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteMemoryRecord.html)  **
  - **Description:** Grants permission to delete a Memory Record
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOauth2CredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteOauth2CredentialProvider.html)  **
  - **Description:** Grants permission to delete a registered OAuth2 Credential Provider
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOnlineEvaluationConfig](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteOnlineEvaluationConfig.html)  **
  - **Description:** Grants permission to delete an online evaluation configuration
  - **Resource types (\*required):** [online-evaluation-config\*](#list_bedrock-agentcore-resource-online-evaluation-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePaymentConnector](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePaymentConnector.html)  **
  - **Description:** Grants permission to delete a payment connector
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePaymentCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePaymentCredentialProvider.html)  **
  - **Description:** Grants permission to delete a registered Payment Credential Provider
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePaymentInstrument](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePaymentInstrument.html)  **
  - **Description:** Grants permission to delete a payment instrument
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePaymentManager](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePaymentManager.html)  **
  - **Description:** Grants permission to delete a payment manager
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePaymentSession](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePaymentSession.html)  **
  - **Description:** Grants permission to delete a payment session
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to delete a policy
  - **Resource types (\*required):** [policy\*](#list_bedrock-agentcore-resource-policy) / **Condition keys:**  
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeletePolicyEngine.html)  **
  - **Description:** Grants permission to delete a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecommendation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteRecommendation.html)  **
  - **Description:** Grants permission to delete a recommendation
  - **Resource types (\*required):** [recommendation\*](#list_bedrock-agentcore-resource-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistry](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteRegistry.html)  **
  - **Description:** Grants permission to delete an existing registry
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRegistryRecord](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteRegistryRecord.html)  **
  - **Description:** Grants permission to delete an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_bedrock-agentcore-resource-registry-record)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete the resource-based policy for a Bedrock resource
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkloadIdentity](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteWorkloadIdentity.html)  **
  - **Description:** Grants permission to delete a registered Workload Identity
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Evaluate](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Evaluate.html)  **
  - **Description:** Grants permission to run an evaluation using an evaluator
  - **Resource types (\*required):** [evaluator\*](#list_bedrock-agentcore-resource-evaluator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetABTest](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetABTest.html)  **
  - **Description:** Grants permission to get details of an A/B test
  - **Resource types (\*required):** [ab-test\*](#list_bedrock-agentcore-resource-ab-test)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentCard](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetAgentCard.html)  **
  - **Description:** Grants permission to retrieve an agent card for A2A
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetAgentRuntime.html)  **
  - **Description:** Grants permission to get details of an agent runtime
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAgentRuntimeEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetAgentRuntimeEndpoint.html)  **
  - **Description:** Grants permission to get details of an agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApiKeyCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetApiKeyCredentialProvider.html)  **
  - **Description:** Grants permission to fetch a registered API Key Credential Provider by its name
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBatchEvaluation.html)  **
  - **Description:** Grants permission to get details of a batch evaluation
  - **Resource types (\*required):** [batch-evaluate\*](#list_bedrock-agentcore-resource-batch-evaluate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBrowser](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetBrowser.html)  **
  - **Description:** Grants permission to get details of a browser
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBrowserProfile](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetBrowserProfile.html)  **
  - **Description:** Grants permission to get details of a browser profile
  - **Resource types (\*required):** [browser-profile\*](#list_bedrock-agentcore-resource-browser-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html)  **
  - **Description:** Grants permission to get details of a browser session
  - **Resource types (\*required):** [browser\*](#list_bedrock-agentcore-resource-browser) / **Condition keys:**  
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetCapacityProvider.html)  **
  - **Description:** Grants permission to get details of a capacity provider
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetCodeInterpreter.html)  **
  - **Description:** Grants permission to get details of a code interpreter
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html)  **
  - **Description:** Grants permission to get details of a code interpreter session
  - **Resource types (\*required):** [code-interpreter\*](#list_bedrock-agentcore-resource-code-interpreter) / **Condition keys:**  
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationBundle](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetConfigurationBundle.html)  **
  - **Description:** Grants permission to get details of a configuration bundle
  - **Resource types (\*required):** [configuration-bundle\*](#list_bedrock-agentcore-resource-configuration-bundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationBundleVersion](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetConfigurationBundleVersion.html)  **
  - **Description:** Grants permission to get a specific version of a configuration bundle
  - **Resource types (\*required):** [configuration-bundle\*](#list_bedrock-agentcore-resource-configuration-bundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataset](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetDataset.html)  **
  - **Description:** Grants permission to get details of a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEvaluator](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetEvaluator.html)  **
  - **Description:** Grants permission to get details of an evaluator
  - **Resource types (\*required):** [evaluator\*](#list_bedrock-agentcore-resource-evaluator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetEvent.html)  **
  - **Description:** Grants permission to fetch an Event
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)<br />[bedrock-agentcore:sessionId](#list_bedrock-agentcore-bedrock-agentcore_sessionId)
  - **Access level:** Read

- **   [GetGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetGateway.html)  **
  - **Description:** Grants permission to retrieve an existing gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGatewayRateLimit](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetGatewayRateLimit.html)  **
  - **Description:** Grants permission to retrieve a rate limit on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGatewayRule](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetGatewayRule.html)  **
  - **Description:** Grants permission to retrieve an existing gateway rule
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetGatewayTarget.html)  **
  - **Description:** Grants permission to retrieve an existing gateway target
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHarness](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetHarness.html)  **
  - **Description:** Grants permission to get details of a harness
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHarnessEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetHarnessEndpoint.html)  **
  - **Description:** Grants permission to get details of a harness endpoint
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harness-endpoint\*](#list_bedrock-agentcore-resource-harness-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetMemory.html)  **
  - **Description:** Grants permission to fetch details for a Memory resource
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetMemoryRecord.html)  **
  - **Description:** Grants permission to fetch a Memory Record
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOauth2CredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetOauth2CredentialProvider.html)  **
  - **Description:** Grants permission to fetch a registered OAuth2 Credential Provider by its name
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOnlineEvaluationConfig](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetOnlineEvaluationConfig.html)  **
  - **Description:** Grants permission to get details of an online evaluation configuration
  - **Resource types (\*required):** [online-evaluation-config\*](#list_bedrock-agentcore-resource-online-evaluation-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentConnector](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentConnector.html)  **
  - **Description:** Grants permission to retrieve details of a payment connector
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentCredentialProvider.html)  **
  - **Description:** Grants permission to fetch a registered Payment Credential Provider by its name
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentInstrument](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentInstrument.html)  **
  - **Description:** Grants permission to retrieve details of a payment instrument
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentInstrumentBalance](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentInstrumentBalance.html)  **
  - **Description:** Grants permission to retrieve the balance of a payment instrument
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentManager](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentManager.html)  **
  - **Description:** Grants permission to retrieve details of a payment manager
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPaymentSession](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPaymentSession.html)  **
  - **Description:** Grants permission to retrieve details of a payment session
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve a policy
  - **Resource types (\*required):** [policy\*](#list_bedrock-agentcore-resource-policy) / **Condition keys:**  
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyEngine.html)  **
  - **Description:** Grants permission to retrieve a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyEngineSummary](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyEngineSummary.html)  **
  - **Description:** Grants permission to retrieve a summary of a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyGeneration.html)  **
  - **Description:** Grants permission to retrieve status and results of a policy generation request
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-generation\*](#list_bedrock-agentcore-resource-policy-generation) / **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicyGenerationSummary](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyGenerationSummary.html)  **
  - **Description:** Grants permission to retrieve a summary of a policy generation request
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-generation\*](#list_bedrock-agentcore-resource-policy-generation) / **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicySummary](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicySummary.html)  **
  - **Description:** Grants permission to retrieve a summary of a policy
  - **Resource types (\*required):** [policy\*](#list_bedrock-agentcore-resource-policy) / **Condition keys:**  
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetRecommendation.html)  **
  - **Description:** Grants permission to get details of a recommendation
  - **Resource types (\*required):** [recommendation\*](#list_bedrock-agentcore-resource-recommendation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegistry](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetRegistry.html)  **
  - **Description:** Grants permission to retrieve an existing registry
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegistryRecord](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetRegistryRecord.html)  **
  - **Description:** Grants permission to retrieve an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_bedrock-agentcore-resource-registry-record)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourceApiKey](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceApiKey.html)  **
  - **Description:** Grants permission to retrieve an API Key associated with an Api Key Credential Provider
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceOauth2Token](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetResourceOauth2Token.html)  **
  - **Description:** Grants permission to retrieve access token with OAuth2 2LO or 3LO flow to access external resource
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePaymentToken](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetResourcePaymentToken.html)  **
  - **Description:** Grants permission to retrieve a payment authentication token associated with a Payment Credential Provider
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to retrieve the resource-based policy for a Bedrock resource
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTokenVault](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetTokenVault.html)  **
  - **Description:** Grants permission to fetch the current configuration of the TokenVault, including encryption settings
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkloadAccessToken](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessToken.html)  **
  - **Description:** Grants permission to retrieve an Workload access token for agentic workloads not acting on behalf of a user
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetWorkloadAccessTokenForJWT](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessTokenForJWT.html)  **
  - **Description:** Grants permission to retrieve an Workload access token for agentic workloads acting on behalf of user with JWT token
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:InboundJwtClaim/aud](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_aud)<br />[bedrock-agentcore:InboundJwtClaim/client\_id](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_client_id)<br />[bedrock-agentcore:InboundJwtClaim/iss](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_iss)<br />[bedrock-agentcore:InboundJwtClaim/scope](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_scope)<br />[bedrock-agentcore:InboundJwtClaim/sub](#list_bedrock-agentcore-bedrock-agentcore_InboundJwtClaim_sub)
  - **Access level:** Write

- **   [GetWorkloadAccessTokenForUserId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetWorkloadAccessTokenForUserId.html)  **
  - **Description:** Grants permission to retrieve an Workload access token for agentic workloads acting on behalf of user with User Id
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:userid](#list_bedrock-agentcore-bedrock-agentcore_userid)
  - **Access level:** Write

- **   [GetWorkloadIdentity](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetWorkloadIdentity.html)  **
  - **Description:** Grants permission to fetch details for a specific Workload identity, including its name and allowed OAuth2 return URLs
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html)  **
  - **Description:** Grants permission to invoke an agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgentRuntimeCommand](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntimeCommand.html)  **
  - **Description:** Grants permission to invoke commands on an agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgentRuntimeCommandShell](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntimeCommandShell.html)  **
  - **Description:** Grants permission to invoke a command shell on an agent runtime endpoint over a web socket stream
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgentRuntimeForUser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html)  **
  - **Description:** Grants permission to invoke an agent runtime endpoint with X-Amzn-Bedrock-AgentCore-Runtime-User-Id header
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgentRuntimeWithWebSocketStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntimeWithWebSocketStream.html)  **
  - **Description:** Grants permission to invoke an agent runtime endpoint with WebSocket stream
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeAgentRuntimeWithWebSocketStreamForUser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntimeWithWebSocketStream.html)  **
  - **Description:** Grants permission to invoke an agent runtime endpoint with WebSocket stream and with X-Amzn-Bedrock-AgentCore-Runtime-User-Id header
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html)  **
  - **Description:** Grants permission to invoke a code interpreter session
  - **Resource types (\*required):** [code-interpreter\*](#list_bedrock-agentcore-resource-code-interpreter) / **Condition keys:**  
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeHarness](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarness.html)  **
  - **Description:** Grants permission to invoke a harness
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harness-endpoint\*](#list_bedrock-agentcore-resource-harness-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeRegistryMcp](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke an MCP operation against an existing registry
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListABTests](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListABTests.html)  **
  - **Description:** Grants permission to list A/B tests
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListActors](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListActors.html)  **
  - **Description:** Grants permission to list Actors
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentRuntimeEndpoints](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListAgentRuntimeEndpoints.html)  **
  - **Description:** Grants permission to list agent runtime endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAgentRuntimeVersions](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListAgentRuntimeVersions.html)  **
  - **Description:** Grants permission to list agent runtime versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAgentRuntimeVersionsByCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListAgentRuntimeVersionsByCapacityProvider.html)  **
  - **Description:** Grants permission to list agent runtime versions by capacity provider
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAgentRuntimes](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListAgentRuntimes.html)  **
  - **Description:** Grants permission to list agent runtimes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApiKeyCredentialProviders](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListApiKeyCredentialProviders.html)  **
  - **Description:** Grants permission to list all API Key Credential Providers in the Token Vault
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBatchEvaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBatchEvaluations.html)  **
  - **Description:** Grants permission to list batch evaluations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBrowserProfiles](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListBrowserProfiles.html)  **
  - **Description:** Grants permission to list browser profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBrowserSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html)  **
  - **Description:** Grants permission to list browser sessions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBrowsers](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListBrowsers.html)  **
  - **Description:** Grants permission to list browsers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCapacityProviders](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListCapacityProviders.html)  **
  - **Description:** Grants permission to list capacity providers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeInterpreterSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html)  **
  - **Description:** Grants permission to list code interpreter sessions
  - **Resource types (\*required):** [code-interpreter\*](#list_bedrock-agentcore-resource-code-interpreter) / **Condition keys:**  
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCodeInterpreters](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListCodeInterpreters.html)  **
  - **Description:** Grants permission to list code interpreters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationBundleVersions](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListConfigurationBundleVersions.html)  **
  - **Description:** Grants permission to list versions of a configuration bundle
  - **Resource types (\*required):** [configuration-bundle\*](#list_bedrock-agentcore-resource-configuration-bundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListConfigurationBundles](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListConfigurationBundles.html)  **
  - **Description:** Grants permission to list configuration bundles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDatasetExamples](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListDatasetExamples.html)  **
  - **Description:** Grants permission to list examples in a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasetVersions](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListDatasetVersions.html)  **
  - **Description:** Grants permission to list versions of a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListDatasets.html)  **
  - **Description:** Grants permission to list datasets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEvaluators](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListEvaluators.html)  **
  - **Description:** Grants permission to list evaluators
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEvents](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListEvents.html)  **
  - **Description:** Grants permission to list events
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)<br />[bedrock-agentcore:sessionId](#list_bedrock-agentcore-bedrock-agentcore_sessionId)
  - **Access level:** List

- **   [ListGatewayRateLimits](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListGatewayRateLimits.html)  **
  - **Description:** Grants permission to list rate limits on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGatewayRules](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListGatewayRules.html)  **
  - **Description:** Grants permission to list existing gateway rules
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGatewayTargets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListGatewayTargets.html)  **
  - **Description:** Grants permission to list existing gateway targets
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGateways](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListGateways.html)  **
  - **Description:** Grants permission to list existing gateways
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHarnessEndpoints](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListHarnessEndpoints.html)  **
  - **Description:** Grants permission to list harness endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHarnessVersions](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListHarnessVersions.html)  **
  - **Description:** Grants permission to list harness versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHarnesses](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListHarnesses.html)  **
  - **Description:** Grants permission to list harnesses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMemories](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListMemories.html)  **
  - **Description:** Grants permission to list memory resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMemoryExtractionJobs](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryExtractionJobs.html)  **
  - **Description:** Grants permission to list extraction jobs for this memory
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html)  **
  - **Description:** Grants permission to list memory records
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:namespace](#list_bedrock-agentcore-bedrock-agentcore_namespace)<br />[bedrock-agentcore:strategyId](#list_bedrock-agentcore-bedrock-agentcore_strategyId)
  - **Access level:** List

- **   [ListOauth2CredentialProviders](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListOauth2CredentialProviders.html)  **
  - **Description:** Grants permission to list all OAuth2 Credential Providers in the Token Vault
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListOnlineEvaluationConfigs](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListOnlineEvaluationConfigs.html)  **
  - **Description:** Grants permission to list online evaluation configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPaymentConnectors](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPaymentConnectors.html)  **
  - **Description:** Grants permission to list payment connectors under a payment manager
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPaymentCredentialProviders](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPaymentCredentialProviders.html)  **
  - **Description:** Grants permission to list all Payment Credential Providers in the Token Vault
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPaymentInstruments](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPaymentInstruments.html)  **
  - **Description:** Grants permission to list payment instruments
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPaymentManagers](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPaymentManagers.html)  **
  - **Description:** Grants permission to list payment managers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPaymentSessions](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPaymentSessions.html)  **
  - **Description:** Grants permission to list payment sessions
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to list policies within a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicyEngineSummaries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngineSummaries.html)  **
  - **Description:** Grants permission to list policy engine summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyEngines](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html)  **
  - **Description:** Grants permission to list policy engines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyGenerationAssets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html)  **
  - **Description:** Grants permission to list generated policy assets from a generation request
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-generation\*](#list_bedrock-agentcore-resource-policy-generation) / **Condition keys:**  
  - **Access level:** List

- **   [ListPolicyGenerationSummaries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html)  **
  - **Description:** Grants permission to list policy generation summaries
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicyGenerations](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerations.html)  **
  - **Description:** Grants permission to list policy generation requests
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPolicySummaries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html)  **
  - **Description:** Grants permission to list policy summaries within a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListRecommendations.html)  **
  - **Description:** Grants permission to list recommendations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegistries](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListRegistries.html)  **
  - **Description:** Grants permission to list existing registries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRegistryRecords](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListRegistryRecords.html)  **
  - **Description:** Grants permission to list existing registry records in a registry
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list sessions
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Bedrock-AgentCore resource
  - **Resource types (\*required):** [apikeycredentialprovider](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [browser-custom](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [browser-profile](#list_bedrock-agentcore-resource-browser-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [capacity-provider](#list_bedrock-agentcore-resource-capacity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [code-interpreter-custom](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [evaluator](#list_bedrock-agentcore-resource-evaluator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harness](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [memory](#list_bedrock-agentcore-resource-memory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [oauth2credentialprovider](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [online-evaluation-config](#list_bedrock-agentcore-resource-online-evaluation-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [payment-manager](#list_bedrock-agentcore-resource-payment-manager) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [paymentcredentialprovider](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-engine](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkloadIdentities](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListWorkloadIdentities.html)  **
  - **Description:** Grants permission to list all Workload Identities in the caller's AWS account
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ProcessPayment](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ProcessPayment.html)  **
  - **Description:** Grants permission to process a payment transaction
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to create or update the resource-based policy for a Bedrock resource
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html)  **
  - **Description:** Grants permission to retrieve memory records through sematic query
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:namespace](#list_bedrock-agentcore-bedrock-agentcore_namespace)<br />[bedrock-agentcore:strategyId](#list_bedrock-agentcore-bedrock-agentcore_strategyId)
  - **Access level:** List

- **   [SaveBrowserSessionProfile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html)  **
  - **Description:** Grants permission to save a browser session profile
  - **Resource types (\*required):** [browser\*](#list_bedrock-agentcore-resource-browser) / **Condition keys:**  
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [browser-profile\*](#list_bedrock-agentcore-resource-browser-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchRegistryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SearchRegistryRecords.html)  **
  - **Description:** Grants permission to search for registry records
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Read

- **   [SetTokenVaultCMK](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SetTokenVaultCMK.html)  **
  - **Description:** Grants permission to associate a Customer Managed Key (CMK) or a Service Managed Key with a specific TokenVault
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBatchEvaluation.html)  **
  - **Description:** Grants permission to start a batch evaluation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html)  **
  - **Description:** Grants permission to start a new browser session
  - **Resource types (\*required):** [browser\*](#list_bedrock-agentcore-resource-browser) / **Condition keys:**  
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [browser-profile](#list_bedrock-agentcore-resource-browser-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html)  **
  - **Description:** Grants permission to start a new code interpreter session
  - **Resource types (\*required):** [code-interpreter\*](#list_bedrock-agentcore-resource-code-interpreter) / **Condition keys:**  
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMemoryExtractionJob](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartMemoryExtractionJob.html)  **
  - **Description:** Grants permission to start memory extraction job
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:actorId](#list_bedrock-agentcore-bedrock-agentcore_actorId)<br />[bedrock-agentcore:sessionId](#list_bedrock-agentcore-bedrock-agentcore_sessionId)<br />[bedrock-agentcore:strategyId](#list_bedrock-agentcore-bedrock-agentcore_strategyId)
  - **Access level:** Write

- **   [StartPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html)  **
  - **Description:** Grants permission to start an AI-powered policy generation request
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRecommendation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartRecommendation.html)  **
  - **Description:** Grants permission to start a recommendation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopBatchEvaluation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBatchEvaluation.html)  **
  - **Description:** Grants permission to stop a batch evaluation
  - **Resource types (\*required):** [batch-evaluate\*](#list_bedrock-agentcore-resource-batch-evaluate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html)  **
  - **Description:** Grants permission to stop a browser session
  - **Resource types (\*required):** [browser\*](#list_bedrock-agentcore-resource-browser) / **Condition keys:**  
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html)  **
  - **Description:** Grants permission to stop a code interpreter session
  - **Resource types (\*required):** [code-interpreter\*](#list_bedrock-agentcore-resource-code-interpreter) / **Condition keys:**  
  - **Resource types (\*required):** [code-interpreter-custom\*](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRuntimeSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopRuntimeSession.html)  **
  - **Description:** Grants permission to stop a runtime session
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SubmitRegistryRecordForApproval](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SubmitRegistryRecordForApproval.html)  **
  - **Description:** Grants permission to submit a registry record for approval
  - **Resource types (\*required):** [registry-record\*](#list_bedrock-agentcore-resource-registry-record)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to Tag a Bedrock-AgentCore resource
  - **Resource types (\*required):** [apikeycredentialprovider](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [browser-custom](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [browser-profile](#list_bedrock-agentcore-resource-browser-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [capacity-provider](#list_bedrock-agentcore-resource-capacity-provider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [code-interpreter-custom](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [evaluator](#list_bedrock-agentcore-resource-evaluator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [harness](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [memory](#list_bedrock-agentcore-resource-memory) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [oauth2credentialprovider](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [online-evaluation-config](#list_bedrock-agentcore-resource-online-evaluation-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [payment-manager](#list_bedrock-agentcore-resource-payment-manager) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [paymentcredentialprovider](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [policy-engine](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [token-vault](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [workload-identity](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [workload-identity-directory](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_bedrock-agentcore-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to Untag a Bedrock-AgentCore resource
  - **Resource types (\*required):** [apikeycredentialprovider](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [browser-custom](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [browser-profile](#list_bedrock-agentcore-resource-browser-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [capacity-provider](#list_bedrock-agentcore-resource-capacity-provider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [code-interpreter-custom](#list_bedrock-agentcore-resource-code-interpreter-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [evaluator](#list_bedrock-agentcore-resource-evaluator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [gateway](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [harness](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [memory](#list_bedrock-agentcore-resource-memory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [oauth2credentialprovider](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [online-evaluation-config](#list_bedrock-agentcore-resource-online-evaluation-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [payment-manager](#list_bedrock-agentcore-resource-payment-manager) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [paymentcredentialprovider](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [policy-engine](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [runtime](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [runtime-endpoint](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [token-vault](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [workload-identity](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Resource types (\*required):** [workload-identity-directory](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_bedrock-agentcore-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateABTest](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateABTest.html)  **
  - **Description:** Grants permission to update an A/B test
  - **Resource types (\*required):** [ab-test\*](#list_bedrock-agentcore-resource-ab-test)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateAgentRuntime.html)  **
  - **Description:** Grants permission to update an agent runtime
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:RuntimeAuthorizerType](#list_bedrock-agentcore-bedrock-agentcore_RuntimeAuthorizerType)<br />[bedrock-agentcore:securityGroups](#list_bedrock-agentcore-bedrock-agentcore_securityGroups)<br />[bedrock-agentcore:subnets](#list_bedrock-agentcore-bedrock-agentcore_subnets)
  - **Access level:** Write

- **   [UpdateAgentRuntimeEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateAgentRuntimeEndpoint.html)  **
  - **Description:** Grants permission to update an agent runtime endpoint
  - **Resource types (\*required):** [runtime\*](#list_bedrock-agentcore-resource-runtime) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runtime-endpoint\*](#list_bedrock-agentcore-resource-runtime-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApiKeyCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateApiKeyCredentialProvider.html)  **
  - **Description:** Grants permission to update an existing API Key Credential Provider
  - **Resource types (\*required):** [apikeycredentialprovider\*](#list_bedrock-agentcore-resource-apikeycredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateBrowserStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html)  **
  - **Description:** Grants permission to update the status of browser session stream
  - **Resource types (\*required):** [browser\*](#list_bedrock-agentcore-resource-browser) / **Condition keys:**  
  - **Resource types (\*required):** [browser-custom\*](#list_bedrock-agentcore-resource-browser-custom) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateCapacityProvider.html)  **
  - **Description:** Grants permission to update a capacity provider
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfigurationBundle](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateConfigurationBundle.html)  **
  - **Description:** Grants permission to update a configuration bundle
  - **Resource types (\*required):** [configuration-bundle\*](#list_bedrock-agentcore-resource-configuration-bundle)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataset](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateDataset.html)  **
  - **Description:** Grants permission to update a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDatasetExamples](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateDatasetExamples.html)  **
  - **Description:** Grants permission to update examples in a dataset
  - **Resource types (\*required):** [dataset\*](#list_bedrock-agentcore-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEvaluator](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateEvaluator.html)  **
  - **Description:** Grants permission to update an evaluator
  - **Resource types (\*required):** [evaluator\*](#list_bedrock-agentcore-resource-evaluator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGateway](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.html)  **
  - **Description:** Grants permission to update an existing gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayRateLimit](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGatewayRateLimit.html)  **
  - **Description:** Grants permission to update a rate limit on a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayRule](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGatewayRule.html)  **
  - **Description:** Grants permission to update an existing gateway rule
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGatewayTarget](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateGatewayTarget.html)  **
  - **Description:** Grants permission to update an existing gateway target
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHarness](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateHarness.html)  **
  - **Description:** Grants permission to update a harness
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHarnessEndpoint](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateHarnessEndpoint.html)  **
  - **Description:** Grants permission to update harness endpoint
  - **Resource types (\*required):** [harness\*](#list_bedrock-agentcore-resource-harness) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [harness-endpoint\*](#list_bedrock-agentcore-resource-harness-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMemory](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.html)  **
  - **Description:** Grants permission to update a Memory resource
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOauth2CredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateOauth2CredentialProvider.html)  **
  - **Description:** Grants permission to update an existing OAuth2 Credential Provider
  - **Resource types (\*required):** [oauth2credentialprovider\*](#list_bedrock-agentcore-resource-oauth2credentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOnlineEvaluationConfig](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateOnlineEvaluationConfig.html)  **
  - **Description:** Grants permission to update an online evaluation configuration
  - **Resource types (\*required):** [online-evaluation-config\*](#list_bedrock-agentcore-resource-online-evaluation-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePaymentConnector](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatePaymentConnector.html)  **
  - **Description:** Grants permission to update an existing payment connector
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePaymentCredentialProvider](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatePaymentCredentialProvider.html)  **
  - **Description:** Grants permission to update an existing Payment Credential Provider
  - **Resource types (\*required):** [paymentcredentialprovider\*](#list_bedrock-agentcore-resource-paymentcredentialprovider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [token-vault\*](#list_bedrock-agentcore-resource-token-vault) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePaymentManager](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatePaymentManager.html)  **
  - **Description:** Grants permission to update an existing payment manager
  - **Resource types (\*required):** [payment-manager\*](#list_bedrock-agentcore-resource-payment-manager)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:DiscoveryUrl](#list_bedrock-agentcore-bedrock-agentcore_DiscoveryUrl)
  - **Access level:** Write

- **   [UpdatePolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatePolicy.html)  **
  - **Description:** Grants permission to update an existing policy
  - **Resource types (\*required):** [policy\*](#list_bedrock-agentcore-resource-policy) / **Condition keys:**  
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdatePolicyEngine.html)  **
  - **Description:** Grants permission to update a policy engine
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegistry](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateRegistry.html)  **
  - **Description:** Grants permission to update an existing registry
  - **Resource types (\*required):** [registry\*](#list_bedrock-agentcore-resource-registry)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRegistryRecord](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateRegistryRecord.html)  **
  - **Description:** Grants permission to update an existing registry record
  - **Resource types (\*required):** [registry-record\*](#list_bedrock-agentcore-resource-registry-record)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRegistryRecordStatus](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateRegistryRecordStatus.html)  **
  - **Description:** Grants permission to update the status of a registry record
  - **Resource types (\*required):** [registry-record\*](#list_bedrock-agentcore-resource-registry-record)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWorkloadIdentity](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateWorkloadIdentity.html)  **
  - **Description:** Grants permission to update the metadata of an existing Workload Identity
  - **Resource types (\*required):** [workload-identity\*](#list_bedrock-agentcore-resource-workload-identity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workload-identity-directory\*](#list_bedrock-agentcore-resource-workload-identity-directory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore-permission-only-actions"></a>

The following actions are defined by Amazon Bedrock Agentcore but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/)  **
  - **Description:** Grants permission to configure vended telemetry for a resource
  - **Resource types (\*required):** [memory\*](#list_bedrock-agentcore-resource-memory) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [payment-manager](#list_bedrock-agentcore-resource-payment-manager) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AuthorizeAction](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to evaluate Cedar policies for authorization requests
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [GatewayAssociateWebACL](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/)  **
  - **Description:** Grants permission to associate an AWS WAF Web ACL with an AgentCore Gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GatewayDisassociateWebACL](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/)  **
  - **Description:** Grants permission to remove the AWS WAF Web ACL association from an AgentCore Gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GatewayGetWebACLForResource](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/)  **
  - **Description:** Grants permission to retrieve the AWS WAF Web ACL ARN currently associated with an AgentCore Gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GatewayListResourcesForWebACL](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/)  **
  - **Description:** Grants permission to list AgentCore Gateways associated with an AWS WAF Web ACL
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [InvokeGateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke a gateway
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [InvokeWebSearch](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to invoke a web search target
  - **Resource types (\*required):** [web-search\*](#list_bedrock-agentcore-resource-web-search)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ManageAdminPolicy](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create or modify wildcard policies that apply to gateway resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ManageResourceScopedPolicy](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to create or modify policies that apply to specific gateway resources
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PartiallyAuthorizeActions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to perform partial evaluation of Cedar policies to authorize a caller to list tools they are allowed to call
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [policy-engine\*](#list_bedrock-agentcore-resource-policy-engine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PassCapacityProvider](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to pass a capacity provider to a runtime resource
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutSystemLogEvents](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to collect system logs from the runtime instances
  - **Resource types (\*required):** [capacity-provider\*](#list_bedrock-agentcore-resource-capacity-provider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)<br />[bedrock-agentcore:runtimeSessionId](#list_bedrock-agentcore-bedrock-agentcore_runtimeSessionId)
  - **Access level:** Write

- **   [SynchronizeGatewayTargets](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/welcome.html)  **
  - **Description:** Grants permission to enable search on gateways
  - **Resource types (\*required):** [gateway\*](#list_bedrock-agentcore-resource-gateway)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ab-test](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/abTest.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:ab-test/${ABTestId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [apikeycredentialprovider](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/apikeycredentialprovider.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:token-vault/${TokenVaultId}/apikeycredentialprovider/${Name} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [batch-evaluate](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/batchEvaluation.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:batch-evaluate/${BatchEvaluationId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/browser.html)  | arn:${Partition}:bedrock-agentcore:${Region}:aws:browser/${BrowserId} |   | 
|  [browser-custom](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/browser.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:browser-custom/${BrowserId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [browser-profile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/browserProfile.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:browser-profile/${BrowserProfileId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [capacity-provider](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/capacityProvider.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:capacity-provider/${CapacityProviderId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [code-interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/codeInterpreter.html)  | arn:${Partition}:bedrock-agentcore:${Region}:aws:code-interpreter/${CodeInterpreterId} |   | 
|  [code-interpreter-custom](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/codeInterpreter.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:code-interpreter-custom/${CodeInterpreterId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [configuration-bundle](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/configurationBundle.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:configuration-bundle/${ConfigurationBundleId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/dataset.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:dataset/${DatasetId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [evaluator](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/evaluator.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:evaluator/${EvaluatorId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/gateway.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:gateway/${GatewayId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [harness](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/harness.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:harness/${HarnessId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [harness-endpoint](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/harness-endpoint.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:harness/${HarnessId}/harness-endpoint/${Name} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/memory.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:memory/${MemoryId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [oauth2credentialprovider](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/oauth2credentialprovider.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:token-vault/${TokenVaultId}/oauth2credentialprovider/${Name} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [online-evaluation-config](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/onlineEvaluationConfig.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:online-evaluation-config/${OnlineEvaluationConfigId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [payment-manager](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/paymentManager.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:payment-manager/${PaymentManagerId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [paymentcredentialprovider](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/paymentcredentialprovider.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:token-vault/${TokenVaultId}/paymentcredentialprovider/${Name} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/policy.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:policy-engine/${PolicyEngineId}/policy/${PolicyId} |   | 
|  [policy-engine](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/policyEngine.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:policy-engine/${PolicyEngineId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [policy-generation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/policyGeneration.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:policy-engine/${PolicyEngineId}/policy-generation/${PolicyGenerationId} |   | 
|  [recommendation](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/recommendation.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:recommendation/${RecommendationId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/registry.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:registry/${RegistryId} |   | 
|  [registry-record](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/registryRecord.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:registry/${RegistryId}/record/${RecordId} |   | 
|  [runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/runtime.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:runtime/${RuntimeId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [runtime-endpoint](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/runtimeEndpoint.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:runtime/${RuntimeId}/runtime-endpoint/${Name} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [token-vault](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/tokenVault.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:token-vault/${TokenVaultId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [web-search](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/webSearch.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:tool/web-search.v1 |   | 
|  [workload-identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/workloadIdentity.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:workload-identity-directory/${DirectoryId}/workload-identity/${WorkloadIdentityName} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 
|  [workload-identity-directory](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/workloadIdentityDirectory.html)  | arn:${Partition}:bedrock-agentcore:${Region}:${Account}:workload-identity-directory/${DirectoryId} | [aws:ResourceTag/${TagKey}](#list_bedrock-agentcore-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Bedrock Agentcore
<a name="list_bedrock-agentcore-policy-keys"></a>

Amazon Bedrock Agentcore defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the allowed set of values for each of the mandatory tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by having actions based on the tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by creating requests based on the presence of mandatory tags in the request | ArrayOfString | 
|   [bedrock-agentcore:AllowedQueryParameters](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-allowedQueryParameters)  | Filters access by the metadataConfiguration.allowedQueryParameters attribute of a gateway target | ArrayOfString | 
|   [bedrock-agentcore:AllowedRequestHeaders](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-allowedRequestHeaders)  | Filters access by the metadataConfiguration.allowedRequestHeaders attribute of a gateway target | ArrayOfString | 
|   [bedrock-agentcore:AllowedResponseHeaders](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-allowedResponseHeaders)  | Filters access by the metadataConfiguration.allowedResponseHeaders attribute of a gateway target | ArrayOfString | 
|   [bedrock-agentcore:CredentialProviderScope](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-credentialProviderScope)  | Filters access by the scopes attribute of an OAuth credential provider on a gateway target | ArrayOfString | 
|   [bedrock-agentcore:CredentialProviderType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-credentialProviderType)  | Filters access by the credentialProviderConfigurations.credentialProviderType attribute of a gateway target | String | 
|   [bedrock-agentcore:DiscoveryUrl](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-discoveryUrl)  | Filters access by the authorizerConfiguration.customJWTAuthorizer.discoveryUrl attribute of a Gateway | String | 
|   [bedrock-agentcore:GatewayAuthorizerType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-gatewayAuthorizerType)  | Filters access by the authorizerType attribute on a Gateway | String | 
|   [bedrock-agentcore:HttpTargetConfigurationType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-httpTargetConfigurationType)  | Filters access by the HTTP target configuration type of a gateway target | String | 
|   [bedrock-agentcore:InboundJwtClaim/aud](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-aud)  | Filters access by the audience claim (aud) in the JWT passed in the request | ArrayOfString | 
|   [bedrock-agentcore:InboundJwtClaim/client\_id](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-client_id)  | Filters access by the client\_id claim in the JWT passed in the request | String | 
|   [bedrock-agentcore:InboundJwtClaim/iss](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-iss)  | Filters access by the issuer (iss) claim present in the JWT passed in the request | String | 
|   [bedrock-agentcore:InboundJwtClaim/scope](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-scope)  | Filters access by the scope claim in the JWT passed in the request | ArrayOfString | 
|   [bedrock-agentcore:InboundJwtClaim/sub](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-sub)  | Filters access by the subject claim (sub) in the JWT passed in the request | String | 
|   [bedrock-agentcore:InferenceTargetConfigurationType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-inferenceTargetConfigurationType)  | Filters access by the inference target configuration type of a gateway target | String | 
|   [bedrock-agentcore:KmsKeyArn](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-kmsKeyArn)  | Filters access by KMS Key arn provided | String | 
|   [bedrock-agentcore:McpTargetConfigurationType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-mcpTargetConfigurationType)  | Filters access by the MCP target configuration type of a gateway target | String | 
|   [bedrock-agentcore:PolicyEngineArn](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-policyEngineArn)  | Filters access by the policyEngineConfiguration.arn attribute of a Gateway | String | 
|   [bedrock-agentcore:PolicyEngineMode](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-policyEngineMode)  | Filters access by the policyEngineConfiguration.mode attribute of a Gateway | String | 
|   [bedrock-agentcore:PrivateEndpointType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-privateEndpointType)  | Filters access by the private endpoint type of a gateway target | String | 
|   [bedrock-agentcore:ProtocolType](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-protocolType)  | Filters access by the protocolType attribute of a Gateway | String | 
|   [bedrock-agentcore:ResourceConfigurationIdentifier](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-resourceConfigurationIdentifier)  | Filters access by the resource configuration identifier of a gateway target private endpoint | String | 
|   [bedrock-agentcore:RuntimeAuthorizerType](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-authorizer-type-condition-key.html)  | Filters access by the authorizer type configured for the AgentCore runtime | String | 
|   [bedrock-agentcore:actorId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-actorId)  | Filters access by Actor Id | String | 
|   [bedrock-agentcore:namespace](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-namespace)  | Filters access by namespace | String | 
|   [bedrock-agentcore:runtimeSessionId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-runtimeSessionId)  | Filters access by Runtime Session Id | String | 
|   [bedrock-agentcore:securityGroups](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-vpc-condition.html)  | Filters access by the ID of security groups configured for an AgentCore resource | ArrayOfString | 
|   [bedrock-agentcore:sessionId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-sessionId)  | Filters access by Memory Session Id | String | 
|   [bedrock-agentcore:strategyId](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-strategyId)  | Filters access by Memory Strategy Id | String | 
|   [bedrock-agentcore:subnets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-vpc-condition.html)  | Filters access by the ID of subnets configured for an AgentCore resource | ArrayOfString | 
|   [bedrock-agentcore:userid](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/#condition-keys-userid)  | Filters access by the static user ID value passed in the request | String | 