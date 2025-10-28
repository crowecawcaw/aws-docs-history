# Enable anomaly detection on sensors of an asset

## Create a computation model (AWS CLI)

To create a computation model, use the AWS Command Line Interface (AWS CLI). After you
define the computation model, train the model, and schedule inference to do anomaly
detection on an asset in AWS IoT SiteWise.

- Create a file `anomaly-detection-computation-model-payload.json` with the
  following content:

```
{
    "computationModelName": "anomaly-detection-computation-model-name",
    "computationModelConfiguration": {
        "anomalyDetection": {
            "inputProperties": "${input_properties}",
            "resultProperty": "${result_property}"
        }
    },
    "computationModelDataBinding": {
        "input_properties": {
            "list": [{
                    "assetModelProperty": {
                        "assetModelId": "`asset-model-id`",
                        "propertyId": "`input-property-id-1`"
                    }
                },
                {
                    "assetModelProperty": {
                        "assetModelId": "`asset-model-id`",
                        "propertyId": "`input-property-id-2`"
                    }
                }
            ]
        },
        "result_property": {
            "assetModelProperty": {
                "assetModelId": "`asset-model-id`",
                "propertyId": "`results-property-id`"
            }
        }
    }
}
```

- Run the following command to create a computation model:

```
aws iotsitewise create-computation-model \
    --cli-input-json `file://anomaly-detection-computation-model-payload.json`
```

## ExecuteAction API payload preparation

The next steps to execute training and inference is performed with the [ExecuteAction](../APIReference/API_ExecuteAction.md "../APIReference/API_ExecuteAction.md") API. Both training and inference are configured with a JSON action
payload configuration. When invoking the [ExecuteAction](../APIReference/API_ExecuteAction.md "../APIReference/API_ExecuteAction.md") API,
the action payload must be provided as a value with a `stringValue` payload.

The payload must strictly adhere to the API requirements. Specifically, the value must
be a **flat string**, with no **control
characters** (for example, newlines, tabs, or carriage returns).

The following options provide two reliable ways to supply a valid action-payload:

### Option 1: Use a clean payload file

The following procedure describes the steps for a clean payload file:

1. Clean the file to remove control characters.

```
tr -d '\n\r\t' < original-action-payload.json > training-or-inference-action-payload.json
```

2. Execute the action with the file `@=file://...`.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=<`MODEL_ID`> \
    --action-definition-id <`ACTION_DEFINITION_ID`> \
    --resolve-to assetId=<`ASSET_ID`> \
    --action-payload stringValue@=file:`//training-or-inference-action-payload.json`
```

### Option 2: Inline string with escaped

quotes

The following steps describes the steps to supply the payload inline, and avoid
intermediary files:

- Use escaped double quotes (`\"`) inside the JSON string.
- Wrap the entire `StringValue=..` expression within double
  quotes.

###### Example of an escaped action payload:

```
aws iotsitewise execute-action \
    --target-resource computationModelId=<`MODEL_ID`> \
    --action-definition-id <`ACTION_DEFINITION_ID`> \
    --resolve-to assetId=<`ASSET_ID`> \
    --action-payload "stringValue={\"exportDataStartTime\":1717225200,\"exportDataEndTime\":1722789360,\"targetSamplingRate\":\"PT1M\"}"
```

## Train the model (AWS CLI)

With a computation model created, you can train a model against the assets. Follow the
below steps to train a model for an asset:

1. Run the following command to find the `actionDefinitionId` of the
   `AWS/ANOMALY_DETECTION_TRAINING` action. Replace
   `computation-model-id` with the ID returned in the previous step.

```
aws iotsitewise describe-computation-model \
    --computation-model-id `computation-model-id`
```

2. Create a file called `anomaly-detection-training-payload.json`
   and add the following values:

###### Note

