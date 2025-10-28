# Optimize a prompt

Amazon Bedrock offers a tool to optimize prompts. Optimization rewrites prompts to yield inference
results that are more suitable for your use case. You can choose the model that you want to
optimize the prompt for and then generate a revised prompt.

After you submit a prompt to optimize, Amazon Bedrock analyzes the components of the prompt.
If the analysis is successful, it then rewrites the prompt. You can then copy and use the text
of the optimized prompt.

###### Note

For best results, we recommend optimizing prompts in English.

###### Topics

- [Supported Regions and models for prompt optimization](#prompt-management-optimize-supported "#prompt-management-optimize-supported")
- [Submit a prompt for optimization](#prompt-management-optimize-submit "#prompt-management-optimize-submit")

## Supported Regions and models for prompt optimization

Prompt optimization is supported in the following Regions (for more information about Regions supported in Amazon Bedrock see [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")):

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- South America (São Paulo)

Prompt optimization is supported for the following foundation models (to see which Regions support each model, refer to [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md")):

- Amazon Nova Lite
- Amazon Nova Micro
- Amazon Nova Premier
- Amazon Nova Pro
- Anthropic Claude 3 Haiku
- Anthropic Claude 3 Opus
- Anthropic Claude 3 Sonnet
- Anthropic Claude 3.5 Haiku
- Anthropic Claude 3.5 Sonnet v2
- Anthropic Claude 3.5 Sonnet
- Anthropic Claude 3.7 Sonnet
- Anthropic Claude Opus 4
- Anthropic Claude Sonnet 4
- DeepSeek DeepSeek-R1
- Meta Llama 3 70B Instruct
- Meta Llama 3.1 70B Instruct
- Meta Llama 3.2 11B Instruct
- Meta Llama 3.3 70B Instruct
- Meta Llama 4 Maverick 17B Instruct
- Meta Llama 4 Scout 17B Instruct
- Mistral AI Mistral Large (24.02)
- Mistral AI Mistral Large (24.07)

## Submit a prompt for optimization

To learn how to optimize a prompt, choose the tab for your preferred method, and then follow the steps:

Console
You can optimize a prompt through using a playground or Prompt management in the
AWS Management Console. You must select a model before you can optimize a prompt. The
prompt is optimized for the model that you choose.

###### To optimize a prompt in a playground

1. To learn how to write a prompt in an Amazon Bedrock playground, follow the steps at [Generate responses in the console using playgrounds](playgrounds.md "playgrounds.md").
2. After you write a prompt and select a model, choose the wand icon (

![Sparkle icon representing cleaning or refreshing functionality.](images/icons/wand.png)

).
The **Optimize prompt** dialog box opens, and Amazon Bedrock begins optimizing
your prompt. 3. When Amazon Bedrock finishes analyzing and optimizing your prompt,
you can compare your original prompt side by side with the
optimized prompt in the dialog box. 4. To replace your prompt with the optimized prompt in the
playground, choose **Use optimized prompt**.
To keep your original prompt, choose **Cancel**. 5. To submit the prompt and generate a response, choose **Run**.

###### To optimize a prompt in Prompt management

1. To learn how to write a prompt using Prompt management, follow the steps at [Create a prompt using Prompt management](prompt-management-create.md "prompt-management-create.md").
2. After you write a prompt and select a model, choose \*\*(

![Sparkle icon representing cleaning or refreshing functionality.](images/icons/wand.png)

) Optimize**
at the top of the **Prompt** box. 3. When Amazon Bedrock finishes analyzing and optimizing your prompt,
your optimized prompt is displayed as a variant side by side with the original prompt. 4. To use the optimized prompt instead of your original one, select
**Replace original prompt**. To keep your original prompt,
choose **Exit comparison\*\* and choose to save the original prompt.

###### Note

If you have 3 prompts in the comparison view and try to
optimize another prompt, you are asked to override and replace
either the original prompt or one of the variants. 5. To submit the prompt and generate a response, choose **Run**.

API
To optimize a prompt, send an [OptimizePrompt](../APIReference/API_agent-runtime_OptimizePrompt.md "../APIReference/API_agent-runtime_OptimizePrompt.md") request with an [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt"). Provide the prompt to optimize in the
`input` object and specify the model to optimize for in the `targetModelId` field.

The response stream returns the following events:

1. [analyzePromptEvent](../APIReference/API_agent-runtime_AnalyzePromptEvent.md "../APIReference/API_agent-runtime_AnalyzePromptEvent.md") – Appears when the prompt is finished being analyzed. Contains a message describing the analysis of the prompt.
2. [optimizedPromptEvent](../APIReference/API_agent-runtime_OptimizedPromptEvent.md "../APIReference/API_agent-runtime_OptimizedPromptEvent.md") – Appears when the prompt has finished being rewritten. Contains the optimized prompt.

Run the following code sample to optimize a prompt:

```
import boto3

# Set values here
TARGET_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0" # Model to optimize for. For model IDs, see https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html
PROMPT = "Please summarize this text: " # Prompt to optimize

def get_input(prompt):
    return {
        "textPrompt": {
            "text": prompt
        }
    }

def handle_response_stream(response):
    try:
        event_stream = response['optimizedPrompt']
        for event in event_stream:
            if 'optimizedPromptEvent' in event:
                print("========================== OPTIMIZED PROMPT ======================\n")
                optimized_prompt = event['optimizedPromptEvent']
                print(optimized_prompt)
            else:
                print("========================= ANALYZE PROMPT =======================\n")
                analyze_prompt = event['analyzePromptEvent']
                print(analyze_prompt)
    except Exception as e:
        raise e


if __name__ == '__main__':
    client = boto3.client('bedrock-agent-runtime')
    try:
        response = client.optimize_prompt(
            input=get_input(PROMPT),
            targetModelId=TARGET_MODEL_ID
        )
        print("Request ID:", response.get("ResponseMetadata").get("RequestId"))
        print("========================== INPUT PROMPT ======================\n")
        print(PROMPT)
        handle_response_stream(response)
    except Exception as e:
        raise e
```
