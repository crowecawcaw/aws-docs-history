# Use the

`fmeval` library to run an automatic evaluation

Using the `fmeval` library in your own code gives you the most
flexibility to customize your work flow. You can use the `fmeval`library
to evaluate any LLM, and also to have more flexibility with your custom input
datasets. The following steps show you how to set up your environment and how to run
both a starting and a customized work flow using the `fmeval`
library.

## Get

started using the `fmeval` library

You can configure your foundation model evaluation and customize it for your
use case in a Studio notebook. Your configuration depends both on the kind
of task that your foundation model is built to predict, and how you want to
evaluate it. FMEval supports open-ended generation, text summarization, question
answering, and classification tasks. The steps in this section show you how to
set up a starting work flow. This starting work flow includes setting up your
environment and running an evaluation algorithm using either a JumpStart or
an Amazon Bedrock foundation model with built-in datasets. If you must use a custom input
dataset and workflow for a more specific use case, see [Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md").

If you don’t want to run a model evaluation in a Studio notebook,
skip to step 11 in the following **Get started using
Studio** section.

###### Prerequisites

- To run a model evaluation in a Studio UI, your AWS Identity and Access Management
  (IAM) role and any input datasets must have the correct
  permissions. If you do not have a SageMaker AI Domain or IAM role, follow
  the steps in [Guide to getting set up with Amazon SageMaker AI](gs.md "gs.md").

###### To set permissions for your Amazon S3 bucket

After your domain and role are created, use the following steps to add
the permissions needed to evaluate your model.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigation pane, enter `S3` into the
   search bar at the top of the page.
3. Choose **S3** under
   **Services**.
4. Choose **Buckets** from the navigation
   pane.
5. In the **General purpose buckets** section, under
   **Name**, choose the name of the S3 bucket that
   you want to use to store your model input and output in the console.
   If you do not have an S3 bucket, do the following:
   1. Select **Create bucket** to open a new
      **Create bucket** page.
   2. In the **General configuration** section,
      under **AWS Region**, select the AWS
      region where your foundation model is located.
   3. Name your S3 bucket in the input box under
      **Bucket name**.
   4. Accept all of the default choices.
   5. Select **Create bucket**.
   6. In the **General purpose buckets**
      section, under **Name**, select the name of
      the S3 bucket that you created.

6. Choose the **Permissions** tab.
7. Scroll to the **Cross-origin resource sharing
   (CORS)** section at the bottom of the window. Choose
   **Edit**.
8. To add permissions to your bucket for foundation evaluations,
   ensure that the following code appears in the input box. You can
   also copy and paste the following into the input box.

```
[
{
    "AllowedHeaders": [
        "*"
    ],
    "AllowedMethods": [
        "GET",
        "PUT",
        "POST",
        "DELETE"
    ],
    "AllowedOrigins": [
        "*"
    ],
    "ExposeHeaders": [
        "Access-Control-Allow-Origin"
    ]
}
]
```

9. Choose **Save changes**.

###### To add permissions to your IAM policy

1. In the search bar at the top of the page, enter
   `IAM`.
2. Under **Services**, select **Identity and
   Access Management (IAM)**.
3. Choose **Policies** from the navigation
   pane.
4. Input [AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess") into the search bar. Select
   the radio button next to the policy that appears. The
   **Actions** button can now be selected.
5. Choose the down arrow next to **Actions**. Two
   options appear.
6. Choose **Attach**.
7. In the IAM listing that appears, search for the name of the role
   you created. Select the check box next to the name.
8. Choose **Attach policy**.

###### Get started using Studio

1. In the search bar at the top of the page, enter
   `SageMaker AI`.
2. Under **Services**, select
   **Amazon SageMaker AI**.
3. Choose **Studio** from the navigation
   pane.
4. Choose your domain from the **Get Started**
   section, after expanding the down arrow under **Select
   Domain**.
5. Choose your user profile from the **Get Started**
   section after expanding the down arrow under **Select user
   profile**.
6. Choose **Open Studio** to open the landing
   page for Studio.
7. Select the file browser from the navigation pane and navigate to
   the root directory.
8. Select **Create notebook**.
9. In the notebook environment dialog box that opens, select the
   **Data Science 3.0** image.
10. Choose **Select**.
11. Install the `fmeval` package in your development
    environment, as shown in the following code example:

```
!pip install fmeval
```

###### Note

Install the `fmeval` library into an environment
that uses Python 3.10. For more information about
requirements needed to run `fmeval` , see [`fmeval` dependencies](https://github.com/aws/fmeval/blob/main/pyproject.toml "https://github.com/aws/fmeval/blob/main/pyproject.toml").
FMEval uses a high-level wrapper called `ModelRunner` to compose
input, invoke and extract output from your model. The `fmeval`
package can evaluate any LLM, however the procedure to configure
`ModelRunner` depends on what kind of model you want to
evaluate. This section explains how to configure `ModelRunner`
for a JumpStart or Amazon Bedrock model. If you want to use a custom input dataset
and custom `ModelRunner`, see [Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md").

### Use a JumpStart model

To use `ModelRunner` to evaluate a JumpStart model,
create or provide an endpoint, define the model and the built-in
dataset, configure, and test `ModelRunner`.

###### Define a JumpStart model and configure a ModelRunner

1.  Provide an endpoint by doing either of the following:

        * Specify the [EndpointName](../APIReference/API_runtime_InvokeEndpoint.md#API_runtime_InvokeEndpoint_RequestSyntax "../APIReference/API_runtime_InvokeEndpoint.md#API_runtime_InvokeEndpoint_RequestSyntax") to an existing JumpStart
         endpoint, the `model_id`, and
         `model_version`.
        * Specify the `model_id` and
         `model_version` for your model, and
         create a JumpStart endpoint.

    The following code example shows how create an endpoint for a
    [Llama 2 foundation model](https://aws.amazon.com/blogs/machine-learning/llama-2-foundation-models-from-meta-are-now-available-in-amazon-sagemaker-jumpstart/ "https://aws.amazon.com/blogs/machine-learning/llama-2-foundation-models-from-meta-are-now-available-in-amazon-sagemaker-jumpstart/") that's
    available through JumpStart.

```
import sagemaker
from sagemaker.jumpstart.model import JumpStartModel

#JumpStart model and version
model_id, model_version = "meta-textgeneration-llama-2-7b-f", "*"

my_model = JumpStartModel(model_id=model_id)
predictor = my_model.deploy()
endpoint_name = predictor.endpoint_name

# Accept the EULA, and test the endpoint to make sure it can predict.
predictor.predict({"inputs": [[{"role":"user", "content": "Hello how are you?"}]]}, custom_attributes='accept_eula=true')
```

The previous code example refers to EULA, which stands for
end-use-license-agreement (EULA). The EULA can be found in the
model card description of the model that you are using. To use
some JumpStart models, you must specify
`accept_eula=true`, as shown in the previous call
to `predict`. For more information about EULA, see
the **Licenses and model sources**
section in [Model sources and license
agreements](jumpstart-foundation-models-choose.md "jumpstart-foundation-models-choose.md")
.

You can find a list of available JumpStart models at
[Built-in Algorithms with pre-trained Model
Table](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html#built-in-algorithms-with-pre-trained-model-table "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html#built-in-algorithms-with-pre-trained-model-table"). 2. Configure `ModelRunner` by using the
`JumpStartModelRunner`, as shown in the following
configuration example:

```
from fmeval.model_runners.sm_jumpstart_model_runner import JumpStartModelRunner

js_model_runner = JumpStartModelRunner(
endpoint_name=endpoint_name,
model_id=model_id,
model_version=model_version
)
```

In the previous configuration example, use the same values for
`endpoint_name`, `model_id`, and
`model_version` that you used to create the
endpoint. 3. Test your `ModelRunner`. Send a sample request to
your model as shown in the following code example:

```
js_model_runner.predict("What is the capital of London")
```

### Use an Amazon Bedrock model

To evaluate an Amazon Bedrock model, you must define the model and built-in
dataset, and configure `ModelRunner`.

###### Define an Amazon Bedrock model and configure a ModelRunner

1. To define and print model details, use the following code
   example for a Titan model that is available through Amazon Bedrock:

```
import boto3
import json
bedrock = boto3.client(service_name='bedrock')
bedrock_runtime = boto3.client(service_name='bedrock-runtime')

model_id = "amazon.titan-tg1-large"
accept = "application/json"
content_type = "application/json"

print(bedrock.get_foundation_model(modelIdentifier=modelId).get('modelDetails'))
```

In the previous code example, the `accept`
parameter specifies the format of the data that you want to use
to evaluate your LLM. The `contentType` specifies the
format of the input data in the request. Only
`MIME_TYPE_JSON` is supported for
`accept` and `contentType` for Amazon Bedrock
models. For more information about these parameters, see [InvokeModelWithResponseStream](../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md#API_runtime_InvokeModelWithResponseStream_RequestSyntax "../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md#API_runtime_InvokeModelWithResponseStream_RequestSyntax"). 2. To configure `ModelRunner`, use the
`BedrockModelRunner`, as shown in the following
configuration example:

```
from fmeval.model_runners.bedrock_model_runner import BedrockModelRunner

bedrock_model_runner = BedrockModelRunner(
model_id=model_id,
output='results[0].outputText',
content_template='{"inputText": $prompt, "textGenerationConfig": \
{"maxTokenCount": 4096, "stopSequences": [], "temperature": 1.0, "topP": 1.0}}',
)
```

Parametrize the `ModelRunner` configuration as
follows.

    * Use the same values for `model_id` that you
     used to deploy the model.
    * Use `output` to specify the format of the
     generated `json` response. As an example, if
     your LLM provided the response `[{"results": "this
     is the output"}]`, then
     `output='results[0].outputText'` returns
     `this is the output`.
    * Use `content_template` to specify how your
     LLM interacts with requests. The following configuration
     template is detailed solely to explain the previous
     configuration example, and it's not required.




    	+ In the previous configuration example, the
    	 variable `inputText` specifies the
    	 prompt, which captures the request made by the
    	 user.
    	+ The variable `textGenerationConfig`
    	 specifies how the LLM generates responses as
    	 follows:




    		- The parameter `maxTokenCount` is
    		 used to limit the length of the response by
    		 limiting the number of tokens returned by the
    		 LLM.
    		- The parameter `stopSequences` is
    		 used to specify a list of character sequences that
    		 tell your LLM to stop generating a response. The
    		 model output is stopped the first time any of the
    		 listed strings are encountered in the output. As
    		 an example, you can use a carriage return sequence
    		 to limit the model response to a single
    		 line.
    		- The parameter `topP` controls the
    		 randomness by limiting the set of tokens to
    		 consider when generating the next token. This
    		 parameter accepts values between `0.0`
    		 and `1.0`. Higher values of
    		 `topP` allow for a set containing a
    		 broader vocabulary and lower values restrict the
    		 set of tokens to more probable words.
    		- The parameter `temperature`
    		 controls the randomness of the generated text, and
    		 accepts positive values. Higher values of
    		 `temperature` instruct the model to
    		 generate more random and diverse responses. Lower
    		 values generate responses that are more
    		 predictable. Typical ranges for
    		 `temperature` lie between
    		 `0.2` and `2.0`.
    	For more information about parameters for a
    	 specific Amazon Bedrock foundation model, see [Inference parameters for foundation
    	 models](../../../bedrock/latest/userguide/model-parameters.md#model-parameters-titan "../../../bedrock/latest/userguide/model-parameters.md#model-parameters-titan").
    The format of the content\_template parameter depends
     on the inputs and parameters supported by your LLM. For
     example, [Anthropic’s Claude 2 model](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2")
     can support the following
     `content_template`:



    ```
    "content_template": "{\"prompt\": $prompt, \"max_tokens_to_sample\": 500}"
    ```

    As another example, the [Falcon
     7b model](https://huggingface.co/tiiuae/falcon-7b "https://huggingface.co/tiiuae/falcon-7b") can support the following
     `content_template`.



    ```
    "content_template": "{\"inputs\": $prompt, \"parameters\":{\"max_new_tokens\": \
    10, \"top_p\": 0.9, \"temperature\": 0.8}}"
    ```

    Lastly, test your `ModelRunner`. Send a
     sample request to your model as shown in the following
     code example:



    ```
    bedrock_model_runner.predict("What is the capital of London?")
    ```

After you configure your data and `ModelRunner`, you can run an
evaluation algorithm on the responses generated by your LLM. To see a list
of all of the available evaluation algorithms, run the following
code:

```
from fmeval.eval_algo_mapping import EVAL_ALGORITHMS
print(EVAL_ALGORITHMS.keys())
```

Each algorithm has both an evaluate and an `evaluate_sample`
method. The `evaluate` method computes a score for the entire
dataset. The `evaluate_sample` method evaluates the score for a
single instance.

The `evaluate_sample` method returns `EvalScore`
objects. `EvalScore` objects contain aggregated scores of how
well your model performed during evaluation. The
`evaluate_sample` method has the following optional
parameters:

- `model_output` – The model response for a single
  request.
- `model_input` – A prompt containing the request
  to your model.
- `target_output` – The expected response from the
  prompt contained in `model_input`.
  The following code example shows how to use the
  `evaluate_sample`:

```
#Evaluate your custom sample
model_output = model_runner.predict("London is the capital of?")[0]
eval_algo.evaluate_sample(target_output="UK<OR>England<OR>United Kingdom", model_output=model_output)
```

The `evaluate` method has the following optional
parameters:

- `model` – An instance of
  `ModelRunner` using the model that you want to
  evaluate.
- `dataset_config` – The dataset configuration. If
  `dataset_config` is not provided, the model is
  evaluated using all of the built-in datasets that are configured for
  this task.
- `prompt_template` – A template used to generate
  prompts. If `prompt_template` is not provided, your model
  is evaluated using a default prompt template.
- `save` – If set to `True`,
  record-wise prompt responses and scores are saved to the file
  `EvalAlgorithmInterface.EVAL_RESULTS_PATH`. Defaults
  to `False`.
- `num_records` – The number of records that are
  sampled randomly from the input dataset for evaluation. Defaults to
  `300`.
  The `evaluate` algorithm returns a list of
  `EvalOutput` objects that can include the following:

- `eval_name` – The name of the evaluation
  algorithm.

`dataset_name` – The name of dataset used by the
evaluation algorithm.

`prompt_template` – A template used to compose
prompts that is consumed if the parameter `model_output`
is not provided in the dataset. For more information, see
`prompt_template` in the **Configure a JumpStart `ModelRunner`
section**.

`dataset_scores` – An aggregated score computed
across the whole dataset.

`category_scores` – A list of
`CategoryScore` objects that contain the scores for
each category in the dataset.

`output_path` – The local path to the evaluation
output. This output contains prompt-responses with record-wise
evaluation scores.

`error` – A string error message for a failed
evaluation job.
The following dimensions are available for model evaluation:

- Accuracy
- Factual knowledge
- Prompt stereotyping
- Semantic robustness
- Toxicity

### Accuracy

You can run an accuracy algorithm for a question answering, text
summarization, or classification task. The algorithms are different for
each task in order to accommodate the different data input types and
problems as follows:

- For question answering tasks, run the `QAAccuracy`
  algorithm with a `QAAccuracyConfig` file.
- For text summarization tasks, run the
  `SummarizationAccuracy` algorithm with a
  `SummarizationAccuracyConfig`.
- For classification tasks, run the
  `ClassificationAccuracy` algorithm with a
  `ClassificationAccuracyConfig`.

The `QAAccuracy` algorithm returns a list of
`EvalOutput` objects that contains one accuracy score for
each sample. To run the question answer accuracy algorithm, instantiate
a `QAAccuracygeConfig` and pass in either
`<OR>` or `None` as the
`target_output_delimiter`. The question answer accuracy
algorithm compares the response that your model generates with a known
response. If you pass in `<OR>` as the target
delimiter, then the algorithm scores the response as correct if it
generates any of the content separated by `<OR>` in the
answer. If you pass `None` or an empty string as the
`target_output_delimiter`, the code throws an
error.

Call the `evaluate` method and pass in your desired
parameters as shown in the following code example:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.qa_accuracy import QAAccuracy, QAAccuracyConfig

eval_algo = QAAccuracy(QAAccuracyConfig(target_output_delimiter="<OR>")))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

The `SummarizationAccuracy` algorithm returns a list of
`EvalOutput` objects that contain scores for [ROUGE-N](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge"), [Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor"), and [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore"). For more information about
these scores, see the Text summarization section in [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md") . To run
the text summarization accuracy algorithm, instantiate a
`SummarizationAccuracyConfig` and pass in the
following:

- Specify the type of [ROUGE](<https://en.wikipedia.org/wiki/ROUGE_(metric)> "https://en.wikipedia.org/wiki/ROUGE_(metric)") metric you want to use in
  your evaluation to `rouge_type`. You can choose
  `rouge1`, `rouge2`, or
  `rougeL`. These metrics compare generated
  summaries to reference summaries. ROUGE-1
  compares the generated summaries and reference summaries using
  overlapping unigrams (sequences of one item such as “the”,
  “is”). ROUGE-2 compares the generated and
  reference summaries using bigrams (groups of two sequences such
  as “the large”, “is home”). ROUGE-L compares the
  longest matching sequence of words. For more information about
  ROUGE, see [ROUGE: A Package for Automatic
  Evaluation of Summaries](https://aclanthology.org/W04-1013.pdf "https://aclanthology.org/W04-1013.pdf").
- Set `use_stemmer_for_rouge` to `True` or
  `False`. A stemmer removes affixes from words
  before comparing them. For example, a stemmer removes the
  affixes from “swimming” and “swam” so that they are both “swim”
  after stemming.
- Set model_type_for_bertscore to the model that you want to use
  to calculate a [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore"). You can choose [ROBERTA_MODEL](https://huggingface.co/docs/transformers/model_doc/roberta "https://huggingface.co/docs/transformers/model_doc/roberta") or the more advanced [MICROSOFT_DEBERTA_MODEL](https://github.com/microsoft/DeBERTa "https://github.com/microsoft/DeBERTa").

Lastly, call the `evaluate` method and pass in your desired
parameters as shown in the following code example:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.summarization_accuracy import SummarizationAccuracy, SummarizationAccuracyConfig

eval_algo = SummarizationAccuracy(SummarizationAccuracyConfig(rouge_type="rouge1",model_type_for_bertscore="MICROSOFT_DEBERTA_MODEL"))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

The `ClassificationAccuracy` algorithm returns a list of
`EvalOutput` objects that contain the classification
accuracy, precision, recall, and balanced accuracy scores for each
sample. For more information about these scores, see the **Classification** section in [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md") . To run
the classification accuracy algorithm, instantiate a
`ClassificationAccuracyConfig` and pass in an averaging
strategy to `multiclass_average_strategy`. You can choose
`micro`, `macro`, `samples`,
`weighted`, or `binary`. The default value is
`micro`. Then, pass in a list containing the names of the
columns that contain the true labels for your classification categories
to valid_labels. Lastly, call the `evaluate` method and pass
in your desired parameters as shown in the following code
example:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.classification_accuracy import ClassificationAccuracy, ClassificationAccuracyConfig

eval_algo = ClassificationAccuracy(ClassificationAccuracyConfig(multiclass_average_strategy="samples",valid_labels=["animal_type","plant_type","fungi_type"]))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

### Factual knowledge

You can run the factual knowledge algorithm for open-ended generation.
To run the factual knowledge algorithm, instantiate a
`FactualKnowledgeConfig` and optionally pass a delimiter
string (by default, this is `<OR>`). The factual
knowledge algorithm compares the response that your model generates with
a known response. The algorithm scores the response as correct if it
generates any of the content separated by the delimiter in the answer.
If you pass `None` as the
`target_output_delimiter`, then the model must generate
the same response as the answer to be scored as correct. Lastly, call
the `evaluate` method and pass in your desired
parameters.

Factual knowledge returns a list of `EvalScore` objects.
These contain aggregated scores on how well your model is able to encode
factual knowledge as described in the **Foundation
model evaluation overview** section. The scores range
between `0` and `1` with the lowest score
corresponding to a lower knowledge of real-world facts.

The following code example shows how to evaluate your LLM using the
factual knowledge algorithm:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.factual_knowledge import FactualKnowledge, FactualKnowledgeConfig

eval_algo = FactualKnowledge(FactualKnowledgeConfig())
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

### Prompt stereotyping

You can run the prompt stereotyping algorithm for open-ended
generation. To run the prompt stereotyping algorithm, your
`DataConfig` must identify the columns in your input
dataset that contain a less stereotypical sentence in
`sent_less_input_location` and a more stereotypical
sentence in `sent_more_output_location`. For more information
about `DataConfig`, see the previous section **2. Configure `ModelRunner`**. Next,
call the `evaluate` method and pass in your desired
parameters.

Prompt stereotyping returns a list of `EvalOutput` objects
that contain a score for each input record and overall scores for each
type of bias. The scores are calculated by comparing the probability of
the more and less stereotypical sentences. The overall score reports how
often the model preferred the stereotypical sentence in that the model
assigns a higher probability to the more stereotypical compared to the
less stereotypical sentence. A score of `0.5` indicates that
your model is unbiased, or that it prefers more and less stereotypical
sentences at equal rates. A score of greater than `0.5`
indicates that your model is likely to generate a response that is more
stereotypical. Scores less than `0.5` indicate that your
model is likely to generate a response that is less
stereotypical.

The following code example shows how to evaluate your LLM using the
prompt stereotyping algorithm:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.prompt_stereotyping import PromptStereotyping

eval_algo = PromptStereotyping()
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

### Semantic robustness

You can run a semantic robustness algorithm for any FMEval task,
however your model should be deterministic. A deterministic model is one
that always generate the same output for the same input. One may
typically achieve determinism by setting a random seed in the decoding
process. The algorithms are different for each task in order to
accommodate the different data input types and problems as
follows:

- For open-ended generation, question answering, or task
  classification run the `GeneralSemanticRobustness`
  algorithm with a `GeneralSemanticRobustnessConfig`
  file.
- For text summarization, run the
  `SummarizationAccuracySemanticRobustness`
  algorithm with a
  `SummarizationAccuracySemanticRobustnessConfig`
  file.

The `GeneralSemanticRobustness` algorithm returns a list of
`EvalScore` objects that contain accuracy with values
between `0` and `1` quantifying the difference
between the perturbed and unperturbed model outputs. To run the general
semantic robustness algorithm, instantiate a
`GeneralSemanticRobustnessConfig` and pass in a
`perturbation_type`. You can choose one of the following
for `perturbation_type`:

- `Butterfinger` – A perturbation that mimics
  spelling mistakes using character swaps based on keyboard
  distance. Input a probability that a given character is
  perturbed. Butterfinger is the default value for
  `perturbation_type`.
- `RandomUpperCase` – A perturbation that
  changes a fraction of characters to uppercase. Input a decimal
  from `0` to `1`.
- `WhitespaceAddRemove` – The probability that
  a white space character is added in front of a non-white space
  character into white.

You can also specify the following parameters:

- `num_perturbations` – The number of
  perturbations for each sample to introduce into the generated
  text. The default is `5`.
- `butter_finger_perturbation_prob` – The
  probability that a character is be perturbed. Used only when
  `perturbation_type` is `Butterfinger`.
  The default is `0.1`.
- `random_uppercase_corrupt_proportion` – The
  fraction of characters to be changed to uppercase. Used only
  when `perturbation_type` is
  `RandomUpperCase`. The default is
  `0.1`.
- `whitespace_add_prob` – Given a white space,
  the probability of removing it from a sample. Used only when
  `perturbation_type` is
  `WhitespaceAddRemove`. The default is
  `0.05`.
- `whitespace_remove_prob` – Given a non-white
  space, the probability of adding a white space in front of it.
  Used only when `perturbation_type` is
  `WhitespaceAddRemove`. The default is
  `0.1`.

Lastly, call the `evaluate` method and pass in your desired
parameters as shown in the following code example:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.general_semantic_robustness import GeneralSemanticRobustness, GeneralSemanticRobustnessConfig

eval_algo = GeneralSemanticRobustness(GeneralSemanticRobustnessConfig(perturbation_type="RandomUpperCase",num_perturbations=2,random_uppercase_corrupt_proportion=0.3)))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

The `SummarizationAccuracySemanticRobustness` algorithm
returns a list of `EvalScore` objects that contain the
difference (or delta) between the [ROUGE-N](https://huggingface.co/spaces/evaluate-metric/rouge "https://huggingface.co/spaces/evaluate-metric/rouge"), [Meteor](https://huggingface.co/spaces/evaluate-metric/meteor "https://huggingface.co/spaces/evaluate-metric/meteor"), and [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore") values between the generated
and reference summaries. For more information about these scores, see
the **Text summarization** section in [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md") . To run
the text summarization semantic robustness algorithm, instantiate a
`SummarizationAccuracySemanticRobustnessConfig` and pass
in a `perturbation_type`.

You can choose one of the following for
`perturbation_type`:

- `Butterfinger` – A perturbation that mimics
  spelling mistakes using character swaps based on keyboard
  distance. Input a probability that a given character is
  perturbed. `Butterfinger` is the default value for
  `perturbation_type`.
- `RandomUpperCase` – A perturbation that
  changes a fraction of characters to uppercase. Input a decimal
  from `0` to `1`.
- `WhitespaceAddRemove` – Input a probability
  that a white space character is added in front of a non-white
  space character into white.

You can also specify the following parameters:

- `num_perturbations` – The number of
  perturbations for each sample to introduce into the generated
  text. Default is `5`.
- `butter_finger_perturbation_prob` – The
  probability that a character is perturbed. Used only when
  `perturbation_type` is `Butterfinger`.
  Default is `0.1`.
- `random_uppercase_corrupt_proportion` – The
  fraction of characters to be changed to uppercase. Used only
  when `perturbation_type` is
  `RandomUpperCase`. Default is
  `0.1`.
- `whitespace_add_prob` – Given a white space,
  the probability of removing it from a sample. Used only when
  `perturbation_type` is
  `WhitespaceAddRemove`. Default is
  `0.05`.
- `whitespace_remove_prob` – Given a non-white
  space, the probability of adding a white space in front of it.
  Used only when `perturbation_type` is
  `WhitespaceAddRemove`, Default is
  `0.1`.
- `rouge_type` – Metrics that compare
  generated summaries to reference summaries. Specify the type of
  [ROUGE](<https://en.wikipedia.org/wiki/ROUGE_(metric)> "https://en.wikipedia.org/wiki/ROUGE_(metric)") metric you want to use in
  your evaluation to `rouge_type`. You can choose
  `rouge1`, `rouge2`, or
  `rougeL`. ROUGE-1 compares the
  generated summaries and reference summaries using overlapping
  unigrams (sequences of one item such as “the”, “is”).
  ROUGE-2 compares the generated and reference
  summaries using bigrams (groups of two sequences such as “the
  large”, “is home”). ROUGE-L compares the longest
  matching sequence of words. For more information about
  ROUGE, see [ROUGE: A Package for Automatic
  Evaluation of Summaries](https://aclanthology.org/W04-1013.pdf "https://aclanthology.org/W04-1013.pdf").
- Set `user_stemmer_for_rouge` to `True`
  or `False`. A stemmer removes affixes from words
  before comparing them. For example, a stemmer removes the
  affixes from “swimming” and “swam” so that they are both “swim”
  after stemming.
- Set `model_type_for_bertscore` to the model that
  you want to use to calculate a [BERTScore](https://huggingface.co/spaces/evaluate-metric/bertscore "https://huggingface.co/spaces/evaluate-metric/bertscore"). You can choose [ROBERTA_MODEL](https://huggingface.co/docs/transformers/model_doc/roberta "https://huggingface.co/docs/transformers/model_doc/roberta") or the more advanced [MICROSOFT_DEBERTA_MODEL](https://github.com/microsoft/DeBERTa "https://github.com/microsoft/DeBERTa").

Call the `evaluate` method and pass in your desired
parameters as shown in the following code example:

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.summarization_accuracy_semantic_robustness import SummarizationAccuracySemanticRobustness, SummarizationAccuracySemanticRobustnessConfig

eval_algo = SummarizationAccuracySemanticRobustness(SummarizationAccuracySemanticRobustnessConfig(perturbation_type="Butterfinger",num_perturbations=3,butter_finger_perturbation_prob=0.2)))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```

### Toxicity

You can run the a toxicity algorithm for open-ended generation, text
summarization, or question answering. There are three distinct classes
depending on the task.

- For open-ended generation, run the Toxicity algorithm with a
  `ToxicityConfig` file.
- For summarization, use the class
  `Summarization_Toxicity`.
- For question answering, use the class
  `QAToxicity`.

The toxicity algorithm returns one or more a list of
`EvalScore` objects (depending on the toxicity detector)
that contain scores between `0` and `1`. To run
the toxicity algorithm, instantiate a `ToxicityConfig` and
pass in a toxicity model to use to evaluate your model against in
`model_type`. You can choose the following for
`model_type`:

- [`detoxify`
  for UnitaryAI Detoxify-unbiased](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify"), a multilabel text
  classifier trained on [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge "https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge") and [Jigsaw Unintended Bias in Toxicity Classification](https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification "https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification").
  The model provides `7` scores for the following
  classes: toxicity, severe toxicity, obscenity, threat, insult,
  sexual explicity and identity attack.

The following is example output from the detoxity
model:

```
EvalScore(name='toxicity', value=0.01936926692724228),

EvalScore(name='severe_toxicity', value=3.3755677577573806e-06),

EvalScore(name='obscene', value=0.00022437423467636108),

EvalScore(name='identity_attack', value=0.0006707844440825284),

EvalScore(name='insult', value=0.005559926386922598),

EvalScore(name='threat', value=0.00016682750720065087),

EvalScore(name='sexual_explicit', value=4.828436431125738e-05)
```

- [`toxigen`
  for Toxigen-roberta](https://github.com/microsoft/TOXIGEN "https://github.com/microsoft/TOXIGEN"), a binary RoBERTa-based text
  classifier fine-tuned on the ToxiGen dataset, which contains
  sentences with subtle and implicit toxicity pertaining to
  `13` minority groups.

Lastly, call the `evaluate` method and pass in your desired
parameters as shown in the following code example.

```
from fmeval.eval import get_eval_algorithm
from fmeval.eval_algorithms.toxicity import Toxicity, ToxicityConfig

eval_algo = Toxicity(ToxicityConfig(model_type="detoxify"))
eval_output = eval_algo.evaluate(model=model_runner, dataset_config=config, prompt_template="$feature", save=True)
```
