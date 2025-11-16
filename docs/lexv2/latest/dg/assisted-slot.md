# Using assisted slot resolution to clarify slot values in Amazon Lex V2

###### Note

Before you can take advantage of the generative AI features, you must fulfill the following prerequisites

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock") and sign up for access
   to the Anthropic Claude model you intend to use (for more information, see [Model access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md")). For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
2. Turn on the
   generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md "generative-features.md").
   You can improve the accuracy of some built-in slots in your bot's conversation flow by using assisted slot resolution. Assisted slot resolution uses Amazon Bedrock large language models (LLMs) to improve recognition of some built-in slots, which results in an improved interpretation of customer responses during slot elicitation. For utterances that could not be resolved normally, Amazon Lex V2 will attempt to resolve them a second time using Amazon Bedrock.

Assisted slot resolution allows you to use the power of Amazon Bedrock foundation models to improve the accuracy of the following built-in slots:

- `AMAZON.Alphanumeric` without regex support
- `AMAZON.City`
- `AMAZON.Country`
- `AMAZON.Date`
- `AMAZON.Number`
- `AMAZON.PhoneNumber`
- `AMAZON.Confirmation`
  You can enable assisted slot resolution for any intent that uses the above listed built-in slots. Assisted slot resolution does not apply to
  custom slots or Amazon built-in slots not listed above.

You can gather data on the accuracy improvements after you enable assisted slot resolution in your Amazon Lex V2 bot by using conversation logs and metrics.

- Conversation logs - Interpretations will have the `interpretationSource` as `Bedrock`, if Amazon Bedrock was used to resolve the slot.
- CloudWatch metrics - Metrics will be published under the dimentions listed in CloudWatch metric. To learn more, see
  [Monitoring Amazon Lex with Amazon CloudWatch](../../../lex/latest/dg/monitoring-aws-lex-cloudwatch.md "../../../lex/latest/dg/monitoring-aws-lex-cloudwatch.md").
  To use the descriptive bot builder, ensure that your IAM role has the proper permissions by following the steps at [Permissions needed in Lex V2 for assisted slot resolution](assisted-slot-permissions.md "assisted-slot-permissions.md").

###### Topics

- [Examples of assisted slot resolution used in Lex V2](assisted-slot-examples.md "assisted-slot-examples.md")
- [Enable assisted slot resolution in the Generative AI configuration screen](assisted-slot-genai.md "assisted-slot-genai.md")
- [Enable assisted slot resolution in the slot settings in Lex V2](assisted-slot-level.md "assisted-slot-level.md")
- [Permissions needed in Lex V2 for assisted slot resolution](assisted-slot-permissions.md "assisted-slot-permissions.md")
