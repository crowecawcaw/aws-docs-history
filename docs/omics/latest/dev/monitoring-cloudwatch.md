# Monitoring HealthOmics with CloudWatch metrics

You can monitor HealthOmics using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

The AWS HealthOmics service reports the following metrics in the `AWS/Omics`
namespace.

API Call Count metrics are reported for the following AWS HealthOmics APIs. Only the API
Operation dimension is reported.

- Reference and reference store APIs —CreateReferenceStore, DeleteReferenceStore,
  StartReferenceImportJob
- Sequence store and read set APIs —CreateSequenceStore, DeleteSequenceStore,
  StartReadSetImportJob, StartReadSetActivationJob, StartReadSetExportJob
- Variant store APIs — CreateVariantStore, DeleteVariantStore, StartVariantImportJob, CancelVariantImportJob
- Annotation store APIs — CreateAnnotationStore, DeleteAnotationStore,
  StartAnnotationImportJob, CancelAnnotationImportJob
- Workflow, run, and run group APIs — CreateWorkflow, DeleteWorkflow, StartRun,
  CancelRun, DeleteRun, CreateRunGroup, DeleteRunGroup

## Viewing `AWS HealthOmics`

metrics

CloudWatch metrics for AWS HealthOmics are viewable in the CloudWatch console.

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Metrics**, choose **All Metrics**, and then
   choose **AWS/Usage**.
3. Filter **Service** for **AWS HealthOmics**.
4. Choose the dimension, choose a metric name, then choose **Add to
   graph**.
5. Choose a value for the date range. The metric count for the selected date range is
   displayed in the graph.

## Creating an alarm using CloudWatch

A CloudWatch alarm watches a single metric over a specified time period, and performs one or
more actions: sending a notification to an Amazon Simple Notification Service (Amazon SNS) topic
or Auto Scaling policy. The action or actions are based on the value of the metric relative to a
given threshold over a number of time periods that you specify. CloudWatch can also send you an
Amazon SNS message when the alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has persisted for the
period you specify.

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home "https://console.aws.amazon.com/cloudwatch/home").
2. Choose **Alarms**, and then choose **Create
   Alarm**.
3. Choose **AWS/Usage**, and then choose an AWS HealthOmics metric using the
   Service dimension.
4. For **Time Range**, choose a time range to monitor, and then choose
   **Next**.
5. Enter a **Name** and **Description**.
6. For Whenever, choose **>=**, and type a maximum value.
7. If you want CloudWatch to send an email when the alarm state is reached, in the Actions
   section, for Whenever this alarm, choose State is **ALARM**. For Send
   notification to, choose a mailing list or choose **New list** and create a new
   mailing list.
8. Preview the alarm in the Alarm Preview section. If you are satisfied with the alarm,
   choose **Create Alarm**.
