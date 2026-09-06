

# Modify a Spot Fleet request
<a name="modify-spot-fleet"></a>

**Important**  
Spot Fleet uses a legacy API with no planned investment. We recommend using EC2 Fleet or an Auto Scaling group instead. For more information, see [Which is the best fleet method to use?](which-fleet-method-to-use.md).

You can modify an active Spot Fleet request to complete the following tasks:
+ Increase the total target capacity and On-Demand portion
+ Decrease the total target capacity and On-Demand portion

When you increase the total target capacity, the Spot Fleet launches additional Spot Instances according to the [allocation strategy](ec2-fleet-allocation-strategy.md) for its Spot Fleet request. When you increase the On-Demand portion, the Spot Fleet launches additional On-Demand Instances.

When you decrease the total target capacity, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet reaches the new target capacity. If the allocation strategy is `diversified`, the Spot Fleet terminates instances across the pools. Alternatively, you can request that the Spot Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.

**Considerations**
+ You can't modify a one-time Spot Fleet request. You can only modify a Spot Fleet request if you selected **Maintain target capacity** when you created the Spot Fleet request.
+ When a Spot Fleet terminates an instance because the target capacity was decreased, the instance receives a Spot Instance interruption notice.

------
#### [ Console ]

**To modify a Spot Fleet request**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request.

1. Choose **Actions**, **Modify target capacity**.

1. In **Modify target capacity**, do the following:

   1. Enter the new target capacity and On-Demand portion.

   1. (Optional) If you are decreasing the target capacity but want to keep the fleet at its current size, clear **Terminate instances**.

   1. Choose **Submit**.

------
#### [ AWS CLI ]

**To modify a Spot Fleet request**  
Use the [modify-spot-fleet-request](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-spot-fleet-request.html) command to update the target capacity of the specified Spot Fleet request.

```
aws ec2 modify-spot-fleet-request \
    --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
    --target-capacity {{20}}
```

You can modify the previous command as follows to decrease the target capacity of the specified Spot Fleet without terminating any Spot Instances as a result.

```
aws ec2 modify-spot-fleet-request \
    --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
    --target-capacity {{10}} \
    --excess-capacity-termination-policy NoTermination
```

------
#### [ PowerShell ]

**To modify a Spot Fleet request**  
Use the [Edit-EC2SpotFleetRequest](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2SpotFleetRequest.html) cmdlet to update the target capacity of the specified Spot Fleet request.

```
Edit-EC2SpotFleetRequest `
    -SpotFleetRequestId "{{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}" `
    -TargetCapacity {{20}}
```

You can modify the previous command as follows to decrease the target capacity of the specified Spot Fleet without terminating any Spot Instances as a result.

```
Edit-EC2SpotFleetRequest `
    -SpotFleetRequestId "{{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}" `
    -TargetCapacity {{20}} `
    -ExcessCapacityTerminationPolicy "NoTermination"
```

------