

# Preview availability and limitations
<a name="bedrock-managed-agents-openai-quotas-limitations"></a>

Amazon Bedrock Managed Agents, powered by OpenAI is available in preview through regional `bedrock-mantle` endpoints in US East (N. Virginia), US West (Oregon), and US East (Ohio).

## Supported workflows in this guide
<a name="bedrock-managed-agents-openai-quotas-limitations-supported-workflows-in-this-guide"></a>
+ Create, retrieve, list, and delete sessions.
+ Submit text messages and cancel the current turn.
+ Read durable items and stream progress events.
+ Execute commands on self-hosted compute or AgentCore Runtime.
+ Discover filesystem-based skills.
+ Use environment-based STDIO MCP servers.

## Preview boundaries
<a name="bedrock-managed-agents-openai-quotas-limitations-preview-boundaries"></a>


|  Area  |  Preview behavior  | 
| --- | --- | 
| Endpoint | Use `bedrock-mantle`. The BMA preview does not use the `bedrock-runtime` endpoint. | 
| Models | Use BMA-supported OpenAI models available in the target Region and account. | 
| Cross-Region inference profiles | Not supported by this BMA preview workflow. | 
| Input | The documented session input surface is text. | 
| Subagents | Not supported. | 
| Programmatic tool calling / code mode | Not included in the supported preview workflow. | 
| Dedicated turn-list and turn-retrieval APIs | Not available in the deployed preview used by these examples. Correlate turn IDs through events and items. | 
| Long-term memory | No built-in long-term memory integration. Session conversation and workspace files have separate lifecycles. | 
| Service-managed session-data KMS key | The preview does not expose a customer-managed key setting. | 
| Console | These procedures use APIs and supplied deployment examples. | 

Acceptance of a configuration field does not establish that its feature is supported for a preview workload. Use the documented surface and test compatibility before relying on additional provider APIs.

## Example configuration limits
<a name="bedrock-managed-agents-openai-quotas-limitations-example-configuration-limits"></a>

These values describe the example and its API schema. They are not a general statement of account-level service quotas.


|  Setting  |  Value  | 
| --- | --- | 
| Item-list page size | 1–100; default 20 | 
| Capability-directory entries | At most 32 unique paths | 
| Example result polling interval | 2 seconds, configurable with `BMA_POLL_INTERVAL`  | 
| Example result polling timeout | 300 seconds, configurable with `BMA_POLL_TIMEOUT`  | 
| AgentCore example idle timeout | 28,800 seconds | 
| AgentCore example maximum compute lifetime | 28,800 seconds | 

Account request limits, model capacity, token limits, and underlying resource quotas also apply. A larger polling timeout does not increase a service quota or extend an execution environment's maximum lifetime.

## Compatibility
<a name="bedrock-managed-agents-openai-quotas-limitations-compatibility"></a>

Use a compatible exec-server version and the request shapes documented for BMA. OpenAI-hosted Agents APIs and BMA do not necessarily expose the same features or change at the same time.

The public preview retains the `bedrock-mantle:CreateAgentSession` style of IAM action names shown in [security](bedrock-managed-agents-openai-security.md). When upgrading examples or client libraries, review API and permission changes together.