# Use AMS SSP to provision AWS Elastic Disaster Recovery in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elastic Disaster Recovery capabilities directly in your AMS managed account. AWS Elastic Disaster Recovery minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery. You can increase IT resilience when you use AWS Elastic Disaster Recovery to replicate on-premises or cloud-based applications running on supported operating systems. Use the AWS Management Console to configure replication and launch settings, monitor data replication, and launch instances for drills or recovery.

To learn more, see [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/").

## AWS Elastic Disaster Recovery in AWS Managed Services FAQ

**Q: How do I request access to AWS Elastic Disaster Recovery in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_drs_console_role`.

After its provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS Elastic Disaster Recovery in my AMS account?**

There are no restrictions to use AWS Elastic Disaster Recovery in your AMS account.

**Q: What are the prerequisites or dependencies to using AWS Elastic Disaster Recovery in my AMS account?**

- After you have access to the console role, you must initialize the Elastic Disaster Recovery service to create the needed IAM roles within the account.
  - You must submit change type Management | Applications | IAM instance profile | Create (managed automation) change type ct-0ixp4ch2tiu04 RFC to create a clone of the `customer-mc-ec2-instance-profile` instance profile and attach the `AWSElasticDisasterRecoveryEc2InstancePolicy` policy. You must specify which machines to attach the new policy to.
  - If the instance isn't using the default instance profile, then AMS can attach `AWSElasticDisasterRecoveryEc2InstancePolicy` through automation.

- You must use a customer-owned KMS key for cross-account recovery. The source account's KMS key must be updated following the policy to allow target account access. For more information, see [Share the EBS encryption key with the target account](../../../drs/latest/userguide/multi-account.md#multi-account-ebs "../../../drs/latest/userguide/multi-account.md#multi-account-ebs").
- The KMS key policy must be updated to allow the allow `customer_drs_console_role` to view the policy if you don't want to switch roles to view.
- For cross-account, cross-Region disaster recovery, AMS must set up the source and target account as Trusted Accounts and deploy the [Failback and in-AWS right-sizing roles](../../../drs/latest/userguide/trusted-accounts-failback-role.md "../../../drs/latest/userguide/trusted-accounts-failback-role.md") through CloudFormation.
