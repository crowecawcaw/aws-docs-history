# Using Amazon EC2 launch templates

with AWS PCS

In Amazon EC2, a launch template can store a set of preferences so that you don't have to
specify them individually when you launch instances. AWS PCS incorporates launch templates as a
flexible way to configure compute node groups. When you create a node group, you provide a launch
template. AWS PCS creates a derived launch template from it that includes transformations to help ensure it works with
the service.

Understanding what the options and considerations are when writing a custom launch template
can help you write one for use with AWS PCS. For more information on launch templates, see
Launching an Instance from a [Launch an instance from a launch
template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md") in the _Amazon EC2 User Guide_.

###### Topics

- [Overview of launch templates in AWS PCS](working-with_launch-templates_overview.md "working-with_launch-templates_overview.md")
- [Create a basic launch template](working-with_launch-templates_create.md "working-with_launch-templates_create.md")
- [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md "working-with_ec2-user-data.md")
- [Capacity Reservations in AWS PCS](working-with_capacity-reservations.md "working-with_capacity-reservations.md")
- [Useful launch template
  parameters](working-with_launch-templates_parameters.md "working-with_launch-templates_parameters.md")
