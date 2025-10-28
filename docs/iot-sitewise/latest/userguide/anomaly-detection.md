# Detect anomalies with Lookout for Equipment

###### Note

Anomaly detection is only available in the Regions where Amazon Lookout for Equipment is available.

You can integrate AWS IoT SiteWise with Amazon Lookout for Equipment to gain insights about your industrial equipment through anomaly
detection and predictive maintenance of industrial equipment. Lookout for Equipment is a machine learning (ML) service for
monitoring industrial equipment that detects abnormal equipment behavior and identifies potential failures. With
Lookout for Equipment, you can implement predictive maintenance programs and identify suboptimal equipment processes. For more
information about Lookout for Equipment, see [What is
Amazon Lookout for Equipment?](../../../lookout-for-equipment/latest/ug/what-is.md "../../../lookout-for-equipment/latest/ug/what-is.md") in the _Amazon Lookout for Equipment User Guide_.

When you create a prediction to train an ML model to detect anomalous equipment behavior, AWS IoT SiteWise sends asset
property values to Lookout for Equipment to train an ML model to detect anomalous equipment behavior. To define a prediction
definition on an asset model, you specify the IAM roles needed for Lookout for Equipment to access your data and the properties to
send to Lookout for Equipment and send processed data to Amazon S3. For more information, see [Create asset models in AWS IoT SiteWise](create-asset-models.md "create-asset-models.md").

To integrate AWS IoT SiteWise and Lookout for Equipment, you'll perform the following high-level steps:

- Add a prediction definition on an asset model that outlines what properties you want to track. The prediction definition is a reusable collection of measurements,
  transforms, and metrics that is used to create predictions on the assets that are based on that asset model.
- Train the prediction based on historical data that you provide.
- Schedule inference, which tells AWS IoT SiteWise how often to run a specific prediction.
  Once inference is scheduled, the Lookout for Equipment model monitors the data it receives from your equipment and looks for
  anomalies in equipment behavior. You can view and analyze the results in SiteWise Monitor, using the AWS IoT SiteWise GET API
  operations, or the Lookout for Equipment console. You can also create alarms using alarm detectors from the asset model to alert you
  about abnormal equipment behavior.

###### Topics

