# Quotas for Amazon Bedrock AgentCore

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To request a quota increase, contact AWS support.

###### Topics

- [AgentCore Runtime Service Quotas](#runtime-service-limits "#runtime-service-limits")
- [AgentCore Memory Service Quotas](#memory-limits "#memory-limits")
- [AgentCore Identity Service Quotas](#identity-service-limits "#identity-service-limits")
- [AgentCore Gateway Service Quotas](#gateway-endpoints-quotas "#gateway-endpoints-quotas")
- [AgentCore Browser Service Quotas](#browser-service-limits "#browser-service-limits")
- [AgentCore Code Interpreter Service Quotas](#code-interpreter-service-limits "#code-interpreter-service-limits")
- [AgentCore Evaluations Service Quotas](#evaluation-service-limits "#evaluation-service-limits")
- [AgentCore Policy Service Quotas](#policy-service-limits "#policy-service-limits")
- [AgentCore Resource Based Policies](#resource-based-policies-quotas "#resource-based-policies-quotas")
- [AWS Agent Registry Service Quotas](#registry-limits "#registry-limits")

## AgentCore Runtime Service Quotas

When working with AgentCore Runtime, you need to be aware of the service limits that apply to your account. These limits help ensure service stability and availability for all users.

### Resource allocation limits

The following table describes the resource allocation limits for AgentCore Runtime. You can request increases for some quotas using the Service Quotas console.

| Limit                                                            | Default Value                                                                      | Adjustable | Notes                                                           |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------- |
| Active session workloads per account                             | 1,000 in US East (N. Virginia) and US West (Oregon), and 500 in other AWS Regions. | Yes        | Can be increased via Service Quotas                             |
| Total agents per account                                         | 1,000                                                                              | Yes        | Can be increased via Service Quotas                             |
| Versions per agent                                               | 1,000                                                                              | Yes        | Can be increased via Service Quotas                             |
| Endpoints (aliases) per agent                                    | 10                                                                                 | Yes        | Can be increased via Service Quotas                             |
| Maximum size for a Docker image in an AgentCore Runtime          | 2 GB                                                                               | No         |                                                                 |
| Maximum size for a direct code deployment package (compressed)   | 250 MB                                                                             | No         | ZIP file size limit for direct code deployment                  |
| Maximum size for a direct code deployment package (uncompressed) | 750 MB                                                                             | No         | Unzipped package size limit for direct code deployment          |
| Maximum hardware allocation per session                          | 2vCPU/8GB                                                                          | No         | The maximum memory/CPU usage and allocation per Runtime session |

For more information about service quotas and how to request increases, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

### Invocation limits

The following table describes the invocation limits for AgentCore Runtime. You can request increases for some quotas using the Service Quotas console.

| Limit                             | Value      | Adjustable | Notes                                                                              |
| --------------------------------- | ---------- | ---------- | ---------------------------------------------------------------------------------- |
| Request timeout                   | 15 minutes | No         | Maximum time for synchronous requests                                              |
| Maximum payload size              | 100 MB     | No         | Maximum size for request/response payloads                                         |
| Streaming chunk size              | 10 MB      | No         | Maximum size for individual chunks                                                 |
| Streaming maximum duration        | 60 mins    | No         | Maximum time for streaming connections (Response streaming, WebSocket connections) |
| Asynchronous job maximum duration | 8 hours    | No         | Maximum execution time for asynchronous jobs                                       |
| WebSocket frame size              | 64 KB      | No         | Maximum size for individual WebSocket frames                                       |

For more information about service quotas and how to request increases, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

### Throttling limits

The following table describes the rate limits for AgentCore Runtime after which you will be throttled. You can request increases for some quotas using the Service Quotas console.

| Limit                                                                  | Value                 | Adjustable | Notes                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------- | --------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| InvokeAgentRuntime API rate, per agent, per account                    | 25 TPS                | Yes        | Transactions per second                                                                                                                                                                                                |
| InvokeAgentRuntimeCommand API rate, per agent, per account             | 25 TPS                | Yes        | Transactions per second. Additional limits: command size 1 byte–64 KB, response size up to 100 MB, timeout 1–3600 seconds (default 300), streaming chunk size up to 64 KB per event, session ID minimum 33 characters. |
| InvokeAgentRuntimeWithWebSocketStream API rate, per agent, per account | 25 TPS                | Yes        | Transactions per second                                                                                                                                                                                                |
| New sessions created rate, per endpoint (container deployment)         | 100 TPM               | Yes        | Transactions per minute                                                                                                                                                                                                |
| Direct code deploy new session rate, per endpoint                      | 25 TPS                | Yes        | Transactions per second                                                                                                                                                                                                |
| WebSocket frame rate per connection                                    | 250 frames per second | No         |                                                                                                                                                                                                                        |
| CreateAgentRuntime API rate                                            | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| CreateAgentRuntimeEndpoint API rate                                    | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| GetAgentRuntime API rate                                               | 50 TPS                | Yes        | Transactions per second                                                                                                                                                                                                |
| GetAgentRuntimeEndpoint API rate                                       | 50 TPS                | Yes        | Transactions per second                                                                                                                                                                                                |
| UpdateAgentRuntime API rate                                            | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| UpdateAgentRuntimeEndpoint API rate                                    | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| DeleteAgentRuntime API rate                                            | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| DeleteAgentRuntimeEndpoint API rate                                    | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| ListAgentRuntimes API rate                                             | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| ListAgentRuntimeEndpoints API rate                                     | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |
| ListAgentRuntimeVersions API rate                                      | 5 TPS                 | Yes        | Transactions per second                                                                                                                                                                                                |

For more information about service quotas and how to request increases, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

### Lifetime session lifecycle parameters

The following table describes the lifetime session lifecycle parameters for AgentCore Runtime:

| Phase                    | Timeout                  | Adjustable                                                                                           | Notes                                                                                                        |
| ------------------------ | ------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Idle session timeout     | 15 minutes of inactivity | Yes, through the `idleRuntimeSessionTimeout` API parameter in the `LifecycleConfiguration` data type | When this limit is reached, the execution environment is terminated and a new one is created for the session |
| Maximum session duration | 8 hrs                    | Yes, through the `maxLifetime` API parameter in the `LifecycleConfiguration` data type               |                                                                                                              |

### Session storage limits

The following table describes the limits for session storage:

| Limit                         | Value       | Adjustable | Description                             |
| ----------------------------- | ----------- | ---------- | --------------------------------------- |
| Maximum storage size          | 1 GB        | No         | Maximum total storage size per session  |
| Maximum filesystem metadata   | ~50 MB      | No         | Approximately 100,000–200,000 files     |
| Maximum directory depth       | 200 levels  | No         | Maximum nested directory depth          |
| Maximum filename length       | 255 bytes   | No         | Maximum length of a single filename     |
| Maximum symlink target length | 4,095 bytes | No         | Maximum length of a symlink target path |

## AgentCore Memory Service Quotas

The following table describes the lifetime session lifecycle parameters for AgentCore Memory:

| Limit                                                                                      | Value   | Adjustable | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------ | ------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum number of AgentCore Memory resources per AWS Region in an AWS account account      | 150     | Yes        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum number of memory strategies per AgentCore Memory resource                          | 6       | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum memory strategies per account                                                      | 900     | Yes        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum CreateMemory requests                                                              | 3       | Yes        | The maximum number of `CreateMemory` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                    |
| Maximum GetMemory requests                                                                 | 5       | Yes        | The maximum number of `GetMemory` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                       |
| Maximum DeleteMemory requests                                                              | 3       | Yes        | The maximum number of `DeleteMemory` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                    |
| Maximum ListMemories requests                                                              | 5       | Yes        | The maximum number of `ListMemories` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                    |
| Maximum UpdateMemory requests                                                              | 3       | Yes        | The maximum number of `UpdateMemory` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                    |
| Minimum EventExpirationDuration days in a CreateEvent operation                            | 7       | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum EventExpirationDuration days in a CreateEvent operation                            | 365     | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum prompt size (AppendToPrompt) for custom memory strategy (Extraction/Consolidation) | 30 KB   | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum number of messages per CreateEvent operation                                       | 100     | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum message size in a CreateEvent operation                                            | 100 KB  | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum event size in a CreateEvent operation                                              | 10 MB   | No         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum CreateEvent requests                                                               | 10      | Yes        | The maximum number of `CreateEvent` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                     |
| Maximum CreateEvent requests per actor, per session, including conversational payloads     | 5       | No         | The maximum number of `CreateEvent` requests per second, per actor, per session, including conversational payloads that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                          |
| Maximum CreateEvent requests per actor, per session, not including conversational payloads | 10      | No         | The maximum number of `CreateEvent` requests per second, per actor, per session, not including conversational payloads that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                      |
| Maximum DeleteEvent requests                                                               | 20      | Yes        | The maximum number of `DeleteEvent` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                                     |
| Maximum DeleteEvent requests per actor, per session                                        | 5       | Yes        | The maximum number of `DeleteEvent` requests per second, per actor, per session that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                             |
| Maximum RetrieveMemoryRecords requests                                                     | 30      | Yes        | The maximum number of `RetrieveMemoryRecords` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                           |
| Maximum ListMemoryRecords requests                                                         | 30      | Yes        | The maximum number of `ListMemoryRecords` requests per second that you can perform in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                                               |
| Maximum requests for all other AgentCore Memory APIs                                       | 20      | Yes        | The maximum transactions per second (TPS) that can be processed in this AWS account account in the current AWS Region for all other AgentCore Memory APIs.                                                                                                                                                                                                                                                                                                                                                              |
| Maximum number of tokens per minute for long-term memory extraction                        | 150,000 | Yes        | The maximum number of tokens per minute that can be processed for long-term memory extraction for built-in strategies in this AWS account in the current AWS Region. You can monitor token use through the [Amazon CloudWatch metric](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") named `TokenCount` in the `Bedrock-AgentCore` namespace. You can request an increase to this limit through the Service Quotas console. |
| Maximum number of tokens per minute for episodic long-term memory extraction per session   | 50,000  | No         | The per-session, tokens per minute limit that can be processed for episodic long-term memory extraction in this AWS account account in the current AWS Region.                                                                                                                                                                                                                                                                                                                                                          |

## AgentCore Identity Service Quotas

When working with AgentCore Identity, you need to be aware of the service limits that apply to your account. These limits help ensure service stability and availability for all users.

| Limit                                 | Value | Adjustable | Notes                                                                                                                              |
| ------------------------------------- | ----- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Workload identities                   | 1,000 | No         | The maximum number of workload identities that you can create in this account in the current Region.                               |
| Resource OAuth2 credential providers  | 50    | No         | The maximum number of OAuth2 credential providers for egress resources that you can create in this account in the current Region.  |
| Resource API key credential providers | 50    | No         | The maximum number of API key credential providers for egress resources that you can create in this account in the current Region. |

## AgentCore Gateway Service Quotas

This section provides information about Amazon Bedrock AgentCore Gateway endpoints and service limits.

### Endpoints

Amazon Bedrock AgentCore Gateway provides AWS Region-specific endpoints for management operations and runtime access.

The Amazon Bedrock AgentCore Gateway control plane endpoints use the following format, where you can replace `<region>` with any of the AWS Regions listed in [Supported AWS Regions](agentcore-regions.md "agentcore-regions.md").

```
bedrock-agentcore-control.<region>.amazonaws.com
```

The AgentCore Gateway URLs for runtime access have the following format:

```
https://{gateway-Id}.gateway.bedrock-agentcore.{Region}.amazonaws.com
```

Where:

- **{gateway-Id}** is the unique identifier for your gateway
- **{Region}** is the AWS Region where your gateway is deployed

Gateway ARNs have the following format:

```
arn:${Partition}:bedrock-agentcore:${Region}:${Account}:gateway/${gateway-Id}
```

The AgentCore service principal is: `bedrock-agentcore.amazonaws.com`

### Service quotas

Amazon Bedrock AgentCore Gateway has the following service quotas. You can request increases for some quotas using the Service Quotas console.

| Quota                                                                              | Default value               | Adjustable |
| ---------------------------------------------------------------------------------- | --------------------------- | ---------- |
| Number of gateways per account                                                     | 1000                        | Yes        |
| Number of targets per gateway                                                      | 100                         | Yes        |
| Number of tools per target                                                         | 1000                        | Yes        |
| Timeout for a gateway invocation                                                   | 15 minutes                  | Yes        |
| Maximum inline schema size                                                         | 1 MB                        | Yes        |
| Maximum S3 payload schema size                                                     | 10 MB                       | Yes        |
| Tool name character limit                                                          | 256 characters              | Yes        |
| CreateGateway API rate                                                             | 5 transactions per second   | Yes        |
| UpdateGateway API rate                                                             | 5 transactions per second   | Yes        |
| GetGateway API rate                                                                | 10 transactions per second  | Yes        |
| ListGateways API rate                                                              | 10 transactions per second  | Yes        |
| DeleteGateway API rate                                                             | 5 transactions per second   | Yes        |
| CreateGatewayTarget API rate                                                       | 5 transactions per second   | Yes        |
| UpdateGatewayTarget API rate                                                       | 5 transactions per second   | Yes        |
| GetGatewayTarget API rate                                                          | 10 transactions per second  | Yes        |
| ListGatewayTargets API rate                                                        | 10 transactions per second  | Yes        |
| DeleteGatewayTarget API rate                                                       | 5 transactions per second   | Yes        |
| Concurrent target operations (total of Create/Update/DeleteTarget) on same gateway | 5                           | Yes        |
| tool-call/tool-list rate at gateway level                                          | 1000 concurrent connections | Yes        |
| tool-call/tool-list rate at account level                                          | 1000 concurrent connections | Yes        |
| Search-based tool-call rate                                                        | 25 transactions per minute  | Yes        |
| Maximum tool-call/tool-list/tool-search payload size                               | 6 MB                        | Yes        |

For more information about service quotas and how to request increases, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## AgentCore Browser Service Quotas

The Browser tool has the following service quotas and considerations that apply to your account.

| Quota                                         | Default Value | Adjustable | Notes                                                      |
| --------------------------------------------- | ------------- | ---------- | ---------------------------------------------------------- |
| Concurrent active sessions per account        | 1000          | Yes        | Can be increased via support ticket                        |
| Total Browser tool configurations per account | 1000          | Yes        | Can be increased via support ticket                        |
| Hardware configuration per session            | 1vCPU/4GB     | No         | The maximum memory/CPU usage and configuration per account |

### Browser Invocation Limits

The following table describes the invocation limits for the Browser tool:

| Limit                               | Value | Adjustable | Notes                                            |
| ----------------------------------- | ----- | ---------- | ------------------------------------------------ |
| Automation stream limit per session | 1     | No         | Maximum number of automation streams per session |
| Live view stream limit per session  | 1     | No         | Maximum number of live view streams per session  |
| Asynchronous command max duration   | 8 hrs | No         | Maximum execution time for asynchronous commands |
| Disk size                           | 10 GB | No         | Maximum disk space available per session         |

### Browser Extensions Limits

The following table describes the limits for browser extensions:

| Limit                           | Value | Adjustable | Notes                         |
| ------------------------------- | ----- | ---------- | ----------------------------- |
| Maximum file size per extension | 10 MB | Yes        | Each extension ZIP file limit |
| Maximum extensions per session  | 10    | Yes        | Total extensions per session  |

### Browser Profile Limitations

The following table describes the limits for browser profiles:

| Limit                                  | Value | Adjustable | Notes                                                       |
| -------------------------------------- | ----- | ---------- | ----------------------------------------------------------- |
| Maximum size per profile               | 50 MB | Yes        | The size limit applies to cookies and localStorage in total |
| Maximum number of profiles per account | 100   | Yes        | Can be increased via support ticket                         |

### Browser Proxy Limits

The following table describes the limits for browser proxies:

| Limit                             | Value          | Adjustable | Notes                                        |
| --------------------------------- | -------------- | ---------- | -------------------------------------------- |
| Maximum proxies per session       | 5              | No         | Total external proxies in proxyConfiguration |
| Maximum domain patterns per proxy | 50             | No         | domainPatterns array per proxy               |
| Maximum total domain patterns     | 100            | No         | Across all proxies and bypass                |
| Server hostname length            | 253 characters | No         | Standard DNS limit                           |
| Domain pattern length             | 253 characters | No         | Standard DNS limit                           |

### Browser Throttling Limits

The following table describes the rate limits for the Browser tool APIs after which you will be throttled:

| Limit                                   | Value  | Adjustable | Notes                               |
| --------------------------------------- | ------ | ---------- | ----------------------------------- |
| CreateBrowser API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| GetBrowser API rate                     | 30 TPS | Yes        | Transactions per second per account |
| ListBrowsers API rate                   | 30 TPS | Yes        | Transactions per second per account |
| DeleteBrowser API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| StartBrowserSession API rate            | 30 TPS | Yes        | Transactions per second per account |
| GetBrowserSession API rate              | 30 TPS | Yes        | Transactions per second per account |
| ListBrowserSessions API rate            | 30 TPS | Yes        | Transactions per second per account |
| StopBrowserSession API rate             | 30 TPS | Yes        | Transactions per second per account |
| UpdateBrowserStream API rate            | 30 TPS | Yes        | Transactions per second per account |
| ConnectBrowserAutomationStream API rate | 30 TPS | Yes        | Transactions per second per account |
| ConnectBrowserLiveViewStream API rate   | 30 TPS | Yes        | Transactions per second per account |
| InvokeBrowser API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| SaveBrowserSessionProfile API rate      | 10 TPS | Yes        | Transactions per second per account |
| CreateBrowserProfile API rate           | 5 TPS  | Yes        | Transactions per second per account |
| GetBrowserProfile API rate              | 30 TPS | Yes        | Transactions per second per account |
| ListBrowserProfiles API rate            | 30 TPS | Yes        | Transactions per second per account |
| DeleteBrowserProfile API rate           | 5 TPS  | Yes        | Transactions per second per account |

## AgentCore Code Interpreter Service Quotas

The Code Interpreter tool has the following service quotas and considerations that apply to your account.

| Quota                                                  | Default Value | Adjustable | Notes                                                      |
| ------------------------------------------------------ | ------------- | ---------- | ---------------------------------------------------------- |
| Concurrent active sessions per account                 | 1000          | Yes        | Can be increased via support ticket                        |
| Total Code Interpreter tool configurations per account | 1000          | Yes        | Can be increased via support ticket                        |
| Hardware configuration per session                     | 2vCPU/8GB     | No         | The maximum memory/CPU usage and configuration per account |

### Code Interpreter Invocation Limits

The following table describes the invocation limits for the Code Interpreter tool:

| Limit                             | Value   | Adjustable | Notes                                            |
| --------------------------------- | ------- | ---------- | ------------------------------------------------ |
| Request timeout                   | 15 mins | No         | Maximum time for synchronous requests            |
| Max payload size                  | 100 MB  | No         | Maximum size for request/response payloads       |
| Asynchronous command max duration | 8 hrs   | No         | Maximum execution time for asynchronous commands |
| Disk size                         | 10 GB   | No         | Maximum disk space available per session         |

### Code Interpreter Throttling Limits

The following table describes the rate limits for the Code Interpreter tool APIs after which you will be throttled:

| Limit                                | Value  | Adjustable | Notes                               |
| ------------------------------------ | ------ | ---------- | ----------------------------------- |
| CreateCodeInterpreter API rate       | 5 TPS  | Yes        | Transactions per second per account |
| GetCodeInterpreter API rate          | 30 TPS | Yes        | Transactions per second per account |
| ListCodeInterpreters API rate        | 30 TPS | Yes        | Transactions per second per account |
| DeleteCodeInterpreter API rate       | 5 TPS  | Yes        | Transactions per second per account |
| StartCodeInterpreterSession API rate | 30 TPS | Yes        | Transactions per second per account |
| GetCodeInterpreterSession API rate   | 30 TPS | Yes        | Transactions per second per account |
| ListCodeInterpreterSessions API rate | 30 TPS | Yes        | Transactions per second per account |
| StopCodeInterpreterSession API rate  | 30 TPS | Yes        | Transactions per second per account |
| InvokeCodeInterpreter API rate       | 30 TPS | Yes        | Transactions per second per account |

## AgentCore Evaluations Service Quotas

The following table describes the service quotas for AgentCore Evaluations:

| Limit                                               | Default Value                                  | Adjustable                          | Note                                           |
| --------------------------------------------------- | ---------------------------------------------- | ----------------------------------- | ---------------------------------------------- |
| Input tokens per minute for built-in evaluators     | 200,000                                        | No                                  | Evaluations per minute for built-in evaluators |
| 100                                                 | No                                             | Spans per on-demand evaluation      | 1000                                           |
| No                                                  | On-demand evaluation payload size (in MB)      | 15                                  | No                                             |
| Evaluators per on-demand evaluation                 | 1                                              | No                                  | Input tokens per evaluation                    |
| 200,000                                             | No                                             | Spans evaluated per sampled session | 1000                                           |
| No                                                  | Size of all spans in a sampled session (in MB) | 15                                  | No                                             |
| Active online evaluation configurations per account | 100                                            | No                                  | Evaluators per online evaluation configuration |

## AgentCore Policy Service Quotas

When working with AgentCore Policy, you need to be aware of the service limits that apply to your account. These limits help ensure service stability and availability for all users.

### Resource limits

| Quota                                                       | Default value | Adjustable | Notes                                                             |
| ----------------------------------------------------------- | ------------- | ---------- | ----------------------------------------------------------------- |
| Policy engines per account per Region                       | 1,000         | No         |                                                                   |
| Policies per policy engine                                  | 1,000         | No         |                                                                   |
| Generated policies (7-day rolling window) per policy engine | 50,000        | No         |                                                                   |
| Maximum policy size                                         | 10 KB         | No         | Per individual policy                                             |
| Maximum total policy size per resource                      | 200 KB        | No         | Combined size of all policies per resource within a policy engine |
| Cedar schema size                                           | 100 KB        | No         | Per policy engine schema                                          |

### Throttling limits

The following table describes the rate limits for AgentCore Policy APIs after which you will be throttled.

| Limit                               | Value | Adjustable | Notes                               |
| ----------------------------------- | ----- | ---------- | ----------------------------------- |
| CreatePolicyEngine API rate         | 1 TPS | No         | Transactions per second per account |
| GetPolicyEngine API rate            | 5 TPS | No         | Transactions per second per account |
| UpdatePolicyEngine API rate         | 1 TPS | No         | Transactions per second per account |
| ListPolicyEngines API rate          | 5 TPS | No         | Transactions per second per account |
| DeletePolicyEngine API rate         | 1 TPS | No         | Transactions per second per account |
| CreatePolicy API rate               | 5 TPS | No         | Transactions per second per account |
| GetPolicy API rate                  | 5 TPS | No         | Transactions per second per account |
| UpdatePolicy API rate               | 5 TPS | No         | Transactions per second per account |
| ListPolicies API rate               | 5 TPS | No         | Transactions per second per account |
| DeletePolicy API rate               | 5 TPS | No         | Transactions per second per account |
| StartPolicyGeneration API rate      | 1 TPS | No         | Transactions per second per account |
| GetPolicyGeneration API rate        | 5 TPS | No         | Transactions per second per account |
| ListPolicyGenerations API rate      | 5 TPS | No         | Transactions per second per account |
| ListPolicyGenerationAssets API rate | 5 TPS | No         | Transactions per second per account |

## AgentCore Resource Based Policies

The following table describes the quotas for resource-based policies:

| Quota                         | Default value | Adjustable |
| ----------------------------- | ------------- | ---------- |
| Maximum policy size           | 20 KB         | No         |
| Maximum statements per policy | 100           | No         |

## AWS Agent Registry Service Quotas

### Resource limits

| Quota                                     | Default value | Adjustable | Notes |
| ----------------------------------------- | ------------- | ---------- | ----- |
| Maximum registries per account per Region | 5             | Yes        |       |

### Throttling limits

The following table describes the rate limits for AgentCore Registry APIs after which you will be throttled. You can request increases for some quotas using the Service Quotas console.

| Limit                                    | Value  | Adjustable | Notes                               |
| ---------------------------------------- | ------ | ---------- | ----------------------------------- |
| CreateRegistry API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| GetRegistry API rate                     | 5 TPS  | Yes        | Transactions per second per account |
| UpdateRegistry API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| DeleteRegistry API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| ListRegistries API rate                  | 5 TPS  | Yes        | Transactions per second per account |
| CreateRegistryRecord API rate            | 5 TPS  | Yes        | Transactions per second per account |
| GetRegistryRecord API rate               | 10 TPS | Yes        | Transactions per second per account |
| UpdateRegistryRecord API rate            | 5 TPS  | Yes        | Transactions per second per account |
| DeleteRegistryRecord API rate            | 10 TPS | Yes        | Transactions per second per account |
| ListRegistryRecords API rate             | 10 TPS | Yes        | Transactions per second per account |
| SubmitRegistryRecordForApproval API rate | 10 TPS | Yes        | Transactions per second per account |
| UpdateRegistryRecordStatus API rate      | 10 TPS | Yes        | Transactions per second per account |
| SearchRegistryRecords API rate           | 50 TPS | Yes        | Transactions per second per account |
| InvokeRegistryMcp API rate               | 50 TPS | Yes        | Transactions per second per account |
