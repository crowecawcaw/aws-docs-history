# AWS PCS Networking

Your AWS PCS cluster is created in an Amazon VPC. This chapter includes the following topics
about networking for your cluster’s scheduler and nodes.

Except for choosing a subnet to launch instances in, you must use EC2 launch templates to
configure networking for AWS PCS compute node groups. For more information about
launch templates, see [Using Amazon EC2 launch templates
with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").

###### Topics

- [AWS PCS VPC and subnet requirements
  and considerations](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md")
- [Creating a VPC for your AWS PCS
  cluster](working-with_networking_create-vpc.md "working-with_networking_create-vpc.md")
- [Security groups in AWS PCS](working-with_networking_sg.md "working-with_networking_sg.md")
- [Multiple network interfaces in
  AWS PCS](working-with_networking_multi-nic.md "working-with_networking_multi-nic.md")
- [Placement groups for EC2 instances in
  AWS PCS](working-with_networking_placement-groups.md "working-with_networking_placement-groups.md")
- [Using Elastic Fabric Adapter (EFA) with
  AWS PCS](working-with_networking_efa.md "working-with_networking_efa.md")
