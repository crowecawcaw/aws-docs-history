

# Automatically register SageMaker AI models with SageMaker Model Registry
<a name="mlflow-track-experiments-model-registration"></a>

When you register an MLflow model, SageMaker AI automatically creates a corresponding Model Package Group and Model Package version in the SageMaker Model Registry. This enables you to:
+ Register models from the MLflow SDK or the MLflow UI.
+ Attach an inference specification to enable direct deployment to SageMaker AI endpoints.
+ Log evaluation metrics that are included as a model card in the Model Package.
+ Manage model lifecycle stages (staging, production) and statuses (pending, active) through MLflow aliases.
+ Control lifecycle transitions and registration with IAM condition keys and resource tag-based policies.

**Note**  
Model Registry sync is an opt-in feature. To enable it, call the [UpdateMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowTrackingServer.html) or [UpdateMlflowApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowApp.html) API with Model Registry sync enabled.

## Log and register models
<a name="mlflow-track-experiments-model-registration-log-register"></a>

This section covers how to prepare a model for registration, register it with the SageMaker Model Registry, and view it in Studio.

### Required IAM permissions
<a name="mlflow-track-experiments-model-registration-iam"></a>

The MLflow tracking server or MLflow App IAM service role must have the following permissions to register models:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sagemaker:CreateModelPackageGroup",
                "sagemaker:DescribeModelPackageGroup",
                "sagemaker:CreateModelPackage",
                "sagemaker:UpdateModelPackage",
                "sagemaker:AddTags",
                "sagemaker:CreateAction",
                "sagemaker:AddAssociation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about setting up IAM roles for MLflow Apps, see [Set up IAM permissions for MLflow Apps](mlflow-app-setup-prerequisites-iam.md).

### Prepare a model for registration
<a name="mlflow-track-experiments-model-registration-prepare"></a>

Before registering a model, you log it during a training run. You can optionally attach an inference specification and evaluation metrics, which are carried forward to the SageMaker AI Model Package upon registration.

#### Log a model
<a name="mlflow-track-experiments-model-registration-log-model"></a>

Use the MLflow SDK to log a model during a training run:

```
import mlflow
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from mlflow.models import infer_signature

mlflow.set_tracking_uri({{arn}})
mlflow.set_experiment("my-experiment")

params = {"n_estimators": 3, "random_state": 42}
X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)

with mlflow.start_run() as run:
    model = RandomForestRegressor(**params).fit(X, y)
    signature = infer_signature(X, model.predict(X))
    mlflow.log_params(params)
    model_info = mlflow.sklearn.log_model(
        model, name="sklearn-model", signature=signature, input_example=X[:3]
    )
```

#### Log an inference specification (optional)
<a name="mlflow-track-experiments-model-registration-inference-spec"></a>

An inference specification defines the container image and instance types required to deploy your model. When attached to a logged model before registration, the inference specification is automatically included in the SageMaker AI Model Package. This enables direct deployment to a SageMaker AI endpoint from the Model Registry without additional configuration.

Use `sagemaker_mlflow.log_inference_specification()` to attach an inference specification:

```
import sagemaker_mlflow

# Get the logged model's artifact location
logged_model = mlflow.MlflowClient().get_logged_model(model_info.model_id)

inference_spec = {
    "Containers": [{
        "Image": "{{763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:2.0.0-cpu-py310}}",
        "ModelDataSource": {
            "S3DataSource": {
                "S3Uri": logged_model.artifact_location + "/",
                "S3DataType": "S3Prefix",
                "CompressionType": "None",
            }
        },
    }],
    "SupportedRealtimeInferenceInstanceTypes": ["ml.m5.xlarge"],
}
sagemaker_mlflow.log_inference_specification(
    model_info.model_id,
    inference_specification=inference_spec
)
```

**Note**  
The inference specification must follow the same schema as the `InferenceSpecification` parameter of the SageMaker AI `CreateModelPackage` API. For more information, see [InferenceSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceSpecification.html) in the SageMaker AI API Reference.

After logging, the inference specification is stored as a `sagemaker_inference_specification.json` artifact alongside your model:

![Inference specification artifact in the MLflow UI.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-ui-inference-spec.png)


#### Log evaluation metrics (optional)
<a name="mlflow-track-experiments-model-registration-evaluation"></a>

Evaluation metrics provide a standardized summary of your model's performance. When logged before registration, evaluation results are included in the SageMaker AI Model Package as a model card, making metrics visible in the SageMaker AI Model Registry and Studio. For more information about model cards, see [Model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema).

Use `sagemaker_mlflow.evaluate()` to log evaluation metrics:

