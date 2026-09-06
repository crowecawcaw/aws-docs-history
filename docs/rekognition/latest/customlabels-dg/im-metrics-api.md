

# Accessing Amazon Rekognition Custom Labels evaluation metrics (SDK)
<a name="im-metrics-api"></a>

The [DescribeProjectVersions](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions) operation provides access to metrics beyond those provided in the console. 

Like the console, `DescribeProjectVersions` provides access to the following metrics as summary information for the testing results and as testing results for each label:
+ [Precision](im-metrics-use.md#im-precision-metric)
+ [Recall](im-metrics-use.md#im-recall-metric)
+ [F1](im-metrics-use.md#im-f1-metric)

The average threshold for all labels and the threshold for individual labels is returned.

`DescribeProjectVersions` also provides access to the following metrics for classification and image detection (object location on image).
+ *Confusion Matrix* for image classification. For more information, see [Viewing the confusion matrix for a model](im-confusion-matrix.md).
+ *Mean Average Precision (mAP)* for image detection.
+ *Mean Average Recall (mAR)* for image detection.

`DescribeProjectVersions` also provides access to true positive, false positive, false negative, and true negative values. For more information, see [Metrics for evaluating your model](im-metrics-use.md).

The aggregate F1 score metric is returned directly by `DescribeProjectVersions`. Other metrics are accessible from a [Accessing the model summary file](im-summary-file-api.md) and [Interpreting the evaluation manifest snapshot](im-evaluation-manifest-snapshot-api.md) files stored in an Amazon S3 bucket. For more information, see [Accessing the summary file and evaluation manifest snapshot (SDK)](im-access-summary-evaluation-manifest.md).

**Topics**
+ [Accessing the model summary file](im-summary-file-api.md)
+ [Interpreting the evaluation manifest snapshot](im-evaluation-manifest-snapshot-api.md)
+ [Accessing the summary file and evaluation manifest snapshot (SDK)](im-access-summary-evaluation-manifest.md)
+ [Viewing the confusion matrix for a model](im-confusion-matrix.md)
+ [Reference: Training results summary file](im-summary-file.md)