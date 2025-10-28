# Launch Dedicated Instances into a VPC with default tenancy

When you create a VPC, you have the option of specifying its instance tenancy. If
you launch an instance into a VPC that has an instance tenancy of `dedicated`,
it runs as a Dedicated Instance on hardware that's dedicated for your use.

For more information about launching an instance with a tenancy of `host`,
see [Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host](launching-dedicated-hosts-instances.md "launching-dedicated-hosts-instances.md").

For more information about VPC tenancy options, see [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the _Amazon VPC User Guide_.

###### Requirements

- Choose a supported instance type. For more information, see [Amazon EC2 Dedicated Instances](https://aws.amazon.com/ec2/pricing/dedicated-instances/ "https://aws.amazon.com/ec2/pricing/dedicated-instances/").

Console

###### To launch a Dedicated Instance into a default tenancy VPC

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, **Launch instance**.
3. In the **Application and OS Images** section, select an AMI from the list.
4. In the **Instance type** section, select the instance type to launch.
5. In the **Key pair** section, select the key pair to associate with the instance.
6. In the **Advanced details** section, for **Tenancy**, select
   **Dedicated**.
7. Configure the remaining instance options as needed. For more information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md "ec2-instance-launch-parameters.md").
8. Choose **Launch instance**.

AWS CLI

###### To set the tenancy option for an instance during launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command and include `Tenancy` with the `--placement` option.

```
--placement Tenancy=dedicated
```

PowerShell

###### To set the tenancy option for an instance during launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-Placement_Tenancy` parameter.

```
-Placement_Tenancy dedicated
```
