Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Set up a detector

After you've [prepared data in an Amazon Simple Storage Service (Amazon S3) bucket](gettingstarted-datasource.md "gettingstarted-datasource.md"), create
a detector and add a dataset. At the end of each interval, the detector imports data from the bucket (your
datasource) into the dataset and analyzes it.

###### Steps

- [Create a detector](#gettingstarted-detector-create "#gettingstarted-detector-create")
- [Add a dataset](#gettingstarted-detector-add-dataset "#gettingstarted-detector-add-dataset")
- [Activate the detector](#gettingstarted-detector-activate "#gettingstarted-detector-activate")
- [(Optional) Add an alert](#gettingstarted-detector-alert "#gettingstarted-detector-alert")
- [Review anomalies](#gettingstarted-detector-anomalies "#gettingstarted-detector-anomalies")
- [Clean up](#gettingstarted-detector-cleanup "#gettingstarted-detector-cleanup")

## Create a detector

Use the Lookout for Metrics console to create the detector that monitors your data.

###### To create a detector

1. Open the [Lookout for Metrics console](https://console.aws.amazon.com/lookoutmetrics/home "https://console.aws.amazon.com/lookoutmetrics/home").
2. Choose **Create detector**.
3. For **Name**, enter `sample-detector`.
4. For **Description**, enter `Getting started detector`.
5. For **Interval**, choose the interval that you used to organize your data.
6. Choose a **Create**.

## Add a dataset

Add a dataset by specifying the location of your data in Amazon S3 and the names of fields in your data that are
timestamps, measures, and dimensions.

###### To add a dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose **sample-detector**.
3. Choose **Add dataset**.
4. For **Name**, enter `S3-dataset`.
5. For **Timezone**, choose the timezone that is reflected in your data's timestamps.
6. For **Datasource**, choose Amazon S3.
7. Choose a detector mode. For **Backtest**, you only provide historical data. For
   **Continuous**, you provide continuous data and can optionally provide historical data to
   speed up learning.
8. Follow the instructions to specify the data path(s) and then choose **Next**.
9. Choose the field in your data that specifies a timestamp for each record. The detector checks the
   timestamp on each record, and only processes records that match the interval that it is analyzing.
10. Choose a numerical field in your data to be a **Measure**. The detector aggregates values
    of the measure field within each interval and monitors the aggregate value. For example,
    `availability`
11. (Optional) Choose additional fields to be measures and dimensions. A dimension is a field that creates
    subgroups of measure values that are monitored separately. For example, `city`.

## Activate the detector

To import data from the bucket and look for anomalies, activate the detector.

###### To activate the detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose the detector.
3. Choose **Activate detector**.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies.
If no historical data is available, the training process takes approximately one day for a five-minute interval. Training time varies
[depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart "gettingstarted-quotas.md#gettingstarted-quotas-coldstart").

## (Optional) Add an alert

In this section, you will add an alert to the detector. You will need to create an Amazon SNS topic. You will use
its ARN in this step. For more information about creating an Amazon SNS topic, see [Tutorial: Creating an Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-create-topic.md "../../../sns/latest/dg/sns-tutorial-create-topic.md").

###### To add an alert

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add alert**.
4. Configure the following options.

######

    * **Name** – `my-alert`
    * **Description** – `Send anomaly alerts to an SNS
     topic.`
    * **Threshold** – `50`
    * **Channel** – Amazon SNS
    * **Format** – Short Text
    * **Resource** – Your SNS topic
    * **Role** – **Create a role**

5. Choose **Add alert**.

## Review anomalies

In this section, you will review the anomalies found by the detector.

###### To review anomalies

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose **sample-detector**.
3. Choose **View anomalies**.
4. Choose an anomaly.

Each anomaly can have multiple metrics associated with it. Review each metric to see if it is relevant or not,
and use the feedback options to help the detector learn about your data.

## Clean up

If you are done using the detector, delete it.

###### To delete the detector

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose the detector, **sample-detector**.
3. Choose **Delete**.

The detector's dataset and alerts are deleted automatically.
