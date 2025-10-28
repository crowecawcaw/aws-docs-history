# Manage your Spot Instances

Amazon EC2 launches a Spot Instance when capacity is available. A Spot Instance runs until it is interrupted or
you terminate it yourself.

###### Contents

- [Find your Spot Instances](#using-spot-instances-running "#using-spot-instances-running")
- [Find instances launched by a specific request](#find-request-spot-instances "#find-request-spot-instances")
- [Stop a Spot Instance](#stopping-a-spot-instance "#stopping-a-spot-instance")
- [Start a Spot Instance](#starting-a-spot-instance "#starting-a-spot-instance")
- [Terminate a Spot Instance](#terminating-a-spot-instance "#terminating-a-spot-instance")

## Find your Spot Instances

A Spot Instance appears in the **Instances** page in the console,
along with On-Demand Instances. Use the following procedure to find your Spot Instances.

Console

###### To find your Spot Instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. To find all Spot Instances, in the search pane, choose **Instance lifecycle=spot**.
4. To verify that an instance is a Spot Instance, select the instance, choose the
   **Details** tab, and check the value of **Lifecycle**.
   The value for a Spot Instance is `spot` and the value for an On-Demand Instance is `normal`.

AWS CLI

###### To find your Spot Instances

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command.

```
aws ec2 describe-instances --filters "Name=instance-lifecycle,Values=spot"
```

###### To determine whether an instance is a Spot Instance

Use the following [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query "Reservations[*].Instances[*].InstanceLifecycle" \
    --output text
```

If the output is `spot`, the instance is a Spot Instance. If there is no output,
the instance is an On-Demand Instance.

PowerShell

###### To find your Spot Instances

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
Get-EC2Instance -Filter @{Name="instance-lifecycle"; Values="spot"}
```

###### To determine whether an instance is a Spot Instance

Use the [Get-EC2Instance](../../../powershell/latest/reference/items/Get-EC2Instance.md "../../../powershell/latest/reference/items/Get-EC2Instance.md")
cmdlet.

```
(Get-EC2Instance -InstanceId `i-1234567890abcdef0`).Instances.InstanceLifecycle
```

If the output is `Spot`, the instance is a Spot Instance. If there is no output,
the instance is an On-Demand Instance.

## Find instances launched by a specific request

Use the following procedure to find the Spot Instances launched from a specific Spot Instance or Spot Fleet request.

Console

###### To find the Spot Instances for a request

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
   The list contains both Spot Instance requests and Spot Fleet requests.
3. If a Spot Instance request is fulfilled,
   **Capacity** is the ID of the Spot Instance. For a Spot Fleet,
   **Capacity** indicates how much of the requested
   capacity has been fulfilled. To view the IDs of the instances in a Spot Fleet,
   choose the expand arrow, or select the fleet and choose
   **Instances**.
4. For a Spot Fleet, **Capacity** indicates how much of the requested
   capacity is fulfilled. To view the IDs of the instances in a Spot Fleet,
   choose the fleet ID to open its details page and locate the
   **Instances** pane.

AWS CLI

###### To find the Spot Instances for a request

Use the following [describe-spot-instance-requests](../../../cli/latest/reference/ec2/describe-spot-instance-requests.md "../../../cli/latest/reference/ec2/describe-spot-instance-requests.md") command.

```
aws ec2 describe-spot-instance-requests \
    --spot-instance-request-ids `sir-0e54a519c9EXAMPLE` \
    --query "SpotInstanceRequests[*].{ID:InstanceId}"
```

The following is example output:

```
[
    {
        "ID": "i-1234567890abcdef0"
    },
    {
        "ID": "i-0598c7d356eba48d7"
    }
]
```

PowerShell

###### To find the Spot Instances for a request

Use the [Get-EC2SpotInstanceRequest](../../../powershell/latest/reference/items/Get-EC2SpotInstanceRequest.md "../../../powershell/latest/reference/items/Get-EC2SpotInstanceRequest.md") cmdlet.

```
(Get-EC2SpotInstanceRequest -SpotInstanceRequestId `sir-0e54a519c9EXAMPLE`).InstanceId
```

## Stop a Spot Instance

If you don't need your Spot Instances now, but you want to restart them later without losing the
data persisted in the Amazon EBS volume, you can stop them. The steps for stopping a Spot Instance
are similar to the steps for stopping an On-Demand Instance.

###### Note

While a Spot Instance is stopped, you can modify some of its instance attributes, but not the
instance type.

We don't charge usage for a stopped Spot Instance, or data transfer fees, but we do
charge for the storage for any Amazon EBS volumes.

###### Limitations

- You can only stop a Spot Instance if the Spot Instance was launched from a `persistent` Spot Instance
  request.
- You can't stop a Spot Instance if the associated Spot Instance request is cancelled. When the Spot Instance request
  is cancelled, you can only terminate the Spot Instance.
- You can't stop a Spot Instance if it is part of a fleet or launch group, or Availability Zone
  group.

Console

###### To stop a Spot Instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance,
   see [Find your Spot Instances](#using-spot-instances-running "#using-spot-instances-running").
4. Choose **Instance state**,
   **Stop instance**.
5. When prompted for confirmation, choose
   **Stop**.

AWS CLI

###### To stop a Spot Instance

Use the [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md")
command to manually stop your Spot Instances.

```
aws ec2 stop-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To stop a Spot Instance

Use the [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md")
cmdlet.

```
Stop-EC2Instance -InstanceId `i-1234567890abcdef0`
```

## Start a Spot Instance

You can start a Spot Instance that you previously stopped.

###### Prerequisites

You can only start a Spot Instance if:

- You manually stopped the Spot Instance.
- The Spot Instance is an EBS-backed instance.
- Spot Instance capacity is available.
- The Spot price is lower than your maximum price.

###### Limitations

- You can't start a Spot Instance if it is part of fleet or launch group, or Availability Zone
  group.

The steps for starting a Spot Instance are similar to the steps for starting an On-Demand Instance.

Console

###### To start a Spot Instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance,
   see [Find your Spot Instances](#using-spot-instances-running "#using-spot-instances-running").
4. Choose **Instance state**,
   **Start instance**.

AWS CLI

###### To start a Spot Instance

Use the [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md")
command to manually start your Spot Instances.

```
aws ec2 start-instances --instance-ids `i-1234567890abcdef0`
```

PowerShell

###### To start a Spot Instance

Use the [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md")
cmdlet.

```
Start-EC2Instance -InstanceId `i-1234567890abcdef0`
```

## Terminate a Spot Instance

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

If you terminate a running or stopped Spot Instance that was launched by a persistent Spot Instance request,
the Spot Instance request transitions to the `open` state so that a new Spot Instance can
be launched. To ensure that no new Spot Instance is launched, you must first cancel the Spot Instance
request.

If you cancel an `active` Spot Instance request that has a running Spot Instance, the running Spot Instance
is not automatically terminated; you must manually terminate the Spot Instance.

If you cancel a `disabled` Spot Instance request that has a stopped Spot Instance, the stopped
Spot Instance is automatically terminated by the Amazon EC2 Spot service. There might be a
short lag between when you cancel the Spot Instance request and when the Spot service
terminates the Spot Instance.

For more information, see [Cancel a Spot Instance request](using-spot-instances-cancel.md "using-spot-instances-cancel.md").

Console

###### To manually terminate a Spot Instance

1. Before you terminate an instance, verify that you won't lose any data by
   checking that your Amazon EBS volumes won't be deleted on termination and that
   you've copied any data that you need from your instance store volumes to
   persistent storage, such as Amazon EBS or Amazon S3.
2. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
3. In the navigation pane, choose **Instances**.
4. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance,
   see [Find your Spot Instances](#using-spot-instances-running "#using-spot-instances-running").
5. Choose **Instance state**, **Terminate (delete) instance**.
6. Choose **Terminate (delete)** when prompted for confirmation.

AWS CLI

###### To manually terminate a Spot Instance

Use the [terminate-instances](../../../cli/latest/reference/ec2/terminate-instances.md "../../../cli/latest/reference/ec2/terminate-instances.md") command to manually terminate your Spot Instances.

```
aws ec2 terminate-instances --instance-ids `i-1234567890abcdef0` `i-0598c7d356eba48d7`
```

PowerShell

###### To manually terminate a Spot Instance

Use the [Remove-EC2Instance](../../../powershell/latest/reference/items/Remove-EC2Instance.md "../../../powershell/latest/reference/items/Remove-EC2Instance.md")
cmdlet.

```
Remove-EC2Instance -InstanceId `i-1234567890abcdef0`
```
