# Use `DescribeSpotDatafeedSubscription` with a CLI

The following code examples show how to use `DescribeSpotDatafeedSubscription`.

CLI

**AWS CLI**

**To describe Spot Instance datafeed subscription for an account**

This example command describes the data feed for the account.

Command:

```
`aws ec2 describe-spot-datafeed-subscription`

```

Output:

```
{
    "SpotDatafeedSubscription": {
        "OwnerId": "123456789012",
        "Prefix": "spotdata",
        "Bucket": "amzn-s3-demo-bucket",
        "State": "Active"
    }
}
```

- For API details, see
  [DescribeSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes your Spot instance data feed.**

```
Get-EC2SpotDatafeedSubscription

```

**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```

- For API details, see
  [DescribeSpotDatafeedSubscription](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes your Spot instance data feed.**

```
Get-EC2SpotDatafeedSubscription

```

**Output:**

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```

- For API details, see
  [DescribeSpotDatafeedSubscription](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
