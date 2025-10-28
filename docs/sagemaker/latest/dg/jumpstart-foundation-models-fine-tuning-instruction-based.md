# Fine-tune a large language model (LLM) using prompt instructions

Instruction-based fine-tuning uses labeled examples to improve the performance
of a pre-trained foundation model on a specific task. The labeled examples are
formatted as prompt, response pairs and phrased as instructions. This
fine-tuning process modifies the weights of the model. For more information on
instruction-based fine-tuning, see the papers [Introducing FLAN: More generalizable Language Models with Instruction
Fine-Tuning](https://ai.googleblog.com/2021/10/introducing-flan-more-generalizable.html "https://ai.googleblog.com/2021/10/introducing-flan-more-generalizable.html") and [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416 "https://arxiv.org/abs/2210.11416").

Fine-tuned LAnguage Net (FLAN) models use instruction tuning to make models
more amenable to solving general downstream NLP tasks. Amazon SageMaker JumpStart provides a
number of foundation models in the FLAN model family. For example, FLAN-T5
models are instruction fine-tuned on a wide range of tasks to increase zero-shot
performance for a variety of common use cases. With additional data and
fine-tuning, instruction-based models can be further adapted to more specific
tasks that weren’t considered during pre-training.

To fine-tune a LLM on a specific task using prompt-response pairs task
instructions:

1. Prepare your instructions in JSON files. For more information about
   the required format for the prompt-response pair files and the structure
   of the data folder, see [Prepare and upload training data for instruction-based
   fine-tuning](#jumpstart-foundation-models-fine-tuning-instruction-based-prepare-data "#jumpstart-foundation-models-fine-tuning-instruction-based-prepare-data").
2. Create your fine-tuning training job. For instructions, see [Create a training job for instruction-based fine-tuning](#jumpstart-foundation-models-fine-tuning-instruction-based-train "#jumpstart-foundation-models-fine-tuning-instruction-based-train").
   You can find end-to-end examples in [Example notebooks](#jumpstart-foundation-models-fine-tuning-instruction-based-examples "#jumpstart-foundation-models-fine-tuning-instruction-based-examples").

Only a subset of JumpStart foundation models are compatible with instruction-based
fine-tuning. Instruction-based fine-tuning is available with the following
foundation models:

###### Note

Some JumpStart foundation models, such as Llama 2 7B, require acceptance of an
end-user license agreement before fine-tuning and performing inference. For
more information, see [End-user license
agreements](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula").

- Flan-T5 Base
- Flan-T5 Large
- Flan-T5 Small
- Flan-T5 XL
- Flan-T5 XXL
- Llama 2 13B
- Llama 2 13B Chat
- Llama 2 13B Neuron
- Llama 2 70B
- Llama 2 70B Chat
- Llama 2 7B
- Llama 2 7B Chat
- Llama 2 7B Neuron
- Mistral 7B
- RedPajama INCITE Base 3B V1
- RedPajama INCITE Base 7B V1
- RedPajama INCITE Chat 3B V1
- RedPajama INCITE Chat 7B V1
- RedPajama INCITE Instruct 3B V1
- RedPajama INCITE Instruct 7B V1

## Prepare and upload training data for instruction-based

fine-tuning

Training data for instruction-based fine-tuning must be provided in JSON
Lines text file format, where each line is a dictionary. All training data
must be in a single folder. The folder can include multiple .jsonl files.

The training folder can also include a template JSON file
(`template.json`) that describes the input and output formats
of your data. If no template file is provided, the following template file
is used:

```
{
  "prompt": "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:\n{instruction}\n\n### Input:\n{context}",
  "completion": "{response}"
}
```

According to the `template.json` file, each .jsonl entry of the
training data must include `{instruction}`,
`{context}`, and `{response}` fields.

If you provide a custom template JSON file, use the `"prompt"`
and `"completion"` keys to define your own required fields.
According to the following custom template JSON file, each .jsonl entry of
the training data must include `{question}`,
`{context}`, and `{answer}` fields:

```
{
  "prompt": "question: {question} context: {context}",
  "completion": "{answer}"
}
```

### Split data for training and testing

You can optionally provide another folder containing validation data.
This folder should also include one or more .jsonl files. If no
validation dataset is provided, then a set amount of the training data
is set aside for validation purposes. You can adjust the percentage of
training data used for validation when you choose the hyperparameters
for fine-tuning your model.

### Upload fine-tuning data to Amazon S3

Upload your prepared data to Amazon Simple Storage Service (Amazon S3) to use when fine-tuning a
JumpStart foundation model. You can use the following commands to upload your
data:

```
from sagemaker.s3 import S3Uploader
import sagemaker
import random

output_bucket = sagemaker.Session().default_bucket()
local_data_file = `"train.jsonl"`
train_data_location = f`"s3://{output_bucket}/dolly_dataset"`
S3Uploader.upload(local_data_file, train_data_location)
S3Uploader.upload("template.json", train_data_location)
print(f"Training data: {train_data_location}")
```

## Create a training job for instruction-based fine-tuning

After your data is uploaded to Amazon S3, you can fine-tune and deploy your
JumpStart foundation model. To fine-tune your model in Studio, see [Fine-tune a model in Studio](jumpstart-foundation-models-use-studio-updated-fine-tune.md "jumpstart-foundation-models-use-studio-updated-fine-tune.md"). To fine-tune your model using the SageMaker Python SDK, see
[Fine-tune publicly available foundation models with the
JumpStartEstimator class](jumpstart-foundation-models-use-python-sdk-estimator-class.md "jumpstart-foundation-models-use-python-sdk-estimator-class.md").

## Example notebooks

For more information on instruction-based fine-tuning, see the following
example notebooks:

- [Fine-tune LLaMA 2 models on JumpStart](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/llama-2-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/llama-2-finetuning.html")
- [Introduction to SageMaker JumpStart - Text Generation with Mistral
  models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/mistral-7b-instruction-domain-adaptation-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/mistral-7b-instruction-domain-adaptation-finetuning.html")
- [Introduction to SageMaker JumpStart - Text Generation with Falcon
  models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/falcon-7b-instruction-domain-adaptation-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/falcon-7b-instruction-domain-adaptation-finetuning.html")
- [SageMaker JumpStart Foundation Models - HuggingFace Text2Text Instruction
  Fine-Tuning](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/instruction-fine-tuning-flan-t5.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/instruction-fine-tuning-flan-t5.html")
