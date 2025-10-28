# Hibernate an Amazon EC2 instance

You can initiate hibernation on an On-Demand Instance or Spot Instance if the instance is an EBS-backed
instance, is [enabled for hibernation](enabling-hibernation.md "enabling-hibernation.md"), and
meets the [hibernation prerequisites](hibernating-prerequisites.md "hibernating-prerequisites.md"). If
an instance cannot hibernate successfully, a normal shutdown occurs.

Console

###### To hibernate an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select an instance, and choose **Instance
   state**, **Hibernate instance**. If
   **Hibernate instance** is disabled, the
   instance is already hibernated or stopped, or it can't be
   hibernated. For more information, see [Prerequisites for EC2 instance hibernation](hibernating-prerequisites.md "hibernating-prerequisites.md").
4. When prompted for confirmation, choose
   **Hibernate**. It can take a few minutes for
   the instance to hibernate. The instance state first changes to
   **Stopping**, and then changes to
   **Stopped** when the instance has
   hibernated.

AWS CLI

###### To hibernate an instance

Use the [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") command and specify the
`--hibernate` parameter.

```
aws ec2 stop-instances \
    --instance-ids `i-1234567890abcdef0` \
    --hibernate
```

PowerShell

###### To hibernate an instance

Use the [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") cmdlet.

```
Stop-EC2Instance `
    -InstanceId `i-1234567890abcdef0` `
    -Hibernate $true
```

You can check whether hibernation was initiated on an instance.

Console

###### To view if hibernation was initiated on an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance and, on the **Details** tab,
   in the **Instance details** section, check the
   value for **State transition message**.

**Client.UserInitiatedHibernate: User initiated
hibernate** indicates that you initiated hibernation on
the On-Demand Instance or Spot Instance.

AWS CLI

###### To view if hibernation was initiated on an instance

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command and specify the
`state-reason-code` filter to see the instances on which
hibernation was initiated.

```
aws ec2 describe-instances \
    --filters "Name=state-reason-code,Values=Client.UserInitiatedHibernate"
```

The following field in the output indicates that hibernation was initiated
on the On-Demand Instance or Spot Instance.

```
"StateReason": {
    "Code": "Client.UserInitiatedHibernate"
}
```

PowerShell

###### To view if hibernation was initiated on an instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md") cmdlet and specify the
`state-reason-code` filter to see the instances on which
hibernation was initiated.

```
Get-EC2Instance `
    -Filter @{Name="state-reason-code";Value="Client.UserInitiatedHibernate"}
```
