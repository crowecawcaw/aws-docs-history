# Find interrupted Spot Instances

When you describe your EC2 instances, the results include your Spot Instances. The instance
lifecycle of a Spot Instance is `spot`. The instance state of a Spot Instance is either
`stopped` or `terminated`, depending on the interruption
behavior that you configured. For a hibernated Spot Instance, the instance state is
`stopped`.

For additional details about the reason for the interruption, check the Spot
request status code. For more information, see [Get the status of a Spot Instance request](spot-request-status.md "spot-request-status.md").

Console

###### To find an interrupted Spot Instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Apply the following filter: **Instance lifecycle=spot**.
4. Apply the **Instance state=stopped** or **Instance state=terminated**
   filter depending on the interruption behavior that you configured.
5. For each Spot Instance, on the **Details** tab, under
   **Instance details**, find **State transition message**.
   The following codes indicate that the Spot Instance was interrupted.
   - `Server.SpotInstanceShutdown`
   - `Server.SpotInstanceTermination`

AWS CLI

###### To find interrupted Spot Instances

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command with the `--filters` option. To list only the instance IDs
in the output, include the `--query` option.

If the interruption behavior is to terminate the Spot Instances, use the following example:

```
aws ec2 describe-instances \
    --filters Name=instance-lifecycle,Values=spot \
              Name=instance-state-name,Values=terminated \
              Name=state-reason-code,Values=Server.SpotInstanceTermination \
    --query "Reservations[*].Instances[*].InstanceId"
```

If the interruption behavior is to stop the Spot Instances, use the following example:

```
aws ec2 describe-instances \
    --filters Name=instance-lifecycle,Values=spot \
              Name=instance-state-name,Values=stopped \
              Name=state-reason-code,Values=Server.SpotInstanceShutdown \
    --query "Reservations[*].Instances[*].InstanceId"
```

PowerShell

###### To find interrupted Spot Instances

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

If the interruption behavior is to terminate the Spot Instances, use the following example:

```
(Get-EC2Instance `
    -Filter @{Key="instance-lifecycle"; Values="spot"} `
            @{Key="instance-state-name"; Values="terminated"} `
            @{Key="state-reason-code"; Values="Server.SpotInstanceTermination"}).Instances.InstanceId
```

If the interruption behavior is to stop the Spot Instances, use the following example:

```
(Get-EC2Instance `
    -Filter @{Key="instance-lifecycle"; Values="spot"} `
            @{Key="instance-state-name"; Values="stopped"} `
            @{Key="state-reason-code"; Values="Server.SpotInstanceTermination"}).Instances.InstanceId
```
