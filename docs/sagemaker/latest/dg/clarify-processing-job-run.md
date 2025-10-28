# Run SageMaker Clarify Processing Jobs for Bias Analysis and

Explainability

To analyze your data and models for bias and explainability using SageMaker Clarify, you must
configure a SageMaker Clarify processing job. This guide shows how to configure the job inputs, outputs,
resources, and analysis configuration using the SageMaker Python SDK API
`SageMakerClarifyProcessor`.

The API acts as a high-level wrapper of the SageMaker AI `CreateProcessingJob` API. It
hides many of the details that are involved in setting up a SageMaker Clarify processing job. The
details to set up a job include retrieving the SageMaker Clarify container image URI and generating the
analysis configuration file. The following steps show you how to configure, initialize and
launch a SageMaker Clarify processing job.

###### Configure a SageMaker Clarify processing job using the API

1.  Define the configuration objects for each portion of the job configuration. These
    portions can include the following:

        * The input dataset and output location: [DataConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.DataConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.DataConfig").
        * The model or endpoint to be analyzed: [ModelConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.ModelConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.ModelConfig").
        * Bias analysis parameters: [BiasConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.BiasConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.BiasConfig").
        * SHapley Additive exPlanations (SHAP) analysis parameters:
         [SHAPConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SHAPConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SHAPConfig").
        * Asymmetric Shapley value analysis parameters (for time series only):
         [AsymmetricShapleyValueConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.AsymmetricShapleyValueConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.AsymmetricShapleyValueConfig").

    The configuration objects for a SageMaker Clarify processing job vary for different types of
    data formats and use cases. Configuration examples for tabular data in [CSV](#clarify-processing-job-run-tabular-csv "#clarify-processing-job-run-tabular-csv") and [JSON Lines](#clarify-processing-job-run-tabular-jsonlines "#clarify-processing-job-run-tabular-jsonlines") format, natural
    language processing ([NLP](#clarify-processing-job-run-tabular-nlp "#clarify-processing-job-run-tabular-nlp")),
    [computer vision](#clarify-processing-job-run-cv "#clarify-processing-job-run-cv") (CV), and time series (TS)
    problems are provided in the
    following sections.

2.  Create a `SageMakerClarifyProcessor` object and initialize it with
    parameters that specify the job resources. These resources include parameters such
    as the number of compute instances to use.

The following code example shows how to create a
`SageMakerClarifyProcessor` object and instruct it to use one
`ml.c4.xlarge` compute instance to do the analysis.

```
from sagemaker import clarify

clarify_processor = clarify.SageMakerClarifyProcessor(
    role=role,
    instance_count=1,
    instance_type='ml.c4.xlarge',
    sagemaker_session=session,
)
```

3.  Call the specific run method of the [SageMakerClarifyProcessor](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SageMakerClarifyProcessor.run "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SageMakerClarifyProcessor.run") object with the configuration objects for
    your use case to launch the job. These run methods include the following:

        * `run_pre_training_bias`
        * `run_post_training_bias`
        * `run_bias`
        * `run_explainability`
        * `run_bias_and_explainability`

    This `SageMakerClarifyProcessor` handles several tasks behind the
    scenes. These tasks include retrieving the SageMaker Clarify container image universal resource
    identifier (URI), composing an analysis configuration file based on the provided
    configuration objects, uploading the file to an Amazon S3 bucket, and [configuring the SageMaker Clarify processing job](clarify-processing-job-configure-parameters.md "clarify-processing-job-configure-parameters.md").

The following expandable sections show how to compute **pre-training** and **post-training bias
metrics**, **SHAP values**,
and **partial dependence plots** (PDPs).
The sections show feature importance for these data types:

    * Tabular datasets in CSV format or JSON Lines format
    * Natural language processing (NLP) datasets
    * Computer vision datasets

A guide to run parallel SageMaker Clarify processing jobs with distributed training using **Spark** follows the expandable sections.

The following examples show how to configure bias analysis and explainability
analysis for a tabular dataset in CSV format. In these examples, the incoming
dataset has four feature columns and one binary label column, `Target`.
The contents of the dataset are as follows. A label value of `1`
indicates a positive outcome.

```
Target,Age,Gender,Income,Occupation
0,25,0,2850,2
1,36,0,6585,0
1,22,1,1759,1
0,48,0,3446,1
...
```

This `DataConfig` object specifies the input dataset and where to store
the output. The `s3_data_input_path` parameter can either be a URI of a
dataset file or an Amazon S3 URI prefix. If you provide a S3 URI prefix, the SageMaker Clarify
processing job recursively collects all Amazon S3 files located under the prefix. The
value for `s3_output_path` should be an S3 URI prefix to hold the
analysis results. SageMaker AI uses the `s3_output_path` while compiling, and
cannot take a value of a SageMaker AI Pipeline parameter, property, expression, or
`ExecutionVariable`, which are used during runtime. The following
code example shows how to specify a data configuration for the previous sample input
dataset.

```
data_config = clarify.DataConfig(
    s3_data_input_path=dataset_s3_uri,
    dataset_type='text/csv',
    headers=[`'Target', 'Age', 'Gender', 'Income', 'Occupation'`],
    label='Target',
    s3_output_path=clarify_job_output_s3_uri,
)
```

### How to

compute all pre-training bias metrics for a CSV dataset

The following code sample shows how to configure a `BiasConfig`
object to measure bias of the previous sample input towards samples with a
`Gender` value of `0`.

```
bias_config = clarify.BiasConfig(
    label_values_or_threshold=[1],
    facet_name='`Gender`',
    facet_values_or_threshold=[0],
)
```

The following code example shows how to use a run statement to launch a SageMaker Clarify
processing job that computes all [pre-training bias
metrics](clarify-measure-data-bias.md "clarify-measure-data-bias.md") for an input dataset.

```
clarify_processor.run_pre_training_bias(
     data_config=data_config,
    data_bias_config=bias_config,
    methods="all",
)
```

Alternatively, you can choose which metrics to compute by assigning a list of
pre-training bias metrics to the methods parameter. For example, replacing
`methods="all"` with `methods=["CI", "DPL"]` instructs
the SageMaker Clarify Processor to compute only [Class
Imbalance](clarify-bias-metric-class-imbalance.md "clarify-bias-metric-class-imbalance.md") and [Difference in Proportions of Labels](clarify-data-bias-metric-true-label-imbalance.md "clarify-data-bias-metric-true-label-imbalance.md").

### How to

compute all post-training bias metrics for a CSV dataset

You can compute pre-training bias metrics prior to training. However, to
compute [post-training bias metrics](clarify-measure-post-training-bias.md "clarify-measure-post-training-bias.md"), you must have a trained model. The
following example output is from a binary classification model that outputs data
in CSV format. In this example output, each row contains two columns. The first
column contains the predicted label, and the second column contains the
probability value for that label.

```
0,0.028986845165491
1,0.825382471084594
...
```

In the following example configuration, the `ModelConfig` object
instructs the job to deploy the SageMaker AI model to an ephemeral endpoint. The
endpoint uses one `ml.m4.xlarge` inference instance. Because the
parameter `content_type` and `accept_type` are not set,
they automatically use the value of the parameter `dataset_type`,
which is `text/csv`.

```
model_config = clarify.ModelConfig(
    model_name=your_model,
    instance_type='ml.m4.xlarge',
    instance_count=1,
)
```

The following configuration example uses a
`ModelPredictedLabelConfig` object with a label index of
`0`. This instructs the SageMaker Clarify processing job to locate the
predicted label in the first column of the model output. The Processing job uses
zero-based indexing in this example.

```
predicted_label_config = clarify.ModelPredictedLabelConfig(
    label=0,
)
```

Combined with the previous configuration example, the following code example
launches a SageMaker Clarify processing job to compute all the post-training bias
metrics.

```
clarify_processor.run_post_training_bias(
    data_config=data_config,
    data_bias_config=bias_config,
    model_config=model_config,
    model_predicted_label_config=predicted_label_config,
    methods="all",
)
```

Similarly, you can choose which metrics to compute by assigning a list of
post-training bias metrics to the `methods` parameter. For example,
replace `methods=“all”` with `methods=["DPPL", "DI"]` to
compute only [Difference in Positive Proportions in Predicted Labels](clarify-post-training-bias-metric-dppl.md "clarify-post-training-bias-metric-dppl.md") and [Disparate Impact](clarify-post-training-bias-metric-di.md "clarify-post-training-bias-metric-di.md").

### How to compute all

bias metrics for a CSV dataset

The following configuration example shows how to run all pre-training and
post-training bias metrics in one SageMaker Clarify processing job.

```
clarify_processor.run_bias(
    data_config=data_config,
     bias_config=bias_config,
     model_config=model_config,
    model_predicted_label_config=predicted_label_config,
    pre_training_methods="all",
    post_training_methods="all",
)
```

For an example notebook with instructions on how to run a SageMaker Clarify processing job in
SageMaker Studio Classic to detect bias, see [Fairness and Explainability with SageMaker Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.ipynb").

### How to compute

SHAP values for a CSV dataset

SageMaker Clarify provides feature attributions using the [KernelSHAP algorithm](https://arxiv.org/abs/1705.07874 "https://arxiv.org/abs/1705.07874").
SHAP analysis requires the probability value or score instead
of predicted label, so this `ModelPredictedLabelConfig` object has
probability index `1`. This instructs the SageMaker Clarify processing job to
extract the probability score from the second column of the model output (using
zero-based indexing).

```
probability_config = clarify.ModelPredictedLabelConfig(
    probability=1,
)
```

The `SHAPConfig` object provides SHAP analysis
parameters. In this example, the SHAP
`baseline` parameter is omitted and the value of the
`num_clusters` parameter is `1`. This instructs the
SageMaker Clarify Processor to compute one SHAP baseline sample based on
clustering the input dataset. If you want to choose the baseline dataset, see
[SHAP Baselines for Explainability](clarify-feature-attribute-shap-baselines.md "clarify-feature-attribute-shap-baselines.md").

```
shap_config = clarify.SHAPConfig(
    num_clusters=1,
)
```

The following code example launches a SageMaker Clarify processing job to compute
SHAP values.

```
clarify_processor.run_explainability(
    data_config=data_config,
    model_config=model_config,
    model_scores=probability_config,
    explainability_config=shap_config,
)
```

For an example notebook with instructions on how to run a SageMaker Clarify processing job
in SageMaker Studio Classic to compute SHAP values, see [Fairness and Explainability with SageMaker Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.ipynb").

### How to compute

partial dependence plots (PDPs) for a CSV dataset

PDPs show the dependence of the predicted target response on
one or more input features of interest while holding all other features
constant. An upward sloping line, or curve in the PDP, indicates that the
relationship between the target and input feature(s) is positive, and the
steepness indicates the strength of the relationship. A downward sloping line or
curve indicates that if an input feature decreases, the target variable
increases. Intuitively, you can interpret the partial dependence as the response
of the target variable to each input feature of interest.

The following configuration example is for using a `PDPConfig`
object to instruct the SageMaker Clarify processing job to compute the importance of the
`Income` feature.

```
pdp_config = clarify.PDPConfig(
    features=["Income"],
    grid_resolution=10,
)
```

In the previous example, the `grid_resolution` parameter divides
the range of the `Income` feature values into `10`
buckets. The SageMaker Clarify processing job will generate PDPs for
`Income` split into `10` segments on the x-axis. The
y-axis will show the marginal impact of `Income` on the target
variable.

The following code example launches a SageMaker Clarify processing job to compute
PDPs.

```
clarify_processor.run_explainability(
    data_config=data_config,
    model_config=model_config,
    model_scores=probability_config,
    explainability_config=pdp_config,
)
```

For an example notebook with instructions on how to run a SageMaker Clarify processing job
in SageMaker Studio Classic to compute PDPs, see [Explainability with SageMaker Clarify - Partial Dependence Plots (PDP)](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-clarify/fairness_and_explainability/explainability_with_pdp.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-clarify/fairness_and_explainability/explainability_with_pdp.ipynb").

### How to compute

both SHAP values and PDPs for a CSV
dataset

You can compute both SHAP values and PDPs in a
single SageMaker Clarify processing job. In the following configuration example, the
`top_k_features` parameter of a new `PDPConfig` object
is set to `2`. This instructs the SageMaker Clarify processing job to compute
PDPs for the `2` features that have the largest
global SHAP values.

```
shap_pdp_config = clarify.PDPConfig(
    top_k_features=2,
    grid_resolution=10,
)
```

The following code example launches a SageMaker Clarify processing job to compute both
SHAP values and PDPs.

```
clarify_processor.run_explainability(
    data_config=data_config,
    model_config=model_config,
    model_scores=probability_config,
    explainability_config=[shap_config, shap_pdp_config],
)
```

The following examples show how to configure bias analysis and explainability
analysis for a tabular dataset in >SageMaker AI JSON Lines dense format. See [JSONLINES request format](cdf-inference.md#cm-jsonlines "cdf-inference.md#cm-jsonlines") for more information. In
these examples, the incoming dataset has the same data as the previous section, but
they're in the JSON Lines format. Each line is a valid JSON object. The key
`Features` points to an array of feature values, and the key
`Label` points to the ground truth label.

```
{"Features":[25,0,2850,2],"Label":0}
{"Features":[36,0,6585,0],"Label":1}
{"Features":[22,1,1759,1],"Label":1}
{"Features":[48,0,3446,1],"Label":0}
...
```

In the following configuration example, the `DataConfig` object
specifies the input dataset and where to store the output.

```
data_config = clarify.DataConfig(
    s3_data_input_path=jsonl_dataset_s3_uri,
    dataset_type='application/jsonlines',
    headers=['Age', 'Gender', 'Income', 'Occupation', 'Target'],
    label='Label',
    features='Features',
    s3_output_path=clarify_job_output_s3_uri,
)
```

In the previous configuration example, the features parameter is set to the [JMESPath](https://jmespath.org/ "https://jmespath.org/") expression `Features` so
that the SageMaker Clarify processing job can extract the array of features from each record.
The `label` parameter is set to JMESPath expression `Label` so
that the SageMaker Clarify processing job can extract the ground truth label from each record.
The `s3_data_input_path` parameter can either be a URI of a dataset file
or an Amazon S3 URI prefix. If you provide a S3 URI prefix, the SageMaker Clarify processing job
recursively collects all S3 files located under the prefix. The value for
`s3_output_path` should be an S3 URI prefix to hold the analysis
results. SageMaker AI uses the `s3_output_path` while compiling, and cannot take
a value of a SageMaker AI Pipeline parameter, property, expression, or
`ExecutionVariable`, which are used during runtime.

You must have a trained model to compute post-training bias metrics or feature
importance. The following example is from a binary classification model that outputs
JSON Lines data in the example's format. Each row of the model output is a valid
JSON object. The key `predicted_label` points to the predicted label, and
the key `probability` points to the probability value.

```
{"predicted_label":0,"probability":0.028986845165491}
{"predicted_label":1,"probability":0.825382471084594}
...
```

In the following configuration example, a `ModelConfig` object
instructs the SageMaker Clarify processing job to deploy the SageMaker AI model to an ephemeral
endpoint. The endpoint uses one `ml.m4.xlarge` inference instance.

```
model_config = clarify.ModelConfig(
    model_name=your_model,
    instance_type='ml.m4.xlarge',
    instance_count=1,
    content_template='{"Features":$features}',
)
```

In previous configuration example, the parameter `content_type` and
`accept_type` are not set. Therefore, they automatically use the
value of the `dataset_type` parameter of the `DataConfig`
object, which is `application/jsonlines`. The SageMaker Clarify processing job uses
the `content_template` parameter to compose the model input by replacing
the `$features` placeholder by an array of features.

The following example configuration shows how to set the label parameter of the
`ModelPredictedLabelConfig` object to the JMESPath expression
`predicted_label`. This will extract the predicted label from the
model output.

```
predicted_label_config = clarify.ModelPredictedLabelConfig(
    label='predicted_label',
)
```

The following example configuration shows how to set the `probability`
parameter of the `ModelPredictedLabelConfig` object to the JMESPath
expression `probability`. This will extract the score from the model
output.

```
probability_config = clarify.ModelPredictedLabelConfig(
    probability='probability',
)
```

To compute bias metrics and feature importance for datasets in JSON Lines format,
use the same run statements and configuration objects as the previous section for
CSV datasets. You can run a SageMaker Clarify processing job in SageMaker Studio Classic to detect bias
and compute feature importance. For instructions and an example notebook, see [Fairness and Explainability with SageMaker Clarify (JSON Lines Format)](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability_jsonlines_format.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability_jsonlines_format.ipynb").

SageMaker Clarify supports explanations for natural language processing (NLP) models. These
explanations help you understand which sections of text are the most important for
your model predictions. You can explain either the model prediction for a single
instance of the input dataset, or model predictions from the baseline dataset.To
understand and visualize a model’s behavior, you can specify multiple levels of
granularity. To do this, define the length of the text segment, such as its tokens,
sentences, paragraphs.

SageMaker Clarify NLP explainability is compatible with both classification and regression
models. You can also use SageMaker Clarify to explain your model's behavior on multi-modal
datasets that contain text, categorical, or numerical features. NLP explainability
for multi-modal datasets can help you understand how important each feature is to
the model's output. SageMaker Clarify supports 62 languages and can handle text which includes
multiple languages.

The following example shows an analysis configuration file for computing feature
importance for NLP. In this example, the incoming dataset is a tabular dataset in
CSV format, with one binary label column and two feature columns.

```
0,2,"Flavor needs work"
1,3,"They taste good"
1,5,"The best"
0,1,"Taste is awful"
...
```

The following configuration example shows how to specify an input dataset in CSV
format and output data path using the `DataConfig` object.

```
nlp_data_config = clarify.DataConfig(
    s3_data_input_path=nlp_dataset_s3_uri,
    dataset_type='text/csv',
    headers=['Target', 'Rating', 'Comments'],
    label='Target',
    s3_output_path=clarify_job_output_s3_uri,
)
```

In the previous configuration example, the `s3_data_input_path`
parameter can either be a URI of a dataset file or an Amazon S3 URI prefix. If you
provide a S3 URI prefix, the SageMaker Clarify processing job recursively collects all S3
files located under the prefix. The value for `s3_output_path` should be
an S3 URI prefix to hold the analysis results. SageMaker AI uses the
`s3_output_path` while compiling, and cannot take a value of a SageMaker AI
Pipeline parameter, property, expression, or `ExecutionVariable`, which
are used during runtime.

The following example output was created from a binary classification model
trained on the previous input dataset. The classification model accepts CSV data,
and it outputs a single score in between `0` and `1`.

```
0.491656005382537
0.569582343101501
...
```

The following example shows how to configure the `ModelConfig` object
to deploy a SageMaker AI model. In this example, an ephemeral endpoint deploys the model.
This endpoint uses one `ml.g4dn.xlarge` inference instance equipped with
a GPU, for accelerated inferencing.

```
nlp_model_config = clarify.ModelConfig(
    model_name=your_nlp_model_name,
    instance_type='ml.g4dn.xlarge',
    instance_count=1,
)
```

The following example shows how to configure the
`ModelPredictedLabelConfig` object to locate the probability (score)
in the first column with an index of `0`.

```
probability_config = clarify.ModelPredictedLabelConfig(
    probability=0,
)
```

The following example SHAP configuration shows how to run a
token-wise explainability analysis using a model and an input dataset in the English
language.

```
text_config = clarify.TextConfig(
    language='english',
    granularity='token',
)
nlp_shap_config = clarify.SHAPConfig(
    baseline=[[4, '[MASK]']],
    num_samples=100,
    text_config=text_config,
)
```

In the previous example, the `TextConfig` object activates the NLP
explainability analysis. The `granularity` parameter indicates that the
analysis should parse tokens. In English, each token is a word. For other languages,
see the [spaCy
documentation for tokenization](https://spacy.io/usage/linguistic-features#tokenization "https://spacy.io/usage/linguistic-features#tokenization"), which SageMaker Clarify uses for NLP processing. The
previous example also shows how to use an average `Rating` of
`4` to set an in-place SHAP baseline instance. A
special mask token `[MASK]` is used to replace a token (word) in
`Comments`.

In the previous example, if the instance is `2,"Flavor needs work"`,
set the baseline to an average `Rating` of `4` with the
following baseline.

```
4, '[MASK]'
```

In the previous example, the SageMaker Clarify explainer iterates through each token and
replaces it with the mask, as follows.

```
2,"[MASK] needs work"

4,"Flavor [MASK] work"

4,"Flavor needs [MASK]"
```

Then, the SageMaker Clarify explainer will send each line to your model for predictions. This
is so that the explainer learns the predictions with and without the masked words.
The SageMaker Clarify explainer then uses this information to compute the contribution of each
token.

The following code example launches a SageMaker Clarify processing job to compute
SHAP values.

```
clarify_processor.run_explainability(
    data_config=nlp_data_config,
    model_config=nlp_model_config,
    model_scores=probability_config,
    explainability_config=nlp_shap_config,
)
```

For an example notebook with instructions on how to run a SageMaker Clarify processing job in
SageMaker Studio Classic for NLP explainability analysis, see [Explaining Text Sentiment Analysis Using SageMaker Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/text_explainability/text_explainability.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/text_explainability/text_explainability.ipynb").

SageMaker Clarify generates heat maps that provide insights into how your computer vision
models classify and detect objects in your images.

In the following configuration example, the input dataset consists of JPEG
images.

```
cv_data_config = clarify.DataConfig(
    s3_data_input_path=cv_dataset_s3_uri,
    dataset_type="application/x-image",
    s3_output_path=clarify_job_output_s3_uri,
)
```

In the previous configuration example, the `DataConfig` object
contains an `s3_data_input_path` set to an Amazon S3 URI prefix. The SageMaker Clarify
processing job recursively collects all image files located under the prefix. The
`s3_data_input_path` parameter can either be a URI of a dataset file
or an Amazon S3 URI prefix. If you provide a S3 URI prefix, the SageMaker Clarify processing job
recursively collects all S3 files located under the prefix. The value for
`s3_output_path` should be an S3 URI prefix to hold the analysis
results. SageMaker AI uses the `s3_output_path` while compiling, and cannot take
a value of a SageMaker AI Pipeline parameter, property, expression, or
`ExecutionVariable`, which are used during runtime.

### How

to explain an image classification model

The SageMaker Clarify processing job explains images using the KernelSHAP algorithm, which
treats the image as a collection of super pixels. Given a dataset consisting of
images, the processing job outputs a dataset of images where each image shows
the heat map of the relevant super pixels.

The following configuration example shows how to configure an explainability
analysis using a SageMaker image classification model. See [Image Classification - MXNet](image-classification.md "image-classification.md") for more
information.

```
ic_model_config = clarify.ModelConfig(
    model_name=your_cv_ic_model,
    instance_type="ml.p2.xlarge",
    instance_count=1,
    content_type="image/jpeg",
    accept_type="application/json",
)
```

In the previous configuration example, a model named
`your_cv_ic_model`, has been trained to classify the animals on
input JPEG images. The `ModelConfig` object in the previous example
instructs the SageMaker Clarify processing job to deploy the SageMaker AI model to an ephemeral
endpoint. For accelerated inferencing, the endpoint uses one
`ml.p2.xlarge` inference instance equipped with a GPU.

After a JPEG image is sent to an endpoint, the endpoint classifies it and
returns a list of scores. Each score is for a category. The
`ModelPredictedLabelConfig` object provides the name of each
category, as follows.

```
ic_prediction_config = clarify.ModelPredictedLabelConfig(
    label_headers=['bird', 'cat', 'dog'],
)
```

An example output for the previous input of ['bird','cat','dog'] could be
0.3,0.6,0.1, where 0.3 represents the confidence score for classifying an image
as a bird.

The following example SHAP configuration shows how to generate
explanations for an image classification problem. It uses an
`ImageConfig` object to activate the analysis.

```
ic_image_config = clarify.ImageConfig(
    model_type="IMAGE_CLASSIFICATION",
    num_segments=20,
    segment_compactness=5,
)

ic_shap_config = clarify.SHAPConfig(
    num_samples=100,
    image_config=ic_image_config,
)
```

SageMaker Clarify extracts features using the [Simple Linear Iterative Clustering (SLIC)](https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.slic "https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.slic") method from scikit-learn
library for image segmentation. The previous configuration example, the
`model_type` parameter, indicates the type of image
classification problem. The parameter `num_segments` estimates how
many approximate number of segments will be labeled in the input image. The
number of segments is then passed to the slic `n_segments` parameter.

Each segment of the image is considered a super-pixel, and local
SHAP values are computed for each segment. The parameter
`segment_compactness` determines the shape and size of the image
segments that are generated by the scikit-image slic method. The sizes and
shapes of the image segments are then passed to the slic
`compactness` parameter.

The following code example launches a SageMaker Clarify processing job to generate heat
maps for your images. Positive heat map values show that the feature increased
the confidence score of detecting the object. Negative values indicate that the
feature decreased the confidence score.

```
clarify_processor.run_explainability(
    data_config=cv_data_config,
    model_config=ic_model_config,
    model_scores=ic_prediction_config,
    explainability_config=ic_shap_config,
)
```

For a sample notebook that uses SageMaker Clarify to classify images and explain its
classification, see [Explaining Image Classification with SageMaker Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/computer_vision/image_classification/explainability_image_classification.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/computer_vision/image_classification/explainability_image_classification.ipynb").

### How to

explain an object detection model

A SageMaker Clarify processing job can detect and classify objects in an image and then
provide an explanation for the detected object. The process for explanation is
as follows.

1. Image objects are first categorized into one of the classes in a
   specified collection. For example, if an object detection model can
   recognize cat, dog and fish, then these three classes are in a
   collection. This collection is specified by the
   `label_headers` parameter as follows.

```
clarify.ModelPredictedLabelConfig(

label_headers=object_categories,

)
```

2. The SageMaker Clarify processing job produces a confidence score for each object.
   A high confidence score indicates that it belongs to one of the classes
   in a specified collection. The SageMaker Clarify processing job also produces the
   coordinates of a bounding box that delimits the object. For more
   information about confidence scores and bounding boxes, see [Response Formats](object-detection-in-formats.md#object-detection-recordio "object-detection-in-formats.md#object-detection-recordio").
3. SageMaker Clarify then provides an explanation for the detection of an object in
   the image scene. It uses the methods described in the **How to explain an image classification model**
   section.

In the following configuration example, a SageMaker AI object detection model
`your_cv_od_model` is trained on JPEG images to identify the
animals on them.

```
od_model_config = clarify.ModelConfig(
    model_name=your_cv_ic_model,
    instance_type="ml.p2.xlarge",
    instance_count=1,
    content_type="image/jpeg",
    accept_type="application/json",
)
```

The `ModelConfig` object in the previous configuration example
instructs the SageMaker Clarify processing job to deploy the SageMaker AI model to an ephemeral
endpoint. For accelerated imaging, this endpoint uses one
`ml.p2.xlarge` inference instance equipped with a GPU.

In the following example configuration, the
`ModelPredictedLabelConfig` object provides the name of each
category for classification.

```
ic_prediction_config = clarify.ModelPredictedLabelConfig(
    label_headers=['bird', 'cat', 'dog'],
)
```

The following example SHAP configuration shows how to generate
explanations for an object detection.

```
od_image_config = clarify.ImageConfig(
    model_type="OBJECT_DETECTION",
    num_segments=20,
    segment_compactness=5,
    max_objects=5,
    iou_threshold=0.5,
    context=1.0,
)
od_shap_config = clarify.SHAPConfig(
    num_samples=100,
    image_config=image_config,
)
```

In the previous example configuration, the `ImageConfig` object
activates the analysis. The `model_type` parameter indicates that the
type of problem is object detection. For a detailed description of the other
parameters, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

The following code example launches a SageMaker Clarify processing job to generate heat
maps for your images. Positive heat map values show that the feature increased
the confidence score of detecting the object. Negative values indicate that the
feature decreased the confidence score.

```
clarify_processor.run_explainability(
    data_config=cv_data_config,
    model_config=od_model_config,
    model_scores=od_prediction_config,
    explainability_config=od_shap_config,
)
```

For a sample notebook that uses SageMaker Clarify to detect objects in an image and
explain its predictions, see [Explaining object detection models with Amazon SageMaker AI Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/computer_vision/object_detection/object_detection_clarify.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-clarify/computer_vision/object_detection/object_detection_clarify.ipynb").

The following examples show how to configure data in SageMaker AI JSON dense format
to explain a time series forecasting model. For more information about JSON formatting,
see [JSON request format](cdf-inference.md#cm-json "cdf-inference.md#cm-json").

```
[
    {
        "item_id": "item1",
        "timestamp": "2019-09-11",
        "target_value": 47650.3,
        "dynamic_feature_1": 0.4576,
        "dynamic_feature_2": 0.2164,
        "dynamic_feature_3": 0.1906,
        "static_feature_1": 3,
        "static_feature_2": 4
    },
    {
        "item_id": "item1",
        "timestamp": "2019-09-12",
        "target_value": 47380.3,
        "dynamic_feature_1": 0.4839,
        "dynamic_feature_2": 0.2274,
        "dynamic_feature_3": 0.1889,
        "static_feature_1": 3,
        "static_feature_2": 4
    },
    {
        "item_id": "item2",
        "timestamp": "2020-04-23",
        "target_value": 35601.4,
        "dynamic_feature_1": 0.5264,
        "dynamic_feature_2": 0.3838,
        "dynamic_feature_3": 0.4604,
        "static_feature_1": 1,
        "static_feature_2": 2
    },
]
```

### Data config

Use `TimeSeriesDataConfig` communicate to your explainability job
how to parse data correctly from the passed input dataset, as shown in the
following example configuration:

```
time_series_data_config = clarify.TimeSeriesDataConfig(
    target_time_series='[].target_value',
    item_id='[].item_id',
    timestamp='[].timestamp',
    related_time_series=['[].dynamic_feature_1', '[].dynamic_feature_2', '[].dynamic_feature_3'],
    static_covariates=['[].static_feature_1', '[].static_feature_2'],
    dataset_format='timestamp_records',
)
```

### Asymmetric Shapley value config

Use `AsymmetricShapleyValueConfig` to define arguments for time series
forecasting model explanation analysis such as baseline, direction, granularity,
and number of samples. Baseline values are set for all three types
of data: related time series, static covariates, and target time series. The
`AsymmetricShapleyValueConfig` config informs
the SageMaker Clarify processor how to compute feature attributions for one item at a time.
The following configuration shows an example definition of `AsymmetricShapleyValueConfig`.

```
asymmetric_shapley_value_config = AsymmetricShapleyValueConfig(
    direction="chronological",
    granularity="fine-grained",
    num_samples=10,
    baseline={
        "related_time_series": "zero",
        "static_covariates": {
            "item1": [0, 0], "item2": [0, 0]
        },
        "target_time_series": "zero"
    },
)
```

The values you provide to `AsymmetricShapleyValueConfig` are passed to the analysis config as an
entry in `methods` with key `asymmetric_shapley_value`.

### Model config

You can control the structure of the payload sent from the SageMaker Clarify processor.
In the following code sample, a `ModelConfig` configuration object
directs a time series forecasting explainability job to aggregate records using
JMESPath syntax into `'{"instances": $records}'` , where the structure
of each record is defined with the following record_template `'{"start": 
 $start_time, "target": $target_time_series, "dynamic_feat": $related_time_series, 
 "cat": $static_covariates}'`. Note that `$start_time`,
`$target_time_series`, `$related_time_series`, and
`$static_covariates` are internal tokens used to map dataset values
to endpoint request values.

```
model_config = clarify.ModelConfig(
    model_name=`your_model`,
    instance_type='ml.m4.xlarge',
    instance_count=1,
    record_template='{"start": $start_time, "target": $target_time_series, "dynamic_feat": $related_time_series, "cat": $static_covariates}',
    content_template='{"instances": $records}',,
    time_series_model_config=TimeSeriesModelConfig(
        forecast={'forecast': 'predictions[*].mean[:2]'}
    )
)
```

Similarly, the attribute `forecast` in `TimeSeriesModelConfig`,
passed to the analysis config with key `time_series_predictor_config`, is used
to extract the model forecast from the endpoint response. For instance, an example
endpoint batch response could be the following:

```
{
    "predictions": [
        {"mean": [13.4, 3.6, 1.0]},
        {"mean": [23.0, 4.7, 3.0]},
        {"mean": [3.4, 5.6, 2.0]}
    ]
}
```

If the JMESPath expression provided for `forecast` is {'predictions[\*].mean[:2]'}}, the
forecast value is parsed as follows:

```
[[13.4, 3.6], [23.0, 4.7], [3.4, 5.6]]
```

## How to run parallel SageMaker Clarify processing

jobs

When working with large datasets, you can use [Apache Spark](https://spark.apache.org/ "https://spark.apache.org/") to increase the speed of your SageMaker Clarify processing jobs. Spark is
a unified analytics engine for large-scale data processing. When you request more than
one instance per SageMaker Clarify processor, SageMaker Clarify uses the distributed computing capabilities from
Spark.

The following configuration example shows how to use
`SageMakerClarifyProcessor` to create a SageMaker Clarify processor with
`5` compute instances. To run any jobs associated with the
`SageMakerClarifyProcessor`, SageMaker Clarify using Spark distributed
processing.

```
from sagemaker import clarify

spark_clarify_processor = clarify.SageMakerClarifyProcessor(
    role=role,
    instance_count=5,
    instance_type='ml.c5.xlarge',
)
```

If you set the `save_local_shap_values` parameter of [SHAPConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SHAPConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.SHAPConfig") to `True`, the SageMaker Clarify processing job saves the local
SHAP value as multiple part files in the job output location.

To associate the local SHAP values to the input dataset instances, use
the `joinsource` parameter of `DataConfig`. If you add more
compute instances, we recommend that you also increase the `instance_count`
of [ModelConfig](https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.ModelConfig "https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.clarify.ModelConfig") for the ephemeral endpoint. This prevents Spark workers'
concurrent inference requests from overwhelming the endpoint. Specifically, we recommend
that you use a one-to-one ratio of endpoint-to-processing instances.