```
import sagemaker_mlflow
import pandas as pd

eval_df = pd.DataFrame(X, columns=["f1", "f2", "f3"])
eval_df["target"] = y
dataset = mlflow.data.from_pandas(
    eval_df, source="s3://my-bucket/eval.csv", name="eval_set", targets="target"
)
sagemaker_mlflow.evaluate(model_info, data=dataset, model_type="regressor")
```

After logging, the evaluation group is stored as an artifact alongside your model:

![Evaluation group artifact in the MLflow UI.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-ui-eval-group.png)


### Register models using the SDK
<a name="mlflow-track-experiments-model-registration-sdk"></a>

Use `mlflow.register_model()` to register a model with the SageMaker Model Registry. This automatically creates a Model Package Group (if one does not exist) and a Model Package version in SageMaker AI.

```
model_uri = f"runs:/{run.info.run_id}/sklearn-model"
mv = mlflow.register_model(model_uri, "MyRegisteredModel")

print(f"Name: {mv.name}")
print(f"Version: {mv.version}")
```

You can also use `create_registered_model` to create the Model Package Group before registering versions:

```
from mlflow import MlflowClient

client = MlflowClient()
client.create_registered_model("MyRegisteredModel", tags={"team": "ml-platform"})
```

After registration, the model version is tagged with the SageMaker AI Model Package ARN. You can retrieve it as follows:

```
mv = client.get_model_version("MyRegisteredModel", mv.version)
sm_arn = mv.tags["sagemaker.model_package_arn"]
print(f"SageMaker Model Package ARN: {sm_arn}")
```

**Note**  
Do not use spaces in a model name. While MLflow supports model names with spaces, SageMaker AI Model Package does not. The registration process fails if you use spaces in your model name.

### Register models using the MLflow UI
<a name="mlflow-track-experiments-model-registration-ui"></a>

You can register a model with the SageMaker Model Registry directly in the MLflow UI. Within the **Models** menu, choose **Create Model**. Models created this way are automatically added to the SageMaker Model Registry.

![Model registry creation within the MLflow UI.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-ui-register-model.png)


After logging a model during experiment tracking, navigate to the run page in the MLflow UI. Choose the **Artifacts** pane and choose **Register model** to register the model version in both MLflow and SageMaker Model Registry.

![Register a model version from the MLflow run page.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-ui-register-model-sync.png)


### View registered models in Studio
<a name="mlflow-track-experiments-model-registration-ui-view"></a>

Within Studio, choose **Models** on the left navigation pane to view your registered models. For more information on getting started with Studio, see [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

The Model Package version page in Studio displays training metrics and datasets that were synced from MLflow:

![Model Package version overview showing training metrics in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-metrics.png)


The **Train** tab also shows the training dataset location and model artifact path:

![Training datasets and model artifacts in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-train-dataset.png)


If you logged an inference specification, the **Container** section shows the container image, model data location, and supported instance types. The **Deploy** stage shows **Approved**, indicating the model is ready for deployment:

![Inference specification containers and instance types in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-container.png)


If you logged evaluation metrics, the **Evaluate** tab displays performance metrics such as score, mean absolute error, and root mean squared error:

![Evaluation metrics in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-eval-metrics.png)


The **Evaluate** tab also shows the evaluation dataset location:

![Evaluation dataset in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-eval-dataset.png)


The **Lineage** tab shows the relationship between the MLflow experiment, model version, container image, and the Model Package Group:

![Model lineage graph showing MLflow experiment association in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-lineage.png)


### Limitations
<a name="mlflow-track-experiments-model-registration-limitations"></a>
+ Do not use spaces in model names. SageMaker AI Model Package does not support spaces, and the registration fails.
+ If the role is missing `s3:GetObject` permission on the artifact paths, inference specification and evaluation artifacts are silently skipped. The Model Package is still created but without inference or evaluation data.
+ If the role is missing `sagemaker:CreateAction` or `sagemaker:AddAssociation`, lineage associations between the MLflow model and the SageMaker AI Model Package are silently skipped. This does not affect registration or lifecycle management.
+ Setting a lifecycle stage and status does not enable the **Deploy** button in Studio. To enable one-click deployment from the UI, you must separately set the Model Package approval status to `Approved` using the SageMaker AI API.
+ Changes to the MLflow App IAM service role permissions can take up to 15 minutes to take effect.

## Manage model lifecycle stages
<a name="mlflow-track-experiments-model-registration-lifecycle"></a>

After registering a model, you can manage its lifecycle stage and status in the SageMaker AI Model Registry by setting MLflow model version aliases. When you set an alias using the lifecycle naming convention, the corresponding SageMaker AI Model Package lifecycle is automatically updated. For more information about model lifecycle stages, see [Stage models in the Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-staging-construct.html).

### IAM permissions for lifecycle management
<a name="mlflow-track-experiments-model-registration-lifecycle-iam"></a>

The MLflow tracking server or MLflow App IAM service role requires `sagemaker:UpdateModelPackage` permission to manage lifecycle stages. This action is already included in the base registration permissions described above.

#### Restrict lifecycle transitions
<a name="mlflow-track-experiments-model-registration-lifecycle-restrict"></a>

You can use IAM condition keys to control which lifecycle transitions a role is allowed to perform:
+ `sagemaker:ModelLifeCycle/stage` — The lifecycle stage being set. Values: `staging`, `production`.
+ `sagemaker:ModelLifeCycle/stageStatus` — The lifecycle status being set. Values: `pending`, `active`.

**Example: Deny production promotions**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "sagemaker:UpdateModelPackage",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sagemaker:ModelLifeCycle/stage": "production"
                }
            }
        }
    ]
}
```

**Example: Allow only staging/pending transitions**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sagemaker:UpdateModelPackage",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "sagemaker:ModelLifeCycle/stage": "staging",
                    "sagemaker:ModelLifeCycle/stageStatus": "pending"
                }
            }
        }
    ]
}
```