- [Add a prediction definition
  (console)](#ad-add-prediction-definition-console "#ad-add-prediction-definition-console")
- [Train a prediction (console)](#ad-train-prediction-console "#ad-train-prediction-console")
- [Start or stop inference on a prediction
  (console)](#ad-start-stop-inference-console "#ad-start-stop-inference-console")
- [Add a prediction definition (CLI)](#ad-add-prediction-definition-cli "#ad-add-prediction-definition-cli")
- [Train a prediction and starting inference
  (CLI)](#ad-train-inference-prediction-cli "#ad-train-inference-prediction-cli")
- [Train a prediction (CLI)](#ad-train-prediction-cli "#ad-train-prediction-cli")
- [Start or stop inference on a prediction
  (CLI)](#ad-start-stop-inference-cli "#ad-start-stop-inference-cli")

## Add a prediction definition

(console)

To begin sending data collected by AWS IoT SiteWise to Lookout for Equipment, you must add an AWS IoT SiteWise prediction definition to an asset model.

###### To add a prediction definition to an AWS IoT SiteWise asset model

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models** and select the asset model to which you want to add the
   prediction definition.
3. Choose **Predictions**.
4. Choose **Add prediction definition**.
5. Define details about the prediction definition.
   1. Enter a unique **Name** and a
      **Description** for your prediction definition.
      Choose the name thoughtfully because after you create the prediction
      definition, you can't change its name.
   2. Create or select an **IAM permissions role** that allows
      AWS IoT SiteWise to share your asset data with Amazon Lookout for Equipment. The role should have the following IAM and trust policies. For help creating the role, see [Creating a role using custom trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").

   **IAM policy**

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "L4EPermissions",
    "Effect": "Allow",
    "Action": [
    "lookoutequipment:CreateDataset",
    "lookoutequipment:CreateModel",
    "lookoutequipment:CreateInferenceScheduler",
    "lookoutequipment:DescribeDataset",
    "lookoutequipment:DescribeModel",
    "lookoutequipment:DescribeInferenceScheduler",
    "lookoutequipment:ListInferenceExecutions",
    "lookoutequipment:StartDataIngestionJob",
    "lookoutequipment:StartInferenceScheduler",
    "lookoutequipment:UpdateInferenceScheduler",
    "lookoutequipment:StopInferenceScheduler"
    ],
    "Resource": [
    "arn:aws:lookoutequipment:`us-east-1`:`123456789012`:inference-scheduler/IoTSiteWise_*",
    "arn:aws:lookoutequipment:`us-east-1`:`123456789012`:model/IoTSiteWise_*",
    "arn:aws:lookoutequipment:`us-east-1`:`123456789012`:dataset/IoTSiteWise_*"
    ]
    },
    {
    "Sid": "L4EPermissions2",
    "Effect": "Allow",
    "Action": [
    "lookoutequipment:DescribeDataIngestionJob"
    ],
    "Resource": "*"
    },
    {
    "Sid": "S3Permissions",
    "Effect": "Allow",
    "Action": [
    "s3:CreateBucket",
    "s3:ListBucket",
    "s3:PutObject",
    "s3:GetObject"
    ],
    "Resource": [
    "arn:aws:s3:::iotsitewise-*"
    ]
    },
    {
    "Sid": "IAMPermissions",
    "Effect": "Allow",
    "Action": [
    "iam:GetRole",
    "iam:PassRole"
    ],
    "Resource": "arn:aws:iam::`111122223333`:role/`Role_name`"
    }
    ]
   }`

   ```

   **Trust policy**

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "iotsitewise.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`123456789012`"
    },
    "ArnEquals": {
    "aws:SourceArn": "arn:aws:iotsitewise:`us-east-1`:`123456789012`:asset/*"
    }
    }
    },
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "lookoutequipment.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`123456789012`"
    },
    "ArnEquals": {
    "aws:SourceArn": "arn:aws:lookoutequipment:`us-east-1`:`123456789012`:*"
    }
    }
    }
    ]
   }`

   ```

   3. Choose **Next**.

6. Select data attributes (measurements, transforms, and metrics) that you want
   to send to Lookout for Equipment.
   1. (Optional) Select measurements.
   2. (Optional) Select transforms.
   3. (Optional) Select metrics.
   4. Choose **Next**.

7. Review your selections. To add the prediction definition to the asset model,
   on the summary page, choose **Add prediction
   definition**.

You can also **Edit** or **Delete** an existing prediction definition that
has active predictions attached.

## Train a prediction (console)

After you've added a prediction definition to an asset model, you can train the predictions that are on your assets.

###### To train a prediction in AWS IoT SiteWise

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**, and select the asset you want to monitor.
3. Choose **Predictions**.
4. Select the predictions that you want to train.
5. Under **Actions**, choose **Start training**, and do the following:
   1. Under **Prediction details**, select an IAM permissions role that allows AWS IoT SiteWise to share your asset data with Lookout for Equipment. If you need
      to create a new role, choose **Create a new role**.
   2. For **Training data settings**, enter a **Training data time range** to select which data to use to train the prediction.
   3. (Optional) Select sampling rate of the data after post processing.
   4. (Optional) For **Data labels**, provide an Amazon S3 bucket and prefix that holds your labeling data.
      For more information about labeling data, see [Labeling your data](../../../lookout-for-equipment/latest/ug/labeling-data.md "../../../lookout-for-equipment/latest/ug/labeling-data.md")
      in the _Amazon Lookout for Equipment User Guide_.
   5. Choose **Next**.

6. (Optional) If you want the prediction to be active as soon as it has completed training, under
   **Advanced settings**, select **Automatically activate the prediction after
   training**, and then do the following:
   1. Under **Input data**, for **Data upload frequency**, define how often data is uploaded, and
      for **Offset delay time**, define how much of a buffer to use.
   2. Choose **Next**.

7. Review the details of the prediction and choose **Save and start**.

## Start or stop inference on a prediction

(console)

###### Note

