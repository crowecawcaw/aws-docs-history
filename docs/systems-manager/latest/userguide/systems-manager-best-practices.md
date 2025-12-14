AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use cases and best practices

This topic lists common use cases and best practices for AWS Systems Manager tools. If available,
this topic also includes links to relevant blog posts and technical documentation.

###### Note

The title of each section here is an active link to the corresponding section in the
technical documentation.

###### [Automation](systems-manager-automation.md "systems-manager-automation.md")

- Create self-service Automation runbooks for infrastructure.
- Use Automation, a tool in AWS Systems Manager, to simplify creating Amazon Machine Images (AMIs)
  from the AWS Marketplace or custom AMIs, using public Systems Manager documents (SSM
  documents) or by authoring your own workflows.
- [Build and maintain AMIs](automation-tutorial-update-ami.md "automation-tutorial-update-ami.md")
  using the `AWS-UpdateLinuxAmi` and `AWS-UpdateWindowsAmi`
  Automation runbooks, or using custom Automation runbooks that you create.

###### [Compliance](systems-manager-compliance.md "systems-manager-compliance.md")

- As a security best practice, we recommend that you update the AWS Identity and Access Management (IAM)
  role used by your managed nodes to restrict the node's ability to use the [PutComplianceItems](../APIReference/API_PutComplianceItems.md "../APIReference/API_PutComplianceItems.md") API action. This API action registers a compliance
  type and other compliance details on a designated resource, such as an Amazon EC2
  instance or a managed node. For more information, see [Configuring permissions for Compliance](compliance-permissions.md "compliance-permissions.md").

###### [Inventory](systems-manager-inventory.md "systems-manager-inventory.md")

- Use Inventory, a tool in AWS Systems Manager, with AWS Config to audit your application
  configurations over time.

###### [Maintenance Windows](maintenance-windows.md "maintenance-windows.md")

- Define a schedule to perform potentially disruptive actions on your nodes such as
  operating system (OS) patching, driver updates, or software installations.
- For information about the differences between State Manager and Maintenance Windows, tools of
  AWS Systems Manager, see [Choosing between State Manager and
  Maintenance Windows](state-manager-vs-maintenance-windows.md "state-manager-vs-maintenance-windows.md").

###### [Parameter Store](systems-manager-parameter-store.md "systems-manager-parameter-store.md")

- Use Parameter Store, a tool in AWS Systems Manager, to centrally manage global configuration
  settings.
- [How
  AWS Systems Manager Parameter Store uses AWS KMS](../../../kms/latest/developerguide/services-parameter-store.md "../../../kms/latest/developerguide/services-parameter-store.md").
- [Reference AWS Secrets Manager secrets from
  Parameter Store parameters](integration-ps-secretsmanager.md "integration-ps-secretsmanager.md").

###### [Patch Manager](patch-manager.md "patch-manager.md")

- Use Patch Manager, a tool in AWS Systems Manager, to roll out patches at scale and increase fleet
  compliance visibility across your nodes.
