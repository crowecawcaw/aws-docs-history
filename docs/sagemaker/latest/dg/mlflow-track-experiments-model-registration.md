# Automatically register SageMaker AI models with SageMaker Model Registry

You can log MLflow models and automatically register them with SageMaker Model Registry
using either the Python SDK or directly through the MLflow UI.

###### Note

Do not use spaces in a model name. While MLflow supports model names with spaces,
SageMaker AI Model Package does not. The auto-registration process fails if you use spaces in
your model name.

## Register models using the SageMaker Python SDK

Use `create_registered_model` within your MLflow client to automatically
create a model package group in SageMaker AI that corresponds to an existing MLflow model of
your choice.

```
import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri(`arn`)

client = MlflowClient()

mlflow_model_name = `'AutoRegisteredModel'`
client.create_registered_model(mlflow_model_name, tags={`"key1"`: `"value1"`})
```

Use `mlflow.register_model()` to automatically register a model with the
SageMaker Model Registry during model training. When registering the MLflow model, a
corresponding model package group and model package version are created in SageMaker AI.

```
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor

mlflow.set_tracking_uri(arn)
params = {"n_estimators": 3, "random_state": 42}
X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)

# Log MLflow entities
with mlflow.start_run() as run:
    rfr = RandomForestRegressor(**params).fit(X, y)
    signature = infer_signature(X, rfr.predict(X))
    mlflow.log_params(params)
    mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model", signature=signature)

model_uri = f"runs:/{run.info.run_id}/sklearn-model"
mv = mlflow.register_model(model_uri, "RandomForestRegressionModel")

print(f"Name: {mv.name}")
print(f"Version: {mv.version}")
```

## Register models using the MLflow UI

You can alternatively register a model with the SageMaker Model Registry directly in
the MLflow UI. Within the **Models** menu in the MLflow UI, choose
**Create Model**. Any models newly created in this way are added to the
SageMaker Model Registry.

![Model registry creation within the MLflow UI.](images/mlflow/mlflow-ui-register-model.png)

After logging a model during experiment tracking, navigate to the run page in the
MLflow UI. Choose the **Artifacts** pane and choose **Register
model** in the upper right corner to register the model version in both MLflow
and SageMaker Model Registry.

![Model registry creation within the MLflow UI.](images/mlflow/mlflow-ui-register-model-2.png)

## View registered models in Studio

Within the SageMaker Studio landing page, choose **Models** on the left navigation pane to view your registered models. For
more information on getting started with Studio, see [Launch
Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").

![MLflow models registered in SageMaker Model Registry in the Studio UI.](images/mlflow/mlflow-studio-model-registry.png)
