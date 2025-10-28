Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Using Amazon AppFlow with Lookout for Metrics

You can use Amazon AppFlow to create a datasource for an Amazon Lookout for Metrics detector. With Amazon AppFlow, you can collect data from
external cloud applications in a flow. A Lookout for Metrics detector reads data from the flow and monitors it for
anomalies.

To use Amazon AppFlow with Lookout for Metrics, you must use an AWS Key Management Service (AWS KMS) encryption key that you create in your account. You
can create a symmetric customer-managed key for your flow and detector [in the AWS KMS console](https://console.aws.amazon.com/kms/home#/kms/keys/create "https://console.aws.amazon.com/kms/home#/kms/keys/create").

Lookout for Metrics supports the following cloud applications with Amazon AppFlow:

- **Salesforce**
- **Marketo**
- **Dynatrace**
- **Singular**
- **Zendesk**
- **Servicenow**
- **Infor Nexus**
- **Trendmicro**
- **Veeva**
- **Google Analytics**
- **Amplitude**

###### To create a flow

1. Open the [Amazon AppFlow console](https://console.aws.amazon.com//appflow "https://console.aws.amazon.com//appflow").
2. Choose **Create flow**.
3. Enter a name for the flow.
4. For **Data encryption** choose **Customize encryption settings**.
5. For **Source details**, choose a datasource.
6. For **Destination details**, choose **Lookout for Metrics**.
7. For **Schedule frequency**, choose a frequency that matches your detector's
   interval.
8. Follow the instructions to configure the remaining options and then choose **Next**.
9. For **Field mapping**, you can choose **Map all fields directly**, or
   choose a subset of fields that contains the measures, dimensions, and timestamps that you will use with
   Lookout for Metrics.
10. Follow the instructions to complete flow setup and then choose **Create flow**.

###### To create an Amazon AppFlow dataset

1. Open the [Lookout for Metrics console Detectors](https://console.aws.amazon.com/lookoutmetrics/home#detectors "https://console.aws.amazon.com/lookoutmetrics/home#detectors") page.
2. Choose a detector.
3. Choose **Add dataset**.
4. Choose the cloud application that you chose for your flow.
5. Follow the instructions to create the datasource.
   With Amazon AppFlow, you choose fields from the flow's data to be measures and dimensions. The detector monitors the
   measures for anomalies within values of the dimensions. For example, if you have a measure named
   `availability` and a dimension named `region`, the detector finds anomalies of
   `availability` in each `region`.

The detector reads new data from Amazon AppFlow periodically, by accessing the flow. If it detects any anomalies in the
metrics for the interval, it records an anomaly and sends anomaly alerts, if configured.

When you activate the detector, it uses data from several intervals to learn, before attempting to find anomalies.
For a five minute interval, the training process takes approximately one day. Training time varies
[depending on the detector's interval](gettingstarted-quotas.md#gettingstarted-quotas-coldstart "gettingstarted-quotas.md#gettingstarted-quotas-coldstart").

###### Note

When you add an Amazon AppFlow dataset to your detector, the Lookout for Metrics console creates a [service role](permissions-service.md "permissions-service.md") with permission to read from the flow.

For more information about Amazon AppFlow, see [Getting started with Amazon AppFlow](../../../appflow/latest/userguide/getting-started.md "../../../appflow/latest/userguide/getting-started.md") in the
Amazon AppFlow User Guide.
