# Cross-region inference in Amazon Bedrock AgentCore Memory

With cross-region inference, Amazon Bedrock AgentCore Memory will automatically select the optimal
region within your geography (as described in more detail below) to process your inference
request, maximizing available compute resources and model availability, and providing the best
customer experience.

Cross-region inference requests are kept within the AWS Regions that are part of the
geography where the data originally resides. For example, a request made within the US is kept
within the AWS Regions in the US. Although the data remains stored only in the primary
region, when using cross-region inference, your input prompts and output results may move
outside of your primary region. All data will be transmitted encrypted across Amazon's secure
network.

###### Note

There's no additional cost for using cross-region inference.

Amazon CloudWatch and AWS CloudTrail logs won't specify the AWS Region in which data inference
occurs.

If you don't want cross-region inference, you can manage your model selection using a
[built-in with overrides](memory-custom-strategy.md "memory-custom-strategy.md")
strategy.

## Supported Regions for AgentCore Memory cross-region inference

For a list of Region codes and endpoints supported in AgentCore, see [AWS Regions](agentcore-regions.md "agentcore-regions.md").
For endpoints, see
[Amazon Bedrock AgentCore endpoints and quotas](../../../general/latest/gr/bedrock_agentcore.md "../../../general/latest/gr/bedrock_agentcore.md").

| Supported AgentCore Memory geography | Inference regions                                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| United States                        | US East (N. Virginia) (us-east-1)<br>US East (Ohio) (us-east-2)<br>US West (Oregon) (us-west-2)                                                                    |
| Europe                               | Europe (Frankfurt) (eu-central-1)<br>Europe (Ireland) (eu-west-1)                                                                                                  |
| Asia Pacific                         | Asia Pacific (Tokyo) (ap-northeast-1)<br>Asia Pacific (Mumbai) (ap-south-1)<br>Asia Pacific (Singapore) (ap-southeast-1)<br>Asia Pacific (Sydney) (ap-southeast-2) |
