

# Actions, resources, and condition keys for AWS Lambda
<a name="list_lambda"></a>

AWS Lambda (service prefix: `lambda`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lambda/latest/dg/lambda-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lambda/lambda.json) for this service.

**Topics**
+ [API operations defined by AWS Lambda](#list_lambda-operations)
+ [Actions defined by AWS Lambda](#list_lambda-actions-as-permissions)
+ [Permission-only actions for AWS Lambda](#list_lambda-permission-only-actions)
+ [Resource types defined by AWS Lambda](#list_lambda-resources-for-iam-policies)
+ [Condition keys for AWS Lambda](#list_lambda-policy-keys)

## API operations defined by AWS Lambda
<a name="list_lambda-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_lambda-actions-as-permissions).




- **   AddEventSource  **
  - **SDK client:** lambda
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) 
  - **Condition key:** iam:PassedToService
  - **Possible value(s):** lambda.amazonaws.com
  - **Access level:** Write

- **   AddLayerVersionPermission  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:AddLayerVersionPermission](#list_lambda-action-AddLayerVersionPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AddPermission  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:AddPermission](#list_lambda-action-AddPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CheckpointDurableExecution  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CheckpointDurableExecution](#list_lambda-action-CheckpointDurableExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAlias  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateAlias](#list_lambda-action-CreateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCapacityProvider  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateCapacityProvider](#list_lambda-action-CreateCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com / **Access level:** Write

- **   CreateCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateCodeSigningConfig](#list_lambda-action-CreateCodeSigningConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEventSourceMapping  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateEventSourceMapping](#list_lambda-action-CreateEventSourceMapping)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFunction  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateFunction](#list_lambda-action-CreateFunction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:GetLayerVersion](#list_lambda-action-GetLayerVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lambda:PassCapacityProvider](#list_lambda-action-PassCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com / **Access level:** Write

- **   CreateFunctionUrlConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:CreateFunctionUrlConfig](#list_lambda-action-CreateFunctionUrlConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlias  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteAlias](#list_lambda-action-DeleteAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCapacityProvider  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteCapacityProvider](#list_lambda-action-DeleteCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteCodeSigningConfig](#list_lambda-action-DeleteCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventSourceMapping  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteEventSourceMapping](#list_lambda-action-DeleteEventSourceMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunction  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteFunction](#list_lambda-action-DeleteFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunctionCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteFunctionCodeSigningConfig](#list_lambda-action-DeleteFunctionCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunctionConcurrency  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteFunctionConcurrency](#list_lambda-action-DeleteFunctionConcurrency) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunctionEventInvokeConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteFunctionEventInvokeConfig](#list_lambda-action-DeleteFunctionEventInvokeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFunctionUrlConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteFunctionUrlConfig](#list_lambda-action-DeleteFunctionUrlConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLayerVersion  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteLayerVersion](#list_lambda-action-DeleteLayerVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProvisionedConcurrencyConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteProvisionedConcurrencyConfig](#list_lambda-action-DeleteProvisionedConcurrencyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:DeleteResourcePolicy](#list_lambda-action-DeleteResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [lambda:RemovePermission](#list_lambda-action-RemovePermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   GetAccountSettings  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetAccountSettings](#list_lambda-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAlias  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetAlias](#list_lambda-action-GetAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCapacityProvider  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetCapacityProvider](#list_lambda-action-GetCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetCodeSigningConfig](#list_lambda-action-GetCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDurableExecution  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetDurableExecution](#list_lambda-action-GetDurableExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDurableExecutionHistory  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetDurableExecutionHistory](#list_lambda-action-GetDurableExecutionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDurableExecutionState  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetDurableExecutionState](#list_lambda-action-GetDurableExecutionState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventSourceMapping  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetEventSourceMapping](#list_lambda-action-GetEventSourceMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunction  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunction](#list_lambda-action-GetFunction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lambda:ListTags](#list_lambda-action-ListTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetFunctionCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionCodeSigningConfig](#list_lambda-action-GetFunctionCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionConcurrency  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionConcurrency](#list_lambda-action-GetFunctionConcurrency) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionConfiguration  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionConfiguration](#list_lambda-action-GetFunctionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionEventInvokeConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionEventInvokeConfig](#list_lambda-action-GetFunctionEventInvokeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionRecursionConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionRecursionConfig](#list_lambda-action-GetFunctionRecursionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionScalingConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionScalingConfig](#list_lambda-action-GetFunctionScalingConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFunctionUrlConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetFunctionUrlConfig](#list_lambda-action-GetFunctionUrlConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLayerVersion  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetLayerVersion](#list_lambda-action-GetLayerVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLayerVersionByArn  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetLayerVersion](#list_lambda-action-GetLayerVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLayerVersionPolicy  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetLayerVersionPolicy](#list_lambda-action-GetLayerVersionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetPolicy](#list_lambda-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProvisionedConcurrencyConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetProvisionedConcurrencyConfig](#list_lambda-action-GetProvisionedConcurrencyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetPolicy](#list_lambda-action-GetPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lambda:GetResourcePolicy](#list_lambda-action-GetResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetRuntimeManagementConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetRuntimeManagementConfig](#list_lambda-action-GetRuntimeManagementConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Invoke  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:InvokeFunction](#list_lambda-action-InvokeFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeAsync  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:InvokeAsync](#list_lambda-action-InvokeAsync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeWithResponseStream  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:InvokeFunction](#list_lambda-action-InvokeFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListAliases  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListAliases](#list_lambda-action-ListAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCapacityProviders  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListCapacityProviders](#list_lambda-action-ListCapacityProviders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeSigningConfigs  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListCodeSigningConfigs](#list_lambda-action-ListCodeSigningConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDurableExecutionsByFunction  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListDurableExecutionsByFunction](#list_lambda-action-ListDurableExecutionsByFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventSourceMappings  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListEventSourceMappings](#list_lambda-action-ListEventSourceMappings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionEventInvokeConfigs  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListFunctionEventInvokeConfigs](#list_lambda-action-ListFunctionEventInvokeConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionUrlConfigs  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListFunctionUrlConfigs](#list_lambda-action-ListFunctionUrlConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionVersionsByCapacityProvider  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListFunctionVersionsByCapacityProvider](#list_lambda-action-ListFunctionVersionsByCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctions  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListFunctions](#list_lambda-action-ListFunctions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFunctionsByCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListFunctionsByCodeSigningConfig](#list_lambda-action-ListFunctionsByCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLayerVersions  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListLayerVersions](#list_lambda-action-ListLayerVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLayers  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListLayers](#list_lambda-action-ListLayers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisionedConcurrencyConfigs  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListProvisionedConcurrencyConfigs](#list_lambda-action-ListProvisionedConcurrencyConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListTags](#list_lambda-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVersionsByFunction  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:ListVersionsByFunction](#list_lambda-action-ListVersionsByFunction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishLayerVersion  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PublishLayerVersion](#list_lambda-action-PublishLayerVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PublishVersion  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PublishVersion](#list_lambda-action-PublishVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFunctionCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutFunctionCodeSigningConfig](#list_lambda-action-PutFunctionCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFunctionConcurrency  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutFunctionConcurrency](#list_lambda-action-PutFunctionConcurrency) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFunctionEventInvokeConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutFunctionEventInvokeConfig](#list_lambda-action-PutFunctionEventInvokeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFunctionRecursionConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutFunctionRecursionConfig](#list_lambda-action-PutFunctionRecursionConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFunctionScalingConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutFunctionScalingConfig](#list_lambda-action-PutFunctionScalingConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutProvisionedConcurrencyConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutProvisionedConcurrencyConfig](#list_lambda-action-PutProvisionedConcurrencyConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:AddPermission](#list_lambda-action-AddPermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [lambda:PutResourcePolicy](#list_lambda-action-PutResourcePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [lambda:RemovePermission](#list_lambda-action-RemovePermission)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write

- **   PutRuntimeManagementConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:PutRuntimeManagementConfig](#list_lambda-action-PutRuntimeManagementConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveLayerVersionPermission  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:RemoveLayerVersionPermission](#list_lambda-action-RemoveLayerVersionPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemovePermission  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:RemovePermission](#list_lambda-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SendDurableExecutionCallbackFailure  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:SendDurableExecutionCallbackFailure](#list_lambda-action-SendDurableExecutionCallbackFailure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDurableExecutionCallbackHeartbeat  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:SendDurableExecutionCallbackHeartbeat](#list_lambda-action-SendDurableExecutionCallbackHeartbeat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendDurableExecutionCallbackSuccess  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:SendDurableExecutionCallbackSuccess](#list_lambda-action-SendDurableExecutionCallbackSuccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDurableExecution  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:StopDurableExecution](#list_lambda-action-StopDurableExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UntagResource](#list_lambda-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAlias  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateAlias](#list_lambda-action-UpdateAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCapacityProvider  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateCapacityProvider](#list_lambda-action-UpdateCapacityProvider) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCodeSigningConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateCodeSigningConfig](#list_lambda-action-UpdateCodeSigningConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventSourceMapping  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateEventSourceMapping](#list_lambda-action-UpdateEventSourceMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunctionCode  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateFunctionCode](#list_lambda-action-UpdateFunctionCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunctionConfiguration  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:GetLayerVersion](#list_lambda-action-GetLayerVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [lambda:PassCapacityProvider](#list_lambda-action-PassCapacityProvider)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:UpdateFunctionConfiguration](#list_lambda-action-UpdateFunctionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com / **Access level:** Write

- **   UpdateFunctionEventInvokeConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateFunctionEventInvokeConfig](#list_lambda-action-UpdateFunctionEventInvokeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFunctionUrlConfig  **
  - **SDK client:** lambda
  - **IAM action:**  [lambda:UpdateFunctionUrlConfig](#list_lambda-action-UpdateFunctionUrlConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNetworkConnector  **
  - **SDK client:** lambda-core
  - **IAM action:**  [lambda:CreateNetworkConnector](#list_lambda-action-CreateNetworkConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com / **Access level:** Write

- **   DeleteNetworkConnector  **
  - **SDK client:** lambda-core
  - **IAM action:**  [lambda:DeleteNetworkConnector](#list_lambda-action-DeleteNetworkConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetNetworkConnector  **
  - **SDK client:** lambda-core
  - **IAM action:**  [lambda:GetNetworkConnector](#list_lambda-action-GetNetworkConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNetworkConnectors  **
  - **SDK client:** lambda-core
  - **IAM action:**  [lambda:ListNetworkConnectors](#list_lambda-action-ListNetworkConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpdateNetworkConnector  **
  - **SDK client:** lambda-core
  - **IAM action:**  [lambda:UpdateNetworkConnector](#list_lambda-action-UpdateNetworkConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lambda.amazonaws.com / **Access level:** Write

- **   CreateMicrovmAuthToken  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:CreateMicrovmAuthToken](#list_lambda-action-CreateMicrovmAuthToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMicrovmImage  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:CreateMicrovmImage](#list_lambda-action-CreateMicrovmImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:PassNetworkConnector](#list_lambda-action-PassNetworkConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateMicrovmShellAuthToken  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:CreateMicrovmShellAuthToken](#list_lambda-action-CreateMicrovmShellAuthToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMicrovmImage  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:DeleteMicrovmImage](#list_lambda-action-DeleteMicrovmImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMicrovmImageVersion  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:DeleteMicrovmImageVersion](#list_lambda-action-DeleteMicrovmImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetMicrovm  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:GetMicrovm](#list_lambda-action-GetMicrovm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMicrovmImage  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:GetMicrovmImage](#list_lambda-action-GetMicrovmImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMicrovmImageBuild  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:GetMicrovmImageBuild](#list_lambda-action-GetMicrovmImageBuild) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMicrovmImageVersion  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:GetMicrovmImageVersion](#list_lambda-action-GetMicrovmImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListManagedMicrovmImageVersions  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListManagedMicrovmImageVersions](#list_lambda-action-ListManagedMicrovmImageVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedMicrovmImages  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListManagedMicrovmImages](#list_lambda-action-ListManagedMicrovmImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMicrovmImageBuilds  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListMicrovmImageBuilds](#list_lambda-action-ListMicrovmImageBuilds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMicrovmImageVersions  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListMicrovmImageVersions](#list_lambda-action-ListMicrovmImageVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMicrovmImages  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListMicrovmImages](#list_lambda-action-ListMicrovmImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMicrovms  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListMicrovms](#list_lambda-action-ListMicrovms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ListTags](#list_lambda-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ResumeMicrovm  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:ResumeMicrovm](#list_lambda-action-ResumeMicrovm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RunMicrovm  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:PassNetworkConnector](#list_lambda-action-PassNetworkConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:RunMicrovm](#list_lambda-action-RunMicrovm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SuspendMicrovm  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:SuspendMicrovm](#list_lambda-action-SuspendMicrovm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:TagResource](#list_lambda-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateMicrovm  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:TerminateMicrovm](#list_lambda-action-TerminateMicrovm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:UntagResource](#list_lambda-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMicrovmImage  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:PassNetworkConnector](#list_lambda-action-PassNetworkConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lambda:UpdateMicrovmImage](#list_lambda-action-UpdateMicrovmImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateMicrovmImageVersion  **
  - **SDK client:** lambda-microvms
  - **IAM action:**  [lambda:UpdateMicrovmImageVersion](#list_lambda-action-UpdateMicrovmImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Lambda
<a name="list_lambda-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddLayerVersionPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddLayerVersionPermission.html)  **
  - **Description:** Grants permission to add permissions to the resource-based policy of a version of an AWS Lambda layer
  - **Resource types (\*required):** [layerVersion\*](#list_lambda-resource-layerVersion)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [AddPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_AddPermission.html)  **
  - **Description:** Grants permission to give an AWS service or another account permission to use an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)<br />[lambda:Principal](#list_lambda-lambda_Principal)
  - **Access level:** Permissions management, Write

- **   [CheckpointDurableExecution](https://docs.aws.amazon.com/lambda/latest/dg/API_CheckpointDurableExecution.html)  **
  - **Description:** Grants permission to save the progress of an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateAlias.html)  **
  - **Description:** Grants permission to create an alias for a Lambda function version
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateCapacityProvider.html)  **
  - **Description:** Grants permission to create an AWS Lambda capacity provider
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)<br />[lambda:SecurityGroupIds](#list_lambda-lambda_SecurityGroupIds)<br />[lambda:SubnetIds](#list_lambda-lambda_SubnetIds)
  - **Access level:** Write

- **   [CreateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateCodeSigningConfig.html)  **
  - **Description:** Grants permission to create an AWS Lambda code signing config
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html)  **
  - **Description:** Grants permission to create a mapping between an event source and an AWS Lambda function
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)
  - **Access level:** Write

- **   [CreateFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html)  **
  - **Description:** Grants permission to create an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)<br />[lambda:CodeSigningConfigArn](#list_lambda-lambda_CodeSigningConfigArn)<br />[lambda:Layer](#list_lambda-lambda_Layer)<br />[lambda:SecurityGroupIds](#list_lambda-lambda_SecurityGroupIds)<br />[lambda:SubnetIds](#list_lambda-lambda_SubnetIds)<br />[lambda:VpcIds](#list_lambda-lambda_VpcIds)
  - **Access level:** Write

- **   [CreateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunctionUrlConfig.html)  **
  - **Description:** Grants permission to create a function url configuration for a Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** Write

- **   [CreateMicrovmAuthToken](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmAuthToken.html)  **
  - **Description:** Grants permission to create an auth token for an AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmImage.html)  **
  - **Description:** Grants permission to create an AWS Lambda MicroVM image
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMicrovmShellAuthToken](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmShellAuthToken.html)  **
  - **Description:** Grants permission to create a shell auth token for an AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateNetworkConnector.html)  **
  - **Description:** Grants permission to create an AWS Lambda network connector
  - **Resource types (\*required):** [networkConnector\*](#list_lambda-resource-networkConnector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)<br />[lambda:SecurityGroupIds](#list_lambda-lambda_SecurityGroupIds)<br />[lambda:SubnetIds](#list_lambda-lambda_SubnetIds)
  - **Access level:** Write

- **   [DeleteAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteAlias.html)  **
  - **Description:** Grants permission to delete an AWS Lambda function alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteCapacityProvider.html)  **
  - **Description:** Grants permission to delete an AWS Lambda capacity provider
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteCodeSigningConfig.html)  **
  - **Description:** Grants permission to delete an AWS Lambda code signing config
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteEventSourceMapping.html)  **
  - **Description:** Grants permission to delete an AWS Lambda event source mapping
  - **Resource types (\*required):** [eventSourceMapping\*](#list_lambda-resource-eventSourceMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)
  - **Access level:** Write

- **   [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunction.html)  **
  - **Description:** Grants permission to delete an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionCodeSigningConfig.html)  **
  - **Description:** Grants permission to detach a code signing config from an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionConcurrency.html)  **
  - **Description:** Grants permission to remove a concurrent execution limit from an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionEventInvokeConfig.html)  **
  - **Description:** Grants permission to delete the configuration for asynchronous invocation for an AWS Lambda function, version, or alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteFunctionUrlConfig.html)  **
  - **Description:** Grants permission to delete function url configuration for a Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** Write

- **   [DeleteLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteLayerVersion.html)  **
  - **Description:** Grants permission to delete a version of an AWS Lambda layer
  - **Resource types (\*required):** [layerVersion\*](#list_lambda-resource-layerVersion)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_DeleteMicrovmImage.html)  **
  - **Description:** Grants permission to delete an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMicrovmImageVersion](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_DeleteMicrovmImageVersion.html)  **
  - **Description:** Grants permission to delete a version of an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteNetworkConnector.html)  **
  - **Description:** Grants permission to delete an AWS Lambda network connector
  - **Resource types (\*required):** [networkConnector\*](#list_lambda-resource-networkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteProvisionedConcurrencyConfig.html)  **
  - **Description:** Grants permission to delete the provisioned concurrency configuration for an AWS Lambda function
  - **Resource types (\*required):** [function alias](#list_lambda-resource-functionalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function version](#list_lambda-resource-functionversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to detach a policy from an AWS Lambda resource
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:Principal](#list_lambda-lambda_Principal)
  - **Access level:** Permissions management, Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to view details about an account's limits and usage in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAlias.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda function alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_GetCapacityProvider.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda capacity provider
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetCodeSigningConfig.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda code signing config
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecution.html)  **
  - **Description:** Grants permission to view details of an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDurableExecutionHistory](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecutionHistory.html)  **
  - **Description:** Grants permission to view execution history of an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDurableExecutionState](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecutionState.html)  **
  - **Description:** Grants permission to view current state of an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_GetEventSourceMapping.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda event source mapping
  - **Resource types (\*required):** [eventSourceMapping\*](#list_lambda-resource-eventSourceMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)
  - **Access level:** Read

- **   [GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionCodeSigningConfig.html)  **
  - **Description:** Grants permission to view the code signing config arn attached to an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConcurrency.html)  **
  - **Description:** Grants permission to view details about the reserved concurrency configuration for a function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html)  **
  - **Description:** Grants permission to view details about the version-specific settings of an AWS Lambda function or version
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionEventInvokeConfig.html)  **
  - **Description:** Grants permission to view the configuration for asynchronous invocation for a function, version, or alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionRecursionConfig.html)  **
  - **Description:** Grants permission to view the recursion configuration of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionScalingConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionScalingConfig.html)  **
  - **Description:** Grants permission to view the scaling configuration of an AWS Lambda function running on a capacity provider
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionUrlConfig.html)  **
  - **Description:** Grants permission to read function url configuration for a Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** Read

