# Endpoints supported by Amazon Bedrock

Amazon Bedrock supports various endpoints for performing [inference](inference.md "inference.md") operations.

**Inference operations**

For new applications, we recommend the `bedrock-runtime` endpoint. It supports the Bedrock-native [InvokeModel](inference-api.md "inference-api.md") and [Converse](conversation-inference.md "conversation-inference.md") APIs, the OpenAI-compatible [Responses](bedrock-mantle.md#bedrock-mantle-responses "bedrock-mantle.md#bedrock-mantle-responses") and [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") APIs, and the Anthropic [Messages](inference-messages-api.md "inference-messages-api.md") API, and it is where Amazon Bedrock features such as [Guardrails](guardrails.md "guardrails.md"), [intelligent prompt routing](prompt-routing.md "prompt-routing.md"), and [cross-Region inference](cross-region-inference.md "cross-region-inference.md") are available. Amazon Bedrock also supports a second endpoint, `bedrock-mantle`, which currently offers additional capabilities such as server-side and pre-configured tool use (including [web search](web-search.md "web-search.md")), asynchronous inference with `background=true`, and creating [Projects](projects.md "projects.md") and [Workspaces](workspaces.md "workspaces.md"). To see which endpoint each model supports, see [Endpoint availability by models](models-endpoint-availability.md "models-endpoint-availability.md").

| **Endpoint**                                           | **Supported APIs**                                                                                                                                                                                                                                                                                                                                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-runtime.{region}.amazonaws.com` (recommended) | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") / [Responses API](bedrock-mantle.md#bedrock-mantle-responses "bedrock-mantle.md#bedrock-mantle-responses") / [Messages API](inference-messages-api.md "inference-messages-api.md") | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the InvokeModel/Converse/Chat Completions/Responses/Messages APIs. For more information about the Bedrock-native operations, see [Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md"). The OpenAI-compatible APIs are called on the `/openai/v1` paths of this endpoint rather than through the AWS SDKs. |
| `bedrock-mantle.{region}.api.aws`                      | [Responses API](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions API](inference-chat-completions-mantle.md "inference-chat-completions-mantle.md") / [Messages API](inference-messages-api.md "inference-messages-api.md")                                                                                                                                                                | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the OpenAI-compatible endpoints and the Anthropic Messages API.                                                                                                                                                                                                                                                                                                                                                   |

Existing applications that use `bedrock-mantle` continue to be fully supported and do not need to change. Both endpoints let you bring an existing OpenAI SDK codebase to Amazon Bedrock by changing only the base URL and API key, and both support the OpenAI-compatible Responses and Chat Completions APIs and the Anthropic Messages API.

The following tables compare what's available on each endpoint.

API support| API | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| [InvokeModel](inference-api.md "inference-api.md") | | |
| [Converse / ConverseStream](conversation-inference.md "conversation-inference.md") | | |
| [Chat Completions (OpenAI-compatible)](inference-chat-completions-mantle.md "inference-chat-completions-mantle.md") | | |
| [Responses API (OpenAI-compatible)](bedrock-mantle.md#bedrock-mantle-responses "bedrock-mantle.md#bedrock-mantle-responses") | | |
| [Messages API (Anthropic-native)](inference-messages-api.md "inference-messages-api.md") | | |

###### Note

The Messages API is available on both endpoints, but the two surfaces do not have identical feature support. In particular, [structured outputs](structured-output.md "structured-output.md") (the `output_config.format` parameter) are not supported on `bedrock-mantle` — requests that include `output_config.format` are rejected with a 400 error. To use structured outputs with Anthropic Claude models, call the Converse or InvokeModel APIs on `bedrock-runtime`.

###### Note

The Responses API is also available on both endpoints without identical feature support. On `bedrock-runtime`:

- **Requests are always synchronous.** `background=true` is rejected with a 400 error. The `store` parameter is unaffected and keeps its default of `true`, so stored, multi-turn conversations work normally.
- **Server-side tool use and pre-configured tools are not available**, including [web search](web-search.md "web-search.md"). Client-side tool use works on both endpoints.
- **Only the default project is supported.** See [Projects (OpenAI-compatible)](projects.md "projects.md").
- **A stored response belongs to the AWS Region that served it.** Retrieving, cancelling, or deleting it, and continuing the conversation with `previous_response_id`, are all handled by that Region.

Inference capabilities| Capability | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| [Cross-region inference (geographic and global profiles)](cross-region-inference.md "cross-region-inference.md") | | |
| [Stateful conversation management](bedrock-mantle.md#bedrock-mantle-responses-state "bedrock-mantle.md#bedrock-mantle-responses-state") | | |
| [Asynchronous (long-running) inference](bedrock-mantle.md "bedrock-mantle.md") | | |
| [Client-side tool use](tool-use-client-side.md "tool-use-client-side.md") | | |
| [Server-side tool use](tool-use-server-side.md "tool-use-server-side.md") | | |
| [Pre-configured ready-to-use tools](tool-use.md "tool-use.md") | | |
| [Projects](projects.md "projects.md") | Default project only | |
| [Workspaces](workspaces.md "workspaces.md") | | |

Operational| Item | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| AWS [SigV4](AmazonS3/latest/API/sig-v4-authenticating-requests.md "AmazonS3/latest/API/sig-v4-authenticating-requests.md") authentication | | |
| [Bedrock API key (also works with OpenAI SDK)](api-keys.md "api-keys.md") | | |
| [Usage attribution](cost-management.md "cost-management.md") | [IAM principal](cost-mgmt-iam-principal-tracking.md "cost-mgmt-iam-principal-tracking.md"), [per-request metadata tagging](cost-mgmt-request-metadata.md "cost-mgmt-request-metadata.md"), [application inference profiles](cost-mgmt-application-inference-profiles.md "cost-mgmt-application-inference-profiles.md") | [Projects](projects.md "projects.md"), [Workspaces](workspaces.md "workspaces.md") |

###### Note

On `bedrock-runtime`, the Responses API attributes usage by [IAM principal](cost-mgmt-iam-principal-tracking.md "cost-mgmt-iam-principal-tracking.md") only. Per-request metadata tagging and application inference profiles are not available on it — a request that names an application inference profile as its inference target is rejected with a 400 error. This does not affect cross-Region inference: the system-defined geographic and global inference profiles work normally.

Bedrock feature availability| Feature | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| [Guardrails](guardrails.md "guardrails.md") | | |
| [Prompt caching](prompt-caching.md "prompt-caching.md") | | |
| [Intelligent prompt routing](prompt-routing.md "prompt-routing.md") | | |

###### Note

Prompt caching support on `bedrock-mantle` depends on the specific model — see each model card under [Models at a glance](model-cards.md "model-cards.md") for details.

**Throughput and quota approach**

Each endpoint uses a different approach to managing throughput.

- **`bedrock-runtime`** – In many traditional multi-tenant services, the architecture is designed around per-account quotas to manage fair-share access to shared resources. This is the approach used with `bedrock-runtime`. Each model has fixed throughput quotas (RPM and TPM) that you can request increases for. For details, see [Quotas for the bedrock-runtime endpoint](quotas-runtime.md "quotas-runtime.md").
- **`bedrock-mantle`** – This endpoint is architected with advanced scheduling and work-queueing mechanisms that deliver fair-share distribution while supporting higher initial throughput limits. This design also allows `bedrock-mantle` to host a broad set of models and deliver the full breadth of capabilities available across the model catalog. In most cases, requests are served immediately. In some cases, a request may be briefly queued while in-flight workloads complete and throughput becomes available. For details, see [Quotas for the bedrock-mantle endpoint](quotas-mantle.md "quotas-mantle.md") and [Scaling and throughput best practices](scaling-throughput-best-practices.md "scaling-throughput-best-practices.md").
  **Pricing**

Per-token pricing for the same model is identical on `bedrock-runtime` and `bedrock-mantle`. Choose an endpoint based on the APIs and capabilities you need, not cost. For current pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

**When to choose each endpoint**

Start with `bedrock-runtime` when you want to:

- Call the OpenAI-compatible Responses or Chat Completions APIs, or the Anthropic Messages API.
- Use the Bedrock-native [InvokeModel](inference-api.md "inference-api.md") or [Converse](conversation-inference.md "conversation-inference.md") APIs.
- Use Amazon Bedrock features that are available only on this endpoint, such as [Guardrails](guardrails.md "guardrails.md") and [intelligent prompt routing](prompt-routing.md "prompt-routing.md").
- Use [cross-Region inference](cross-region-inference.md "cross-region-inference.md") to route requests across a geography or globally.
  Use `bedrock-mantle` when you want to:

- Build agentic workflows with server-side tool use or pre-configured tools, including [web search](web-search.md "web-search.md").
- Run asynchronous or long-running inference workloads, including Responses requests with `background=true`.
- Create [Projects (OpenAI-compatible)](projects.md "projects.md") or [Workspaces (Anthropic-compatible)](workspaces.md "workspaces.md") to isolate workloads and track cost and usage at the application level.
- Use a model that is available only on `bedrock-mantle`. See [Endpoint availability by models](models-endpoint-availability.md "models-endpoint-availability.md").
  Both endpoints can be used together from the same application — choose per use case.

###### Reduce data egress costs with VPC interface endpoints

If you are calling Amazon Bedrock from within a VPC, consider using [VPC interface endpoints (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md") to keep traffic within the AWS network and avoid data egress charges associated with NAT gateways or internet gateways.
