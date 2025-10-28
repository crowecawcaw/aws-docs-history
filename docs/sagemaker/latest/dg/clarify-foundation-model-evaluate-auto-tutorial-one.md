#

Evaluate a JumpStart model for prompt stereotyping

You can use a high-level `ModelRunner` wrapper to evaluate an
Amazon SageMaker JumpStart model for prompt stereotyping. The prompt stereotyping
algorithm measures the probability of your model encoding biases in its
response. These biases include those for race, gender, sexual orientation,
religion, age, nationality, disability, physical appearance, and socioeconomic
status.

This tutorial shows how to load the [Falcon 7-B](https://huggingface.co/tiiuae/falcon-7b "https://huggingface.co/tiiuae/falcon-7b") model from
the [Technology Innovation Institute](https://www.tii.ae/ "https://www.tii.ae/"),
available in JumpStart, and ask this model to generate responses to prompts.
Then, this tutorial shows how to evaluate the responses for prompt stereotyping
against the built-in [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs "https://github.com/nyu-mll/crows-pairs") open source challenge dataset.

The sections of this tutorial show how to do the following:

- Set up your environment.
- Run your model evaluation.
- View your analysis results.

## Set up your environment

###### Prerequisites

- Use a base Python 3.10 kernel environment and an
  `ml.g4dn.2xlarge` Amazon Elastic Compute Cloud (Amazon EC2) instance before
  starting this tutorial.

For more information about instance types and their recommended
use cases, see [Instance Types Available for Use With
Amazon SageMaker Studio Classic Notebooks](notebooks-available-instance-types.md "notebooks-available-instance-types.md").

###### Install required libraries

1. Install the SageMaker AI, `fmeval`, and other required
   libraries in your code as follows:

```
!pip3 install sagemaker
!pip3 install -U pyarrow
!pip3 install -U accelerate
!pip3 install "ipywidgets>=8"
!pip3 install jsonlines
!pip install fmeval
!pip3 install boto3==1.28.65
import sagemaker
```

2. Download the sample `JSON Lines` dataset [crows-pairs_sample.jsonl](https://github.com/aws/fmeval/blob/main/examples/crows-pairs_sample.jsonl "https://github.com/aws/fmeval/blob/main/examples/crows-pairs_sample.jsonl"), into your current working
   directory.
3. Check that your environment contains the sample input file using
   the following code:

```
import glob

# Check for fmeval wheel and built-in dataset
if not glob.glob("crows-pairs_sample.jsonl"):
print("ERROR - please make sure file exists: crows-pairs_sample.jsonl")

```

4. Define a JumpStart model as follows:

```
from sagemaker.jumpstart.model import JumpStartModel

model_id, model_version, = (
"huggingface-llm-falcon-7b-instruct-bf16",
"*",
)
```

5. Deploy the JumpStart model and create an endpoint as
   follows:

```
my_model = JumpStartModel(model_id=model_id)
predictor = my_model.deploy()
endpoint_name = predictor.endpoint_name
```

6. Define a prompt and the format of the model request, or payload,
   as follows:

```
prompt = "London is the capital of"
payload = {
"inputs": prompt,
"parameters": {
    "do_sample": True,
    "top_p": 0.9,
    "temperature": 0.8,
    "max_new_tokens": 1024,
    "decoder_input_details" : True,
    "details" : True
},
}
```

In the previous code example, the following parameters are
included in the model request:

    * `do_sample` – Instructs the model to
     sample from the raw model outputs (prior to normalization)
     during model inference to introduce diversity and creativity
     into model responses. Defaults to `False`. If you
     set `do_sample` to `True`, then you
     must specify a value for one of the following parameters:
     `temperature`, `top_k`,
     `top_p`, or `typical_p`.
    * `top_p` – Controls the randomness by
     limiting the set of tokens to consider when generating the
     next token. Higher values of `top_p` allow for a
     set containing a broader vocabulary. Lower values restrict
     the set of tokens to more probable words. Ranges for
     `top_p` are greater than `0` and
     less than `1`.
    * `temperature` – Controls the randomness
     of the generated text. Higher values of
     `temperature` instruct the model to generate
     more random and diverse responses. Lower values generate
     responses that are more predictable. Values for
     `temperature` must be positive.
    * `max_new_tokens` – Limits the length of
     the response by limiting the number of tokens returned by
     your model. Defaults to `20`.
    * `decoder_input_details` – Returns
     information about the log probabilities assigned by the
     model to each potential next token and the corresponding
     token IDs. If `decoder_input_details` is set to
     `True`, you must also set
     `details` to `True` in order to
     receive the requested details. Defaults to
     `False`.

For more information about parameters for this `Hugging
 Face` model, see [types.py](https://github.com/huggingface/text-generation-inference/blob/v0.9.3/clients/python/text_generation/types.py#L8 "https://github.com/huggingface/text-generation-inference/blob/v0.9.3/clients/python/text_generation/types.py#L8").

## Send a sample inference request

To test your model, send a sample request to your model and print the
model response as follows:

```
response = predictor.predict(payload)
print(response[0]["generated_text"])
```

In the previous code example, if your model provided the response
`[{"response": "this is the output"}]`, then the
`print` statement returns `this is the
 output`.

## Set up FMEval

1. Load the required libraries to run FMEval as follows:

```
import fmeval
from fmeval.data_loaders.data_config import DataConfig
from fmeval.model_runners.sm_jumpstart_model_runner import JumpStartModelRunner
from fmeval.constants import MIME_TYPE_JSONLINES
from fmeval.eval_algorithms.prompt_stereotyping import PromptStereotyping, PROMPT_STEREOTYPING
from fmeval.eval_algorithms import EvalAlgorithm
```

2. Set up the data configuration for your input dataset.

If you don't use a built-in dataset, your data configuration must
identify the column that contains more bias in
`sent_more_input_location`. You must also identify
the column that contains less bias in
`sent_less_input_location`. If you are using a
built-in dataset from JumpStart, these parameters are passed to
FMEval automatically through the model metadata.

Specify the `sent_more_input_location` and
`sent_less_input_location` columns for a prompt
stereotyping task, the name, uniform resource identifier (URI), and
`MIME` type.

```
config = DataConfig(
dataset_name="crows-pairs_sample",
dataset_uri="crows-pairs_sample.jsonl",
dataset_mime_type=MIME_TYPE_JSONLINES,
sent_more_input_location="sent_more",
sent_less_input_location="sent_less",
category_location="bias_type",
)
```

For more information about column information that other tasks
require, see the **Use a custom input dataset
section** in [Use a
custom input dataset](clarify-foundation-model-evaluate-auto-lib-custom.md#clarify-foundation-model-evaluate-auto-lib-custom-input "clarify-foundation-model-evaluate-auto-lib-custom.md#clarify-foundation-model-evaluate-auto-lib-custom-input"). 3. Set up a custom `ModelRunner` as shown in the following
code example:

```
js_model_runner = JumpStartModelRunner(
endpoint_name=endpoint_name,
model_id=model_id,
model_version=model_version,
output='[0].generated_text',
log_probability='[0].details.prefill[*].logprob',
content_template='{"inputs": $prompt, "parameters":
{"do_sample": true, "top_p": 0.9, "temperature": 0.8, "max_new_tokens": 1024,
"decoder_input_details": true,"details": true}}',
)
```

The previous code example specifies the following:

    * `endpoint_name` – The name of the
     endpoint that you created in the previous **Install required libraries**
     step.
    * `model_id` – The id used to specify your
     model. This parameter was specified when the JumpStart
     model was defined.
    * `model_version` – The version of your
     model used to specify your model. This parameter was
     specified when the JumpStart model was defined.
    * `output` – Captures the output from the
     [Falcon 7b model](https://huggingface.co/tiiuae/falcon-7b "https://huggingface.co/tiiuae/falcon-7b"), which returns its response in
     a `generated_text` key. If your model provided
     the response `[{"generated_text": "this is the
     output"}]`, then `[0].generated_text`
     returns `this is the output`.
    * `log_probability` – Captures the log
     probability returned by this JumpStart model.
    * `content_template` – Specifies how your
     model interacts with requests. The example configuration
     template is detailed solely to explain the previous example,
     and it's not required. The parameters in the content
     template are the same ones that are declared for
     `payload`. For more information about
     parameters for this `Hugging Face` model, see
     [types.py](https://github.com/huggingface/text-generation-inference/blob/v0.9.3/clients/python/text_generation/types.py#L8 "https://github.com/huggingface/text-generation-inference/blob/v0.9.3/clients/python/text_generation/types.py#L8").

4. Configure your evaluation report and save it to a directory as
   shown in the following example code:

```
import os
eval_dir = "results-eval-prompt-stereotyping"
curr_dir = os.getcwd()
eval_results_path = os.path.join(curr_dir, eval_dir) + "/"
os.environ["EVAL_RESULTS_PATH"] = eval_results_path
if os.path.exists(eval_results_path):
print(f"Directory '{eval_results_path}' exists.")
else:
os.mkdir(eval_results_path)
```

5. Set up a parallelization factor as follows:

```
os.environ["PARALLELIZATION_FACTOR"] = "1"
```

A `PARALLELIZATION_FACTOR` is a multiplier for the
number of concurrent batches sent to your compute instance. If your
hardware allows for parallelization, you can set this number to
multiply the number of invocations for your evaluation job. For
example, if you have `100` invocations, and
`PARALLELIZATION_FACTOR` is set to `2`,
then your job will run `200` invocations. You can
increase `PARALLELIZATION_FACTOR` up to `10`,
or remove the variable entirely. To read a blog about how AWS
Lambda uses `PARALLELIZATION_FACTOR` see [New AWS Lambda scaling controls for Kinesis and DynamoDB event
sources](https://aws.amazon.com/blogs/compute/new-aws-lambda-scaling-controls-for-kinesis-and-dynamodb-event-sources/ "https://aws.amazon.com/blogs/compute/new-aws-lambda-scaling-controls-for-kinesis-and-dynamodb-event-sources/").

## Run

your model evaluation

1. Define your evaluation algorithm. The following example shows how
   to define a `PromptStereotyping` algorithm:

```
eval_algo = PromptStereotyping()
```

For examples of algorithms that calculate metrics for other
evaluation tasks, see **Evaluate your
model** in [Use the
fmeval library to run an automatic evaluation](clarify-foundation-model-evaluate-auto-lib.md "clarify-foundation-model-evaluate-auto-lib.md"). 2. Run your evaluation algorithm. The following code example uses the
model and data configuration that was previously defined, and a
`prompt_template` that uses `feature` to
pass your prompt to the model as follows:

```
eval_output = eval_algo.evaluate(model=js_model_runner, dataset_config=config,
prompt_template="$feature", save=True)
```

Your model output may be different than the previous sample
output.

## View your analysis results

1. Parse an evaluation report from the `eval_output`
   object returned by the evaluation algorithm as follows:

```
import json
print(json.dumps(eval_output, default=vars, indent=4))

```

The previous command returns the following output (condensed for
brevity):

```
[
{
    "eval_name": "prompt_stereotyping",
    "dataset_name": "crows-pairs_sample",
    "dataset_scores": [
        {
            "name": "prompt_stereotyping",
            "value": 0.6666666666666666
        }
    ],
    "prompt_template": "$feature",
    "category_scores": [
        {
            "name": "disability",
            "scores": [
                {
                    "name": "prompt_stereotyping",
                    "value": 0.5
                }
            ]
        },
        ...
    ],
    "output_path": "/home/sagemaker-user/results-eval-prompt-stereotyping/prompt_stereotyping_crows-pairs_sample.jsonl",
    "error": null
}
]
```

The previous example output displays an overall score for dataset
following `"name": prompt_stereotyping`. This score is
the normalized difference in log probabilities between the model
response providing **more** versus less
bias. If the score is greater than `0.5`, this means that
your model response is more likely to return a response containing
more bias. If the score is less than `0.5`, your model is
more likely to return a response containing less bias. If the score
is `0.5`, the model response does not contain bias as
measured by the input dataset. You will use the
`output_path` to create a `Pandas`
`DataFrame` in the following step. 2. Import your results and read them into a `DataFrame`,
and attach the prompt stereotyping scores to the model input, model
output, and target output as follows:

```
import pandas as pd
data = []
with open(os.path.join(eval_results_path,
"prompt_stereotyping_crows-pairs_sample.jsonl"), "r") as file:
for line in file:
data.append(json.loads(line))
df = pd.DataFrame(data)
df['eval_algo'] = df['scores'].apply(lambda x: x[0]['name'])
df['eval_score'] = df['scores'].apply(lambda x: x[0]['value'])
df
```

For a notebook that contains the code examples given in this
section, see [jumpstart-falcon-stereotyping.ipnyb](https://github.com/aws/fmeval/blob/main/examples/jumpstart-falcon-stereotyping.ipynb "https://github.com/aws/fmeval/blob/main/examples/jumpstart-falcon-stereotyping.ipynb").
