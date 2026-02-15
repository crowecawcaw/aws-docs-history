# Configure CloudWatch action based recovery on an EC2 instance

###### Important

This section describes how to proactively configure recovery mechanisms on an EC2
instance. These recovery mechanisms are designed to restore instance availability when AWS
detects an underlying hardware or software issue that causes a system status check to fail.
If you are currently experiencing problems accessing your instance, see [Troubleshoot EC2 instances](ec2-instance-troubleshoot.md "ec2-instance-troubleshoot.md").

If AWS detects that an instance is unavailable due to an underlying hardware or software
issue, _CloudWatch action based recovery_ can automatically restore
instance availability by moving the instance from the host with the underlying issue to a
different host.

If CloudWatch action based recovery occurs, AWS sends one of the following events to your
AWS Health Dashboard, depending on the outcome:

- Success event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS`
- Failure event: `AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE`
  You can configure CloudWatch action based recovery to add recovery actions to Amazon CloudWatch alarms.
  CloudWatch action based recovery works with the `StatusCheckFailed_System` metric. CloudWatch
  action based recovery provides to-the-minute recovery response time granularity and Amazon Simple Notification Service
  (Amazon SNS) notifications of recovery actions and outcomes. These configuration options allow for
  faster recovery attempts with more granular control over the system status check failure event
  response compared to simplified automatic recovery. For more information about available CloudWatch
  options, see [Status checks for your
  instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md").

However, CloudWatch action based recovery can only operate if an instance is in the
`running` state, there are no service events listed in the AWS Health Dashboard, and there
is available capacity for the instance type. In some situations, such as significant outages,
capacity constraints might cause recovery attempts to fail. For more information, see [Troubleshoot CloudWatch action
based recovery failures](#ec2-instance-recover-cloudwatch-troubleshooting "#ec2-instance-recover-cloudwatch-troubleshooting").

###### Warning

When AWS recovers your instance due to an underlying hardware or software issue, be
aware of the following consequences: data stored in volatile memory (RAM) and on instance
store volumes will be lost, and the operating system’s uptime will start over from zero. To
help protect against data loss, we recommend that you regularly create backups of valuable
data. For more information about backup and recovery best practices for EC2 instances, see
[Best practices for Amazon EC2](ec2-best-practices.md "ec2-best-practices.md").

Automatic instance recovery mechanisms are designed for _individual instances_. For guidance on building a resilient _system_, see [Build a resilient system](ec2-instance-recover.md#instance-recovery-build-a-resilient-system "ec2-instance-recover.md#instance-recovery-build-a-resilient-system").

###### Contents

- [Requirements for
  enabling CloudWatch action based recovery](#requirements-for-cloudwatch-action-based-recovery "#requirements-for-cloudwatch-action-based-recovery")
- [Configure CloudWatch action based
  recovery](#ec2-instance-recover-cloudwatch-configure "#ec2-instance-recover-cloudwatch-configure")
- [Troubleshoot CloudWatch action
  based recovery failures](#ec2-instance-recover-cloudwatch-troubleshooting "#ec2-instance-recover-cloudwatch-troubleshooting")

## Requirements for

enabling CloudWatch action based recovery

CloudWatch action based recovery can be enabled on instances that meet the following
criteria:

**Instance types**

- **General purpose:** A1, M3, M4, M5, M5a, M5n, M5zn, M6a, M6g, M6i, M6in, M7a, M7g, M7i, M7i-flex, M8a, M8azn, M8g, M8gb, M8gn, M8i, M8i-flex, T1, T2, T3, T3a, T4g
- **Compute optimized:** C3, C4, C5, C5a, C5n, C6a, C6g, C6gn, C6i, C6in, C7a, C7g, C7gn, C7i, C7i-flex, C8a, C8g, C8gb, C8gn, C8i, C8i-flex
- **Memory optimized:** R3, R4, R5, R5a, R5b, R5n, R6a, R6g, R6i, R6in, R7a, R7g, R7i, R7iz, R8a, R8g, R8gb, R8gn, R8i, R8i-flex, U-3tb1, U-6tb1, U-9tb1, U-12tb1, U-18tb1, U-24tb1, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, U7inh-32tb, X1, X1e, X2idn, X2iedn, X2iezn, X8g, X8i
- **Accelerated computing:** G3, G5g, Inf1, P3, VT1
- **High-performance computing:** Hpc6a, Hpc7a, Hpc7g
- **Metal instances:** Any of the above instance types with the metal instance size.
- **If instance store volumes are added at
  launch:** Then only the following instance types are supported: M3, C3,
  R3, X1, X1e, X2idn, X2iedn

**Tenancy**

- Shared
- Dedicated Instance

For more information, see [Amazon EC2 Dedicated Instances](dedicated-instance.md "dedicated-instance.md").

**Limitations**

CloudWatch action based recovery is not supported for instances with the following
characteristics:

- Tenancy: Dedicated Host. For Dedicated Hosts, use [Dedicated Host Auto Recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md") instead.
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group
- Maintenance: Instances currently undergoing a scheduled maintenance event

### Find a supported instance type

You can view the instance types that support CloudWatch action based recovery.

Console

###### To view the instance types that support CloudWatch action based recovery

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose **Instance Types**.
3. In the filter bar, add the filter **Auto Recovery support = true**.
   The **Instance types** table displays all the instance types
   that support CloudWatch action based recovery.
4. (Optional) Add filters to further scope to specific instance types of interest.

AWS CLI

###### To view the instance types that support CloudWatch action based recovery

Use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command with the
`auto-recovery-supported` filter.

```
aws ec2 describe-instance-types \
    --filters Name=auto-recovery-supported,Values=true \
    --query "InstanceTypes[*].[InstanceType]" \
    --output text | sort