- **   [GetLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersion.html)  **
  - **Description:** Grants permission to view details about a version of an AWS Lambda layer. Note this action also supports GetLayerVersionByArn API
  - **Resource types (\*required):** [layerVersion\*](#list_lambda-resource-layerVersion)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLayerVersionPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersionPolicy.html)  **
  - **Description:** Grants permission to view the resource-based policy for a version of an AWS Lambda layer
  - **Resource types (\*required):** [layerVersion\*](#list_lambda-resource-layerVersion)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovm.html)  **
  - **Description:** Grants permission to view information about an AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImage.html)  **
  - **Description:** Grants permission to view information about an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMicrovmImageBuild](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImageBuild.html)  **
  - **Description:** Grants permission to view information about a build of an AWS Lambda MicroVM image version
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMicrovmImageVersion](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImageVersion.html)  **
  - **Description:** Grants permission to view information about a version of an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/API_GetNetworkConnector.html)  **
  - **Description:** Grants permission to view details about an AWS Lambda network connector
  - **Resource types (\*required):** [networkConnector\*](#list_lambda-resource-networkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetPolicy.html)  **
  - **Description:** Grants permission to view the resource-based policy for an AWS Lambda function, version, or alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetProvisionedConcurrencyConfig.html)  **
  - **Description:** Grants permission to view the provisioned concurrency configuration for an AWS Lambda function's alias or version
  - **Resource types (\*required):** [function alias](#list_lambda-resource-functionalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function version](#list_lambda-resource-functionversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetResourcePolicy.html)  **
  - **Description:** Grants permission to view a policy for an AWS Lambda resource
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetRuntimeManagementConfig.html)  **
  - **Description:** Grants permission to view the runtime management configuration of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeAsync](https://docs.aws.amazon.com/lambda/latest/dg/API_InvokeAsync.html)  **
  - **Description:** Grants permission to invoke a function asynchronously (Deprecated)
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html)  **
  - **Description:** Grants permission to invoke an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:EventSourceToken](#list_lambda-lambda_EventSourceToken)<br />[lambda:InvokedViaFunctionUrl](#list_lambda-lambda_InvokedViaFunctionUrl)
  - **Access level:** Write

- **   [ListAliases](https://docs.aws.amazon.com/lambda/latest/dg/API_ListAliases.html)  **
  - **Description:** Grants permission to retrieve a list of aliases for an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCapacityProviders](https://docs.aws.amazon.com/lambda/latest/dg/API_ListCapacityProviders.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda capacity providers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeSigningConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListCodeSigningConfigs.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda code signing configs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_ListDurableExecutionsByFunction.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda durable executions of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/dg/API_ListEventSourceMappings.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda event source mappings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFunctionEventInvokeConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionEventInvokeConfigs.html)  **
  - **Description:** Grants permission to retrieve a list of configurations for asynchronous invocation for a function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFunctionUrlConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionUrlConfigs.html)  **
  - **Description:** Grants permission to read function url configurations for a function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** List

- **   [ListFunctionVersionsByCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionVersionsByCapacityProvider.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda function versions by the capacity provider assigned
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda functions, with the version-specific configuration of each function
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFunctionsByCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionsByCodeSigningConfig.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda functions by the code signing config assigned 
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLayerVersions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayerVersions.html)  **
  - **Description:** Grants permission to retrieve a list of versions of an AWS Lambda layer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLayers](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayers.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda layers, with details about the latest version of each layer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedMicrovmImageVersions](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListManagedMicrovmImageVersions.html)  **
  - **Description:** Grants permission to retrieve a list of versions for a managed AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListManagedMicrovmImages](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListManagedMicrovmImages.html)  **
  - **Description:** Grants permission to retrieve a list of managed AWS Lambda MicroVM images
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMicrovmImageBuilds](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImageBuilds.html)  **
  - **Description:** Grants permission to retrieve a list of builds for an AWS Lambda MicroVM image version
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMicrovmImageVersions](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImageVersions.html)  **
  - **Description:** Grants permission to retrieve a list of versions for an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMicrovmImages](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImages.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda MicroVM images
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMicrovms](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovms.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda MicroVMs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNetworkConnectors](https://docs.aws.amazon.com/lambda/latest/dg/API_ListNetworkConnectors.html)  **
  - **Description:** Grants permission to retrieve a list of AWS Lambda network connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListProvisionedConcurrencyConfigs.html)  **
  - **Description:** Grants permission to retrieve a list of provisioned concurrency configurations for an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/lambda/latest/dg/API_ListTags.html)  **
  - **Description:** Grants permission to retrieve a list of tags for an AWS Lambda function, event source mapping, capacity provider, code signing configuration, network connector or MicroVM image resource
  - **Resource types (\*required):** [capacityProvider](#list_lambda-resource-capacityProvider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [code signing config](#list_lambda-resource-codesigningconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [eventSourceMapping](#list_lambda-resource-eventSourceMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function](#list_lambda-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [microvmImage](#list_lambda-resource-microvmImage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [networkConnector](#list_lambda-resource-networkConnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVersionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_ListVersionsByFunction.html)  **
  - **Description:** Grants permission to retrieve a list of versions for an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PublishLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_PublishLayerVersion.html)  **
  - **Description:** Grants permission to create an AWS Lambda layer
  - **Resource types (\*required):** [layer\*](#list_lambda-resource-layer)
  - **Condition keys:**  
  - **Access level:** Write

- **   [PublishVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_PublishVersion.html)  **
  - **Description:** Grants permission to create an AWS Lambda function version
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionCodeSigningConfig.html)  **
  - **Description:** Grants permission to attach a code signing config to an AWS Lambda function
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:CodeSigningConfigArn](#list_lambda-lambda_CodeSigningConfigArn)
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:CodeSigningConfigArn](#list_lambda-lambda_CodeSigningConfigArn)
  - **Access level:** Write

- **   [PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionConcurrency.html)  **
  - **Description:** Grants permission to configure reserved concurrency for an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionEventInvokeConfig.html)  **
  - **Description:** Grants permission to configures options for asynchronous invocation on an AWS Lambda function, version, or alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionRecursionConfig.html)  **
  - **Description:** Grants permission to update the recursion configuration of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutFunctionScalingConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutFunctionScalingConfig.html)  **
  - **Description:** Grants permission to update the scaling configuration of an AWS Lambda function running on a capacity provider
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutProvisionedConcurrencyConfig.html)  **
  - **Description:** Grants permission to configure provisioned concurrency for an AWS Lambda function's alias or version
  - **Resource types (\*required):** [function alias](#list_lambda-resource-functionalias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function version](#list_lambda-resource-functionversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach a policy to an AWS Lambda resource
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:Principal](#list_lambda-lambda_Principal)
  - **Access level:** Permissions management, Write

- **   [PutRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_PutRuntimeManagementConfig.html)  **
  - **Description:** Grants permission to update the runtime management configuration of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemoveLayerVersionPermission](https://docs.aws.amazon.com/lambda/latest/dg/API_RemoveLayerVersionPermission.html)  **
  - **Description:** Grants permission to remove a statement from the permissions policy for a version of an AWS Lambda layer
  - **Resource types (\*required):** [layerVersion\*](#list_lambda-resource-layerVersion)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [RemovePermission](https://docs.aws.amazon.com/lambda/latest/dg/API_RemovePermission.html)  **
  - **Description:** Grants permission to revoke function-use permission from an AWS service or another account
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)<br />[lambda:Principal](#list_lambda-lambda_Principal)
  - **Access level:** Permissions management, Write

- **   [ResumeMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ResumeMicrovm.html)  **
  - **Description:** Grants permission to resume a suspended AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RunMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_RunMicrovm.html)  **
  - **Description:** Grants permission to run an AWS Lambda MicroVM from a MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDurableExecutionCallbackFailure](https://docs.aws.amazon.com/lambda/latest/dg/API_SendDurableExecutionCallbackFailure.html)  **
  - **Description:** Grants permission to send a failure response for a callback operation in an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDurableExecutionCallbackHeartbeat](https://docs.aws.amazon.com/lambda/latest/dg/API_SendDurableExecutionCallbackHeartbeat.html)  **
  - **Description:** Grants permission to send a heartbeat for a callback operation in an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDurableExecutionCallbackSuccess](https://docs.aws.amazon.com/lambda/latest/dg/API_SendDurableExecutionCallbackSuccess.html)  **
  - **Description:** Grants permission to send a successful response for a callback operation in an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDurableExecution](https://docs.aws.amazon.com/lambda/latest/dg/API_StopDurableExecution.html)  **
  - **Description:** Grants permission to stop an AWS Lambda durable execution
  - **Resource types (\*required):** [durable execution\*](#list_lambda-resource-durableexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SuspendMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_SuspendMicrovm.html)  **
  - **Description:** Grants permission to suspend an AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lambda/latest/dg/API_TagResources.html)  **
  - **Description:** Grants permission to add tags to an AWS Lambda function, event source mapping, capacity provider, code signing configuration, network connector or MicroVM image resource
  - **Resource types (\*required):** [capacityProvider](#list_lambda-resource-capacityProvider) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [code signing config](#list_lambda-resource-codesigningconfig) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [eventSourceMapping](#list_lambda-resource-eventSourceMapping) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [function](#list_lambda-resource-function) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [microvmImage](#list_lambda-resource-microvmImage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [networkConnector](#list_lambda-resource-networkConnector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lambda-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_TerminateMicrovm.html)  **
  - **Description:** Grants permission to terminate an AWS Lambda MicroVM
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/lambda/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an AWS Lambda function, event source mapping, capacity provider, code signing configuration, network connector or MicroVM image resource
  - **Resource types (\*required):** [capacityProvider](#list_lambda-resource-capacityProvider) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [code signing config](#list_lambda-resource-codesigningconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [eventSourceMapping](#list_lambda-resource-eventSourceMapping) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [function](#list_lambda-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [microvmImage](#list_lambda-resource-microvmImage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Resource types (\*required):** [networkConnector](#list_lambda-resource-networkConnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lambda-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateAlias.html)  **
  - **Description:** Grants permission to update the configuration of an AWS Lambda function's alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateCapacityProvider.html)  **
  - **Description:** Grants permission to update an AWS Lambda capacity provider
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateCodeSigningConfig.html)  **
  - **Description:** Grants permission to update an AWS Lambda code signing config
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateEventSourceMapping.html)  **
  - **Description:** Grants permission to update the configuration of an AWS Lambda event source mapping
  - **Resource types (\*required):** [eventSourceMapping\*](#list_lambda-resource-eventSourceMapping)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)
  - **Access level:** Write

- **   [UpdateFunctionCode](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionCode.html)  **
  - **Description:** Grants permission to update the code of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionCodeSigningConfig.html)  **
  - **Description:** Grants permission to update the code signing config of an AWS Lambda function
  - **Resource types (\*required):** [code signing config\*](#list_lambda-resource-codesigningconfig) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionConfiguration.html)  **
  - **Description:** Grants permission to modify the version-specific settings of an AWS Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:Layer](#list_lambda-lambda_Layer)<br />[lambda:SecurityGroupIds](#list_lambda-lambda_SecurityGroupIds)<br />[lambda:SubnetIds](#list_lambda-lambda_SubnetIds)<br />[lambda:VpcIds](#list_lambda-lambda_VpcIds)
  - **Access level:** Write

- **   [UpdateFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionEventInvokeConfig.html)  **
  - **Description:** Grants permission to modify the configuration for asynchronous invocation for an AWS Lambda function, version, or alias
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateFunctionUrlConfig.html)  **
  - **Description:** Grants permission to update a function url configuration for a Lambda function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** Write

- **   [UpdateMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_UpdateMicrovmImage.html)  **
  - **Description:** Grants permission to update an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMicrovmImageVersion](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_UpdateMicrovmImageVersion.html)  **
  - **Description:** Grants permission to update a version of an AWS Lambda MicroVM image
  - **Resource types (\*required):** [microvmImage\*](#list_lambda-resource-microvmImage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/API_UpdateNetworkConnector.html)  **
  - **Description:** Grants permission to update an AWS Lambda network connector
  - **Resource types (\*required):** [networkConnector\*](#list_lambda-resource-networkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Lambda
<a name="list_lambda-permission-only-actions"></a>

The following actions are defined by AWS Lambda but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ConnectMicrovm](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)  **
  - **Description:** Grants permission to connect to a Lambda MicroVM via HTTP (VPC Endpoint only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableReplication](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-permissions.html)  **
  - **Description:** Grants permission to disable replication for a Lambda@Edge function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [EnableReplication](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-edge-permissions.html)  **
  - **Description:** Grants permission to enable replication for a Lambda@Edge function
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [InvokeFunctionUrl](https://docs.aws.amazon.com/lambda/latest/dg/API_InvokeFunctionUrl.html)  **
  - **Description:** Grants permission to invoke an AWS Lambda function through url
  - **Resource types (\*required):** [function\*](#list_lambda-resource-function)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)<br />[lambda:EventSourceToken](#list_lambda-lambda_EventSourceToken)<br />[lambda:FunctionArn](#list_lambda-lambda_FunctionArn)<br />[lambda:FunctionUrlAuthType](#list_lambda-lambda_FunctionUrlAuthType)
  - **Access level:** Write

- **   [PassCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)  **
  - **Description:** Grants permission to pass an AWS Lambda capacity provider to a service
  - **Resource types (\*required):** [capacityProvider\*](#list_lambda-resource-capacityProvider)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PassNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)  **
  - **Description:** Grants permission to pass an AWS Lambda network connector to a service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Lambda
<a name="list_lambda-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [capacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:capacity-provider:${CapacityProviderName} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [code signing config](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:code-signing-config:${CodeSigningConfigId} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}:${Version}/durable-execution/${ExecutionName}/${ExecutionId} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [eventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:event-source-mapping:${UUID} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [function alias](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}:${Alias} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [function version](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:function:${FunctionName}:${Version} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [layer](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:layer:${LayerName} |   | 
|  [layerVersion](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:layer:${LayerName}:${LayerVersion} |   | 
|  [microvmImage](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:microvm-image:${MicrovmImageName} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 
|  [networkConnector](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | arn:${Partition}:lambda:${Region}:${Account}:network-connector:${NetworkConnectorId} | [aws:ResourceTag/${TagKey}](#list_lambda-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Lambda
<a name="list_lambda-policy-keys"></a>

AWS Lambda defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [lambda:CodeSigningConfigArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ARN of an AWS Lambda code signing config | ARN | 
|   [lambda:EventSourceToken](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ID from a non-AWS event source configured for the AWS Lambda function | String | 
|   [lambda:FunctionArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ARN of an AWS Lambda function | ARN | 
|   [lambda:FunctionUrlAuthType](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by authorization type specified in request. Available during CreateFunctionUrlConfig, UpdateFunctionUrlConfig, DeleteFunctionUrlConfig, GetFunctionUrlConfig, ListFunctionUrlConfig, AddPermission and RemovePermission operations | String | 
|   [lambda:InvokedViaFunctionUrl](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Limits the scope of lambda:InvokeFunction action to Function URLs only. Available during AddPermission operation | Bool | 
|   [lambda:Layer](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ARN of a version of an AWS Lambda layer | ArrayOfString | 
|   [lambda:Principal](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by restricting the AWS service or account that can invoke a function | String | 
|   [lambda:SecurityGroupIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ID of security groups configured for the AWS Lambda function | ArrayOfString | 
|   [lambda:SourceFunctionArn](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ARN of the AWS Lambda function from which the request originated | ARN | 
|   [lambda:SubnetIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ID of subnets configured for the AWS Lambda function | ArrayOfString | 
|   [lambda:VpcIds](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html)  | Filters access by the ID of the VPC configured for the AWS Lambda function | String | 