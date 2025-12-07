# Quotas for Amazon Bedrock AgentCore

Your AWS account has default quotas, formerly referred to as limits, for
each AWS service. Unless otherwise noted, each quota is Region-specific. You
can request increases for some quotas, and other quotas cannot be increased.

To request a quota increase, contact AWS support.

###### Topics

- [AgentCore Runtime Service Quotas](#runtime-service-limits "#runtime-service-limits")
- [AgentCore Memory Service Quotas](#memory-limits "#memory-limits")
- [AgentCore Identity Service Quotas](#identity-service-limits "#identity-service-limits")
- [AgentCore Gateway Service Quotas](#gateway-endpoints-quotas "#gateway-endpoints-quotas")
- [AgentCore Browser Service Quotas](#browser-service-limits "#browser-service-limits")
- [AgentCore Code Interpreter Service
  Quotas](#code-interpreter-service-limits "#code-interpreter-service-limits")
- [AgentCore Evaluations Service Quotas](#evaluation-service-limits "#evaluation-service-limits")
- [AgentCore Resource Based Policies](#resource-based-policies-quotas "#resource-based-policies-quotas")

## AgentCore Runtime Service Quotas

When working with AgentCore Runtime, you need to be aware of the service limits that
apply to your account. These limits help ensure service stability and availability for
all users.

### Resource allocation limits

The following table describes the resource allocation limits for
AgentCore Runtime:

| Resource allocation limits                                          | Limit                                                                                 | Default Value | Adjustable                                                         | Notes |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------ | ----- |
| Active session workloads per account                                | 1,000 in US East (N. Virginia) and US West (Oregon), and 500 in<br>other AWS Regions. | Yes           | Can be increased via support ticket                                |
| Total agents per account                                            | 1,000                                                                                 | Yes           | Can be increased via support ticket                                |
| Versions per agent                                                  | 1,000                                                                                 | Yes           | Inactive versions deleted after 45 days                            |
| Endpoints (aliases) per agent                                       | 10                                                                                    | Yes           | Can be increased via support ticket                                |
| Maximum size for a Docker image in an AgentCore Runtime             | 1 GB                                                                                  | No            |                                                                    |
| Maximum size for a direct code deployment package<br>(compressed)   | 250 MB                                                                                | No            | ZIP file size limit for direct code deployment                     |
| Maximum size for a direct code deployment package<br>(uncompressed) | 750 MB                                                                                | No            | Unzipped package size limit for direct code deployment             |
| Maximum hardware allocation per session                             | 2vCPU/8GB                                                                             | No            | The maximum memory/CPU usage and allocation per Runtime<br>session |

### Invocation limits

The following table describes the invocation limits for AgentCore Runtime:

| Invocation limits                 | Limit           | Value | Adjustable                                   | Notes |
| --------------------------------- | --------------- | ----- | -------------------------------------------- | ----- |
| Request timeout                   | 15 minutes      | No    | Maximum time for synchronous requests        |
| Maximum payload size              | 100 MB          | No    | Maximum size for request/response payloads   |
| Streaming chunk size              | 10 MB           | No    | Maximum size for individual chunks           |
| Streaming maximum duration        | 60 mins         | No    | Maximum time for streaming connections       |
| Asynchronous job maximum duration | 8 hours         | No    | Maximum execution time for asynchronous jobs |
| Invocations per second            | 25 per endpoint | Yes   | Rate limit for API calls                     |
| WebSocket frame size              | 16 KB           | No    | Maximum size for individual WebSocket frames |

### Throttling limits

The following table describes the rate limits for AgentCore Runtime after which you
will be throttled:

| Throttling limits                                                         | Limit                 | Value | Adjustable              | Notes |
| ------------------------------------------------------------------------- | --------------------- | ----- | ----------------------- | ----- |
| InvokeAgentRuntime API rate, per agent, per account                       | 25 TPS                | Yes   | Transactions per second |
| InvokeAgentRuntimeWithWebSocketStream API rate, per agent, per<br>account | 25 TPS                | Yes   | Transactions per second |
| New sessions created rate, per endpoint (container<br>deployment)         | 100 TPM               | Yes   | Transactions per minute |
| Direct code deploy new session rate, per endpoint                         | 25 TPS                | Yes   | Transactions per second |
| WebSocket frame rate per connection                                       | 250 frames per second | No    |                         |
| CreateAgentRuntime API rate                                               | 5 TPS                 | Yes   | Transactions per second |
| CreateAgentRuntimeEndpoint API rate                                       | 5 TPS                 | Yes   | Transactions per second |
| GetAgentRuntime API rate                                                  | 50 TPS                | Yes   | Transactions per second |
| GetAgentRuntimeEndpoint API rate                                          | 50 TPS                | Yes   | Transactions per second |
| UpdateAgentRuntime API rate                                               | 5 TPS                 | Yes   | Transactions per second |
| UpdateAgentRuntimeEndpoint API rate                                       | 5 TPS                 | Yes   | Transactions per second |
| DeleteAgentRuntime API rate                                               | 5 TPS                 | Yes   | Transactions per second |
| DeleteAgentRuntimeEndpoint API rate                                       | 5 TPS                 | Yes   | Transactions per second |
| ListAgentRuntimes API rate                                                | 5 TPS                 | Yes   | Transactions per second |
| ListAgentRuntimeEndpoints API rate                                        | 5 TPS                 | Yes   | Transactions per second |
| ListAgentRuntimeVersions API rate                                         | 5 TPS                 | Yes   | Transactions per second |

### Lifetime session lifecycle parameters

The following table describes the lifetime session lifecycle parameters for
AgentCore Runtime:

| Lifetime session lifecycle parameters | Phase                    | Timeout                                                                                                    | Adjustable                                                                                                      | Notes |
| ------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----- |
| Idle session timeout                  | 15 minutes of inactivity | Yes, through the `idleRuntimeSessionTimeout` API<br>parameter in the `LifecycleConfiguration` data<br>type | When this limit is reached, the execution environment is<br>terminated and a new one is created for the session |
| Maximum session duration              | 8 hrs                    | Yes, through the `maxLifetime` API parameter in the<br>`LifecycleConfiguration` data type                  |                                                                                                                 |

## AgentCore Memory Service Quotas

The following table describes the lifetime session lifecycle parameters for
AgentCore Memory:

| AgentCore Memory limits                                                                       | Limit   | Value | Adjustable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes |
| --------------------------------------------------------------------------------------------- | ------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Maximum number of AgentCore Memory resources per AWS Region in an<br>AWS account account      | 50      | Yes   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum number of memory strategies per AgentCore Memory<br>resource                          | 6       | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Minimum EventExpirationDuration days in a CreateEvent<br>operation                            | 7       | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum EventExpirationDuration days in a CreateEvent<br>operation                            | 365     | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum prompt size (AppendToPrompt) for custom memory strategy<br>(Extraction/Consolidation) | 30 KB   | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum number of messages per CreateEvent operation                                          | 100     | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum message size in a CreateEvent operation                                               | 9 KB    | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum event size in a CreateEvent operation                                                 | 10 MB   | No    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Maximum CreateEvent requests                                                                  | 10      | Yes   | The maximum number of `CreateEvent` requests per second<br>that you can perform in this AWS account account in the current<br>AWS Region.                                                                                                                                                                                                                                                                                                                                                                                              |
| Maximum CreateEvent requests per actor, per session, including<br>conversational payloads     | 0.25    | No    | The maximum number of `CreateEvent` requests per second,<br>per actor, per session, including conversational payloads that you can<br>perform in this AWS account account in the current<br>AWS Region.                                                                                                                                                                                                                                                                                                                                |
| Maximum CreateEvent requests per actor, per session, not including<br>conversational payloads | 10      | No    | The maximum number of `CreateEvent` requests per second,<br>per actor, per session, not including conversational payloads that you<br>can perform in this AWS account account in the current<br>AWS Region.                                                                                                                                                                                                                                                                                                                            |
| Maximum RetrieveMemoryRecords requests                                                        | 20      | Yes   | The maximum number of `RetrieveMemoryRecords` requests per<br>second that you can perform in this AWS account account in the current<br>AWS Region.                                                                                                                                                                                                                                                                                                                                                                                    |
| Maximum requests for all other AgentCore Memory APIs                                          | 20      | Yes   | The maximum transactions per second (TPS) that can be processed in<br>this AWS account account in the current AWS Region for all other<br>AgentCore Memory APIs.                                                                                                                                                                                                                                                                                                                                                                       |
| Maximum number of tokens per minute for long-term memory<br>extraction                        | 150,000 | Yes   | The maximum number of tokens per minute that can be processed for<br>long-term memory extraction for built-in strategies in this<br>AWS account in the current AWS Region. You can monitor token use<br>through the [Amazon CloudWatch metric](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") named `TokenCount` in the<br>`Bedrock-AgentCore` namespace. You can request an<br>increase to this limit through the Service Quotas console. |

## AgentCore Identity Service Quotas

When working with AgentCore Identity, you need to be aware of the service limits that apply to
your account. These limits help ensure service stability and availability for all
users.

| AgentCore Identity Limits             | Limit | Value | Adjustable                                                                                                                               | Notes |
| ------------------------------------- | ----- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Workload identities                   | 1,000 | No    | The maximum number of workload identities that you can create in this<br>account in the current Region.                                  |
| Resource OAuth2 credential providers  | 50    | No    | The maximum number of OAuth2 credential providers for egress<br>resources that you can create in this account in the current<br>Region.  |
| Resource API key credential providers | 50    | No    | The maximum number of API key credential providers for egress<br>resources that you can create in this account in the current<br>Region. |

## AgentCore Gateway Service Quotas

This section provides information about Amazon Bedrock AgentCore Gateway endpoints and service
limits.

### Endpoints

Amazon Bedrock AgentCore Gateway provides AWS Region-specific endpoints for management operations
and runtime access.

The Amazon Bedrock AgentCore Gateway control plane endpoints use the following format, where you can
replace `<region>` with any of the AWS Regions
listed in [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").

```
bedrock-agentcore-control.`<region>`.amazonaws.com
```

The AgentCore Gateway URLs for runtime access have the following format:

```
https://{gateway-Id}.gateway.bedrock-agentcore.{Region}.amazonaws.com
```

Where:

- **{gateway-Id}** is the unique identifier for
  your gateway
- **{Region}** is the AWS Region where your
  gateway is deployed

Gateway ARNs have the following format:

```
arn:${Partition}:bedrock-agentcore:${Region}:${Account}:gateway/${gateway-Id}
```

The AgentCore service principal is:
`bedrock-agentcore.amazonaws.com`

### Service quotas

Amazon Bedrock AgentCore Gateway has the following service quotas. You can request increases for
some quotas using the Service Quotas console.

| Amazon Bedrock AgentCore Gateway service quotas                                       | Quota                      | Default value | Adjustable |
| ------------------------------------------------------------------------------------- | -------------------------- | ------------- | ---------- |
| Number of gateways per account                                                        | 1000                       | Yes           |
| Number of targets per gateway                                                         | 100                        | Yes           |
| Number of tools per target                                                            | 1000                       | Yes           |
| Timeout for a gateway invocation                                                      | 5 minutes                  | Yes           |
| Maximum inline schema size                                                            | 1 MB                       | Yes           |
| Maximum S3 payload schema size                                                        | 10 MB                      | Yes           |
| Tool name character limit                                                             | 256 characters             | Yes           |
| CreateGateway API rate                                                                | 5 transactions per second  | Yes           |
| UpdateGateway API rate                                                                | 5 transactions per second  | Yes           |
| GetGateway API rate                                                                   | 10 transactions per second | Yes           |
| ListGateways API rate                                                                 | 10 transactions per second | Yes           |
| DeleteGateway API rate                                                                | 5 transactions per second  | Yes           |
| CreateGatewayTarget API rate                                                          | 5 transactions per second  | Yes           |
| UpdateGatewayTarget API rate                                                          | 5 transactions per second  | Yes           |
| GetGatewayTarget API rate                                                             | 10 transactions per second | Yes           |
| ListGatewayTargets API rate                                                           | 10 transactions per second | Yes           |
| DeleteGatewayTarget API rate                                                          | 5 transactions per second  | Yes           |
| Concurrent target operations (total of<br>Create/Update/DeleteTarget) on same gateway | 5                          | Yes           |
| tool-call/tool-list rate at gateway level                                             | 50 concurrent connections  | Yes           |
| tool-call/tool-list rate at account level                                             | 50 concurrent connections  | Yes           |
| Search-based tool-call rate                                                           | 25 transactions per minute | Yes           |
| Maximum tool-call/tool-list/tool-search payload size                                  | 6 MB                       | Yes           |

For more information about service quotas and how to request increases, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
Guide_.

## AgentCore Browser Service Quotas

The Browser tool has the following service quotas and considerations that apply to
your account.

| Browser service quotas                                    | Quota     | Default Value | Adjustable                                                 | Notes |
| --------------------------------------------------------- | --------- | ------------- | ---------------------------------------------------------- | ----- |
| Concurrent active sessions per account for browser and CI | 1000      | Yes           | Can be increased via support ticket                        |
| Total Browser tool configurations per account             | 100       | Yes           | Can be increased via support ticket                        |
| Hardware configuration per session                        | 1vCPU/4GB | No            | The maximum memory/CPU usage and configuration per account |

### Browser Invocation Limits

The following table describes the invocation limits for the Browser tool:

| Browser invocation limits           | Limit | Value | Adjustable                                       | Notes |
| ----------------------------------- | ----- | ----- | ------------------------------------------------ | ----- |
| Automation stream limit per session | 1     | No    | Maximum number of automation streams per session |
| Live view stream limit per session  | 1     | No    | Maximum number of live view streams per session  |
| Asynchronous command max duration   | 8 hrs | No    | Maximum execution time for asynchronous commands |
| Disk size                           | 10 GB | No    | Maximum disk space available per session         |

## AgentCore Code Interpreter Service

Quotas

The Code Interpreter tool has the following service quotas and considerations that
apply to your account.

| Code Interpreter service quotas                        | Quota     | Default Value | Adjustable                                                 | Notes |
| ------------------------------------------------------ | --------- | ------------- | ---------------------------------------------------------- | ----- |
| Concurrent active sessions per account                 | 500       | Yes           | Can be increased via support ticket                        |
| Total Code Interpreter tool configurations per account | 100       | Yes           | Can be increased via support ticket                        |
| Hardware configuration per session                     | 2vCPU/8GB | No            | The maximum memory/CPU usage and configuration per account |

### Code Interpreter Invocation Limits

The following table describes the invocation limits for the Code Interpreter
tool:

| Code Interpreter invocation limits | Limit   | Value | Adjustable                                       | Notes |
| ---------------------------------- | ------- | ----- | ------------------------------------------------ | ----- |
| Request timeout                    | 15 mins | No    | Maximum time for synchronous requests            |
| Max payload size                   | 100 MB  | No    | Maximum size for request/response payloads       |
| Invocations per second             | 3       | No    | Rate limit for API calls per session             |
| Asynchronous command max duration  | 8 hrs   | No    | Maximum execution time for asynchronous commands |
| Disk size                          | 10 GB   | No    | Maximum disk space available per session         |

## AgentCore Evaluations Service Quotas

The following table describes the service quotas for AgentCore Evaluations:

| AgentCore Evaluations service quotas                | Limit   | Default Value | Adjustable | Note |
| --------------------------------------------------- | ------- | ------------- | ---------- | ---- |
| Input tokens per minute for built-in evaluators     | 200,000 | No            |
| Evaluations per minute for built-in evaluators      | 100     | No            |
| Spans per on-demand evaluation                      | 1000    | No            |
| On-demand evaluation payload size (in MB)           | 15      | No            |
| Evaluators per on-demand evaluation                 | 1       | No            |
| Input tokens per evaluation                         | 200,000 | No            |
| Spans evaluated per sampled session                 | 1000    | No            |
| Size of all spans in a sampled session (in MB)      | 15      | No            |
| Active online evaluation configurations per account | 100     | No            |
| Evaluators per online evaluation configuration      | 10      | No            |

## AgentCore Resource Based Policies

The following table describes the quotas for resource-based policies:

| Resource-based policies quotas | Quota | Default value | Adjustable |
| ------------------------------ | ----- | ------------- | ---------- |
| Maximum policy size            | 20 KB | No            |
| Maximum statements per policy  | 100   | No            |
