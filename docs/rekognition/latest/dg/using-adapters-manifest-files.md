# Manifest file formats

The following sections show samples of the manifest file formats for input,
output, and evaluation files.

## Input manifest

A manifest file is a json-line delimited file, with each line containing a
JSON that holds information about a single image.

Each entry in the Input Manifest must contain the `source-ref`
field with a path to the image in the Amazon S3 bucket and, for Custom Moderation,
the `content-moderation-groundtruth` field with ground annotations.
All images in one dataset are expected to be in the same bucket. The structure
is common to both training and testing manifest files.

The `CreateProjectVersion` operation for Custom Moderation uses the
information provided in the Input Manifest to train an adapter.

The following example is one line of a manifest file for a single image that
contains single unsafe class:

```
{
   "source-ref": "s3://foo/bar/1.jpg",
   "content-moderation-groundtruth": {
        "ModerationLabels": [
            {
                "Name": "Rude Gesture"
            }
        ]
   }
}

```

The following example is one line of a manifest file for a single, unsafe image that contains
multiple unsafe classes, specifically Nudity and Rude Gesture.

```
{
   "source-ref": "s3://foo/bar/1.jpg",
   "content-moderation-groundtruth": {
        "ModerationLabels": [
            {
                "Name": "Rude Gesture"
            },
            {
                "Name": "Nudity"
            }
        ]
   }
}

```

The following example is one line of a manifest file for a single image that
does not contain any unsafe classes:

```
{
   "source-ref": "s3://foo/bar/1.jpg",
   "content-moderation-groundtruth": {
        "ModerationLabels": []
   }
}
```

For the complete list of supported labels refer to [Moderating content](moderation.md "moderation.md").

## Output manifest

On completion of a training job, an output manifest file is returned. The
output manifest file is a JSON-line delimited file with each line containing a
JSON that holds information for a single image.
Amazon S3 Path to the OutputManifest can be obtained from
`DescribeProjectVersion`
response:

- `TrainingDataResult.Output.Assets[0].GroundTruthManifest.S3Object`
  for training dataset
- `TestingDataResult.Output.Assets[0].GroundTruthManifest.S3Object`
  for testing dataset

The following information is returned for each entry in the Output
Manifest:

|                                       |                                                                     |
| ------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key Name                              | Description                                                         |
| `source-ref`                          | Reference to an image in s3 that was provided in the input maniefst |
| `content-moderation-groundtruth`      | Ground truth annotations that were provided in the input manifest   |
| `detect-moderation-labels`            | Adapter predictions, part of the testing dataset only               |
| `detect-moderation-labels-base-model` | Base model predictions, part of the testing dataset only            | Adapter and Base model predictions are returned at ConfidenceTrehsold 5.0 in the format that is similar to the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md") response. The following example shows structure of the Adapter and Base model predictions: `{ "ModerationLabels": [ { "Confidence": number, "Name": "string", "ParentName": "string" } ], "ModerationModelVersion": "string", "ProjectVersion": "string" }` For the complete list of labels returned refer to [Moderating content](moderation.md "moderation.md"). ## Evaluation results manifest On completion of a training job, an evaluation result manifest file is returned. The evaluation results manifest is a JSON file output by the training job, and it contains information on how well the adapter performed on the test data. Amazon S3 Path to the evaluation results manifest can be obtained from the `EvaluationResult.Summary.S3Object` field in the DescribeProejctVersion response. The following example shows the structure of the evaluation results manifest: `{ "AggregatedEvaluationResults": { "F1Score": number }, "EvaluationDetails": { "EvaluationEndTimestamp": "datetime", "Labels": [ "string" ], "NumberOfTestingImages": number, "NumberOfTrainingImages": number, "ProjectVersionArn": "string" }, "ContentModeration": { "InputConfidenceThresholdEvalResults": { "ConfidenceThreshold": float, "AggregatedEvaluationResults": { "BaseModel": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int }, "Adapter": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int } }, "LabelEvaluationResults": [ { "Label": "string", "BaseModel": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int }, "Adapter": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int } } ] } "AllConfidenceThresholdsEvalResults": [ { "ConfidenceThreshold": float, "AggregatedEvaluationResults": { "BaseModel": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int }, "Adapter": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int } }, "LabelEvaluationResults": [ { "Label": "string", "BaseModel": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int }, "Adapter": { "TruePositive": int, "TrueNegative": int, "FalsePositive": int, "FalseNegative": int } } ] } ] } }` The evaluation manifest file contains: <br>• Aggregated results as defined by `F1Score` <br>• Details for the evaluation job including the ProjectVersionArn, number of training images, number of testing images, and the labels the adapter was trained on. <br>• Aggregated TruePositive, TrueNegative, FalsePositive, and FalseNegative results for both base model and adapter performance. <br>• Per label TruePositive, TrueNegative, FalsePositive, and FalseNegative results for both base model and adapter performance, calculated at the input confidence threshold. <br>• Aggregated and per label TruePositive, TrueNegative, FalsePositive, and FalseNegative results for both base model and adapter performance at different confidence thresholds. The confidence threshold ranges from 5 to 100 in steps of 5. |
