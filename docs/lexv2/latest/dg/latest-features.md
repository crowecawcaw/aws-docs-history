# Latest features

This topic provides information about the latest features that Amazon Lex V2 offers:

## AMAZON.BedrockAgentIntent for connecting with Bedrock Agents and Knowledge Bases

Amazon Lex V2 now provides the AMAZON.BedrockAgentIntent built-in intent to seamlessly connect your bot with Amazon Bedrock Agents and Knowledge Bases for enhanced conversational AI capabilities.

- [Documentation](built-in-intent-bedrockagent.md "built-in-intent-bedrockagent.md")

## Assisted NLU for improved intent classification and slot resolution

Amazon Lex V2 now offers Assisted NLU to improve intent classification and slot resolution using Large Language Models (LLMs) while staying within your bot's configured intents and slots.

- [Documentation](assisted-nlu.md "assisted-nlu.md")

## Custom vocabulary support for 17 additional languages

Amazon Lex V2 now supports custom vocabularies in 17 additional languages to improve speech recognition accuracy.

- [Documentation](vocab.md "vocab.md")

## QinConnect built-in intent for Amazon Connect integration

Amazon Lex V2 now provides the QinConnect built-in intent to seamlessly connect your bot with Amazon Connect for enhanced contact center experiences.

- [Documentation](building-intents-built-in.md "building-intents-built-in.md")

## AMAZON.Currency and AMAZON.Confirmation built-in slots now support all locales

Amazon Lex V2 now supports AMAZON.Currency and AMAZON.Confirmation built-in slot types in all locales, expanding beyond the previously supported English and Spanish locales.

- [Documentation](building-slot-types-built-in.md "building-slot-types-built-in.md")

## Enhanced QnA intent with Bedrock Knowledge Base and Guardrails

The QnA built-in intent for generative AI now supports Bedrock Knowledge Base and Guardrails for more secure and accurate responses.

- [Documentation](built-in-intent-qna.md "built-in-intent-qna.md")

## Support for Anthropic Claude 3 models

The QnA built-in intent for generative AI now supports Anthropic Claude 3 Haiku and Anthropic Claude 3 Sonnet models for enhanced conversational capabilities.

- [Documentation](generative-features.md "generative-features.md")

## Global resiliency for bot replication across regions

Amazon Lex V2 now offers Global resiliency to replicate your bot in a second AWS region for improved availability and disaster recovery.

- [Documentation](global-resiliency.md "global-resiliency.md")

## Regional support for AWS GovCloud (US-West)

Amazon Lex V2 is now available in AWS GovCloud (US-West).

- [Amazon Lex endpoints and quotas](../../../general/latest/gr/lex.md "../../../general/latest/gr/lex.md")

## Generative AI features for Amazon Lex V2

Amazon Lex V2 now allows you to take advantage of Amazon Bedrock's generative AI capabilities for your bot.

- Descriptive bot builder
  - [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/11/descriptive-bot-builder-generative-ai/ "https://aws.amazon.com/about-aws/whats-new/2023/11/descriptive-bot-builder-generative-ai/")
  - [Documentation](nld-bots.md "nld-bots.md")

- Assisted slot resolution
  - [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/11/assisted-slot-resolution-generative-ai/ "https://aws.amazon.com/about-aws/whats-new/2023/11/assisted-slot-resolution-generative-ai/")
  - [Documentation](assisted-slot.md "assisted-slot.md")

- Utterance generation
  - [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-lex-utterance-generation/ "https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-lex-utterance-generation/")
  - [Documentation](utterance-generation.md "utterance-generation.md")

- `AMAZON.QnAIntent` (Conversational FAQ)
  - [What's new post](https://aws.amazon.com/about-aws/whats-new/2024/03/qnaintent-amazon-lex-available/ "https://aws.amazon.com/about-aws/whats-new/2024/03/qnaintent-amazon-lex-available/")
  - [Documentation](generative-qna.md "generative-qna.md")

- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/elevate-your-self-service-assistants-with-new-generative-ai-features-in-amazon-lex "https://aws.amazon.com/blogs/machine-learning/elevate-your-self-service-assistants-with-new-generative-ai-features-in-amazon-lex")

## AMAZON.Confirmation built-in slot for Yes/No/Maybe/Don't know disambiguation.

Amazon Lex V2 now offers `AMAZON.Confimation` built-in slot to improve the accuracy of slot confirmation and
Yes/No/Maybe/Don't know responses.

- [Documentation](built-in-slots.md "built-in-slots.md")

## Measuring business performance with Analytics

Amazon Lex V2 now offers users the ability to view the performance of intents and slots on the Analytics dashboard.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/07/analytics-amazon-lex/ "https://aws.amazon.com/about-aws/whats-new/2023/07/analytics-amazon-lex/")
- [Documentation](analytics.md "analytics.md")

## Evaluating bot performance with Test workbench

