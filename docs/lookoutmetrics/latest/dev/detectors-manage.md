Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Managing detectors

You manage [detectors](lookoutmetrics-detectors.md "lookoutmetrics-detectors.md") in the Lookout for Metrics
console.

When you create a detector, you configure just a name, description, and interval.
Optionally, you can choose an encryption key to use with the dataset's data, instead of the
service's default key. After the detector is created, you can [add a dataset](detectors-dataset.md "detectors-dataset.md") and activate the detector to start finding anomalies.

###### Topics

- [Viewing detector logs](#detectors-log "#detectors-log")
- [Deleting detectors](#detectors-delete "#detectors-delete")
- [Deactivating detectors](#detectors-deactivate "#detectors-deactivate")
- [Reactivating detectors](#detectors-retry "#detectors-retry")

## Viewing detector logs

When activation is complete, the detector analyzes data after each interval. If there are
any anomalies in the data for an interval, the detector assigns each a severity score. If the
score exceeds an alert target's threshold, the detector sends an alert to that target. You can
view the results of each analysis in the detector log.

###### To view the detector log

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Scroll down to the bottom of the page.

## Deleting detectors

To stop analyzing data and delete it from Lookout for Metrics, delete the detector. This also deletes
the detector's dataset and alerts.

###### To delete a detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Delete**.

You can't recover a deleted detector or its subresources. Data stored in Amazon Lookout for Metrics is
completely deleted within 90 days of the detector being deleted.

## Deactivating detectors

You can deactivate detectors if its status is `LEARNING` or
`ACTIVE`. To reconfigure a detector, you must first deactivate the detector.

###### To deactivate a detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Deactivate detector**.

Deactivating a detector does not delete the detector or its subresources. If you are using
the Lookout for Metrics SDK, use the [DeactivateAnomalyDetector](../api/API_DeactivateAnomalyDetector.md "../api/API_DeactivateAnomalyDetector.md") operation.

## Reactivating detectors

Failed and inactive detectors can be edited and reactivated. You can reconfigure the
detector and dataset before reactivating the detector. If a detector is active, you can
deactivate, reconfigure, and then reactivate the detector.

A detector can only be reactivated if its status is `FAILED` or
`INACTIVE`. Detectors that are `INITIALIZING`, `LEARNING`,
or `ACTIVE` cannot be reactivated.

When reconfiguring the detector, the Detector name (`AnomalyDetectorName`) and
Tags fields are not editable. You can change the KMS key (`KmsKeyArn`) if the
detector is inactive. If the detector failed, the KMS key cannot be changed.

When reconfiguring the dataset, the Detector Arn (`AnomalyDetectorArn`),
Dataset name (`MetricSetName`), and Tags fields are not editable.

###### To reactivate a detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose the failed or inactive detector.
3. **[Optional]** To [reconfigure the detector](detectors-setup.md#detectors-create "detectors-setup.md#detectors-create"), choose **Edit** under
   **Create a detector**.
4. **[Optional]** To[reconfigure the dataset](detectors-setup.md#dataset-create "detectors-setup.md#dataset-create"), choose **Edit** under **Add a
   dataset**.
5. Choose **Activate detector**.

If you are using the Lookout for Metrics SDK, use the [UpdateAnomalyDetector](../api/API_UpdateAnomalyDetector.md "../api/API_UpdateAnomalyDetector.md") operation to edit the detector settings and the [UpdateMetricSet](../api/API_UpdateMetricSet.md "../api/API_UpdateMetricSet.md") operation to edit the dataset. Use [ActivateAnomalyDetector](../api/API_ActivateAnomalyDetector.md "../api/API_ActivateAnomalyDetector.md") to reactivate the detector.
