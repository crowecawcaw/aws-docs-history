

# Create a placement group for your EC2 instances
<a name="create-placement-group"></a>

You can use a placement group to control the placement of instances relative to each other. After you create a placement group, you can launch instances in the placement group.

**Limitation**  
You can create a maximum of 500 placement groups per Region.

------
#### [ Console ]

**To create a placement group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Placement Groups**.

1. Choose **Create placement group**.

1. For **Name**, specify a name for the group.

1. For **Placement strategy**, choose the placement strategy for the group: **Cluster**, **Spread**, **Partition**, or **Precision time**.

   1. If you chose **Spread**, for **Spread level**, choose **Host** or **Rack**.

   1. If you chose **Partition**, for **Number of partitions**, enter the number of partitions for the group.

   1. If you chose **Cluster**, you can optionally specify a parent precision time placement group to ensure that instances in the cluster placement group launch on precision time capable hardware.

1. (Optional) To add a tag, under **Tags**, choose **Add new tag**, and then enter a key and value.

1. Choose **Create group**.

------
#### [ AWS CLI ]

Use the [create-placement-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-placement-group.html) command.

**To create a cluster placement group**  
The following example creates a placement group that uses the `cluster` placement strategy, and it applies a tag with a key of `purpose` and a value of `production`.

```
aws ec2 create-placement-group \
    --group-name {{my-cluster}} \
    --strategy cluster \
    --tag-specifications 'ResourceType=placement-group,Tags={Key={{purpose}},Value={{production}}}'
```

**To create a cluster placement group with a precision time placement group parent**  
The following example creates a cluster placement group that specifies a parent precision time placement group using the `--parent-group-id` parameter.

```
aws ec2 create-placement-group \
    --group-name {{my-cluster}} \
    --strategy cluster \
    --parent-group-id {{pg-0aaa1111111111111}}
```

**To create a partition placement group**  
The following example creates a placement group that uses the `partition` placement strategy, and specifies the five partitions using the `--partition-count` parameter.

```
aws ec2 create-placement-group \
    --group-name {{HDFS-Group-A}} \
    --strategy partition \
    --partition-count {{5}}
```

**To create a precision time placement group**  
The following example creates a placement group that uses the `precision-time` placement strategy.

```
aws ec2 create-placement-group \
    --group-name {{my-precision-time-pg}} \
    --strategy precision-time
```

------
#### [ PowerShell ]

Use the [New-EC2PlacementGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2PlacementGroup.html) cmdlet.

**To create a cluster placement group**  
The following example creates a cluster placement group.

```
New-EC2PlacementGroup `
    -GroupName {{my-placement-group}} `
    -Strategy cluster
```

**To create a cluster placement group with a precision time placement group parent**  
The following example creates a cluster placement group that specifies a parent precision time placement group using the `-ParentGroupId` parameter.

```
New-EC2PlacementGroup `
    -GroupName {{my-placement-group}} `
    -Strategy cluster `
    -ParentGroupId {{pg-0aaa1111111111111}}
```

**To create a partition placement group**  
The following example creates a partition placement group.

```
New-EC2PlacementGroup `
    -GroupName {{my-placement-group}} `
    -Strategy partition `
    -PartitionCount {{5}}
```

**To create a precision time placement group**  
The following example creates a precision time placement group.

```
New-EC2PlacementGroup `
    -GroupName {{my-precision-time-pg}} `
    -Strategy precision-time
```

------