# Use `CancelSpotInstanceRequests` with a CLI

The following code examples show how to use `CancelSpotInstanceRequests`.

CLI

**AWS CLI**

**To cancel Spot Instance requests**

This example command cancels a Spot Instance request.

Command:

```
`aws ec2 cancel-spot-instance-requests --spot-instance-request-ids `sir-08b93456``

```

Output:

```
{
    "CancelledSpotInstanceRequests": [
        {
            "State": "cancelled",
            "SpotInstanceRequestId": "sir-08b93456"
        }
    ]
}
```

- For API details, see
  [CancelSpotInstanceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-instance-requests.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-instance-requests.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example cancels the specified Spot instance request.**

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678

```

**Output:**

```
SpotInstanceRequestId    State
---------------------    -----
sir-12345678             cancelled
```

- For API details, see
  [CancelSpotInstanceRequests](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example cancels the specified Spot instance request.**

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678

```

**Output:**

```
SpotInstanceRequestId    State
---------------------    -----
sir-12345678             cancelled
```

- For API details, see
  [CancelSpotInstanceRequests](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
