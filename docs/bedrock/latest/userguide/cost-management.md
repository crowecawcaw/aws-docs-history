# Managing Amazon Bedrock costs

With Amazon Bedrock, you can attribute inference costs to specific users, teams, and applications, set budgets to prevent cost overruns, and analyze your usage through AWS billing tools. Amazon Bedrock supports several cost attribution methods that you can combine. For example, use IAM principal attribution for per-user visibility alongside projects for per-application tagging.

## Choosing an approach

The cost attribution method you choose depends on which Amazon Bedrock APIs you use and what level of granularity you need.

| I want to attribute costs by...                 | Use...                                                                                                                      | Supported APIs                                                                                                                                                                                                   | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| Identity (IAM users, IAM roles, and federation) | [IAM principal attribution](cost-mgmt-iam-principal-tracking.md "cost-mgmt-iam-principal-tracking.md")                      | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") | Yes               | No               |
| Application or team with tags                   | [Projects](cost-mgmt-projects.md "cost-mgmt-projects.md") (Recommended)                                                     | [Responses](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions](bedrock-mantle.md "bedrock-mantle.md")                                                                                                   | No                | Yes              |
| Application or team with tags                   | [Application inference profiles](cost-mgmt-application-inference-profiles.md "cost-mgmt-application-inference-profiles.md") | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") | Yes               | No               |

## How Amazon Bedrock pricing works

Amazon Bedrock costs are driven by model inference. Each API call processes tokens, which are units of text that the model reads and generates. Your cost depends on:

- **Model.** Different models have different per-token rates.
- **Token type.** Input tokens, output tokens, cache read tokens, and cache write tokens are each priced separately.
- **Routing.** Cross-region inference has different pricing than in-region requests.
- **Inference tier.** On-demand, provisioned throughput, and batch inference each have different pricing structures. For more information, see [Capacity and Performance](capacity-limits-cost-optimization.md "capacity-limits-cost-optimization.md").

For current pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

For guidance on optimizing costs by choosing the right tier, see [Capacity and Performance](capacity-limits-cost-optimization.md "capacity-limits-cost-optimization.md").
