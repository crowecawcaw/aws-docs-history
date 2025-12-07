# EC2 instance bandwidth weighting configuration

Some instance types support configurable bandwidth weighting, where you can select
baseline bandwidth weighting that favors either network processing or EBS operations. Default
settings for baseline bandwidth are determined by your instance type. You can configure the
bandwidth weighting during launch, or modify your instance settings with the following
weighting preferences:

- **default** – This option uses the standard
  bandwidth configuration for your instance type.
- **vpc-1** – This option increases the baseline
  bandwidth available for networking and decreases the baseline bandwidth for EBS operations.
- **ebs-1** – This option increases the baseline
  bandwidth available for EBS operations, and decreases the baseline bandwidth for
  networking.

## Bandwidth weighting considerations

The following are some considerations that might affect your bandwidth weighting strategy.

- Setting bandwidth weighting preferences only affects bandwidth specifications. The
  network packets per second (PPS) and EBS input/output operations per second (IOPS)
  specifications don't change.
- The combined bandwidth specification
  between networking and EBS does not change. When you select a bandwidth weighting
  configuration, the baseline bandwidth available for the selected option increases, and
  the baseline bandwidth for the remaining option is reduced by the same absolute amount.
  For all instances except Flex instances, the available burst bandwidth remains the same for your selected option, and is reduced for the remaining option. For Flex instances up to 4xlarge, burst bandwidth remains unchanged. For Flex instances 8xlarge and larger, burst bandwidth increases by the same amount as the baseline bandwidth.
- It's important to understand how changes in bandwidth allocation can affect I/O
  performance for EBS. For EC2 instances that have `vpc-1` configuration
  (increased networking bandwidth), you might experience lower IOPS for EBS volumes
  if you reach the EBS bandwidth limit before you've reached the IOPS limit. This is
  more noticeable with larger I/O sizes.

For example, on an instance type that normally supports 240,000 IOPS with 16 KiB I/O size,
if you select `vpc-1` weighting, that might reduce the achievable IOPS due to the
adjusted EBS baseline bandwidth limit.

When planning your workload, consider your I/O size and patterns. Smaller I/O sizes are less
likely to be affected by bandwidth limitations, while larger I/O sizes or sequential workloads
might see more impact from bandwidth changes. Always test your specific workload to ensure
optimal performance with your chosen configuration.

- The networking multi-flow bandwidth specification for traffic that goes through an internet
  gateway or a local gateway is adjusted to 50% of the baseline bandwidth of the configured
  option or 5 Gbps, where applicable. For more information, see [Amazon EC2 instance network bandwidth](ec2-instance-network-bandwidth.md "ec2-instance-network-bandwidth.md").

The following example is based on an instance type that has a default baseline bandwidth of
40 Gbps, and a default border bandwidth of 20 Gbps. If you choose `vpc-1`
bandwidth weighting for this instance, the weighted baseline bandwidth changes to 50 Gbps,
and the border bandwidth changes to 25 Gbps.

- This feature is available in all commercial regions, aligned with EC2 instance availablilty and
  support.
- This feature adds no additional cost to your EC2 instance.

## Supported instance types for bandwidth weighting

Instance types in the following instance families support configurable bandwidth weighting.

- **General purpose:** M8a, M8g, M8gd, M8i, M8i-flex
- **Compute optimized:** C8a, C8g, C8gd, C8i, C8i-flex
- **Memory optimized:** R8a, R8g, R8gd, R8i, R8i-flex, X8g, X8aedz

## Check current bandwidth settings

To see the current bandwidth settings for your instance, select one of the tabs for
instructions.

Console

###### To get the bandwidth setting for an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance that you want to check from the list, and navigate
   to the **Networking** tab. Your current setting is shown in
   the **Configured bandwidth** field. Amazon EC2 uses default
   settings for your instance type if the bandwidth is not set to a specific
   value.

AWS CLI

###### To get the bandwidth setting for an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query Reservations[].Instances[].NetworkPerformanceOptions.BandwidthWeighting \
    --output text
```

The following is example output.

```
default
```

This example lists all of your instances that have the
bandwidth weighting preference set to `vpc-1`, for higher
networking bandwidth.

```
aws ec2 describe-instances \
    --filters "Name=network-performance-options.bandwidth-weighting,Values=vpc-1" \
    --query Reservations[].Instances[].InstanceId \
    --output text
