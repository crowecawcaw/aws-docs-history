# What is a prompt?

A prompt is the input that you send to a model in order for it to generate a response. For example, you could send the following user prompt to a model: `What is Avebury stone circle?`.

This prompt would likely generate a response similar to the following:

```
Avebury stone circle is a Neolithic monument located in Wiltshire, England.
It consists of a massive circular bank and ditch, with a large outer circle of standing stones
that originally numbered around 100.
```

Some models support _multimodal_ prompts, which are prompts that support different types of media input, such as text, images, or video.
For example, you could send an image to a model and ask it to describe what the image contains. Not all models support multimodal prompts and modality support varies by model. For information on how to best create prompts for a specific model, see [Prompt engineering guides](#prompt-guides "#prompt-guides").

In addition to user prompts, Amazon Bedrock in SageMaker Unified Studio also supports inference parameters and system instructions, which allow you to customize and influence model behavior. The following sections provide information and guidance on how to use inference parameters and sytem prompts.

###### Topics

- [Inference parameters](#inference-parameters "#inference-parameters")
- [System instructions](#system-prompts "#system-prompts")
- [Prompt engineering guides](#prompt-guides "#prompt-guides")

## Inference parameters

Inference parameters are values that you can adjust to influence how a model generates
a response to a prompt. For example, in the chat agent app you create in [Build a chat agent app with Amazon Bedrock](create-chat-app.md "create-chat-app.md"), you can use inference parameters to adjust the randomness and
diversity of the songs that the model generates for a playlist.

You can apply inference parameters to models you use in the [Amazon Bedrock playgrounds](bedrock-playgrounds.md "bedrock-playgrounds.md"), [chat agent apps](create-chat-app.md "create-chat-app.md"), and [flow apps](create-flows-app.md "create-flows-app.md").

### Randomness and diversity

For any given sequence, a model determines a probability distribution of options for
the next token in the sequence. To generate each token in an output, the model samples
from this distribution. Randomness and diversity refer to the amount of variation in a
model's response. You can control these factors by limiting or adjusting the
distribution. Foundation models typically support the following parameters to control
randomness and diversity in the response.

- **Temperature**– Affects the shape of the
  probability distribution for the predicted output and influences the likelihood
  of the model selecting lower-probability outputs.

      + Choose a lower value to influence the model to select
       higher-probability outputs.
      + Choose a higher value to influence the model to select
       lower-probability outputs.

  In technical terms, the temperature modulates the probability mass function
  for the next token. A lower temperature steepens the function and leads to more
  deterministic responses, and a higher temperature flattens the function and
  leads to more random responses.

- **Top K** – The number of most-likely
  candidates that the model considers for the next token.

      + Choose a lower value to decrease the size of the pool and limit the
       options to more likely outputs.
      + Choose a higher value to increase the size of the pool and allow the
       model to consider less likely outputs.

  For example, if you choose a value of 50 for Top K, the model selects from 50
  of the most probable tokens that could be next in the sequence.

- **Top P** – The percentage of most-likely
  candidates that the model considers for the next token.

      + Choose a lower value to decrease the size of the pool and limit the
       options to more likely outputs.
      + Choose a higher value to increase the size of the pool and allow the
       model to consider less likely outputs.

  In technical terms, the model computes the cumulative probability distribution
  for the set of responses and considers only the top P% of the
  distribution.

For example, if you choose a value of 0.8 for Top P, the model selects from
the top 80% of the probability distribution of tokens that could be next in the
sequence.

The following table summarizes the effects of these parameters.

| Parameter   | Effect of lower value                                                                                  | Effect of higher value                                                                             |
| ----------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Temperature | Increase likelihood of higher-probability tokens<br>Decrease<br>likelihood of lower-probability tokens | Increase likelihood of lower-probability tokensDecrease<br>likelihood of higher-probability tokens |
| Top K       | Remove lower-probability tokens                                                                        | Allow lower-probability tokens                                                                     |
| Top P       | Remove lower-probability tokens                                                                        | Allow lower-probability tokens                                                                     |

As an example to understand these parameters, consider the example prompt `I hear
 the hoof beats of "`. Let's say that the model determines the following three words
to be candidates for the next token. The model also assigns a probability for each word.

```
{
    "horses": 0.7,
    "zebras": 0.2,
    "unicorns": 0.1
}
```

- If you set a high **temperature**, the probability
  distribution is flattened and the probabilities become less different, which would increase
  the probability of choosing "unicorns" and decrease the probability of choosing
  "horses".
- If you set **Top K** as 2, the model only considers the top
  2 most likely candidates: "horses" and "zebras."
- If you set **Top P** as 0.7, the model only considers
  "horses" because it is the only candidate that lies in the top 70% of the probability
  distribution. If you set **Top P** as 0.9, the model considers
  "horses" and "zebras" as they lie in the top 90% of probability distribution.

## System instructions

A system instruction an overarching initial guideline that defines how a model should
behave in future interactions. System instructions provide context to the model about the task it should perform or the persona it should adopt during the conversation.

For example, you could use a system instruction to specify that the model should behave as an app that creates playlists for a radio station that plays rock and pop music. You can then use the model to
create playlists of rock and pop songs based on different themes, such as songs that are related by artist

You can apply system instructions to models you use in the [Amazon Bedrock playgrounds](bedrock-playgrounds.md "bedrock-playgrounds.md"), [chat agent apps](create-chat-app.md "create-chat-app.md"), and [flow apps](create-flows-app.md "create-flows-app.md").

## Prompt engineering guides

Amazon Bedrock in SageMaker Unified Studio provides models from a variety of model providers. Each provider provides
guidance on how to best create prompt for their models.

- **Amazon Nova user guide:**
  [https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html](../../../nova/latest/userguide/what-is-nova.md "../../../nova/latest/userguide/what-is-nova.md")
- **Anthropic Claude model prompt
  guide:**
  [https://docs.anthropic.com/claude/docs](https://docs.anthropic.com/claude/docs/configuring-gpt-prompts-for-claude "https://docs.anthropic.com/claude/docs/configuring-gpt-prompts-for-claude")
- **Anthropic Claude prompt engineering
  resources:**
  [https://docs.anthropic.com/claude/docs/guide-to-anthropics-prompt-engineering-resources](https://docs.anthropic.com/claude/docs/configuring-gpt-prompts-for-claude "https://docs.anthropic.com/claude/docs/configuring-gpt-prompts-for-claude")
- **Cohere prompt guide:**
  [https://txt.cohere.com/how-to-train-your-pet-llm-prompt-engineering](https://txt.cohere.com/how-to-train-your-pet-llm-prompt-engineering "https://txt.cohere.com/how-to-train-your-pet-llm-prompt-engineering")
- **AI21 Labs Jurassic model prompt guide:**
  [https://docs.ai21.com/docs/prompt-engineering](https://docs.ai21.com/docs/prompt-engineering "https://docs.ai21.com/docs/prompt-engineering")
- **Meta Llama 2 prompt guide:**
  [https://ai.meta.com/llama/get-started/#prompting](https://ai.meta.com/llama/get-started/#prompting "https://ai.meta.com/llama/get-started/#prompting")
- **Stability documentation:**
  [https://platform.stability.ai/docs/getting-started](https://platform.stability.ai/docs/getting-started "https://platform.stability.ai/docs/getting-started")
- **Mistral AI prompt guide:**
  [https://docs.mistral.ai/guides/prompting_capabilities/](https://docs.mistral.ai/guides/prompting_capabilities/ "https://docs.mistral.ai/guides/prompting_capabilities/")

For general guidelines about creating prompts with Amazon Bedrock, see [General guidelines for Amazon Bedrock LLM users](../../../bedrock/latest/userguide/general-guidelines-for-bedrock-users.md "../../../bedrock/latest/userguide/general-guidelines-for-bedrock-users.md").
