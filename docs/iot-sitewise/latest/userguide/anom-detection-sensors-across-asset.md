# Enable anomaly detection on sensors across

assets

## Create a computation model

(AWS CLI)

To create a computation model, use the AWS Command Line Interface (AWS CLI). After you
define the computation model, train the model and schedule inference to do anomaly detection
across assets in AWS IoT SiteWise.

The following steps explain this process:

1. To set up anomaly detection, use the [UpdateAssetModel
   (AWS CLI)](../../../cli/latest/reference/iotsitewise/update-asset-model.md "../../../cli/latest/reference/iotsitewise/update-asset-model.md"), and meet the following requirements:
   1. At least one input property that is of either `DOUBLE` or
      `INTEGER` data type. It is either a measurement or transform property,
      and is used to train the model.
   2. A result property of `STRING` data type. It must be a measurement
      property, and stores the anomaly detection results.

2. Create a file `anomaly-detection-computation-model-payload.json` with the
   following content:

###### Note

Create a computation model by directly providing `assetProperty` as the
data source.

```
{
    "computationModelName": "name of ComputationModel",
    "computationModelConfiguration": {
        "anomalyDetection": {
            "inputProperties": "${properties}",
            "resultProperty": "${p3}"
        }
    },
    "computationModelDataBinding": {
        "properties": {
            "list": [
                {
                    "assetProperty": {
                        "assetId": "asset-id",
                        "propertyId": "input-property-id-1"
                    }
                },
                {
                    "assetProperty": {
                        "assetId": "asset-id",
                        "propertyId": "input-property-id-2"
                    }
                }
            ]
        },
        "p3": {
            "assetProperty": {
                "assetId": "asset-id",
                "propertyId": "results-property-id"
            }
        }
    }
}
```

3. Run the following command to create a computation model:

```
aws iotsitewise create-computation-model \
    --cli-input-json file://`anomaly-detection-computation-model-payload.json`
```

## ExecuteAction API payload

preparation

The next steps to execute training and inference is performed with the [ExecuteAction](../APIReference/API_ExecuteAction.md "../APIReference/API_ExecuteAction.md") API. Both training and inference are configured with a JSON action
payload configuration. When invoking the [ExecuteAction](../APIReference/API_ExecuteAction.md "../APIReference/API_ExecuteAction.md") API,
the action payload must be provided as a value with a `stringValue` payload.

The payload must strictly adhere to the API requirements. Specifically, the value must
be a **flat string** with no **control
characters** (for example, newlines, tabs, or carriage returns). The following
options provides two reliable ways to supply a valid action-payload.

### Option 1: Use a clean payload

file

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
    --action-payload "stringValue={\"exportDataStartTime\":1717225200,\"exportDataEndTime\":1722789360,\"targetSamplingRate\":\"PT1M\"}"
```

## Train the model (AWS CLI)

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

The payload must conform to [Option 1: Use a clean payload
file](#clean-payload-file-across-assets "#clean-payload-file-across-assets").

    1. `StartTime` with the start of the training data, provided in epoch
     seconds.
    2. `EndTime` with the end of the training data, provided in epoch
     seconds.
    3. You can optionally configure [Advanced inference configurations](advanced-inference-configurations.md "advanced-inference-configurations.md").


    	1. (Optional) `TargetSamplingRate` with the sampling rate of the
    	 data.
    	2. (Optional) `LabelInputConfiguration` to specify time periods when
    	 anomalous behavior occurred for improved model training.
    	3. (Optional) `ModelEvaluationConfiguration` to evaluate model
    	 performance by running inference on a specified time range after training
    	 completes.

```
{
  "exportDataStartTime": StartTime,
  "exportDataEndTime": EndTime
}
```

###### Example of a training payload example:

```
{
  "exportDataStartTime": 1717225200,
  "exportDataEndTime": 1722789360
}
```

3. Run the following command to start training (without providing asset as a target
   resource). Replace the following parameters in the command:

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file:`//anomaly-detection-training-payload.json`
```

4. Run the following command to check for status of the model training process. The
   latest execution summary shows the execution status
   (`RUNNING`/`COMPLETED`/`FAILED`).

```
aws iotsitewise list-executions \
    --target-resource-type COMPUTATION_MODEL \
    --target-resource-id `computation-model-id`
