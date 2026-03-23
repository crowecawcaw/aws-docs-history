# Creating a subnet group

When you create a new subnet group, note the number of available
IP addresses. If the subnet has very few free IP addresses, you might be
constrained as to how many more nodes you can add to the cluster. To
resolve this issue, you can assign one or more subnets to a subnet group
so that you have a sufficient number of IP addresses in your cluster's
Availability Zone. After that, you can add more nodes to your
cluster.

The following procedures show you how to create a subnet group called
`mysubnetgroup` (console), the AWS CLI, and the
MemoryDB API.

## Creating a subnet group (Console)

The following procedure shows how to create a subnet group (console).

###### To create a subnet group (Console)

1.  Sign in to the AWS Management Console, and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2.  In the left navigation pane, choose **Subnet Groups**.
3.  Choose **Create Subnet Group**.
4.  In the **Create Subnet Group** page,
    do the following:
    1. In the **Name** box,
       type a name for your subnet group.

    Cluster naming constraints are as follows:

        * Must contain 1–40 alphanumeric characters or hyphens.
        * Must begin with a letter.
        * Can't contain two consecutive hyphens.
        * Can't end with a hyphen.

    2. In the **Description** box,
       type a description for your subnet group.
    3. In the **VPC ID** box,
       choose the Amazon VPC that you created. If you have not created one, choose the **Create VPC** button and follow the
       steps to create one.
    4. In **Selected subnets**,
       choose the Availability Zone and ID of your private subnet,
       and then choose **Choose**.

5.  For **Tags**, you can optionally apply tags to search and filter your subnets or track your AWS costs.
6.  When all the settings are as you want them, choose **Create**.
7.  In the confirmation message that appears, choose **Close**.

Your new subnet group appears in the **Subnet Groups** list of
the MemoryDB console. At the bottom of the window you can choose the subnet group to see details,
such as all of the subnets associated with this group.

## Creating a subnet group (AWS CLI)

At a command prompt, use the command `create-subnet-group` to create a subnet group.

For Linux, macOS, or Unix:

```
aws memorydb create-subnet-group \
    --subnet-group-name `mysubnetgroup` \
    --description `"Testing"` \
    --subnet-ids `subnet-53df9c3a`
```

For Windows:

```
aws memorydb create-subnet-group ^
    --subnet-group-name `mysubnetgroup` ^
    --description `"Testing"` ^
    --subnet-ids `subnet-53df9c3a`
```

This command should produce output similar to the following:

```
    {
        "SubnetGroup": {
            "Subnets": [
                {
                    "Identifier": "subnet-53df9c3a",
                    "AvailabilityZone": {
                    "Name": "us-east-1a"
                    }
                }
            ],
            "VpcId": "vpc-3cfaef47",
            "Name": "mysubnetgroup",
            "ARN": "arn:aws:memorydb:us-east-1:012345678912:subnetgroup/mysubnetgroup",
            "Description": "Testing"
        }
    }
```

For more information, see the AWS CLI topic create-subnet-group.

## Creating a subnet group (MemoryDB API)

Using the MemoryDB API, call `CreateSubnetGroup` with the following
parameters:

- `SubnetGroupName=``mysubnetgroup`
- `Description=``Testing`
- `SubnetIds.member.1=``subnet-53df9c3a`
