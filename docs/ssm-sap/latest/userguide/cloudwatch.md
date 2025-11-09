# AWS Systems Manager for SAP metrics with Amazon CloudWatch

You can view CloudTrail metrics for AWS Systems Manager for SAP via AWS Management Console or AWS CLI.

AWS Management Console
Metrics are grouped first by the service namespace, and then by the various dimension combination within each namespace. Use the following steps to view the metrics in AWS Management Console.

1. Open [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, select **Metrics**.
3. In namespace, select **AWS/SSMForSAP**.

AWS Command Line Interface
Use the following command to view the metrics via AWS CLI.

```
aws cloudwatch list-metrics --namespace "AWS/SSMForSAP"
```

**The following are all the metrics available to you.**

|                    |                |           |                            |
| ------------------ | -------------- | --------- | -------------------------- |
| **Metric**         | **Dimensions** | **Units** | **Description**            |
| OperationStarted   | OperationType  | Count     | An operation is started.   |
| OperationSucceeded | OperationType  | Count     | An operation is succeeded. |
| OperationFailed    | OperationType  | Count     | An operation is failed.    |

**Usage Metrics**

AWS Systems Manager for SAP provides resource usage metrics in the **AWS/Usage** namespace. For more information, see [AWS usage metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md").
