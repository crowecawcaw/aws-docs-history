# Using AWS CloudShell in Amazon VPC

AWS CloudShell virtual private cloud (VPC) enables you to create a CloudShell environment in
your VPC. For each VPC environment, you can assign a VPC, add a subnet, and associate up to five
security groups. AWS CloudShell inherits the network configuration of the VPC and enables you to use
AWS CloudShell securely within the same subnet as other resources in the VPC and connect to them.

With Amazon VPC, you can launch AWS resources in a logically isolated virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. For more information about VPC, see [Amazon Virtual Private Cloud](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

## Operating constraints

AWS CloudShell VPC environments have the following constraints:

- You can create a maximum of two VPC environments per IAM principal.
- You can assign a maximum of five security groups for a VPC environment.
- You cannot use the CloudShell upload and download options in the Actions menu
  for VPC environments.

###### Note

It is possible to upload or download files from VPC environments that have
access to the internet ingress/egress through other CLI tools.

- VPC environments do not support persistent storage. Storage is ephemeral. Data and
  home directory are deleted when an active environment session ends.
- Your AWS CloudShell environment can only connect to the internet if it is in a private
  VPC subnet.

###### Note

Public IP addresses are not allocated to CloudShell VPC environments by
default. VPC environments created in public subnets with routing tables configured
to route all traffic to Internet Gateway will not have access to public internet,
but private subnets configured with Network Address Translation (NAT) have access
to public internet. VPC environments created in such private subnets will have
access to public internet.

- To provide a managed CloudShell environment for your account, AWS might provision
  network access to the following services for the underlying compute host:

      + Amazon S3
      + VPC endpoints




      	- com.amazonaws.<region>.ssmmessages
      	- com.amazonaws.<region>.logs
      	- com.amazonaws.<region>.kms
      	- com.amazonaws.<region>.execute-api
      	- com.amazonaws.<region>.ecs-telemetry
      	- com.amazonaws.<region>.ecs-agent
      	- com.amazonaws.<region>.ecs
      	- com.amazonaws.<region>.ecr.dkr
      	- com.amazonaws.<region>.ecr.api
      	- com.amazonaws.<region>.codecatalyst.packages
      	- com.amazonaws.<region>.codecatalyst.git
      	- aws.api.global.codecatalyst

  You cannot restrict access to these endpoints by modifying your VPC
  configuration.

CloudShell VPC is available in all AWS
Regions and
GovCloud Regions. For a list of Regions in which CloudShell VPC is
available, see [Supported AWS Regions for
AWS CloudShell](supported-aws-regions.md "supported-aws-regions.md").
