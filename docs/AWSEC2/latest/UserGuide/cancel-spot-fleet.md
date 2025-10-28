# Cancel (delete) a Spot Fleet request

If you no longer require a Spot Fleet, you can cancel the Spot Fleet request, which deletes the
request. After you cancel a fleet request, all Spot requests associated with the fleet
are also canceled, so that no new Spot Instances are launched.

When you cancel a Spot Fleet request, you must also specify if you want to terminate all of
its instances. These include both On-Demand Instances and Spot Instances.

###### Warning

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently
deleted and can't be recovered. All data stored on instance store volumes is permanently lost.
For more information, see [How instance termination
works](how-ec2-instance-termination-works.md "how-ec2-instance-termination-works.md").

Before you terminate an instance, ensure that you have backed up all data that you need to
retain after the termination to persistent storage.

If you specify that the instances must be terminated when the fleet request is
canceled, the fleet request enters the `cancelled_terminating` state.
Otherwise, it enters the `cancelled_running` state, and the instances
continue to run until they are interrupted or you terminate them manually.

###### Restrictions

- You can cancel up to 100 fleets in a single request. If you exceed the
  specified number, no fleets are canceled.

Console

###### To cancel (delete) a Spot Fleet request

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot
   Requests**.
3. Select your Spot Fleet request.
4. Choose **Actions**, **Cancel
   request**.
5. In the **Cancel Spot request** dialog box, do the
   following:
   1. To terminate the associated instances at the same time as
      canceling the Spot Fleet request, leave the **Terminate
      instances** checkbox selected. To cancel the
      Spot Fleet request without terminating the associated instances,
      clear the **Terminate instances**
      checkbox.
   2. Choose **Confirm**.

AWS CLI

###### To cancel (delete) a Spot Fleet request and terminate its instances

Use the [cancel-spot-fleet-requests](../../../cli/latest/reference/ec2/cancel-spot-fleet-requests.md "../../../cli/latest/reference/ec2/cancel-spot-fleet-requests.md") command with the
`--terminate-instances` option.

```
aws ec2 cancel-spot-fleet-requests \
    --spot-fleet-request-ids `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --terminate-instances
```

The following is example output.

```
{
    "SuccessfulFleetRequests": [
        {
            "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
            "CurrentSpotFleetRequestState": "cancelled_terminating",
            "PreviousSpotFleetRequestState": "active"
        }
    ],
    "UnsuccessfulFleetRequests": []
}
```

###### To cancel (delete) a Spot Fleet request without terminating its

instances

Modify the previous example by using the
`--no-terminate-instances` option instead.

```
aws ec2 cancel-spot-fleet-requests \
    --spot-fleet-request-ids `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --no-terminate-instances
```

The following is example output.

```
{
    "SuccessfulFleetRequests": [
        {
            "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
            "CurrentSpotFleetRequestState": "cancelled_running",
            "PreviousSpotFleetRequestState": "active"
        }
    ],
    "UnsuccessfulFleetRequests": []
}
```

PowerShell

###### To cancel (delete) a Spot Fleet request and terminate its instances

Use the [Stop-EC2SpotFleetRequest](../../../powershell/latest/reference/items/Stop-EC2SpotFleetRequest.md "../../../powershell/latest/reference/items/Stop-EC2SpotFleetRequest.md") cmdlet with the
`-TerminateInstance` parameter.

```
Stop-EC2SpotFleetRequest `
    -SpotFleetRequestId "`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`" `
    -TerminateInstance $true
```

###### To cancel (delete) a Spot Fleet request without terminating its

instances

Modify the previous example by changing the value of the
`-TerminateInstance` parameter.

```
Stop-EC2SpotFleetRequest `
    -SpotFleetRequestId "`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`" `
    -TerminateInstance $false
```
