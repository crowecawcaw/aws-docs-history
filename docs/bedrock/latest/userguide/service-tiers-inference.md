# Service tiers for optimizing performance and cost

Amazon Bedrock offers three service tiers for model inference: Priority, Standard, and Flex. The Priority tier delivers the fastest response times for a price premium over standard on-demand pricing. It is best suited for mission-critical applications like customer-facing chatbots and real-time language translation services. The Standard tier provides consistent performance for everyday AI tasks, ideal for content generation, text analysis, and routine document processing. For workloads that can handle longer processing times, the Flex tier offers cost-effective processing for a pricing discount, perfect for model evaluations, content summarization, agentic workflows.

Accessing the service tier capability requires no additional setup, allowing for immediate enhancement of existing applications with price/performance optimization. You can set the "service_tier" optional parameter to "priority", "default", or "flex" while calling the Amazon Bedrock runtime API. If you select "default" as your invocation option, your requests will be served by standard inference. By default all requests are routed to through standard inference.

```
"service_tier" : "priority | default | flex"
```

Your on-demand quota for a model is shared across all service tiers. The service tier configuration for a served request is visible in API response and AWS CloudTrail Events. You can also view metrics for service tiers in Amazon CloudWatch Metrics under "model-id+priority" and "model-id+flex".

For more information about pricing, visit the [pricing page](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

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
