# Use AMS SSP to provision AWS Transfer Family in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Transfer Family (Transfer Family) capabilities directly in your AMS managed account. AWS Transfer Family is a fully managed AWS service that enables you to transfer files over
Secure File Transfer Protocol (SFTP), into and out of Amazon Simple Storage Service (Amazon S3) storage.
SFTP is also known as Secure Shell (SSH) File Transfer Protocol. SFTP is used in data exchange workflows
across different industries such as financial services, healthcare, advertising, and retail, among others.

With AWS SFTP, you get access to an SFTP server in AWS without the need to run any server infrastructure.
You can use this service to migrate your SFTP-based workflows to AWS while maintaining your end users' clients
and configurations as is. You first associate your hostname with the SFTP server endpoint, then add your users
and provision them with the right level of access. After you do, your users' transfer requests are serviced directly
out of your AWS SFTP server endpoint.
To learn more, see [AWS Transfer for SFTP](https://aws.amazon.com/aws-transfer-family "https://aws.amazon.com/aws-transfer-family"), also
[Create an SFTP-enabled server](../../../transfer/latest/userguide/create-server-sftp.md "../../../transfer/latest/userguide/create-server-sftp.md").

## AWS Transfer for SFTP in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to AWS Transfer for SFTP in my AMS account?**

Request access to AWS Transfer for SFTP by submitting an RFC with the Management | AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
Through this RFC the following IAM roles, and a policy, are provisioned in your account:

- `customer_transfer_author_role`. This role is designed for you to manage the SFTP service through the console.
- `customer_transfer_sftp_server_logging_role`. This role is designed to be attached
  on the SFTP Server. It allows the SFTP server to pull logs into CloudWatch.
- `customer_transfer_sftp_user_role`. This role is designed to be attached on the
  SFTP users. It allows the SFTP users to interact with the S3 bucket.
- `policy customer_transfer_scope_down_policy`. This policy is a scope-down
  policy that can be applied to the SFTP User to limit their access on the S3 bucket to their home folders.
- `customer_transfer_sftp_efs_user_role`. This role is designed to be attached on the SFTP users. It allows the
  SFTP users to interact with the EFS file system.

After it's provisioned in your account, you must onboard the roles in your federation solution.

**Q: What are the restrictions to using AWS Transfer for SFTP in my AMS account?**

AWS Transfer for SFTP configuration is limited to resources without "AMS-" or "MC-"
prefixes to prevent any modifications to AMS infrastructure.

**Q: What are the prerequisites or dependencies to using AWS Transfer for SFTP in my AMS account?**

- You must have an Amazon S3 bucket with a name that contains the keyword "transfer"
  before creating the AWS Transfer for SFTP server and users.
- To use a "Customer Identify Provider," you must deploy the API Gateway, Lambda function, and
  your user repository (AD, Secrets Manager, and so on). For more information, see
  [Enable password authentication for AWS Transfer for SFTP using AWS Secrets Manager](https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-for-sftp-using-aws-secrets-manager/ "https://aws.amazon.com/blogs/storage/enable-password-authentication-for-aws-transfer-for-sftp-using-aws-secrets-manager/") and
  [Working with Identity Providers](../../../transfer/latest/userguide/authenticating-users.md "../../../transfer/latest/userguide/authenticating-users.md").
