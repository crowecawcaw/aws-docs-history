# Viewing subnet group details

The following procedures show you how to view details a subnet group.

## Viewing details of subnet groups (console)

###### To view details of a subnet group (Console)

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. In the left navigation pane, choose **Subnet Groups**.
3. On the **Subnet groups** page, choose the subnet group under **Name** or enter the subnet group's name
   in the search bar.
4. On the **Subnet groups** page, choose the subnet group under **Name** or enter the subnet group's name
   in the search bar.
5. Under **Subnet group settings** you can view the name,description, VPC ID and Amazon Resource Name (ARN) of the subnet group.
6. Under **Subnets** you can view the Availability Zones, Subnet IDs and CIDR blocks of the subnet group
7. Under **Tags** you can view any tags associated with the subnet group.

## Viewing subnet groups details (AWS CLI)

At a command prompt, use the command `describe-subnet-groups` to
view a specified subnet group's details.

For Linux, macOS, or Unix:

```
aws memorydb describe-subnet-groups \
    --subnet-group-name `mysubnetgroup`
```

For Windows:

```
aws memorydb describe-subnet-groups ^
    --subnet-group-name `mysubnetgroup`
```

This command should produce output similar to the following:

```
{
  "subnetgroups": [
    {
      "Subnets": [
        {
          "Identifier": "subnet-060cae3464095de6e", 
          "AvailabilityZone": {
            "Name": "us-east-1a"
          }
        }, 
        {
          "Identifier": "subnet-049d11d4aa78700c3", 
          "AvailabilityZone": {
            "Name": "us-east-1c"
          }
        }, 
        {
          "Identifier": "subnet-0389d4c4157c1edb4", 
          "AvailabilityZone": {
            "Name": "us-east-1d"
          }
        }
      ], 
      "VpcId": "vpc-036a8150d4300bcf2", 
      "Name": "mysubnetgroup", 
      "ARN": `"arn:aws:memorydb:us-east-1:53791xzzz7620:subnetgroup/mysubnetgroup"`, 
      "Description": "test"
    }
  ]
}
```

To view details on all subnet groups, use the same command but without specifying a subnet group name.

```
aws memorydb describe-subnet-groups
```

For more information, see the AWS CLI topic describe-subnet-groups.

## Viewing subnet groups (MemoryDB API)

Using the MemoryDB API, call `DescribeSubnetGroups` with the following
parameters:

`SubnetGroupName=``mysubnetgroup`

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
    &Timestamp=20211801T220302Z
    &Version=2021-01-01
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20210801T220302Z
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Signature=<signature>
    &X-Amz-SignedHeaders=Host
```
