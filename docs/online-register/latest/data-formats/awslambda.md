

# Data retrieval APIs for AWS Lambda
<a name="awslambda"></a>

AWS Lambda provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="lambda-GetAccountSettings"></a>[GetAccountSettings](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAccountSettings.html) | View details about an account's limits and usage in an AWS Region | Read | 
| <a name="lambda-GetAlias"></a>[GetAlias](https://docs.aws.amazon.com/lambda/latest/dg/API_GetAlias.html) | View details about an AWS Lambda function alias | Read | 
| <a name="lambda-GetCapacityProvider"></a>[GetCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_GetCapacityProvider.html) | View details about an AWS Lambda capacity provider | Read | 
| <a name="lambda-GetCodeSigningConfig"></a>[GetCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetCodeSigningConfig.html) | View details about an AWS Lambda code signing config | Read | 
| <a name="lambda-GetDurableExecution"></a>[GetDurableExecution](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecution.html) | View details of an AWS Lambda durable execution | Read | 
| <a name="lambda-GetDurableExecutionHistory"></a>[GetDurableExecutionHistory](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecutionHistory.html) | View execution history of an AWS Lambda durable execution | Read | 
| <a name="lambda-GetDurableExecutionState"></a>[GetDurableExecutionState](https://docs.aws.amazon.com/lambda/latest/dg/API_GetDurableExecutionState.html) | View current state of an AWS Lambda durable execution | Read | 
| <a name="lambda-GetEventSourceMapping"></a>[GetEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_GetEventSourceMapping.html) | View details about an AWS Lambda event source mapping | Read | 
| <a name="lambda-GetFunction"></a>[GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html) | View details about an AWS Lambda function | Read | 
| <a name="lambda-GetFunctionCodeSigningConfig"></a>[GetFunctionCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionCodeSigningConfig.html) | View the code signing config arn attached to an AWS Lambda function | Read | 
| <a name="lambda-GetFunctionConcurrency"></a>[GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConcurrency.html) | View details about the reserved concurrency configuration for a function | Read | 
| <a name="lambda-GetFunctionConfiguration"></a>[GetFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html) | View details about the version-specific settings of an AWS Lambda function or version | Read | 
| <a name="lambda-GetFunctionEventInvokeConfig"></a>[GetFunctionEventInvokeConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionEventInvokeConfig.html) | View the configuration for asynchronous invocation for a function, version, or alias | Read | 
| <a name="lambda-GetFunctionRecursionConfig"></a>[GetFunctionRecursionConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionRecursionConfig.html) | View the recursion configuration of an AWS Lambda function | Read | 
| <a name="lambda-GetFunctionScalingConfig"></a>[GetFunctionScalingConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionScalingConfig.html) | View the scaling configuration of an AWS Lambda function running on a capacity provider | Read | 
| <a name="lambda-GetFunctionUrlConfig"></a>[GetFunctionUrlConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionUrlConfig.html) | Read function url configuration for a Lambda function | Read | 
| <a name="lambda-GetLayerVersion"></a>[GetLayerVersion](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersion.html) | View details about a version of an AWS Lambda layer. Note this action also supports GetLayerVersionByArn API | Read | 
| <a name="lambda-GetLayerVersionPolicy"></a>[GetLayerVersionPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetLayerVersionPolicy.html) | View the resource-based policy for a version of an AWS Lambda layer | Read | 
| <a name="lambda-GetMicrovm"></a>[GetMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovm.html) | View information about an AWS Lambda MicroVM | Read | 
| <a name="lambda-GetMicrovmImage"></a>[GetMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImage.html) | View information about an AWS Lambda MicroVM image | Read | 
| <a name="lambda-GetMicrovmImageBuild"></a>[GetMicrovmImageBuild](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImageBuild.html) | View information about a build of an AWS Lambda MicroVM image version | Read | 
| <a name="lambda-GetMicrovmImageVersion"></a>[GetMicrovmImageVersion](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_GetMicrovmImageVersion.html) | View information about a version of an AWS Lambda MicroVM image | Read | 
| <a name="lambda-GetNetworkConnector"></a>[GetNetworkConnector](https://docs.aws.amazon.com/lambda/latest/dg/API_GetNetworkConnector.html) | View details about an AWS Lambda network connector | Read | 
| <a name="lambda-GetPolicy"></a>[GetPolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetPolicy.html) | View the resource-based policy for an AWS Lambda function, version, or alias | Read | 
| <a name="lambda-GetProvisionedConcurrencyConfig"></a>[GetProvisionedConcurrencyConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetProvisionedConcurrencyConfig.html) | View the provisioned concurrency configuration for an AWS Lambda function's alias or version | Read | 
| <a name="lambda-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/lambda/latest/dg/API_GetResourcePolicy.html) | View a policy for an AWS Lambda resource | Read | 
| <a name="lambda-GetRuntimeManagementConfig"></a>[GetRuntimeManagementConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_GetRuntimeManagementConfig.html) | View the runtime management configuration of an AWS Lambda function | Read | 
| <a name="lambda-ListAliases"></a>[ListAliases](https://docs.aws.amazon.com/lambda/latest/dg/API_ListAliases.html) | Retrieve a list of aliases for an AWS Lambda function | List | 
| <a name="lambda-ListCapacityProviders"></a>[ListCapacityProviders](https://docs.aws.amazon.com/lambda/latest/dg/API_ListCapacityProviders.html) | Retrieve a list of AWS Lambda capacity providers | List | 
| <a name="lambda-ListCodeSigningConfigs"></a>[ListCodeSigningConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListCodeSigningConfigs.html) | Retrieve a list of AWS Lambda code signing configs | List | 
| <a name="lambda-ListDurableExecutionsByFunction"></a>[ListDurableExecutionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_ListDurableExecutionsByFunction.html) | Retrieve a list of AWS Lambda durable executions of an AWS Lambda function | List | 
| <a name="lambda-ListEventSourceMappings"></a>[ListEventSourceMappings](https://docs.aws.amazon.com/lambda/latest/dg/API_ListEventSourceMappings.html) | Retrieve a list of AWS Lambda event source mappings | List | 
| <a name="lambda-ListFunctionEventInvokeConfigs"></a>[ListFunctionEventInvokeConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionEventInvokeConfigs.html) | Retrieve a list of configurations for asynchronous invocation for a function | List | 
| <a name="lambda-ListFunctionUrlConfigs"></a>[ListFunctionUrlConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionUrlConfigs.html) | Read function url configurations for a function | List | 
| <a name="lambda-ListFunctionVersionsByCapacityProvider"></a>[ListFunctionVersionsByCapacityProvider](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionVersionsByCapacityProvider.html) | Retrieve a list of AWS Lambda function versions by the capacity provider assigned | List | 
| <a name="lambda-ListFunctions"></a>[ListFunctions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctions.html) | Retrieve a list of AWS Lambda functions, with the version-specific configuration of each function | List | 
| <a name="lambda-ListFunctionsByCodeSigningConfig"></a>[ListFunctionsByCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/dg/API_ListFunctionsByCodeSigningConfig.html) | Retrieve a list of AWS Lambda functions by the code signing config assigned  | List | 
| <a name="lambda-ListLayerVersions"></a>[ListLayerVersions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayerVersions.html) | Retrieve a list of versions of an AWS Lambda layer | List | 
| <a name="lambda-ListLayers"></a>[ListLayers](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayers.html) | Retrieve a list of AWS Lambda layers, with details about the latest version of each layer | List | 
| <a name="lambda-ListManagedMicrovmImageVersions"></a>[ListManagedMicrovmImageVersions](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListManagedMicrovmImageVersions.html) | Retrieve a list of versions for a managed AWS Lambda MicroVM image | List | 
| <a name="lambda-ListManagedMicrovmImages"></a>[ListManagedMicrovmImages](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListManagedMicrovmImages.html) | Retrieve a list of managed AWS Lambda MicroVM images | List | 
| <a name="lambda-ListMicrovmImageBuilds"></a>[ListMicrovmImageBuilds](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImageBuilds.html) | Retrieve a list of builds for an AWS Lambda MicroVM image version | List | 
| <a name="lambda-ListMicrovmImageVersions"></a>[ListMicrovmImageVersions](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImageVersions.html) | Retrieve a list of versions for an AWS Lambda MicroVM image | List | 
| <a name="lambda-ListMicrovmImages"></a>[ListMicrovmImages](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImages.html) | Retrieve a list of AWS Lambda MicroVM images | List | 
| <a name="lambda-ListMicrovms"></a>[ListMicrovms](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovms.html) | Retrieve a list of AWS Lambda MicroVMs | List | 
| <a name="lambda-ListNetworkConnectors"></a>[ListNetworkConnectors](https://docs.aws.amazon.com/lambda/latest/dg/API_ListNetworkConnectors.html) | Retrieve a list of AWS Lambda network connectors | List | 
| <a name="lambda-ListProvisionedConcurrencyConfigs"></a>[ListProvisionedConcurrencyConfigs](https://docs.aws.amazon.com/lambda/latest/dg/API_ListProvisionedConcurrencyConfigs.html) | Retrieve a list of provisioned concurrency configurations for an AWS Lambda function | List | 
| <a name="lambda-ListTags"></a>[ListTags](https://docs.aws.amazon.com/lambda/latest/dg/API_ListTags.html) | Retrieve a list of tags for an AWS Lambda function, event source mapping, capacity provider, code signing configuration, network connector or MicroVM image resource | Read | 
| <a name="lambda-ListVersionsByFunction"></a>[ListVersionsByFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_ListVersionsByFunction.html) | Retrieve a list of versions for an AWS Lambda function | List | 