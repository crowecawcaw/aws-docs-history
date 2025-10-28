#

Evaluate an Amazon Bedrock model for text summarization accuracy

You can use a high-level `ModelRunner` wrapper to create a custom
evaluation based on a model that is hosted outside of JumpStart.

This tutorial shows how to load the [Anthropic Claude 2
model](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2"), which is available in Amazon Bedrock, and ask this model to summarize
text prompts. Then, this tutorial shows how to evaluate the model response for
accuracy using the [Rouge-L](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge"), [Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor"), and [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore") metrics.

The tutorials show how to do the following:

- Set up your environment.
- Run your model evaluation.
- View your analysis results.

## Set up your environment

###### Prerequisites

- Use a base Python 3.10 kernel environment and an
  `ml.m5.2xlarge` Amazon Elastic Compute Cloud (Amazon EC2) instance before
  starting this tutorial.

For additional information about instance types and their
recommended use cases, see [Instance Types Available for Use With
Amazon SageMaker Studio Classic Notebooks](notebooks-available-instance-types.md "notebooks-available-instance-types.md").

###### Set up Amazon Bedrock

Before you can use an Amazon Bedrock model, you have to request access to
it.

1. Sign into your AWS account.
   1. If you do not have an AWS account, see [Sign up for an AWS account](../../../bedrock/latest/userguide/setting-up.md#sign-up-for-aws "../../../bedrock/latest/userguide/setting-up.md#sign-up-for-aws") in **Set up Amazon Bedrock**.

2. Open the [Amazon Bedrock
   console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
3. In the **Welcome to Amazon Bedrock!** section
   that opens, choose **Manage model access**.
4. In the **Model access** section that
   appears, choose **Manage model access**.
5. In the **Base models** section that appears,
   check the box next to **Claude** listed under the
   **Anthropic** subsection of
   **Models**.
6. Choose **Request model access**.
7. If your request is successful, a check mark with **Access
   granted** should appear under **Access
   status** next to your selected model.
8. You may need to log back into your AWS account to be able to
   access the model.

###### Install required libraries

1. In your code, install the `fmeval` and
   `boto3` libraries as follows:

```
!pip install fmeval
!pip3 install boto3==1.28.65
```

2. Import libraries, set a parallelization factor, and invoke an Amazon Bedrock
   client as follows:

```
import boto3
import json
import os

# Dependent on available hardware and memory
os.environ["PARALLELIZATION_FACTOR"] = "1"

# Bedrock clients for model inference
bedrock = boto3.client(service_name='bedrock')
bedrock_runtime = boto3.client(service_name='bedrock-runtime')
```

In the previous code example, the following applies:

    * `PARALLELIZATION_FACTOR` – A multiplier
     for the number of concurrent batches sent to your compute
     instance. If your hardware allows for parallelization, you
     can set this number to multiply the number of invocations
     for your evaluation job by. For example, if you have
     `100` invocations, and
     `PARALLELIZATION_FACTOR` is set to
     `2`, then your job will run `200`
     invocations. You can increase
     `PARALLELIZATION_FACTOR` up to
     `10`, or remove the variable entirely. To
     read a blog about how AWS Lambda uses
     `PARALLELIZATION_FACTOR` see [New Lambda scaling controls for Kinesis and
     DynamoDB event sources](https://aws.amazon.com/blogs/compute/new-aws-lambda-scaling-controls-for-kinesis-and-dynamodb-event-sources/ "https://aws.amazon.com/blogs/compute/new-aws-lambda-scaling-controls-for-kinesis-and-dynamodb-event-sources/").

3. Download the sample `JSON Lines` dataset, [sample-dataset.jsonl](https://github.com/aws/fmeval/blob/8da27af2f20369fd419c03d5bb0707ab24010b14/examples/xsum_sample.jsonl "https://github.com/aws/fmeval/blob/8da27af2f20369fd419c03d5bb0707ab24010b14/examples/xsum_sample.jsonl"), into your current working
   directory.
4. Check that your environment contains the sample input file as
   follows:

```
import glob

# Check for the built-in dataset
if not glob.glob("sample-dataset.jsonl"):
print("ERROR - please make sure file exists: sample-dataset.jsonl")
```

###### Send a sample inference request to your model

1. Define the model and the `MIME` type of your prompt.
   For an [Anthropic Claude 2 model](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2") hosted on Amazon Bedrock, your prompt
   must be structured as follows:

```
import json
model_id = 'anthropic.claude-v2'
accept = "application/json"
contentType = "application/json"
# Ensure that your prompt has the correct format
prompt_data = """Human: Who is Barack Obama?
Assistant:
"""
```

For more information about how to structure the body of your
request, see [Model invocation request body field](../../../bedrock/latest/userguide/model-parameters-claude.md#model-parameters-claude-request-body "../../../bedrock/latest/userguide/model-parameters-claude.md#model-parameters-claude-request-body"). Other models may
have different formats. 2. Send a sample request to your model. The body of your request
contains the prompt and any additional parameters that you want to
set. A sample request with the `max_tokens_to_sample` set
to `500` follows:

```
body = json.dumps({"prompt": prompt_data, "max_tokens_to_sample": 500})
response = bedrock_runtime.invoke_model(
body=body, modelId=model_id, accept=accept, contentType=contentType
)
response_body = json.loads(response.get("body").read())
print(response_body.get("completion"))
```

In the previous code example, you can set the following
parameters:

    * `temperature` – Controls the randomness
     of the generated text, and accepts positive values. Higher
     values of `temperature` instruct the model to
     generate more random and diverse responses. Lower values
     generate responses that are more predictable. Ranges for
     `temperature` lie between `0` and
     `1`, with a default value of 0.5.
    * `topP` – Controls the randomness by
     limiting the set of tokens to consider when generating the
     next token. Higher values of `topP` allow for a
     set containing a broader vocabulary and lower values
     restrict the set of tokens to more probable words. Ranges
     for `topP` are `0` to `1`,
     with a default value of `1`.
    * `topK` – Limits the model predictions to
     the top `k` most probable tokens. Higher values
     of `topK` allow for more inventive responses.
     Lower values generate responses that are more coherent.
     Ranges for `topK` are `0` to
     `500`, with a default value of
     `250`.
    * `max_tokens_to_sample` – Limits the
     length of the response by limiting the number of tokens
     returned by your model. Ranges for
     `max_tokens_to_sample` are `0` to
     `4096`, with a default value of
     `200`.
    * `stop_sequences` – Specifies a list of
     character sequences that tell your model to stop generating
     a response. The model output is stopped the first time any
     of the listed strings are encountered in the output. The
     response does not contain the stop sequence. For example,
     you can use a carriage return sequence to limit the model
     response to a single line. You can configure up to
     `4` stop sequences.

For more information about the parameters that you can specify in
a request, see [Anthropic Claude models](../../../bedrock/latest/userguide/model-parameters-claude.md "../../../bedrock/latest/userguide/model-parameters-claude.md").

###### Set up FMEval

1. Load the required libraries to run FMEval as follows:

```
from fmeval.data_loaders.data_config import DataConfig
from fmeval.model_runners.bedrock_model_runner import BedrockModelRunner
from fmeval.constants import MIME_TYPE_JSONLINES
from fmeval.eval_algorithms.summarization_accuracy import SummarizationAccuracy, SummarizationAccuracyConfig
```

2. Set up the data configuration for your input dataset.

The following sample input is one line from
`sample-dataset.jsonl`:

```
{
"document": "23 October 2015 Last updated at 17:44
    BST\nIt's the highest rating a tropical storm
    can get and is the first one of this magnitude
    to hit mainland Mexico since 1959.\nBut how are
    the categories decided and what do they mean?
    Newsround reporter Jenny Lawrence explains.",
"summary": "Hurricane Patricia has been rated as
    a category 5 storm.",
"id": "34615665",
}
```

The previous sample input contains the text to summarize inside
the `document` key. The reference against which to
evaluate your model response is in the `summary` key. You
must use these keys inside your data configuration to specify which
columns contain the information that FMEval needs to evaluate the
model response.

Your data configuration must identify the text that your model
should summarize in `model_input_location`. You must
identify the reference value with
`target_output_location`.

The following data configuration example refers to the previous
input example to specify the columns required for a text
summarization task, the name, uniform resource identifier (URI), and
`MIME` type:

```
config = DataConfig(
dataset_name="sample-dataset",
dataset_uri="sample-dataset.jsonl",
dataset_mime_type=MIME_TYPE_JSONLINES,
model_input_location="document",
target_output_location="summary"
)
```

For more information about the column information required for
other tasks, see the **Use a custom input
dataset** section in [Automatic model evaluation](clarify-foundation-model-evaluate-auto.md "clarify-foundation-model-evaluate-auto.md"). 3. Set up a custom `ModelRunner` as shown in the following
code example:

```
bedrock_model_runner = BedrockModelRunner(
model_id=model_id,
output='completion',
content_template='{"prompt": $prompt, "max_tokens_to_sample": 500}'
)
```

The previous code example specifies the following:

    * `model_id` – The id used to specify your
     model.
    * `output` – Captures the output from the
     [Anthropic Claude 2](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2") model, which returns its
     response in a `completion` key.
    * `content_template` – Specifies how your
     model interacts with requests. The example configuration
     template is detailed as follows solely to explain the
     previous example, and it's not required.




    	+ In the previous `content_template`
    	 example, the following apply:




    		- The variable `prompt` specifies
    		 the input prompt, which captures the request made
    		 by the user.
    		- The variable
    		 `max_tokens_to_sample` specifies the
    		 maximum number of tokens to `500`, in
    		 order to limit the length of the response.


    		For more information about the parameters
    		 that you can specify in your request, see [Anthropic Claude models](../../../bedrock/latest/userguide/model-parameters-claude.md "../../../bedrock/latest/userguide/model-parameters-claude.md").
    	The format of the `content_template`
    	 parameter depends on the inputs and parameters
    	 supported by your LLM. In this tutorial, [Anthropic’s Claude 2 model](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2") uses the
    	 following `content_template`:



    	```
    	   "content_template": "{\"prompt\": $prompt, \"max_tokens_to_sample\": 500}"
    	```

    	As another example, the [Falcon 7b model](https://huggingface.co/tiiuae/falcon-7b "https://huggingface.co/tiiuae/falcon-7b") can support the following
    	 `content_template`:



    	```
    	"content_template": "{\"inputs\": $prompt, \"parameters\":{\"max_new_tokens\": \
    	10, \"top_p\": 0.9, \"temperature\": 0.8}}"
    	```

## Run your model evaluation

###### Define and run your evaluation algorithm

1. Define your evaluation algorithm. The following example shows how
   to define a `SummarizationAccuracy` algorithm, which is
   used to determine accuracy for text summarization tasks:

```
eval_algo = SummarizationAccuracy(SummarizationAccuracyConfig())
```

For examples of algorithms that calculate metrics for other
evaluation tasks, see **Evaluate your
model** in [Use the
fmeval library to run an automatic evaluation](clarify-foundation-model-evaluate-auto-lib.md "clarify-foundation-model-evaluate-auto-lib.md"). 2. Run your evaluation algorithm. The following code example uses the
data configuration that was previously defined, and a
`prompt_template` that uses the `Human`
and `Assistant` keys:

```
eval_output = eval_algo.evaluate(model=bedrock_model_runner,
dataset_config=config,
prompt_template="Human: $feature\n\nAssistant:\n", save=True)
```

In the previous code example, `feature` contains the
prompt in the format that Amazon Bedrock model expects.

## View your analysis results

1. Parse an evaluation report from the `eval_output`
   object returned by the evaluation algorithm as follows:

```
# parse report
print(json.dumps(eval_output, default=vars, indent=4))
```

The previous command returns the following output:

```
[
{
    "eval_name": "summarization_accuracy",
    "dataset_name": "sample-dataset",
    "dataset_scores": [
        {
            "name": "meteor",
            "value": 0.2048823008681274
        },
        {
            "name": "rouge",
            "value": 0.03557697913367101
        },
        {
            "name": "bertscore",
            "value": 0.5406564395678671
        }
    ],
    "prompt_template": "Human: $feature\n\nAssistant:\n",
    "category_scores": null,
    "output_path": "/tmp/eval_results/summarization_accuracy_sample_dataset.jsonl",
    "error": null
}
]
```

The previous example output displays the three accuracy scores:
[Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor"), [Rouge](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge"), and [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore"), the input
`prompt_template`, a `category_score` if
you requested one, any errors, and the `output_path`. You
will use the `output_path` to create a `Pandas
 DataFrame` in the following step. 2. Import your results and read them into a `DataFrame`,
and attach the accuracy scores to the model input, model output, and
target output as follows:

```
import pandas as pd

data = []
with open("/tmp/eval_results/summarization_accuracy_sample_dataset.jsonl", "r") as file:
for line in file:
    data.append(json.loads(line))
df = pd.DataFrame(data)
df['meteor_score'] = df['scores'].apply(lambda x: x[0]['value'])
df['rouge_score'] = df['scores'].apply(lambda x: x[1]['value'])
df['bert_score'] = df['scores'].apply(lambda x: x[2]['value'])
df
```

In this invocation, the previous code example returns the
following output (contracted for brevity):

```
model_input     model_output     target_output     prompt     scores     meteor_score     rouge_score     bert_score
0     John Edward Bates, formerly of Spalding, Linco...     I cannot make any definitive judgments, as th...     A former Lincolnshire Police officer carried o...     Human: John Edward Bates, formerly of Spalding...     [{'name': 'meteor', 'value': 0.112359550561797...     0.112360     0.000000     0.543234 ...
1     23 October 2015 Last updated at 17:44 BST\nIt'...     Here are some key points about hurricane/trop...     Hurricane Patricia has been rated as a categor...     Human: 23 October 2015 Last updated at 17:44 B...     [{'name': 'meteor', 'value': 0.139822692925566...     0.139823     0.017621     0.426529 ...
2     Ferrari appeared in a position to challenge un...     Here are the key points from the article:\n\n...     Lewis Hamilton stormed to pole position at the...     Human: Ferrari appeared in a position to chall...     [{'name': 'meteor', 'value': 0.283411142234671...     0.283411     0.064516     0.597001 ...
3     The Bath-born player, 28, has made 36 appearan...     Okay, let me summarize the key points from th...     Newport Gwent Dragons number eight Ed Jackson ...     Human: The Bath-born player, 28, has made 36 a...     [{'name': 'meteor', 'value': 0.089020771513353...     0.089021     0.000000     0.533514 ...
...
```

Your model output may be different than the previous sample
output.

For a notebook that contains the code examples given in this
section, see [bedrock-claude-summarization-accuracy.ipnyb](https://github.com/aws/fmeval/blob/main/examples/bedrock-claude-summarization-accuracy.ipynb "https://github.com/aws/fmeval/blob/main/examples/bedrock-claude-summarization-accuracy.ipynb").
