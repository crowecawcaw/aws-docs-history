# Use `CancelSpotFleetRequests` with a CLI

The following code examples show how to use `CancelSpotFleetRequests`.

CLI

**AWS CLI**

**Example 1: To cancel a Spot fleet request and terminate the associated instances**

The following `cancel-spot-fleet-requests` example cancels a Spot Fleet request and terminates the associated On-Demand Instances and Spot Instances.

```
`aws ec2 cancel-spot-fleet-requests \
 --spot-fleet-request-ids `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
 --terminate-instances`

```

Output:

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

**Example 2: To cancel a Spot fleet request without terminating the associated instances**

The following `cancel-spot-fleet-requests` example cancels a Spot Fleet request without terminating the associated On-Demand Instances and Spot Instances.

```
`aws ec2 cancel-spot-fleet-requests \
 --spot-fleet-request-ids `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
 --no-terminate-instances`

```

Output:

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

For more information, see [Cancel a Spot Fleet request](../../../AWSEC2/latest/UserGuide/cancel-spot-fleet.md "../../../AWSEC2/latest/UserGuide/cancel-spot-fleet.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [CancelSpotFleetRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-fleet-requests.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-fleet-requests.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example cancels the specified Spot fleet request and terminates the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $true

```

**Example 2: This example cancels the specified Spot fleet request without terminating the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $false

```

- For API details, see
  [CancelSpotFleetRequests](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example cancels the specified Spot fleet request and terminates the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $true

```

**Example 2: This example cancels the specified Spot fleet request without terminating the associated Spot instances.**

```
Stop-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TerminateInstance $false

```

- For API details, see
  [CancelSpotFleetRequests](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
