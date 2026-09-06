

# Verify if automatic instance recovery occurred
<a name="verify-if-automatic-recovery-occurred"></a>

If your instance appears to have been offline and then unexpectedly rebooted, it might have undergone [automatic instance recovery](ec2-instance-recover.md#ec2-automatic-instance-recovery-key-concepts) in response to an underlying hardware or software issue. You can verify this by checking for automatic instance recovery events in your Health Dashboard. You can also check whether an underlying hardware or software issue was detected for your instance by checking the **StatusCheckFailed\_System** Amazon CloudWatch metric.

## Check for events in Health Dashboard
<a name="automatic-instance-recovery-events"></a>

When an automatic instance recovery attempt occurs, AWS sends events to your Health Dashboard. The specific event depends on the configured recovery mechanism and whether the attempt succeeded or failed.

**To check for automatic instance recovery events in the Health Dashboard**

1. Open the Health Dashboard at [https://phd.aws.amazon.com/phd/home\#/](https://phd.aws.amazon.com/phd/).

1. Look for the events associated with automatic instance recovery. The presence of these events can confirm whether an attempt at automatic instance recovery occurred and its outcome.
   + Simplified automatic recovery
     + Success event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS`
     + Failure event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE`
   + CloudWatch action based recovery
     + Success event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS`
     + Failure event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE`

## Monitor system status checks with CloudWatch
<a name="verify-an-underlying-hardware-issue"></a>

You can verify if an underlying hardware or software issue was detected for your instance by checking the [StatusCheckFailed\_System](viewing_metrics_with_cloudwatch.md#status-check-metrics) metric in CloudWatch. The metric value indicates whether a system status check passed (no hardware or software issue) or failed (hardware or software issue).

**To verify if an underlying hardware or software issue was detected**

1. Open the CloudWatch console **Metrics** page at [https://console.aws.amazon.com/cloudwatch/home?\#metricsV2](https://console.aws.amazon.com/cloudwatch/home?#metricsV2).

1. Verify that you're in the same Region as your EC2 instance.

1. Paste the following metric in the **Metrics** search field, and press Enter.

   ```
   StatusCheckFailed_System
   ```

1. Choose **EC2 > Per-Instance Metrics**.

1. In the table, select the check box next to the instance that you want to check.

1. Change the query period to the time that you suspect the recovery event occurred.

1. Choose the **Graphed metrics** tab, and for **StatusCheckFailed\_System**, do the following:

   1. For **Statistic**, choose either **Average**, **Maximum**, or **Minimum**.

   1. For **Period**, choose **1 minute**.

1. Check the value for **StatusCheckFailed\_System**.
   + Value of **0**: The system status check passed, indicating no underlying hardware or software issue.
   + Value of **1**: The system status check failed, indicating an underlying hardware or software issue.

For more information, see [Automatic instance recovery](ec2-instance-recover.md).