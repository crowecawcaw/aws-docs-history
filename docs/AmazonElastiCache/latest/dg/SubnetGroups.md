# Modifying a subnet group

You can modify a subnet group's description, or modify the list of subnet IDs associated with the subnet group.
You cannot delete a subnet ID from a subnet group if a cache is currently using that subnet.

The following procedures show you how to modify a subnet group.

## Modifying subnet groups (Console)

###### To modify a subnet group

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Subnet groups**.
3. In the list of subnet groups, select the radio button of the one you want to modify and choose **Modify**.
4. In the **Selected subnets** panel, choose **Manage**.
5. Make any changes to the selected subnets and click **Choose**.
6. Click **Save changes** to save your changes.

## Modifying subnet groups (AWS CLI)

At a command prompt, use the command `modify-cache-subnet-group` to
modify a subnet group.

For Linux, macOS, or Unix:

```
aws elasticache modify-cache-subnet-group \
    --cache-subnet-group-name `mysubnetgroup` \
    --cache-subnet-group-description `"New description"` \
    --subnet-ids "`subnet-42df9c3a`" "`subnet-48fc21a9`"
```

For Windows:

```
aws elasticache modify-cache-subnet-group ^
    --cache-subnet-group-name `mysubnetgroup` ^
    --cache-subnet-group-description `"New description"` ^
    --subnet-ids "`subnet-42df9c3a`" "`subnet-48fc21a9`"
```

This command should produce output similar to the following:

```
{
    "CacheSubnetGroup": {
        "VpcId": "vpc-73cd3c17",
        "CacheSubnetGroupDescription": "New description",
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-42dcf93a",
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            },
            {
                "SubnetIdentifier": "subnet-48fc12a9",
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            }
        ],
        "CacheSubnetGroupName": "mysubnetgroup"
    }
}
```

For more information, see the AWS CLI topic modify-cache-subnet-group.