```

PowerShell

###### To get the bandwidth setting for an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.NetworkPerformanceOptions.BandwidthWeighting.Value
```

The following is example output.

```
default
```

This example lists all of your instances that have the
bandwidth weighting preference set to `vpc-1`, for higher
networking bandwidth.

```
(Get-EC2Instance `
    -Filter @{Name="network-performance-options.bandwidth-weighting";Values="vpc-1"}).Instances.InstanceId
```

## Configure bandwidth weighting for your instance

You can configure bandwidth weighting either at launch or by modifying existing instances
from the EC2 console, API/SDKs or CLI.

### Configure bandwidth weighting when you launch an instance

To configure bandwidth settings when you launch an instance, select one of the tabs for
instructions.

You can also specify bandwidth weighting in a launch template. To create a
launch template, see [Create an Amazon EC2 launch template](create-launch-template.md "create-launch-template.md"). The parameter to set is in the same
location as it is for launching an instance directly from the console. Expand
the **Advanced details** section, and set the **Instance
bandwidth configuration**.

To launch an instance with your launch template, see
[Launch EC2 instances using a launch template](launch-instances-from-launch-template.md "launch-instances-from-launch-template.md").

Console

###### To launch an instance with configurable bandwidth weighting

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Choose **Launch instances**. This opens the
   **Launch an instance** dialog. There are several
   additional ways that you can get to the launch dialog, depending
   on your preference. For example, you can launch an instance directly
   from an AMI or from the Amazon EC2 dashboard itself.
4. The Amazon Machine Image (AMI) that you launch from must be based
   on `Arm` architecture. Many **Quick Start**
   images support both `x86` and `Arm` architectures,
   After you choose the operating system for your instance, select the
   `Arm` option from the **Architecture** list.
5. The instance type must be one of the [Supported instance types](#config-bw-support "#config-bw-support") for
   this feature.
6. When you expand the **Advanced details** section,
   you can scroll down to find the **Instance bandwidth configuration**
   settings. Select the bandwidth configuration option for your instance.
7. Configure all of the other settings for your instance as you
   normally would, and choose **Launch instance**.

AWS CLI

###### To launch an instance with configurable bandwidth weighting

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the following option to launch instances that are configured for
higher network bandwidth weighting.

```
--network-performance-options BandwidthWeighting=vpc-1
```

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the following option to launch instances that are configured for
higher EBS bandwidth weighting.

```
--network-performance-options BandwidthWeighting=ebs-1
```

PowerShell

###### To launch an instance with configurable bandwidth weighting

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the following parameter to launch instances that are configured
for higher network bandwidth weighting.

```
-NetworkPerformanceOptions_BandwidthWeighting vpc-1
```

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the following parameter to launch instances that are configured
for higher EBS bandwidth weighting.

```
-NetworkPerformanceOptions_BandwidthWeighting ebs-1
```

### Update bandwidth weighting for an existing instance

To update bandwidth weighting for an existing instance, your instance must be in the
`Stopped` state.

Console

###### To update bandwidth weighting

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance that you want to update from the list.
4. Before you change the bandwidth configuration, your instance must be
   in a `Stopped` state. If your instance is running, select
   **Stop instance** from the **Instance
   state** menu.
5. Choose **Manage bandwidth** from the
   **Actions > Networking** menu. This opens the
   **Manage bandwidth** dialog.

###### Note

If your instance type doesn't support configuration for bandwidth
weighting, that menu item is disabled. 6. Select the option to update your instance, and choose **Change**
to save your settings.

AWS CLI

###### To update bandwidth weighting

Use the [modify-instance-network-performance-options](../../../cli/latest/reference/ec2/modify-instance-network-performance-options.md "../../../cli/latest/reference/ec2/modify-instance-network-performance-options.md") command to configure
higher network bandwidth weighting for the specified instance.

```
aws ec2 modify-instance-network-performance-options \
    --instance-id `i-1234567890abcdef0` \
    --bandwidth-weighting=vpc-1
```

The following example configures higher EBS bandwidth weighting
for the specified instance.

```
aws ec2 modify-instance-network-performance-options \
    --instance-id `i-1234567890abcdef0` \
    --bandwidth-weighting=ebs-1
