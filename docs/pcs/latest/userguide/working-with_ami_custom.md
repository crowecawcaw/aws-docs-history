# Custom Amazon Machine Images (AMIs) for

AWS PCS

AWS PCS is designed to work with Amazon Machine Images (AMI) that you bring to the
service. These AMIs can have arbitrary software and configurations installed on them, so long as
they have the AWS PCS agent and a compatible version of Slurm installed and configured
correctly. You must use AWS-provided installers to install the AWS PCS software on your
custom AMI. We recommend you use AWS-provided installers to install Slurm on your custom AMI but
you can install Slurm on your own if you prefer (not recommended).

###### Note

If you want to try AWS PCS without building a custom AMI, you can use a sample AMI
provided by AWS. For more information, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md "working-with_ami_samples.md").

###### Important

AWS PCS currently requires a kernel with IPv4 support for local node
communication, even when you use AWS PCS in an IPv6-only network.

This tutorial helps you create an AMI that can be used with PCS compute node groups to power
your HPC and AI/ML workloads.

###### Topics

- [Step 1 – Launch a temporary
  instance](working-with_ami_custom_launch-instance.md "working-with_ami_custom_launch-instance.md")
- [Step 2 – Install the AWS PCS
  agent](working-with_ami_custom_install-agent.md "working-with_ami_custom_install-agent.md")
- [Step 3 – Install Slurm](working-with_ami_custom_install-slurm.md "working-with_ami_custom_install-slurm.md")
- [Step 4 – (Optional) Install
  additional drivers, libraries, and application software](working-with_ami_custom_install-software.md "working-with_ami_custom_install-software.md")
- [Step 5 – Create an AMI compatible
  with AWS PCS](working-with_ami_custom_create-ami.md "working-with_ami_custom_create-ami.md")
- [Step 6 – Use the custom AMI with an
  AWS PCS compute node group](working-with_ami_custom_use-ami.md "working-with_ami_custom_use-ami.md")
- [Step 7 – Terminate the
  temporary instance](working-with_ami_custom_terminate-instance.md "working-with_ami_custom_terminate-instance.md")
