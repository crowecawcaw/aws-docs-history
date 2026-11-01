

# Use `ModifyReservedInstances` with a CLI
<a name="example_ec2_ModifyReservedInstances_section"></a>

The following code examples show how to use `ModifyReservedInstances`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To modify Reserved Instances**  
The following `modify-reserved-instances` example moves a Reserved Instance to another Availability Zone in the same region.  

```
aws ec2 modify-reserved-instances \
    --reserved-instances-ids {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --target-configurations {{AvailabilityZone=us-west-2c,Platform=EC2-Classic,InstanceCount=10}}
```
Output:  

```
{
    "ReservedInstancesModificationId": "rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687"
}
```
For more information, see [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html) in the *Amazon EC2 User Guide*.  
**Example 2: To modify the network platform of Reserved Instances**  
The following `modify-reserved-instances` example converts EC2-Classic Reserved Instances to EC2-VPC.  

```
aws ec2 modify-reserved-instances \
    --reserved-instances-ids {{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}} \
    --target-configurations {{AvailabilityZone=us-west-2c,Platform=EC2-VPC,InstanceCount=5}}
```
Output:  

```
{
    "ReservedInstancesModificationId": "rimod-82fa9020-668f-4fb6-945d-61537009d291"
}
```
For more information, see [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html) in the *Amazon EC2 User Guide*.  
**Example 3: To modify the instance size of Reserved Instances**  
The following `modify-reserved-instances` example modifies a Reserved Instance that has 10 m1.small Linux/UNIX instances in us-west-2c so that 8 m1.small instances become 2 m1.large instances, and the remaining 2 m1.small become 1 m1.medium instance in the same Availability Zone.  

```
aws ec2 modify-reserved-instances \
    --reserved-instances-ids {{a1b2c3d4-5678-90ab-cdef-EXAMPLE33333}} \
    --target-configurations {{AvailabilityZone=us-west-2c,Platform=EC2-Classic,InstanceCount=2,InstanceType=m1.large}} {{AvailabilityZone=us-west-2c,Platform=EC2-Classic,InstanceCount=1,InstanceType=m1.medium}}
```
Output:  

```
{
    "ReservedInstancesModificationId": "rimod-acc5f240-080d-4717-b3e3-1c6b11fa00b6"
}
```
For more information, see [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html#ri-modification-instancemove) in the *Amazon EC2 User Guide*.  
+  For API details, see [ModifyReservedInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-reserved-instances.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example modifies the Availability Zone, instance count, and platform for the specified Reserved instances.**  

```
$config = New-Object Amazon.EC2.Model.ReservedInstancesConfiguration
$config.AvailabilityZone = "us-west-2a"
$config.InstanceCount = 1
$config.Platform = "EC2-VPC"

Edit-EC2ReservedInstance `
-ReservedInstancesId @("FE32132D-70D5-4795-B400-AE435EXAMPLE", "0CC556F3-7AB8-4C00-B0E5-98666EXAMPLE") `
-TargetConfiguration $config
```
+  For API details, see [ModifyReservedInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example modifies the Availability Zone, instance count, and platform for the specified Reserved instances.**  

```
$config = New-Object Amazon.EC2.Model.ReservedInstancesConfiguration
$config.AvailabilityZone = "us-west-2a"
$config.InstanceCount = 1
$config.Platform = "EC2-VPC"

Edit-EC2ReservedInstance `
-ReservedInstancesId @("FE32132D-70D5-4795-B400-AE435EXAMPLE", "0CC556F3-7AB8-4C00-B0E5-98666EXAMPLE") `
-TargetConfiguration $config
```
+  For API details, see [ModifyReservedInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.