# Create a placement group for your EC2 instances

You can use a placement group to control the placement of instances
relative to each other. After you create a placement group, you can launch
instances in the placement group.

###### Limitation

You can create a maximum of 500 placement groups per Region.

Console

###### To create a placement group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Placement
   Groups**.
3. Choose **Create placement group**.
4. Specify a name for the group.
5. Choose the placement strategy for the group: **Cluster**,
   **Spread**, or **Partition**.

If you chose **Spread**, you must choose the
spread level: **Rack** or **Host**.

If you chose **Partition**, you must enter
the number of partitions for the group. 6. (Optional) To add a tag, choose **Add new tag**, and
then enter a key and value. 7. Choose **Create group**.

AWS CLI
Use the [create-placement-group](../../../cli/latest/reference/ec2/create-placement-group.md "../../../cli/latest/reference/ec2/create-placement-group.md") command.

###### To create a cluster placement group

The following example creates a placement group that uses
the `cluster` placement strategy, and it applies a tag
with a key of `purpose` and a value of
`production`.

```
aws ec2 create-placement-group \
    --group-name `my-cluster` \
    --strategy cluster \
    --tag-specifications 'ResourceType=placement-group,Tags={Key=`purpose`,Value=`production`}'
```

###### To create a partition placement group

The following example creates a placement group that uses
the `partition` placement strategy, and specifies the
five partitions using the `--partition-count` parameter.

```
aws ec2 create-placement-group \
    --group-name `HDFS-Group-A` \
    --strategy partition \
    --partition-count `5`
```

PowerShell
Use the [New-EC2PlacementGroup](../../../powershell/latest/reference/items/New-EC2PlacementGroup.md "../../../powershell/latest/reference/items/New-EC2PlacementGroup.md") cmdlet.

###### To create a cluster placement group

The following example creates a cluster placement group.

```
New-EC2PlacementGroup `
    -GroupName `my-placement-group` `
    -Strategy cluster
```

###### To create a partition placement group

The following example creates a partition placement group.

```
New-EC2PlacementGroup `
    -GroupName `my-placement-group` `
    -Strategy partition `
    -PartitionCount `5`
```
