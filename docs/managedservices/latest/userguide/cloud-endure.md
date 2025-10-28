# Use AMS SSP to provision AWS CloudEndure in your AMS account

###### Note

Following the successful launch of AWS Application Migration Service, the CloudEndure Migration service is now end of life in all AWS Regions. We recommend customers use
AWS Application Migration Service for lift and shift migrations to GovCloud Regions and to the Commercial Regions. For information, see
[What Is AWS Application Migration Service?](../../../mgn/latest/ug/what-is-application-migration-service.md "../../../mgn/latest/ug/what-is-application-migration-service.md").

If you want to use the AWS Application Migration Service, reach out to your CA so they can guide you.

Use AMS Self-Service Provisioning (SSP) mode to access AWS CloudEndure capabilities directly in your AMS managed account. AWS CloudEndure migration simplifies, expedites, and automates large-scale migrations from physical, virtual,
and cloud-based infrastructure to AWS. CloudEndure Disaster Recovery (DR) protects against downtime and data
loss from any threat, including ransomware and server corruption.

## AWS CloudEndure in AWS Managed Services FAQ

**Q: How do I request access to CloudEndure in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM User to your account:
`customer_cloud_endure_user`. After it's provisioned in your account, the access key and
secret key for the user is shared in AWS Secrets Manager.

These policies are provisioned to the account as well: `customer_cloud_endure_policy`
and `customer_cloud_endure_deny_policy`.

Additionally, you must provide a Risk Acceptance as the CloudEndure DR solution for application integration
has infrastructure-mutating permissions. To do this, work with your cloud service delivery
manager (CSDM).

**Q: What are the restrictions to using CloudEndure in my AMS account?**

The cloud endure replication and conversion instances can be launched only in the subnet
you indicate.

**Q: What are the prerequisites or dependencies to using CloudEndure in my AMS
account?** Share the following via RFC bidirectional correspondence:

- VPC Subnet details for Replication and Conversion instances to be launched.
- The KMS Key Amazon Resource Name (ARN) if the EBS volumes are encrypted.
