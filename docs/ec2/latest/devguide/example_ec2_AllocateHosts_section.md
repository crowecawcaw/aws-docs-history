

# Use `AllocateHosts` with a CLI
<a name="example_ec2_AllocateHosts_section"></a>

The following code examples show how to use `AllocateHosts`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To allocate a Dedicated Host**  
The following `allocate-hosts` example allocates a single Dedicated Host in the `eu-west-1a` Availability Zone, onto which you can launch `m5.large` instances. By default, the Dedicated Host accepts only target instance launches, and does not support host recovery.  

```
aws ec2 allocate-hosts \
    --instance-type {{m5.large}} \
    --availability-zone {{eu-west-1a}} \
    --quantity {{1}}
```
Output:  

```
{
    "HostIds": [
        "h-07879acf49EXAMPLE"
    ]
}
```
**Example 2: To allocate a Dedicated Host with auto-placement and host recovery enabled**  
The following `allocate-hosts` example allocates a single Dedicated Host in the `eu-west-1a` Availability Zone with auto-placement and host recovery enabled.  

```
aws ec2 allocate-hosts \
    --instance-type {{m5.large}} \
    --availability-zone {{eu-west-1a}} \
    --auto-placement {{on}} \
    --host-recovery {{on}} \
    --quantity {{1}}
```
Output:  

```
{
     "HostIds": [
         "h-07879acf49EXAMPLE"
     ]
}
```
**Example 3: To allocate a Dedicated Host with tags**  
The following `allocate-hosts` example allocates a single Dedicated Host and applies a tag with a key named `purpose` and a value of `production`.  

```
aws ec2 allocate-hosts \
    --instance-type {{m5.large}} \
    --availability-zone {{eu-west-1a}} \
    --quantity {{1}} \
    --tag-specifications '{{ResourceType=dedicated-host,Tags={Key=purpose,Value=production}}}'
```
Output:  

```
{
    "HostIds": [
        "h-07879acf49EXAMPLE"
    ]
}
```
For more information, see [Allocate a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-allocating.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [AllocateHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-hosts.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example allocates a Dedicated Host to your account for the given instance type and availability zone**  

```
New-EC2Host -AutoPlacement on -AvailabilityZone eu-west-1b -InstanceType m4.xlarge -Quantity 1
```
**Output:**  

```
h-01e23f4cd567890f3
```
+  For API details, see [AllocateHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example allocates a Dedicated Host to your account for the given instance type and availability zone**  

```
New-EC2Host -AutoPlacement on -AvailabilityZone eu-west-1b -InstanceType m4.xlarge -Quantity 1
```
**Output:**  

```
h-01e23f4cd567890f3
```
+  For API details, see [AllocateHosts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.