# Define a pipeline

To orchestrate your workflows with Amazon SageMaker Pipelines, you must generate a directed acyclic graph (DAG) in the
form of a JSON pipeline definition. The DAG specifies the different steps involved in your ML process,
such as data preprocessing, model training, model evaluation, and model deployment, as well as the
dependencies and flow of data between these steps. The following topic shows you how to generate a
pipeline definition.

You can generate your JSON pipeline definition using either the SageMaker Python SDK or the visual drag-and-drop
Pipeline Designer feature in Amazon SageMaker Studio. The following image is a representation of the pipeline DAG
that you create in this tutorial:

![Screenshot of the visual drag-and-drop interface for Pipelines in Studio.](images/pipelines/pipelines-studio-overview.png)
The pipeline that you define in the following sections solves a regression
problem to determine the age of an abalone based on its physical measurements. For a runnable
Jupyter notebook that includes the content in this tutorial, see [Orchestrating Jobs with Amazon SageMaker Model Building Pipelines](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-pipelines/tabular/abalone_build_train_deploy/sagemaker-pipelines-preprocess-train-evaluate-batch-transform.html").

###### Note

You can reference the model location as a property of the training step, as shown in the
end-to-end example [CustomerChurn pipeline](https://github.com/aws-samples/customer-churn-sagemaker-pipelines-sample/blob/main/pipelines/customerchurn/pipeline.py "https://github.com/aws-samples/customer-churn-sagemaker-pipelines-sample/blob/main/pipelines/customerchurn/pipeline.py") in Github.

###### Topics

The following walkthrough guides you through the steps to create a barebones pipeline
using the drag-and-drop Pipeline Designer. If you need to pause or end your Pipeline editing session in
the visual designer at any time, click on the **Export** option. This
allows you to download the current definition of your Pipeline to your local environment.
Later, when you want to resume the Pipeline editing process, you can import the same JSON
definition file into the visual designer.

### Create a Processing step

To create a data processing job step, do the following:

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, select **Pipelines**.
3. Choose **Create**.
4. Choose **Blank**.
5. In the left sidebar, choose **Process data** and drag it to the
   canvas.
6. In the canvas, choose the **Process data** step you added.
7. To add an input dataset, choose **Add** under **Data
   (input)** in the right sidebar and select a dataset.
8. To add a location to save output datasets, choose **Add** under
   **Data (output)** in the right sidebar and navigate to the
   destination.
9. Complete the remaining fields in the right sidebar. For information about the
   fields in these tabs, see
   [sagemaker.workflow.steps.ProcessingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.ProcessingStep").

### Create a Training step

To set up a model training step, do the following:

1. In the left sidebar, choose **Train model** and drag it to the
   canvas.
2. In the canvas, choose the **Train model** step you added.
3. To add an input dataset, choose **Add** under **Data
   (input)** in the right sidebar and select a dataset.
4. To choose a location to save your model artifacts, enter an Amazon S3 URI in the
   **Location (S3 URI)** field, or choose **Browse
   S3** to navigate to the destination location.
5. Complete the remaining fields in the right sidebar. For information about the
   fields in these tabs, see [sagemaker.workflow.steps.TrainingStep](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.steps.TrainingStep").
6. Click and drag the cursor from the **Process data** step you
   added in the previous section to the **Train model** step to create
   an edge connecting the two steps.

### Create a model package with a Register model

step

To create a model package with a model registration step, do the following:

1. In the left sidebar, choose **Register model** and drag it to the
   canvas.
2. In the canvas, choose the **Register model** step you
   added.
3. To select a model to register, choose **Add** under
   **Model (input)**.
4. Choose **Create a model group** to add your model to a new model
   group.
5. Complete the remaining fields in the right sidebar. For information about the
   fields in these tabs, see [sagemaker.workflow.step_collections.RegisterModel](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_collections.RegisterModel").
6. Click and drag the cursor from the **Train model** step you added
   in the previous section to the **Register model** step to create an
   edge connecting the two steps.

### Deploy the model to an endpoint with a Deploy

model (endpoint) step

To deploy your model using a model deployment step, do the following:

1. In the left sidebar, choose **Deploy model (endpoint)** and drag
   it to the canvas.
2. In the canvas, choose the **Deploy model (endpoint)** step you
   added.
3. To choose a model to deploy, choose **Add** under **Model
   (input)**.
4. Choose the **Create endpoint** radio button to create a new
   endpoint.
5. Enter a **Name** and **Description** for your
   endpoint.
6. Click and drag the cursor from the **Register model** step you
   added in the previous section to the **Deploy model (endpoint)** step
   to create an edge connecting the two steps.
7. Complete the remaining fields in the right sidebar.

### Define the Pipeline parameters

You can configure a set of Pipeline parameters whose values can be updated for every
execution. To define the pipeline parameters and set the default values, click on the gear
icon at the bottom of the visual designer.

### Save Pipeline

After you have entered all the required information to create your pipeline, click on
**Save** at the bottom of the visual designer. This validates your
pipeline for any potential errors at runtime and notifies you. The **Save**
operation won't succeed until you address all errors flagged by the automated validations
checks. If you want to resume editing at a later point, you can save your in-progress
pipeline as a JSON definition in your local environment. You can export your Pipeline as a
JSON definition file by clicking on the **Export** button at the bottom
of the visual designer. Later, to resume updating your Pipeline, upload that JSON
definition file by clicking on the **Import** button.

### Prerequisites

To run the following tutorial, complete the following:

- Set up your notebook instance as outlined in [Create a notebook instance](howitworks-create-ws.md "howitworks-create-ws.md"). This gives your role permissions to read and
  write to Amazon S3, and create training, batch transform, and processing jobs in SageMaker AI.
- Grant your notebook permissions to get and pass its own role as shown in [Modifying a role permissions policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy"). Add the following JSON snippet to
  attach this policy to your role. Replace `<your-role-arn>` with the
  ARN used to create your notebook instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`"
 }
 ]
}`

```

- Trust the SageMaker AI service principal by following the steps in [Modifying a role trust policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-managingrole_edit-trust-policy-cli "../../../IAM/latest/UserGuide/roles-managingrole-editing-cli.md#roles-managingrole_edit-trust-policy-cli"). Add the following statement fragment to the
  trust relationship of your role:

```
{
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
```

#### Set up your environment

Create a new SageMaker AI session using the following code block. This returns the role ARN
for the session. This role ARN should be the execution role ARN that you set up as a
prerequisite.

```
import boto3
import sagemaker
import sagemaker.session
from sagemaker.workflow.pipeline_context import PipelineSession

region = boto3.Session().region_name
sagemaker_session = sagemaker.session.Session()
role = sagemaker.get_execution_role()
default_bucket = sagemaker_session.default_bucket()

pipeline_session = PipelineSession()

model_package_group_name = f"AbaloneModelPackageGroupName"
```

### Create a pipeline

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

Run the following steps from your SageMaker AI notebook instance to create a pipeline that
includes steps for:

- preprocessing
- training
- evaluation
- conditional evaluation
- model registration

###### Note

You can use [ExecutionVariables](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#execution-variables "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#execution-variables") and the [Join](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#execution-variables "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#execution-variables") function to specify your output location.
`ExecutionVariables` is resolved at runtime. For instance,
`ExecutionVariables.PIPELINE_EXECUTION_ID` is resolved to the ID of the
current execution, which can be used as a unique identifier across different
runs.

#### Step 1: Download the dataset

This notebook uses the UCI Machine Learning Abalone Dataset. The dataset contains
the following features:

- `length` – The longest shell measurement of the
  abalone.
- `diameter` – The diameter of the abalone perpendicular to its
  length.
- `height` – The height of the abalone with meat in the
  shell.
- `whole_weight` – The weight of the whole abalone.
- `shucked_weight` – The weight of the meat removed from the
  abalone.
- `viscera_weight` – The weight of the abalone viscera after
  bleeding.
- `shell_weight` – The weight of the abalone shell after meat
  removal and drying.
- `sex` – The sex of the abalone. One of 'M', 'F', or 'I', where
  'I' is an infant abalone.
- `rings` – The number of rings in the abalone shell.

The number of rings in the abalone shell is a good approximation for its age using
the formula `age=rings + 1.5`. However, getting this number is a
time-consuming task. You must cut the shell through the cone, stain the section, and
count the number of rings through a microscope. However, the other physical measurements
are easier to get. This notebook uses the dataset to build a predictive model of the
variable rings using the other physical measurements.

###### To download the dataset

1. Download the dataset into your account's default Amazon S3 bucket.

```
!mkdir -p data
local_path = "data/abalone-dataset.csv"

s3 = boto3.resource("s3")
s3.Bucket(f"sagemaker-servicecatalog-seedcode-{region}").download_file(
    "dataset/abalone-dataset.csv",
    local_path
)

base_uri = f"s3://{default_bucket}/abalone"
input_data_uri = sagemaker.s3.S3Uploader.upload(
    local_path=local_path,
    desired_s3_uri=base_uri,
)
print(input_data_uri)
```

2. Download a second dataset for batch transformation after your model is
   created.

```
local_path = "data/abalone-dataset-batch.csv"

s3 = boto3.resource("s3")
s3.Bucket(f"sagemaker-servicecatalog-seedcode-{region}").download_file(
    "dataset/abalone-dataset-batch",
    local_path
)

base_uri = f"s3://{default_bucket}/abalone"
batch_data_uri = sagemaker.s3.S3Uploader.upload(
    local_path=local_path,
    desired_s3_uri=base_uri,
)
print(batch_data_uri)
```

#### Step 2: Define pipeline parameters

This code block defines the following parameters for your pipeline:

- `processing_instance_count` – The instance count of the processing
  job.
- `input_data` – The Amazon S3 location of the input data.
- `batch_data` – The Amazon S3 location of the input data for batch
  transformation.
- `model_approval_status` – The approval status to register the
  trained model with for CI/CD. For more information, see [MLOps Automation With SageMaker Projects](sagemaker-projects.md "sagemaker-projects.md").

```
from sagemaker.workflow.parameters import (
    ParameterInteger,
    ParameterString,
)

processing_instance_count = ParameterInteger(
    name="ProcessingInstanceCount",
    default_value=1
)
model_approval_status = ParameterString(
    name="ModelApprovalStatus",
    default_value="PendingManualApproval"
)
input_data = ParameterString(
    name="InputData",
    default_value=input_data_uri,
)
batch_data = ParameterString(
    name="BatchData",
    default_value=batch_data_uri,
)
```

#### Step 3: Define a processing step

for feature engineering

This section shows how to create a processing step to prepare the data from the
dataset for training.

###### To create a processing step

1. Create a directory for the processing script.

```
!mkdir -p abalone
```

2. Create a file in the `/abalone` directory named
   `preprocessing.py` with the following content. This preprocessing
   script is passed in to the processing step for running on the input data. The
   training step then uses the preprocessed training features and labels to train a
   model. The evaluation step uses the trained model and preprocessed test features and
   labels to evaluate the model. The script uses `scikit-learn` to do the
   following:
   - Fill in missing `sex` categorical data and encode it so it's
     suitable for training.
   - Scale and normalize all numerical fields except for `rings` and
     `sex`.
   - Split the data into training, test, and validation datasets.

```
%%writefile abalone/preprocessing.py
import argparse
import os
import requests
import tempfile
import numpy as np
import pandas as pd


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# Because this is a headerless CSV file, specify the column names here.
feature_columns_names = [
    "sex",
    "length",
    "diameter",
    "height",
    "whole_weight",
    "shucked_weight",
    "viscera_weight",
    "shell_weight",
]
label_column = "rings"

feature_columns_dtype = {
    "sex": str,
    "length": np.float64,
    "diameter": np.float64,
    "height": np.float64,
    "whole_weight": np.float64,
    "shucked_weight": np.float64,
    "viscera_weight": np.float64,
    "shell_weight": np.float64
}
label_column_dtype = {"rings": np.float64}


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


if __name__ == "__main__":
    base_dir = "/opt/ml/processing"

    df = pd.read_csv(
        f"{base_dir}/input/abalone-dataset.csv",
        header=None,
        names=feature_columns_names + [label_column],
        dtype=merge_two_dicts(feature_columns_dtype, label_column_dtype)
    )
    numeric_features = list(feature_columns_names)
    numeric_features.remove("sex")
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    categorical_features = ["sex"]
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocess = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    y = df.pop("rings")
    X_pre = preprocess.fit_transform(df)
    y_pre = y.to_numpy().reshape(len(y), 1)

    X = np.concatenate((y_pre, X_pre), axis=1)

    np.random.shuffle(X)
    train, validation, test = np.split(X, [int(.7*len(X)), int(.85*len(X))])


    pd.DataFrame(train).to_csv(f"{base_dir}/train/train.csv", header=False, index=False)
    pd.DataFrame(validation).to_csv(f"{base_dir}/validation/validation.csv", header=False, index=False)
    pd.DataFrame(test).to_csv(f"{base_dir}/test/test.csv", header=False, index=False)
```

3. Create an instance of an `SKLearnProcessor` to pass in to the
   processing step.

```
from sagemaker.sklearn.processing import SKLearnProcessor


framework_version = "0.23-1"

sklearn_processor = SKLearnProcessor(
    framework_version=framework_version,
    instance_type="ml.m5.xlarge",
    instance_count=processing_instance_count,
    base_job_name="sklearn-abalone-process",
    sagemaker_session=pipeline_session,
    role=role,
)
```

4. Create a processing step. This step takes in the `SKLearnProcessor`,
   the input and output channels, and the `preprocessing.py` script that you
   created. This is very similar to a processor instance's `run` method in
   the SageMaker AI Python SDK. The `input_data` parameter passed into
   `ProcessingStep` is the input data of the step itself. This input data
   is used by the processor instance when it runs.

Note the  `"train`, `"validation`, and
`"test"` named channels specified in the output configuration
for the processing job. Step `Properties` such as these can be used in
subsequent steps and resolve to their runtime values at runtime.

```
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep


processor_args = sklearn_processor.run(
    inputs=[
      ProcessingInput(source=input_data, destination="/opt/ml/processing/input"),
    ],
    outputs=[
        ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
        ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
        ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
    ],
    code="abalone/preprocessing.py",
)

step_process = ProcessingStep(
    name="AbaloneProcess",
    step_args=processor_args
)
```

#### Step 4: Define a training step

This section shows how to use the SageMaker AI [XGBoost
Algorithm](xgboost.md "xgboost.md") to train a model on the training data output from the processing
steps.

###### To define a training step

1. Specify the model path where you want to save the models from training.

```
model_path = f"s3://{default_bucket}/AbaloneTrain"
```

2.  Configure an estimator for the XGBoost algorithm and the input dataset. The
    training instance type is passed into the estimator. A typical training
    script:

        * loads data from the input channels
        * configures training with hyperparameters
        * trains a model
        * saves a model to `model_dir` so that it can be hosted
         later

    SageMaker AI uploads the model to Amazon S3 in the form of a `model.tar.gz` at the
    end of the training job.

```
from sagemaker.estimator import Estimator


image_uri = sagemaker.image_uris.retrieve(
    framework="xgboost",
    region=region,
    version="1.0-1",
    py_version="py3",
    instance_type="ml.m5.xlarge"
)
xgb_train = Estimator(
    image_uri=image_uri,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    output_path=model_path,
    sagemaker_session=pipeline_session,
    role=role,
)
xgb_train.set_hyperparameters(
    objective="reg:linear",
    num_round=50,
    max_depth=5,
    eta=0.2,
    gamma=4,
    min_child_weight=6,
    subsample=0.7,
    silent=0
)
```

3. Create a `TrainingStep` using the estimator instance and properties
   of the `ProcessingStep`. Pass in the `S3Uri` of the
   `"train"` and `"validation"` output
   channel to the `TrainingStep`. 

```
from sagemaker.inputs import TrainingInput
from sagemaker.workflow.steps import TrainingStep


train_args = xgb_train.fit(
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
    },
)

step_train = TrainingStep(
    name="AbaloneTrain",
    step_args = train_args
)
```

#### Step 5: Define a processing step for

model evaluation

This section shows how to create a processing step to evaluate the accuracy of the
model. The result of this model evaluation is used in the condition step to determine
which run path to take.

###### To define a processing step for model evaluation

1. Create a file in the `/abalone` directory named
   `evaluation.py`. This script is used in a processing step to perform
   model evaluation. It takes a trained model and the test dataset as input, then
   produces a JSON file containing classification evaluation metrics.

```
%%writefile abalone/evaluation.py
import json
import pathlib
import pickle
import tarfile
import joblib
import numpy as np
import pandas as pd
import xgboost


from sklearn.metrics import mean_squared_error


if __name__ == "__main__":
    model_path = f"/opt/ml/processing/model/model.tar.gz"
    with tarfile.open(model_path) as tar:
        tar.extractall(path=".")

    model = pickle.load(open("xgboost-model", "rb"))

    test_path = "/opt/ml/processing/test/test.csv"
    df = pd.read_csv(test_path, header=None)

    y_test = df.iloc[:, 0].to_numpy()
    df.drop(df.columns[0], axis=1, inplace=True)

    X_test = xgboost.DMatrix(df.values)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    std = np.std(y_test - predictions)
    report_dict = {
        "regression_metrics": {
            "mse": {
                "value": mse,
                "standard_deviation": std
            },
        },
    }

    output_dir = "/opt/ml/processing/evaluation"
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

    evaluation_path = f"{output_dir}/evaluation.json"
    with open(evaluation_path, "w") as f:
        f.write(json.dumps(report_dict))
```

2. Create an instance of a `ScriptProcessor` that is used to create a
   `ProcessingStep`.

```
from sagemaker.processing import ScriptProcessor


script_eval = ScriptProcessor(
    image_uri=image_uri,
    command=["python3"],
    instance_type="ml.m5.xlarge",
    instance_count=1,
    base_job_name="script-abalone-eval",
    sagemaker_session=pipeline_session,
    role=role,
)
```

3.  Create a `ProcessingStep` using the processor instance, the input
    and output channels, and the  `evaluation.py` script. Pass in:

        * the `S3ModelArtifacts` property from the `step_train`
         training step
        * the `S3Uri` of the `"test"` output channel
         of the `step_process` processing step

    This is very similar to a processor instance's `run` method in the
    SageMaker AI Python SDK. 

```
from sagemaker.workflow.properties import PropertyFile


evaluation_report = PropertyFile(
    name="EvaluationReport",
    output_name="evaluation",
    path="evaluation.json"
)

eval_args = script_eval.run(
        inputs=[
        ProcessingInput(
            source=step_train.properties.ModelArtifacts.S3ModelArtifacts,
            destination="/opt/ml/processing/model"
        ),
        ProcessingInput(
            source=step_process.properties.ProcessingOutputConfig.Outputs[
                "test"
            ].S3Output.S3Uri,
            destination="/opt/ml/processing/test"
        )
    ],
    outputs=[
        ProcessingOutput(output_name="evaluation", source="/opt/ml/processing/evaluation"),
    ],
    code="abalone/evaluation.py",
)

step_eval = ProcessingStep(
    name="AbaloneEval",
    step_args=eval_args,
    property_files=[evaluation_report],
)
```

#### Step 6: Define a CreateModelStep for

batch transformation

###### Important

We recommend using [Model step](build-and-manage-steps-types.md#step-type-model "build-and-manage-steps-types.md#step-type-model") to create models as of v2.90.0 of the SageMaker Python SDK. `CreateModelStep`
will continue to work in previous versions of the SageMaker Python SDK, but is no longer
actively supported.

This section shows how to create a SageMaker AI model from the output of the training step.
This model is used for batch transformation on a new dataset. This step is passed into
the condition step and only runs if the condition step evaluates to
`true`.

###### To define a CreateModelStep for batch transformation

1. Create a SageMaker AI model. Pass in the `S3ModelArtifacts` property from
   the `step_train` training step.

```
from sagemaker.model import Model


model = Model(
    image_uri=image_uri,
    model_data=step_train.properties.ModelArtifacts.S3ModelArtifacts,
    sagemaker_session=pipeline_session,
    role=role,
)
```

2. Define the model input for your SageMaker AI model.

```
from sagemaker.inputs import CreateModelInput


inputs = CreateModelInput(
    instance_type="ml.m5.large",
    accelerator_type="ml.eia1.medium",
)
```

3. Create your `CreateModelStep` using the `CreateModelInput`
   and SageMaker AI model instance you defined.

```
from sagemaker.workflow.steps import CreateModelStep


step_create_model = CreateModelStep(
    name="AbaloneCreateModel",
    model=model,
    inputs=inputs,
)
```

#### Step 7: Define a TransformStep to perform

batch transformation

This section shows how to create a `TransformStep` to perform batch
transformation on a dataset after the model is trained. This step is passed into the
condition step and only runs if the condition step evaluates to
`true`.

###### To define a TransformStep to perform batch transformation

1. Create a transformer instance with the appropriate compute instance type,
   instance count, and desired output Amazon S3 bucket URI. Pass in the
   `ModelName` property from the `step_create_model`
   `CreateModel` step.

```
from sagemaker.transformer import Transformer


transformer = Transformer(
    model_name=step_create_model.properties.ModelName,
    instance_type="ml.m5.xlarge",
    instance_count=1,
    output_path=f"s3://{default_bucket}/AbaloneTransform"
)
```

2. Create a `TransformStep` using the transformer instance you defined
   and the `batch_data` pipeline parameter.

```
from sagemaker.inputs import TransformInput
from sagemaker.workflow.steps import TransformStep


step_transform = TransformStep(
    name="AbaloneTransform",
    transformer=transformer,
    inputs=TransformInput(data=batch_data)
)
```

#### Step 8: Define a RegisterModel step to create

a model package

###### Important

We recommend using [Model step](build-and-manage-steps-types.md#step-type-model "build-and-manage-steps-types.md#step-type-model") to register models as of v2.90.0 of the SageMaker Python SDK. `RegisterModel`
will continue to work in previous versions of the SageMaker Python SDK, but is no longer
actively supported.

This section shows how to create an instance of `RegisterModel`. The
result of running `RegisterModel` in a pipeline is a model package. A model
package is a reusable model artifacts abstraction that packages all ingredients
necessary for inference. It consists of an inference specification that defines the
inference image to use along with an optional model weights location. A model package
group is a collection of model packages. You can use a `ModelPackageGroup`
for Pipelines to add a new version and model package to the group for every pipeline run.
For more information about model registry, see [Model Registration Deployment with Model Registry](model-registry.md "model-registry.md").

This step is passed into the condition step and only runs if the condition step
evaluates to `true`.

###### To define a RegisterModel step to create a model package

- Construct a `RegisterModel` step using the estimator instance you
  used for the training step . Pass in the `S3ModelArtifacts` property from
  the `step_train` training step and specify a
  `ModelPackageGroup`. Pipelines creates this `ModelPackageGroup`
  for you.

```
from sagemaker.model_metrics import MetricsSource, ModelMetrics
from sagemaker.workflow.step_collections import RegisterModel


model_metrics = ModelMetrics(
    model_statistics=MetricsSource(
        s3_uri="`{}/evaluation.json`".format(
            step_eval.arguments["ProcessingOutputConfig"]["Outputs"][0]["S3Output"]["S3Uri"]
        ),
        content_type="application/json"
    )
)
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

#### Step 9: Define a condition step to verify

model accuracy

A `ConditionStep` allows Pipelines to support conditional running in your
pipeline DAG based on the condition of step properties. In this case, you only want to
register a model package if the accuracy of that model exceeds the required value. The
accuracy of the model is determined by the model evaluation step. If the accuracy
exceeds the required value, the pipeline also creates a SageMaker AI Model and runs batch
transformation on a dataset. This section shows how to define the Condition step.

###### To define a condition step to verify model accuracy

1. Define a `ConditionLessThanOrEqualTo` condition using the accuracy
   value found in the output of the model evaluation processing
   step, `step_eval`. Get this output using the property file you indexed
   in the processing step and the respective JSONPath of the mean squared error value,
   `"mse"`.

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
```

2. Construct a `ConditionStep`. Pass the `ConditionEquals`
   condition in, then set the model package registration and batch transformation steps
   as the next steps if the condition passes.

```
step_cond = ConditionStep(
    name="AbaloneMSECond",
    conditions=[cond_lte],
    if_steps=[step_register, step_create_model, step_transform],
    else_steps=[],
)
```

#### Step 10: Create a pipeline

Now that you’ve created all of the steps, combine them into a pipeline.

###### To create a pipeline

1. Define the following for your pipeline: `name`,
   `parameters`, and `steps`. Names must be unique within
   an `(account, region)` pair.

###### Note

A step can only appear once in either the pipeline's step list or the if/else
step lists of the condition step. It cannot appear in both.

```
from sagemaker.workflow.pipeline import Pipeline


pipeline_name = f"AbalonePipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[
        processing_instance_count,
        model_approval_status,
        input_data,
        batch_data,
    ],
    steps=[step_process, step_train, step_eval, step_cond],
)
```

2. (Optional) Examine the JSON pipeline definition to ensure that it's
   well-formed.

```
import json

json.loads(pipeline.definition())
```

This pipeline definition is ready to submit to SageMaker AI. In the next tutorial, you
submit this pipeline to SageMaker AI and start a run.

You can also use [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_pipeline "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_pipeline") or [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.md") to create a pipeline.
Creating a pipeline requires a pipeline definition, which is a JSON object that
defines each step of the pipeline. The SageMaker SDK offers a simple way to construct the pipeline definition,
which you can use with any of the APIs previously mentioned to create the pipeline itself. Without using the SDK,
users have to write the raw JSON definition to create the pipeline without any of the error
checks provided by the SageMaker Python SDK. To see the schema for the pipeline JSON definition, see [SageMaker AI Pipeline Definition JSON Schema](https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/ "https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/"). The following code sample shows an example of a SageMaker AI pipeline
definition JSON object:

```
{'Version': '2020-12-01',
 'Metadata': {},
 'Parameters': [{'Name': 'ProcessingInstanceType',
   'Type': 'String',
   'DefaultValue': 'ml.m5.xlarge'},
  {'Name': 'ProcessingInstanceCount', 'Type': 'Integer', 'DefaultValue': 1},
  {'Name': 'TrainingInstanceType',
   'Type': 'String',
   'DefaultValue': 'ml.m5.xlarge'},
  {'Name': 'ModelApprovalStatus',
   'Type': 'String',
   'DefaultValue': 'PendingManualApproval'},
  {'Name': 'ProcessedData',
   'Type': 'String',
   'DefaultValue': '`S3_URL`',
{'Name': 'InputDataUrl',
   'Type': 'String',
   'DefaultValue': '`S3_URL`',
 'PipelineExperimentConfig': {'ExperimentName': {'Get': 'Execution.PipelineName'},
  'TrialName': {'Get': 'Execution.PipelineExecutionId'}},
 'Steps': [{'Name': 'ReadTrainDataFromFS',
   'Type': 'Processing',
   'Arguments': {'ProcessingResources': {'ClusterConfig': {'InstanceType': 'ml.m5.4xlarge',
      'InstanceCount': 2,
      'VolumeSizeInGB': 30}},
    'AppSpecification': {'ImageUri': '`IMAGE_URI`',
     'ContainerArguments': [....]},
    'RoleArn': '`ROLE`',
      'ProcessingInputs': [...],
    'ProcessingOutputConfig': {'Outputs': [.....]},
    'StoppingCondition': {'MaxRuntimeInSeconds': 86400}},
   'CacheConfig': {'Enabled': True, 'ExpireAfter': '30d'}},
   ...
   ...
   ...
  }
```

**Next step:**
[Run a pipeline](run-pipeline.md "run-pipeline.md")