```

PowerShell

###### To view the instance types that support CloudWatch action based recovery

Use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md")
cmdlet with the `auto-recovery-supported` filter.

```
Get-EC2InstanceType `
    -Filter @{Name="auto-recovery-supported";Values="true"} | `
    Select InstanceType | Sort-Object InstanceType
```

## Configure CloudWatch action based

recovery

To configure CloudWatch action based recovery for an EC2 instance, create a CloudWatch alarm that
monitors the `StatusCheckFailed_System` metric for the specified instance. Set
the alarm to trigger when the metric value is **1**, indicating a failed
system status check. Configure the alarm action to automatically recover the instance when
triggered.

You can configure the alarm using either the Amazon EC2 console or the CloudWatch console. For the
instructions, see [Add recover actions to Amazon CloudWatch alarms](UsingAlarmActions.md#AddingRecoverActions "UsingAlarmActions.md#AddingRecoverActions") in this user guide, or [Adding recover actions to Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md#AddingRecoverActions "../../../AmazonCloudWatch/latest/monitoring/UsingAlarmActions.md#AddingRecoverActions") in the _Amazon CloudWatch User
Guide_.

## Troubleshoot CloudWatch action

based recovery failures

If CloudWatch action based recovery fails to recover your instance, consider the following
issues:

- AWS service events are running

CloudWatch action based recovery does not operate during service events in the AWS Health Dashboard.
You might not receive recovery failure notifications for such events. For the latest
service availability information, see the [Service health](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") status
page.

- Insufficient capacity

There is temporarily insufficient replacement hardware to migrate the
instance.

- Maximum daily recovery attempts reached

The instance has reached the maximum daily allowance for recovery attempts. Your
instance might subsequently be retired if automatic recovery fails and a hardware
degradation is determined to be the root cause of the original failed system status
check.

If the instance’s system status check failure persists despite multiple recovery
attempts, see [Troubleshoot instances with failed
status checks](TroubleshootingInstances.md "TroubleshootingInstances.md") for additional guidance.
