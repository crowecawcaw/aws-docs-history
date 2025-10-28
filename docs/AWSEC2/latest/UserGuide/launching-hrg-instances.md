# Launch Amazon EC2 instances into a host resource group

Dedicated Hosts are also integrated with AWS License Manager. With License Manager, you can create a host resource
group, which is a collection of Dedicated Hosts that are managed as a single entity. When creating
a host resource group, you specify the host management preferences, such as
auto-allocate and auto-release, for the Dedicated Hosts. This allows you to launch instances onto
Dedicated Hosts without manually allocating and managing those hosts. For more information, see
[Host Resource
Groups](../../../license-manager/latest/userguide/host-resource-groups.md "../../../license-manager/latest/userguide/host-resource-groups.md") in the _AWS License Manager User Guide_.

When you launch an instance into a host resource group that has a Dedicated Host with
available instance capacity, Amazon EC2 launches the instance onto that host. If the host
resource group does not have a host with available instance capacity, Amazon EC2
automatically allocates a new host in the host resource group, and then launches the
instance onto that host. For more information, see [Host Resource
Groups](../../../license-manager/latest/userguide/host-resource-groups.md "../../../license-manager/latest/userguide/host-resource-groups.md") in the _AWS License Manager User Guide_.

###### Requirements and limits

- You must associate a core- or socket-based license configuration with the
  AMI.
- You can't use SQL Server, SUSE, or RHEL AMIs provided
  by Amazon EC2 with Dedicated Hosts.
- You can't target a specific host by choosing a host ID, and you can't
  enable instance affinity when launching an instance into a host resource
  group.

Console

###### To launch an instance into a host resource group

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
    1.  For **Tenancy**, select
        **Dedicated Host**.
    2.  For **Target host by**, select
        **Host resource group**.
    3.  For **Tenancy host resource group**,
        select the host resource group into which to launch the
        instance.
    4.  For **Tenancy affinity**, do one of
        the following:

            * Select **Off**
             — The instance launches onto the specified
             host, but it is not guaranteed to restart on the
             same Dedicated Host if stopped.
            * Select the Dedicated Host ID — If stopped, the
             instance always restarts on this specific host.

        For more information about Affinity, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").

7.  Configure the remaining instance options as needed. For more
    information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md "ec2-instance-launch-parameters.md").
8.  Choose **Launch instance**.

AWS CLI

###### To launch an instance into a host resource group

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command. In the
`--placement` option, omit the tenancy
and specify the ARN of the host resource group.

```
--placement HostResourceGroupArn=arn:aws:resource-groups:`us-east-2`:`123456789012`:group/`my-resource-group`
```

PowerShell

###### To launch an instance into a host resource group

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet. In the
`-Placement` parameter, omit the tenancy
and specify the ARN of the host resource group.

```
-Placement_HostResourceGroupArn arn:aws:resource-groups:`us-east-2`:`123456789012`:group/`my-resource-group`
```
