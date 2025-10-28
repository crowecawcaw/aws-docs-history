# Advanced training configurations

## Sample rate configuration

The **sample rate** defines how frequently sensor readings
are recorded (for example, once every second, or once every minute). This setting directly
impacts the **granularity** of the training data, and
influences the model's ability to capture short-term variations in sensor behavior.

Visit [Sampling for high-frequency data and
consistency between training and inference](ano-best-practices.md#apply-sampling-high-frequency-data "ano-best-practices.md#apply-sampling-high-frequency-data") to learn about best practices.

### Configure target sampling rate

You can optionally specify a `TargetSamplingRate` in your training
configuration, to control the frequency at which data is sampled. Supported values
are:

```
PT1S | PT5S | PT10S | PT15S | PT30S | PT1M | PT5M | PT10M | PT15M | PT30M | PT1H
```

These are ISO 8601 duration formats, representing the following time formats:

- `PT1S` = 1 second
- `PT1M` = 1 minute
- `PT1H` = 1 hour

Choose a sampling rate that strikes the right balance between **data resolution**, and **training efficiency**.
The following rates are available:

- **Higher sampling rates** (`PT1S`) offer
  finer detail but may increase data volume and training time.
- **Lower sampling rates** (`PT10M`,
  `PT1H`) reduce data size and cost but may miss short-lived
  anomalies.

### Handling timestamp misalignment

AWS IoT SiteWise automatically compensates for **timestamp
misalignment** across multiple data streams during training. This ensures
consistent model behavior even if input signals are not perfectly aligned in time.

Visit [Sampling for high-frequency data and
consistency between training and inference](ano-best-practices.md#apply-sampling-high-frequency-data "ano-best-practices.md#apply-sampling-high-frequency-data") to learn about best
practices.

### Enable sampling

Add the following code to
`anomaly-detection-training-payload.json`.

Configure sampling by adding `TargetSamplingRate` in the training action
payload, with the sampling rate of the data. The allowed values are: `PT1S | PT5S |
 PT10S | PT15S | PT30S | PT1M | PT5M | PT10M | PT15M | PT30M | PT1H`.

```
{
    "exportDataStartTime": StartTime,
    "exportDataEndTime": EndTime,
    "targetSamplingRate": "TargetSamplingRate"
}
```

###### Example of a sample rate configuration:

```
{
    "exportDataStartTime": 1717225200,
    "exportDataEndTime": 1722789360,
    "targetSamplingRate": "PT1M"
}
```

## Label your data

When labeling your data, you must define time intervals that represent periods of
abnormal equipment behavior. This labeling information is provided as a
`CSV` file, where each row specifies a time range during which the
equipment was not operating correctly.

Each row contains two timestamps:

- The **start time**, indicating when abnormal behavior
  is believed to have begun.
- The **end time**, representing when the failure or
  issue was first observed.

This CSV file is stored in an Amazon S3 bucket and is used during model training to help the
system learn from known examples of abnormal behavior. The following example shows how your
label data should appear as a `.csv` file. The file has no header.

###### Example of a CSV file:

```
2024-06-21T00:00:00.000000,2024-06-21T12:00:00.000000
2024-07-11T00:00:00.000000,2024-07-11T12:00:00.000000
2024-07-31T00:00:00.000000,2024-07-31T12:00:00.000000
```

**Row 1** represents a maintenance event on **June 21, 2024**, with a **12-hour
window** (from `2024-06-21T00:00:00.000000Z` to
`2024-06-21T12:00:00.000000Z`) for AWS IoT SiteWise to look for abnormal behavior.

**Row 2** represents a maintenance event on **July 11, 2024**, with a **12-hour
window** (from `2024-07-11T00:00:00.000000Z` to
`2024-07-11T12:00:00.000000Z`) for AWS IoT SiteWise to look for abnormal behavior.

**Row 3** represents a maintenance event on **July 31, 2024**, with a **12-hour
window** (from `2024-07-31T00:00:00.000000Z` to
`2024-07-31T12:00:00.000000Z`) for AWS IoT SiteWise to look for abnormal behavior.

AWS IoT SiteWise uses all of these time windows to train and evaluate models that can identify
abnormal behavior around these events. Note that not all events are detectable, and results
are highly dependent on the quality and characteristics of the underlying data.

For details about best practices for sampling, see [Best practices](ano-best-practices.md "ano-best-practices.md").

### Data labeling steps

- Configure your Amazon S3 bucket according to the labeling prerequisites at [Labeling data prerequisites](anomaly-prerequisites.md#label-data "anomaly-prerequisites.md#label-data").
- Upload the file to your labeling bucket.
- Add the following to
  `anomaly-detection-training-payload.json`.
  - Provide the locations in the `labelInputConfiguration` section of
    the file. Replace `labels-bucket` with bucket name and
    `files-prefix` with file(s) path or any part of prefix. All files at
    the location are parsed, and (on success) used as label files.

```
{
    "exportDataStartTime": `StartTime`,
    "exportDataEndTime": `EndTime`,
    "labelInputConfiguration":
      {
       "bucketName": "`label-bucket`",
       "prefix": "`files-prefix`"
      }
}
```

###### Example of a label configuration:

```
{
    "exportDataStartTime": 1717225200,
    "exportDataEndTime": 1722789360,
    "labelInputConfiguration": {
      "bucketName": "anomaly-detection-customer-data-278129555252-iad",
      "prefix": "Labels/model=b2d8ab3e-73af-48d8-9b8f-a290bef931b4/asset[d3347728-4796-4c5c-afdb-ea2f551ffe7a]/Lables.csv"
    }
}
```

## Evaluate your model

Pointwise model diagnostics for an AWS IoT SiteWise training model is an evaluation of the model
performance at the individual events. During training, AWS IoT SiteWise generates an anomaly score,
and sensor contribution diagnostics for each row in the input dataset. A higher anomaly
score indicates a higher likelihood of an abnormal event.

Pointwise diagnostics are available, when you train a model with [ExecuteAction](../APIReference/API_ExecuteAction.md "../APIReference/API_ExecuteAction.md") API, and `AWS/ANOMALY_DETECTION_TRAINING` action
type.

To configure model evaluation,

- Configure your Amazon S3 bucket according to the labelling prerequisites at [Labeling data prerequisites](anomaly-prerequisites.md#label-data "anomaly-prerequisites.md#label-data").
- Add the following to
  `anomaly-detection-training-payload.json`.
  - Provide the `evaluationStartTime` and `evaluationEndTime`
    (both in epoch seconds) for the data in the window used to evaluate the performance
    of the model.
  - Provide the Amazon S3 bucket location (`resultDestination`) in order for
    the the evaluation diagnostics to be written to.

###### Note

The model evaluation interval (`dataStartTime` to `dataEndtime`)
must either overlap, or be contiguous to the training interval. No gaps are
permitted.

```
{
  "exportDataStartTime": `StartTime`,
  "exportDataEndTime": `EndTime`,
  "modelEvaluationConfiguration": {
    "dataStartTime": `evaluationStartTime`,
    "dataEndTime": `evaluationEndTime`
    "resultDestination": {
      "bucketName": "`s3BucketName`",
      "prefix": "`bucketPrefix`"
    }
  }
}

```

###### Example of a model evaluation configuration:

```
{
  "exportDataStartTime": 1717225200,
  "exportDataEndTime": 1722789360,
  "modelEvaluationConfiguration": {
    "dataStartTime": 1722789360,
    "dataEndTime": 1725174000,
    "resultDestination": {
      "bucketName": "anomaly-detection-customer-data-278129555252-iad",
      "prefix": "Evaluation/asset[d3347728-4796-4c5c-afdb-ea2f551ffe7a]/1747681026-evaluation_results.jsonl"
    }
  }
}

```

## Generate model metrics

Model metrics provide comprehensive insights into your trained anomaly detection models'
performance and quality. The training process automatically generates these metrics and
publishes them to your specified Amazon S3 bucket, making them easily accessible for analysis,
model comparison, and promotion decisions in retraining workflows.

### Understanding model metrics

The training process automatically generates model metrics and provides detailed
information about:

- **Model Performance**: Quantitative measures like
  precision, recall, and AUC when labeled data is available
- **Data Quality**: Information about the training data
  used and time periods covered
- **Event Detection**: Statistics about identified
  anomalies and labeled events
- **Model Comparison**: Comparison metrics between
  different model versions during retraining

### Configure model metrics

destination

To enable model metrics generation, configure an Amazon S3 destination where the metrics
are published.

1. Configure your Amazon S3 bucket as per the [Model evaluation prerequisites](anomaly-prerequisites.md#prerequisites-model-evaluation "anomaly-prerequisites.md#prerequisites-model-evaluation").
2. Add the following to your training action payload to specify where model metrics
   should be stored:

```
{
    "trainingMode": "TRAIN_MODEL",
    "exportDataStartTime": `StartTime`,
    "exportDataEndTime": `EndTime`,
    "modelMetricsDestination": {
        "bucketName": "`bucket-name`",
        "prefix": "`prefix`"
    }
}
```

###### Example of model metrics configuration

```
{
    "exportDataStartTime": 1717225200,
    "exportDataEndTime": 1722789360,
    "modelMetricsDestination": {
        "bucketName": "anomaly-detection-metrics-bucket-123456789012-iad",
        "prefix": "ModelMetrics/computation-model-id/asset-id/training-metrics.json"
    }
}
```

### Configure model metrics for

retraining

When you set up retraining schedules, model metrics destination is required to enable
comprehensive model performance tracking and comparison:

```
{
    "trainingMode": "START_RETRAINING_SCHEDULER",
    "modelMetricsDestination": {
        "bucketName": "`bucket-name`",
        "prefix": "`prefix`"
    },
    "retrainingConfiguration": {
        "lookbackWindow": "P180D",
        "promotion": "SERVICE_MANAGED",
        "retrainingFrequency": "P30D",
        "retrainingStartDate": "`StartDate`"
    }
}
```

###### Parameters

`bucketName`

Amazon S3 bucket where model metrics will be stored

`prefix`

Amazon S3 prefix/path for organizing model metrics files

### Model metrics structure

Model metrics are stored as JSON files in your Amazon S3 bucket in the following
structure:

```
{
    "labeled_ranges": [],
    "labeled_event_metrics": {
        "num_labeled": 0,
        "num_identified": 0,
        "total_warning_time_in_seconds": 0
    },
    "predicted_ranges": [],
    "unknown_event_metrics": {
        "num_identified": 0,
        "total_duration_in_seconds": 0
    },
    "data_start_time": "2023-11-01",
    "data_end_time": "2023-12-31",
    "labels_present": false,
    "model_version_metrics": {
        "precision": 1.0,
        "recall": 1.0,
        "mean_fractional_lead_time": 0.7760964912280702,
        "auc": 0.5971207364893062
    }
}
```

###### Key metrics

`labeled_ranges`

Time ranges where labeled anomalies were provided during training

`labeled_event_metrics`

Statistics about how well the model identified known labeled events

`num_labeled`

Total number of labeled events in the training data

`num_identified`

Number of labeled events the model correctly identified

`total_warning_time_in_seconds`

Total time the model spent in warning state for labeled events

`predicted_ranges`

Time ranges where the model predicted anomalies during evaluation

`unknown_event_metrics`

Statistics about anomalies detected in unlabeled data

`data_start_time / data_end_time`

Time window covered by the training data

`labels_present`

Boolean indicating whether labeled data was used during training

`model_version_metrics`

Additional version-specific metrics for model comparison

### Advanced metrics for labeled

models

When you provide labeled data during training, additional performance metrics are
included in the Amazon S3 files:

- **Recall**: The proportion of events that
  AWS IoT SiteWise correctly identified to the events that you labeled during the same period. For
  example, you may have labeled 10 events, but AWS IoT SiteWise only identified 9 of them. In this
  case, the recall is 90%.
- **Precision**: The proportion of true positives
  to total identified events. For example, if AWS IoT SiteWise identifies 10 events, but only 7 of
  those events correspond to events you labeled, then the precision is 70%.
- **MeanFractionalLeadTime**: A measurement of
  how quickly (relative to the length of the event), on average, AWS IoT SiteWise detects each
  event. For example, a typical event at your facility may last 10 hours. On average, it
  may take the model 3 hours to identify the event. In this case, the mean fractional
  lead time is 0.7.
- **AUC**: Area Under the Curve (AUC) measures
  the ability of a machine learning model to predict a higher score for positive
  examples as compared to negative examples. A value between 0 and 1 that indicates how
  well your model is able to separate the categories in your dataset. A value of 1
  indicates that it was able to separate the categories perfectly.

### Model promotion and metrics

During retraining workflows, the metrics stored in Amazon S3 enable informed model
promotion decisions:

#### Managed mode (Automatic promotion)

- The system automatically compares metrics between old and new model versions
  using the Amazon S3-stored data
- Models are promoted based on improved performance indicators
- Promotion decisions include specific reason codes stored alongside the
  metrics:
  - `AUTO_PROMOTION_SUCCESSFUL`: New model metrics are better than
    current version
  - `MODEL_METRICS_DIDNT_IMPROVE`: New model performance did not
    improve
  - `POOR_MODEL_QUALITY_DETECTED`: New model has poor quality
    assessment

#### Manual mode (Customer-controlled

promotion)

- You can download and analyze detailed metrics from Amazon S3 to make promotion
  decisions
- All historical model versions and their metrics remain accessible in Amazon S3
- You can build custom dashboards and analysis tools using the Amazon S3-stored
  metrics
