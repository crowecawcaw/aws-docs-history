# EMR notebooks security and

access control

Several features are available to help you tailor the security posture of EMR Notebooks.
This helps ensure that only authorized users have access to an EMR notebook, can
work with notebooks, and use the notebook editor to execute code on the cluster. These
features work along with the security features available for Amazon EMR and Amazon EMR clusters.
For more information, see [Security in Amazon EMR](emr-security.md "emr-security.md").

- You can use AWS Identity and Access Management policy statements together with notebook tags to limit
  access. For more information, see [How Amazon EMR works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md") and [Example identity-based
  policy statements for EMR Notebooks](emr-fine-grained-cluster-access.md#emr-managed-notebooks-tags-examples "emr-fine-grained-cluster-access.md#emr-managed-notebooks-tags-examples").
- Amazon EC2 security groups act as virtual firewalls that control network traffic
  between the cluster's primary instance and the notebook editor. You can use
  defaults or customize these security groups. For more information, see [Specifying EC2 security groups
  for EMR Notebooks](emr-managed-notebooks-security-groups.md "emr-managed-notebooks-security-groups.md").
- You specify an AWS Service Role that determines what permissions an
  EMR notebook has when interacting with other AWS services. For more
  information, see [Service role for
  EMR Notebooks](emr-managed-notebooks-service-role.md "emr-managed-notebooks-service-role.md").

###### Note

EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](emr-managed-notebooks-migration.md "emr-managed-notebooks-migration.md") and [Amazon EMR console](whats-new-in-console.md "whats-new-in-console.md").
