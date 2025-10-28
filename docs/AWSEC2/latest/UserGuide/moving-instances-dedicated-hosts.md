# Modify Amazon EC2 Dedicated Host tenancy and affinity for an Amazon EC2 instance

You can change the tenancy of an instance after
you have launched it. You can also modify the affinity for your instance to target a
specific host or allow it to launch on any available dedicated host with matching
attributes in your account. To modify either instance tenancy or affinity, the
instance must be in the `stopped` state.

The operating system details of your instance—and whether SQL Server is
installed—affect what conversions are supported. For more information about
the tenancy conversion paths available to your instance, see [Tenancy
conversion](../../../license-manager/latest/userguide/conversion-tenancy.md "../../../license-manager/latest/userguide/conversion-tenancy.md") in the _License Manager User Guide_.

###### Note

For T3 instances, you must launch the instance on a Dedicated Host to use a
tenancy of `host`. For T3 instances, you can't change the tenancy
from `host` to `dedicated` or `default`.
Attempting to make one of these unsupported tenancy changes results in an
`InvalidRequest` error code.

Console

###### To modify instance tenancy or affinity

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  Choose **Instances**, and select the instance
    to modify.
3.  Choose **Instance state**,
    **Stop**.
4.  With the instance selected, choose
    **Actions**, **Instance
    settings**, **Modify instance
    placement**.
5.  On the **Modify instance placement** page,
    configure the following:

        * **Tenancy**—Choose one of the
         following:




        	+ Run a dedicated hardware
        	 instance—Launches the instance as a Dedicated Instance.
        	 For more information, see [Amazon EC2 Dedicated Instances](dedicated-instance.md "dedicated-instance.md").
        	+ Launch the instance on a Dedicated Host—Launches
        	 the instance onto a Dedicated Host with configurable
        	 affinity.
        * **Affinity**—Choose one of the
         following:




        	+ This instance can run on any one of my
        	 hosts—The instance launches onto any
        	 available Dedicated Host in your account that supports its
        	 instance type.
        	+ This instance can only run on the selected
        	 host—The instance is only able to run on the
        	 Dedicated Host selected for **Target
        	 Host**.
        * **Target Host**—Select the Dedicated Host
         that the instance must run on. If no target host is
         listed, you might not have available, compatible Dedicated Hosts
         in your account.

    For more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").

6.  Choose **Save**.

AWS CLI

###### To modify instance tenancy or affinity

Use the [modify-instance-placement](../../../cli/latest/reference/ec2/modify-instance-placement.md "../../../cli/latest/reference/ec2/modify-instance-placement.md") command. The following
example changes the specified instance's affinity from
`default` to `host`, and specifies the
Dedicated Host that the instance has affinity with.

```
aws ec2 modify-instance-placement \
    --instance-id `i-1234567890abcdef0` \
    --affinity `host` \
    --tenancy `host` \
    --host-id `h-012a3456b7890cdef`
```

PowerShell

###### To modify instance tenancy or affinity

Use the [Edit-EC2InstancePlacement](../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md "../../../powershell/latest/reference/items/Edit-EC2InstancePlacement.md") cmdlet. The
following example changes the specified instance's affinity from
`default` to `host`, and specifies the
Dedicated Host that the instance has affinity with.

```
Edit-EC2InstancePlacement `
    -InstanceId `i-1234567890abcdef0` `
    -Affinity `host` `
    -Tenancy `host` `
    -HostId `h-012a3456b7890cdef`
```
