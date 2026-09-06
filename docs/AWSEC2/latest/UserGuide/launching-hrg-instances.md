

# Launch Amazon EC2 instances into a host resource group
<a name="launching-hrg-instances"></a>

Dedicated Hosts are also integrated with AWS License Manager. With License Manager, you can create a host resource group, which is a collection of Dedicated Hosts that are managed as a single entity. When creating a host resource group, you specify the host management preferences, such as auto-allocate and auto-release, for the Dedicated Hosts. This allows you to launch instances onto Dedicated Hosts without manually allocating and managing those hosts. For more information, see [ Host Resource Groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html) in the *AWS License Manager User Guide*.

When you launch an instance into a host resource group that has a Dedicated Host with available instance capacity, Amazon EC2 launches the instance onto that host. If the host resource group does not have a host with available instance capacity, Amazon EC2 automatically allocates a new host in the host resource group, and then launches the instance onto that host. For more information, see [ Host Resource Groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html) in the *AWS License Manager User Guide*.

**Requirements and limits**
+ Creating license configurations (self-managed licenses) for host resource groups is optional:
  + If you required license configurations when creating the host resource group, you can launch instances only from AMIs with a matching core- or socket-based license configuration.
  + If you created the host resource group to not require license configurations, you do not need to set up self-managed licenses or associate an AMI.
+ You can't use SQL Server, SUSE, or RHEL AMIs provided by Amazon EC2 with Dedicated Hosts.
+ You can't target a specific host by choosing a host ID, and you can't enable instance affinity when launching an instance into a host resource group.

------
#### [ Console ]

**To launch an instance into a host resource group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**, **Launch instance**.

1. In the **Application and OS Images** section, select an AMI from the list.

1. In the **Instance type** section, select the instance type to launch.

1. In the **Key pair** section, select the key pair to associate with the instance.

1. In the **Advanced details** section, do the following:

   1. For **Tenancy**, select **Dedicated Host**.

   1. For **Target host by**, select **Host resource group**.

   1. For **Tenancy host resource group**, select the host resource group into which to launch the instance.

   1. For **Tenancy affinity**, do one of the following:
      + Select **Off** — The instance launches onto the specified host, but it is not guaranteed to restart on the same Dedicated Host if stopped.
      + Select the Dedicated Host ID — If stopped, the instance always restarts on this specific host. 

      For more information about Affinity, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md).

1. Configure the remaining instance options as needed. For more information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md).

1. Choose **Launch instance**.

------
#### [ AWS CLI ]

**To launch an instance into a host resource group**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command. In the `--placement` option, omit the tenancy and specify the ARN of the host resource group.

```
--placement HostResourceGroupArn=arn:aws:resource-groups:{{us-east-2}}:{{123456789012}}:group/{{my-resource-group}}
```

------
#### [ PowerShell ]

**To launch an instance into a host resource group**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet. In the `-Placement` parameter, omit the tenancy and specify the ARN of the host resource group.

```
-Placement_HostResourceGroupArn arn:aws:resource-groups:{{us-east-2}}:{{123456789012}}:group/{{my-resource-group}}
```

------