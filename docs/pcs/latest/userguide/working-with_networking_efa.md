# Using Elastic Fabric Adapter (EFA) with

AWS PCS

Elastic Fabric Adapter (EFA) is a high performance advanced networking interconnect from AWS
that you can attach to your EC2 instance to accelerate High Performance Computing (HPC) and
machine learning applications. Enabling your applications running on an AWS PCS cluster with
EFA involves configuring the AWS PCS compute node group instances to use EFA as follows.

###### Note

Install EFA on an AWS PCS-compatible AMI –
The AMI used in the AWS PCS compute node group must have the EFA driver installed and
loaded. For information on how to build a custom AMI with EFA software installed, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

###### Contents

- [Identify EFA-enabled EC2
  instances](working-with_networking_efa_identify-instances.md "working-with_networking_efa_identify-instances.md")
- [Create a security group to support EFA
  communications](working-with_networking_efa_create-sg.md "working-with_networking_efa_create-sg.md")
- [(Optional) Create a
  placement group](working-with_networking_efa_create-placement-group.md "working-with_networking_efa_create-placement-group.md")
- [Create or update an EC2 launch
  template](working-with_networking_efa_create-lt.md "working-with_networking_efa_create-lt.md")
- [Create or update compute node
  groups for EFA](working-with_networking_efa_create-cng.md "working-with_networking_efa_create-cng.md")
- [(Optional) Test EFA](working-with_networking_efa_test-efa.md "working-with_networking_efa_test-efa.md")
- [(Optional) Use a CloudFormation
  template to create an EFA-enabled launch template](working-with_networking_efa_create-lt-cfn.md "working-with_networking_efa_create-lt-cfn.md")
