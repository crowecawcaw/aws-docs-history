# Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host

After you have allocated a Dedicated Host, you can launch instances onto it. You can't
launch instances with `host` tenancy if you do not have active Dedicated Hosts with
enough available capacity for the instance type that you are launching.

###### Considerations

- SQL Server, SUSE, and RHEL AMIs provided by Amazon EC2 can't be
  used with Dedicated Hosts.
- For Dedicated Hosts that support multiple instance sizes, we recommend that you launch
  the larger instance sizes first, and then fill the remaining instance capacity
  with the smaller instance sizes as needed.
- Before you launch your instances, take note of the limitations. For more
  information, see [Dedicated Hosts restrictions](dedicated-hosts-overview.md#dedicated-hosts-limitations "dedicated-hosts-overview.md#dedicated-hosts-limitations").

Console

###### To launch an instance onto a specific Dedicated Host from the Dedicated Hosts

page

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Dedicated Hosts** in the navigation
   pane.
3. On the **Dedicated Hosts** page, select a host and
   choose **Actions**, **Launch
   Instance(s) onto host**.
4. In the **Application and OS Images** section,
   select an AMI from the list.
5. In the **Instance type** section, select the
   instance type to launch.

###### Note

If the Dedicated Host supports a single instance type only, the
supported instance type is selected by default and can't be
changed.

If the Dedicated Host supports multiple instance types, you must
select an instance type within the supported instance family
based on the available instance capacity of the Dedicated Host. We
recommend that you launch the larger instance sizes first,
and then fill the remaining instance capacity with the
smaller instance sizes as needed. 6. In the **Key pair** section, select the key
pair to associate with the instance. 7. In the **Advanced details** section, for
**Tenancy affinity**, choose one of the
following:

    * **Off** — Host affinity
     disabled. The instance launches onto the specified host, but
     it is not guaranteed to restart on the same Dedicated Host if stopped.
    * A Dedicated Host ID — Host affinity enabled. If stopped, the
     instance always restarts on this specified host if it has
     capacity. If the host does not have capacity, the instance
     can't be restarted; you must establish affinity with a
     different host.

For more information about Affinity, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").

###### Note

The **Tenancy** and
**Host** options are pre-configured
based on the host that you selected. 8. Configure the remaining instance options as needed. For more
information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md "ec2-instance-launch-parameters.md"). 9. Choose **Launch instance**.

###### To launch an instance onto a Dedicated Host using the Launch Instance

wizard

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  In the navigation pane, choose **Instances**,
    **Launch instance**.
3.  In the **Application and OS Images** section,
    select an AMI from the list.
4.  In the **Instance type** section, select the
    instance type to launch.
5.  In the **Key pair** section, select the key
    pair to associate with the instance.
6.  In the **Advanced details** section, do the
    following:
    1.  For **Tenancy**, select **Dedicated Host**.
    2.  For **Target host by**, select **Host ID**.
    3.  For **Target host ID**, select the
        host onto which to launch the instance.
    4.  For **Tenancy affinity**, choose one of the
        following:

            * **Off** — Host affinity
             disabled. The instance launches onto the specified host, but
             it is not guaranteed to restart on the same Dedicated Host if stopped.
            * A Dedicated Host ID — Host affinity enabled. If stopped, the
             instance always restarts on this specified host if it has
             capacity. If the host does not have capacity, the instance
             can't be restarted; you must establish affinity with a
             different host.

        For more information about Affinity, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").

7.  Configure the remaining instance options as needed. For more
    information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md "ec2-instance-launch-parameters.md").
8.  Choose **Launch instance**.

AWS CLI

###### To launch an instance onto a Dedicated Host

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command and specify the instance
affinity, tenancy, and host in the `--placement`
option.

To launch onto a specific Dedicated Host with host affinity (instance
always restarts on the same host if stopped):

```
--placement Affinity=host,Tenancy=host,HostId=`h-07879acf49EXAMPLE`
```

To launch onto a specific Dedicated Host without host affinity (instance
can restart on any available host):

```
--placement Tenancy=host,HostId=`h-07879acf49EXAMPLE`
```

To launch onto any available
Dedicated Host with auto-placement enabled and matching instance type:

```
--placement Tenancy=host
```

PowerShell

###### To launch an instance onto a Dedicated Host

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet and specify the instance
affinity, tenancy, and host in the `-Placement`
parameter.

To launch onto a specific Dedicated Host with host affinity (instance
always restarts on the same host if stopped):

```
-Placement_Affinity host `
-Placement_Tenancy host `
-Placement_HostId `h-07879acf49EXAMPLE`
```

To launch onto a specific Dedicated Host without host affinity (instance
can restart on any available host):

```
-Placement_Tenancy host `
-Placement_HostId `h-07879acf49EXAMPLE`
```

To launch onto any available
Dedicated Host with auto-placement enabled and matching instance type:

```
-Placement_Tenancy host
```
