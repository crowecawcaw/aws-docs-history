# Finding the data you need (SKMS), AMS

Finding the data you need when using your AWS Managed Services (AMS) accounts calls on the AMS service knowledge management, or SKMS, system. AMS.

SKMS stands for service knowledge management system and refers to all information related
to the AWS Managed Services (AMS) service for a customer. AMS has an SKMS API for finding data.

###### Topics

- [What Is service knowledge management?](#what-is-skms "#what-is-skms")
- [Finding VPC IDs in AMS](find-vpc.md "find-vpc.md")
- [Finding subnet IDs in AMS](find-subnet.md "find-subnet.md")
- [Find AMI IDs, AMS](find-ami.md "find-ami.md")
- [Find security group (SG) IDs, AMS](find-SGs.md "find-SGs.md")
- [Find IAM entities in AMS](find-iam-entities.md "find-iam-entities.md")
- [Find stack IDs in AMS](find-stack.md "find-stack.md")
- [Find instance IDs or IP addresses in AMS](find-instance-id.md "find-instance-id.md")
- [Find Amazon Resource Names (ARNs) in AMS](find-arn.md "find-arn.md")
- [Find resources by ARN in AMS](find-resource-by-arn.md "find-resource-by-arn.md")
- [Find AMS account settings](find-your-settings.md "find-your-settings.md")

## What Is service knowledge management?

Service knowledge management is the store of all information on your AMS account. Information about the following is obtained from the AMS service
knowledge management system (SKMS), through the AMS SKMS API or through the AMS Console:

- VPCs
- Managed subnets
- Stacks and stack components, including Amazon EC2 instances and other resources
- Amazon Machine Images (AMIs)

You can use information from the SKMS to understand the infrastructure under
management and as input to change management and service requests to create, change, or remove infrastructure.

###### Note

All AMS SKMS API calls are recorded in AWS CloudTrail.

Access the SKMS through the AMS SKMS API, which provides operations for discovering information about an environment (VPCs and subnets) and the
application resources (stacks, Amazon EC2 instances, and instance images or AMIs) that can be deployed there.

VPCs and instance images are set up in an account, with the necessary access permissions, during onboarding. After they have been established, you can use the change
management system to populate the VPCs with working stacks.