```

5. Run the following command to check the configuration of the latest trained model.
   This command produces an output only if at least one model has completed training
   successfully.

```
aws iotsitewise describe-computation-model-execution-summary \
    --computation-model-id computation-model-id
```

## Start and stop retraining the model

(AWS CLI)

After initial model training, you can configure automatic retraining to address data
drift and maintain model accuracy over time. The retraining scheduler allows you to set up
periodic model updates with configurable promotion modes.

### Start retraining scheduler

1. Prepare the same payload as mentioned in [Start retraining scheduler](anom-detection-sensors-asset.md#start-retraining-scheduler "anom-detection-sensors-asset.md#start-retraining-scheduler").
2. Execute training action (without providing asset as target resource). Replace the
   following parameters in the command:
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `training-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_TRAINING` action.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file://`anomaly-detection-start-retraining-payload.json`
```

3. Run the following command to check for status of start retraining scheduler
   process. The latest execution summary shows the execution status
   (`RUNNING`/`COMPLETED`/`FAILED`).

```
aws iotsitewise list-executions \
    --target-resource-type COMPUTATION_MODEL \
    --target-resource-id `computation-model-id`
```

### Stop retraining scheduler

1. Prepare the same payload as mentioned in [Stop retraining scheduler](anom-detection-sensors-asset.md#stop-retraining-scheduler "anom-detection-sensors-asset.md#stop-retraining-scheduler").
2. Execute training action (without providing asset as target resource). Replace the
   following parameters in the command:
   1. `computation-model-id` with the ID of the target computation
      model.
   2. `training-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_TRAINING` action.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --action-definition-id `training-action-definition-id` \
    --action-payload stringValue@=file://`anomaly-detection-stop-retraining-payload.json`
```

3. Run the following command to check for status of stop retraining scheduler
   process. The latest execution summary shows the execution status
   (`RUNNING`/`COMPLETED`/`FAILED`).

```
aws iotsitewise list-executions \
    --target-resource-type COMPUTATION_MODEL \
    --target-resource-id `computation-model-id`
```

## Start and stop inference

(AWS CLI)

After training the model, start the inference, which instructs AWS IoT SiteWise to begin
monitoring your industrial assets for anomalies.

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
   the following code. Replace the following parameters as described:

###### Note

The payload must conform to [Option 1: Use a clean payload
file](#clean-payload-file-across-assets "#clean-payload-file-across-assets").

    1. `DataUploadFrequency`: Configure the frequency at which the
     inference schedule runs to perform anomaly detection. Allowed values are:
     `PT5M, PT10M, PT15M, PT30M, PT1H, PT2H..PT12H, PT1D`.



    ```
    "inferenceMode": "START",
    "dataUploadFrequency": "`DataUploadFrequency`"
    ```
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
   2. `inference-action-definition-id` with the ID of the
      `AWS/ANOMALY_DETECTION_INFERENCE` action from Step 1.

```
aws iotsitewise execute-action \
    --target-resource computationModelId=`computation-model-id` \
    --action-definition-id `inference-action-definition-id` \
    --action-payload stringValue@=file:`//anomaly-detection-inference-payload.json`
```

4. Run the following command to check if inference is still running. The
   `inferenceTimerActive` field is set to `TRUE` when inference
   is active.

```
aws iotsitewise describe-computation-model-execution-summary \
    --computation-model-id `computation-model-id`
```

5. The following command lists all the inference executions:

```
aws iotsitewise list-executions \
    --target-resource-type COMPUTATION_MODEL \
    --target-resource-id `computation-model-id`
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

The payload must conform to [Option 1: Use a clean payload file](anom-detection-sensors-asset.md#clean-payload-file "anom-detection-sensors-asset.md#clean-payload-file"). 3. Run the following command to stop inference. Replace the following parameter in
the payload file:

    1. `computation-model-id` with the ID of the target computation
     model.
    2. `inference-action-definition-id` with the ID of the
     `AWS/ANOMALY_DETECTION_INFERENCE` action from Step 1.###### Example of the stop inference command:

```
aws iotsitewise execute-action \
--target-resource computationModelId=`computation-model-id` \
--action-definition-id `inference-action-definition-id` \
--action-payload stringValue@=file:`//anomaly-detection-stop-inference-payload.json`

```
