

# Actions, resources, and condition keys for Amazon SageMaker with MLflow
<a name="list_sagemaker-mlflow"></a>

Amazon SageMaker with MLflow (service prefix: `sagemaker-mlflow`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sagemaker/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sagemaker/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sagemaker-mlflow/sagemaker-mlflow.json) for this service.

**Topics**
+ [Actions defined by Amazon SageMaker with MLflow](#list_sagemaker-mlflow-actions-as-permissions)
+ [Resource types defined by Amazon SageMaker with MLflow](#list_sagemaker-mlflow-resources-for-iam-policies)
+ [Condition keys for Amazon SageMaker with MLflow](#list_sagemaker-mlflow-policy-keys)

## Actions defined by Amazon SageMaker with MLflow
<a name="list_sagemaker-mlflow-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AccessUI](${APIReferenceDocPage})  **
  - **Description:** Grants permission to access the MLflow UI
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateExperiment](${APIReferenceDocPage})  **
  - **Description:** Grants permission to create an MLflow experiment
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModelVersion](${APIReferenceDocPage})  **
  - **Description:** Grants permission to create a new model version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRegisteredModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to create a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRun](${APIReferenceDocPage})  **
  - **Description:** Grants permission to create a new run within an experiment
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExperiment](${APIReferenceDocPage})  **
  - **Description:** Grants permission to mark an MLflow experiment for deletion
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoggedModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLoggedModelTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a tag for a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelVersion](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a model version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelVersionTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a model version tag
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegisteredModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegisteredModelAlias](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a registered model alias
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegisteredModelTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a registered model tag 
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRun](${APIReferenceDocPage})  **
  - **Description:** Grants permission to mark a run for deletion
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a tag on a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTraceTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete a trace tag in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTraces](${APIReferenceDocPage})  **
  - **Description:** Grants permission to delete traces in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EndTrace](${APIReferenceDocPage})  **
  - **Description:** Grants permission to end a trace in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FinalizeLoggedModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set status for a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDownloadURIForModelVersionArtifacts](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get a URI to download model artifacts for a specific model version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperiment](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get metadata for an MLflow experiment
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentByName](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get metadata for an MLflow experiment by name
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLatestModelVersions](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get the latest model versions
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetLoggedModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetricHistory](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get a list of all values for the specified metric for a given run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelVersion](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get a model version by model name and version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModelVersionByAlias](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get model version by alias in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRegisteredModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRun](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get metadata, metrics, parameters, and tags for a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTraceInfo](${APIReferenceDocPage})  **
  - **Description:** Grants permission to get information about a trace in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListArtifacts](${APIReferenceDocPage})  **
  - **Description:** Grants permission to list artifacts for a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLoggedModelArtifacts](${APIReferenceDocPage})  **
  - **Description:** Grants permission to list artifacts for a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [LogBatch](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log a batch of metrics, parameters, and tags for a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogInputs](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log inputs for a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogLoggedModelParams](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log params for a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogMetric](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log a metric for a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log the model associated with a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogOutputs](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log outputs, such as models, for a run in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [LogParam](${APIReferenceDocPage})  **
  - **Description:** Grants permission to log a parameter tracked during a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RenameRegisteredModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to rename a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreExperiment](${APIReferenceDocPage})  **
  - **Description:** Grants permission to restore an experiment marked for deletion
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreRun](${APIReferenceDocPage})  **
  - **Description:** Grants permission to restore a deleted run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchExperiments](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for MLflow experiments
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchLoggedModels](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for logged models in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchModelVersions](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for a model version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchRegisteredModels](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for registered models in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchRuns](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for runs that satisfy expressions
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchTraces](${APIReferenceDocPage})  **
  - **Description:** Grants permission to search for traces in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SetExperimentTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a tag on an experiment
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetLoggedModelTags](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set tags for a logged model in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetModelVersionTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a tag for the model version 
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetRegisteredModelAlias](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a registered model alias
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetRegisteredModelTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a tag for a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a tag on a run
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetTraceTag](${APIReferenceDocPage})  **
  - **Description:** Grants permission to set a trace tag in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTrace](${APIReferenceDocPage})  **
  - **Description:** Grants permission to start a trace in MLflow
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TransitionModelVersionStage](${APIReferenceDocPage})  **
  - **Description:** Grants permission to transition a model version to a particular stage
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExperiment](${APIReferenceDocPage})  **
  - **Description:** Grants permission to update the metadata for an MLflow experiment
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModelVersion](${APIReferenceDocPage})  **
  - **Description:** Grants permission to update the model version
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegisteredModel](${APIReferenceDocPage})  **
  - **Description:** Grants permission to update a registered model
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRun](${APIReferenceDocPage})  **
  - **Description:** Grants permission to update run metadata
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-mlflow-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-mlflow-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon SageMaker with MLflow
<a name="list_sagemaker-mlflow-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [mlflow-tracking-server](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MlflowTrackingServer.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:mlflow-tracking-server/${MlflowTrackingServerName} |   | 

## Condition keys for Amazon SageMaker with MLflow
<a name="list_sagemaker-mlflow-policy-keys"></a>

Amazon SageMaker with MLflow defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a tag key and value pair | String | 