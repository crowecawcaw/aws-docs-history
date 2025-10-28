# Start a hibernated Amazon EC2 instance

Start a hibernated instance by starting it in the same way that you would start a
stopped instance.

For Spot Instances, if Amazon EC2 hibernated the instance, then only Amazon EC2 can resume it. You
can only resume a hibernated Spot Instance if _you_
hibernated it. Spot Instances can only be resumed if capacity is available and the Spot price
is less than or equal to your specified maximum price.

Console

###### To start a hibernated instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select a hibernated instance, and choose **Instance
   state**, **Start instance**. It can
   take a few minutes for the instance to enter the
   `running` state. During this time, the instance [status checks](monitoring-system-instance-status-check.md#types-of-instance-status-checks "monitoring-system-instance-status-check.md#types-of-instance-status-checks")
   show the instance in a failed state until the instance has
   started.

AWS CLI

###### To start a hibernated instance

Use the [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") command.

```
aws ec2 start-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To start a hibernated instance

Use the [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") cmdlet.

```
Start-EC2Instance -InstanceId `i-1234567890abcdef0`
```