```

PowerShell

###### To update bandwidth weighting

Use the [Edit-EC2InstanceNetworkPerformanceOption](../../../powershell/latest/reference/items/Edit-EC2InstanceNetworkPerformanceOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceNetworkPerformanceOption.md")
cmdlet to configure higher network bandwidth weighting for the specified instance.

```
Edit-EC2InstanceNetworkPerformanceOption `
    -InstanceId `i-1234567890abcdef0` `
    -BandwidthWeighting vpc-1
```

The following example configures higher EBS bandwidth weighting
for the specified instance.

```
Edit-EC2InstanceNetworkPerformanceOption `
    -InstanceId `i-1234567890abcdef0` `
    -BandwidthWeighting ebs-1
```

## Networking performance

The following table shows the networking performance, in Gbps, that can be achieved with
the `default`, `vpc-1`, and `ebs-1` configurations.

| Instance type     | **`default`**(Baseline / Burst) | **`vpc-1`**(Baseline / Burst) | **`ebs-1`**(Baseline / Burst) |
| ----------------- | ------------------------------- | ----------------------------- | ----------------------------- |
| c8a.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.438 / 10.0                  |
| c8a.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| c8a.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| c8a.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| c8a.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| c8a.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| c8a.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| c8a.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| c8a.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| c8a.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| c8a.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| c8a.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| c8g.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| c8g.large         | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| c8g.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| c8g.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| c8g.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| c8g.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| c8g.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| c8g.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| c8g.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| c8g.48xlarge      | 50.0                            | 62.5                          | 40.0                          |
| c8g.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| c8g.metal-48xl    | 50.0                            | 62.5                          | 40.0                          |
| c8gd.medium       | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| c8gd.large        | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| c8gd.xlarge       | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| c8gd.2xlarge      | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| c8gd.4xlarge      | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| c8gd.8xlarge      | 15.0                            | 18.75                         | 12.5                          |
| c8gd.12xlarge     | 22.5                            | 28.125                        | 18.75                         |
| c8gd.16xlarge     | 30.0                            | 37.5                          | 25.0                          |
| c8gd.24xlarge     | 40.0                            | 50.0                          | 32.5                          |
| c8gd.48xlarge     | 50.0                            | 62.5                          | 40.0                          |
| c8gd.metal-24xl   | 40.0                            | 50.0                          | 32.5                          |
| c8gd.metal-48xl   | 50.0                            | 62.5                          | 40.0                          |
| c8i.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| c8i.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| c8i.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| c8i.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| c8i.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| c8i.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| c8i.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| c8i.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| c8i.32xlarge      | 50.0                            | 62.5                          | 40.0                          |
| c8i.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| c8i.96xlarge      | 100.0                           | 125.0                         | 80.0                          |
| c8i.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| c8i.metal-96xl    | 100.0                           | 125.0                         | 80.0                          |
| c8i-flex.large    | 0.468 / 12.5                    | 0.585 / 12.5                  | 0.389 / 10.0                  |
| c8i-flex.xlarge   | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.779 / 10.0                  |
| c8i-flex.2xlarge  | 1.875 / 15.0                    | 2.344 / 15.0                  | 1.562 / 12.5                  |
| c8i-flex.4xlarge  | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| c8i-flex.8xlarge  | 7.5 / 15.0                      | 9.375 / 18.75                 | 6.25 / 12.5                   |
| c8i-flex.12xlarge | 11.25 / 22.5                    | 14.063 / 28.125               | 9.375 / 18.75                 |
| c8i-flex.16xlarge | 15.0 / 30.0                     | 18.75 / 37.5                  | 12.5 / 25.0                   |
| m8a.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.438 / 10.0                  |
| m8a.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| m8a.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| m8a.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| m8a.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| m8a.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| m8a.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| m8a.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| m8a.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| m8a.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| m8a.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| m8a.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| m8g.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| m8g.large         | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| m8g.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| m8g.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| m8g.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| m8g.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| m8g.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| m8g.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| m8g.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| m8g.48xlarge      | 50.0                            | 62.5                          | 40.0                          |
| m8g.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| m8g.metal-48xl    | 50.0                            | 62.5                          | 40.0                          |
| m8gd.medium       | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| m8gd.large        | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| m8gd.xlarge       | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| m8gd.2xlarge      | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| m8gd.4xlarge      | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| m8gd.8xlarge      | 15.0                            | 18.75                         | 12.5                          |
| m8gd.12xlarge     | 22.5                            | 28.125                        | 18.75                         |
| m8gd.16xlarge     | 30.0                            | 37.5                          | 25.0                          |
| m8gd.24xlarge     | 40.0                            | 50.0                          | 32.5                          |
| m8gd.48xlarge     | 50.0                            | 62.5                          | 40.0                          |
| m8gd.metal-24xl   | 40.0                            | 50.0                          | 32.5                          |
| m8gd.metal-48xl   | 50.0                            | 62.5                          | 40.0                          |
| m8i.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| m8i.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| m8i.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| m8i.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| m8i.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| m8i.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| m8i.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| m8i.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| m8i.32xlarge      | 50.0                            | 62.5                          | 40.0                          |
| m8i.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| m8i.96xlarge      | 100.0                           | 125.0                         | 80.0                          |
| m8i.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| m8i.metal-96xl    | 100.0                           | 125.0                         | 80.0                          |
| m8i-flex.large    | 0.468 / 12.5                    | 0.585 / 12.5                  | 0.389 / 10.0                  |
| m8i-flex.xlarge   | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.779 / 10.0                  |
| m8i-flex.2xlarge  | 1.875 / 15.0                    | 2.344 / 15.0                  | 1.562 / 12.5                  |
| m8i-flex.4xlarge  | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| m8i-flex.8xlarge  | 7.5 / 15.0                      | 9.375 / 18.75                 | 6.25 / 12.5                   |
| m8i-flex.12xlarge | 11.25 / 22.5                    | 14.063 / 28.125               | 9.375 / 18.75                 |
| m8i-flex.16xlarge | 15.0 / 30.0                     | 18.75 / 37.5                  | 12.5 / 25.0                   |
| r8a.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.438 / 10.0                  |
| r8a.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| r8a.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| r8a.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| r8a.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| r8a.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| r8a.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| r8a.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| r8a.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| r8a.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| r8a.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| r8a.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| r8g.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| r8g.large         | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| r8g.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| r8g.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| r8g.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| r8g.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| r8g.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| r8g.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| r8g.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| r8g.48xlarge      | 50.0                            | 62.5                          | 40.0                          |
| r8g.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| r8g.metal-48xl    | 50.0                            | 62.5                          | 40.0                          |
| r8gd.medium       | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| r8gd.large        | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| r8gd.xlarge       | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| r8gd.2xlarge      | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| r8gd.4xlarge      | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| r8gd.8xlarge      | 15.0                            | 18.75                         | 12.5                          |
| r8gd.12xlarge     | 22.5                            | 28.125                        | 18.75                         |
| r8gd.16xlarge     | 30.0                            | 37.5                          | 25.0                          |
| r8gd.24xlarge     | 40.0                            | 50.0                          | 32.5                          |
| r8gd.48xlarge     | 50.0                            | 62.5                          | 40.0                          |
| r8gd.metal-24xl   | 40.0                            | 50.0                          | 32.5                          |
| r8gd.metal-48xl   | 50.0                            | 62.5                          | 40.0                          |
| r8i.large         | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.774 / 10.0                  |
| r8i.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| r8i.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| r8i.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| r8i.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| r8i.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| r8i.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| r8i.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| r8i.32xlarge      | 50.0                            | 62.5                          | 40.0                          |
| r8i.48xlarge      | 75.0                            | 93.75                         | 60.0                          |
| r8i.96xlarge      | 100.0                           | 125.0                         | 80.0                          |
| r8i.metal-48xl    | 75.0                            | 93.75                         | 60.0                          |
| r8i.metal-96xl    | 100.0                           | 125.0                         | 80.0                          |
| r8i-flex.large    | 0.468 / 12.5                    | 0.585 / 12.5                  | 0.389 / 10.0                  |
| r8i-flex.xlarge   | 0.937 / 12.5                    | 1.172 / 12.5                  | 0.779 / 10.0                  |
| r8i-flex.2xlarge  | 1.875 / 15.0                    | 2.344 / 15.0                  | 1.562 / 12.5                  |
| r8i-flex.4xlarge  | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| r8i-flex.8xlarge  | 7.5 / 15.0                      | 9.375 / 18.75                 | 6.25 / 12.5                   |
| r8i-flex.12xlarge | 11.25 / 22.5                    | 14.063 / 28.125               | 9.375 / 18.75                 |
| r8i-flex.16xlarge | 15.0 / 30.0                     | 18.75 / 37.5                  | 12.5 / 25.0                   |
| x8g.medium        | 0.52 / 12.5                     | 0.65 / 12.5                   | 0.441 / 10.0                  |
| x8g.large         | 0.937 / 12.5                    | 1.171 / 12.5                  | 0.779 / 10.0                  |
| x8g.xlarge        | 1.875 / 12.5                    | 2.344 / 12.5                  | 1.562 / 10.0                  |
| x8g.2xlarge       | 3.75 / 15.0                     | 4.688 / 15.0                  | 3.125 / 12.5                  |
| x8g.4xlarge       | 7.5 / 15.0                      | 9.375 / 15.0                  | 6.25 / 12.5                   |
| x8g.8xlarge       | 15.0                            | 18.75                         | 12.5                          |
| x8g.12xlarge      | 22.5                            | 28.125                        | 18.75                         |
| x8g.16xlarge      | 30.0                            | 37.5                          | 25.0                          |
| x8g.24xlarge      | 40.0                            | 50.0                          | 32.5                          |
| x8g.48xlarge      | 50.0                            | 62.5                          | 40.0                          |
| x8g.metal-24xl    | 40.0                            | 50.0                          | 32.5                          |
| x8g.metal-48xl    | 50.0                            | 62.5                          | 40.0                          |
| x8aedz.large      | 1.562 / 18.75                   | 1.953 / 18.75                 | 1.249 / 15.0                  |
| x8aedz.xlarge     | 3.125 / 18.75                   | 3.907 / 18.75                 | 2.5 / 15.0                    |
| x8aedz.3xlarge    | 9.375 / 18.75                   | 11.719 / 18.75                | 7.5 / 15.0                    |
| x8aedz.6xlarge    | 18.75                           | 23.438                        | 15.0                          |
| x8aedz.12xlarge   | 37.5                            | 46.875                        | 30.0                          |
| x8aedz.24xlarge   | 75.0                            | 93.75                         | 60.0                          |
| x8aedz.metal-12xl | 37.5                            | 46.875                        | 30.0                          |
| x8aedz.metal-24xl | 75.0                            | 93.75                         | 60.0                          |

## Amazon EBS performance

The following table shows the Amazon EBS performance, in Gbps, that can be achieved with
the `default`, `vpc-1`, and `ebs-1` configurations.

| Instance type     | **`default`**(Baseline / Burst) | **`vpc-1`**(Baseline / Burst) | **`ebs-1`**(Baseline / Burst) |
| ----------------- | ------------------------------- | ----------------------------- | ----------------------------- |
| c8a.medium        | 0.325 / 10.0                    | 0.195 / 6.25                  | 0.407 / 10.0                  |
| c8a.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| c8a.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| c8a.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| c8a.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| c8a.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| c8a.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| c8a.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| c8a.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| c8a.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| c8a.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| c8a.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| c8g.medium        | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| c8g.large         | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| c8g.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| c8g.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| c8g.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| c8g.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| c8g.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| c8g.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| c8g.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| c8g.48xlarge      | 40.0                            | 27.5                          | 50.0                          |
| c8g.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| c8g.metal-48xl    | 40.0                            | 27.5                          | 50.0                          |
| c8gd.medium       | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| c8gd.large        | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| c8gd.xlarge       | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| c8gd.2xlarge      | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| c8gd.4xlarge      | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| c8gd.8xlarge      | 10.0                            | 6.25                          | 12.5                          |
| c8gd.12xlarge     | 15.0                            | 9.375                         | 18.75                         |
| c8gd.16xlarge     | 20.0                            | 12.5                          | 25.0                          |
| c8gd.24xlarge     | 30.0                            | 20.0                          | 37.5                          |
| c8gd.48xlarge     | 40.0                            | 27.5                          | 50.0                          |
| c8gd.metal-24xl   | 30.0                            | 20.0                          | 37.5                          |
| c8gd.metal-48xl   | 40.0                            | 27.5                          | 50.0                          |
| c8i.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| c8i.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| c8i.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| c8i.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| c8i.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| c8i.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| c8i.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| c8i.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| c8i.32xlarge      | 40.0                            | 27.5                          | 50.0                          |
| c8i.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| c8i.96xlarge      | 80.0                            | 55.0                          | 100.0                         |
| c8i.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| c8i.metal-96xl    | 80.0                            | 55.0                          | 100.0                         |
| c8i-flex.large    | 0.315 / 10.0                    | 0.198 / 6.25                  | 0.394 / 10.0                  |
| c8i-flex.xlarge   | 0.63 / 10.0                     | 0.395 / 6.25                  | 0.788 / 10.0                  |
| c8i-flex.2xlarge  | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| c8i-flex.4xlarge  | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| c8i-flex.8xlarge  | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 12.5                   |
| c8i-flex.12xlarge | 7.5 / 15.0                      | 4.687 / 9.375                 | 9.375 / 18.75                 |
| c8i-flex.16xlarge | 10.0 / 20.0                     | 6.25 / 12.5                   | 12.5 / 25.0                   |
| m8a.medium        | 0.325 / 10.0                    | 0.195 / 6.25                  | 0.407 / 10.0                  |
| m8a.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| m8a.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| m8a.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| m8a.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| m8a.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| m8a.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| m8a.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| m8a.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| m8a.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| m8a.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| m8a.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| m8g.medium        | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| m8g.large         | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| m8g.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| m8g.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| m8g.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| m8g.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| m8g.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| m8g.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| m8g.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| m8g.48xlarge      | 40.0                            | 27.5                          | 50.0                          |
| m8g.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| m8g.metal-48xl    | 40.0                            | 27.5                          | 50.0                          |
| m8gd.medium       | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| m8gd.large        | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| m8gd.xlarge       | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| m8gd.2xlarge      | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| m8gd.4xlarge      | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| m8gd.8xlarge      | 10.0                            | 6.25                          | 12.5                          |
| m8gd.12xlarge     | 15.0                            | 9.375                         | 18.75                         |
| m8gd.16xlarge     | 20.0                            | 12.5                          | 25.0                          |
| m8gd.24xlarge     | 30.0                            | 20.0                          | 37.5                          |
| m8gd.48xlarge     | 40.0                            | 27.5                          | 50.0                          |
| m8gd.metal-24xl   | 30.0                            | 20.0                          | 37.5                          |
| m8gd.metal-48xl   | 40.0                            | 27.5                          | 50.0                          |
| m8i.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| m8i.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| m8i.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| m8i.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| m8i.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| m8i.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| m8i.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| m8i.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| m8i.32xlarge      | 40.0                            | 27.5                          | 50.0                          |
| m8i.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| m8i.96xlarge      | 80.0                            | 55.0                          | 100.0                         |
| m8i.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| m8i.metal-96xl    | 80.0                            | 55.0                          | 100.0                         |
| m8i-flex.large    | 0.315 / 10.0                    | 0.198 / 6.25                  | 0.394 / 10.0                  |
| m8i-flex.xlarge   | 0.63 / 10.0                     | 0.395 / 6.25                  | 0.788 / 10.0                  |
| m8i-flex.2xlarge  | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| m8i-flex.4xlarge  | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| m8i-flex.8xlarge  | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 12.5                   |
| m8i-flex.12xlarge | 7.5 / 15.0                      | 4.687 / 9.375                 | 9.375 / 18.75                 |
| m8i-flex.16xlarge | 10.0 / 20.0                     | 6.25 / 12.5                   | 12.5 / 25.0                   |
| r8a.medium        | 0.325 / 10.0                    | 0.195 / 6.25                  | 0.407 / 10.0                  |
| r8a.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| r8a.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| r8a.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| r8a.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| r8a.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| r8a.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| r8a.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| r8a.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| r8a.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| r8a.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| r8a.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| r8g.medium        | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| r8g.large         | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| r8g.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| r8g.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| r8g.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| r8g.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| r8g.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| r8g.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| r8g.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| r8g.48xlarge      | 40.0                            | 27.5                          | 50.0                          |
| r8g.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| r8g.metal-48xl    | 40.0                            | 27.5                          | 50.0                          |
| r8gd.medium       | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| r8gd.large        | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| r8gd.xlarge       | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| r8gd.2xlarge      | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| r8gd.4xlarge      | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| r8gd.8xlarge      | 10.0                            | 6.25                          | 12.5                          |
| r8gd.12xlarge     | 15.0                            | 9.375                         | 18.75                         |
| r8gd.16xlarge     | 20.0                            | 12.5                          | 25.0                          |
| r8gd.24xlarge     | 30.0                            | 20.0                          | 37.5                          |
| r8gd.48xlarge     | 40.0                            | 27.5                          | 50.0                          |
| r8gd.metal-24xl   | 30.0                            | 20.0                          | 37.5                          |
| r8gd.metal-48xl   | 40.0                            | 27.5                          | 50.0                          |
| r8i.large         | 0.65 / 10.0                     | 0.415 / 6.25                  | 0.813 / 10.0                  |
| r8i.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| r8i.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| r8i.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| r8i.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| r8i.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| r8i.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| r8i.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| r8i.32xlarge      | 40.0                            | 27.5                          | 50.0                          |
| r8i.48xlarge      | 60.0                            | 41.25                         | 75.0                          |
| r8i.96xlarge      | 80.0                            | 55.0                          | 100.0                         |
| r8i.metal-48xl    | 60.0                            | 41.25                         | 75.0                          |
| r8i.metal-96xl    | 80.0                            | 55.0                          | 100.0                         |
| r8i-flex.large    | 0.315 / 10.0                    | 0.198 / 6.25                  | 0.394 / 10.0                  |
| r8i-flex.xlarge   | 0.63 / 10.0                     | 0.395 / 6.25                  | 0.788 / 10.0                  |
| r8i-flex.2xlarge  | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| r8i-flex.4xlarge  | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| r8i-flex.8xlarge  | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 12.5                   |
| r8i-flex.12xlarge | 7.5 / 15.0                      | 4.687 / 9.375                 | 9.375 / 18.75                 |
| r8i-flex.16xlarge | 10.0 / 20.0                     | 6.25 / 12.5                   | 12.5 / 25.0                   |
| x8g.medium        | 0.315 / 10.0                    | 0.185 / 6.25                  | 0.394 / 10.0                  |
| x8g.large         | 0.63 / 10.0                     | 0.396 / 6.25                  | 0.788 / 10.0                  |
| x8g.xlarge        | 1.25 / 10.0                     | 0.781 / 6.25                  | 1.563 / 10.0                  |
| x8g.2xlarge       | 2.5 / 10.0                      | 1.562 / 6.25                  | 3.125 / 10.0                  |
| x8g.4xlarge       | 5.0 / 10.0                      | 3.125 / 6.25                  | 6.25 / 10.0                   |
| x8g.8xlarge       | 10.0                            | 6.25                          | 12.5                          |
| x8g.12xlarge      | 15.0                            | 9.375                         | 18.75                         |
| x8g.16xlarge      | 20.0                            | 12.5                          | 25.0                          |
| x8g.24xlarge      | 30.0                            | 20.0                          | 37.5                          |
| x8g.48xlarge      | 40.0                            | 27.5                          | 50.0                          |
| x8g.metal-24xl    | 30.0                            | 20.0                          | 37.5                          |
| x8g.metal-48xl    | 40.0                            | 27.5                          | 50.0                          |
| x8aedz.large      | 1.25 / 15.0                     | 0.859 / 10.312                | 1.563 / 15.0                  |
| x8aedz.xlarge     | 2.5 / 15.0                      | 1.718 / 10.312                | 3.125 / 15.0                  |
| x8aedz.3xlarge    | 7.5 / 15.0                      | 5.156 / 10.312                | 9.375 / 15.0                  |
| x8aedz.6xlarge    | 15.0                            | 10.312                        | 18.75                         |
| x8aedz.12xlarge   | 30.0                            | 20.625                        | 37.5                          |
| x8aedz.24xlarge   | 60.0                            | 41.25                         | 75.0                          |
| x8aedz.metal-12xl | 30.0                            | 20.625                        | 37.5                          |
| x8aedz.metal-24xl | 60.0                            | 41.25                         | 75.0                          |
