Defect Detection App is in preview release and is subject to change.

# Performance metrics

Defect Detection App provides the following metrics.

###### Topics

- [Image classification
  metrics](#dda-evaluate-model-classification-metrics "#dda-evaluate-model-classification-metrics")
- [Precision](#dda-precision-metric "#dda-precision-metric")
- [Recall](#dda-recall-metric "#dda-recall-metric")
- [F1 score](#dda-f1-metric "#dda-f1-metric")
- [Testing results](#test-results "#test-results")

## Image classification

metrics

Defect Detection App provides the following summary metrics for the classifications that a model
makes during testing:

- [Precision](#dda-precision-metric "#dda-precision-metric")
- [Recall](#dda-recall-metric "#dda-recall-metric")
- [F1 score](#dda-f1-metric "#dda-f1-metric")

## Precision

The precision metric answers the question – _When the model predicts that
an image contains an anomaly, how often is that prediction correct?_

Precision is a useful metric for situations where the cost of a false positive is high.
For example, the cost of removing a machine part that is not defective from an assembled
machine.

Defect Detection App provides a summary precision metric value for the entire test dataset.

_Precision_ is the fraction of correctly predicted anomalies (true
positives) over all predicted anomalies (true and false positives). The formula for precision
is as follows.

_Precision value = true positives / (true positives + false
positives)_

The possible values for precision range from 0–1. The Defect Detection App console displays
precision as a percentage value (0–100).

A higher precision value indicates that more of the predicted anomalies are correct. For
example, suppose your model predicts that 100 images are anomalous. If 85 of the predictions
are correct (the true positives) and 15 are incorrect (the false positives), the precision is
calculated as follows:

85 _true positives_ / (85 _true positives_ + 15
_false positives_) = **0.85** precision
value

However, if the model only predicts 40 images correctly out of 100 anomaly predictions,
the resulting precision value is lower at **0.40** (that is, 40 /
(40 + 60) = 0.40). In this case, your model is making more incorrect predictions than correct
predictions. To fix this, consider making improvements to your model. For more information, see
[Improving your model](improve-model.md "improve-model.md").

For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall").

## Recall

The recall metric answers the question - _Of the total number of anomalous images
in the test dataset, how many are correctly predicted as anomalous?_

The recall metric is useful for situations where the cost of a false negative is high. For
example, when the cost of not removing a defective part is high. Defect Detection App provides a summary
recall metric value for the entire test dataset.

_Recall_ is the fraction of the anomalous test images that were
detected correctly. It is a measure of how often the model can correctly predict an anomalous
image, when it's actually present in the images of your test dataset. The formula for recall is
calculated as follows:

_Recall value = true positives / (true positives + false negatives)_

The range for recall is 0–1. The Defect Detection App console displays recall as a percentage
value (0–100).

A higher recall value indicates that more of the anomalous images are correctly
identified. For example, suppose the test dataset contains 100 anomalous images. If the model
correctly detects 90 of the 100 anomalous images, then the recall is as follows:

90 _true positives_ / (90 _true positives_ + 10
_false negatives_) = **0.90** recall
value

A recall value of 0.90 indicates that your model is correctly predicting most of the
anomalous images in the test dataset. If the model only predicts 20 of the anomalous images
correctly, the recall is lower at **0.20** (that is, 20 / (20 + 80) = 0.20).

In this case, you should consider making improvements to your model. For more information,
see [Improving your model](improve-model.md "improve-model.md").

For more information, see [Precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall "https://en.wikipedia.org/wiki/Precision_and_recall").

## F1 score

Defect Detection App provides an average model performance score for the test dataset. Specifically,
model performance for anomaly classification is measured by the F1 score metric, which is the
harmonic mean of the precision and recall scores.

_F1 score_ is an aggregate measure that takes into account both
precision and recall. The model performance score is a value between 0 and 1. The higher the
value, the better the model is performing for both recall and precision. For example, for a
model with precision of 0.9 and a recall of 1.0, the F1 score is 0.947.

If the model isn't performing well, for example, with a low precision of 0.30 and a high
recall of 1.0, the F1 score is 0.46. Similarly, if the precision is high (0.95) and the recall
is low (0.20), the F1 score is 0.33. In both cases, the F1 score is low, which indicates
problems with the model.

For more information, see [F1
score](https://en.wikipedia.org/wiki/F1_score "https://en.wikipedia.org/wiki/F1_score").

## Testing results

During testing, the model predicts classification for each test image in the test dataset.
The result for each prediction is compared to the label (normal or anomaly) of the
corresponding test image as follows:

- Correctly predicting that an image is anomalous is considered a _true
  positive_.
- Incorrectly predicting that an image is anomalous is considered a _false
  positive_.
- Correctly predicting that an image is normal is considered a _true
  negative_.
- Incorrectly predicting that an image is normal is considered a _false
  negative_.

If the model is a segmentation model, the model also predicts masks and anomaly labels for
the location of anomalies on the test image.

Defect Detection App uses the results of the comparisons to generate the performance metrics.
