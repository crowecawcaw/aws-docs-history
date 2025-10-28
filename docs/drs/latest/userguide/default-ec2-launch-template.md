# Default Amazon Elastic Compute Cloud (Amazon EC2) launch

template

The default Amazon EC2 launch template sets the default values that are copied to EC2
templates created for newly added source servers. This template defines how drill,
recovery, or failback instances are launched. If you didn't create any default EC2
template, AWS DRS copies the default values for each setting to EC2 launch templates
for newly added servers.

You can usually launch a drill instance without modifying the automatically
created EC2 launch template (unless you have removed the default VPC/subnet from
your AWS account).

###### Topics

- [Editing the default EC2
  launch template](edit-default-ec2-launch-template.md "edit-default-ec2-launch-template.md")
