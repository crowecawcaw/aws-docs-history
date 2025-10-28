# Best Practice 7.2 – Manage privileged

access to your SAP workload

Adopt an approach of least privilege where possible. Only grant the minimum access
required to perform a particular role to a minimum set of users, while managing usability
and efficiency. There are administrative accounts (for example,
`<sid>adm`), which by default, have access to significantly impact the
reliability or data security of your SAP workload. Consider how you can limit this
risk.

**Suggestion 7.2.1 – Manage AWS credentials and
authentication**

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely.
Using IAM, you can create and manage AWS users and groups for different SAP and cloud
administration tasks. Use IAM permissions to allow and deny users access to AWS resources.
Standard guidance should be followed, in particular restricting and securing root access.

- AWS Documentation: [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
  For access that is not assigned to a user but is required for the operation of the SAP
  application, pay particular attention to ensuring least privilege.

- AWS Documentation: [Using an IAM role to grant permissions to applications running on Amazon EC2
  instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md")
  [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") helps identify security risks associated with resources that are
  shared with an external entity, validates policies against IAM policy grammar and best
  practice, and can generate an IAM policy from the analysis of AWS CloudTrail logs. Consider its
  use as a mechanism for continuously reducing permissions based on user and role access
  patterns.

**Suggestion 7.2.2 – Manage SAP Administrative credentials and
authentication**

Implement a process for approving and granting elevated permissions only when
required, for a limited time-period. Use auditing functionality that addresses who and why
the access was granted.

Restrict the use of username/password for privileged accounts. Disable direct access
where possible. Store credentials securely, for example, in a privileged access management
solution or password vault.

Evaluate how Systems Manager could be used to restrict direct operating system access for
specific tasks using runbooks, RunCommand, and AWS Secrets Manager.

- AWS Documentation: [Restricting access to root-level commands through SSM Agent](../../../systems-manager/latest/userguide/ssm-agent-restrict-root-level-commands.md "../../../systems-manager/latest/userguide/ssm-agent-restrict-root-level-commands.md")
- AWS Documentation: [Referencing AWS Secrets Manager secrets from Parameter Store](../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md "../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md")
