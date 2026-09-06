

# Network settings
<a name="configure-vpc-networking-iam-based-domains"></a>

When you configure VPC networking for your domain, all projects created after the configuration will automatically use the specified VPC. You can choose to update existing projects that do not have a VPC configured — see [Update VPC configuration and projects](update-individual-projects-vpc.md).

VPC configuration applies to the life of a project. VPC connection information can change the VPC itself, the subnets within, or the security group. These changes apply to projects created after the VPC is modified.

## Prerequisites
<a name="prerequisites-vpc-networking"></a>
+ Domain administrator permissions for Amazon SageMaker Unified Studio
+ An existing VPC that meets the following requirements:
  + At least 2 private subnets in different Availability Zones
  + DNS hostname and DNS support enabled
  + At least 5 free IP addresses per Amazon SageMaker Unified Studio project
+ Appropriate IAM permissions to access VPC resources

## Add VPC
<a name="add-vpc-networking"></a>

To add a VPC, complete the following steps:

1. From the domain administration page, choose **Settings** in the left navigation pane.

1. In the **Networking** section, choose **Add VPC**. IAM-based domains support only one VPC configuration at a time. Identity Center-based domains can have a VPC per Region to support accounts that are associated with the domain.

1. In the **VPC** section, choose **Select** and select the VPC where your compute resources will be housed.
**Note**  
If no VPC has been set up for use with Amazon SageMaker Unified Studio, you can choose **Create VPC** to create a new VPC using AWS CloudFormation.

1. In the **Subnets** section, choose **Select** and select at least two subnets in different Availability Zones.
**Warning**  
Your subnets must be private or some functionality will not be available. Select subnets configured with the required VPC endpoints to establish connectivity to AWS services.

1. In the **Security group** section, select a security group. If a security group is not selected, the service creates one for the VPC.

1. Choose **Save**.

You can now view the configured VPC details in the **Networking** section of the Settings tab. All new projects created in the domain will use this VPC configuration.