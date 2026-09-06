

# Describe a Spot Fleet request, its instances, and event history
<a name="manage-spot-fleet"></a>

**Important**  
Spot Fleet uses a legacy API with no planned investment. We recommend using EC2 Fleet or an Auto Scaling group instead. For more information, see [Which is the best fleet method to use?](which-fleet-method-to-use.md).

You can describe your Spot Fleet configuration, the instances in your Spot Fleet, and the event history of your Spot Fleet.

------
#### [ Console ]

**To describe your Spot Fleet**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select your Spot Fleet request. The ID begins with **sfr-**. To see the configuration details, choose **Description**.

1. To list the Spot Instances for the Spot Fleet, choose **Instances**.

1. To view the history for the Spot Fleet, choose **History**.

------
#### [ AWS CLI ]

**To describe your Spot Fleet request**  
Use the [describe-spot-fleet-requests](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-fleet-requests.html) command.

```
aws ec2 describe-spot-fleet-requests \
    --spot-fleet-request-ids {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}
```

**To describe the running instances for the specified Spot Fleet request**  
Use the [describe-spot-fleet-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-fleet-instances.html) command.

```
aws ec2 describe-spot-fleet-instances \
    --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}
```

**To describe the event history for the specified Spot Fleet request**  
Use the [describe-spot-fleet-request-history](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-fleet-request-history.html) command.

```
aws ec2 describe-spot-fleet-request-history \
    --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}} \
    --start-time {{2024-05-18T00:00:00Z}}
```

------
#### [ PowerShell ]

**To describe your Spot Fleet request**  
Use the [Get-EC2SpotFleetRequest](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2SpotFleetRequest.html) cmdlet.

```
Get-EC2SpotFleetRequest
```

**To describe the running instances for the specified Spot Fleet request**  
Use the [Get-EC2SpotFleetInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2SpotFleetInstance.html) cmdlet.

```
Get-EC2SpotFleetInstance `
    -SpotFleetRequestId "{{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}"
```

**To describe the event history for the specified Spot Fleet request**  
Use the [Get-EC2SpotFleetRequestHistory](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2SpotFleetRequestHistory.html) cmdlet.

```
Get-EC2SpotFleetRequestHistory `
    -SpotFleetRequestId "{{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"}} `
    -UtcStartTime {{2024-05-18T00:00:00Z}}
```

------