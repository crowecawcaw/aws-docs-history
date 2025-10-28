# Describe a Spot Fleet request, its instances, and event

history

You can describe your Spot Fleet configuration, the instances in your Spot Fleet, and the event
history of your Spot Fleet.

Console

###### To describe your Spot Fleet

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot
   Requests**.
3. Select your Spot Fleet request. The ID begins with
   **sfr-**. To see the configuration details,
   choose **Description**.
4. To list the Spot Instances for the Spot Fleet, choose
   **Instances**.
5. To view the history for the Spot Fleet, choose
   **History**.

AWS CLI

###### To describe your Spot Fleet request

Use the [describe-spot-fleet-requests](../../../cli/latest/reference/ec2/describe-spot-fleet-requests.md "../../../cli/latest/reference/ec2/describe-spot-fleet-requests.md") command.

```
aws ec2 describe-spot-fleet-requests \
    --spot-fleet-request-ids `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

###### To describe the running instances for the specified Spot Fleet

request

Use the [describe-spot-fleet-instances](../../../cli/latest/reference/ec2/describe-spot-fleet-instances.md "../../../cli/latest/reference/ec2/describe-spot-fleet-instances.md") command.

```
aws ec2 describe-spot-fleet-instances \
    --spot-fleet-request-id `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

###### To describe the event history for the specified Spot Fleet request

Use the [describe-spot-fleet-request-history](../../../cli/latest/reference/ec2/describe-spot-fleet-request-history.md "../../../cli/latest/reference/ec2/describe-spot-fleet-request-history.md") command.

```
aws ec2 describe-spot-fleet-request-history \
    --spot-fleet-request-id `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --start-time `2024-05-18T00:00:00Z`
```

PowerShell

###### To describe your Spot Fleet request

Use the [Get-EC2SpotFleetRequest](../../../powershell/latest/reference/items/Get-EC2SpotFleetRequest.md "../../../powershell/latest/reference/items/Get-EC2SpotFleetRequest.md") cmdlet.

```
Get-EC2SpotFleetRequest
```

###### To describe the running instances for the specified Spot Fleet

request

Use the [Get-EC2SpotFleetInstance](../../../powershell/latest/reference/items/Get-EC2SpotFleetInstance.md "../../../powershell/latest/reference/items/Get-EC2SpotFleetInstance.md") cmdlet.

```
Get-EC2SpotFleetInstance `
    -SpotFleetRequestId "`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`"
```

###### To describe the event history for the specified Spot Fleet request

Use the [Get-EC2SpotFleetRequestHistory](../../../powershell/latest/reference/items/Get-EC2SpotFleetRequestHistory.md "../../../powershell/latest/reference/items/Get-EC2SpotFleetRequestHistory.md") cmdlet.

```
Get-EC2SpotFleetRequestHistory `
    -SpotFleetRequestId "`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"` `
    -UtcStartTime `2024-05-18T00:00:00Z`
```
