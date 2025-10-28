# What are foundation model evaluations?

FMEval can help you quantify model risks, such as inaccurate, toxic, or biased content.
Evaluating your LLM helps you comply with international guidelines around responsible
generative AI, such as the [ISO 42001](https://aistandardshub.org/ai-standards/information-technology-artificial-intelligence-management-system/ "https://aistandardshub.org/ai-standards/information-technology-artificial-intelligence-management-system/") AI Management System Standard and the NIST AI Risk Management
Framework.

The follow sections give a broad overview of the supported methods for creating model evaluations, viewing the results of a model evaluation job, and analyzing the results.

## Model evaluation tasks

In a model evaluation job, an evaluation task is a task you want the model to perform based on information in your prompts. You can choose one task type per model evaluation job

###### Supported task types in model evaluation jobs

- **Open-ended generation** – The production
  of natural human responses to text that does not have a pre-defined
  structure.
- **Text summarization** – The generation of
  a concise and condensed summary while retaining the meaning and key information
  that's contained in larger text.
- **Question answering** – The generation of
  a relevant and accurate response to a prompt.
- **Classification** – Assigning a category,
  such as a label or score to text, based on its content.
- **Custom** – Allows you to define custom evaluation dimensions for your model evaluation job.

Each task type has specific metrics associated with them that you can use in an automated model evaluation jobs. To learn about the metrics associated with automatic model evaluation jobs, and model evaluation jobs that use human workers, see [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md") .

## Updating inference parameters

Inference parameters are a way to influence a model's output without having to retrain or fine-tune a model.

In automatic model evaluation job, you can change the model's Temperature, Top P, and the Max new tokens.

###### Temperature

Changes the amount of randomness in the model's responses. Lower the default temperature to decrease the amount
of randomness, and increase to have more.

###### Top P

During inference, the model is generating text and choosing from a list of words to place the next word.
Updating Top P changes the number of words in that list based on a percentage.
Decreasing Top P results in more deterministic samples, while a higher value will allow for more variability and creativity in the generated text.

###### Max new tokens

Changes the length of response the model can provide.

You can update the inference parameters in Studio after adding the model to your model evaluation job.

## Automatic model evaluation jobs

Automatic model evaluation jobs use metrics based on benchmarks to measure toxic, harmful, or otherwise poor responses to your customers. Model responses are scored using either built-in datasets specific to the task or you can specify your own custom prompt dataset.

To create an automatic model evaluation job you can use Studio or the [`fmeval`](https://github.com/aws/fmeval?tab=readme-ov-file#foundation-model-evaluations-library "https://github.com/aws/fmeval?tab=readme-ov-file#foundation-model-evaluations-library") library. Automatic model evaluation jobs support the use of a single model. In Studio, you can use either a JumpStart model or you can use JumpStart model that you've previously deployed to an endpoint.

Alternatively, you can deploy the `fmeval` library into your own code base, and customize the model evaluation job for your own use cases.

To better understand your results, use the generated report. The report includes visualizations and examples. You also see the results saved in the Amazon S3 bucket specified when creating the job. To learn more about the structure of the results, see [Understand the
results of an automatic evaluation job](clarify-foundation-model-evaluate-auto-ui-results.md "clarify-foundation-model-evaluate-auto-ui-results.md").

To use a model not publicly available in JumpStart , you must use the `fmeval` library to run the automatic model evaluation job. For a list of JumpStart models, see [Available foundation models](jumpstart-foundation-models-latest.md "jumpstart-foundation-models-latest.md").

### Prompt templates

To help ensure that the JumpStart model you select performs well against all
prompts, SageMaker Clarify automatically augments your input prompts into a format that works
best for the model and the **Evaluation dimensions** you select. To see the default prompt template that Clarify provides, choose **Prompt template** in the card for the evaluation dimension. If you select, for example, the task type **Text summarization** in the UI, Clarify by default displays a card for each of the associated evaluation
dimensions - in this case, **Accuracy**, **Toxicity**,
and **Semantic Robustness**. In these cards, you can configure the datasets and
prompt templates Clarify uses to measure that evaluation dimension. You can also remove
any dimension you don’t want to use.

#### Default prompt templates

Clarify provides a selection of datasets you can use to measure each evaluation
dimension. You can choose to use one or more of these datasets, or you can supply your
own custom dataset. If you use the datasets provided by Clarify, you can also use
the prompt templates inserted by Clarify as defaults. We derived these default
prompts by analyzing the response format in each dataset and determining query
augmentations needed to achieve the same response format.

The prompt template provided by Clarify also depends upon the model you select. You
might choose a model that is fine-tuned to expect instructions in specific locations
of the prompt. For example,
choosing the model **meta-textgenerationneuron-llama-2-7b**, task type
**Text Summarization**, and the Gigaword dataset,
shows a default prompt template of the following:

```
Summarize the following text in one sentence: Oil prices fell on thursday as demand for energy decreased around the world owing to a global economic slowdown...
```

Choosing the llama chat model **meta-textgenerationneuron-llama-2-7b-f**, on the other hand, shows the following default prompt template:

```
[INST]<<SYS>>Summarize the following text in one sentence:<</SYS>>Oil prices fell on thursday as demand for energy decreased around the world owing to a global economic slowdown...[/INST]
```

#### Custom

prompt templates

In the prompt template dialog box, you can toggle on or off the automatic prompt
templating support that SageMaker Clarify provides. If you turn off automatic prompt templating, Clarify
provides the default prompt (as a baseline across all datasets within the same
evaluation dimension) which you can modify. For
example, if the default prompt template includes the instruction _Summarize
the following in one sentence_, you can modify it to _Summarize
the following in less than 100 words_ or any other instruction you
want to use.

Also, if you modify a prompt for an evaluation dimension, the same prompt is applied to
all datasets using that same dimension. So if you choose to apply the prompt
_Summarize the following text in 17 sentences_ to dataset
Gigaword to measure toxicity, this same instruction is used for the
dataset Government report to measure toxicity. If you want to
use a different prompt for a different dataset (using the same task type and evaluation
dimension), you can use the python packages provided by FMEval. For details, see
[Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md").

###### Example of an updated prompt template using \*\*Prompt

template\*\*

Imagine a simple scenario where you have a simple dataset made up of only two
prompts, and you want to evaluate them using
`**meta-textgenerationneuron-llama-2-7b-f**`.

```
{
	"model_input": "Is himalaya the highest mountain in the world?",
    "target_output": "False, Mt. Everest is the highest mountain in the world",
    "category": "Geography"
},
{
    "model_input": "Is Olympia the capital of Washington?",
    "target_output": "True",
    "category": "Capitals"
}
```

Because your prompts are question and answer pairs, you choose the
**Question Answering (Q&A)** task type.

By choosing **Prompt template** in Studio you can see
how SageMaker Clarify will format your prompts to match the requirements of the
`**meta-textgenerationneuron-llama-2-7b-f**`
JumpStart model.

```
[INST]<<SYS>>Respond to the following question. Valid answers are "True" or "False".<<SYS>>Is himalaya the highest mountain in the world?[/INST]
```

For this model SageMaker Clarify will supplement your prompts to contain the correct prompt
format by adding the `[INST]` and `<<SYS>>`tags. It
will also augment your initial request by adding `Respond to the following
 question. Valid answers are "True" or "False".` to help the model
respond better.

The SageMaker Clarify provided text might not be well suited for your use case. To turn
off the default prompt templates, slide the **Dataset default prompt
templates** toggle to **Off**.

You can edit the prompt template to be aligned with your use case. For example,
you can prompt for a short response instead of a True/False answer format, as shown in the following line:

```
[INST]<<SYS>>`Respond to the following question with a short response.`<<SYS>>Is himalaya the highest mountain in the world?[/INST]
```

Now all built-in or custom prompt datasets under the specified
**Evaluation dimension** will use the prompt template you
specified.

## Model evaluation jobs that use humans workers

You can also employ **human workers** to manually
evaluate your model responses for more subjective dimensions, such as helpfulness or
style. To create a model evaluation job that uses human workers, you must use
Studio.

In a model evaluation job that uses human workers you can compare the responses
for up to two JumpStart models. Optionally, you can also specify responses from
models outside of AWS. All model evaluation jobs that use human workers require
that you create a custom prompt dataset, and store it in Amazon S3. To learn more about how to create a custom prompt data, see [Creating a model evaluation job that uses human workers](clarify-foundation-model-evaluate-human.md#clarify-foundation-model-evaluate-human-run "clarify-foundation-model-evaluate-human.md#clarify-foundation-model-evaluate-human-run").

In Studio, you can define the criteria that your human workforce uses to
evaluate responses from models. You can also document evaluation instructions using
a template available in Studio. Furthermore, you can create a work team in
Studio. The work team are people who you want to participate in your model
evaluation job.