Amazon Lex V2 now offers users the ability to create and run test sets to measure bot performance and improve bot metrics.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-lex-test-workbench/ "https://aws.amazon.com/about-aws/whats-new/2023/06/amazon-lex-test-workbench/")
- [Documentation](test-workbench.md "test-workbench.md")
- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/expedite-the-amazon-lex-chatbot-development-lifecycle-with-test-workbench/ "https://aws.amazon.com/blogs/machine-learning/expedite-the-amazon-lex-chatbot-development-lifecycle-with-test-workbench/")

## Vertical specific bot templates

Amazon Lex V2 now offers users pre-built bot templates with ready-to-use conversation flows along with both training data and dialog prompts, for both voice and chat modalities.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/02/lex-console-vertical-specific-bot-templates "https://aws.amazon.com/about-aws/whats-new/2023/02/lex-console-vertical-specific-bot-templates")
- [Documentation](bot-templates.md "bot-templates.md")

## Network of bots

Amazon Lex V2 now offers users the ability to combine multiple bots into a single network and the ability to route requests to the appropriate bot based on user input.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2023/02/network-bots-amazon-lex "https://aws.amazon.com/about-aws/whats-new/2023/02/network-bots-amazon-lex")
- [Documentation](network-of-bots.md "network-of-bots.md")

## Visual conversation builder

Amazon Lex V2 now offers a drag and drop conversation builder to easily design and visualize conversation paths by using intents within a rich visual environment.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-visual-conversation-builder/ "https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-visual-conversation-builder/")
- [Documentation](visual-conversation-builder.md "visual-conversation-builder.md")
- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/announcing-visual-conversation-builder-for-amazon-lex/ "https://aws.amazon.com/blogs/machine-learning/announcing-visual-conversation-builder-for-amazon-lex/")

## Composite slot type

Amazon Lex V2 now offers users the ability to combine multiple slots into a composite slot using logical expressions.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-lex-composite-slot-type/ "https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-lex-composite-slot-type/")
- [Documentation](composite-slots.md "composite-slots.md")

## Conditional branching

Amazon Lex V2 now offers users the ability to write conditions to better control the path that customers take through a conversation with your bot.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-lex-conditional-branching-simplified-dialog-management/ "https://aws.amazon.com/about-aws/whats-new/2022/08/amazon-lex-conditional-branching-simplified-dialog-management/")
- [Documentation](paths-branching.md "paths-branching.md")

## Automated chatbot designer

Amazon Lex V2 now offers users the option of automatically designing a chatbot from conversation transcripts. Read the for usage examples.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/06/amazon-lex-automated-chatbox-designer-available/ "https://aws.amazon.com/about-aws/whats-new/2022/06/amazon-lex-automated-chatbox-designer-available/")
- [Documentation](designing.md "designing.md")
- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/expedite-conversation-design-with-the-automated-chatbot-designer-in-amazon-lex/ "https://aws.amazon.com/blogs/machine-learning/expedite-conversation-design-with-the-automated-chatbot-designer-in-amazon-lex/")
- [Amazon Lex Automated Chatbot Designer page](https://aws.amazon.com/lex/chatbot-designer/ "https://aws.amazon.com/lex/chatbot-designer/")

## Runtime hints

Amazon Lex V2 now offers users the option of configuring runtime hints to improve recognition of phrases to improve elicitation of slot values.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-lex-supports-phrase-hints/ "https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-lex-supports-phrase-hints/")
- [Documentation](using-hints.md "using-hints.md")

## Custom vocabulary

Amazon Lex V2 now offers users the option of creating a custom vocabulary, a list of phrases that can include proper nouns or domain-specific words, for Amazon Lex V2 to recognize in the audio input.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-lex-supports-custom-vocabulary/ "https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-lex-supports-custom-vocabulary/")
- [Documentation](vocab.md "vocab.md")
- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/use-custom-vocabulary-in-amazon-lex-to-enhance-speech-recognition/ "https://aws.amazon.com/blogs/machine-learning/use-custom-vocabulary-in-amazon-lex-to-enhance-speech-recognition/")

## Grammar slot type

Amazon Lex V2 now offers users the ability to author grammars in XML format following the Speech Recognition Grammar Specification (SRGS) to collect information in a conversation.

- [What's new post](https://aws.amazon.com/about-aws/whats-new/2022/03/introducing-grammar-slot-type-amazon-lex/ "https://aws.amazon.com/about-aws/whats-new/2022/03/introducing-grammar-slot-type-amazon-lex/")
- [Documentation](building-srgs.md "building-srgs.md")
- [AWS Machine Learning Blog post](https://aws.amazon.com/blogs/machine-learning/interpret-caller-input-using-grammar-slot-types-in-amazon-lex/ "https://aws.amazon.com/blogs/machine-learning/interpret-caller-input-using-grammar-slot-types-in-amazon-lex/")
