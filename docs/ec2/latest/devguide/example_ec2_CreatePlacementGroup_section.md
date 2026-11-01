

# Use `CreatePlacementGroup` with a CLI
<a name="example_ec2_CreatePlacementGroup_section"></a>

The following code examples show how to use `CreatePlacementGroup`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To create a placement group**  
The following `create-placement-group` example creates a placement group with the specified name.  

```
aws ec2 create-placement-group \
    --group-name {{my-cluster}} \
    --strategy {{cluster}}
```
Output:  

```
{
    "PlacementGroup": {
        "GroupName": "my-cluster",
        "State": "available",
        "Strategy": "cluster",
        "GroupId": "pg-0123456789example",
        "GroupArn": "arn:aws:ec2:us-west-2:123456789012:placement-group/my-cluster"
    }
}
```
For more information, see [Placement groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the *Amazon EC2 User Guide*.  
**Example 2: To create a partition placement group**  
The following `create-placement-group` example creates a partition placement group named `HDFS-Group-A` with five partitions.  

```
aws ec2 create-placement-group \
    --group-name {{HDFS-Group-A}} \
    --strategy {{partition}} \
    --partition-count {{5}}
```
Output:  

```
{
    "PlacementGroup": {
        "GroupName": "HDFS-Group-A",
        "State": "available",
        "Strategy": "partition",
        "PartitionCount": 5,
        "GroupId": "pg-0abcdef1234example",
        "GroupArn": "arn:aws:ec2:us-west-2:123456789012:placement-group/HDFS-Group-A"
    }
}
```
For more information, see [Placement strategies for your placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [CreatePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates a placement group with the specified name.**  

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster
```
+  For API details, see [CreatePlacementGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates a placement group with the specified name.**  

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster
```
+  For API details, see [CreatePlacementGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.