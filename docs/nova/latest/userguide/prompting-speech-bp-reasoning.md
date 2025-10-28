# Chain-of-thought for speech

The [chain-of-thought reasoning technique](prompting-chain-of-thought.md "prompting-chain-of-thought.md") remains valuable but requires adaptation.

- Keep reasoning chains shorter than you would for text interactions.
- Break complex explanations into smaller conversational chunks.
- Use verbal signposting (that is, "First point... Second point...") more explicitly than in text.
  Here is an example prompt for chain of thought:

`You are a friendly assistant. The user will give you a problem. Explain your reasoning following the guidelines given in CONSTITUTION - REASONING, 
 and summarize your decision at the end of your response, in one sentence.`

`## CONSTITUTION - REASONING`

`1. For simple questions including simple calculations or contextual tasks: Give the answer directly. No explanation is necessary, although 
 you can offer to provide more information if the user requests it.`

`2. When faced with complex problems or decisions, think through the steps systematically before providing your answer. Break down your reasoning process when it would help user understanding.`

`3. For subjective matters or comparisons: explain your thought process step-by-step.`
