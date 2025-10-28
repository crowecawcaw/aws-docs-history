# Customize your workflow using the `fmeval` library

You can customize your model evaluation to allow for a model that is not a
JumpStart or Amazon Bedrock model or use a custom workflow for evaluation. If you use your own
model, you have to create a custom `ModelRunner`. If you use your own dataset
for evaluation, you must configure a `DataConfig` object. The following
section shows how to format your input dataset, customize a `DataConfig`
object to use your custom dataset, and create a custom `ModelRunner`.

If you want to use your own dataset to evaluate your model, you must use a
`DataConfig` object to specify the `dataset_name` and
the `dataset_uri` of the dataset that you want to evaluate. If you
use a built-in dataset, the `DataConfig` object is already configured
as the default for evaluation algorithms.

You can use one custom dataset every time you use the `evaluate`
function. You can invoke `evaluate` any number of times to use any
number of datasets that you want.

Configure a custom dataset with your model request specified in the question
column, and the target answer specified in the column answer, as follows:

```
from fmeval.data_loaders.data_config import DataConfig
from fmeval.constants import MIME_TYPE_JSONLINES

config = DataConfig(
dataset_name="tiny_dataset",
dataset_uri="tiny_dataset.jsonl",
dataset_mime_type=MIME_TYPE_JSONLINES,
model_input_location="question",
target_output_location="answer",
)
```

The `DataConfig` class contains the following parameters:

- `dataset_name` – The name of the dataset that you
  want to use to evaluate your LLM.

`dataset_uri` – The local path or uniform resource
identifier (URI) to the S3 location of your dataset.

- `dataset_mime_type` – The format of the input data
  that you want to use to evaluate your LLM. The FMEval library can support
  both `MIME_TYPE_JSON` and
  `MIME_TYPE_JSONLINES`.
- `model_input_location` – (Optional) The name of the
  column in your dataset that contains the model inputs or prompts that
  you want to evaluate.

Use a `model_input_location` that specifies the name of
your column. The column must contain the following values corresponding
to the following associated tasks:

    + For **open-ended generation**,
     **toxicity**, and **accuracy** evaluations, specify the
     column that contains the **prompt**
     that your model should respond to.
    + For a **question answering**
     task, specify the column that contains the **question** that your model should generate a
     response to.
    + For a **text summarization
     task**, specify the name of the column that contains
     the **text** that you want your
     model to summarize.
    + For a **classification task**,
     specify the name of the column that contains the **text** that you want your model to
     classify.
    + For a **factual knowledge**
     evaluations, specify the name of the column that contains the
     **question** that you want the
     model to predict the answer to.
    + For **semantic robustness**
     evaluations, specify the name of the column that contains the
     **input** that you want your
     model to perturb.
    + For **prompt stereotyping**
     evaluations, use the `sent_more_input_location`
     and `sent_less_input_location` instead of
     `model_input_location`, as shown in the following
     parameters.

- `model_output_location` – (Optional) The name of the
  column in your dataset that contains the predicted output that you want
  to compare against the reference output that is contained in
  `target_output_location`. If you provide
  `model_output_location`, then FMEval won't send a request
  to your model for inference. Instead, it uses the output contained in
  the specified column to evaluate your model.
- `target_output_location`– The name of the column in
  the reference dataset that contains the true value to compare against
  the predicted value that is contained in
  `model_output_location`. Required only for factual
  knowledge, accuracy, and semantic robustness. For factual knowledge,
  each row in this column should contain all possible answers separated by
  a delimiter. For example, if the answers for a question are
  [“UK”,“England”], then the column should contain “UK<OR>England”.
  The model prediction is correct if it contains any of the answers
  separated by the delimiter.
- `category_location` – The name of the column that
  contains the name of a category. If you provide a value for
  `category_location`, then scores are aggregated and
  reported for each category.
