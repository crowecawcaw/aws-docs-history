

# Use `RequestSpotFleet` with a CLI
<a name="example_ec2_RequestSpotFleet_section"></a>

The following code examples show how to use `RequestSpotFleet`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To request a Spot fleet in the subnet with the lowest price**  
The following `request-spot-fleet` example creates a Spot fleet request with two launch specifications that differ only by subnet. The Spot fleet launches the instances in the specified subnet with the lowest price. If the instances are launched in a default VPC, they receive a public IP address by default. If the instances are launched in a nondefault VPC, they do not receive a public IP address by default.  
Note that you can't specify different subnets from the same Availability Zone in a Spot fleet request.  

```
aws ec2 request-spot-fleet \
    --spot-fleet-request-config {{file://config.json}}
```
Contents of `config.json`:  

```
{
    "SpotPrice": "0.04",
    "TargetCapacity": 2,
    "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role",
    "LaunchSpecifications": [
        {
            "ImageId": "ami-1a2b3c4d",
            "KeyName": "my-key-pair",
            "SecurityGroups": [
                {
                    "GroupId": "sg-1a2b3c4d"
                }
            ],
            "InstanceType": "m3.medium",
            "SubnetId": "subnet-1a2b3c4d, subnet-3c4d5e6f",
            "IamInstanceProfile": {
                "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
            }
        }
    ]
}
```
Output:  

```
{
    "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
}
```
For more information, see [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html) in the *Amazon EC2 User Guide*.  
**Example 2: To request a Spot fleet in the Availability Zone with the lowest price**  
The following `request-spot-fleet` example creates a Spot fleet request with two launch specifications that differ only by Availability Zone. The Spot fleet launches the instances in the specified Availability Zone with the lowest price. If your account supports EC2-VPC only, Amazon EC2 launches the Spot instances in the default subnet of the Availability Zone. If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the Availability Zone.  

```
aws ec2 request-spot-fleet \
    --spot-fleet-request-config {{file://config.json}}
```
Contents of `config.json`:  

```
{
    "SpotPrice": "0.04",
    "TargetCapacity": 2,
    "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role",
    "LaunchSpecifications": [
        {
            "ImageId": "ami-1a2b3c4d",
            "KeyName": "my-key-pair",
            "SecurityGroups": [
                {
                    "GroupId": "sg-1a2b3c4d"
                }
            ],
            "InstanceType": "m3.medium",
            "Placement": {
                "AvailabilityZone": "us-west-2a, us-west-2b"
            },
            "IamInstanceProfile": {
                "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
            }
        }
    ]
}
```
Output:  

```
{
    "SpotFleetRequestId": "sfr-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```
For more information, see [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html) in the *Amazon EC2 User Guide*.  
**Example 3: To launch Spot instances in a subnet and assign them public IP addresses**  
The following `request-spot-fleet` example assigns public addresses to instances launched in a nondefault VPC. Note that when you specify a network interface, you must include the subnet ID and security group ID using the network interface.  

```
aws ec2 request-spot-fleet \
    --spot-fleet-request-config {{file://config.json}}
```
Contents of `config.json`:  

```
{
    "SpotPrice": "0.04",
    "TargetCapacity": 2,
    "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role",
    "LaunchSpecifications": [
        {
            "ImageId": "ami-1a2b3c4d",
            "KeyName": "my-key-pair",
            "InstanceType": "m3.medium",
            "NetworkInterfaces": [
                {
                    "DeviceIndex": 0,
                    "SubnetId": "subnet-1a2b3c4d",
                    "Groups": [
                        "sg-1a2b3c4d"
                    ],
                    "AssociatePublicIpAddress": true
                }
            ],
            "IamInstanceProfile": {
                "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
            }
        }
    ]
}
```
Output:  

```
{
    "SpotFleetRequestId": "sfr-a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
}
```
For more information, see [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html) in the *Amazon EC2 User Guide*.  
**Example 4: To request a Spot fleet using the diversified allocation strategy**  
The following `request-spot-fleet` example creates a Spot fleet request that launches 30 instances using the diversified allocation strategy. The launch specifications differ by instance type. The Spot fleet distributes the instances across the launch specifications such that there are 10 instances of each type.  

```
aws ec2 request-spot-fleet \
    --spot-fleet-request-config {{file://config.json}}
```
Contents of `config.json`:  

```
{
    "SpotPrice": "0.70",
    "TargetCapacity": 30,
    "AllocationStrategy": "diversified",
    "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role",
    "LaunchSpecifications": [
        {
            "ImageId": "ami-1a2b3c4d",
            "InstanceType": "c4.2xlarge",
            "SubnetId": "subnet-1a2b3c4d"
        },
        {
            "ImageId": "ami-1a2b3c4d",
            "InstanceType": "m3.2xlarge",
            "SubnetId": "subnet-1a2b3c4d"
        },
        {
            "ImageId": "ami-1a2b3c4d",
            "InstanceType": "r3.2xlarge",
            "SubnetId": "subnet-1a2b3c4d"
        }
    ]
}
```
Output:  

```
{
    "SpotFleetRequestId": "sfr-a1b2c3d4-5678-90ab-cdef-EXAMPLE44444"
}
```
For more information, see [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [RequestSpotFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/request-spot-fleet.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates a Spot fleet request in the Availability Zone with the lowest price for the specified instance type. If your account supports EC2-VPC only, the Spot fleet launches the instances in the lowest-priced Availability Zone that has a default subnet. If your account supports EC2-Classic, the Spot fleet launches the instances in EC2-Classic in the lowest-priced Availability Zone. Note that the price you pay will not exceed the specified Spot price for the request.**  

```
$sg = New-Object Amazon.EC2.Model.GroupIdentifier
$sg.GroupId = "sg-12345678"
$lc = New-Object Amazon.EC2.Model.SpotFleetLaunchSpecification
$lc.ImageId = "ami-12345678"
$lc.InstanceType = "m3.medium"
$lc.SecurityGroups.Add($sg) 
Request-EC2SpotFleet -SpotFleetRequestConfig_SpotPrice 0.04 `
-SpotFleetRequestConfig_TargetCapacity 2 `
-SpotFleetRequestConfig_IamFleetRole arn:aws:iam::123456789012:role/my-spot-fleet-role `
-SpotFleetRequestConfig_LaunchSpecification $lc
```
+  For API details, see [RequestSpotFleet](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates a Spot fleet request in the Availability Zone with the lowest price for the specified instance type. If your account supports EC2-VPC only, the Spot fleet launches the instances in the lowest-priced Availability Zone that has a default subnet. If your account supports EC2-Classic, the Spot fleet launches the instances in EC2-Classic in the lowest-priced Availability Zone. Note that the price you pay will not exceed the specified Spot price for the request.**  

```
$sg = New-Object Amazon.EC2.Model.GroupIdentifier
$sg.GroupId = "sg-12345678"
$lc = New-Object Amazon.EC2.Model.SpotFleetLaunchSpecification
$lc.ImageId = "ami-12345678"
$lc.InstanceType = "m3.medium"
$lc.SecurityGroups.Add($sg) 
Request-EC2SpotFleet -SpotFleetRequestConfig_SpotPrice 0.04 `
-SpotFleetRequestConfig_TargetCapacity 2 `
-SpotFleetRequestConfig_IamFleetRole arn:aws:iam::123456789012:role/my-spot-fleet-role `
-SpotFleetRequestConfig_LaunchSpecification $lc
```
+  For API details, see [RequestSpotFleet](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.