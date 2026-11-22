

# Monitor Apache Spark with CloudWatch metrics

Athena publishes calculation-related metrics to Amazon CloudWatch when the **[Publish CloudWatch metrics](notebooks-spark-getting-started.md#notebook-gs-metrics)** option for your Spark-enabled workgroup is selected. You can create custom dashboards, set alarms and triggers on metrics in the CloudWatch console. 

The namespace and metric depend on the engine version of your workgroup:
+ PySpark engine version 3 – Athena publishes `DPUCount` to the `AmazonAthenaForApacheSpark` namespace, as described later in this topic.
+ Apache Spark version 3.5 – Athena publishes `DPUConsumed` to the `AWS/Athena` namespace. For details, see [List of CloudWatch metrics and dimensions for Athena Spark interactive sessions](#notebooks-spark-metrics-interactive-sessions).

For PySpark engine version 3, Athena publishes the following metric to the CloudWatch console under the `AmazonAthenaForApacheSpark` namespace:
+ `DPUCount` – number of DPUs consumed during the session to execute the calculations.

This metric has the following dimensions:
+ `SessionId` – The ID of the session in which the calculations are submitted.
+ `WorkGroup` – Name of the workgroup.

**To view metrics for Spark-enabled workgroups in the Amazon CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**, **All metrics**.

1. Select the **AmazonAthenaForApacheSpark** namespace for PySpark engine version 3, or the **AWS/Athena** namespace for Apache Spark version 3.5.

**To view metrics with the CLI**
+ Do one of the following:
  + To list the metrics for Athena workgroups that use PySpark engine version 3, open a command prompt, and use the following command:

    ```
    aws cloudwatch list-metrics --namespace "AmazonAthenaForApacheSpark"
    ```
  + To list the metrics for Athena workgroups that use Apache Spark version 3.5, use the following command:

    ```
    aws cloudwatch list-metrics --namespace "AWS/Athena" --metric-name "DPUConsumed"
    ```
  + To list all available metrics, use the following command:

    ```
    aws cloudwatch list-metrics
    ```

## List of CloudWatch metrics and dimensions for Apache Spark calculations in Athena
<a name="notebooks-spark-metrics-metrics-table"></a>

For workgroups that use PySpark engine version 3, if you've enabled CloudWatch metrics in your Spark-enabled Athena workgroup, Athena sends the following metric to CloudWatch per workgroup. The metric uses the `AmazonAthenaForApacheSpark` namespace.



| Metric name | Description | 
| --- | --- | 
| DPUCount  | Number of DPUs (data processing units) consumed during the session to execute the calculations. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. | 

This metric has the following dimensions.


| Dimension | Description | 
| --- | --- | 
| SessionId | The ID of the session in which the calculations are submitted. | 
| WorkGroup | The name of the workgroup. | 

## List of CloudWatch metrics and dimensions for Athena Spark interactive sessions
<a name="notebooks-spark-metrics-interactive-sessions"></a>

In the release version Apache Spark version 3.5, if you've enabled CloudWatch metrics in your Athena Spark workgroup, Athena sends the following metric to CloudWatch. The metric uses the `AWS/Athena` namespace.



| Name | Description | 
| --- | --- | 
| DPUConsumed | The number of DPUs actively consumed by queries in a RUNNING state at a given time in the workgroup. | 

Athena publishes this metric with the following dimensions.


| Dimension | Description | 
| --- | --- | 
| None | The total DPUs consumed by Apache Spark version 3.5 workloads across all workgroups in the account. In the CloudWatch console, this metric appears under **AWS/Athena**, **Metrics with no dimensions**. This metric does not include sessions that use PySpark engine version 3. For those sessions, use the `DPUCount` metric in the `AmazonAthenaForApacheSpark` namespace. | 
| WorkGroup | The name of the workgroup. | 