# Flywheel iterations

Use flywheel iterations to help you create and manage new model versions.

###### Topics

- [Iteration workflow](#flywheels-iterate-flow "#flywheels-iterate-flow")
- [Managing iterations (console)](#flywheels-iterate-console "#flywheels-iterate-console")
- [Managing iterations (API)](#flywheels-iterate-api "#flywheels-iterate-api")

## Iteration workflow

A flywheel starts out with a trained model version or uses an initial dataset to train a model version.

Over time, as you obtain new labeled data, you train new model versions to improve the performance of your flywheel model.
When you run the flywheel, it creates a new iteration that trains and evaluates a new model version. You can
promote the new model version if its performance is superior to the existing active model version.

The flywheel iteration workflow includes the following steps:

1. You create datasets for the new labeled data.
2. You run the flywheel to create a new iteration. The iteration follows these steps to train and evaluate a new
   model version:
   1. Evaluates the active model version using the new data.
   2. Trains a new model version using the new data.
   3. Stores the evaluation and training results in the data lake.
   4. Returns the F1 scores for both models.

3. After the iteration completes, you can compare the F1 scores for the existing active model and the new model.
4. If the new model version has superior performance, you promote it to be the active model version.
   You can use the [console](#flywheels-iterate-console-promote "#flywheels-iterate-console-promote") or the [API](#flywheels-iterate-console-promote "#flywheels-iterate-console-promote") to promote the new model version.

## Managing iterations (console)

You can use the console to start a new iteration and query the status of an in-progress iteration. You can
also view the results of completed iterations.

### Start a flywheel iteration (console)

Before you can start a new iteration, create one or more new training or test datasets.
See [Configuring datasets](datasets-config.md "datasets-config.md")

###### Start a flywheel iteration (console)

1. Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2. From the left menu, choose **Flywheels**.
3. From the **Flywheels** table, choose a flywheel.
4. Choose **Run flywheel**.

### Analyze iteration results (Console)

After it runs the flywheel iteration, the console displays the results in the **Flywheels
iterations** table.

### Promote new model version (Console)

From the model details page in the console, you can promote a new model version to be the active model version.

###### Promote a flywheel model version to active model version (console)

1. Sign in to the AWS Management Console and open the [Amazon Comprehend console](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/").
2. From the left menu, choose **Flywheels**.
3. From the **Flywheels** table, choose a flywheel.
4. From the **Flywheel details page** table, choose the version to promote from the
   **Flywheels iterations** table.
5. Choose **Make active model**.

## Managing iterations (API)

You can use the Amazon Comprehend API to start a new iteration and query the status of an in-progress iteration. You can
also view the results of completed iterations.

### Start flywheel iteration (API)

Use the Amazon Comprehend [StartFlywheelIteration](../APIReference/API_StartFlywheelIteration.md "../APIReference/API_StartFlywheelIteration.md") operation to start a flywheel iteration.

```
aws comprehend start-flywheel-iteration \
    --flywheel-arn  "flywheelArn"
```

The response contains the following content.

```
{
  "FlywheelIterationArn": "arn:aws::comprehend:`aws-region`:`111122223333`:flywheel/name"
}
```

### Promote new model version (API)

Use the [UpdateFlywheel](../APIReference/API_UpdateFlywheel.md "../APIReference/API_UpdateFlywheel.md") operation to promote a model version to be the active model version.

Send the `UpdateFlywheel` request with the `ActiveModelArn` parameter
set to the ARN of the new active model version.

```
aws comprehend update-flywheel \
    --active-model-arn  "modelArn" \
```

The response contains the following content.

```
{
  "FlywheelArn": "arn:aws::comprehend:`aws-region`:`111122223333`:flywheel/name",
  "ActiveModelArn": "modelArn"
}
```

### Describe flywheel iteration results (API)

The Amazon Comprehend [DescribeFlywheelIteration](../APIReference/API_DescribeFlywheelIteration.md "../APIReference/API_DescribeFlywheelIteration.md") operation returns information about an iteration after it runs to
completion.

```
aws comprehend describe-flywheel-iteration \
	--flywheel-arn "flywheelArn" \
	--flywheel-iteration-id  "flywheelIterationId" \
	--region `aws-region`
```

The response contains the followng content.

```
{
    "FlywheelIterationProperties": {
        "FlywheelArn": "flywheelArn",
        "FlywheelIterationId": "iterationId",
        "CreationTime": <createdAt>,
        "EndTime": <endedAt>,
        "Status": <status>,
        "Message": <message>,
        "EvaluatedModelArn": "modelArn",
        "EvaluatedModelMetrics": {
            "AverageF1Score": <value>,
            "AveragePrecision": <value>,
            "AverageRecall": <value>,
            "AverageAccuracy": <value>
        },
        "TrainedModelArn": "modelArn",
        "TrainedModelMetrics": {
            "AverageF1Score": <value>,
            "AveragePrecision": <value>,
            "AverageRecall": <value>,
            "AverageAccuracy": <value>
        }
    }
}
```

### Get iteration history (API)

Use the [ListFlywheelIterationHistory](../APIReference/API_ListFlywheelIterationHistory.md "../APIReference/API_ListFlywheelIterationHistory.md") operation to get information about iteration history.

```
aws comprehend list-flywheel-iteration-history \
	--flywheel-arn "flywheelArn"
```

The response contains the followng content.

```
{
    "FlywheelIterationPropertiesList": [
        {
            "FlywheelArn": "<flywheelArn>",
            "FlywheelIterationId": "20220907T214613Z",
            "CreationTime": 1662587173.224,
            "EndTime": 1662592043.02,
            "Status": "<status>",
            "Message": "<message>",
            "EvaluatedModelArn": "modelArn",
            "EvaluatedModelMetrics": {
                "AverageF1Score": 0.8333333333333333,
                "AveragePrecision": 0.75,
                "AverageRecall": 0.9375,
                "AverageAccuracy": 0.8125
            },
            "TrainedModelArn": "modelArn",
            "TrainedModelMetrics": {
                "AverageF1Score": 0.865497076023392,
                "AveragePrecision": 0.7636363636363637,
                "AverageRecall": 1.0,
                "AverageAccuracy": 0.84375
            }
        }
    ]
}

```
