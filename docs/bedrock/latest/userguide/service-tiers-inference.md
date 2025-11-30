# Service tiers for optimizing performance and cost

Amazon Bedrock offers four service tiers for model inference: Reserved, Priority, Standard, and Flex. With service tiers, you can optimize for availability, cost, and performance.

## Reserved Tier

The Reserved tier provides the ability to reserve prioritized compute capacity for your mission-critical applications that cannot tolerate any downtime. You have the flexibility to allocate different input and output tokens-per-minute capacities to match the exact requirements of your workload and control cost. When your application needs more tokens-per-minute capacity than what you reserved, the service automatically overflows to the Standard tier, ensuring uninterrupted operations. The Reserved tier targets 99.5% uptime for model response. Customers can reserve capacity for 1 month or 3 month duration. Customers pay a fixed price per 1K tokens-per-minute and are billed monthly.

To get access to the Reserved tier, please contact your AWS account team.

## Priority Tier

The Priority tier delivers the fastest response times for a price premium over standard on-demand pricing. It is best suited for mission-critical applications with customer-facing business workflows that do not warrant 24X7 capacity reservation. Priority tier does not require prior reservation. You can simply set the "service_tier" optional parameter to "priority" to avail request level prioritization. Priority tier requests are prioritized over Standard and Flex tier requests.

## Standard Tier

The Standard tier provides consistent performance for everyday AI tasks such as content generation, text analysis, and routine document processing. By default all inference requests are routed to the Standard tier when the "service_tier" parameter is missing. You can also set the "service_tier" optional parameter to "default" for your inference request to be served with Standard tier.

## Flex Tier

For workloads that can handle longer processing times, the Flex tier offers cost-effective processing for a pricing discount. This helps you optimize cost for workloads such as model evaluations, content summarization, and agentic workflows. You can set the "service_tier" optional parameter to "flex" for your inference request to be served with the Flex tier and avail the pricing discount.

## Using the service tier capability

To access the service tier capability, you can set the "service_tier" optional parameter to "reserved", "priority", "default", or "flex" while calling the Amazon Bedrock runtime API.

```
"service_tier" : "reserved | priority | default | flex"
```

Your on-demand quota for a model is shared across the "priority", "default", and "flex" service tiers. Your "reserved" tier capacity reservation is separate from your on-demand quota. The service tier configuration for a served request is visible in API response and AWS CloudTrail Events. You can also view service tier metrics in Amazon CloudWatch Metrics under ModelId, ServiceTier, and ResolvedServiceTier, where ResolvedServiceTier shows the actual tier that served your requests.

For more information about pricing, visit the [pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

Models and regions supported by the Reserved service tier:

|                  |                   |                                                                                              |                |
| ---------------- | ----------------- | -------------------------------------------------------------------------------------------- | -------------- |
| **Provider**     | **Model**         | **Model IDs**                                                                                | **Regions**    |
| Anthropic        | Claude Sonnet 4.5 | global.anthropic.claude-sonnet-4-5-20250929-v1:0us.anthropic.claude-sonnet-4-5-20250929-v1:0 | ap-northeast-1 |
| ap-northeast-2   |
| ap-northeast-3   |
| ap-southeast-1   |
| ap-southeast-2   |
| ap-south-1       |
| ap-southeast-3   |
| ap-south-2       |
| ap-southeast-4   |
| ca-central-1     |
| Europe-west-1    |
| Europe-central-1 |
| Europe-central-2 |
| Europe-north-1   |
| Europe-south-1   |
| Europe-south-2   |
| Europe-west-2    |
| Europe-west-3    |
| sa-east-1        |
| us-east-1        |
| us-east-2        |
| us-west-1        |
| us-west-2        |

###### Note

1M context length for Sonnet 4.5 is not supported by the Reserved tier.

Models and regions supported by Priority and Flex service tiers:

|                  |                                |                                 |             |
| ---------------- | ------------------------------ | ------------------------------- | ----------- |
| **Provider**     | **Model**                      | **Model ID**                    | **Regions** |
| OpenAI           | gpt-oss-120b                   | openai.gpt-oss-120b-1:0         | us-east-1   |
| us-east-2        |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-central-1     |
| eu-north-1       |
| eu-south-1       |
| eu-west-1        |
| eu-west-2        |
| sa-east-1        |
| OpenAI           | gpt-oss-20b                    | openai.gpt-oss-20b-1:0          | us-east-1   |
| us-east-2        |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-central-1     |
| eu-north-1       |
| eu-south-1       |
| eu-west-1        |
| eu-west-2        |
| sa-east-1        |
| Qwen             | Qwen3 235B A22B 2507           | qwen.qwen3-235b-a22b-2507-v1:0  | us-east-2   |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-central-1     |
| eu-north-1       |
| eu-south-1       |
| eu-west-2        |
| Qwen             | Qwen3 Coder 480B A35B Instruct | qwen.qwen3-coder-480b-a35b-v1:0 | us-east-2   |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-north-1       |
| eu-west-2        |
| Qwen             | Qwen3-Coder-30B-A3B-Instruct   | qwen.qwen3-coder-30b-a3b-v1:0   | us-east-1   |
| us-east-2        |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-central-1     |
| eu-north-1       |
| eu-south-1       |
| eu-west-1        |
| eu-west-2        |
| sa-east-1        |
| Qwen             | Qwen3 32B (dense)              | qwen.qwen3-32b-v1:0             | us-east-1   |
| us-east-2        |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-central-1     |
| eu-north-1       |
| eu-south-1       |
| eu-west-1        |
| eu-west-2        |
| sa-east-1        |
| DeepSeek         | DeepSeek-V3.1                  | deepseek.v3-v1:0                | us-east-2   |
| us-west-2        |
| ap-northeast-1   |
| ap-south-1       |
| ap-southeast-3   |
| eu-north-1       |
| eu-west-2        |
| Amazon           | Nova Premier                   | amazon.nova-premier-v1:0        | us-east-1\* |
| us-east-2\*      |
| us-west-2\*      |
| Amazon           | Nova Pro                       | amazon.nova-pro-v1:0            | us-east-1   |
| us-east-2\*      |
| us-west-1\*      |
| us-west-2\*      |
| ap-east-2\*      |
| ap-northeast-1\* |
| ap-northeast-2\* |
| ap-south-1\*     |
| ap-southeast-1\* |
| ap-southeast-2   |
| ap-southeast-3   |
| ap-southeast-4\* |
| ap-southeast-5\* |
| ap-southeast-7\* |
| eu-central-1\*   |
| eu-north-1\*     |
| eu-south-1\*     |
| eu-south-2\*     |
| eu-west-1\*      |
| eu-west-2        |
| eu-west-3\*      |
| il-central-1\*   |
| me-central-1     |

\*Model inference may be served using multiple regions.

To control access to service tiers refer [Control access to service tiers](security_iam_id-based-policy-examples-agent.md#security_iam_id-based-policy-examples-service-tiers "security_iam_id-based-policy-examples-agent.md#security_iam_id-based-policy-examples-service-tiers")
