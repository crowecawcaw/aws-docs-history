# Use AMS SSP to provision VM Import/Export in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access VM Import/Exportcapabilities directly in your AMS managed account. VM Import/Export enables you to easily import virtual machine images from your existing environment to Amazon EC2 instances and export them back to your on-premises environment.
This offering allows you to leverage your existing investments in the virtual machines that you have built to meet your IT security, configuration management,
and compliance requirements
by bringing those virtual machines into Amazon EC2 as ready-to-use instances. You can also export imported instances back to your on-premises virtualization infrastructure,
allowing you to deploy workloads across your IT infrastructure.

To learn more, see [VM Import/Export](https://aws.amazon.com/ec2/vm-import/ "https://aws.amazon.com/ec2/vm-import/").

## VM Import/Export in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to VM Import/Export in my AMS account?**

Request access to VM Import/Export by submitting an RFC with the Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM policy to your account: `customer_vmimport_policy`. After it's provisioned in your
account, you must onboard the role in your federation solution.

An additional role, the **VM Import/Export Service** role, is required for the service to perform actions in your account.

**Q: What are the restrictions to using VM Import/Export in my AMS account?**

- Functionality to import custom machine images and data volumes is both available in AMS
  VM Import/Export. However, permissions to S3 have been
  scoped down to limit actions to buckets matching the name `customer-vmimport-*` in order to
  limit access to information within the account.
- Image and snapshot import is supported in AMS VM Import/Export. However, instance import and
  instance export functionality is not available due to security measures.
- Additionally, export functionality has been disabled to mitigate the risk of exporting
  restricted and sensitive data.

**Q: What are the prerequisites or dependencies to using VM Import/Export in my AMS account?**

- You must provide a supported disk image to import into the AWS environment. For information,
  see [VM Import/Export Requirements](../../../vm-import/latest/userguide/vmie_prereqs.md "../../../vm-import/latest/userguide/vmie_prereqs.md").
- VM Import/Export isn't accessible through the AWS console. You must access this service through the AWS CLI, AWS Tools for PowerShell, or the AWS
  SDKs. Or, you can request an instance profile by submitting change type ct-117rmp64d5mvb: Deployment | Advanced stack components | Identity and Access Management (IAM) | Create EC2 instance profile. This instance profile allows the tools to perform commands from an instance.
