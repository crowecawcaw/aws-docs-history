# Updating a subnet group

You can update a subnet group's description, or modify the list of subnet IDs associated with the subnet group.
You cannot delete a subnet ID from a subnet group if a cluster is currently using that subnet.

The following procedures show you how to update a subnet group.

## Updating subnet groups (Console)

###### To update a subnet group

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. In the left navigation pane, choose **Subnet Groups**.
3. In the list of subnet groups, choose the one you want to modify.
4. **Name**, **VPCId** and **Description** fields are not modifiable.
5. In the **Selected subnets** section click **Manage** to make any changes to the Availability Zones you need for the subnets. To save your changes, choose
   **Save**.

## Updating subnet groups (AWS CLI)

At a command prompt, use the command `update-subnet-group` to
update a subnet group.

For Linux, macOS, or Unix:

```
aws memorydb update-subnet-group \
    --subnet-group-name `mysubnetgroup` \
    --description `"New description"` \
    --subnet-ids "`subnet-42df9c3a`" "`subnet-48fc21a9`"
```

For Windows:

```
aws memorydb update-subnet-group ^
    --subnet-group-name `mysubnetgroup` ^
    --description `"New description"` ^
    --subnet-ids "`subnet-42df9c3a`" "`subnet-48fc21a9`"
```

This command should produce output similar to the following:

```
{
    "SubnetGroup": {
        "VpcId": "vpc-73cd3c17",
        "Description": "New description",
        "Subnets": [
            {
                "Identifier": "subnet-42dcf93a",
                "AvailabilityZone": {
                    "Name": "us-east-1a"
                }
            },
            {
                "Identifier": "subnet-48fc12a9",
                "AvailabilityZone": {
                    "Name": "us-east-1a"
                }
            }
        ],
        "Name": "mysubnetgroup",
        "ARN": "arn:aws:memorydb:us-east-1:012345678912:subnetgroup/mysubnetgroup",
    }
}
```

For more information, see the AWS CLI topic [update-subnet-group](../../../cli/latest/reference/memorydb/update-subnet-group.md "../../../cli/latest/reference/memorydb/update-subnet-group.md").

## Updating subnet groups (MemoryDB API)

Using the MemoryDB API, call `UpdateSubnetGroup` with the following
parameters:

- `SubnetGroupName=``mysubnetgroup`
- Any other parameters whose values you want to change. This example uses
  `Description=``New%20description`
  to change the description of the subnet group.

###### Example

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=UpdateSubnetGroup
    &Description=New%20description
    &SubnetGroupName=mysubnetgroup
    &SubnetIds.member.1=subnet-42df9c3a
    &SubnetIds.member.2=subnet-48fc21a9
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Timestamp=20141201T220302Z
    &Version=2014-12-01
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20141201T220302Z
    &X-Amz-Expires=20141201T220302Z
    &X-Amz-Signature=<signature>
    &X-Amz-SignedHeaders=Host
```

###### Note

When you create a new subnet group, take note the number of available IP addresses.
If the subnet has very few free IP addresses,
you might be constrained as to how many more nodes you can add to the cluster.
To resolve this issue,
you can assign one or more subnets to a subnet group
so that you have a sufficient number of IP addresses in your cluster's Availability Zone.
After that, you can add more nodes to your cluster.
