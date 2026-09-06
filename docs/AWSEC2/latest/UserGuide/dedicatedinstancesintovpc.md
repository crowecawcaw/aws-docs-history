

# Launch Dedicated Instances into a VPC with default tenancy
<a name="dedicatedinstancesintovpc"></a>

When you create a VPC, you have the option of specifying its instance tenancy. If you launch an instance into a VPC that has an instance tenancy of `dedicated`, it runs as a Dedicated Instance on hardware that's dedicated for your use.

For more information about launching an instance with a tenancy of `host`, see [Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host](launching-dedicated-hosts-instances.md).

For more information about VPC tenancy options, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon VPC User Guide*.

**Requirements**
+ Choose a supported instance type. For more information, see [Amazon EC2 Dedicated Instances](https://aws.amazon.com/ec2/pricing/dedicated-instances/).

------
#### [ Console ]

**To launch a Dedicated Instance into a default tenancy VPC**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**, **Launch instance**.

1. In the **Application and OS Images** section, select an AMI from the list.

1. In the **Instance type** section, select the instance type to launch.

1. In the **Key pair** section, select the key pair to associate with the instance.

1. In the **Advanced details** section, for **Tenancy**, select **Dedicated**.

1. Configure the remaining instance options as needed. For more information, see [Reference for Amazon EC2 instance configuration parameters](ec2-instance-launch-parameters.md).

1. Choose **Launch instance**.

------
#### [ AWS CLI ]

**To set the tenancy option for an instance during launch**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command and include `Tenancy` with the `--placement` option.

```
--placement Tenancy=dedicated
```

------
#### [ PowerShell ]

**To set the tenancy option for an instance during launch**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet with the `-Placement_Tenancy` parameter.

```
-Placement_Tenancy dedicated
```

------