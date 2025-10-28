# Network and Storage

The following topic describes network access and data storage considerations for your RStudio
instance. For general information about network access and data storage when using Amazon SageMaker AI,
see [Data Protection in Amazon SageMaker AI](data-protection.md "data-protection.md").

**Amazon EFS volume**

RStudio on Amazon SageMaker AI shares an Amazon EFS volume with the Amazon SageMaker Studio Classic application in the
domain. When the RStudio application is added to a domain, SageMaker AI creates a folder named
`shared` in the Amazon EFS directory. If this `shared` folder is deleted or
changed manually, then the RStudio application may no longer function. For more information
about the Amazon EFS volume, see [Manage Your Amazon EFS Storage Volume in Amazon SageMaker Studio Classic](studio-tasks-manage-storage.md "studio-tasks-manage-storage.md").

**Installed packages and scripts**

Packages that you install from within RStudio are scoped to the user profile level. This
means that the installed package persists through RSession shut down, restarts, and across
RSessions for each user profile that they are installed in. R Scripts that are saved in
RSessions behave the same way. Both packages and R Scripts are saved in the user's Amazon EFS
volume.

**Encryption**

RStudio on Amazon SageMaker AI supports encryption at rest.

**Use RStudio in VPC-only mode**

RStudio on Amazon SageMaker AI supports [AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") integration.
With this integration, you can use RStudio on SageMaker AI in VPC-only mode without direct access to the
internet. When you use RStudio in VPC-only mode, your security groups are automatically managed
by the service. This includes connectivity between your RServer and your RSessions.

The following are required to use RStudio in VPC-only mode. For more information on
selecting a VPC, see [Choose an Amazon VPC](onboard-vpc.md "onboard-vpc.md").

- A private subnet with either access the internet to make a call to Amazon SageMaker AI &
  License Manager, or Amazon Virtual Private Cloud (Amazon VPC) endpoints for both Amazon SageMaker AI & License Manager.
- The domain cannot have any more than two associated Security Groups.
- A Security Group ID for use with the domain in domain Settings. This must allow
  all outbound access.
- A Security Group ID for use with the Amazon VPC endpoint. This security group must allow
  inbound traffic from the domain Security Group ID.
- Amazon VPC Endpoint for `sagemaker.api` and AWS License Manager. This
  must be in the same Amazon VPC as the private subnet.
