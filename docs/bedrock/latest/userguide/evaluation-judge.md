# Evaluate model performance using another LLM as a judge

With a model evaluation job that uses a judge model, Amazon Bedrock uses an LLM to score another model's responses and provide an
explanation of how it scored each prompt and response pair. Scores and explanations are available in the Amazon Bedrock console through the
[Evaluations](https://console.aws.amazon.com/bedrock/home#/eval/evaluation "https://console.aws.amazon.com/bedrock/home#/eval/evaluation") page.

This kind of model evaluation requires two different models, a _generator model_ and an _evaluator model_.
You define prompts for the generator model in a dataset, and the evaluator model scores the responses to those prompts based on metrics
you select.

The metrics summary card in the console displays a histogram that shows the number of times a responses received a certain score, and explanations of the score for
the first five prompts found in your dataset. The full evaluation job report is available in the Amazon S3 bucket you specify when you create the model evaluation job.

When you create the model evaluation job, you can either select an Amazon Bedrock model as the generator model, or you can evaluate a non-Amazon Bedrock model by providing
your own inference response data in the prompt dataset. If you provide your own response data, Amazon Bedrock skips the model invoke step and directly evaluates the
data you supply.

To rate the generator models' responses, Amazon Bedrock provides a set of built-in metrics you can select from. Each metric uses a different prompt for the evaluator model.
You can also define your own custom metrics for your particular business case. See [Use metrics to understand model performance](model-evaluation-metrics.md "model-evaluation-metrics.md") to learn more.

## Supported models

### Supported evaluator models (built-in metrics)

To create an evaluation job that uses an LLM as a judge with Amazon Bedrock's built-in metrics, you need access to at least one of the judge models in the following list. To learn more about gaining access to models and Region availability,
see [Access Amazon Bedrock foundation models](model-access.md "model-access.md").

- Amazon Nova Pro – `amazon.nova-pro-v1:0`
- Anthropic Claude 3.5 Sonnet v1 – `anthropic.claude-3-5-sonnet-20240620-v1:0`
- Anthropic Claude 3.5 Sonnet v2 – `anthropic.claude-3-5-sonnet-20241022-v2:0`
- Anthropic Claude 3.7 Sonnet – `anthropic.claude-3-7-sonnet-20250219-v1:0`
- Anthropic Claude 3 Haiku – `anthropic.claude-3-haiku-20240307-v1:0`
- Anthropic Claude 3.5 Haiku – `anthropic.claude-3-5-haiku-20241022-v1:0`
- Meta Llama 3.1 70B Instruct – `meta.llama3-1-70b-instruct-v1:0`
- Mistral Large – `mistral.mistral-large-2402-v1:0`

[Cross Region inference](cross-region-inference.md "cross-region-inference.md") profiles are supported for the listed models. To learn more, see [Supported cross-Region inference profiles](inference-profiles-support.md#inference-profiles-support-system "inference-profiles-support.md#inference-profiles-support-system").

### Supported evaluator models (custom metrics)

To create an evaluation job that uses an LLM as a judge with custom metrics, you need access to at least one of the judge models in the following list.

- Mistral Large 24.02 – `mistral.mistral-large-2402-v1:0`
- Mistral Large 24.07 – `mistral.mistral-large-2407-v1:0`
- Anthropic Claude 3.5 Sonnet v1 – `anthropic.claude-3-5-sonnet-20240620-v1:0`
- Anthropic Claude 3.5 Sonnet v2 – `anthropic.claude-3-5-sonnet-20241022-v2:0`
- Anthropic Claude 3.7 Sonnet – `anthropic.claude-3-7-sonnet-20250219-v1:0`
- Anthropic Claude 3 Haiku 3 – `anthropic.claude-3-haiku-20240307-v1:0`
- Anthropic Claude 3 Haiku 3.5 – `anthropic.claude-3-5-haiku-20241022-v1:0`
- Meta Llama 3.1 70B Instruct – `meta.llama3-1-70b-instruct-v1:0`
- Meta Llama 3.3 70B Instruct – `meta.llama3-3-70b-instruct-v1:0`
- Amazon Nova Pro – `amazon.nova-pro-v1:0`

[Cross Region inference](cross-region-inference.md "cross-region-inference.md") profiles are supported for the listed models. To learn more, see [Supported cross-Region inference profiles](inference-profiles-support.md#inference-profiles-support-system "inference-profiles-support.md#inference-profiles-support-system").

### Supported generator models

You can use the following model types in Amazon Bedrock as the generator model in an evaluation job. You can also bring your own inference response data from non-Amazon Bedrock models.

- Foundation models – [Amazon Bedrock foundation model information](foundation-models-reference.md "foundation-models-reference.md")
- Amazon Bedrock Marketplace models – [Amazon Bedrock Marketplace](amazon-bedrock-marketplace.md "amazon-bedrock-marketplace.md")
- Customized foundation models – [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md")
- Imported foundation models – [Use Custom model import to import a customized open-source model into Amazon Bedrock](model-customization-import-model.md "model-customization-import-model.md")
- Prompt routers – [Understanding intelligent prompt routing in
  Amazon Bedrock](prompt-routing.md "prompt-routing.md")
- Models for which you have purchased Provisioned Throughput – [Provisioned Throughput](prov-throughput.md "prov-throughput.md")
