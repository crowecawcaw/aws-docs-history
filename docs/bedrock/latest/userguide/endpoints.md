# Endpoints supported by Amazon Bedrock

Amazon Bedrock supports various endpoints for performing [inference](inference.md "inference.md") operations.

**Inference operations**

Amazon Bedrock supports the following primary two end points for performing inference programmatically:

| **Endpoint**                             | **Supported APIs**                                                                                                                                                                                                                                                                       | **Description**                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-mantle.{region}.api.aws`        | [Responses API](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions API](inference-chat-completions-mantle.md "inference-chat-completions-mantle.md") / [Messages API](inference-messages-api.md "inference-messages-api.md")                                                     | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the OpenAI-compatible endpoints and the Anthropic Messages API.                                                                                                                                                                                  |
| `bedrock-runtime.{region}.amazonaws.com` | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") / [Messages API](inference-messages-api.md "inference-messages-api.md") | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the InvokeModel/Converse/Chat Completions/Messages APIs. For more information, see [Amazon Bedrock Runtime API operations](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md"). |

For new applications, we recommend the `bedrock-mantle` endpoint. It supports OpenAI-compatible APIs (Responses and Chat Completions) and the Anthropic Messages API, includes built-in tool use and stateful conversation management, and lets you bring an existing OpenAI SDK codebase to Amazon Bedrock by changing only the base URL and API key. The `bedrock-runtime` endpoint remains fully supported and is the right choice when you're using the Bedrock-native InvokeModel or Converse APIs, or when the model you want isn't yet available on `bedrock-mantle`. To see which endpoint each model supports, see [Endpoint availability by models](models-endpoint-availability.md "models-endpoint-availability.md").

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

Inference capabilities| Capability | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| [Cross-region inference (geographic and global profiles)](cross-region-inference.md "cross-region-inference.md") | | |
| [Stateful conversation management](bedrock-mantle.md#bedrock-mantle-responses-state "bedrock-mantle.md#bedrock-mantle-responses-state") | | |
| [Asynchronous (long-running) inference](bedrock-mantle.md "bedrock-mantle.md") | | |
| [Client-side tool use](tool-use-client-side.md "tool-use-client-side.md") | | |
| [Server-side tool use](tool-use-server-side.md "tool-use-server-side.md") | | |
| [Pre-configured ready-to-use tools](tool-use.md "tool-use.md") | | |
| [Projects](projects.md "projects.md") | | |
| [Workspaces](workspaces.md "workspaces.md") | | |

Operational| Item | `bedrock-runtime` | `bedrock-mantle` |
| --- | --- | --- |
| AWS [SigV4](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") authentication | | |
| [Bedrock API key (also works with OpenAI SDK)](api-keys.md "api-keys.md") | | |
| [Usage attribution](cost-management.md "cost-management.md") | [IAM](cost-mgmt-iam-principal-tracking.md "cost-mgmt-iam-principal-tracking.md"), [per-request metadata tagging](cost-mgmt-request-metadata.md "cost-mgmt-request-metadata.md") | [Projects](projects.md "projects.md"), [Workspaces](workspaces.md "workspaces.md") |

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

Start with `bedrock-mantle` when you want to:

- Use the Responses API, Chat Completions API, or Messages API with stateful, multi-turn conversations.
- Bring existing OpenAI SDK code to Amazon Bedrock by changing only the base URL and API key.
- Run asynchronous or long-running inference workloads.
- Build agentic workflows with server-side tool use or pre-configured tools.
- Use [Projects (OpenAI-compatible)](projects.md "projects.md") or [Workspaces (Anthropic-compatible)](workspaces.md "workspaces.md") to isolate workloads and track cost and usage at the application level.
  Use `bedrock-runtime` when you want to:

- Continue using the Bedrock-native [InvokeModel](inference-api.md "inference-api.md") or [Converse](conversation-inference.md "conversation-inference.md") APIs.
- Use a model that isn't yet available on `bedrock-mantle`. See [Endpoint availability by models](models-endpoint-availability.md "models-endpoint-availability.md").
  Both endpoints can be used together from the same application — choose per use case.

###### Reduce data egress costs with VPC interface endpoints

If you are calling Amazon Bedrock from within a VPC, consider using [VPC interface endpoints (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md") to keep traffic within the AWS network and avoid data egress charges associated with NAT gateways or internet gateways.
