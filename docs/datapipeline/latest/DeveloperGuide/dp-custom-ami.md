AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Task Runner and Custom AMIs

When you specify an `Ec2Resource` object for your pipeline, AWS Data Pipeline creates
an EC2 instance for you, using an AMI that installs and configures Task Runner for
you. A PV-compatible instance type is required in this case. Alternatively, you can
create a custom AMI with Task Runner, and then specify the ID of this AMI using the
`imageId` field of the `Ec2Resource` object. For more
information, see [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md").

A custom AMI must meet the following requirements for AWS Data Pipeline to use it
successfully for Task Runner:

- Create the AMI in the same region in which the instances will run. For more
  information, see [Creating Your
  Own AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami.md "../../../AWSEC2/latest/UserGuide/creating-an-ami.md") in the _Amazon EC2 User Guide_.
- Ensure that the virtualization type of the AMI is supported by
  the instance type you plan to use. For example, the I2 and G2 instance
  types require an HVM AMI and the T1, C1, M1, and M2 instance types
  require a PV AMI. For more information, see [Linux AMI Virtualization Types](../../../AWSEC2/latest/UserGuide/virtualization_types.md "../../../AWSEC2/latest/UserGuide/virtualization_types.md") in the _Amazon EC2 User Guide_.
- Install the following software:
  - Linux
  - Bash
  - wget
  - unzip
  - Java 1.6 or 1.8
  - cloud-init

- Create and configure a user named `ec2-user`.
