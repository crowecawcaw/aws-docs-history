

# Use `AssignPrivateIpAddresses` with a CLI
<a name="example_ec2_AssignPrivateIpAddresses_section"></a>

The following code examples show how to use `AssignPrivateIpAddresses`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To assign a specific secondary private IP address to a network interface**  
The following `assign-private-ip-addresses` example assigns the specified secondary private IP address to the specified network interface.  

```
aws ec2 assign-private-ip-addresses \
    --network-interface-id {{eni-e5aa89a3}} \
    --private-ip-addresses {{10.0.0.82}}
```
Output:  

```
{
    "NetworkInterfaceId": "eni-e5aa89a3",
    "AssignedPrivateIpAddresses": [
        {
            "PrivateIpAddress": "10.0.0.82"
        }
    ]
}
```
For more information, see [Secondary IP addresses for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.html) in the *Amazon EC2 User Guide*.  
**Example 2: To assign secondary private IP addresses that Amazon EC2 selects to a network interface**  
The following `assign-private-ip-addresses` example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses in the CIDR block range of the subnet the network interface is associated with.  

```
aws ec2 assign-private-ip-addresses \
    --network-interface-id {{eni-e5aa89a3}} \
    --secondary-private-ip-address-count {{2}}
```
Output:  

```
{
    "NetworkInterfaceId": "eni-e5aa89a3",
    "AssignedPrivateIpAddresses": [
        {
            "PrivateIpAddress": "10.0.0.93"
        },
        {
            "PrivateIpAddress": "10.0.0.147"
        }
    ]
}
```
For more information, see [Secondary IP addresses for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [AssignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-ip-addresses.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example assigns the specified secondary private IP address to the specified network interface.**  

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
**Example 2: This example creates two secondary private IP addresses and assigns them to the specified network interface.**  

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -SecondaryPrivateIpAddressCount 2
```
+  For API details, see [AssignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example assigns the specified secondary private IP address to the specified network interface.**  

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -PrivateIpAddress 10.0.0.82
```
**Example 2: This example creates two secondary private IP addresses and assigns them to the specified network interface.**  

```
Register-EC2PrivateIpAddress -NetworkInterfaceId eni-1a2b3c4d -SecondaryPrivateIpAddressCount 2
```
+  For API details, see [AssignPrivateIpAddresses](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.