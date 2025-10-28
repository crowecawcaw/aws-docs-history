# Change the instance tenancy of a VPC

You can change the instance tenancy of a virtual private cloud (VPC) from
`dedicated` to `default` after you create it. Modifying the
instance tenancy of a VPC does not affect the tenancy of any existing instances in the
VPC. The next time that you launch an instance in the VPC, it has a tenancy of
`default`, unless you specify otherwise during instance launch.

Alternatively, you can change the tenancy of specific instances. For more information, see
[Change the tenancy of an EC2 instance](dedicated-change-tenancy.md "dedicated-change-tenancy.md").

###### Limitations

- You can't change the instance tenancy of a VPC from `default` to
  `dedicated` after it is created.
- You can't modify the instance tenancy of a VPC using the AWS Management Console.

AWS CLI

###### To modify the instance tenancy attribute of a VPC

Use the [modify-vpc-tenancy](../../../cli/latest/reference/ec2/modify-vpc-tenancy.md "../../../cli/latest/reference/ec2/modify-vpc-tenancy.md")
command. The only supported tenancy value is `default`.

```
aws ec2 modify-vpc-tenancy \
    --vpc-id `vpc-1234567890abcdef0` \
    --instance-tenancy default
```

PowerShell

###### To modify the instance tenancy attribute of a VPC

Use the [Edit-EC2VpcTenancy](../../../powershell/latest/reference/items/Edit-EC2VpcTenancy.md "../../../powershell/latest/reference/items/Edit-EC2VpcTenancy.md")
cmdlet. The only supported tenancy value is `Default`.

```
Edit-EC2VpcTenancy `
    -VpcId `vpc-1234567890abcdef0` `
    -InstanceTenancy Default
```
