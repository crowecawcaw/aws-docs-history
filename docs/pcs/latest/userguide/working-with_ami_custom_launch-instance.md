# Step 1 – Launch a temporary

instance

Launch a temporary instance that you can use to install and configure the AWS PCS
software and Slurm scheduler. You use this instance to create an AMI compatible with AWS PCS.

###### To launch a temporary instance

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. In the navigation pane, choose **Instances**, then choose
   **Launch instances** to open the new launch instance wizard.
3. (Optional) In the **Name and tags** section, provide a name for the
   instance, such as `PCS-AMI-instance`. The name is assigned to the instance as a
   resource tag (`Name=PCS-AMI-instance`).
4. In the **Application and OS Images** section, select an AMI for one of
   the [supported operating systems](working-with_ami_installers.md#working-with_ami_installers_os "working-with_ami_installers.md#working-with_ami_installers_os").
5. In the **Instance type** section, select a [supported instance type](working-with_ami_installers.md#working-wth_ami_installers_instance-types "working-with_ami_installers.md#working-wth_ami_installers_instance-types").
6. In the **Key pair** section, select the key pair to use for the
   instance.
7. In the **Network settings** section:
   1. For **Firewall (security groups)**, choose **Select existing
      security group**, then select a security group that allows inbound SSH access to
      your instance.

8. In the **Storage** section, configure the volumes as needed. Make sure
   to configure sufficient space to install your own applications and libraries.
9. In the **Summary** panel, choose **Launch instance**.
