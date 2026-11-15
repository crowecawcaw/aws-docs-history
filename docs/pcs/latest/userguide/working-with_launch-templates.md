

# Using Amazon EC2 launch templates with AWS PCS
<a name="working-with_launch-templates"></a>

A custom launch template is optional. You can configure the AMI, security groups, and SSH key pair directly on a compute node group. These are called instance settings. If you specify an instance setting both on the compute node group and in your launch template, AWS PCS uses the value on the compute node group instead of the value in the launch template. For more information, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

In Amazon EC2, a launch template can store a set of preferences so that you don't have to specify them individually when you launch instances. AWS PCS can use a launch template to configure compute node groups. When you create a compute node group with launch template configuration, you provide a custom launch template. AWS PCS also creates a launch template of its own from the settings on the compute node group and your custom launch template. AWS PCS doesn't change your launch template. For more information, see [Launch templates that AWS PCS creates](working-with_cng_create.md#working-with_cng_create_pcs-launch-templates).

The topics in this chapter describe options and considerations for writing a custom launch template for AWS PCS. For more information about launch templates, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Overview of launch templates in AWS PCS](working-with_launch-templates_overview.md)
+ [Create a basic launch template](working-with_launch-templates_create.md)
+ [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md)
+ [Capacity Reservations in AWS PCS](working-with_capacity-reservations.md)
+ [Useful launch template parameters](working-with_launch-templates_parameters.md)