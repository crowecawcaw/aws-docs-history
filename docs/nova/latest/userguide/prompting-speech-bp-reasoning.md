

# Chain-of-thought for speech
<a name="prompting-speech-bp-reasoning"></a>

**Note**  
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

The [chain-of-thought reasoning technique](https://docs.aws.amazon.com/nova/latest/userguide/prompting-chain-of-thought.html) remains valuable but requires adaptation.
+ Keep reasoning chains shorter than you would for text interactions.
+ Break complex explanations into smaller conversational chunks.
+ Use verbal signposting (that is, "First point... Second point...") more explicitly than in text.

Here is an example prompt for chain of thought:

`You are a friendly assistant. The user will give you a problem. Explain your reasoning following the guidelines given in CONSTITUTION - REASONING, and summarize your decision at the end of your response, in one sentence.`

`## CONSTITUTION - REASONING `

`1. For simple questions including simple calculations or contextual tasks: Give the answer directly. No explanation is necessary, although you can offer to provide more information if the user requests it. `

`2. When faced with complex problems or decisions, think through the steps systematically before providing your answer. Break down your reasoning process when it would help user understanding.`

`3. For subjective matters or comparisons: explain your thought process step-by-step.`