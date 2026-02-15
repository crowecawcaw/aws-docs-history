# Add a step

The following describes the requirements of each step type and provides an example
implementation of the step, as well as how to add the step to a Pipelines. These are not working implementations because they don't provide
the resource and inputs needed. For a tutorial that implements these steps, see [Pipelines actions](pipelines-build.md "pipelines-build.md").

###### Note

You can also create a step from your local machine learning code by converting it to a
Pipelines step with the `@step` decorator. For more information, see [@step decorator](#step-type-custom "#step-type-custom").

Amazon SageMaker Pipelines support the following step types:

- [Execute code](#step-type-executecode "#step-type-executecode")

[Processing](#step-type-processing "#step-type-processing")

- [Training](#step-type-training "#step-type-training")
- [Tuning](#step-type-tuning "#step-type-tuning")
- [AutoML](#step-type-automl "#step-type-automl")
- [Model](#step-type-model "#step-type-model")
- [Create model](#step-type-create-model "#step-type-create-model")
- [Register
  model](#step-type-register-model "#step-type-register-model")
- [Deploy model
  (endpoint)](#step-type-deploy-model-endpoint "#step-type-deploy-model-endpoint")
- [Transform](#step-type-transform "#step-type-transform")
- [Condition](#step-type-condition "#step-type-condition")
- [Callback](#step-type-callback "#step-type-callback")
- [Lambda](#step-type-lambda "#step-type-lambda")
- [ClarifyCheck](#step-type-clarify-check "#step-type-clarify-check")
- [QualityCheck](#step-type-quality-check "#step-type-quality-check")
- [EMR](#step-type-emr "#step-type-emr")
- [Notebook Job](#step-type-notebook-job "#step-type-notebook-job")
- [Fail](#step-type-fail "#step-type-fail")

## @step decorator

If you want to orchestrate a custom ML job that leverages advanced SageMaker AI features or
other AWS services in the drag-and-drop Pipelines UI, use the [Execute code step](#step-type-executecode "#step-type-executecode").

You can create a step from local machine learning code using the `@step`
decorator. After you test your code, you can convert the function to a SageMaker AI pipeline step by
annotating it with the `@step` decorator. Pipelines creates and runs a pipeline when
you pass the output of the `@step`-decorated function as a step to your pipeline.
You can also create a multi-step DAG pipeline that includes one or more
`@step`-decorated functions as well as traditional SageMaker AI pipeline steps. For more
details about how to create a step with `@step` decorator, see [Lift-and-shift Python code with the @step decorator](pipelines-step-decorator.md "pipelines-step-decorator.md").

In the Pipelines drag-and-drop UI, you can use an **Execute code** step to
run your own code as a pipeline step. You can upload a Python function, script, or notebook
to be executed as part of your pipeline. You should use this step if you want to orchestrate
a custom ML job that leverages advanced SageMaker AI features or other AWS services.

The **Execute Code** step uploads files to your default Amazon S3 bucket for
Amazon SageMaker AI. This bucket might not have the required Cross-Origin Resource Sharing (CORS)
permissions set. To learn more about configuring CORS permissions, see [CORS Requirement for Input Image Data](sms-cors-update.md "sms-cors-update.md").

The **Execute Code** step uses an Amazon SageMaker training job to run your
code. Ensure that your IAM role has the `sagemaker:DescribeTrainingJob` and
`sagemaker:CreateTrainingJob` API permissions. To learn more about all the
required permissions for Amazon SageMaker AI and how to set them up, see [Amazon SageMaker AI API Permissions: Actions,
Permissions, and Resources Reference](api-permissions-reference.md "api-permissions-reference.md").

To add an execute code step to a pipeline using the Pipeline Designer, do the
following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Execute code** and drag it to the
   canvas.
6. In the canvas, choose the **Execute code** step you added.
7. In the right sidebar, complete the forms in the **Setting** and
   **Details** tabs.
8. You can upload a single file to execute or upload a compressed folder containing
   multiple artifacts.
9. For single file uploads, you can provide optional parameters for notebooks, python
   functions, or scripts.
10. When providing Python functions, a handler must be provided in the format
    `file.py:`<function_name>``
11. For compressed folder uploads, relative paths to your code must be provided, and you
    can optionally provide paths to a `requirements.txt` file or initialization
    script inside the compressed folder.
12. If the canvas includes any step that immediately precedes the **Execute
    code** step you added, click and drag the cursor from the step to the
    **Execute code** step to create an edge.
13. If the canvas includes any step that immediately succeeds the **Execute
    code** step you added, click and drag the cursor from the **Execute
    code** step to the step to create an edge. Outputs from **Execute
    code** steps can be referenced for Python functions.
    Use a processing step to create a processing job for data processing. For more
    information on processing jobs, see [Process Data and
    Evaluate Models](processing-job.md "processing-job.md").

Pipeline Designer
To add a processing step to a pipeline using the Pipeline Designer, do the
following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. In the left sidebar, choose **Process data** and drag it to
   the canvas.
5. In the canvas, choose the **Process data** step you
   added.
6. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.steps.ProcessingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep").
7. If the canvas includes any step that immediately precedes the
   **Process data** step you added, click and drag the cursor from
   the step to the **Process data** step to create an edge.
8. If the canvas includes any step that immediately succeeds the
   **Process data** step you added, click and drag the cursor from
   the **Process data** step to the step to create an edge.

SageMaker Python SDK
A processing step requires a processor, a Python script that defines the
processing code, outputs for processing, and job arguments. The following example
shows how to create a `ProcessingStep` definition.

```
from sagemaker.sklearn.processing import SKLearnProcessor

sklearn_processor = SKLearnProcessor(framework_version='1.0-1',
                                     role=`<role>`,
                                     instance_type='ml.m5.xlarge',
                                     instance_count=1)
```

```
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep

inputs = [
    ProcessingInput(source=`<input_data>`, destination="/opt/ml/processing/input"),
]

outputs = [
    ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
    ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
    ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
]

step_process = ProcessingStep(
    name="AbaloneProcess",
    step_args = sklearn_processor.run(inputs=inputs, outputs=outputs,
        code="abalone/preprocessing.py")
)
```

**Pass runtime parameters**

The following example shows how to pass runtime parameters from a PySpark
processor to a `ProcessingStep`.

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.spark.processing import PySparkProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep

pipeline_session = PipelineSession()

pyspark_processor = PySparkProcessor(
    framework_version='2.4',
    role=`<role>`,
    instance_type='ml.m5.xlarge',
    instance_count=1,
    sagemaker_session=pipeline_session,
)

step_args = pyspark_processor.run(
    inputs=[ProcessingInput(source=`<input_data>`, destination="/opt/ml/processing/input"),],
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

For more information on processing step requirements, see the [sagemaker.workflow.steps.ProcessingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep") documentation. For an in-depth
example, see the [Orchestrate Jobs to Train and Evaluate Models with Amazon SageMaker Pipelines](https://github.com/aws/amazon-sagemaker-examples/blob/62de6a1fca74c7e70089d77e36f1356033adbe5f/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/62de6a1fca74c7e70089d77e36f1356033adbe5f/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.ipynb")
example notebook. The _Define a Processing Step for Feature
Engineering_ section includes more information.

You use a training step to create a training job to train a model. For more information
on training jobs, see [Train a
Model with Amazon SageMaker AI](how-it-works-training.md "how-it-works-training.md").

A training step requires an estimator, as well as training and validation data
inputs.

Pipeline Designer
To add a training step to a pipeline using the Pipeline Designer, do the
following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Train model** and drag it to
   the canvas.
6. In the canvas, choose the **Train model** step you
   added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.steps.TrainingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep").
8. If the canvas includes any step that immediately precedes the **Train
   model** step you added, click and drag the cursor from the step to the
   **Train model** step to create an edge.
9. If the canvas includes any step that immediately succeeds the **Train
   model** step you added, click and drag the cursor from the
   **Train model** step to the step to create an edge.

SageMaker Python SDK
The following example shows how to create a `TrainingStep` definition.
For more information about training step requirements, see the [sagemaker.workflow.steps.TrainingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep") documentation.

```
from sagemaker.workflow.pipeline_context import PipelineSession

from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TrainingStep

from sagemaker.xgboost.estimator import XGBoost

pipeline_session = PipelineSession()

xgb_estimator = XGBoost(..., sagemaker_session=pipeline_session)

step_args = xgb_estimator.fit(
    inputs={
        "train": TrainingInput(
            s3_data=step_process.properties.ProcessingOutputConfig.Outputs[
                "train"
            ].S3Output.S3Uri,
            content_type="text/csv"
        ),
        "validation": TrainingInput(
            s3_data=step_process.properties.ProcessingOutputConfig.Outputs[
                "validation"
            ].S3Output.S3Uri,
            content_type="text/csv"
        )
    }
)

step_train = TrainingStep(
    name="TrainAbaloneModel",
    step_args=step_args,
)
```

You use a tuning step to create a hyperparameter tuning job, also known as
hyperparameter optimization (HPO). A hyperparameter tuning job runs multiple training jobs,
with each job producing a model version. For more information on hyperparameter tuning, see
[Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

The tuning job is associated with the SageMaker AI experiment for the pipeline, with the
training jobs created as trials. For more information, see [Experiments Integration](pipelines-experiments.md "pipelines-experiments.md").

A tuning step requires a [HyperparameterTuner](https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html "https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html") and training inputs. You can retrain previous tuning
jobs by specifying the `warm_start_config` parameter of the
`HyperparameterTuner`. For more information on hyperparameter tuning and
warm start, see [Run a Warm Start Hyperparameter Tuning
Job](automatic-model-tuning-warm-start.md "automatic-model-tuning-warm-start.md").

You use the [get_top_model_s3_uri](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep.get_top_model_s3_uri "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep.get_top_model_s3_uri") method of the [sagemaker.workflow.steps.TuningStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep") class to get the model artifact from
one of the top-performing model versions. For a notebook that shows how to use a
tuning step in a SageMaker AI pipeline, see [sagemaker-pipelines-tuning-step.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/tuning-step/sagemaker-pipelines-tuning-step.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/tuning-step/sagemaker-pipelines-tuning-step.ipynb").

###### Important

Tuning steps were introduced in Amazon SageMaker Python SDK v2.48.0 and Amazon SageMaker Studio Classic
v3.8.0. You must update Studio Classic before you use a tuning step or the pipeline DAG
doesn't display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md").

The following example shows how to create a `TuningStep`
definition.

```
from sagemaker.workflow.pipeline_context import PipelineSession

from sagemaker.tuner import HyperparameterTuner
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TuningStep

tuner = HyperparameterTuner(..., sagemaker_session=PipelineSession())

step_tuning = TuningStep(
    name = "HPTuning",
    step_args = tuner.fit(inputs=TrainingInput(s3_data="s3://`amzn-s3-demo-bucket/my-data`"))
)
```

**Get the best model version**

The following example shows how to get the best model version from the tuning job
using the `get_top_model_s3_uri` method. At most, the top 50 performing
versions are available ranked according to [HyperParameterTuningJobObjective](../APIReference/API_HyperParameterTuningJobObjective.md "../APIReference/API_HyperParameterTuningJobObjective.md"). The `top_k` argument is an
index into the versions, where `top_k=0` is the best-performing version and
`top_k=49` is the worst-performing version.

```
best_model = Model(
    image_uri=image_uri,
    model_data=step_tuning.get_top_model_s3_uri(
        top_k=0,
        s3_bucket=sagemaker_session.default_bucket()
    ),
    ...
)
```

For more information on tuning step requirements, see the [sagemaker.workflow.steps.TuningStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TuningStep") documentation.

Fine-tuning trains a pretrained foundation model from Amazon SageMaker JumpStart on a new
dataset. This process, also known as transfer learning, can produce accurate models with
smaller datasets and less training time. When you fine-tune a model, you can use the default
dataset or choose your own data. To learn more about fine-tuning a foundation model from
JumpStart, see [Fine-Tune a Model](jumpstart-fine-tune.md "jumpstart-fine-tune.md").

The fine-tuning step uses an Amazon SageMaker training job to customize
your model. Ensure that your IAM role has the `sagemaker:DescribeTrainingJob`
and `sagemaker:CreateTrainingJob` API permissions to execute the fine-tuning
job in your pipeline. To learn more about the required permissions for Amazon SageMaker AI and how
to set them up, see [Amazon SageMaker AI API Permissions: Actions,
Permissions, and Resources Reference](api-permissions-reference.md "api-permissions-reference.md").

To add a **Fine-tune model** step to your pipeline using the
drag-and-drop editor, follow these steps:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Fine-tune model** and drag it to the
   canvas.
6. In the canvas, choose the **Fine-tune model** step you
   added.
7. In the right sidebar, complete the forms in the **Setting** and
   **Details** tabs.
8. If the canvas includes any step that immediately precedes the **Fine-tune
   model** step you added, click and drag the cursor from the step to the
   **Fine-tune model** step to create an edge.
9. If the canvas includes any step that immediately succeeds the **Fine-tune
   model** step you added, click and drag the cursor from the
   **Fine-tune model** step to the step to create an edge.
   Use the [AutoML](https://sagemaker.readthedocs.io/en/stable/api/training/automl.html "https://sagemaker.readthedocs.io/en/stable/api/training/automl.html") API to create an AutoML job to automatically train a model. For more
   information on AutoML jobs, see [Automate model
   development with Amazon SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md").

###### Note

Currently, the AutoML step supports only [ensembling training
mode](autopilot-model-support-validation.md "autopilot-model-support-validation.md").

The following example shows how to create a definition using
`AutoMLStep`.

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.automl_step import AutoMLStep

pipeline_session = PipelineSession()

auto_ml = AutoML(...,
    role="`<role>`",
    target_attribute_name="`my_target_attribute_name`",
    mode="`ENSEMBLING`",
    sagemaker_session=pipeline_session)

input_training = AutoMLInput(
    inputs="s3://`amzn-s3-demo-bucket/my-training-data`",
    target_attribute_name="`my_target_attribute_name`",
    channel_type="training",
)
input_validation = AutoMLInput(
    inputs="s3://`amzn-s3-demo-bucket/my-validation-data`",
    target_attribute_name="`my_target_attribute_name`",
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

The AutoML step automatically trains several model candidates. Get the model with the
best objective metric from the AutoML job using the `get_best_auto_ml_model`
method as follows. You must also use an IAM `role` to access model
artifacts.

```
best_model = step_automl.get_best_auto_ml_model(`role=<role>`)
```

For more information, see the [AutoML](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.automl_step.AutoMLStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.automl_step.AutoMLStep") step in the SageMaker Python SDK.

Use a `ModelStep` to create or register a SageMaker AI model. For more information
on `ModelStep` requirements, see the [sagemaker.workflow.model_step.ModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.model_step.ModelStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.model_step.ModelStep") documentation.

### Create a model

You can use a `ModelStep` to create a SageMaker AI model. A `ModelStep`
requires model artifacts and information about the SageMaker AI instance type that you need to use
to create the model. For more information about SageMaker AI models, see [Train a
Model with Amazon SageMaker AI](how-it-works-training.md "how-it-works-training.md").

The following example shows how to create a `ModelStep` definition.

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.model import Model
from sagemaker.workflow.model_step import ModelStep

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

You can use a `ModelStep` to register a `sagemaker.model.Model`
or a `sagemaker.pipeline.PipelineModel` with the Amazon SageMaker Model Registry. A
`PipelineModel` represents an inference pipeline, which is a model composed
of a linear sequence of containers that process inference requests. For more information
about how to register a model, see [Model Registration Deployment with Model Registry](model-registry.md "model-registry.md").

The following example shows how to create a `ModelStep` that registers a
`PipelineModel`.

```
import time

from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.sklearn import SKLearnModel
from sagemaker.xgboost import XGBoostModel

pipeline_session = PipelineSession()

code_location = 's3://{0}/{1}/code'.format(`bucket_name`, prefix)

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

from sagemaker.workflow.model_step import ModelStep
from sagemaker import PipelineModel

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

You use a Create model step to create a SageMaker AI model. For more information on SageMaker AI models,
see [Train a Model with Amazon SageMaker](how-it-works-training.md "how-it-works-training.md").

A create model step requires model artifacts and information about the SageMaker AI instance
type that you need to use to create the model. The following examples show how to create a
Create model step definition. For more information about Create model step requirements, see
the [sagemaker.workflow.steps.CreateModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep") documentation.

Pipeline Designer
To add a create model step to your pipeline, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Create model** and drag it to
   the canvas.
6. In the canvas, choose the **Create model** step you
   added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.steps.CreateModelStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.CreateModelStep").
8. If the canvas includes any step that immediately precedes the **Create
   model** step you added, click and drag the cursor from the step to the
   **Create model** step to create an edge.
9. If the canvas includes any step that immediately succeeds the **Create
   model** step you added, click and drag the cursor from the
   **Create model** step to the step to create an edge.

SageMaker Python SDK

###### Important

We recommend using [Model step](#step-type-model "#step-type-model") to create models as of v2.90.0 of the SageMaker AI
Python SDK. `CreateModelStep` will continue to work in previous versions
of the SageMaker Python SDK, but is no longer actively supported.

```
from sagemaker.workflow.steps import CreateModelStep

step_create_model = CreateModelStep(
    name="AbaloneCreateModel",
    model=best_model,
    inputs=inputs
)
```

The Register model step registers a model into the SageMaker Model Registry.

Pipeline Designer
To register a model from a pipeline using the Pipeline Designer, do the
following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Register model** and drag it to
   the canvas.
6. In the canvas, choose the **Register model** step you
   added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.step_collections.RegisterModel](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel").
8. If the canvas includes any step that immediately precedes the
   **Register model** step you added, click and drag the cursor
   from the step to the **Register model** step to create an
   edge.
9. If the canvas includes any step that immediately succeeds the
   **Register model** step you added, click and drag the cursor
   from the **Register model** step to the step to create an
   edge.

SageMaker Python SDK

###### Important

We recommend using [Model step](#step-type-model "#step-type-model") to register models as of v2.90.0 of the SageMaker AI
Python SDK. `RegisterModel` will continue to work in previous versions of
the SageMaker Python SDK, but is no longer actively supported.

You use a `RegisterModel` step to register a [sagemaker.model.Model](https://sagemaker.readthedocs.io/en/stable/api/inference/model.html "https://sagemaker.readthedocs.io/en/stable/api/inference/model.html") or a [sagemaker.pipeline.PipelineModel](https://sagemaker.readthedocs.io/en/stable/api/inference/pipeline.html#pipelinemodel "https://sagemaker.readthedocs.io/en/stable/api/inference/pipeline.html#pipelinemodel") with the Amazon SageMaker Model Registry. A
`PipelineModel` represents an inference pipeline, which is a model
composed of a linear sequence of containers that process inference requests.

For more information about how to register a model, see [Model Registration Deployment with Model Registry](model-registry.md "model-registry.md"). For more information on
`RegisterModel` step requirements, see the [sagemaker.workflow.step_collections.RegisterModel](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel") documentation.

The following example shows how to create a `RegisterModel` step that
registers a `PipelineModel`.

```
import time
from sagemaker.sklearn import SKLearnModel
from sagemaker.xgboost import XGBoostModel

code_location = 's3://{0}/{1}/code'.format(`bucket_name`, prefix)

sklearn_model = SKLearnModel(model_data=processing_step.properties.ProcessingOutputConfig.Outputs['model'].S3Output.S3Uri,
 entry_point='inference.py',
 source_dir='`sklearn_source_dir/`',
 code_location=code_location,
 framework_version='1.0-1',
 role=role,
 sagemaker_session=sagemaker_session,
 py_version='py3')

xgboost_model = XGBoostModel(model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
 entry_point='inference.py',
 source_dir='`xgboost_source_dir/`',
 code_location=code_location,
 framework_version='0.90-2',
 py_version='py3',
 sagemaker_session=sagemaker_session,
 role=role)

from sagemaker.workflow.step_collections import RegisterModel
from sagemaker import PipelineModel
pipeline_model = PipelineModel(models=[sklearn_model,xgboost_model],role=role,sagemaker_session=sagemaker_session)

step_register = RegisterModel(
 name="`AbaloneRegisterModel`",
 model=pipeline_model,
 content_types=["application/json"],
 response_types=["application/json"],
 inference_instances=["`ml.t2.medium`", "`ml.m5.xlarge`"],
 transform_instances=["`ml.m5.xlarge`"],
 model_package_group_name='`sipgroup`',
)
```

If `model` isn't provided, the register model step requires an
estimator as shown in the following example.

```
from sagemaker.workflow.step_collections import RegisterModel

step_register = RegisterModel(
    name="`AbaloneRegisterModel`",
    estimator=xgb_train,
    model_data=step_train.properties.ModelArtifacts.S3ModelArtifacts,
    content_types=["text/csv"],
    response_types=["text/csv"],
    inference_instances=["`ml.t2.medium", "ml.m5.xlarge`"],
    transform_instances=["`ml.m5.xlarge`"],
    model_package_group_name=model_package_group_name,
    approval_status=model_approval_status,
    model_metrics=model_metrics
)
```

In the Pipeline Designer, use the Deploy model (endpoint) step to deploy your model to
an endpoint. You can create a new endpoint or use an existing endpoint. Real-time inference
is ideal for inference workloads where you have real-time, interactive, low latency
requirements. You can deploy your model to SageMaker AI Hosting services and get a real-time
endpoint that can be used for inference. These endpoints are fully managed and support
auto-scaling. To learn more about real-time inference in SageMaker AI, see [Real-time inference](realtime-endpoints.md "realtime-endpoints.md").

Before adding a deploy model step to your pipeline, make sure that your IAM role has
the following permissions:

- `sagemaker:CreateModel`
- `sagemaker:CreateEndpointConfig`
- `sagemaker:CreateEndpoint`
- `sagemaker:UpdateEndpoint`
- `sagemaker:DescribeModel`
- `sagemaker:DescribeEndpointConfig`
- `sagemaker:DescribeEndpoint`
  To learn more about all the required permissions for SageMaker AI and how to set them up, see
  [Amazon SageMaker AI API Permissions: Actions,
  Permissions, and Resources Reference](api-permissions-reference.md "api-permissions-reference.md").

To add a model deployment step to your Pipeline in the drag-and-drop editor, complete
the following steps:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Deploy model (endpoint)** and drag it
   to the canvas.
6. In the canvas, choose the **Deploy model (endpoint)** step you
   added.
7. In the right sidebar, complete the forms in the **Setting** and
   **Details** tabs.
8. If the canvas includes any step that immediately precedes the **Deploy model
   (endpoint)** step you added, click and drag the cursor from the step to the
   **Deploy model (endpoint)** step to create an edge.
9. If the canvas includes any step that immediately succeeds the **Deploy model
   (endpoint)** step you added, click and drag the cursor from the
   **Deploy model (endpoint)** step to the step to create an
   edge.
   You use a transform step for batch transformation to run inference on an entire dataset.
   For more information about batch transformation, see [Batch transforms with inference
   pipelines](inference-pipeline-batch.md "inference-pipeline-batch.md").

A transform step requires a transformer and the data on which to run batch
transformation. The following example shows how to create a Transform step definition. For
more information on Transform step requirements, see the [sagemaker.workflow.steps.TransformStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep") documentation.

Pipeline Designer
To add a batch transform step to your pipeline using the drag-and-drop visual
editor, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Deploy model (batch
   transform)** and drag it to the canvas.
6. In the canvas, choose the **Deploy model (batch transform)**
   step you added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.steps.TransformStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TransformStep").
8. If the canvas includes any step that immediately precedes the **Deploy
   model (batch transform)** step you added, click and drag the cursor
   from the step to the **Deploy model (batch transform)** step to
   create an edge.
9. If the canvas includes any step that immediately succeeds the **Deploy
   model (batch transform)** step you added, click and drag the cursor
   from the **Deploy model (batch transform)** step to the step to
   create an edge.

SageMaker Python SDK

```
from sagemaker.workflow.pipeline_context import PipelineSession

from sagemaker.transformer import Transformer
from sagemaker.inputs import TransformInput
from sagemaker.workflow.steps import TransformStep

transformer = Transformer(..., sagemaker_session=PipelineSession())

step_transform = TransformStep(
    name="AbaloneTransform",
    step_args=transformer.transform(data="s3://`amzn-s3-demo-bucket/my-data`"),
)
```

You use a condition step to evaluate the condition of step properties to assess which
action should be taken next in the pipeline.

A condition step requires:

- A list of conditions.
- A list of steps to run if the condition evaluates to `true`.
- A list of steps to run if the condition evaluates to `false`.

Pipeline Designer
To add a condition step to a pipeline using the Pipeline Designer, do the
following:

1. Open the Amazon SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Condition** and drag it to the
   canvas.
6. In the canvas, choose the **Condition** step you
   added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.condition_step.ConditionStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.condition_step.ConditionStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.condition_step.ConditionStep").
8. If the canvas includes any step that immediately precedes the
   **Condition** step you added, click and drag the cursor from
   the step to the **Condition** step to create an edge.
9. If the canvas includes any step that immediately succeeds the
   **Condition** step you added, click and drag the cursor from
   the **Condition** step to the step to create an edge.

SageMaker Python SDK
The following example shows how to create a `ConditionStep`
definition.

**Limitations**

- Pipelines doesn't support the use of nested condition steps. You can't pass a
  condition step as the input for another condition step.
- A condition step can't use identical steps in both branches. If you need the
  same step functionality in both branches, duplicate the step and give it a
  different name.

```
from sagemaker.workflow.conditions import ConditionLessThanOrEqualTo
from sagemaker.workflow.condition_step import ConditionStep
from sagemaker.workflow.functions import JsonGet

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

For more information on `ConditionStep` requirements, see the [sagemaker.workflow.condition_step.ConditionStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#conditionstep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#conditionstep") API reference. For more
information on supported conditions, see _[Amazon SageMaker Pipelines - Conditions](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#conditions "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#conditions")_ in the SageMaker AI Python SDK documentation.

Use a `Callback` step to add additional processes and AWS services into
your workflow that aren't directly provided by Amazon SageMaker Pipelines. When a `Callback` step
runs, the following procedure occurs:

- Pipelines sends a message to a customer-specified Amazon Simple Queue Service (Amazon SQS) queue. The message
  contains a Pipelines–generated token and a customer-supplied list of input
  parameters. After sending the message, Pipelines waits for a response from the
  customer.
- The customer retrieves the message from the Amazon SQS queue and starts their custom
  process.
- When the process finishes, the customer calls one of the following APIs and submits
  the Pipelines–generated token:
  - [SendPipelineExecutionStepSuccess](../APIReference/API_SendPipelineExecutionStepSuccess.md "../APIReference/API_SendPipelineExecutionStepSuccess.md"), along with a list of output
    parameters
  - [SendPipelineExecutionStepFailure](../APIReference/API_SendPipelineExecutionStepFailure.md "../APIReference/API_SendPipelineExecutionStepFailure.md"), along with a failure reason

- The API call causes Pipelines to either continue the pipeline process or fail the
  process.
  For more information on `Callback` step requirements, see the [sagemaker.workflow.callback_step.CallbackStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.callback_step.CallbackStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.callback_step.CallbackStep") documentation. For a complete
  solution, see [Extend SageMaker Pipelines to include custom steps using callback steps](https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/ "https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/").

###### Important

`Callback` steps were introduced in Amazon SageMaker Python SDK v2.45.0 and
Amazon SageMaker Studio Classic v3.6.2. You must update Studio Classic before you use a `Callback`
step or the pipeline DAG doesn't display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md").

The following sample shows an implementation of the preceding procedure.

```
from sagemaker.workflow.callback_step import CallbackStep

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

###### Note

Output parameters for `CallbackStep` should not be nested. For example, if
you use a nested dictionary as your output parameter, then the dictionary is treated as a
single string (ex. `{"output1": "{\"nested_output1\":\"my-output\"}"}`). If you
provide a nested value, then when you try to refer to a particular output parameter, SageMaker AI
throws a non-retryable client error.

**Stopping behavior**

A pipeline process doesn't stop while a `Callback` step is running.

When you call [StopPipelineExecution](../APIReference/API_StopPipelineExecution.md "../APIReference/API_StopPipelineExecution.md") on a pipeline process with a running `Callback`
step, Pipelines sends an Amazon SQS message to the SQS queue. The body of the SQS message contains a
**Status** field, which is set to `Stopping`. The following
shows an example SQS message body.

```
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

You should add logic to your Amazon SQS message consumer to take any needed action (for
example, resource cleanup) upon receipt of the message. Then add a call to
`SendPipelineExecutionStepSuccess` or
`SendPipelineExecutionStepFailure`.

Only when Pipelines receives one of these calls does it stop the pipeline process.

You use a Lambda step to run an AWS Lambda function. You can run an existing Lambda
function, or SageMaker AI can create and run a new Lambda function. If you choose to use an
existing Lambda function, it must be in the same AWS Region as the SageMaker AI pipeline. For a
notebook that shows how to use a Lambda step in a SageMaker AI pipeline, see [sagemaker-pipelines-lambda-step.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/lambda-step/sagemaker-pipelines-lambda-step.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/lambda-step/sagemaker-pipelines-lambda-step.ipynb").

###### Important

Lambda steps were introduced in Amazon SageMaker Python SDK v2.51.0 and Amazon SageMaker Studio Classic v3.9.1.
You must update Studio Classic before you use a Lambda step or the pipeline DAG doesn't
display. To update Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md "studio-tasks-update-studio.md").

SageMaker AI provides the [sagemaker.lambda_helper.Lambda](https://sagemaker.readthedocs.io/en/stable/api/utility/lambda_helper.html "https://sagemaker.readthedocs.io/en/stable/api/utility/lambda_helper.html") class to create, update, invoke, and delete Lambda
functions. `Lambda` has the following signature.

```
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

The [sagemaker.workflow.lambda_step.LambdaStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.lambda_step.LambdaStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.lambda_step.LambdaStep") class has a `lambda_func`
argument of type `Lambda`. To invoke an existing Lambda function, the only
requirement is to supply the Amazon Resource Name (ARN) of the function to
`function_arn`. If you don't supply a value for `function_arn`, you
must specify `handler` and one of the following:

- `zipped_code_dir` – The path of the zipped Lambda function

`s3_bucket` – Amazon S3 bucket where `zipped_code_dir` is to
be uploaded

- `script` – The path of the Lambda function script file
  The following example shows how to create a `Lambda` step definition that
  invokes an existing Lambda function.

```
from sagemaker.workflow.lambda_step import LambdaStep
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

The following example shows how to create a `Lambda` step definition that
creates and invokes a Lambda function using a Lambda function script.

```
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

If your `Lambda` function has inputs or outputs, these must also be defined
in your `Lambda` step.

###### Note

Input and output parameters should not be nested. For example, if you use a nested
dictionary as your output parameter, then the dictionary is treated as a single string
(ex. `{"output1": "{\"nested_output1\":\"my-output\"}"}`). If you provide a
nested value and try to refer to it later, a non-retryable client error is thrown.

When defining the `Lambda` step, `inputs` must be a dictionary of
key-value pairs. Each value of the `inputs` dictionary must be a primitive type
(string, integer, or float). Nested objects are not supported. If left undefined, the
`inputs` value defaults to `None`.

The `outputs` value must be a list of keys. These keys refer to a dictionary
defined in the output of the `Lambda` function. Like `inputs`, these
keys must be primitive types, and nested objects are not supported.

**Timeout and stopping behavior**

The `Lambda` class has a `timeout` argument that specifies the
maximum time that the Lambda function can run. The default value is 120 seconds with a
maximum value of 10 minutes. If the Lambda function is running when the timeout is met, the
Lambda step fails; however, the Lambda function continues to run.

A pipeline process can't be stopped while a Lambda step is running because the Lambda
function invoked by the Lambda step can't be stopped. If you stop the process while the Lambda
function is running, the pipeline waits for the function to finish or until the timeout is
hit. This depends on whichever occurs first. The process then stops. If the Lambda function
finishes, the pipeline process status is `Stopped`. If the timeout is hit the
pipeline process status is `Failed`.

You can use the `ClarifyCheck` step to conduct baseline drift checks against
previous baselines for bias analysis and model explainability. You can then generate and
[register your baselines](pipelines-quality-clarify-baseline-lifecycle.md#pipelines-quality-clarify-baseline-calculations "pipelines-quality-clarify-baseline-lifecycle.md#pipelines-quality-clarify-baseline-calculations") with the `model.register()` method and pass
the output of that method to [Model step](#step-type-model "#step-type-model") using `step_args`. These baselines for drift check can be used by Amazon SageMaker Model Monitor for your
model endpoints. As a result, you don’t need to do a [baseline](model-monitor-create-baseline.md "model-monitor-create-baseline.md") suggestion
separately.

The `ClarifyCheck` step can also pull baselines for drift check from the
model registry. The `ClarifyCheck` step uses the SageMaker Clarify prebuilt container.
This container provides a range of model monitoring capabilities, including constraint
suggestion and constraint validation against a given baseline. For more information, see
[Prebuilt SageMaker Clarify
Containers](clarify-processing-job-configure-container.md "clarify-processing-job-configure-container.md").

### Configuring the ClarifyCheck step

You can configure the `ClarifyCheck` step to conduct only one of the
following check types each time it’s used in a pipeline.

- Data bias check
- Model bias check
- Model explainability check

To do this, set the `clarify_check_config` parameter with one of the
following check type values:

- `DataBiasCheckConfig`
- `ModelBiasCheckConfig`
- `ModelExplainabilityCheckConfig`

The `ClarifyCheck` step launches a processing job that runs the SageMaker AI
Clarify prebuilt container and requires dedicated [configurations for the
check and the processing job](clarify-configure-processing-jobs.md "clarify-configure-processing-jobs.md"). `ClarifyCheckConfig` and
`CheckJobConfig` are helper functions for these configurations. These helper
functions are aligned with how the SageMaker Clarify processing job computes for checking model
bias, data bias, or model explainability. For more information, see [Run SageMaker Clarify Processing Jobs for Bias Analysis and
Explainability](clarify-processing-job-run.md "clarify-processing-job-run.md").

### Controlling step behaviors for drift

check

The `ClarifyCheck` step requires the following two boolean flags to control
its behavior:

- `skip_check`: This parameter indicates if the drift check against the
  previous baseline is skipped or not. If it is set to `False`, the previous
  baseline of the configured check type must be available.
- `register_new_baseline`: This parameter indicates if a newly calculated
  baseline can be accessed though step property
  `BaselineUsedForDriftCheckConstraints`. If it is set to
  `False`, the previous baseline of the configured check type also must be
  available. This can be accessed through the
  `BaselineUsedForDriftCheckConstraints` property.

For more information, see [Baseline calculation, drift
detection and lifecycle with ClarifyCheck and QualityCheck steps in Amazon SageMaker Pipelines](pipelines-quality-clarify-baseline-lifecycle.md "pipelines-quality-clarify-baseline-lifecycle.md").

### Working with baselines

You can optionally specify the `model_package_group_name` to locate the
existing baseline. Then, the `ClarifyCheck` step pulls the
`DriftCheckBaselines` on the latest approved model package in the model
package group.

Or, you can provide a previous baseline through the
`supplied_baseline_constraints` parameter. If you specify both the
`model_package_group_name` and the
`supplied_baseline_constraints`, the `ClarifyCheck` step uses the
baseline specified by the `supplied_baseline_constraints` parameter.

For more information on using the `ClarifyCheck` step requirements, see the
[sagemaker.workflow.steps.ClarifyCheckStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.clarify_check_step.ClarifyCheckStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.clarify_check_step.ClarifyCheckStep") in the _Amazon SageMaker AI SageMaker AI
SDK for Python_. For an Amazon SageMaker Studio Classic notebook that shows how to use
`ClarifyCheck` step in Pipelines, see [sagemaker-pipeline-model-monitor-clarify-steps.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb").

###### Example Create a `ClarifyCheck` step for data bias check

```
from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.workflow.clarify_check_step import DataBiasCheckConfig, ClarifyCheckStep
from sagemaker.workflow.execution_variables import ExecutionVariables

check_job_config = CheckJobConfig(
    role=role,
    instance_count=1,
    instance_type="`ml.c5.xlarge`",
    volume_size_in_gb=`120`,
    sagemaker_session=sagemaker_session,
)

data_bias_data_config = DataConfig(
    s3_data_input_path=step_process.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri,
    s3_output_path=Join(on='/', values=['s3:/', your_bucket, base_job_prefix, ExecutionVariables.PIPELINE_EXECUTION_ID, '`databiascheckstep`']),
    label=0,
    dataset_type="`text/csv`",
    s3_analysis_config_output_path=data_bias_analysis_cfg_output_path,
)

data_bias_config = BiasConfig(
    label_values_or_threshold=[`15.0`], facet_name=[`8`], facet_values_or_threshold=[[`0.5`]]
)

data_bias_check_config = DataBiasCheckConfig(
    data_config=data_bias_data_config,
    data_bias_config=data_bias_config,
)h

data_bias_check_step = ClarifyCheckStep(
    name="`DataBiasCheckStep`",
    clarify_check_config=data_bias_check_config,
    check_job_config=check_job_config,
    skip_check=False,
    register_new_baseline=False
   supplied_baseline_constraints="`s3://sagemaker-us-west-2-111122223333/baseline/analysis.json`",
    model_package_group_name="`MyModelPackageGroup`"
)
```

Use the `QualityCheck` step to conduct [baseline suggestions](model-monitor-create-baseline.md "model-monitor-create-baseline.md")
and drift checks against a previous baseline for data quality or model quality in a
pipeline. You can then generate and [register your baselines](pipelines-quality-clarify-baseline-lifecycle.md#pipelines-quality-clarify-baseline-calculations "pipelines-quality-clarify-baseline-lifecycle.md#pipelines-quality-clarify-baseline-calculations") with the `model.register()` method and pass
the output of that method to [Model step](#step-type-model "#step-type-model") using `step_args`. ]

Model Monitor can use these baselines for drift check for your model endpoints so that you don’t
need to do a baseline suggestion separately. The `QualityCheck` step can also
pull baselines for drift check from the model registry. The `QualityCheck` step
leverages the Amazon SageMaker AI Model Monitor prebuilt container. This container has a range of model
monitoring capabilities including constraint suggestion, statistics generation, and
constraint validation against a baseline. For more information, see [Amazon SageMaker Model Monitor prebuilt container](model-monitor-pre-built-container.md "model-monitor-pre-built-container.md").

### Configuring the QualityCheck step

You can configure the `QualityCheck` step to run only one of the following
check types each time it’s used in a pipeline.

- Data quality check
- Model quality check

You do this by setting the `quality_check_config` parameter with one of the
following check type values:

- `DataQualityCheckConfig`
- `ModelQualityCheckConfig`

The `QualityCheck` step launches a processing job that runs the Model Monitor
prebuilt container and requires dedicated configurations for the check and the processing
job. The `QualityCheckConfig` and `CheckJobConfig` are helper
functions for these configurations. These helper functions are aligned with how Model Monitor
creates a baseline for the model quality or data quality monitoring. For more information
on the Model Monitor baseline suggestions, see [Create a Baseline](model-monitor-create-baseline.md "model-monitor-create-baseline.md") and [Create a model quality
baseline](model-monitor-model-quality-baseline.md "model-monitor-model-quality-baseline.md").

### Controlling step behaviors for drift

check

The `QualityCheck` step requires the following two Boolean flags to control
its behavior:

- `skip_check`: This parameter indicates if the drift check against the
  previous baseline is skipped or not. If it is set to `False`, the previous
  baseline of the configured check type must be available.
- `register_new_baseline`: This parameter indicates if a newly calculated
  baseline can be accessed through step properties
  `BaselineUsedForDriftCheckConstraints` and
  `BaselineUsedForDriftCheckStatistics`. If it is set to
  `False`, the previous baseline of the configured check type must also be
  available. These can be accessed through the
  `BaselineUsedForDriftCheckConstraints` and
  `BaselineUsedForDriftCheckStatistics` properties.

For more information, see [Baseline calculation, drift
detection and lifecycle with ClarifyCheck and QualityCheck steps in Amazon SageMaker Pipelines](pipelines-quality-clarify-baseline-lifecycle.md "pipelines-quality-clarify-baseline-lifecycle.md").

### Working with baselines

You can specify a previous baseline directly through the
`supplied_baseline_statistics` and `supplied_baseline_constraints`
parameters. You can also specify the `model_package_group_name` and the
`QualityCheck` step pulls the `DriftCheckBaselines` on the latest
approved model package in the model package group.

When you specify the following, the `QualityCheck` step uses the baseline
specified by `supplied_baseline_constraints` and
`supplied_baseline_statistics` on the check type of the
`QualityCheck` step.

- `model_package_group_name`
- `supplied_baseline_constraints`
- `supplied_baseline_statistics`

For more information on using the `QualityCheck` step requirements, see the
[sagemaker.workflow.steps.QualityCheckStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.quality_check_step.QualityCheckStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.quality_check_step.QualityCheckStep") in the _Amazon SageMaker AI SageMaker AI
SDK for Python_. For an Amazon SageMaker Studio Classic notebook that shows how to use
`QualityCheck` step in Pipelines, see [sagemaker-pipeline-model-monitor-clarify-steps.ipynb](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb").

###### Example Create a `QualityCheck` step for data quality check

```
from sagemaker.workflow.check_job_config import CheckJobConfig
from sagemaker.workflow.quality_check_step import DataQualityCheckConfig, QualityCheckStep
from sagemaker.workflow.execution_variables import ExecutionVariables

check_job_config = CheckJobConfig(
    role=role,
    instance_count=1,
    instance_type="`ml.c5.xlarge`",
    volume_size_in_gb=`120`,
    sagemaker_session=sagemaker_session,
)

data_quality_check_config = DataQualityCheckConfig(
    baseline_dataset=step_process.properties.ProcessingOutputConfig.Outputs["`train`"].S3Output.S3Uri,
    dataset_format=DatasetFormat.csv(header=False, output_columns_position="START"),
    output_s3_uri=Join(on='/', values=['s3:/', your_bucket, base_job_prefix, ExecutionVariables.PIPELINE_EXECUTION_ID, 'dataqualitycheckstep'])
)

data_quality_check_step = QualityCheckStep(
    name="DataQualityCheckStep",
    skip_check=False,
    register_new_baseline=False,
    quality_check_config=data_quality_check_config,
    check_job_config=check_job_config,
    supplied_baseline_statistics="s3://`sagemaker-us-west-2-555555555555/baseline/statistics.json`",
    supplied_baseline_constraints="s3://`sagemaker-us-west-2-555555555555/baseline/constraints.json`",
    model_package_group_name="`MyModelPackageGroup`"
)
```

Use the Amazon SageMaker Pipelines [EMR](../../../emr/latest/ManagementGuide/emr-overview.md "../../../emr/latest/ManagementGuide/emr-overview.md") step to:

- Process [Amazon EMR steps](../../../emr/latest/ManagementGuide/emr-work-with-steps.md "../../../emr/latest/ManagementGuide/emr-work-with-steps.md") on a
  running Amazon EMR cluster.
- Have the pipeline create and manage an Amazon EMR cluster for you.
  For more information about Amazon EMR, see [Getting started with Amazon EMR](../../../emr/latest/ManagementGuide/emr-gs.md "../../../emr/latest/ManagementGuide/emr-gs.md").

The EMR step requires that `EMRStepConfig` include the location of the JAR
file used by the Amazon EMR cluster and any arguments to be passed. You also provide the Amazon EMR
cluster ID if you want to run the step on a running EMR cluster. You can also pass the
cluster configuration to run the EMR step on a cluster that it creates, manages, and
terminates for you. The following sections include examples and links to sample notebooks
demonstrating both methods.

###### Note

- EMR steps require that the role passed to your pipeline has additional
  permissions. Attach the [AWS managed policy: `AmazonSageMakerPipelinesIntegrations`](security-iam-awsmanpol-pipelines.md#security-iam-awsmanpol-AmazonSageMakerPipelinesIntegrations "security-iam-awsmanpol-pipelines.md#security-iam-awsmanpol-AmazonSageMakerPipelinesIntegrations") to
  your pipeline role, or ensure that the role includes the permissions in that
  policy.
- If you process an EMR step on a running cluster, you can only use a cluster that
  is in one of the following states:
  - `STARTING`
  - `BOOTSTRAPPING`
  - `RUNNING`
  - `WAITING`

- If you process EMR steps on a running cluster, you can have at most 256 EMR steps
  in a `PENDING` state on an EMR cluster. EMR steps submitted beyond this
  limit result in pipeline execution failure. You may consider using [Retry Policy for Pipeline Steps](pipelines-retry-policy.md "pipelines-retry-policy.md").
- You can specify either cluster ID or cluster configuration, but not both.
- The EMR step relies on Amazon EventBridge to monitor changes in the EMR step or cluster
  state. If you process your Amazon EMR job on a running cluster, the EMR step uses the
  `SageMakerPipelineExecutionEMRStepStatusUpdateRule` rule to monitor EMR
  step state. If you process your job on a cluster that the EMR step creates, the step
  uses the `SageMakerPipelineExecutionEMRClusterStatusRule` rule to monitor
  changes in cluster state. If you see either of these EventBridge rules in your AWS account,
  do not delete them or else your EMR step may not complete.
  **Add an Amazon EMR step to your pipeline**

To add an EMR step to your pipeline, do the following:

- Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
- In the left navigation pane, select **Pipelines**.
- Choose **Create**.
- Choose **Blank**.
- In the left sidebar, choose **Process data** and drag it to the canvas.
- In the canvas, choose the **Process data** step you added.
- In the right sidebar, under mode, choose **EMR (managed)**.
- In the right sidebar, complete the forms in the **Setting and
  Details** tabs. For information about the fields in these tabs, see [sagemaker.workflow.fail_step.EMRstep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.emr_step.EMRStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.emr_step.EMRStep").
  **Launch a new job on a running Amazon EMR cluster**

To launch a new job on a running Amazon EMR cluster, pass the cluster ID as a string to the
`cluster_id` argument of `EMRStep`. The following example
demonstrates this procedure.

```
from sagemaker.workflow.emr_step import EMRStep, EMRStepConfig

emr_config = EMRStepConfig(
    jar="`jar-location`", # required, path to jar file used
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

For a sample notebook that guides you through a complete example, see [Pipelines EMR Step With Running EMR Cluster](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-running-emr-cluster.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-running-emr-cluster.ipynb").

**Launch a new job on a new Amazon EMR cluster**

To launch a new job on a new cluster that `EMRStep` creates for you, provide
your cluster configuration as a dictionary. The dictionary must have the same structure as a
[RunJobFlow](../../../emr/latest/APIReference/API_RunJobFlow.md "../../../emr/latest/APIReference/API_RunJobFlow.md") request. However, do not include the following fields in your cluster
configuration:

- [`Name`]
- [`Steps`]
- [`AutoTerminationPolicy`]
- [`Instances`][`KeepJobFlowAliveWhenNoSteps`]
- [`Instances`][`TerminationProtected`]
  All other `RunJobFlow` arguments are available for use in your cluster
  configuration. For details about the request syntax, see [RunJobFlow](../../../emr/latest/APIReference/API_RunJobFlow.md "../../../emr/latest/APIReference/API_RunJobFlow.md").

The following example passes a cluster configuration to an EMR step definition. This
prompts the step to launch a new job on a new EMR cluster. The EMR cluster configuration in
this example includes specifications for primary and core EMR cluster nodes. For more
information about Amazon EMR node types, see [Understand node types:
primary, core, and task nodes](../../../emr/latest/ManagementGuide/emr-master-core-task-nodes.md "../../../emr/latest/ManagementGuide/emr-master-core-task-nodes.md").

```
from sagemaker.workflow.emr_step import EMRStep, EMRStepConfig

emr_step_config = EMRStepConfig(
    jar="`jar-location`", # required, path to jar file used
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
    "JobFlowRole": "`job-flow-role`",
    "ServiceRole": "`service-role`"
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

For a sample notebook that guides you through a complete example, see [Pipelines EMR Step With Cluster Lifecycle Management](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-cluster-lifecycle-management.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/emr-step/sagemaker-pipelines-emr-step-with-cluster-lifecycle-management.ipynb").

To add an EMR serverless step to your pipeline, do the following:

- Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
- In the left navigation pane, select **Pipelines**.
- Choose **Create**.
- Choose **Blank**.
- In the left sidebar, choose **Process data** and drag it to the canvas.
- In the canvas, choose the **Process data** step you added.
- In the right sidebar, under mode, choose **EMR (serverless)**.
- In the right sidebar, complete the forms in the **Setting and
  Details** tabs.
  Use a `NotebookJobStep` to run your SageMaker Notebook Job non-interactively as a
  pipeline step. If you build your pipeline in the Pipelines drag-and-drop UI, use the [Execute code step](#step-type-executecode "#step-type-executecode") to run your
  notebook. For more information about SageMaker Notebook Jobs, see [SageMaker Notebook Jobs](notebook-auto-run.md "notebook-auto-run.md").

A `NotebookJobStep` requires at minimum an input notebook, image URI and
kernel name. For more information about Notebook Job step requirements and other parameters
you can set to customize your step, see [sagemaker.workflow.steps.NotebookJobStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.notebook_job_step.NotebookJobStep").

The following example uses minimum arguments to define a
`NotebookJobStep`.

```
from sagemaker.workflow.notebook_job_step import NotebookJobStep


notebook_job_step = NotebookJobStep(
    input_notebook=`input_notebook`,
    image_uri=`image_uri`,
    kernel_name=`kernel_name`
)
```

Your `NotebookJobStep` pipeline step is treated as a SageMaker notebook job. As a
result, track the execution status in the Studio Classic UI notebook job dashboard by including
specific tags with the `tags` argument. For more details about tags to include,
see [View your notebook jobs in the Studio
UI dashboard](create-notebook-auto-run-sdk.md#create-notebook-auto-run-dash "create-notebook-auto-run-sdk.md#create-notebook-auto-run-dash").

Also, if you schedule your notebook job using the SageMaker Python SDK, you can only specify
certain images to run your notebook job. For more information, see [Image constraints for SageMaker AI
Python SDK notebook jobs](notebook-auto-run-constraints.md#notebook-auto-run-constraints-image-sdk "notebook-auto-run-constraints.md#notebook-auto-run-constraints-image-sdk").

Use a Fail step to stop an Amazon SageMaker Pipelines execution when a desired condition or state is not
achieved. The Fail step also allows you to enter a custom error message, indicating the
cause of the pipeline's execution failure.

###### Note

When a Fail step and other pipeline steps execute at the same time, the pipeline does
not terminate until all concurrent steps are completed.

### Limitations for using Fail step

- You cannot add a Fail step to the `DependsOn` list of other steps. For
  more information, see [Custom dependency between steps](build-and-manage-steps.md#build-and-manage-custom-dependency "build-and-manage-steps.md#build-and-manage-custom-dependency").
- Other steps cannot reference the Fail step. It is _always_ the
  last step in a pipeline's execution.
- You cannot retry a pipeline execution ending with a Fail step.

You can create the Fail step error message in the form of a static text string.
Alternatively, you can also use [Pipeline Parameters](build-and-manage-parameters.md "build-and-manage-parameters.md"), a
[Join](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html?highlight=Join#sagemaker.workflow.functions.Join "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html?highlight=Join#sagemaker.workflow.functions.Join") operation, or other [step
properties](build-and-manage-steps.md#build-and-manage-properties "build-and-manage-steps.md#build-and-manage-properties") to create a more informative error message if you use the SDK.

Pipeline Designer
To add a Fail step to your pipeline, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Fail** and drag it to the
   canvas.
6. In the canvas, choose the **Fail** step you added.
7. In the right sidebar, complete the forms in the **Setting**
   and **Details** tabs. For information about the fields in these
   tabs, see [sagemaker.workflow.fail_step.FailStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.fail_step.FailStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.fail_step.FailStep").
8. If the canvas includes any step that immediately precedes the
   **Fail** step you added, click and drag the cursor from the
   step to the **Fail** step to create an edge.
9. If the canvas includes any step that immediately succeeds the
   **Fail** step you added, click and drag the cursor from the
   **Fail** step to the step to create an edge.

SageMaker Python SDK

###### Example

The following example code snippet uses a `FailStep` with an
`ErrorMessage` configured with Pipeline Parameters and a
`Join` operation.

```
from sagemaker.workflow.fail_step import FailStep
from sagemaker.workflow.functions import Join
from sagemaker.workflow.parameters import ParameterInteger

mse_threshold_param = ParameterInteger(name="MseThreshold", default_value=5)
step_fail = FailStep(
    name="`AbaloneMSEFail`",
    error_message=Join(
        on=" ", values=["`Execution failed due to MSE >`", mse_threshold_param]
    ),
)

```