Lookout for Equipment charges apply to scheduled inferences with the data transferred between AWS IoT SiteWise and Lookout for Equipment. For more information, see [Amazon Lookout for Equipment pricing](https://aws.amazon.com/lookout-for-equipment/pricing/ "https://aws.amazon.com/lookout-for-equipment/pricing/").

If you added the prediction `lookoutequipment:CreateDataset`, but did not choose to activate it after training, you must activate it to
start monitoring your assets.

###### To start inference for a prediction

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**, and select the asset the prediction is added to.
3. Choose **Predictions**.
4. Select the predictions that you want to activate.
5. Under **Actions**, choose **Start inference**, and do the following:
   1. Under **Input data**, for **Data upload frequency**, define how often data is uploaded, and
      for **Offset delay time**, define how much of a buffer to use.
   2. Choose **Save and start**.

###### To stop inference for a prediction

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**, and select the asset the prediction is added to.
3. Choose **Predictions**.
4. Select the predictions that you want to stop.
5. Under **Actions**, choose **Stop inference**.

## Add a prediction definition (CLI)

To define a prediction definition on a new or existing asset model, you can use the AWS Command Line Interface (AWS CLI). After
you define the prediction definition on the asset model, you train, and schedule inference for, a prediction on an
asset in AWS IoT SiteWise to do anomaly detection with Lookout for Equipment.

**Prerequisites**

To complete these steps, you must have an asset model and at least one asset created. For more information,
see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli") and [Create an asset (AWS CLI)](create-assets.md#create-asset-cli "create-assets.md#create-asset-cli").

If you are new to AWS IoT SiteWise, you must call the `CreateBulkImportJob` API operation to import asset
property values into AWS IoT SiteWise, which will be used to train the model. For more information, see [Create an AWS IoT SiteWise bulk import job (AWS CLI)](CreateBulkImportJob.md "CreateBulkImportJob.md").

###### To add a prediction definition

1. Create a file called `asset-model-payload.json`. Follow the steps in these other sections to add your asset model's details to the file,
   but don't submit the request to create or update the asset model.
   - For more information about how to create an asset model, see [Create an asset model (AWS CLI)](create-asset-models.md#create-asset-model-cli "create-asset-models.md#create-asset-model-cli")
   - For more information about how to update an existing asset model, see [Update an asset model, component model, or interface
     (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli")

2. Add a Lookout for Equipment composite model (`assetModelCompositeModels`) to the asset model by adding the following
   code.
   - Replace `Property` with the ID of the properties that you want to include.
     To get those IDs, call [`DescribeAssetModel`](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md").
   - Replace `RoleARN` with the ARN of an IAM role that allows Lookout for Equipment to access
     your AWS IoT SiteWise data.

```
{
  ...
  "assetModelCompositeModels": [
    {
      "name": "L4Epredictiondefinition",
      "type": "AWS/L4E_ANOMALY",
      "properties": [
          {
            "name": "AWS/L4E_ANOMALY_RESULT",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_RESULT",
            "unit": "none",
            "type": {
              "measurement": {}
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_INPUT",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_INPUT",
            "type": {
               "attribute": {
                 "defaultValue": "{\"properties\": [\"`Property1`\", \"`Property2`\"]}"
               }
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_PERMISSIONS",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_PERMISSIONS",
            "type": {
              "attribute": {
                "defaultValue": "{\"roleArn\": \"`RoleARN`\"}"
              }
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_DATASET",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_DATASET",
            "type": {
                "attribute": {}
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_MODEL",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_MODEL",
            "type": {
              "attribute": {}
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_INFERENCE",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_INFERENCE",
            "type": {
              "attribute": {}
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_TRAINING_STATUS",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_TRAINING_STATUS",
            "type": {
              "attribute": {
                "defaultValue": "{}"
              }
            }
          },
          {
            "name": "AWS/L4E_ANOMALY_INFERENCE_STATUS",
            "dataType": "STRUCT",
            "dataTypeSpec": "AWS/L4E_ANOMALY_INFERENCE_STATUS",
            "type": {
              "attribute": {
                "defaultValue": "{}"
              }
            }
          }
   ]
}
```

3. Create the asset model or update the existing asset model. Do one of the following:
   - To create the asset model, run the following command:

   ```
   aws iotsitewise create-asset-model --cli-input-json file://asset-model-payload.json
   ```

   - To update the existing asset model, run the following command. Replace
     `asset-model-id` with the ID of the asset model that you want to
     update.

   ```
   aws iotsitewise update-asset-model \
     --asset-model-id `asset-model-id` \
     --cli-input-json file://asset-model-payload.json
   ```

After you run the command, note the `assetModelId` in the response.

## Train a prediction and starting inference

(CLI)

Now that the prediction definition is defined, you can train assets based on it and start inference. If you want to train your prediction but not start inference, skip to [Train a prediction (CLI)](#ad-train-prediction-cli "#ad-train-prediction-cli"). To train the prediction and start inference on the asset, you’ll need the `assetId` of the target resource.

###### To train and start inference of the prediction

1. Run the following command to find the `assetModelCompositeModelId` under `assetModelCompositeModelSummaries`. Replace
   `asset-model-id` with the ID of the asset model that you created in
   [Update an asset model, component model, or interface
   (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli").

```
aws iotsitewise describe-asset-model \
  --asset-model-id `asset-model-id` \
```

2. Run the following command to find the `actionDefinitionId` of the `TrainingWithInference` action. Replace
   `asset-model-id` with the ID used in previous step and replace `asset-model-composite-model-id` with the ID returned in the previous step.

```
aws iotsitewise describe-asset-model-composite-model \
  --asset-model-id `asset-model-id` \
  --asset-model-composite-model-id `asset-model-composite-model-id` \
```

3. Create a file called `train-start-inference-prediction.json` and add the following code, replacing the following:
   - `asset-id` with the ID of the target asset
   - `action-definition-id` with the ID of the TrainingWithInference action
   - `StartTime` with the start of the training data, provided in epoch seconds
   - `EndTime` with the end of the training data, provided in epoch seconds
   - `TargetSamplingRate` with the sampling rate of the data after post processing by Lookout for Equipment. Allowed
     values are: `PT1S | PT5S | PT10S | PT15S | PT30S | PT1M | PT5M | PT10M | PT15M | PT30M | PT1H`.

```
{
  "targetResource": {
    "assetId": "`asset-id`"
  },
  "actionDefinitionId": "`action-definition-Id`",
  "actionPayload":{
    "stringValue": "{\"l4ETrainingWithInference\":{\"trainingWithInferenceMode\":\"START\",\"trainingPayload\":{\"exportDataStartTime\":`StartTime`,\"exportDataEndTime\":`EndTime`},\"targetSamplingRate\":\"`TargetSamplingRate`\"},\"inferencePayload\":{\"dataDelayOffsetInMinutes\":0,\"dataUploadFrequency\":\"PT5M\"}}}"
  }
}
```

4. Run the following command to start training and inference:

```
aws iotsitewise execute-action --cli-input-json file://train-start-inference-prediction.json
```

## Train a prediction (CLI)

Now that the prediction definition is defined, you can train assets based on it. To train the prediction on the asset, you’ll need the `assetId` of the target resource.

###### To train the prediction

1. Run the following command to find the `assetModelCompositeModelId` under `assetModelCompositeModelSummaries`. Replace
   `asset-model-id` with the ID of the asset model that you created in
   [Update an asset model, component model, or interface
   (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli").

```
aws iotsitewise describe-asset-model \
  --asset-model-id `asset-model-id` \
```

2. Run the following command to find the `actionDefinitionId` of the `Training` action. Replace
   `asset-model-id` with the ID used in previous step and replace `asset-model-composite-model-id` with the ID returned in the previous step.

```
aws iotsitewise describe-asset-model-composite-model \
  --asset-model-id `asset-model-id` \
  --asset-model-composite-model-id `asset-model-composite-model-id` \
```

3. Create a file called `train-prediction.json` and add the following code, replacing the following:
   - `asset-id` with the ID of the target asset
   - `action-definition-id` with the ID of the training action
   - `StartTime` with the start of the training data, provided in epoch seconds
   - `EndTime` with the end of the training data, provided in epoch seconds
   - (Optional) `BucketName` with the name of the Amazon S3 bucket that holds your label data
   - (Optional) `Prefix` with the prefix associated with the Amazon S3 bucket.
   - `TargetSamplingRate` with the sampling rate of the data after post processing by Lookout for Equipment.
     Allowed values are: `PT1S | PT5S | PT10S | PT15S | PT30S | PT1M | PT5M | PT10M | PT15M | PT30M | PT1H`.

   ###### Note

   Include both the bucket name and prefix or neither.

```
{
  "targetResource": {
    "assetId": "`asset-id`"
  },
  "actionDefinitionId": "`action-definition-Id`",
  "actionPayload":{ "stringValue": "{\"l4ETraining\": {\"trainingMode\":\"START\",\"exportDataStartTime\": `StartTime`, \"exportDataEndTime\": `EndTime`, \"targetSamplingRate\":\"`TargetSamplingRate`\"}, \"labelInputConfiguration\": {\"bucketName\": \"`BucketName`\", \"prefix\": \"`Prefix`\"}}}"
}
}
```

4. Run the following command to start training:

```
aws iotsitewise execute-action --cli-input-json file://train-prediction.json
```

Before you can start inference, training must be completed. To check the status of the training, do one of the
following:

- From the console, navigate to the asset the prediction is on.
- From the AWS CLI, call `BatchGetAssetPropertyValue` using the `propertyId` of the `trainingStatus` property.

## Start or stop inference on a prediction

(CLI)

Once the prediction is trained, you can start inference to tell Lookout for Equipment to start monitoring your assets. To
start or stop inference, you’ll need the `assetId` of the target resource.

###### To start inference

1. Run the following command to find the `assetModelCompositeModelId` under `assetModelCompositeModelSummaries`. Replace
   `asset-model-id` with the ID of the asset model that you created in
   [Update an asset model, component model, or interface
   (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli").

```
aws iotsitewise describe-asset-model \
  --asset-model-id `asset-model-id` \
```

2. Run the following command to find the `actionDefinitionId` of the `Inference` action. Replace
   `asset-model-id` with the ID used in previous step and replace `asset-model-composite-model-id` with the ID returned in the previous step.

```
aws iotsitewise describe-asset-model-composite-model \
  --asset-model-id `asset-model-id` \
  --asset-model-composite-model-id `asset-model-composite-model-id` \
```

3. Create a file called `start-inference.json` and add the following code, replacing the following:
   - `asset-id` with the ID of the target asset
   - `action-definition-id` with the ID of the start inference action
   - `Offset` with the amount of buffer to use
   - `Frequency` with how often data is uploaded

```
{
  "targetResource": {
    "assetId": "`asset-id`"
  },
  "actionDefinitionId": "`action-definition-Id`",
  "actionPayload":{ "stringValue": "{\"l4EInference\": {\"inferenceMode\":\"START\",\"dataDelayOffsetInMinutes\": `Offset`, \"dataUploadFrequency\": \"`Frequency`\"}}"
}}
```

4. Run the following command to start inference:

```
aws iotsitewise execute-action --cli-input-json file://start-inference.json
```

###### To stop inference

1. Run the following command to find the `assetModelCompositeModelId` under `assetModelCompositeModelSummaries`. Replace
   `asset-model-id` with the ID of the asset model that you created in
   [Update an asset model, component model, or interface
   (AWS CLI)](update-asset-models.md#update-asset-model-cli "update-asset-models.md#update-asset-model-cli").

```
aws iotsitewise describe-asset-model \
  --asset-model-id `asset-model-id` \
```

2. Run the following command to find the `actionDefinitionId` of the `Inference` action. Replace
   `asset-model-id` with the ID used in previous step and replace `asset-model-composite-model-id` with the ID returned in the previous step.

```
aws iotsitewise describe-asset-model-composite-model \
  --asset-model-id `asset-model-id` \
  --asset-model-composite-model-id `asset-model-composite-model-id` \
```

3. Create a file called `stop-inference.json` and add the following code, replacing the following:
   - `asset-id` with the ID of the target asset
   - `action-definition-id` with the ID of the start inference action

```
{
  "targetResource": {
    "assetId": "`asset-id`"
  },
  "actionDefinitionId": "`action-definition-Id`",
  "actionPayload":{ "stringValue": "{\"l4EInference\":{\"inferenceMode\":\"STOP\"}}"
}}
```

4. Run the following command to stop inference:

```
aws iotsitewise execute-action --cli-input-json file://stop-inference.json
```
