# Launch an EC2 instance using details from an existing instance

The Amazon EC2 console provides a **Launch more like this**
option that enables you to use a current instance as a base for launching other
instances. This option automatically populates the Amazon EC2 launch instance wizard with
certain configuration details from the selected instance.

###### Considerations

- We do not clone your instances; we only replicate some of the configuration
  details. To create a copy of your instance, first create an AMI from it, then
  launch more instances from the AMI. Create a [launch template](ec2-launch-templates.md "ec2-launch-templates.md") to ensure that you
  launch your instances using the same launch details.
- The current instance must be in the `running` state.

###### Copied details

The following configuration details are copied from the selected instance into the
launch instance wizard:

- AMI ID
- Instance type
- Availability Zone, or the VPC and subnet in which the selected instance is
  located
- Public IPv4 address. If the selected instance currently has a public IPv4
  address, the new instance receives a public IPv4 address, regardless of the
  selected instance's default public IPv4 address setting. For more information
  about public IPv4 addresses, see [Public IPv4 addresses](using-instance-addressing.md#concepts-public-addresses "using-instance-addressing.md#concepts-public-addresses").
- Placement group, if applicable
- IAM role associated with the instance, if applicable
- Shutdown behavior setting (stop or terminate)
- Termination protection setting (true or false)
- CloudWatch monitoring (enabled or disabled)
- Amazon EBS-optimization setting (true or false)
- Tenancy setting, if launching into a VPC (shared or dedicated)
- Kernel ID and RAM disk ID, if applicable
- User data, if specified
- Tags associated with the instance, if applicable
- Security groups associated with the instance
- [Windows instances] Association information. If the selected instance is
  associated with a configuration file, the same file is automatically associated
  with the new instance. If the configuration file includes a joined domain
  configuration, the new instance is joined to the same domain. For more
  information about joining a domain, see [Seamlessly join a Windows EC2
  instance to your AWS Managed Microsoft AD Active Directory](../../../directoryservice/latest/admin-guide/launching_instance.md "../../../directoryservice/latest/admin-guide/launching_instance.md") in the
  _AWS Directory Service Administration Guide_.

###### Details not copied

The following configuration details are not copied from your selected instance.
Instead, the wizard applies their default settings or behavior:

- Number of network interfaces – The default is one network interface,
  which is the primary network interface (eth0).
- Storage – The default storage configuration is determined by the AMI and
  the instance type.

###### To launch more instances like an existing instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select an instance, and then choose **Actions**,
   **Images and templates**, **Launch more like
   this**.
4. The launch instance wizard opens. You can make any necessary changes to the
   instance configuration by selecting different options on this screen.

When you are ready to launch your instance, choose **Launch
instance**. 5. If the instance fails to launch or the state immediately goes to
`terminated` instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md "troubleshooting-launch.md").