- [Integrate Patch Manager with
  AWS Security Hub CSPM](patch-manager-security-hub-integration.md "patch-manager-security-hub-integration.md") to receive alerts when nodes in your fleet go out of compliance
  and monitor the patching status of your fleets from a security point of view. There
  is a charge to use Security Hub CSPM. For more information, see [Pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/").
- Use only one method at a time for scanning managed nodes for patch compliance to
  [avoid unintentionally
  overwriting compliance data](patch-manager-compliance-data-overwrites.md "patch-manager-compliance-data-overwrites.md").

###### [Run Command](run-command.md "run-command.md")

- [Manage Instances at Scale without SSH Access Using EC2 Run
  Command](https://aws.amazon.com/blogs/aws/manage-instances-at-scale-without-ssh-access-using-ec2-run-command/ "https://aws.amazon.com/blogs/aws/manage-instances-at-scale-without-ssh-access-using-ec2-run-command/").
- Audit all API calls made by or on behalf of Run Command, a tool in AWS Systems Manager, using
  AWS CloudTrail.
- When you send a command using Run Command, don't include sensitive information formatted
  as plaintext, such as passwords, configuration data, or other secrets. All Systems Manager API
  activity in your account is logged in an S3 bucket for AWS CloudTrail logs. This means that any
  user with access to S3 bucket can view the plaintext values of those secrets. For this
  reason, we recommend creating and using `SecureString` parameters to encrypt
  sensitive data you use in your Systems Manager operations.

For more information, see [Restricting access to Parameter Store parameters
using IAM policies](sysman-paramstore-access.md "sysman-paramstore-access.md").

###### Note

By default, the log files delivered by CloudTrail to your bucket are encrypted by
Amazon [server-side
encryption with Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md"). To provide a
security layer that is directly manageable, you can instead use [server-side encryption with AWS KMS–managed keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") for your
CloudTrail log files.

For more information, see [Encrypting CloudTrail log files with AWS KMS–managed keys (SSE-KMS)](../../../awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.md "../../../awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.md") in the
_AWS CloudTrail User Guide_.

- [Use the targets and rate control features
  in Run Command to perform a staged command operation](send-commands-multiple.md "send-commands-multiple.md").
- [Use fine-grained access permissions for
  Run Command (and all Systems Manager tools) by using AWS Identity and Access Management (IAM)
  policies](security_iam_id-based-policy-examples.md#customer-managed-policies "security_iam_id-based-policy-examples.md#customer-managed-policies").

###### [Session Manager](session-manager.md "session-manager.md")

- [Log session activity in your
  AWS account using AWS CloudTrail](session-manager-auditing.md "session-manager-auditing.md").
- [Log session data in your AWS account
  using Amazon CloudWatch Logs or Amazon S3](session-manager-logging.md "session-manager-logging.md").
- [Control user session access to instances](session-manager-getting-started-restrict-access.md "session-manager-getting-started-restrict-access.md").
- [Restrict access to commands in a session](session-manager-restrict-command-access.md "session-manager-restrict-command-access.md").
- [Turn off or turn on ssm-user account administrative permissions](session-manager-getting-started-ssm-user-permissions.md "session-manager-getting-started-ssm-user-permissions.md").

###### [State Manager](systems-manager-state.md "systems-manager-state.md")

- [Update SSM Agent at least once a
  month using the pre-configured AWS-UpdateSSMAgent
  document](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md").
- (Windows) Upload the PowerShell or DSC module to Amazon Simple Storage Service (Amazon S3), and use
  `AWS-InstallPowerShellModule`.
- Use tags to create application groups for your nodes. And then target nodes using
  the `Targets` parameter instead of specifying individual node IDs.
- [Automatically remediate findings generated by Amazon Inspector by using
  Systems Manager](https://aws.amazon.com/blogs/security/how-to-remediate-amazon-inspector-security-findings-automatically/ "https://aws.amazon.com/blogs/security/how-to-remediate-amazon-inspector-security-findings-automatically/").
- [Use a centralized configuration repository
  for your SSM documents, and share documents across your
  organization](documents-ssm-sharing.md "documents-ssm-sharing.md").
- For information about the differences between State Manager and Maintenance Windows, see [Choosing between State Manager and
  Maintenance Windows](state-manager-vs-maintenance-windows.md "state-manager-vs-maintenance-windows.md").

###### [Managed nodes](fleet-manager-managed-nodes.md "fleet-manager-managed-nodes.md")

- Systems Manager requires accurate time references to perform its operations. If your node's
  date and time aren't set correctly, they might not match the signature date of your
  API requests. This might lead to errors or incomplete functionality. For example,
  nodes with incorrect time settings won't be included in your lists of managed
  nodes.

For information about setting the time on your nodes, see [Set the time
for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md").

- On Linux managed nodes, [verify the
  signature of SSM Agent](verify-agent-signature.md "verify-agent-signature.md").

**More info**

- [Security best practices for
  Systems Manager](security-best-practices.md "security-best-practices.md")