The payload must conform to [Option 1: Use a clean payload file](#clean-payload-file "#clean-payload-file").

    1. `StartTime` with the start of the training data, provided in epoch
     seconds.
    2. `EndTime` with the end of the training data, provided in epoch
     seconds.
    3. You can optionally configure [Advanced training configurations](adv-training-configs.md "adv-training-configs.md"), to improve the model performance.


    	1. (Optional) `TargetSamplingRate` with the sampling rate of the
    	 data.
    	2. (Optional) `LabelInputConfiguration` to specify time periods when
    	 anomalous behavior occurred for improved model training.
    	3. (Optional) `ModelEvaluationConfiguration` to evaluate model
    	 performance by running inference on a specified time range after training
    	 completes.
    	4. (Optional) `ModelMetricsDestination` to collect comprehensive
    	 performance data (precision, recall, Area Under the Curve).

```
{
  "trainingMode": "TRAIN_MODEL",
  "exportDataStartTime": StartTime,
  "exportDataEndTime": EndTime
}
```

###### Example of a training payload example:

```
{
  "trainingMode": "TRAIN_MODEL",
  "exportDataStartTime": 1717225200,
  "exportDataEndTime": 1722789360
}
```

3. Run the following command to start training. Replace the following parameters in the
   command:
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `asset-id` with the ID of the asset against which you'll train the
      model.
   3. `training-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_TRAINING` action from Step 1.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --resolve-to assetId=`asset-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file:`//anomaly-detection-training-payload.json`
```

###### Example of an execute action:

```
aws iotsitewise execute-action --target-resource computationModelId=27cb824c-fd84-45b0-946b-0a5b0466d890 --resolve-to assetId=cefd4b68-481b-4735-b466-6a4220cd19ee --action-definition-id e54cea94-5d1c-4230-a59e-4f54dcbc972d --action-payload stringValue@=file://anomaly-detection-training-payload.json
```

4. Run the following command to check for status of the model training process. The
   latest execution summary shows the execution status
   (`RUNNING`/`COMPLETED`/`FAILED`).

```
aws iotsitewise list-executions \
    --target-resource-type COMPUTATION_MODEL \
    --target-resource-id `computation-model-id`\
    --resolve-to-resource-type ASSET \
    --resolve-to-resource-id `asset-id`
```

5. Run the following command to check the configuration of the latest trained model.
   This command produces an output only if atleast one model was trained
   successfully.

```
aws iotsitewise describe-computation-model-execution-summary \
    --computation-model-id `computation-model-id` \
    --resolve-to-resource-type ASSET \
    --resolve-to-resource-id `asset-id`
```

6. When a `ComputationModel` is using AssetModelProperty, use the [ListComputationModelResolveToResources](../APIReference/API_ListComputationModelResolveToResources.md "../APIReference/API_ListComputationModelResolveToResources.md") API to identify the assets with
   executed actions.

```
aws iotsitewise list-computation-model-resolve-to-resources \
    --computation-model-id `computation-model-id`
```

## Start and stop retraining the model

(AWS CLI)

After initial model training, you can configure automatic retraining to address data
drift and maintain model accuracy over time. The retraining scheduler allows you to set up
periodic model updates with configurable promotion modes.

### Start retraining scheduler

1. Run the following command to find the `actionDefinitionId` of the
   `AWS/ANOMALY_DETECTION_TRAINING` action. Replace
   `computation-model-id` with the ID returned from your computation model
   creation.

```
aws iotsitewise describe-computation-model \
    --computation-model-id `computation-model-id`
```

2. Create a file called
   `anomaly-detection-start-retraining-payload.json` and add the
   following code. Replace the parameters with values as described.

###### Note

The payload must conform to [Option 1: Use a clean payload file](#clean-payload-file "#clean-payload-file").

    1. `lookbackWindow` with the historical data window to use for
     retraining
     (`P180D`/`P360D`/`P540D`/`P720D`).
    2. `retrainingFrequency` with how often to retrain the model (minimum
     `P30D`, maximum `P1Y`).
    3. (Optional) `promotion` with the model promotion mode
     (`SERVICE_MANAGED` or `CUSTOMER_MANAGED`). Default is
     `SERVICE_MANAGED`.
    4. (Optional) `retrainingStartDate` with the start date for retraining
     schedule, provided in epoch seconds. Truncates the time to the nearest UTC day.
     Optional, defaults to current date.
    5. You can optionally configure [Advanced training configurations](adv-training-configs.md "adv-training-configs.md") to improve the model performance.


    	1. (Optional) `ModelMetricsDestination` to get comprehensive
    	 performance data (precision, recall, Area Under the Curve).

```
{
    "trainingMode": "START_RETRAINING_SCHEDULER",
    "retrainingConfiguration": {
        "lookbackWindow": "P180D",
        "promotion": "SERVICE_MANAGED",
        "retrainingFrequency": "P30D",
        "retrainingStartDate": "StartDate"
    }
}
```

3. Run the following command to start the retraining scheduler. Replace the following
   parameters in the command:
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `asset-id` with the ID of the asset against which you'll train the
      model.
   3. `training-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_TRAINING` action from Step 1.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --resolve-to assetId=`asset-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file://`anomaly-detection-start-retraining-payload.json`
```

###### Example of execute action command

```
aws iotsitewise execute-action --target-resource computationModelId=27cb824c-fd84-45b0-946b-0a5b0466d890 --resolve-to assetId=cefd4b68-481b-4735-b466-6a4220cd19ee --action-definition-id e54cea94-5d1c-4230-a59e-4f54dcbc972d --action-payload stringValue@=file://anomaly-detection-start-retraining-payload.json
```

### Stop retraining scheduler

1. Run the following command to find the `actionDefinitionId` of the
   `AWS/ANOMALY_DETECTION_TRAINING` action. Replace
   `computation-model-id` with the actual ID of computation model created
   earlier.

```
aws iotsitewise describe-computation-model \
    --computation-model-id `computation-model-id`
```

2. Create a file `anomaly-detection-stop-retraining-payload.json`
   and add the following:

###### Note

The payload must conform to [Option 1: Use a clean payload file](#clean-payload-file "#clean-payload-file").

```
{
    "trainingMode": "STOP_RETRAINING_SCHEDULER"
}
```

3. Run the following command to stop the retraining scheduler. Replace the following
   parameters in the command:
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `asset-id` with the ID of the asset against which you'll train the
      model.
   3. `training-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_TRAINING` action from Step 1.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --resolve-to assetId=`asset-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file://`anomaly-detection-stop-retraining-payload.json`
```

## Start and stop inference (AWS CLI)

After training the model, start the inference. This instructs AWS IoT SiteWise to actively monitor
your industrial assets for anomalies.

### Start inference

1. Run the following command to find the `actionDefinitionId` of the
   `AWS/ANOMALY_DETECTION_INFERENCE` action. Replace
   `computation-model-id` with the actual ID of computation model created
   earlier.

```
aws iotsitewise describe-computation-model \
    --computation-model-id `computation-model-id`
```

2. Create a file `anomaly-detection-start-inference-payload.json` and add
   the following values:

###### Note

The payload must conform to [Option 1: Use a clean payload file](#clean-payload-file "#clean-payload-file").

```
"inferenceMode": "START",
"dataUploadFrequency": "`DataUploadFrequency`"
```

    1. `DataUploadFrequency`: Configure the frequency at which the
     inference schedule runs to perform anomaly detection. Allowed values are:
     `PT5M, PT10M, PT15M, PT30M, PT1H, PT2H..PT12H, PT1D`.
    2. (Optional) `DataDelayOffsetInMinutes` with the delay offset in
     minutes. Set this value between 0 and 60 minutes.
    3. (Optional) `TargetModelVersion` with the model version to
     activate.
    4. (Optional) Configure the `weeklyOperatingWindow` with a shift
     configuration.
    5. You can optionally configure [Advanced inference configurations](advanced-inference-configurations.md "advanced-inference-configurations.md").


    	1. [High frequency inferencing (5 minutes – 1
    	 hour)](advanced-inference-configurations.md#high-frequency-inferencing "advanced-inference-configurations.md#high-frequency-inferencing").
    	2. [Low frequency inferencing (2 hours – 1
    	 day)](advanced-inference-configurations.md#low-frequency-inferencing "advanced-inference-configurations.md#low-frequency-inferencing").
    	3. [Flexible scheduling](advanced-inference-configurations.md#flexible-scheduling "advanced-inference-configurations.md#flexible-scheduling").

3. Run the following command to start inference. Replace the following parameters in
   the payload file.
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `asset-id` with the ID of the asset against which the model was
      trained.
   3. `inference-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_INFERENCE` action from Step 1.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --resolve-to assetId=`asset-id` \
    --action-definition-id `inference-action-definition-id` \
    --action-payload stringValue@=file:`//anomaly-detection-inference-payload.json`
```

4. Run the following command to check if inference is still running. The
   `inferenceTimerActive` field is set to `TRUE` when inference
   is active.

```
aws iotsitewise describe-computation-model-execution-summary \
    --computation-model-id `computation-model-id` \
    --resolve-to-resource-type ASSET \
    --resolve-to-resource-id `asset-id`
```

5. The following command lists all the inference executions:

```
aws iotsitewise list-executions \
   --target-resource-type COMPUTATION_MODEL \
   --target-resource-id `computation-model-id` \
   --resolve-to-resource-type ASSET \
   --resolve-to-resource-id `asset-id`
```

6. Run the following command to describe an individual execution. Replace
   `execution-id` with the id from previous Step 5.

```
aws iotsitewise describe-execution \
    --execution-id `execution-id`
```

### Stop inference

1. Run the following command to find the `actionDefinitionId` of the
   `AWS/ANOMALY_DETECTION_INFERENCE` action. Replace
   `computation-model-id` with the actual ID of computation model created
   earlier.

```
aws iotsitewise describe-computation-model \
    --computation-model-id `computation-model-id`
```

2. Create a file `anomaly-detection-stop-inference-payload.json` and add
   the following code.

```
{
    "inferenceMode": "STOP"
}
```

###### Note

The payload must conform to [Option 1: Use a clean payload file](#clean-payload-file "#clean-payload-file"). 3. Run the following command to stop inference. Replace the following parameter in
the payload file:

    1. `computation-model-id` with the ID of the target computation
     model.
    2. `asset-id` with the ID of the asset against which the model was
     trained.
    3. `inference-action-definition-id` with the ID of the
     `AWS/ANOMALY_DETECTION_INFERENCE` action from Step 1.###### Example of the stop inference command:

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --resolve-to assetId=`asset-id` \
    --action-definition-id `inference-action-definition-id` \
    --action-payload stringValue@=file:`//anomaly-detection-stop-inference-payload.json`

```

## Find computation models that uses a

given resource in data binding

To list computation models which are bound to a given resource:

- **asset model** (fetch all computation models where any
  of this asset model's properties are bound).
- **asset** (fetch all computation models where any of
  this asset's properties are bound)
- **asset model property** (fetch all computation models
  where this property is bound)
- **asset property** (fetch all computation models where
  this property is bound. This could be for informational purposes, or required when user
  tries to bind this property to another computation model but it is already bound
  somewhere else)

Use [ListComputationModelDataBindingUsages](../APIReference/API_ListComputationModelDataBindingUsages.md "../APIReference/API_ListComputationModelDataBindingUsages.md") API to fetch a list of
`ComputationModelId`s that take the asset (property) or asset model (property)
as data binding.

Prepare a `request.json` with the following information:

```
{
  "dataBindingValueFilter": {
    "asset": {
      "assetId": "<string>"
    }
    // OR
    "assetModel": {
      "assetModelId": "<string>"
    }
    // OR
    "assetProperty": {
      "assetId": "<string>",
      "propertyId": "<string>"
    }
    // OR
    "assetModelProperty": {
      "assetModelId": "<string>",
      "propertyId": "<string>"
    }
  },
  "nextToken": "<string>",
  "maxResults": "<number>"
}
```

Use the `list-computation-model-data-binding-usages` command to retrieve the
models with assets or asset models as data bindings.

```
aws iotsitewise list-computation-model-data-binding-usages \
--cli-input-json file:`//request.json`
```
