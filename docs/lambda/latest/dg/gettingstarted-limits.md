# Lambda quotas

###### Important

New AWS accounts have reduced concurrency and memory quotas for Lambda Functions and Lambda MicroVMs. AWS raises these quotas automatically based on your usage.

AWS Lambda is designed to scale rapidly to meet demand, allowing your functions to scale up to serve traffic
in your application. Lambda is designed for short-lived compute tasks that do not retain or rely upon state between
invocations. Code can run for up to 15 minutes in a single invocation and a single function can use up to
10,240 MB of memory.

It's important to understand the guardrails that are put in place to protect your account and the workloads of
other customers. Service quotas exist in all AWS services and consist of hard limits, which you cannot change,
and soft limits, which you can request increases for. By default, all new accounts are assigned a quota profile
that allows exploration of AWS services.

To see the quotas that apply to your account, navigate to the
[Service Quotas dashboard](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). Here, you can view
your service quotas, request a quota increase, and view current utilization. From here, you can drill down to a
specific AWS service, such as Lambda:

![The Service Quotas console showing Lambda quotas with current utilization.](images/application-design-figure-1.png)
The following sections list default quotas and limits in Lambda by category.

###### Topics

- [Compute and storage](#compute-and-storage "#compute-and-storage")
- [Function configuration, deployment, and execution](#function-configuration-deployment-and-execution "#function-configuration-deployment-and-execution")
- [Lambda API requests](#api-requests "#api-requests")
- [Lambda MicroVMs](#microvms-quotas "#microvms-quotas")
- [Other services](#quotas-other-services "#quotas-other-services")

## Compute and storage

Lambda sets quotas for the amount of compute and storage resources that you can use to run and store functions.
Quotas for concurrent executions and storage apply per AWS Region. Elastic network interface (ENI) quotas apply
per virtual private cloud (VPC), regardless of Region. The following quotas can be increased from their default
values. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

| Resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Default quota                                                                                                                                      | Can be increased up to                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Concurrent executions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1,000                                                                                                                                              | Tens of thousands                                                                                                                                                 |
| Storage for uploaded functions (.zip file archives) and layers using Lambda-managed storage. Each function version and layer<br>version consumes storage.<br>To avoid storage limits, you can configure your functions and layers to use [self-managed S3 code storage](configuration-self-managed-storage.md "configuration-self-managed-storage.md") instead.<br>For best practices on managing your code storage, see [Monitoring Lambda code storage](https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/code-storage "https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/code-storage") in Serverless Land. | 300 GB (unzipped)                                                                                                                                  | Not increasable. Use [self-managed S3 code storage](configuration-self-managed-storage.md "configuration-self-managed-storage.md") for storage beyond this limit. |
| Storage for functions defined as container images. These images are stored in Amazon ECR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | See [Amazon ECR service<br>quotas](../../../AmazonECR/latest/userguide/service-quotas.md "../../../AmazonECR/latest/userguide/service-quotas.md"). |                                                                                                                                                                   |
| [Elastic network interfaces per virtual private cloud<br>(VPC)](configuration-vpc.md "configuration-vpc.md")<br>NoteThis quota is shared with other services, such as Amazon Elastic File System (Amazon EFS). See [Amazon VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md").                                                                                                                                                                                                                                                                                                                                 | 500                                                                                                                                                | Thousands                                                                                                                                                         |
| Maximum running durable executions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1,000,000                                                                                                                                          | Millions                                                                                                                                                          |

For details on concurrency and how Lambda scales your function concurrency in response to traffic, see [Understanding Lambda function scaling](lambda-concurrency.md "lambda-concurrency.md").

## Function configuration, deployment, and execution

The following quotas apply to function configuration, deployment, and execution. Except as noted, they can't be changed.

###### Note

The Lambda documentation, log messages, and console use the abbreviation MB (rather than MiB) to refer to
1,024 KB.

| Resource                                                                                                      | Quota                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Function [memory allocation](configuration-memory.md "configuration-memory.md")                               | 128 MB to 10,240 MB, in 1-MB increments.<br>**Note:_<br>• Lambda allocates CPU power in proportion to the amount of memory configured. You can increase or decrease the memory and CPU power allocated to your function using the \**Memory (MB)_<br>• setting. At 1,769 MB, a function has the equivalent of one vCPU.                                                                |
| Function timeout                                                                                              | 900 seconds (15 minutes)                                                                                                                                                                                                                                                                                                                                                               |
| Function [environment variables](configuration-envvars.md "configuration-envvars.md")                         | 4 KB, for all environment variables associated with the function, in aggregate                                                                                                                                                                                                                                                                                                         |
| Function [resource-based policy](access-control-resource-based.md "access-control-resource-based.md")         | 20 KB                                                                                                                                                                                                                                                                                                                                                                                  |
| Function [layers](chapter-layers.md "chapter-layers.md")                                                      | 5 layers                                                                                                                                                                                                                                                                                                                                                                               |
| Function [concurrency scaling limit](scaling-behavior.md "scaling-behavior.md")                               | For each function, 1,000 execution environments every 10 seconds                                                                                                                                                                                                                                                                                                                       |
| [Invocation payload](lambda-invocation.md "lambda-invocation.md") (request and response)                      | 6 MB each for request and response (synchronous)<br>200 MB for each [streamed response](configuration-response-streaming.md "configuration-response-streaming.md") (synchronous)<br>1 MB (asynchronous)<br>1 MB for the total combined size of request line and header values                                                                                                          |
| Bandwidth for [streamed responses](configuration-response-streaming.md "configuration-response-streaming.md") | Uncapped for the first 6 MB of your function's response<br>For responses larger than 6 MB, 2MBps for the remainder of the response                                                                                                                                                                                                                                                     |
| [Deployment package (.zip file archive)](configuration-function-zip.md "configuration-function-zip.md") size  | 50 MB (zipped, when uploaded through the Lambda API or SDKs). Upload larger files with Amazon S3.<br>50 MB (when uploaded through the Lambda console)<br>250 MB The maximum size of the contents of a deployment package, including layers and custom runtimes. (unzipped)                                                                                                             |
| Container image settings size                                                                                 | 16 KB                                                                                                                                                                                                                                                                                                                                                                                  |
| [Container image](images-create.md "images-create.md") code package size                                      | 10 GB (maximum uncompressed image size, including all layers)                                                                                                                                                                                                                                                                                                                          |
| Test events (console editor)                                                                                  | 10                                                                                                                                                                                                                                                                                                                                                                                     |
| `/tmp` directory storage                                                                                      | Between 512 MB and 10,240 MB, in 1-MB increments                                                                                                                                                                                                                                                                                                                                       |
| File descriptors                                                                                              | 1,024<br>NoteLambda Managed Instances use a higher file descriptor limit of 4,096. For more information, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md "lambda-managed-instances-execution-environment.md").                                                                                                |
| Execution processes/threads                                                                                   | 1,024<br>NoteLambda Managed Instances use the default process and thread limits from [Bottlerocket](https://aws.amazon.com/bottlerocket/ "https://aws.amazon.com/bottlerocket/"). For more information, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md "lambda-managed-instances-execution-environment.md"). |
| Maximum number of durable operations per durable execution                                                    | 3,000<br>NoteFor more information, see [Available durable operations](durable-execution-sdk.md#durable-sdk-operations "durable-execution-sdk.md#durable-sdk-operations").                                                                                                                                                                                                              |
| Durable execution storage written in megabytes                                                                | 100 MB<br>NoteCumulative payload size persisted by durable functions per execution.<br>For more information, see [persisted data per durable operation](durable-execution-sdk.md#durable-operations-checkpoint-consumption "durable-execution-sdk.md#durable-operations-checkpoint-consumption").                                                                                      |

## Lambda API requests

The following quotas are associated with Lambda API requests.

| Resource                                                                                                                                                        | Quota                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Invocation requests per function per Region (synchronous)                                                                                                       | Each instance of your execution environment can serve up to 10 requests per second.<br>In other words, the total invocation limit is 10 times your concurrency limit. See<br>[Understanding Lambda function scaling](lambda-concurrency.md "lambda-concurrency.md").                         |
| Invocation requests per function per Region (asynchronous)                                                                                                      | Each instance of your execution environment can serve an unlimited number of requests.<br>In other words, the total invocation limit is based only on concurrency available to your<br>function. See [Understanding Lambda function scaling](lambda-concurrency.md "lambda-concurrency.md"). |
| Invocation requests per function version or alias (requests per second)                                                                                         | 10 x allocated [provisioned concurrency](configuration-concurrency.md "configuration-concurrency.md")<br>NoteThis quota applies only to functions that use provisioned concurrency.                                                                                                          |
| [GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md") API requests                                                                               | 100 requests per second. Cannot be increased.                                                                                                                                                                                                                                                |
| [GetPolicy](../api/API_GetPolicy.md "../api/API_GetPolicy.md") API requests                                                                                     | 15 requests per second. Cannot be increased.                                                                                                                                                                                                                                                 |
| [CheckpointDurableExecution](../api/API_CheckpointDurableExecution.md "../api/API_CheckpointDurableExecution.md") API requests                                  | 1,000 requests per second.                                                                                                                                                                                                                                                                   |
| [GetDurableExecution](../api/API_GetDurableExecution.md "../api/API_GetDurableExecution.md") API requests                                                       | 30 requests per second.                                                                                                                                                                                                                                                                      |
| [GetDurableExecutionHistory](../api/API_GetDurableExecutionHistory.md "../api/API_GetDurableExecutionHistory.md") API requests                                  | 15 requests per second.                                                                                                                                                                                                                                                                      |
| [GetDurableExecutionState](../api/API_GetDurableExecutionState.md "../api/API_GetDurableExecutionState.md") API requests                                        | 1,000 requests per second.                                                                                                                                                                                                                                                                   |
| [ListDurableExecutionsByFunction](../api/API_ListDurableExecutionsByFunction.md "../api/API_ListDurableExecutionsByFunction.md") API requests                   | 15 requests per second.                                                                                                                                                                                                                                                                      |
| [SendDurableExecutionCallbackFailure](../api/API_SendDurableExecutionCallbackFailure.md "../api/API_SendDurableExecutionCallbackFailure.md") API requests       | 300 requests per second.                                                                                                                                                                                                                                                                     |
| [SendDurableExecutionCallbackHeartbeat](../api/API_SendDurableExecutionCallbackHeartbeat.md "../api/API_SendDurableExecutionCallbackHeartbeat.md") API requests | 300 requests per second.                                                                                                                                                                                                                                                                     |
| [SendDurableExecutionCallbackSuccess](../api/API_SendDurableExecutionCallbackSuccess.md "../api/API_SendDurableExecutionCallbackSuccess.md") API requests       | 300 requests per second.                                                                                                                                                                                                                                                                     |
| [StopDurableExecution](../api/API_StopDurableExecution.md "../api/API_StopDurableExecution.md") API requests                                                    | 30 requests per second.                                                                                                                                                                                                                                                                      |
| Remainder of the control plane API requests (excludes invocation, GetFunction, and GetPolicy<br>requests)                                                       | 15 requests per second across all APIs (not 15 requests per second per API). Cannot be increased.                                                                                                                                                                                            |

## Lambda MicroVMs

Lambda MicroVMs sets quotas for compute, storage, and API requests. Quotas
marked as adjustable can be increased through the Service Quotas
console.

###### Note

Lambda MicroVMs support the ARM64 (AWS Graviton) architecture.

### Compute and storage

| Resource                                                          | Default quota                                                                                                                                                                                                                                                                                                                                                              | Adjustable |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Memory allocated across all MicroVMs (per account, per<br>Region) | 400 GB (that is, 200 MicroVMs at 2 GB configured memory each or 400<br>MicroVMs at 1 GB configured memory each).<br>1,024 GB in US East (N. Virginia), US West (Oregon), US East<br>(Ohio), and Asia Pacific (Tokyo) (that is, 512 MicroVMs at 2 GB configured<br>memory each or 1,024 MicroVMs at 1 GB configured memory each).<br>Burstable up to four times this quota. | Yes        |
| Maximum execution duration per MicroVM                            | 8 hours (28,800 seconds)                                                                                                                                                                                                                                                                                                                                                   | No         |

### Images and versions

| Resource                                          | Default quota                                                                                   | Adjustable |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| MicroVM images per account per Region             | 100                                                                                             | Yes        |
| Versions per MicroVM image                        | 50                                                                                              | Yes        |
| Concurrent image builds (per account, per Region) | 5<br>10 in US East (N. Virginia), US West (Oregon), US East<br>(Ohio), and Asia Pacific (Tokyo) | Yes        |

### Per-MicroVM throughput

| Resource                           | Limit                                                               | Adjustable |
| ---------------------------------- | ------------------------------------------------------------------- | ---------- |
| Concurrent connections per MicroVM | 8 (1 vCPU), 16 (2 vCPU), 32 (4 vCPU), 64 (8 vCPU), 128 (16<br>vCPU) | No         |
| Requests per second per MicroVM    | 40 (4 vCPU / 8 GB), 160 (16 vCPU / 32 GB)                           | No         |

### API rate limits

| API operation                 | Rate (TPS) | Burst | Adjustable |
| ----------------------------- | ---------- | ----- | ---------- |
| `RunMicrovm`                  | 5          | 5     | Yes        |
| `ResumeMicrovm`               | 5          | 5     | Yes        |
| `SuspendMicrovm`              | 2          | 2     | Yes        |
| `TerminateMicrovm`            | 10         | 10    | Yes        |
| `GetMicrovm`                  | 100        | 100   | Yes        |
| `CreateMicrovmAuthToken`      | 50         | 50    | Yes        |
| `CreateMicrovmShellAuthToken` | 5          | 5     | Yes        |

###### Note

TPS = transactions per second. These rate limits are per account, per
Region. Retry throttled requests using exponential backoff
with jitter.

## Other services

Quotas for other services, such as AWS Identity and Access Management (IAM), Amazon CloudFront (Lambda@Edge), and Amazon Virtual Private Cloud (Amazon VPC), can
impact your Lambda functions. For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_Amazon Web Services General Reference_, and [Invoking Lambda with events from other AWS services](lambda-services.md "lambda-services.md").

Many applications involving Lambda use multiple AWS services. Because different services
have different quotas for various features, it can be challenging to manage these quotas across
your entire application. For example, API Gateway has a default throttle limit of 10,000 requests per
second, whereas Lambda has a default concurrency limit of 1,000. Because of this mismatch, it's possible
to have more incoming requests from API Gateway that Lambda can handle. You can resolve this by requesting
a Lambda concurrency limit increase to match the expected level of traffic.

Load testing your application helps you monitor the performance of your application end-to-end
before deploying to production. During a load test, you can identify any quotas that may act as a
limiting factor for the traffic levels you expect and take action accordingly.
