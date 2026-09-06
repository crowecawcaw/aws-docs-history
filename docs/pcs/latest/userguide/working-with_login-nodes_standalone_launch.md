

# Step 2 – Launch an EC2 instance
<a name="working-with_login-nodes_standalone_launch"></a>

**To launch an EC2 instance**

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2).

1. In the navigation pane, choose **Instances**, and then choose **Launch Instances** to open the new launch instance wizard.

1. (Optional) In the **Name and tags** section, provide a name for the instance, such as `PCS-LoginNode`. The name is assigned to the instance as a resource tag (`Name=PCS-LoginNode`).

1. In the **Application and OS Images** section, select an AMI for one of the operating systems supported by AWS PCS. For more information, see [Supported operating systems](working-with_ami_installers.md#working-with_ami_installers_os).

1. In the **Instance type** section, select a supported instance type. For more information, see [Supported instance types](working-with_ami_installers.md#working-wth_ami_installers_instance-types).

1. In the **Key pair** section, select the SSH key pair to use for the instance.

1. In the **Network settings** section:

   1. Choose **Edit**.

     1. Select the VPC of your AWS PCS cluster.

     1. For **Firewall (security groups)**, choose **Select existing security group**.

        1. Select a security group that permits traffic between the instance and the target AWS PCS cluster’s Slurm controller. For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements).

        1. (Optional) Select a security group that allows inbound SSH access to your instance.

1. In the **Storage** section, configure storage volumes as needed. Make sure to configure sufficient space to install applications and libraries to enable your use case.

1.  Under **Advanced**, choose an IAM role that allows access to the cluster secret. For more information, see [Get the Slurm cluster secret](working-with_clusters_secrets_get.md). 

1.  In the **Summary** pane, choose **Launch instance**. 