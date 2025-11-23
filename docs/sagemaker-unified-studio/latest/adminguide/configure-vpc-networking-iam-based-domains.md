# Configure VPC Networking for

Amazon SageMaker Unified Studio Domain

Amazon Virtual Private Cloud (Amazon VPC) networking with subnets is required when using
certain compute services within Amazon SageMaker Unified Studio. You configure VPC networking at the domain
level to provide network isolation and connectivity for compute resources, database
connections, and other AWS services.

When you configure VPC networking for your domain, all projects created after the
configuration will automatically use the specified VPC. You can choose to update existing
projects immediately or update them individually at a later time.

VPC configuration is permanent once applied to a domain and cannot be changed or removed
after it is saved.

Prerequisites:

- Domain administrator permissions for Amazon SageMaker Unified Studio
- An existing VPC that meets the following requirements:
  - At least 2 private subnets in different Availability Zones
  - DNS hostname and DNS support enabled
  - At least 5 free IP addresses per Amazon SageMaker Unified Studio project

- Appropriate IAM permissions to access VPC resources

1. From the domain administration page, choose **Settings** in the
   left navigation pane.
2. In the **Networking** section, choose **Add
   VPC**.
3. In the **Add VPC** dialog, review the warning message that VPC
   configuration cannot be changed after it is added.
4. In the **VPC** section, choose **Select** and
   select the VPC where your compute resources will be housed.

###### Note

If no VPC has been set up for use with Amazon SageMaker Unified Studio, you can choose
**Create VPC** to create a new VPC using AWS
CloudFormation. 5. In the **Subnets** section, choose **Select** and
select at least two subnets in different Availability Zones.

###### Warning

Your subnets must be private or some functionality will not be available. Select
subnets configured with the required VPC endpoints to establish connectivity to AWS
services. 6. In the **Project update option** section, choose one of the
following:

    * Update all projects immediately - All existing projects will be updated
     automatically after saving. This may take a few minutes for domains with more than
     20 projects.
    * Update projects separately - Go to each project detail page and manually update
     projects with the VPC configuration.

7. Choose **Save & Update**.
   You can now view the configured VPC details in the **Networking**
   section of the Settings tab. All new projects created in the domain will use this VPC
   configuration.
