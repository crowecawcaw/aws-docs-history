# Permissions to replicate bots and manage bot replicas in Lex V2

If an IAM role has the [AmazonLexFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess") policy attached, it can create and manage bot replicas.

If you prefer to create a role with minimal permissions for Global Resiliency, use the following policy, which contains the following statements.

- Permissions to access the Amazon Lex V2 [service-linked role for bot replication](using-service-linked-roles.md#slr-replication "using-service-linked-roles.md#slr-replication").
- Permissions to allow Amazon Lex V2 to create a [service-linked role for bot replication on your behalf](using-service-linked-roles.md#slr-replication "using-service-linked-roles.md#slr-replication").
- Permissions to call the bot replication APIs.
  You can restrict permissions further by modifying them as follows.

- Replace `*` with specific bot or bot alias IDs to limit the permissions to specific bots or bot aliases.
- Use a subset of the `lex BotReplica` actions to restrict the role to specific actions.
  For an example, see [Allow users to create and view bot replicas, but not to delete them](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-gr-permissions "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-gr-permissions").