- `sent_more_input_location` – The name of the column
  that contains a prompt with more bias. Required only for prompt
  stereotyping. Avoid unconscious bias. For bias examples, see the [CrowS-Pairs
  dataset](https://paperswithcode.com/dataset/crows-pairs "https://paperswithcode.com/dataset/crows-pairs").
- `sent_less_input_location` – The name of the column
  that contains a prompt with less bias. Required only for prompt
  stereotyping. Avoid unconscious bias. For bias examples, see the [CrowS-Pairs
  dataset](https://paperswithcode.com/dataset/crows-pairs "https://paperswithcode.com/dataset/crows-pairs").
- `sent_more_output_location` – (Optional) The name of
  the column that contains a predicted probability that your model’s
  generated response will contain more bias. This parameter is only used
  in prompt stereotyping tasks.
- `sent_less_output_location` – (Optional) The name of
  the column that contains a predicted probability that your model’s
  generated response will contain less bias. This parameter is only used
  in prompt stereotyping tasks.
  If you want to add a new attribute that corresponds to a dataset column to the
  `DataConfig` class, you must add the `suffix
 _location` to the end of the attribute name.

To evaluate a custom model, use a base data class to configure your model and
create a custom `ModelRunner`. Then, you can use this
`ModelRunner` to evaluate any language model. Use the following
steps to define a model configuration, create a custom `ModelRunner`,
and test it.

The `ModelRunner` interface has one abstract method as
follows:

```
def predict(self, prompt: str) → Tuple[Optional[str], Optional[float]]
```

This method takes in a prompt as a string input, and returns a Tuple
containing a model text response and an input log probability. Every
`ModelRunner` must implement a `predict`
method.

###### Create a custom `ModelRunner`

1. Define a model configuration.

The following code example shows how to apply a `dataclass`
decorator to a custom `HFModelConfig` class so that you can
define a model configuration for a **Hugging
Face** model:

```
from dataclasses import dataclass

@dataclass
class HFModelConfig:
model_name: str
max_new_tokens: int
seed: int = 0
remove_prompt_from_generated_text: bool = True
```

In the previous code example, the following applies:

    * The parameter `max_new_tokens` is used to limit the
     length of the response by limiting the number of tokens returned
     by an LLM. The type of model is set by passing a value for
     `model_name` when the class is instantiated. In
     this example, the model name is set to `gpt2`, as
     shown in the end of this section. The parameter
     `max_new_tokens` is one option to configure text
     generation strategies using a `gpt2` model
     configuration for a pre-trained OpenAI GPT model. See [AutoConfig](https://huggingface.co/transformers/v3.5.1/model_doc/auto.html "https://huggingface.co/transformers/v3.5.1/model_doc/auto.html") for other model types.
    * If the parameter
     `remove_prompt_from_generated_text` is set to
     `True`, then the generated response won't contain
     the originating prompt sent in the request.

For other text generation parameters, see the [Hugging Face documentation for
GenerationConfig](https://huggingface.co/docs/transformers/v4.34.1/en/main_classes/text_generation#transformers.GenerationConfig "https://huggingface.co/docs/transformers/v4.34.1/en/main_classes/text_generation#transformers.GenerationConfig"). 2. Create a custom `ModelRunner` and implement a predict
method. The following code example shows how to create a custom
`ModelRunner` for a Hugging Face model
using the `HFModelConfig` class created in the previous code
example.

```
from typing import Tuple, Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from fmeval.model_runners.model_runner import ModelRunner

class HuggingFaceCausalLLMModelRunner(ModelRunner):
def __init__(self, model_config: HFModelConfig):
    self.config = model_config
    self.model = AutoModelForCausalLM.from_pretrained(self.config.model_name)
    self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)

def predict(self, prompt: str) -> Tuple[Optional[str], Optional[float]]:
    input_ids = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
    generations = self.model.generate(
        **input_ids,
        max_new_tokens=self.config.max_new_tokens,
        pad_token_id=self.tokenizer.eos_token_id,
    )
    generation_contains_input = (
        input_ids["input_ids"][0] == generations[0][: input_ids["input_ids"].shape[1]]
    ).all()
    if self.config.remove_prompt_from_generated_text and not generation_contains_input:
        warnings.warn(
            "Your model does not return the prompt as part of its generations. "
            "`remove_prompt_from_generated_text` does nothing."
        )
    if self.config.remove_prompt_from_generated_text and generation_contains_input:
        output = self.tokenizer.batch_decode(generations[:, input_ids["input_ids"].shape[1] :])[0]
    else:
        output = self.tokenizer.batch_decode(generations, skip_special_tokens=True)[0]

    with torch.inference_mode():
        input_ids = self.tokenizer(self.tokenizer.bos_token + prompt, return_tensors="pt")["input_ids"]
        model_output = self.model(input_ids, labels=input_ids)
        probability = -model_output[0].item()

    return output, probability
```

The previous code uses a custom
`HuggingFaceCausalLLMModelRunner` class that inherits
properties from the FMEval `ModelRunner` class. The custom
class contains a constructor and a definition for a predict function,
which returns a `Tuple`.

For more `ModelRunner` examples, see the [model_runner](https://github.com/aws/fmeval/tree/main/src/fmeval/model_runners "https://github.com/aws/fmeval/tree/main/src/fmeval/model_runners") section of the `fmeval`
library.

The `HuggingFaceCausalLLMModelRunner` constructor contains
the following definitions:

    * The configuration is set to `HFModelConfig`,
     defined in the beginning of this section.
    * The model is set to a pre-trained model from the
     Hugging Face
     [Auto Class](https://huggingface.co/transformers/v3.5.1/model_doc/auto.html "https://huggingface.co/transformers/v3.5.1/model_doc/auto.html") that is specified using the model\_name
     parameter upon instantiation.
    * The tokenizer is set to a class from the [Hugging Face tokenizer library](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoTokenizer "https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoTokenizer")
     that matches the pre-trained model specified by
     `model_name`.

The `predict` method in the
`HuggingFaceCausalLLMModelRunner` class uses the
following definitions:

    * `input_ids` – A variable that contains input
     for your model. The model generates the input as follows.




    	+ A `tokenizer` Converts the request
    	 contained in `prompt` into token identifiers
    	 (IDs). These token IDs, which are numerical values that
    	 represent a specific token (word, sub-word or
    	 character), can be used directly by your model as input.
    	 The token IDs are returned as a PyTorch
    	 tensor objects, as specified by
    	 `return_tensors="pt"`. For other types of
    	 return tensor types, see the Hugging Face
    	 documentation for [apply\_chat\_template](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer.apply_chat_template "https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer.apply_chat_template").
    	+ Token IDs are sent to a device where the model is
    	 located so that they can be used by the model.
    * `generations` – A variable that contains the
     response generated by your LLM. The model’s generate function
     uses the following inputs to generate the response:




    	+ The `input_ids` from the previous
    	 step.
    	+ The parameter `max_new_tokens` specified in
    	 `HFModelConfig`.
    	+ A `pad_token_id` adds an end of sentence
    	 (eos) token to the response. For other tokens that you
    	 can use, see the Hugging Face
    	 documentation for [PreTrainedTokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer "https://huggingface.co/docs/transformers/main_classes/tokenizer#transformers.PreTrainedTokenizer").
    * `generation_contains_input` – A boolean
     variable that returns `True` when the generated
     response includes the input prompt in its response, and
     `False` otherwise. The return value is calculated
     using an element-wise comparison between the following.




    	+ All of the token IDs in the input prompt that are
    	 contained in
    	 `input_ids["input_ids"][0]`.
    	+ The beginning of the generated content that is
    	 contained in `generations[0][:
    	 input_ids["input_ids"].shape[1]]`.
    The `predict` method returns a warning if you
     directed the LLM to
     `remove_prompt_from_generated_text` in your
     configuration but the generated response doesn’t contain the
     input prompt.


    The output from the `predict` method contains a
     string returned by the `batch_decode` method, which
     converts token IDs returned in the response into human readable
     text. If you specified
     `remove_prompt_from_generated_text` as
     `True`, then the input prompt is removed from the
     generated text. If you specified
     `remove_prompt_from_generated_text` as
     `False`, the generated text will be returned
     without any special tokens that you included in the dictionary
     `special_token_dict`, as specified by
     `skip_special_tokens=True`.

3. Test your `ModelRunner`. Send a sample request to your
   model.

The following example shows how to test a model using the
`gpt2` pre-trained model from the Hugging
Face
`AutoConfig` class:

```
hf_config = HFModelConfig(model_name="gpt2", max_new_tokens=32)
model = HuggingFaceCausalLLMModelRunner(model_config=hf_config)
```

In the previous code example, `model_name` specifies the
name of the pre-trained model. The `HFModelConfig` class is
instantiated as hf_config with a value for the parameter
`max_new_tokens`, and used to initialize
`ModelRunner`.

If you want to use another pre-trained model from Hugging
Face, choose a `pretrained_model_name_or_path` in
`from_pretrained` under [AutoClass](https://huggingface.co/transformers/v3.5.1/model_doc/auto.html "https://huggingface.co/transformers/v3.5.1/model_doc/auto.html").

Lastly, test your `ModelRunner`. Send a sample request to
your model as shown in the following code example:

```
model_output = model.predict("London is the capital of?")[0]
print(model_output)
eval_algo.evaluate_sample()
```
