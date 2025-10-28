# Change the tenancy of an EC2 instance

You can change the tenancy of a stopped instance after launch.
The changes that you make take effect the next time the instance starts.

Alternatively, you can change the tenancy of your virtual private cloud (VPC). For more
information, see [Change the instance tenancy of a VPC](change-tenancy-vpc.md "change-tenancy-vpc.md").

###### Limitations

- You can't change the tenancy of an instance using the AWS Management Console.
- The instance must be in the `stopped` state.
- The operating system details of your instance—and whether SQL Server is
  installed—affect what conversions are supported. For more information about
  the tenancy conversion paths available to your instance, see [Tenancy
  conversion](../../../license-manager/latest/userguide/conversion-tenancy.md "../../../license-manager/latest/userguide/conversion-tenancy.md") in the _License Manager User Guide_.
- For T3 instances, you must launch the instance on a Dedicated Host to use a
  tenancy of `host`. You can't change the tenancy from
  `host` to `dedicated` or `default`.
  Attempting to make one of these unsupported tenancy changes results in an
  `InvalidRequest` error code.

AWS CLI

###### To modify the tenancy value of an instance

Use the [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") command.

```
aws ec2 modify-instance-placement \
    --instance-id `i-1234567890abcdef0` \
    --tenancy `dedicated`
```

PowerShell

###### To modify the tenancy value of an instance

Use the [Edit-EC2InstancePlacement](../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md "../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md") cmdlet.

```
Edit-EC2InstancePlacement `
    -InstanceId `i-1234567890abcdef0` `
    -Tenancy `Dedicated`
```
