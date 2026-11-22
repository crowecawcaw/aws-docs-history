

# Add a step

The following describes the requirements of each step type and provides an example implementation of the step, as well as how to add the step to a Pipelines. These are not working implementations because they don't provide the resource and inputs needed. For a tutorial that implements these steps, see [Pipelines actions](pipelines-build.md).

**Note**  
You can also create a step from your local machine learning code by converting it to a Pipelines step with the `@step` decorator. For more information, see [@step decorator](#step-type-custom).

Amazon SageMaker Pipelines support the following step types:
+ [Execute code](#step-type-executecode)

  [Processing](#step-type-processing)
+ [Training](#step-type-training)
+ [Tuning](#step-type-tuning)
+ [AutoML](#step-type-automl)
+ [`Model`](#step-type-model)
+ [`Create model`](#step-type-create-model)
+ [`Register model`](#step-type-register-model)
+ [`Deploy model (endpoint)`](#step-type-deploy-model-endpoint)
+ [EndpointConfig](#step-type-endpoint-config)
+ [Endpoint](#step-type-endpoint)
+ [InferenceComponent](#step-type-inference-component)
+ [Lineage](#step-type-lineage)
+ [Job](#step-type-job)
+ [HubContent](#step-type-hub-content)
+ [Transform](#step-type-transform)
+ [Condition](#step-type-condition)
+ [`Callback`](#step-type-callback)
+ [Lambda](#step-type-lambda)
+ [`ClarifyCheck`](#step-type-clarify-check)
+ [`QualityCheck`](#step-type-quality-check)
+ [EMR](#step-type-emr)
+ [Athena](#step-type-athena)
+ [ForEach](#step-type-foreach)
+ [Cleanup](#step-type-cleanup)
+ [Notebook Job](#step-type-notebook-job)
+ [Fail](#step-type-fail)

## @step decorator
<a name="step-type-custom"></a>

If you want to orchestrate a custom ML job that leverages advanced SageMaker AI features or other AWS services in the drag-and-drop Pipelines UI, use the [Execute code step](#step-type-executecode).

You can create a step from local machine learning code using the `@step` decorator. After you test your code, you can convert the function to a SageMaker AI pipeline step by annotating it with the `@step` decorator. Pipelines creates and runs a pipeline when you pass the output of the `@step`-decorated function as a step to your pipeline. You can also create a multi-step DAG pipeline that includes one or more `@step`-decorated functions as well as traditional SageMaker AI pipeline steps. For more details about how to create a step with `@step` decorator, see [Lift-and-shift Python code with the @step decorator](pipelines-step-decorator.md).

## Execute code step
<a name="step-type-executecode"></a>

In the Pipelines drag-and-drop UI, you can use an **Execute code** step to run your own code as a pipeline step. You can upload a Python function, script, or notebook to be executed as part of your pipeline. You should use this step if you want to orchestrate a custom ML job that leverages advanced SageMaker AI features or other AWS services.

The **Execute Code** step uploads files to your default Amazon S3 bucket for Amazon SageMaker AI. This bucket might not have the required Cross-Origin Resource Sharing (CORS) permissions set. To learn more about configuring CORS permissions, see [CORS Requirement for Input Image Data](sms-cors-update.md).

The **Execute Code** step uses an Amazon SageMaker training job to run your code. Ensure that your IAM role has the `sagemaker:DescribeTrainingJob` and `sagemaker:CreateTrainingJob` API permissions. To learn more about all the required permissions for Amazon SageMaker AI and how to set them up, see [Amazon SageMaker AI API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md).

To add an execute code step to a pipeline using the Pipeline Designer, do the following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Execute code** and drag it to the canvas.

1. In the canvas, choose the **Execute code** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs.

1. You can upload a single file to execute or upload a compressed folder containing multiple artifacts.

1. For single file uploads, you can provide optional parameters for notebooks, python functions, or scripts.

1. When providing Python functions, a handler must be provided in the format `file.py:{{<function_name>}}`

1. For compressed folder uploads, relative paths to your code must be provided, and you can optionally provide paths to a `requirements.txt` file or initialization script inside the compressed folder.

1. If the canvas includes any step that immediately precedes the **Execute code** step you added, click and drag the cursor from the step to the **Execute code** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Execute code** step you added, click and drag the cursor from the **Execute code** step to the step to create an edge. Outputs from **Execute code** steps can be referenced for Python functions.

## Processing step
<a name="step-type-processing"></a>

Use a processing step to create a processing job for data processing. For more information on processing jobs, see [Process Data and Evaluate Models](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html).

------
#### [ Pipeline Designer ]

To add a processing step to a pipeline using the Pipeline Designer, do the following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. In the left sidebar, choose **Process data** and drag it to the canvas.

1. In the canvas, choose the **Process data** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.steps.ProcessingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep).

1. If the canvas includes any step that immediately precedes the **Process data** step you added, click and drag the cursor from the step to the **Process data** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Process data** step you added, click and drag the cursor from the **Process data** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

A processing step requires a processor, a Python script that defines the processing code, outputs for processing, and job arguments. The following example shows how to create a `ProcessingStep` definition. 

```python
from sagemaker.core.processing import Processor, ProcessingInput, ProcessingOutput

processor = Processor(
    image_uri='{{sklearn-processing-image-uri}}',
    role={{<role>}},
    instance_type='ml.m5.xlarge',
    instance_count=1
)
```

```python
from sagemaker.mlops.workflow.steps import ProcessingStep

inputs = [
    ProcessingInput(source={{<input_data>}}, destination="/opt/ml/processing/input"),
]

outputs = [
    ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
    ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
    ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
]

step_process = ProcessingStep(
    name="AbaloneProcess",
    step_args = processor.run(inputs=inputs, outputs=outputs,
        code="abalone/preprocessing.py")
)
```

**Pass runtime parameters**

The following example shows how to pass runtime parameters from a PySpark processor to a `ProcessingStep`.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.core.processing import Processor, ProcessingInput, ProcessingOutput
from sagemaker.mlops.workflow.steps import ProcessingStep

pipeline_session = PipelineSession()

pyspark_processor = Processor(
    image_uri='{{pyspark-processing-image-uri}}',
    role={{<role>}},
    instance_type='ml.m5.xlarge',
    instance_count=1,
    sagemaker_session=pipeline_session,
)

step_args = pyspark_processor.run(
    inputs=[ProcessingInput(source={{<input_data>}}, destination="/opt/ml/processing/input"),],
    outputs=[
        ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
        ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
        ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
    ],
    code="preprocess.py",
    arguments=None,
)


step_process = ProcessingStep(
    name="AbaloneProcess",
    step_args=step_args,
)
```

For more information on processing step requirements, see the [sagemaker.workflow.steps.ProcessingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep) documentation. For an in-depth example, see the [Orchestrate Jobs to Train and Evaluate Models with Amazon SageMaker Pipelines](https://github.com/aws/amazon-sagemaker-examples/blob/62de6a1fca74c7e70089d77e36f1356033adbe5f/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb) example notebook. The *Define a Processing Step for Feature Engineering* section includes more information.

------

## Training step
<a name="step-type-training"></a>

You use a training step to create a training job to train a model. For more information on training jobs, see [Train a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html).

A training step requires a ModelTrainer, as well as training and validation data inputs.

------
#### [ Pipeline Designer ]

To add a training step to a pipeline using the Pipeline Designer, do the following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Train model** and drag it to the canvas.

1. In the canvas, choose the **Train model** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.steps.TrainingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep).

1. If the canvas includes any step that immediately precedes the **Train model** step you added, click and drag the cursor from the step to the **Train model** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Train model** step you added, click and drag the cursor from the **Train model** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

The following example shows how to create a `TrainingStep` definition. For more information about training step requirements, see the [sagemaker.workflow.steps.TrainingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep) documentation.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData, Compute
from sagemaker.mlops.workflow.steps import TrainingStep
from sagemaker.core import image_uris

pipeline_session = PipelineSession()

training_image = image_uris.retrieve("xgboost", region, "1.7-1")

model_trainer = ModelTrainer(
    training_image=training_image,
    role=role,
    compute=Compute(instance_type="ml.m5.xlarge", instance_count=1),
    hyperparameters={...}
)

step_args = model_trainer.train(
    input_data_config=[
        InputData(
            channel_name="train",
            data_source=step_process.properties.ProcessingOutputConfig.Outputs[
                "train"
            ].S3Output.S3Uri,
        ),
        InputData(
            channel_name="validation",
            data_source=step_process.properties.ProcessingOutputConfig.Outputs[
                "validation"
            ].S3Output.S3Uri,
        )
    ]
)

step_train = TrainingStep(
    name="TrainAbaloneModel",
    step_args=step_args,
)
```

------

## Tuning step
<a name="step-type-tuning"></a>

You use a tuning step to create a hyperparameter tuning job, also known as hyperparameter optimization (HPO). A hyperparameter tuning job runs multiple training jobs, with each job producing a model version. For more information on hyperparameter tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md).

The tuning job is associated with the SageMaker AI experiment for the pipeline, with the training jobs created as trials. For more information, see [Experiments Integration](pipelines-experiments.md).

A tuning step requires a [HyperparameterTuner](https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html) and training inputs. You can retrain previous tuning jobs by specifying the `warm_start_config` parameter of the `HyperparameterTuner`. For more information on hyperparameter tuning and warm start, see [Run a Warm Start Hyperparameter Tuning Job](automatic-model-tuning-warm-start.md).

You use the [get\_top\_model\_s3\_uri](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep.get_top_model_s3_uri) method of the [sagemaker.workflow.steps.TuningStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep) class to get the model artifact from one of the top-performing model versions. For a notebook that shows how to use a tuning step in a SageMaker AI pipeline, see [sagemaker-pipelines-tuning-step.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/tuning-step/sagemaker-pipelines-tuning-step.ipynb).

**Important**  
Tuning steps were introduced in Amazon SageMaker Python SDK v2.48.0 and Amazon SageMaker Studio Classic v3.8.0. You must update Studio Classic before you use a tuning step or the pipeline DAG doesn't display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

The following example shows how to create a `TuningStep` definition.

```python
from sagemaker.workflow.pipeline_context import PipelineSession

from sagemaker.tuner import HyperparameterTuner
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TuningStep

tuner = HyperparameterTuner(..., sagemaker_session=PipelineSession())
    
step_tuning = TuningStep(
    name = "HPTuning",
    step_args = tuner.fit(inputs=TrainingInput(s3_data="s3://{{amzn-s3-demo-bucket/my-data}}"))
)
```

**Get the best model version**

The following example shows how to get the best model version from the tuning job using the `get_top_model_s3_uri` method. At most, the top 50 performing versions are available ranked according to [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html). The `top_k` argument is an index into the versions, where `top_k=0` is the best-performing version and `top_k=49` is the worst-performing version.

```python
best_model = Model(
    image_uri=image_uri,
    model_data=step_tuning.get_top_model_s3_uri(
        top_k=0,
        s3_bucket=sagemaker_session.default_bucket()
    ),
    ...
)
```

For more information on tuning step requirements, see the [sagemaker.workflow.steps.TuningStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep) documentation.

## Fine-tuning step
<a name="step-type-fine-tuning"></a>

Fine-tuning trains a pretrained foundation model from Amazon SageMaker JumpStart on a new dataset. This process, also known as transfer learning, can produce accurate models with smaller datasets and less training time. When you fine-tune a model, you can use the default dataset or choose your own data. To learn more about fine-tuning a foundation model from JumpStart, see [Fine-Tune a Model](jumpstart-fine-tune.md).

The fine-tuning step uses an Amazon SageMaker training job to customize your model. Ensure that your IAM role has the `sagemaker:DescribeTrainingJob` and `sagemaker:CreateTrainingJob` API permissions to execute the fine-tuning job in your pipeline. To learn more about the required permissions for Amazon SageMaker AI and how to set them up, see [Amazon SageMaker AI API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md).

To add a **Fine-tune model** step to your pipeline using the drag-and-drop editor, follow these steps:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Fine-tune model** and drag it to the canvas.

1. In the canvas, choose the **Fine-tune model** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs.

1. If the canvas includes any step that immediately precedes the **Fine-tune model** step you added, click and drag the cursor from the step to the **Fine-tune model** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Fine-tune model** step you added, click and drag the cursor from the **Fine-tune model** step to the step to create an edge.

## AutoML step
<a name="step-type-automl"></a>

Use the [AutoML](https://sagemaker.readthedocs.io/en/stable/api/training/automl.html) API to create an AutoML job to automatically train a model. For more information on AutoML jobs, see [Automate model development with Amazon SageMaker Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html). 

**Note**  
Currently, the AutoML step supports only [ensembling training mode](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html).

The following example shows how to create a definition using `AutoMLStep`.

```python
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.automl_step import AutoMLStep

pipeline_session = PipelineSession()

auto_ml = AutoML(...,
    role="{{<role>}}",
    target_attribute_name="{{my_target_attribute_name}}",
    mode="{{ENSEMBLING}}",
    sagemaker_session=pipeline_session) 

input_training = AutoMLInput(
    inputs="s3://{{amzn-s3-demo-bucket/my-training-data}}",
    target_attribute_name="{{my_target_attribute_name}}",
    channel_type="training",
)
input_validation = AutoMLInput(
    inputs="s3://{{amzn-s3-demo-bucket/my-validation-data}}",
    target_attribute_name="{{my_target_attribute_name}}",
    channel_type="validation",
)

step_args = auto_ml.fit(
    inputs=[input_training, input_validation]
)

step_automl = AutoMLStep(
    name="AutoMLStep",
    step_args=step_args,
)
```

**Get the best model version**

The AutoML step automatically trains several model candidates. Get the model with the best objective metric from the AutoML job using the `get_best_auto_ml_model` method as follows. You must also use an IAM `role` to access model artifacts.

```
best_model = step_automl.get_best_auto_ml_model({{role=<role>}})
```

For more information, see the [AutoML](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.automl_step.AutoMLStep) step in the SageMaker Python SDK.

## Model step
<a name="step-type-model"></a>

Use a `ModelStep` to create or register a SageMaker AI model. For more information on `ModelStep` requirements, see the [sagemaker.workflow.model\_step.ModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.model_step.ModelStep) documentation.

### Create a model
<a name="step-type-model-create"></a>

You can use a `ModelStep` to create a SageMaker AI model. A `ModelStep` requires model artifacts and information about the SageMaker AI instance type that you need to use to create the model. For more information about SageMaker AI models, see [Train a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html).

The following example shows how to create a `ModelStep` definition.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.core.resources import Model
from sagemaker.mlops.workflow.model_step import ModelStep

step_train = TrainingStep(...)
model = Model(
    image_uri=pytorch_estimator.training_image_uri(),
    model_data=step_train.properties.ModelArtifacts.S3ModelArtifacts,
    sagemaker_session=PipelineSession(),
    role=role,
)

step_model_create = ModelStep(
   name="MyModelCreationStep",
   step_args=model.create(instance_type="ml.m5.xlarge"),
)
```

### Register a model
<a name="step-type-model-register"></a>

You can use a `ModelStep` to register a `sagemaker.model.Model` or a `sagemaker.pipeline.PipelineModel` with the Amazon SageMaker Model Registry. A `PipelineModel` represents an inference pipeline, which is a model composed of a linear sequence of containers that process inference requests. For more information about how to register a model, see [Model Registration Deployment with Model Registry](model-registry.md).

The following example shows how to create a `ModelStep` that registers a `PipelineModel`.

```python
import time

from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.core.resources import Model
from sagemaker.core import image_uris

pipeline_session = PipelineSession()

code_location = 's3://{0}/{1}/code'.format({{bucket_name}}, prefix)

sklearn_model = SKLearnModel(
   model_data=processing_step.properties.ProcessingOutputConfig.Outputs['model'].S3Output.S3Uri,
   entry_point='inference.py',
   source_dir='sklearn_source_dir/',
   code_location=code_location,
   framework_version='1.0-1',
   role=role,
   sagemaker_session=pipeline_session,
   py_version='py3'
)

xgboost_model = XGBoostModel(
   model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
   entry_point='inference.py',
   source_dir='xgboost_source_dir/',
   code_location=code_location,
   framework_version='0.90-2',
   py_version='py3',
   sagemaker_session=pipeline_session,
   role=role
)

from sagemaker.mlops.workflow.model_step import ModelStep
from sagemaker.core.pipeline_model import PipelineModel

pipeline_model = PipelineModel(
   models=[sklearn_model, xgboost_model],
   role=role,sagemaker_session=pipeline_session,
)

register_model_step_args = pipeline_model.register(
    content_types=["application/json"],
   response_types=["application/json"],
   inference_instances=["ml.t2.medium", "ml.m5.xlarge"],
   transform_instances=["ml.m5.xlarge"],
   model_package_group_name='sipgroup',
)

step_model_registration = ModelStep(
   name="AbaloneRegisterModel",
   step_args=register_model_step_args,
)
```

## Create model step
<a name="step-type-create-model"></a>

You use a Create model step to create a SageMaker AI model. For more information on SageMaker AI models, see [Train a Model with Amazon SageMaker](how-it-works-training.md).

A create model step requires model artifacts and information about the SageMaker AI instance type that you need to use to create the model. The following examples show how to create a Create model step definition. For more information about Create model step requirements, see the [sagemaker.workflow.steps.CreateModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep) documentation.

------
#### [ Pipeline Designer ]

To add a create model step to your pipeline, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Create model** and drag it to the canvas.

1. In the canvas, choose the **Create model** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.steps.CreateModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep).

1. If the canvas includes any step that immediately precedes the **Create model** step you added, click and drag the cursor from the step to the **Create model** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Create model** step you added, click and drag the cursor from the **Create model** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

**Important**  
We recommend using [Model step](#step-type-model) to create models as of v2.90.0 of the SageMaker AI Python SDK. `CreateModelStep` will continue to work in previous versions of the SageMaker Python SDK, but is no longer actively supported.

```python
from sagemaker.workflow.steps import CreateModelStep

step_create_model = CreateModelStep(
    name="AbaloneCreateModel",
    model=best_model,
    inputs=inputs
)
```

------

## Register model step
<a name="step-type-register-model"></a>

The Register model step registers a model into the SageMaker Model Registry.

------
#### [ Pipeline Designer ]

To register a model from a pipeline using the Pipeline Designer, do the following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Register model** and drag it to the canvas.

1. In the canvas, choose the **Register model** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.step\_collections.RegisterModel](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel).

1. If the canvas includes any step that immediately precedes the **Register model** step you added, click and drag the cursor from the step to the **Register model** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Register model** step you added, click and drag the cursor from the **Register model** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

**Important**  
We recommend using [Model step](#step-type-model) to register models as of v2.90.0 of the SageMaker AI Python SDK. `RegisterModel` will continue to work in previous versions of the SageMaker Python SDK, but is no longer actively supported.

You use a `RegisterModel` step to register a [sagemaker.model.Model](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html) or a [sagemaker.pipeline.PipelineModel](https://sagemaker.readthedocs.io/en/stable/api/inference/pipeline.html#pipelinemodel) with the Amazon SageMaker Model Registry. A `PipelineModel` represents an inference pipeline, which is a model composed of a linear sequence of containers that process inference requests.

For more information about how to register a model, see [Model Registration Deployment with Model Registry](model-registry.md). For more information on `RegisterModel` step requirements, see the [sagemaker.workflow.step\_collections.RegisterModel](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel) documentation.

The following example shows how to create a `RegisterModel` step that registers a `PipelineModel`.

```python
import time
from sagemaker.sklearn import SKLearnModel
from sagemaker.xgboost import XGBoostModel

code_location = 's3://{0}/{1}/code'.format({{bucket_name}}, prefix)

sklearn_model = SKLearnModel(model_data=processing_step.properties.ProcessingOutputConfig.Outputs['model'].S3Output.S3Uri,
 entry_point='inference.py',
 source_dir='{{sklearn_source_dir/}}',
 code_location=code_location,
 framework_version='1.0-1',
 role=role,
 sagemaker_session=sagemaker_session,
 py_version='py3')

xgboost_model = XGBoostModel(model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
 entry_point='inference.py',
 source_dir='{{xgboost_source_dir/}}',
 code_location=code_location,
 framework_version='0.90-2',
 py_version='py3',
 sagemaker_session=sagemaker_session,
 role=role)

from sagemaker.workflow.step_collections import RegisterModel
from sagemaker import PipelineModel
pipeline_model = PipelineModel(models=[sklearn_model,xgboost_model],role=role,sagemaker_session=sagemaker_session)

step_register = RegisterModel(
 name="{{AbaloneRegisterModel}}",
 model=pipeline_model,
 content_types=["application/json"],
 response_types=["application/json"],
 inference_instances=["{{ml.t2.medium}}", "{{ml.m5.xlarge}}"],
 transform_instances=["{{ml.m5.xlarge}}"],
 model_package_group_name='{{sipgroup}}',
)
```

If `model` isn't provided, the register model step requires an estimator as shown in the following example.

```python
from sagemaker.workflow.step_collections import RegisterModel

step_register = RegisterModel(
    name="{{AbaloneRegisterModel}}",
    estimator=xgb_train,
    model_data=step_train.properties.ModelArtifacts.S3ModelArtifacts,
    content_types=["text/csv"],
    response_types=["text/csv"],
    inference_instances=["{{ml.t2.medium", "ml.m5.xlarge}}"],
    transform_instances=["{{ml.m5.xlarge}}"],
    model_package_group_name=model_package_group_name,
    approval_status=model_approval_status,
    model_metrics=model_metrics
)
```

------

## Deploy model (endpoint) step
<a name="step-type-deploy-model-endpoint"></a>

In the Pipeline Designer, use the Deploy model (endpoint) step to deploy your model to an endpoint. You can create a new endpoint or use an existing endpoint. Real-time inference is ideal for inference workloads where you have real-time, interactive, low latency requirements. You can deploy your model to SageMaker AI Hosting services and get a real-time endpoint that can be used for inference. These endpoints are fully managed and support auto-scaling. To learn more about real-time inference in SageMaker AI, see [Real-time inference](realtime-endpoints.md).

Before adding a deploy model step to your pipeline, make sure that your IAM role has the following permissions:
+ `sagemaker:CreateModel`
+ `sagemaker:CreateEndpointConfig`
+ `sagemaker:CreateEndpoint`
+ `sagemaker:UpdateEndpoint`
+ `sagemaker:DescribeModel`
+ `sagemaker:DescribeEndpointConfig`
+ `sagemaker:DescribeEndpoint`

To learn more about all the required permissions for SageMaker AI and how to set them up, see [Amazon SageMaker AI API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md).

To add a model deployment step to your Pipeline in the drag-and-drop editor, complete the following steps:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Deploy model (endpoint)** and drag it to the canvas.

1. In the canvas, choose the **Deploy model (endpoint)** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs.

1. If the canvas includes any step that immediately precedes the **Deploy model (endpoint)** step you added, click and drag the cursor from the step to the **Deploy model (endpoint)** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Deploy model (endpoint)** step you added, click and drag the cursor from the **Deploy model (endpoint)** step to the step to create an edge.

## EndpointConfig step
<a name="step-type-endpoint-config"></a>

Use an EndpointConfig step to create a SageMaker AI endpoint configuration as part of a pipeline. The step calls the `CreateEndpointConfig` operation. An endpoint configuration defines the models to host and the instances to host them on. To create the endpoint itself, follow it with an Endpoint step. For more information, see [Endpoint step](#step-type-endpoint).

To create an EndpointConfig step, use `EndpointConfigStep`, available in the SageMaker Python SDK v3.23.0 or later. Call `create_endpoint_config()` on a `PipelineSession` and pass the result as `step_args`. Under a `PipelineSession`, the call returns the step arguments instead of creating the configuration. The following example creates an endpoint configuration for one model.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.mlops.workflow import EndpointConfigStep

pipeline_session = PipelineSession()

step_endpoint_config = EndpointConfigStep(
    name="CreateEndpointConfig",
    step_args=pipeline_session.create_endpoint_config(
        name="my-endpoint-config",
        production_variants=[
            {
                "VariantName": "AllTraffic",
                "ModelName": {{model_name}},
                "InstanceType": "ml.m5.xlarge",
                "InitialInstanceCount": 1,
            }
        ],
    ),
)
```

`ModelName` can be the name of an existing model or a property of a model step in the same pipeline. Downstream steps reference the configuration through `step_endpoint_config.properties`, which follows the shape of the `DescribeEndpointConfig` response.

**Important**  
The EndpointConfig step adds a suffix that is unique to each pipeline execution to the name of the endpoint configuration that it creates. To use the endpoint configuration in a downstream step, reference it through `step_endpoint_config.properties.EndpointConfigName` instead of the name that you requested. If you use the requested name, the downstream step can't find the endpoint configuration and fails.

The EndpointConfig step supports retries through `retry_policies`. It doesn't support caching.

After a pipeline execution, the step's `Metadata.EndpointConfig.Arn` in `execution.list_steps()` contains the ARN of the endpoint configuration.

## Endpoint step
<a name="step-type-endpoint"></a>

Use an Endpoint step to deploy an endpoint configuration to a SageMaker AI real-time endpoint as part of a pipeline. If the endpoint doesn't exist, the step creates it with `CreateEndpoint`. If the endpoint already exists, the step updates it with `UpdateEndpoint`, so rerunning the pipeline deploys the new configuration to the same endpoint.

To create an Endpoint step, use `EndpointStep`, available in the SageMaker Python SDK v3.23.0 or later. Call `create_endpoint()` on a `PipelineSession` and pass the result as `step_args`. The following example deploys the configuration from the preceding EndpointConfig step.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.mlops.workflow import EndpointStep

pipeline_session = PipelineSession()

step_endpoint = EndpointStep(
    name="DeployEndpoint",
    step_args=pipeline_session.create_endpoint(
        endpoint_name="my-endpoint",
        config_name=step_endpoint_config.properties.EndpointConfigName,
    ),
)
```

Downstream steps reference the endpoint through `step_endpoint.properties`, which follows the shape of the `DescribeEndpoint` response. The Endpoint step doesn't support caching or retry policies.

After a pipeline execution, the step's `Metadata.Endpoint.Arn` in `execution.list_steps()` contains the ARN of the endpoint.

## InferenceComponent step
<a name="step-type-inference-component"></a>

Use an InferenceComponent step to deploy a model to an existing endpoint as an inference component. With inference components, you can host several models on one endpoint and scale each model independently. If the inference component doesn't exist, the step creates it with `CreateInferenceComponent`. If it already exists, the step updates it with `UpdateInferenceComponent`.

To create an InferenceComponent step, use `InferenceComponentStep`, available in the SageMaker Python SDK v3.23.0 or later. Call `create_inference_component()` on a `PipelineSession` and pass the result as `step_args`.

The endpoint must be created from an endpoint configuration for inference components. In that configuration, the production variant doesn't name a model, and you pass the execution role through `role`. The following example creates such an endpoint and then deploys a model to it as an inference component. Replace {{role}} with the ARN of an IAM role that SageMaker AI can assume to create the endpoint and host the model.

```python
from sagemaker.mlops.workflow import (
    EndpointConfigStep,
    EndpointStep,
    InferenceComponentStep,
)

step_ic_config = EndpointConfigStep(
    name="CreateComponentEndpointConfig",
    step_args=pipeline_session.create_endpoint_config(
        name="my-component-endpoint-config",
        production_variants=[
            {
                "VariantName": "AllTraffic",
                "InstanceType": "ml.m5.xlarge",
                "InitialInstanceCount": 1,
                "ManagedInstanceScaling": {
                    "Status": "ENABLED",
                    "MinInstanceCount": 1,
                    "MaxInstanceCount": 1,
                },
                "RoutingConfig": {"RoutingStrategy": "LEAST_OUTSTANDING_REQUESTS"},
            }
        ],
        role={{role}},
    ),
)

step_ic_endpoint = EndpointStep(
    name="DeployComponentEndpoint",
    step_args=pipeline_session.create_endpoint(
        endpoint_name="my-component-endpoint",
        config_name=step_ic_config.properties.EndpointConfigName,
    ),
)

step_component = InferenceComponentStep(
    name="CreateInferenceComponent",
    step_args=pipeline_session.create_inference_component(
        inference_component_name="my-component",
        endpoint_name=step_ic_endpoint.properties.EndpointName,
        variant_name="AllTraffic",
        specification={
            "ModelName": {{model_name}},
            "ComputeResourceRequirements": {
                "NumberOfCpuCoresRequired": 1,
                "MinMemoryRequiredInMb": 1024,
            },
        },
        runtime_config={"CopyCount": 1},
    ),
)
```

Downstream steps reference the component through `step_component.properties`, which follows the shape of the `DescribeInferenceComponent` response. The InferenceComponent step doesn't support caching or retry policies.

After a pipeline execution, the step's `Metadata.InferenceComponent.Arn` in `execution.list_steps()` contains the ARN of the inference component.

## Lineage step
<a name="step-type-lineage"></a>

Use a Lineage step to create lineage actions, artifacts, and contexts, and the associations between them, in a single pipeline step. The step creates every entity first and then adds the associations, so an association can refer to an entity that the same step creates. For more information about lineage entities, see [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md).

To create a Lineage step, use `LineageStep`, available in the SageMaker Python SDK v3.23.0 or later. Create each entity with `Action.create()`, `Artifact.create()`, or `Context.create()` and a `PipelineSession`, and pass the results to `actions`, `artifacts`, or `contexts`. Declare associations with `LineageAssociation`. The following example records a training action, the model it produced, and the association between them.

```python
from sagemaker.core.lineage import Action, Artifact
from sagemaker.mlops.workflow import (
    LineageAssociation,
    LineageEntityReference,
    LineageStep,
)

step_lineage = LineageStep(
    name="RecordLineage",
    actions=[
        Action.create(
            action_name="training-run",
            source_uri="s3://{{amzn-s3-demo-bucket}}/runs/training-run",
            action_type="ModelTraining",
            sagemaker_session=pipeline_session,
        )
    ],
    artifacts=[
        Artifact.create(
            artifact_name="trained-model",
            source_uri="s3://{{amzn-s3-demo-bucket}}/models/model.tar.gz",
            artifact_type="Model",
            sagemaker_session=pipeline_session,
        )
    ],
    associations=[
        LineageAssociation(
            source=LineageEntityReference(name="training-run", type="Action"),
            destination=LineageEntityReference(name="trained-model", type="Artifact"),
            association_type="Produced",
        )
    ],
)
```

A `LineageEntityReference` refers to an entity in one of two ways:
+ With `name` and `type` (`Action`, `Artifact`, or `Context`), for an entity that the same Lineage step creates. The SDK raises a `ValueError` if the step doesn't create an entity with that name and type.
+ With `arn`, for an entity that already exists or that another step created.

Downstream steps reference the ARNs of the created entities by name, for example `step_lineage.properties.ArtifactArns["trained-model"]`. The `ActionArns` and `ContextArns` properties work the same way. After a pipeline execution, the step's `Metadata.Lineage` in `execution.list_steps()` contains these ARN maps and the associations that the step added.

If an entity with the same name already exists, for example when the pipeline runs again, the step reuses it and updates it if its properties changed. The Lineage step doesn't support caching or retry policies.

## Job step
<a name="step-type-job"></a>

Use a Job step to run a SageMaker AI job that is created through the `CreateJob` operation, such as an agentic reinforcement fine-tuning job. The job type and its settings are defined by the producer that you use to create the step arguments.

To create a Job step, use `JobStep`, available in the SageMaker Python SDK v3.24.0 or later. Create the job with a supported producer and a `PipelineSession`, and pass the result as `step_args`. The supported producers are `MultiTurnRLTrainer` and, in the SageMaker Python SDK v3.30.0 or later, `DataPreparer`. The following example runs a `MultiTurnRLTrainer` job.

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession
from sagemaker.mlops.workflow import JobStep
from sagemaker.train import MultiTurnRLTrainer

pipeline_session = PipelineSession()

trainer = MultiTurnRLTrainer(
    model={{model}},
    agent_env={{agent_env}},
    training_dataset={{training_dataset}},
    output_model_package_group={{model_package_group}},
    s3_output_path="s3://{{amzn-s3-demo-bucket}}/mtrl/output",
    accept_eula=True,
    sagemaker_session=pipeline_session,
)

step_job = JobStep(name="TrainAgent", step_args=trainer.train(wait=False))
```

The Job step writes the job output under a separate prefix for each pipeline execution. Downstream steps reference the job through `step_job.properties`, which follows the shape of the `DescribeJob` response. You can reference members inside the job configuration document, for example `step_job.properties.JobConfigDocument.OutputModelPackageArn`. The Job step doesn't support caching or retry policies.

After a pipeline execution, the step's `Metadata.Job.Arn` in `execution.list_steps()` contains the ARN of the job.

## HubContent step
<a name="step-type-hub-content"></a>

Use a HubContent step to import content, such as a model or a dataset, into a SageMaker AI private hub as part of a pipeline. The step calls the `ImportHubContent` operation.

To create a HubContent step, use `HubContentStep`, available in the SageMaker Python SDK v3.30.0 or later. Call `import_hub_content()` on a `PipelineSession` and pass the result as `step_args`. The following example imports a model into a hub.

```python
from sagemaker.mlops.workflow import HubContentStep

step_hub_content = HubContentStep(
    name="ImportModel",
    step_args=pipeline_session.import_hub_content(
        hub_name="my-hub",
        hub_content_name="my-model",
        hub_content_type="Model",
        document_schema_version="2.4.0",
        hub_content_document={
            "Url": "{{https://example.com/my-model}}",
            "ModelTypes": ["OPEN_WEIGHTS"],
            "Capabilities": [],
            "TrainingSupported": False,
            "IncrementalTrainingSupported": False,
        },
    ),
)
```

The `hub_content_document` must follow the document schema for the content type. You can pass it as a JSON string or a dictionary, and pipeline variables inside a dictionary are resolved at run time. If you don't set `hub_content_version`, each pipeline execution imports a new version of the content.

Downstream steps reference the imported content through `step_hub_content.properties`, which follows the shape of the `DescribeHubContent` response. For example, a condition step can check `step_hub_content.properties.HubContentStatus` for the value `Available`. The HubContent step supports caching through `cache_config` and retries through `retry_policies`.

After a pipeline execution, the step's `Metadata.HubContent` in `execution.list_steps()` contains the `HubArn` and `HubContentArn`.

## Transform step
<a name="step-type-transform"></a>

You use a transform step for batch transformation to run inference on an entire dataset. For more information about batch transformation, see [Batch transforms with inference pipelines](inference-pipeline-batch.md).

A transform step requires a transformer and the data on which to run batch transformation. The following example shows how to create a Transform step definition. For more information on Transform step requirements, see the [sagemaker.workflow.steps.TransformStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep) documentation.

------
#### [ Pipeline Designer ]

To add a batch transform step to your pipeline using the drag-and-drop visual editor, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Deploy model (batch transform)** and drag it to the canvas.

1. In the canvas, choose the **Deploy model (batch transform)** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.steps.TransformStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep).

1. If the canvas includes any step that immediately precedes the **Deploy model (batch transform)** step you added, click and drag the cursor from the step to the **Deploy model (batch transform)** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Deploy model (batch transform)** step you added, click and drag the cursor from the **Deploy model (batch transform)** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

```python
from sagemaker.core.workflow.pipeline_context import PipelineSession

from sagemaker.core.transformer import Transformer
from sagemaker.train.configs import TransformInput
from sagemaker.mlops.workflow.steps import TransformStep

transformer = Transformer(..., sagemaker_session=PipelineSession())

step_transform = TransformStep(
    name="AbaloneTransform",
    step_args=transformer.transform(data="s3://{{amzn-s3-demo-bucket/my-data}}"),
)
```

------

## Condition step
<a name="step-type-condition"></a>

You use a condition step to evaluate the condition of step properties to assess which action should be taken next in the pipeline.

A condition step requires:
+ A list of conditions.
+ A list of steps to run if the condition evaluates to `true`.
+ A list of steps to run if the condition evaluates to `false`.

------
#### [ Pipeline Designer ]

To add a condition step to a pipeline using the Pipeline Designer, do the following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Condition** and drag it to the canvas.

1. In the canvas, choose the **Condition** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.condition\_step.ConditionStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.condition_step.ConditionStep).

1. If the canvas includes any step that immediately precedes the **Condition** step you added, click and drag the cursor from the step to the **Condition** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Condition** step you added, click and drag the cursor from the **Condition** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

 The following example shows how to create a `ConditionStep` definition. 

**Limitations**
+ Pipelines doesn't support the use of nested condition steps. You can't pass a condition step as the input for another condition step.
+ A condition step can't use identical steps in both branches. If you need the same step functionality in both branches, duplicate the step and give it a different name.

```python
from sagemaker.core.workflow.conditions import ConditionLessThanOrEqualTo
from sagemaker.mlops.workflow.condition_step import ConditionStep
from sagemaker.core.workflow.functions import JsonGet

cond_lte = ConditionLessThanOrEqualTo(
    left=JsonGet(
        step_name=step_eval.name,
        property_file=evaluation_report,
        json_path="regression_metrics.mse.value"
    ),
    right=6.0
)

step_cond = ConditionStep(
    name="AbaloneMSECond",
    conditions=[cond_lte],
    if_steps=[step_register, step_create_model, step_transform],
    else_steps=[]
)
```

For more information on `ConditionStep` requirements, see the [sagemaker.workflow.condition\_step.ConditionStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#conditionstep) API reference. For more information on supported conditions, see *[Amazon SageMaker Pipelines - Conditions](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#conditions)* in the SageMaker AI Python SDK documentation. 

------

## Callback step
<a name="step-type-callback"></a>

Use a `Callback` step to add additional processes and AWS services into your workflow that aren't directly provided by Amazon SageMaker Pipelines. When a `Callback` step runs, the following procedure occurs:
+ Pipelines sends a message to a customer-specified Amazon Simple Queue Service (Amazon SQS) queue. The message contains a Pipelines–generated token and a customer-supplied list of input parameters. After sending the message, Pipelines waits for a response from the customer.
+ The customer retrieves the message from the Amazon SQS queue and starts their custom process.
+ When the process finishes, the customer calls one of the following APIs and submits the Pipelines–generated token:
  +  [SendPipelineExecutionStepSuccess](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SendPipelineExecutionStepSuccess.html), along with a list of output parameters
  +  [SendPipelineExecutionStepFailure](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SendPipelineExecutionStepFailure.html), along with a failure reason
+ The API call causes Pipelines to either continue the pipeline process or fail the process.

For more information on `Callback` step requirements, see the [sagemaker.workflow.callback\_step.CallbackStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.callback_step.CallbackStep) documentation. For a complete solution, see [Extend SageMaker Pipelines to include custom steps using callback steps](https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/).

**Important**  
`Callback` steps were introduced in Amazon SageMaker Python SDK v2.45.0 and Amazon SageMaker Studio Classic v3.6.2. You must update Studio Classic before you use a `Callback` step or the pipeline DAG doesn't display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

The following sample shows an implementation of the preceding procedure.

```python
from sagemaker.mlops.workflow.callback_step import CallbackStep

step_callback = CallbackStep(
    name="MyCallbackStep",
    sqs_queue_url="https://sqs.us-east-2.amazonaws.com/012345678901/MyCallbackQueue",
    inputs={...},
    outputs=[...]
)

callback_handler_code = '
    import boto3
    import json

    def handler(event, context):
        sagemaker_client=boto3.client("sagemaker")

        for record in event["Records"]:
            payload=json.loads(record["body"])
            token=payload["token"]

            # Custom processing

            # Call SageMaker AI to complete the step
            sagemaker_client.send_pipeline_execution_step_success(
                CallbackToken=token,
                OutputParameters={...}
            )
'
```

**Note**  
Output parameters for `CallbackStep` should not be nested. For example, if you use a nested dictionary as your output parameter, then the dictionary is treated as a single string (ex. `{"output1": "{\"nested_output1\":\"my-output\"}"}`). If you provide a nested value, then when you try to refer to a particular output parameter, SageMaker AI throws a non-retryable client error.

**Stopping behavior**

A pipeline process doesn't stop while a `Callback` step is running.

When you call [StopPipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopPipelineExecution.html) on a pipeline process with a running `Callback` step, Pipelines sends an Amazon SQS message to the SQS queue. The body of the SQS message contains a **Status** field, which is set to `Stopping`. The following shows an example SQS message body.

```json
{
  "token": "26vcYbeWsZ",
  "pipelineExecutionArn": "arn:aws:sagemaker:us-east-2:012345678901:pipeline/callback-pipeline/execution/7pinimwddh3a",
  "arguments": {
    "number": 5,
    "stringArg": "some-arg",
    "inputData": "s3://sagemaker-us-west-2-012345678901/abalone/abalone-dataset.csv"
  },
  "status": "Stopping"
}
```

You should add logic to your Amazon SQS message consumer to take any needed action (for example, resource cleanup) upon receipt of the message. Then add a call to `SendPipelineExecutionStepSuccess` or `SendPipelineExecutionStepFailure`.

Only when Pipelines receives one of these calls does it stop the pipeline process.

## Lambda step
<a name="step-type-lambda"></a>

You use a Lambda step to run an AWS Lambda function. You can run an existing Lambda function, or SageMaker AI can create and run a new Lambda function. If you choose to use an existing Lambda function, it must be in the same AWS Region as the SageMaker AI pipeline. For a notebook that shows how to use a Lambda step in a SageMaker AI pipeline, see [sagemaker-pipelines-lambda-step.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/lambda-step/sagemaker-pipelines-lambda-step.ipynb).

**Important**  
Lambda steps were introduced in Amazon SageMaker Python SDK v2.51.0 and Amazon SageMaker Studio Classic v3.9.1. You must update Studio Classic before you use a Lambda step or the pipeline DAG doesn't display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

SageMaker AI provides the [sagemaker.lambda\_helper.Lambda](https://sagemaker.readthedocs.io/en/stable/api/utility/lambda_helper.html) class to create, update, invoke, and delete Lambda functions. `Lambda` has the following signature.

```python
Lambda(
    function_arn,       # Only required argument to invoke an existing Lambda function

    # The following arguments are required to create a Lambda function:
    function_name,
    execution_role_arn,
    zipped_code_dir,    # Specify either zipped_code_dir and s3_bucket, OR script
    s3_bucket,          # S3 bucket where zipped_code_dir is uploaded
    script,             # Path of Lambda function script
    handler,            # Lambda handler specified as "lambda_script.lambda_handler"
    timeout,            # Maximum time the Lambda function can run before the lambda step fails
    ...
)
```

The [sagemaker.workflow.lambda\_step.LambdaStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.lambda_step.LambdaStep) class has a `lambda_func` argument of type `Lambda`. To invoke an existing Lambda function, the only requirement is to supply the Amazon Resource Name (ARN) of the function to `function_arn`. If you don't supply a value for `function_arn`, you must specify `handler` and one of the following:
+ `zipped_code_dir` – The path of the zipped Lambda function

  `s3_bucket` – Amazon S3 bucket where `zipped_code_dir` is to be uploaded
+ `script` – The path of the Lambda function script file

The following example shows how to create a `Lambda` step definition that invokes an existing Lambda function.

```python
from sagemaker.mlops.workflow.lambda_step import LambdaStep
from sagemaker.lambda_helper import Lambda

step_lambda = LambdaStep(
    name="ProcessingLambda",
    lambda_func=Lambda(
        function_arn="arn:aws:lambda:us-west-2:012345678910:function:split-dataset-lambda"
    ),
    inputs={
        s3_bucket = s3_bucket,
        data_file = data_file
    },
    outputs=[
        "train_file", "test_file"
    ]
)
```

The following example shows how to create a `Lambda` step definition that creates and invokes a Lambda function using a Lambda function script.

```python
from sagemaker.workflow.lambda_step import LambdaStep
from sagemaker.lambda_helper import Lambda

step_lambda = LambdaStep(
    name="ProcessingLambda",
    lambda_func=Lambda(
      function_name="split-dataset-lambda",
      execution_role_arn=execution_role_arn,
      script="lambda_script.py",
      handler="lambda_script.lambda_handler",
      ...
    ),
    inputs={
        s3_bucket = s3_bucket,
        data_file = data_file
    },
    outputs=[
        "train_file", "test_file"
    ]
)
```

**Inputs and outputs**

If your `Lambda` function has inputs or outputs, these must also be defined in your `Lambda` step.

**Note**  
Input and output parameters should not be nested. For example, if you use a nested dictionary as your output parameter, then the dictionary is treated as a single string (ex. `{"output1": "{\"nested_output1\":\"my-output\"}"}`). If you provide a nested value and try to refer to it later, a non-retryable client error is thrown.

When defining the `Lambda` step, `inputs` must be a dictionary of key-value pairs. Each value of the `inputs` dictionary must be a primitive type (string, integer, or float). Nested objects are not supported. If left undefined, the `inputs` value defaults to `None`.

The `outputs` value must be a list of keys. These keys refer to a dictionary defined in the output of the `Lambda` function. Like `inputs`, these keys must be primitive types, and nested objects are not supported.

**Timeout and stopping behavior**

The `Lambda` class has a `timeout` argument that specifies the maximum time that the Lambda function can run. The default value is 120 seconds with a maximum value of 10 minutes. If the Lambda function is running when the timeout is met, the Lambda step fails; however, the Lambda function continues to run.

A pipeline process can't be stopped while a Lambda step is running because the Lambda function invoked by the Lambda step can't be stopped. If you stop the process while the Lambda function is running, the pipeline waits for the function to finish or until the timeout is hit. This depends on whichever occurs first. The process then stops. If the Lambda function finishes, the pipeline process status is `Stopped`. If the timeout is hit the pipeline process status is `Failed`.

## ClarifyCheck step
<a name="step-type-clarify-check"></a>

You can use the `ClarifyCheck` step to conduct baseline drift checks against previous baselines for bias analysis and model explainability. You can then generate and [register your baselines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-calculations) with the `model.register()` method and pass the output of that method to [Model step](#step-type-model) using `[step\_args](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#model-step)`. These baselines for drift check can be used by Amazon SageMaker Model Monitor for your model endpoints. As a result, you don’t need to do a [baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html) suggestion separately. 

The `ClarifyCheck` step can also pull baselines for drift check from the model registry. The `ClarifyCheck` step uses the SageMaker Clarify prebuilt container. This container provides a range of model monitoring capabilities, including constraint suggestion and constraint validation against a given baseline. For more information, see [Prebuilt SageMaker Clarify Containers](clarify-processing-job-configure-container.md).

### Configuring the ClarifyCheck step
<a name="configuring-step-type-clarify"></a>

You can configure the `ClarifyCheck` step to conduct only one of the following check types each time it’s used in a pipeline.
+ Data bias check
+ Model bias check
+ Model explainability check

To do this, set the `clarify_check_config` parameter with one of the following check type values:
+ `DataBiasCheckConfig`
+ `ModelBiasCheckConfig`
+ `ModelExplainabilityCheckConfig`

The `ClarifyCheck` step launches a processing job that runs the SageMaker AI Clarify prebuilt container and requires dedicated [configurations for the check and the processing job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html). `ClarifyCheckConfig` and `CheckJobConfig` are helper functions for these configurations. These helper functions are aligned with how the SageMaker Clarify processing job computes for checking model bias, data bias, or model explainability. For more information, see [Run SageMaker Clarify Processing Jobs for Bias Analysis and Explainability](clarify-processing-job-run.md). 

### Controlling step behaviors for drift check
<a name="controlling-step-type-clarify"></a>

The `ClarifyCheck` step requires the following two boolean flags to control its behavior:
+ `skip_check`: This parameter indicates if the drift check against the previous baseline is skipped or not. If it is set to `False`, the previous baseline of the configured check type must be available.
+ `register_new_baseline`: This parameter indicates if a newly calculated baseline can be accessed though step property `BaselineUsedForDriftCheckConstraints`. If it is set to `False`, the previous baseline of the configured check type also must be available. This can be accessed through the `BaselineUsedForDriftCheckConstraints` property. 

For more information, see [Baseline calculation, drift detection and lifecycle with ClarifyCheck and QualityCheck steps in Amazon SageMaker Pipelines](pipelines-quality-clarify-baseline-lifecycle.md).

### Working with baselines
<a name="step-type-clarify-working-with-baselines"></a>

You can optionally specify the `model_package_group_name` to locate the existing baseline. Then, the `ClarifyCheck` step pulls the `DriftCheckBaselines` on the latest approved model package in the model package group. 

Or, you can provide a previous baseline through the `supplied_baseline_constraints` parameter. If you specify both the `model_package_group_name` and the `supplied_baseline_constraints`, the `ClarifyCheck` step uses the baseline specified by the `supplied_baseline_constraints` parameter.

For more information on using the `ClarifyCheck` step requirements, see the [ sagemaker.workflow.steps.ClarifyCheckStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.clarify_check_step.ClarifyCheckStep) in the *Amazon SageMaker AI SageMaker AI SDK for Python (Boto)*. For an Amazon SageMaker Studio Classic notebook that shows how to use `ClarifyCheck` step in Pipelines, see [sagemaker-pipeline-model-monitor-clarify-steps.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb).

**Example Create a `ClarifyCheck` step for data bias check**  

```Python
from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.mlops.workflow.clarify_check_step import DataBiasCheckConfig, ClarifyCheckStep
from sagemaker.workflow.execution_variables import ExecutionVariables
from sagemaker.core.clarify import DataConfig, BiasConfig
from sagemaker.core.workflow.functions import Join

check_job_config = CheckJobConfig(
    role=role,
    instance_count=1,
    instance_type="{{ml.c5.xlarge}}",
    volume_size_in_gb={{120}},
    sagemaker_session=sagemaker_session,
)

data_bias_data_config = DataConfig(
    s3_data_input_path=step_process.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri,
    s3_output_path=Join(on='/', values=['s3:/', your_bucket, base_job_prefix, ExecutionVariables.PIPELINE_EXECUTION_ID, '{{databiascheckstep}}']),
    label=0,
    dataset_type="{{text/csv}}",
    s3_analysis_config_output_path=data_bias_analysis_cfg_output_path,
)

data_bias_config = BiasConfig(
    label_values_or_threshold=[{{15.0}}], facet_name=[{{8}}], facet_values_or_threshold=[[{{0.5}}]]  
)

data_bias_check_config = DataBiasCheckConfig(
    data_config=data_bias_data_config,
    data_bias_config=data_bias_config,
)

data_bias_check_step = ClarifyCheckStep(
    name="{{DataBiasCheckStep}}",
    clarify_check_config=data_bias_check_config,
    check_job_config=check_job_config,
    skip_check=False,
    register_new_baseline=False,
    supplied_baseline_constraints="{{s3://sagemaker-us-west-2-111122223333/baseline/analysis.json}}",
    model_package_group_name="{{MyModelPackageGroup}}"
)
```

## QualityCheck step
<a name="step-type-quality-check"></a>

Use the `QualityCheck` step to conduct [baseline suggestions](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html) and drift checks against a previous baseline for data quality or model quality in a pipeline. You can then generate and [register your baselines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-quality-clarify-baseline-lifecycle.html#pipelines-quality-clarify-baseline-calculations) with the `model.register()` method and pass the output of that method to [Model step](#step-type-model) using `[step\_args](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#model-step)`. ]

Model Monitor can use these baselines for drift check for your model endpoints so that you don’t need to do a baseline suggestion separately. The `QualityCheck` step can also pull baselines for drift check from the model registry. The `QualityCheck` step leverages the Amazon SageMaker AI Model Monitor prebuilt container. This container has a range of model monitoring capabilities including constraint suggestion, statistics generation, and constraint validation against a baseline. For more information, see [Amazon SageMaker Model Monitor prebuilt container](model-monitor-pre-built-container.md).

### Configuring the QualityCheck step
<a name="configuring-step-type-quality"></a>

You can configure the `QualityCheck` step to run only one of the following check types each time it’s used in a pipeline.
+ Data quality check
+ Model quality check

You do this by setting the `quality_check_config` parameter with one of the following check type values:
+ `DataQualityCheckConfig`
+ `ModelQualityCheckConfig`

The `QualityCheck` step launches a processing job that runs the Model Monitor prebuilt container and requires dedicated configurations for the check and the processing job. The `QualityCheckConfig` and `CheckJobConfig` are helper functions for these configurations. These helper functions are aligned with how Model Monitor creates a baseline for the model quality or data quality monitoring. For more information on the Model Monitor baseline suggestions, see [Create a Baseline](model-monitor-create-baseline.md) and [Create a model quality baseline](model-monitor-model-quality-baseline.md).

### Controlling step behaviors for drift check
<a name="controlling-step-type-quality"></a>

The `QualityCheck` step requires the following two Boolean flags to control its behavior:
+ `skip_check`: This parameter indicates if the drift check against the previous baseline is skipped or not. If it is set to `False`, the previous baseline of the configured check type must be available.
+ `register_new_baseline`: This parameter indicates if a newly calculated baseline can be accessed through step properties `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics`. If it is set to `False`, the previous baseline of the configured check type must also be available. These can be accessed through the `BaselineUsedForDriftCheckConstraints` and `BaselineUsedForDriftCheckStatistics` properties.

For more information, see [Baseline calculation, drift detection and lifecycle with ClarifyCheck and QualityCheck steps in Amazon SageMaker Pipelines](pipelines-quality-clarify-baseline-lifecycle.md).

### Working with baselines
<a name="step-type-quality-working-with-baselines"></a>

You can specify a previous baseline directly through the `supplied_baseline_statistics` and `supplied_baseline_constraints` parameters. You can also specify the `model_package_group_name` and the `QualityCheck` step pulls the `DriftCheckBaselines` on the latest approved model package in the model package group. 

When you specify the following, the `QualityCheck` step uses the baseline specified by `supplied_baseline_constraints` and `supplied_baseline_statistics` on the check type of the `QualityCheck` step.
+ `model_package_group_name`
+ `supplied_baseline_constraints`
+ `supplied_baseline_statistics`

For more information on using the `QualityCheck` step requirements, see the [sagemaker.workflow.steps.QualityCheckStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.quality_check_step.QualityCheckStep) in the *Amazon SageMaker AI SageMaker AI SDK for Python (Boto)*. For an Amazon SageMaker Studio Classic notebook that shows how to use `QualityCheck` step in Pipelines, see [sagemaker-pipeline-model-monitor-clarify-steps.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb). 

**Example Create a `QualityCheck` step for data quality check**  

```Python
from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.mlops.workflow.quality_check_step import DataQualityCheckConfig, QualityCheckStep
from sagemaker.workflow.execution_variables import ExecutionVariables
from sagemaker.core.model_monitor.dataset_format import DatasetFormat
from sagemaker.core.workflow.functions import Join

check_job_config = CheckJobConfig(
    role=role,
    instance_count=1,
    instance_type="{{ml.c5.xlarge}}",
    volume_size_in_gb={{120}},
    sagemaker_session=sagemaker_session,
)

data_quality_check_config = DataQualityCheckConfig(
    baseline_dataset=step_process.properties.ProcessingOutputConfig.Outputs["{{train}}"].S3Output.S3Uri,
    dataset_format=DatasetFormat.csv(header=False, output_columns_position="START"),
    output_s3_uri=Join(on='/', values=['s3:/', your_bucket, base_job_prefix, ExecutionVariables.PIPELINE_EXECUTION_ID, 'dataqualitycheckstep'])
)

data_quality_check_step = QualityCheckStep(
    name="DataQualityCheckStep",
    skip_check=False,
    register_new_baseline=False,
    quality_check_config=data_quality_check_config,
    check_job_config=check_job_config,
    supplied_baseline_statistics="s3://{{sagemaker-us-west-2-555555555555/baseline/statistics.json}}",
    supplied_baseline_constraints="s3://{{sagemaker-us-west-2-555555555555/baseline/constraints.json}}",
    model_package_group_name="{{MyModelPackageGroup}}"
)
```

## EMR step
<a name="step-type-emr"></a>

Use the Amazon SageMaker Pipelines [EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-overview.html) step to:
+ Process [Amazon EMR steps](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-work-with-steps.html) on a running Amazon EMR cluster.
+ Have the pipeline create and manage an Amazon EMR cluster for you.

For more information about Amazon EMR, see [Getting started with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html).

The EMR step requires that `EMRStepConfig` include the location of the JAR file used by the Amazon EMR cluster and any arguments to be passed. You also provide the Amazon EMR cluster ID if you want to run the step on a running EMR cluster. You can also pass the cluster configuration to run the EMR step on a cluster that it creates, manages, and terminates for you. The following sections include examples and links to sample notebooks demonstrating both methods.

**Note**  
EMR steps require that the role passed to your pipeline has additional permissions. Attach the [AWS managed policy: `AmazonSageMakerPipelinesIntegrations`](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-pipelines.html#security-iam-awsmanpol-AmazonSageMakerPipelinesIntegrations) to your pipeline role, or ensure that the role includes the permissions in that policy.
If you process an EMR step on a running cluster, you can only use a cluster that is in one of the following states:   
`STARTING`
`BOOTSTRAPPING`
`RUNNING`
`WAITING`
If you process EMR steps on a running cluster, you can have at most 256 EMR steps in a `PENDING` state on an EMR cluster. EMR steps submitted beyond this limit result in pipeline execution failure. You may consider using [Retry Policy for Pipeline Steps](pipelines-retry-policy.md).
You can specify either cluster ID or cluster configuration, but not both.
The EMR step relies on Amazon EventBridge to monitor changes in the EMR step or cluster state. If you process your Amazon EMR job on a running cluster, the EMR step uses the `SageMakerPipelineExecutionEMRStepStatusUpdateRule` rule to monitor EMR step state. If you process your job on a cluster that the EMR step creates, the step uses the `SageMakerPipelineExecutionEMRClusterStatusRule` rule to monitor changes in cluster state. If you see either of these EventBridge rules in your AWS account, do not delete them or else your EMR step may not complete.

**Add an Amazon EMR step to your pipeline**

To add an EMR step to your pipeline, do the following:
+ Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).
+ In the left navigation pane, select **Pipelines**.
+ Choose **Create**.
+ Choose **Blank**.
+ In the left sidebar, choose **Process data** and drag it to the canvas.
+ In the canvas, choose the **Process data** step you added.
+ In the right sidebar, under mode, choose **EMR (managed)**.
+ In the right sidebar, complete the forms in the **Setting and Details** tabs. For information about the fields in these tabs, see [sagemaker.workflow.fail\_step.EMRstep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.emr_step.EMRStep).

**Launch a new job on a running Amazon EMR cluster**

To launch a new job on a running Amazon EMR cluster, pass the cluster ID as a string to the `cluster_id` argument of `EMRStep`. The following example demonstrates this procedure.

```Python
from sagemaker.workflow.emr_step import EMRStep, EMRStepConfig

emr_config = EMRStepConfig(
    jar="{{jar-location}}", # required, path to jar file used
    args=["--verbose", "--force"], # optional list of arguments to pass to the jar
    main_class="com.my.Main1", # optional main class, this can be omitted if jar above has a manifest 
    properties=[ # optional list of Java properties that are set when the step runs
    {
        "key": "mapred.tasktracker.map.tasks.maximum",
        "value": "2"
    },
    {
        "key": "mapreduce.map.sort.spill.percent",
        "value": "0.90"
   },
   {
       "key": "mapreduce.tasktracker.reduce.tasks.maximum",
       "value": "5"
    }
  ]
)

step_emr = EMRStep (
    name="EMRSampleStep", # required
    cluster_id="j-1ABCDEFG2HIJK", # include cluster_id to use a running cluster
    step_config=emr_config, # required
    display_name="My EMR Step",
    description="Pipeline step to execute EMR job"
)
```

For a sample notebook that guides you through a complete example, see [ Pipelines EMR Step With Running EMR Cluster](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-running-emr-cluster.ipynb).

**Launch a new job on a new Amazon EMR cluster**

To launch a new job on a new cluster that `EMRStep` creates for you, provide your cluster configuration as a dictionary. The dictionary must have the same structure as a [RunJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html) request. However, do not include the following fields in your cluster configuration:
+ [`Name`]
+ [`Steps`]
+ [`AutoTerminationPolicy`]
+ [`Instances`][`KeepJobFlowAliveWhenNoSteps`]
+ [`Instances`][`TerminationProtected`]

All other `RunJobFlow` arguments are available for use in your cluster configuration. For details about the request syntax, see [RunJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html).

The following example passes a cluster configuration to an EMR step definition. This prompts the step to launch a new job on a new EMR cluster. The EMR cluster configuration in this example includes specifications for primary and core EMR cluster nodes. For more information about Amazon EMR node types, see [ Understand node types: primary, core, and task nodes](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html).

```Python
from sagemaker.workflow.emr_step import EMRStep, EMRStepConfig

emr_step_config = EMRStepConfig(
    jar="{{jar-location}}", # required, path to jar file used
    args=["--verbose", "--force"], # optional list of arguments to pass to the jar
    main_class="com.my.Main1", # optional main class, this can be omitted if jar above has a manifest 
    properties=[ # optional list of Java properties that are set when the step runs
    {
        "key": "mapred.tasktracker.map.tasks.maximum",
        "value": "2"
    },
    {
        "key": "mapreduce.map.sort.spill.percent",
        "value": "0.90"
   },
   {
       "key": "mapreduce.tasktracker.reduce.tasks.maximum",
       "value": "5"
    }
  ]
)

# include your cluster configuration as a dictionary
emr_cluster_config = {
    "Applications": [
        {
            "Name": "Spark", 
        }
    ],
    "Instances":{
        "InstanceGroups":[
            {
                "InstanceRole": "MASTER",
                "InstanceCount": 1,
                "InstanceType": "m5.2xlarge"
            },
            {
                "InstanceRole": "CORE",
                "InstanceCount": 2,
                "InstanceType": "m5.2xlarge"
            }
        ]
    },
    "BootstrapActions":[],
    "ReleaseLabel": "emr-6.6.0",
    "JobFlowRole": "{{job-flow-role}}",
    "ServiceRole": "{{service-role}}"
}

emr_step = EMRStep(
    name="emr-step",
    cluster_id=None,
    display_name="emr_step",
    description="MyEMRStepDescription",
    step_config=emr_step_config,
    cluster_config=emr_cluster_config
)
```

For a sample notebook that guides you through a complete example, see [ Pipelines EMR Step With Cluster Lifecycle Management](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-cluster-lifecycle-management.ipynb).

## EMR serverless step
<a name="step-type-serverless"></a>

To add an EMR serverless step to your pipeline, do the following:
+ Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).
+ In the left navigation pane, select **Pipelines**.
+ Choose **Create**.
+ Choose **Blank**.
+ In the left sidebar, choose **Process data** and drag it to the canvas.
+ In the canvas, choose the **Process data** step you added.
+ In the right sidebar, under mode, choose **EMR (serverless)**.
+ In the right sidebar, complete the forms in the **Setting and Details** tabs.

## Notebook job step
<a name="step-type-notebook-job"></a>

Use a `NotebookJobStep` to run your SageMaker Notebook Job non-interactively as a pipeline step. If you build your pipeline in the Pipelines drag-and-drop UI, use the [Execute code step](#step-type-executecode) to run your notebook. For more information about SageMaker Notebook Jobs, see [SageMaker Notebook Jobs](notebook-auto-run.md).

A `NotebookJobStep` requires at minimum an input notebook, image URI and kernel name. For more information about Notebook Job step requirements and other parameters you can set to customize your step, see [sagemaker.workflow.steps.NotebookJobStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep).

The following example uses minimum arguments to define a `NotebookJobStep`.

```py
from sagemaker.workflow.notebook_job_step import NotebookJobStep


notebook_job_step = NotebookJobStep(
    input_notebook={{input_notebook}},
    image_uri={{image_uri}},
    kernel_name={{kernel_name}}
)
```

Your `NotebookJobStep` pipeline step is treated as a SageMaker notebook job. As a result, track the execution status in the Studio Classic UI notebook job dashboard by including specific tags with the `tags` argument. For more details about tags to include, see [View your notebook jobs in the Studio UI dashboard](create-notebook-auto-run-sdk.md#create-notebook-auto-run-dash).

Also, if you schedule your notebook job using the SageMaker Python SDK, you can only specify certain images to run your notebook job. For more information, see [Image constraints for SageMaker AI Python SDK notebook jobs](notebook-auto-run-constraints.md#notebook-auto-run-constraints-image-sdk).

## Athena step
<a name="step-type-athena"></a>

Use an Athena step to run an Amazon Athena query from your pipeline. The step calls the Athena `StartQueryExecution` operation and monitors the query until it reaches a terminal state. A downstream step, such as a training or processing step, can then consume the query results.

### Define an Athena step
<a name="step-type-athena-define"></a>

To create an Athena step, use `AthenaStep` with an `AthenaQueryConfig`, available in the SageMaker Python SDK v3.28.0 or later. `AthenaQueryConfig` builds the Athena `StartQueryExecution` request for the step. The following example shows how to create an Athena step.

```python
from sagemaker.mlops.workflow import AthenaQueryConfig, AthenaStep

step_query = AthenaStep(
    name="QueryTransactions",
    query_config=AthenaQueryConfig(
        query_string="SELECT * FROM daily_txn WHERE txn_date >= ?",
        execution_parameters=["CAST('2026-01-01' AS DATE)"],
        catalog="AwsDataCatalog",
        database="prod_transactions",
        work_group="primary",
        output_location="s3://{{amzn-s3-demo-bucket}}/sagemaker-athena-staging/",
        encryption_option="SSE_S3",
    ),
)
```

For a `StartQueryExecution` member that `AthenaQueryConfig` doesn't cover, pass the complete request as a dictionary with the API's PascalCase keys to `query_config`. The dictionary is used unchanged. Don't set `ClientRequestToken`, because the pipeline generates it at run time.

The `query_string` must be literal SQL text. A pipeline parameter or other pipeline variable in `query_string` is rejected when the pipeline is created. To bind runtime values, use `?` placeholders in the query and pass the values in `execution_parameters`, which accepts pipeline parameters. Each `execution_parameters` value is a SQL expression that Athena substitutes for a `?` placeholder in order; it is not a typed parameter binding and is not quoted for you. A string value must include its own embedded single quotes, and the preceding example uses `CAST` to supply a `DATE` for the `txn_date >= ?` comparison.

### Reference the query results in downstream steps
<a name="step-type-athena-reference-results"></a>

After the query reaches a terminal state, the step publishes output properties from the Athena query execution. Downstream steps reference them through `step_query.properties.QueryExecution`, which follows the shape of the Athena `GetQueryExecution` response. The effective result location is `step_query.properties.QueryExecution.ResultConfiguration.OutputLocation`. The following example passes the result location to a training step.

For a `SELECT` query, `OutputLocation` is the Amazon S3 URI of the result CSV file, not a prefix. It is absent when Athena returns managed query results, and a downstream step that reads it then fails.

```python
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData
from sagemaker.mlops.workflow import TrainingStep

model_trainer = ModelTrainer(..., sagemaker_session=pipeline_session)

step_train = TrainingStep(
    name="TrainModel",
    step_args=model_trainer.train(
        input_data_config=[
            InputData(
                channel_name="train",
                data_source=step_query.properties.QueryExecution.ResultConfiguration.OutputLocation,
            )
        ]
    ),
)
```

### View the query results
<a name="step-type-athena-view-results"></a>

After a pipeline execution, `execution.list_steps()` returns the step details from `ListPipelineExecutionSteps`. For an Athena step, `Metadata.Athena` contains the `QueryExecutionId`, which you can use to find the query in the Athena console, and the `S3OutputLocation` of the results. `S3OutputLocation` is absent when Athena returns managed query results with no Amazon S3 location.

```python
execution = pipeline.start()
execution.wait()

for step in execution.list_steps():
    if step["StepName"] == "QueryTransactions":
        print(step["Metadata"]["Athena"])
```

### Query types and output files
<a name="step-type-athena-query-types"></a>

How an Athena step produces output, and whether a downstream step can consume it, depends on the query type.
+ A `SELECT` (DML) query writes CSV results to the `output_location`. The CSV includes a header row and uses the column order that Athena returns, so you might need a processing step to reshape the data (for example, to remove the header or move the target column first) before training.
+ An `UNLOAD` query writes output to the Amazon S3 path that you specify inside the SQL statement, not to the step result location. The supported output formats are `ORC`, `PARQUET`, `AVRO`, `JSON`, and `TEXTFILE`. Reference that Amazon S3 path directly in your downstream step rather than the step output property.
+ A DDL query, such as `CREATE TABLE`, produces no data output for downstream consumption.

### Caching and retries
<a name="step-type-athena-caching-retries"></a>

Athena steps support step caching through `cache_config`, Athena result reuse through the `result_reuse_max_age_in_minutes` parameter of `AthenaQueryConfig`, and retries through `retry_policies`.

**Warning**  
A retry within the same pipeline execution can return the original query execution instead of running the query again. A new pipeline execution runs the query again, so make sure that side-effecting queries, such as `INSERT`, `CREATE TABLE AS`, or `UNLOAD` to a fixed location, are safe to repeat.

### Permissions
<a name="step-type-athena-permissions"></a>

The pipeline execution role requires the following permissions:
+ `athena:StartQueryExecution`, `athena:GetQueryExecution`, and `athena:StopQueryExecution`.
+ Amazon Simple Storage Service (Amazon S3) permissions to read from the queried data location and to write query results to the `output_location`.
+ AWS Glue Data Catalog permissions to read the table and database metadata that your query references.
+ AWS Key Management Service (AWS KMS) permissions if the queried data or the query results are encrypted with a customer managed key.
+ AWS Lake Formation permissions if your query reads tables that are governed by Lake Formation.

**Note**  
Because Athena is a managed service, it cannot write results to an Amazon S3 bucket that is restricted to a VPC endpoint.

## ForEach step
<a name="step-type-foreach"></a>

Use a ForEach step for runtime fan-out. An upstream step emits a list, the ForEach body runs once for each item in the list, and the results are collected back into a single value for downstream steps. The body can be a single step or several steps that form a mini directed acyclic graph (DAG).

**Note**  
A ForEach body cannot contain a `Condition` step, a `Fail` step, or another `ForEach` step. Nested ForEach steps are not supported.

### Define a ForEach step
<a name="step-type-foreach-define"></a>

To create a ForEach step, use `ForEachStep`, available in the SageMaker Python SDK v3.27.0 or later. Inside a body step, `CurrentItem()` references the current item. The following example trains one model for each dataset in a pipeline parameter whose value is a JSON list string, and selects the iteration with the highest metric.

```python
from sagemaker.core.workflow.parameters import ParameterString
from sagemaker.mlops.workflow import (
    CurrentItem,
    ForEachSelector,
    ForEachStep,
    IterationOutput,
    TrainingStep,
)
from sagemaker.train import ModelTrainer
from sagemaker.train.configs import InputData

dataset_paths = ParameterString(
    name="DatasetPaths",
    default_value='[{"s3": "s3://{{amzn-s3-demo-bucket}}/datasets/a/"}, '
    '{"s3": "s3://{{amzn-s3-demo-bucket}}/datasets/b/"}]',
)

model_trainer = ModelTrainer(..., sagemaker_session=pipeline_session)

train_on_item = TrainingStep(
    name="TrainOnItem",
    step_args=model_trainer.train(
        input_data_config=[InputData(channel_name="train", data_source=CurrentItem().s3)]
    ),
)

step_foreach = ForEachStep(
    name="TrainEachDataset",
    iterable_items=dataset_paths,
    max_concurrency=5,
    for_each_body=[train_on_item],
    selector=ForEachSelector(
        pick="MaxBy",
        field=IterationOutput(train_on_item).FinalMetricDataList[0].Value,
    ),
)
```

`ForEachStep` takes the following parameters:
+ `iterable_items`: Required. The list to fan out over. Provide a pipeline parameter or step property that resolves to a JSON list string at run time, or a Python list whose elements are pipeline variables or scalar values (`str`, `int`, `float`, or `bool`). Each list element is one iteration item. In both forms, the list can have at most 100 items. If a list that resolves at run time has more than 100 items, the ForEach step fails.
+ `max_concurrency`: Required. The maximum number of body steps that run at the same time, across all iterations, from 1 to 50.
+ `for_each_body`: Required. The steps to run for each item. A body step is created the same way as a standalone step. Each item creates one child step for every body step, with the ID `{{<BodyStepName>}}-{{<index>}}`. Body step names must be unique across all ForEach bodies in the pipeline, and no other step name can have the form `{{<BodyStepName>}}-{{<digits>}}`.
+ `selector`: Optional. A `ForEachSelector` that picks one iteration as the selected result. Set `pick` to `MaxBy` or `MinBy`, and set `field` to an `IterationOutput` reference to a numeric output member of a body step, at least one member deep, for example `IterationOutput(train_on_item).FinalMetricDataList[0].Value`. A bare `IterationOutput(train_on_item)` is rejected. `FinalMetricDataList[0]` depends on the order in which the training job reports its metrics, so make sure that the metric at that index is the one you want to compare.

You don't need to add the body steps to the pipeline's `steps` list. They are included through `for_each_body`.

### Reference the current item
<a name="step-type-foreach-current-item"></a>

Body steps reference the current item through `CurrentItem()`:
+ `CurrentItem()`: The current item itself. Use this form when the items are scalars.
+ `CurrentItem().{{<key>}}`: The value of a top-level key of the current item, when the items are JSON objects. Only top-level key access is supported.

### Reference the collected output
<a name="step-type-foreach-collected-output"></a>

The ForEach step is the join node. Downstream steps depend on it and reference its collected output through `step_foreach.properties`:
+ `properties.IterationOutputs[{{<index>}}].{{<BodyStepName>}}.{{<member>}}`: A single output member of a body step for one iteration, where {{<index>}} is the zero-based iteration index. The `IterationOutputs` list is ordered by input index rather than by completion order.
+ `properties.Selected.{{<member>}}`: A member of the output of the iteration chosen by the `selector`, present only when you specify a `selector`. `Selected` directly exposes the output members of the selected body step, such as `FinalMetricDataList`, with no body-step-name or index wrapper.
+ `properties.Status`, `properties.InputItemCount`, and the `properties.{{<Total|Succeeded|Failed|Stopped>}}StepCount` counts. The overall `Status` is `Succeeded`, `Failed`, or `Stopped`.

The following example references the selected metric and the model from the first iteration.

```python
best_metric = step_foreach.properties.Selected.FinalMetricDataList[0].Value
first_model = step_foreach.properties.IterationOutputs[0].TrainOnItem.ModelArtifacts.S3ModelArtifacts
```

### View iteration results
<a name="step-type-foreach-metadata"></a>

After a pipeline execution, `execution.list_steps()` returns the step details from `ListPipelineExecutionSteps`. The ForEach step reports its counts and the selected iteration in `Metadata.ForEach`, as in the following example.

```json
{
    "StepName": "TrainEachDataset",
    "StepStatus": "Succeeded",
    "Metadata": {
        "ForEach": {
            "Status": "Succeeded",
            "InputItemCount": 2,
            "TotalStepCount": 2,
            "SucceededStepCount": 2,
            "FailedStepCount": 0,
            "StoppedStepCount": 0,
            "Selector": { "StepName": "TrainOnItem-1", "Index": 1 }
        }
    }
}
```

Each body step of each iteration is listed as a separate child step, such as `TrainOnItem-0`. A child step's `IterationContext` contains the `ParentStepName`, the zero-based `Index`, and the `Item` of its iteration.

### Behavior
<a name="step-type-foreach-behavior"></a>
+ **Failures:** If any iteration fails, the ForEach step fails and the pipeline execution stops. Body steps that are already running finish. No other body steps start, including the remaining steps of iterations in progress. Only steps with a `FAILED`, `STOPPED`, or `ANY` run condition can still run.
+ **Caching:** The ForEach step itself does not support caching. Body steps can set `cache_config`.
+ **Retries:** The ForEach step doesn't support retry policies. When you retry the pipeline execution, all iterations of the ForEach step run again. Body steps can set their own retry policies.
+ **Selective execution:** The ForEach parent is the only unit you can select. Its child steps are referenced only through the ForEach step.

## Cleanup step
<a name="step-type-cleanup"></a>

Use a Cleanup step to delete Amazon S3 data that other steps in the same pipeline execution produced. This helps you avoid orphaned intermediate copies, such as Athena query results or preprocessed datasets. A Cleanup step takes references to other steps' outputs rather than arbitrary Amazon S3 URIs, and the pipeline verifies at run time that each resolved URI belongs to a known output of a step in the current execution.

### Define a Cleanup step
<a name="step-type-cleanup-define"></a>

To create a Cleanup step, use `CleanupStep`, available in the SageMaker Python SDK v3.26.0 or later. Pass one `S3CleanupSource` for each step whose Amazon S3 output you want to delete. Amazon S3 is the only supported resource type. The following example deletes the outputs of an Athena step, a training step, and one file from a processing step.

```python
from sagemaker.mlops.workflow import CleanupStep, S3CleanupSource

step_cleanup = CleanupStep(
    name="CleanupIntermediateData",
    s3_sources=[
        S3CleanupSource(step=step_query),
        S3CleanupSource(step=step_train),
        S3CleanupSource(
            step=step_process,
            s3_uris=["s3://{{amzn-s3-demo-bucket}}/intermediate/preprocessed-data.csv"],
        ),
    ],
)
```

The Cleanup step depends on each source step. You don't need to list the source steps in `depends_on`, because the SDK adds any source step that isn't already listed. List each source step only once in `s3_sources`.

An `S3CleanupSource` takes one of two forms, depending on the type of the source step:
+ **Step only (omit `s3_uris`)**: Supported for Athena and training steps. The pipeline finds the source step's own output location and deletes within it.
+ **Step and `s3_uris`**: Supported for processing and transform steps. Each Amazon S3 URI must be an exact object URI within the source step's declared output location. A URI outside that location fails the step.

### Limits and safety
<a name="step-type-cleanup-limits-safety"></a>
+ **Best-effort deletion:** If one source fails, the Cleanup step continues with the other sources. The step ends with the status `Failed` if any source failed.
+ **Training safety cap:** A training step source deletes at most 25 objects. If the output prefix has more than 25 objects, the source fails with a `ClientError` before any object is deleted. To resolve this, narrow the step's output scope or delete the objects manually.
+ **Athena sources:** An Athena step source deletes the query result file and its metadata file. For `UNLOAD` and `CREATE TABLE AS` queries, the data files that the query writes are kept.
+ **URI limit:** A processing or transform step source can list at most 10 Amazon S3 URIs in `s3_uris`.
+ **No caching or retries:** The Cleanup step does not support caching or retry policies.
+ **VPC restriction:** The Cleanup step rejects a source training or processing step that has a `VpcConfig`, and a source transform step whose model has a `VpcConfig`.
+ **Permissions:** The pipeline execution role always requires `s3:DeleteObject`. It additionally requires `s3:ListBucket` for a training step source, and `sagemaker:DescribeModel` for transform step model verification.

**Note**  
A Cleanup step cannot delete objects in an Amazon S3 bucket that is restricted to a VPC endpoint.

### View cleanup results
<a name="step-type-cleanup-metadata"></a>

After a pipeline execution, `execution.list_steps()` returns the step details from `ListPipelineExecutionSteps`. For a Cleanup step, `Metadata.Cleanup` lists the source steps that were cleaned, failed, or skipped. Each failed entry includes an error code and message.

```json
{
    "StepName": "CleanupIntermediateData",
    "StepStatus": "Failed",
    "Metadata": {
        "Cleanup": {
            "CleanedSteps": ["QueryTransactions"],
            "FailedSteps": [
                { "StepName": "TrainModel", "ErrorCode": "ClientError", "ErrorMessage": "{{<message>}}" }
            ],
            "SkippedSteps": []
        }
    }
}
```

### Run a Cleanup step after a failure
<a name="step-type-cleanup-after-failure"></a>

By default, a Cleanup step is skipped when an upstream step fails. A Cleanup step runs only after every source step reaches a terminal state. To run cleanup after a source step fails or stops, pass each source step in `depends_on` as a `StepDependency` with `TriggerCondition.ANY`. A source step that isn't in `depends_on` is added with the default `COMPLETED` trigger, so its failure would still skip the cleanup. If an earlier failure prevents a source step from starting, that source never reaches a terminal state, the Cleanup step doesn't run, and the execution ends with the status `Failed`. For more information, see [Run conditions for steps](build-and-manage-steps.md#build-and-manage-run-conditions).

```python
from sagemaker.mlops.workflow import (
    CleanupStep,
    S3CleanupSource,
    StepDependency,
    TriggerCondition,
)

step_cleanup = CleanupStep(
    name="CleanupIntermediateData",
    s3_sources=[S3CleanupSource(step=step_query), S3CleanupSource(step=step_train)],
    depends_on=[
        StepDependency(step_query, TriggerCondition.ANY),
        StepDependency(step_train, TriggerCondition.ANY),
    ],
)
```

## Fail step
<a name="step-type-fail"></a>

Use a Fail step to stop an Amazon SageMaker Pipelines execution when a desired condition or state is not achieved. The Fail step also allows you to enter a custom error message, indicating the cause of the pipeline's execution failure.

**Note**  
When a Fail step and other pipeline steps execute at the same time, the pipeline does not terminate until all concurrent steps are completed.

### Limitations for using Fail step
<a name="step-type-fail-limitations"></a>
+ You cannot add a Fail step to the `DependsOn` list of other steps. For more information, see [Custom dependency between steps](build-and-manage-steps.md#build-and-manage-custom-dependency).
+ Other steps cannot reference the Fail step. It is *always* the last step in a pipeline's execution.
+ You cannot retry a pipeline execution ending with a Fail step.

You can create the Fail step error message in the form of a static text string. Alternatively, you can also use [Pipeline Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-parameters.html), a [Join](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html?highlight=Join#sagemaker.workflow.functions.Join) operation, or other [step properties](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#build-and-manage-properties) to create a more informative error message if you use the SDK.

------
#### [ Pipeline Designer ]

To add a Fail step to your pipeline, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. In the left navigation pane, select **Pipelines**.

1. Choose **Create**.

1. Choose **Blank**.

1. In the left sidebar, choose **Fail** and drag it to the canvas.

1. In the canvas, choose the **Fail** step you added.

1. In the right sidebar, complete the forms in the **Setting** and **Details** tabs. For information about the fields in these tabs, see [ sagemaker.workflow.fail\_step.FailStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.fail_step.FailStep).

1. If the canvas includes any step that immediately precedes the **Fail** step you added, click and drag the cursor from the step to the **Fail** step to create an edge.

1. If the canvas includes any step that immediately succeeds the **Fail** step you added, click and drag the cursor from the **Fail** step to the step to create an edge.

------
#### [ SageMaker Python SDK ]

**Example**  
The following example code snippet uses a `FailStep` with an `ErrorMessage` configured with Pipeline Parameters and a `Join` operation.  

```Python
from sagemaker.workflow.fail_step import FailStep
from sagemaker.workflow.functions import Join
from sagemaker.workflow.parameters import ParameterInteger

mse_threshold_param = ParameterInteger(name="MseThreshold", default_value=5)
step_fail = FailStep(
    name="{{AbaloneMSEFail}}",
    error_message=Join(
        on=" ", values=["{{Execution failed due to MSE >}}", mse_threshold_param]
    ),
)
```

------