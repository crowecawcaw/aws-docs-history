# Fine-tune a large language model (LLM) using domain adaptation

Domain adaptation fine-tuning allows you to leverage pre-trained foundation
models and adapt them to specific tasks using limited domain-specific data. If
prompt engineering efforts do not provide enough customization, you can use
domain adaption fine-tuning to get your model working with domain-specific
language, such as industry jargon, technical terms, or other specialized data.
This fine-tuning process modifies the weights of the model.

To fine-tune your model on a domain-specific dataset:

1. Prepare your training data. For instructions, see [Prepare and upload training data for domain adaptation
   fine-tuning](#jumpstart-foundation-models-fine-tuning-domain-adaptation-prepare-data "#jumpstart-foundation-models-fine-tuning-domain-adaptation-prepare-data").
2. Create your fine-tuning training job. For instructions, see [Create a training job for instruction-based fine-tuning](#jumpstart-foundation-models-fine-tuning-domain-adaptation-train "#jumpstart-foundation-models-fine-tuning-domain-adaptation-train").
   You can find end-to-end examples in [Example notebooks](#jumpstart-foundation-models-fine-tuning-domain-adaptation-examples "#jumpstart-foundation-models-fine-tuning-domain-adaptation-examples").

Domain adaptation fine-tuning is available with the following foundation
models:

###### Note

Some JumpStart foundation models, such as Llama 2 7B, require acceptance of an
end-user license agreement before fine-tuning and performing inference. For
more information, see [End-user license
agreements](jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula "jumpstart-foundation-models-choose.md#jumpstart-foundation-models-choose-eula").

- Bloom 3B
- Bloom 7B1
- BloomZ 3B FP16
- BloomZ 7B1 FP16
- GPT-2 XL
- GPT-J 6B
- GPT-Neo 1.3B
- GPT-Neo 125M
- GPT-NEO 2.7B
- Llama 2 13B
- Llama 2 13B Chat
- Llama 2 13B Neuron
- Llama 2 70B
- Llama 2 70B Chat
- Llama 2 7B
- Llama 2 7B Chat
- Llama 2 7B Neuron

## Prepare and upload training data for domain adaptation

fine-tuning

Training data for domain adaptation fine-tuning can be provided in CSV,
JSON, or TXT file format. All training data must be in a single file within
a single folder.

The training data is taken from the **Text** column for
CSV or JSON training data files. If no column is labeled
**Text**, then the training data is taken from the
first column for CSV or JSON training data files.

The following is an example body of a TXT file to be used for
fine-tuning:

```
This report includes estimates, projections, statements relating to our
business plans, objectives, and expected operating results that are “forward-
looking statements” within the meaning of the Private Securities Litigation
Reform Act of 1995, Section 27A of the Securities Act of 1933, and Section 21E
of ....
```

### Split data for training and testing

You can optionally provide another folder containing validation data.
This folder should also include one CSV, JSON, or TXT file. If no
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
local_data_file = `"train.txt"`
train_data_location = f`"s3://{output_bucket}/training_folder"`
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

For more information on domain adaptation fine-tuning, see the following
example notebooks:

- [SageMaker JumpStart Foundation Models - Fine-tuning text generation GPT-J
  6B model on domain specific dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/domain-adaption-finetuning-gpt-j-6b.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/domain-adaption-finetuning-gpt-j-6b.html")
- [Fine-tune LLaMA 2 models on JumpStart](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/llama-2-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/llama-2-finetuning.html")
