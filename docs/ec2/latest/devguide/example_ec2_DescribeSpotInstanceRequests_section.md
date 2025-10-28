# Use `DescribeSpotInstanceRequests` with a CLI

The following code examples show how to use `DescribeSpotInstanceRequests`.

CLI

**AWS CLI**

**Example 1: To describe a Spot Instance request**

The following `describe-spot-instance-requests` example describes the specified Spot Instance request.

```
`aws ec2 describe-spot-instance-requests \
 --spot-instance-request-ids `sir-08b93456``

```

Output:

```
{
    "SpotInstanceRequests": [
        {
            "CreateTime": "2018-04-30T18:14:55.000Z",
            "InstanceId": "i-1234567890abcdef1",
            "LaunchSpecification": {
                "InstanceType": "t2.micro",
                "ImageId": "ami-003634241a8fcdec0",
                "KeyName": "my-key-pair",
                "SecurityGroups": [
                    {
                        "GroupName": "default",
                        "GroupId": "sg-e38f24a7"
                    }
                ],
                "BlockDeviceMappings": [
                    {
                        "DeviceName": "/dev/sda1",
                        "Ebs": {
                            "DeleteOnTermination": true,
                            "SnapshotId": "snap-0e54a519c999adbbd",
                            "VolumeSize": 8,
                            "VolumeType": "standard",
                            "Encrypted": false
                        }
                    }
                ],
                "NetworkInterfaces": [
                    {
                        "DeleteOnTermination": true,
                        "DeviceIndex": 0,
                        "SubnetId": "subnet-049df61146c4d7901"
                    }
                ],
                "Placement": {
                    "AvailabilityZone": "us-east-2b",
                    "Tenancy": "default"
                },
                "Monitoring": {
                    "Enabled": false
                }
            },
            "LaunchedAvailabilityZone": "us-east-2b",
            "ProductDescription": "Linux/UNIX",
            "SpotInstanceRequestId": "sir-08b93456",
            "SpotPrice": "0.010000"
            "State": "active",
            "Status": {
                "Code": "fulfilled",
                "Message": "Your Spot request is fulfilled.",
                "UpdateTime": "2018-04-30T18:16:21.000Z"
            },
            "Tags": [],
            "Type": "one-time",
            "InstanceInterruptionBehavior": "terminate"
        }
    ]
}
```

**Example 2: To describe Spot Instance requests based on filters**

The following `describe-spot-instance-requests` example uses filters to scope the results to Spot Instance requests with the specified instance type in the specified Availability Zone. The example uses the `--query` parameter to display only the instance IDs.

```
`aws ec2 describe-spot-instance-requests \
 --filters `Name=launch.instance-type,Values=m3.medium` `Name=launched-availability-zone,Values=us-east-2a` \
 --query `"SpotInstanceRequests[*].[InstanceId]"` \
 --output `text``

```

Output:

```
i-057750d42936e468a
i-001efd250faaa6ffa
i-027552a73f021f3bd
...
```

For additional examples using filters, see [Listing and filtering your resources](../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI "../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI") in the _Amazon Elastic Compute Cloud User Guide_.

**Example 3: To describe Spot Instance requests based on tags**

The following `describe-spot-instance-requests` example uses tag filters to scope the results to Spot Instance requests that have the tag `cost-center=cc123`.

```
`aws ec2 describe-spot-instance-requests \
 --filters `Name=tag:cost-center,Values=cc123``

```

For an example of the output for `describe-spot-instance-requests`, see Example 1.

For additional examples using tag filters, see [Working with tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI") in the _Amazon EC2 User Guide_.

- For API details, see
  [DescribeSpotInstanceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-instance-requests.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-instance-requests.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified Spot instance request.**

```
Get-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678

```

**Output:**

```
ActualBlockHourlyPrice   :
AvailabilityZoneGroup    :
BlockDurationMinutes     : 0
CreateTime               : 4/8/2015 2:51:33 PM
Fault                    :
InstanceId               : i-12345678
LaunchedAvailabilityZone : us-west-2b
LaunchGroup              :
LaunchSpecification      : Amazon.EC2.Model.LaunchSpecification
ProductDescription       : Linux/UNIX
SpotInstanceRequestId    : sir-12345678
SpotPrice                : 0.020000
State                    : active
Status                   : Amazon.EC2.Model.SpotInstanceStatus
Tags                     : {Name}
Type                     : one-time
```

**Example 2: This example describes all your Spot instance requests.**

```
Get-EC2SpotInstanceRequest

```

- For API details, see
  [DescribeSpotInstanceRequests](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified Spot instance request.**

```
Get-EC2SpotInstanceRequest -SpotInstanceRequestId sir-12345678

```

**Output:**

```
ActualBlockHourlyPrice   :
AvailabilityZoneGroup    :
BlockDurationMinutes     : 0
CreateTime               : 4/8/2015 2:51:33 PM
Fault                    :
InstanceId               : i-12345678
LaunchedAvailabilityZone : us-west-2b
LaunchGroup              :
LaunchSpecification      : Amazon.EC2.Model.LaunchSpecification
ProductDescription       : Linux/UNIX
SpotInstanceRequestId    : sir-12345678
SpotPrice                : 0.020000
State                    : active
Status                   : Amazon.EC2.Model.SpotInstanceStatus
Tags                     : {Name}
Type                     : one-time
```

**Example 2: This example describes all your Spot instance requests.**

```
Get-EC2SpotInstanceRequest

```

- For API details, see
  [DescribeSpotInstanceRequests](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
