# Modifying an Amazon DocumentDB subnet group

You can use the AWS Management Console or AWS CLI to modify a subnet group's description or to add or remove subnets from an Amazon DocumentDB subnet group. However, you
cannot modify the `default` subnet group.

Using the AWS Management Console
You can use the AWS Management Console to change a subnet group's description or to add and remove subnets. Remember that when you're finished, you must have
at least two Availability Zones associated with your subnet group.

###### To modify your subnet group

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Subnet groups**. Then choose the button to the left of the subnet group's name. Remember
   that you can't modify the `default` subnet group.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. Choose **Actions**, and then choose **Modify**. 4. **Description**—To change the description of your subnet group, enter a new description. 5. To change the subnets associated with your subnet group, in the **Add subnets** section, do any one or more of the
following:

    * To remove all subnets from this subnet group, choose **Remove all**.
    * To remove specific subnets from this subnet group, choose **Remove** for each subnet you want to remove.
    * To add all the subnets associated with this VPC, choose **Add all the subnets related to this VPC**.
    * To add specific subnets to this subnet group, do the following for each Availability Zone for which you want to add a subnet.


    	1. **Availability zone**—In the list, choose a new Availability Zone.
    	2. **Subnet**—In the list, choose a subnet from the chosen Availability Zone for this subnet
    	 group.
    	3. Choose **Add subnet**.

6. In the confirmation dialog box:
   - To make these changes to the subnet group, choose **Modify**.
   - To keep the subnet group unchanged, choose **Cancel**.

Using the AWS CLI
You can use the AWS CLI to change a subnet group's description or to add and remove subnets. Remember that when you're finished, you must have at
least two Availability Zones associated with your subnet group. You can't modify the `default` subnet group.

###### Parameters:

- `--db-subnet-group-name`—Required. The name of the Amazon DocumentDB subnet group you are modifying.
- `--subnet-ids`—Required. A list of all the subnets that you want in the subnet group after this change is done.

###### Important

Any subnets currently in the subnet group that are not included in this list are removed from the subnet group. If you want to keep any
of the subnets currently in the subnet group, you must include them in this list.

- `--db-subnet-group-description`—Optional. The description of the subnet group.

###### Example

The following code modifies the description and replaces the existing subnets with the subnets `subnet-991cb8d0`,
`subnet-53ab3636`, and `subnet-29ab1025`.

For Linux, macOS, or Unix:

```
aws docdb modify-db-subnet-group \
    --db-subnet-group-name sample-subnet-group \
    --subnet-ids subnet-991cb8d0 subnet-53ab3636 subnet-29ab1025 \
    --db-subnet-group-description "Modified subnet group"
```

For Windows:

```
aws docdb modify-db-subnet-group ^
    --db-subnet-group-name sample-subnet-group ^
    --subnet-ids subnet-991cb8d0 subnet-53ab3636 subnet-29ab1025 ^
    --db-subnet-group-description "Modified subnet group"
```

Output from this operation looks something like the following (JSON format). Notice that this is the same subnet group that was created in the
[Creating an Amazon DocumentDB subnet group](document-db-subnet-group-create.md "document-db-subnet-group-create.md") section. However, the subnets in the subnet
group are replaced with those listed in the `modify-db-subnet-group` operation.

```
{
    "DBSubnetGroup": {
        "DBSubnetGroupArn": "arn:aws:rds:us-east-1:123SAMPLE012:subgrp:sample-subnet-group",
        "DBSubnetGroupDescription": "Modified subnet group",
        "SubnetGroupStatus": "Complete",
        "Subnets": [
            {
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1d"
                },
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-53ab3636"
            },
            {
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1b"
                },
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-991cb8d0"
            },
            {
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1f"
                },
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-29ab1025"
            }
        ],
        "VpcId": "vpc-91280df6",
        "DBSubnetGroupName": "sample-subnet-group"
    }
}
```
