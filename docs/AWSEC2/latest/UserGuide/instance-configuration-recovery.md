# Configure simplified automatic recovery on

an Amazon EC2 instance

###### Important

This section describes how to proactively configure recovery mechanisms on an EC2
instance. These recovery mechanisms are designed to restore instance availability when AWS
detects an underlying hardware or software issue that causes a system status check to fail.
If you are currently experiencing problems accessing your instance, see [Troubleshoot EC2 instances](ec2-instance-troubleshoot.md "ec2-instance-troubleshoot.md").

If AWS detects that an instance is unavailable due to an underlying hardware or software
issue, _simplified automatic recovery_ can automatically
restore instance availability by moving the instance from the host with the underlying issue
to a different host.

If simplified automatic recovery occurs, AWS sends one of the following events to your
AWS Health Dashboard, depending on the outcome:

- Success event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS`
- Failure event: `AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE`
  To be notified of these events, you can configure notifications. For more information, see
  [Creating your first notification configuration in AWS User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md") in the
  _AWS User Notifications User Guide_. You can also use [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") to monitor
  simplified automatic recovery events.

Simplified automatic recovery is enabled by default on all supported instances during
instance launch. However, it can only operate if an instance is in the `running`
state, there are no service events listed in the AWS Health Dashboard, and there is available capacity
for the instance type. In some situations, such as significant outages, capacity constraints
might cause recovery attempts to fail. For more information, see [Troubleshoot
simplified automatic recovery failures](#ec2-instance-recover-simplified-auto-recovery-troubleshooting "#ec2-instance-recover-simplified-auto-recovery-troubleshooting").

You can disable simplified automatic recovery during or after launch, and re-enable it
later if required.

###### Warning

When AWS recovers your instance due to an underlying hardware or software issue, be
aware of the following consequences: data stored in volatile memory (RAM) will be lost and
the operating system’s uptime will start over from zero. To help protect against data loss,
we recommend that you regularly create backups of valuable data. For more information about
backup and recovery best practices for EC2 instances, see [Best practices for Amazon EC2](ec2-best-practices.md "ec2-best-practices.md").

Automatic instance recovery mechanisms are designed for _individual instances_. For guidance on building a resilient _system_, see [Build a resilient system](ec2-instance-recover.md#instance-recovery-build-a-resilient-system "ec2-instance-recover.md#instance-recovery-build-a-resilient-system").

###### Contents

- [Requirements for enabling
  simplified automatic recovery](#requirements-for-simplified-automatic-recovery "#requirements-for-simplified-automatic-recovery")
- [Configure simplified automatic recovery](#set-recovery-behavior "#set-recovery-behavior")
- [Troubleshoot
  simplified automatic recovery failures](#ec2-instance-recover-simplified-auto-recovery-troubleshooting "#ec2-instance-recover-simplified-auto-recovery-troubleshooting")

## Requirements for enabling

simplified automatic recovery

Simplified automatic recovery can be enabled on instances that meet the following
criteria:

**Instance types**

- **General purpose:** A1, M3, M4, M5, M5a, M5n, M5zn, M6a, M6g, M6i, M6in, M7a, M7g, M7i, M7i-flex, M8a, M8g, M8i, M8i-flex, T1, T2, T3, T3a, T4g
- **Compute optimized:** C3, C4, C5, C5a, C5n, C6a, C6g, C6gn, C6i, C6in, C7a, C7g, C7gn, C7i, C7i-flex, C8g, C8gn, C8i, C8i-flex
- **Memory optimized:** R3, R4, R5, R5a, R5b, R5n, R6a, R6g, R6i, R6in, R7a, R7g, R7i, R7iz, R8g, R8gb, R8gn, R8i, R8i-flex, U-3tb1, U-6tb1, U-9tb1, U-12tb1, U-18tb1, U-24tb1, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, U7inh-32tb, X1, X1e, X2iezn, X8g
- **Accelerated computing:** G3, G5g, Inf1, P3, VT1
- **High-performance computing:** Hpc6a, Hpc7a, Hpc7g

**Tenancy**

- Shared
- Dedicated Instance

For more information, see [Amazon EC2 Dedicated Instances](dedicated-instance.md "dedicated-instance.md").

**Limitations**

Simplified automatic recovery is not supported for instances with the following
characteristics:

- Instance size: `metal` instances
- Tenancy: Dedicated Host. For Dedicated Hosts, use [Dedicated Host Auto Recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md") instead.
- Storage: Instances with instance store volumes
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group
- Maintenance: Instances currently undergoing a scheduled maintenance event

## Configure simplified automatic recovery

Simplified automatic recovery is enabled by default when you launch a supported
instance. You can set the automatic recovery behavior to `disabled` during or
after launching the instance.

The `default` configuration doesn't enable simplified automatic recovery for
an unsupported instance.

Console

###### To disable simplified automatic recovery at launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and then choose
   **Launch instance**.
3. In the **Advanced details** section, for **Instance
   auto-recovery**, choose **Disabled**.
4. Configure the remaining instance launch settings as needed and then launch the
   instance.

###### To disable simplified automatic recovery after launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance, and then choose **Actions**,
   **Instance settings**, **Change auto-recovery
   behavior**.
4. Choose **Off**, and then choose
   **Save**.

###### To enable simplified automatic recovery after launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance, and then choose **Actions**,
   **Instance settings**, **Change auto-recovery
   behavior**.
4. Choose **Default (On)**, and then choose
   **Save**.

AWS CLI

###### To disable simplified automatic recovery at launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instance.md "../../../cli/latest/reference/ec2/run-instance.md")
command with the `--maintenance-options` option.

```
--maintenance-options AutoRecovery=Disabled
```

###### To disable simplified automatic recovery after launch

Use the [modify-instance-maintenance-options](../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md "../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md") command.

```
aws ec2 modify-instance-maintenance-options \
    --instance-id `i-1234567890abcdef0` \
    --auto-recovery disabled
```

###### To enable simplified automatic recovery after launch

Use the [modify-instance-maintenance-options](../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md "../../../cli/latest/reference/ec2/modify-instance-maintenance-options.md") command.

```
aws ec2 modify-instance-maintenance-options \
    --instance-id `i-1234567890abcdef0` \
    --auto-recovery default
```

PowerShell

###### To disable simplified automatic recovery at launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet.

```
-MaintenanceOptions_AutoRecovery Disabled
```

###### To disable simplified automatic recovery after launch

Use the [Edit-EC2InstanceMaintenanceOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md") cmdlet.

```
Edit-EC2InstanceMaintenanceOption `
    -InstanceId `i-1234567890abcdef0` `
    -AutoRecovery Disabled
```

###### To enable simplified automatic recovery after launch

Use the [Edit-EC2InstanceMaintenanceOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMaintenanceOption.md") cmdlet.

```
Edit-EC2InstanceMaintenanceOption `
    -InstanceId `i-1234567890abcdef0` `
    -AutoRecovery Enabled
```

## Troubleshoot

simplified automatic recovery failures

If simplified automatic recovery fails to recover your instance, consider the following
issues:

- AWS service events are running

Simplified automatic recovery does not operate during service events in the
AWS Health Dashboard. You might not receive recovery failure notifications for such events. For the
latest service availability information, see the [Service health](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") status
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