When a lifecycle transition is denied by IAM policy, the MLflow alias operation fails and returns an error to the caller.

For more information about model lifecycle in SageMaker AI Model Registry, see [Deploy a Model from the Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-deploy.html).

### Set lifecycle stages using the SDK
<a name="mlflow-track-experiments-model-registration-lifecycle-sdk"></a>

Use the following alias format to set the lifecycle stage and status:

```
sagemakerlifecycle-{{stage}}-{{status}}
```

Supported stages: `staging`, `production`

Supported statuses: `pending`, `active`

**Note**  
Stage and status values must be lowercase. MLflow aliases only support lowercase characters, so values such as `Production` or `Active` are not valid.

```
import mlflow

mlflow.set_tracking_uri({{arn}})
client = mlflow.MlflowClient()

# Set lifecycle to staging/pending
client.set_registered_model_alias("MyRegisteredModel", "sagemakerlifecycle-staging-pending", {{version}})

# Promote to production/active
client.set_registered_model_alias("MyRegisteredModel", "sagemakerlifecycle-production-active", {{version}})
```

You can verify the lifecycle state by describing the SageMaker AI Model Package:

```
import boto3

sm = boto3.client("sagemaker")
mv = client.get_model_version("MyRegisteredModel", {{version}})
sm_arn = mv.tags["sagemaker.model_package_arn"]

desc = sm.describe_model_package(ModelPackageName=sm_arn)
print(desc["ModelLifeCycle"]["Stage"])       # "staging"
print(desc["ModelLifeCycle"]["StageStatus"]) # "pending"
```

### Set lifecycle stages using the MLflow UI
<a name="mlflow-track-experiments-model-registration-lifecycle-ui"></a>

In the MLflow UI, navigate to the model version page. Under **Aliases**, add an alias using the `sagemakerlifecycle-{{stage}}-{{status}}` format. The SageMaker AI Model Package lifecycle is automatically updated when the alias is saved.

![Setting a lifecycle alias in the MLflow UI.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-ui-lifecycle-alias.png)


### View lifecycle stages in Studio
<a name="mlflow-track-experiments-model-registration-lifecycle-view"></a>

In Studio, navigate to **Models** and select a Model Package version. The lifecycle stage and status are displayed on the **Details** tab under **Model Lifecycle**.

![Model lifecycle stage and status in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/mlflow/mlflow-studio-mp-lifecycle.png)


## Prevent updates to registered models using resource tags
<a name="mlflow-track-experiments-model-registration-tag-control"></a>

You can use IAM resource tag-based conditions to prevent the MLflow tracking server or MLflow App role from modifying specific Model Package Groups or Model Package versions. This allows you to lock individual models from being updated through MLflow after they reach a certain state.

For example, the following policy denies `UpdateModelPackage` on any Model Package that has the tag `locked=true`:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "sagemaker:UpdateModelPackage",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/locked": "true"
                }
            }
        }
    ]
}
```

When this policy is attached to the tracking server or MLflow App role, any attempt to update the lifecycle of a tagged Model Package from MLflow fails with an access denied error.

You can similarly restrict `CreateModelPackage` on a Model Package Group to prevent new versions from being registered:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "sagemaker:CreateModelPackage",
            "Resource": "arn:aws:sagemaker:{{region}}:{{account}}:model-package-group/{{group-name}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/frozen": "true"
                }
            }
        }
    ]
}
```

**Note**  
Resource tag-based conditions rely on tags that are applied to the SageMaker AI Model Package Group or Model Package resource (not the MLflow model). You can apply these tags through the SageMaker AI console, CLI, or SDK. Tag-based conditions may take up to 15 minutes to propagate after a tag is applied.