# Use AMS SSP to provision AWS CloudHSM in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS CloudHSM capabilities directly in your AMS managed account. AWS CloudHSM helps you meet corporate, contractual, and regulatory compliance requirements for data security by
using dedicated Hardware Security Module (HSM)
instances within the AWS cloud. AWS, and AWS Marketplace partners, offer a variety of solutions for protecting sensitive
data within the AWS platform, but for some
applications and data subject to contractual or regulatory mandates for managing cryptographic keys, additional
protection may be necessary. AWS CloudHSM complements
existing data protection solutions and allows you to protect your encryption keys within HSMs that are designed and
validated to government standards for secure key management.
AWS CloudHSM allows you to securely generate, store, and manage cryptographic keys used for data encryption in a way that keys
are accessible only by you.
To learn more, see [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/").

## AWS CloudHSM in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS CloudHSM in my AMS account?**

Utilization of in your AMS account is a two-step process:

1. Request an AWS CloudHSM cluster. Do this by submitting an RFC with the Management | Other | Other |
   Create (ct-1e1xtak34nx76) change type. Include the following details:
   - AWS Region.
   - VPC ID/ARN. Provide a VPC ID/VPC ARN that is in the same account as the RFC that you submit.
   - Specify at least two Availability Zones for the cluster.
   - Amazon EC2 instance ID that will connect to the HSM cluster.

2. Access the AWS CloudHSM console. Do this by submitting an RFC with the Management | AWS service | Self-provisioned service | Add (ct-1w8z66n899dct)
   change type.
   This RFC provisions the following IAM role to your account: `customer_cloudhsm_console_role`.

After the role is provisioned in your account, you must onboard it in your
federation solution.

**Q: What are the restrictions to using AWS CloudHSM in my AMS account?**

Access to the AWS CloudHSM console doesn't provide you with the ability to create, terminate or restore your cluster. To do those things, submit a
Management | Other | Other | Create change type (ct-1e1xtak34nx76) change type.

**Q: What are the prerequisites or dependencies to using AWS CloudHSM in my AMS account?**

You must allow TCP traffic using port 2225 through a client Amazon EC2 instance within a VPC, or use Direct Connect VPN for on-premise servers
that want access to the HSM cluster. AWS CloudHSM is dependent on Amazon EC2 for security groups and network interfaces.
For log monitoring or auditing, HSM relies on CloudTrail (AWS API operations) and CloudWatch Logs for all local HSM device activity.

**Q: Who will apply updates to the AWS CloudHSM client and related software libraries?**

You are responsible for applying the library and client updates. You'll want to
monitor the
[CloudHSM version history](../../../cloudhsm/latest/userguide/client-history.md "../../../cloudhsm/latest/userguide/client-history.md") page for releases, and then apply updates using the
[CloudHSM client upgrade](../../../cloudhsm/latest/userguide/client-upgrade.md "../../../cloudhsm/latest/userguide/client-upgrade.md").

###### Note

Software patches for the HSM appliance are always automatically applied by the AWS CloudHSM service.
