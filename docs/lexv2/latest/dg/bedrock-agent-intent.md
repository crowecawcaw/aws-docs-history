# Using BedrockAgentIntent to use a Amazon Bedrock Agent in Amazon Lex V2

###### Note

Before you can take advantage of the generative AI features, you must fulfill the following prerequisites

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock") and sign up for access
   to the Anthropic Claude model you intend to use (for more information, see [Model access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md")). For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
2. Turn on the
   generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md "generative-features.md").
   You can take advantage of Amazon Bedrock Agents to handle complex workloads requested by customers without having to go
   through a comprehensive task definition process. Amazon Lex V2 offers a built-in `AMAZON.BedrockAgentIntent` that you can
   add to your bot. This intent harnesses generative AI capabilities from Amazon Bedrock by recognizing customer requests,
   analyzing them, reasoning them, and finally responding. It also has the capability to ask any follow-up questions in order to
   achieve the task needed (for example, image you defined a retail agent that can check customer’s order status. When
   the customer asks for order status, agent first requests `customerId` or associated `emailId` to retrieve the details, and finally
   responds with correct order status). You can also decide to integrate your AMAZON.BedrockAgentIntent with a Bedrock Knowledge Base
   to directly answer any customer queries.

Ensure that your IAM role has the proper permissions to access the AMAZON.BedrockAgentIntent by following the steps at Permissions for the AMAZON.BedrockAgentIntent

To take advantage of the AMAZON.BedrockAgentIntent you must have set up one of the following knowledge stores.

- Amazon Bedrock Agents – For more information, see [Creating Bedrock Agents](../../../bedrock/latest/userguide/agents.md "../../../bedrock/latest/userguide/agents.md").
- Amazon Bedrock Knowledge Base – For more information, see [Building a Knowledge Base](../../../bedrock/latest/userguide/knowledge-base-create.md "../../../bedrock/latest/userguide/knowledge-base-create.md").
  To use the AMAZON.BedrockAgentIntent, ensure that your IAM role has the proper permissions by following the steps at [Permissions needed in Lex V2 for Bedrock Agent Intent](bedrock-agent-intent-permissions.md "bedrock-agent-intent-permissions.md").

###### Topics

- [Enable Bedrock Agent Intent in the Generative AI configuration screen](bedrock-agent-intent-genai.md "bedrock-agent-intent-genai.md")
- [Enable Bedrock Agent Intent by adding a built-in intent to your bot](bedrock-agent-intent-level.md "bedrock-agent-intent-level.md")
- [Permissions needed in Lex V2 for Bedrock Agent Intent](bedrock-agent-intent-permissions.md "bedrock-agent-intent-permissions.md")
- [Sample request with session attributes](bedrock-agent-intent-sample.md "bedrock-agent-intent-sample.md")
  For more information, see [AMAZON.BedrockAgentIntent](built-in-intent-bedrockagent.md "built-in-intent-bedrockagent.md").
