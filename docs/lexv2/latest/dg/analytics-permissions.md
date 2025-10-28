# Managing access permissions for analytics

To provide a user access to analytics, attach a policy to an IAM role that permits the role to call the API operations for analytics. You can attach the [AWS
managed policy: AmazonLexFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess") to the
IAM role to provide full access to Amazon Lex API operations, or you can create a custom policy allowing only permissions to analytics and attach it to an IAM role.

###### To create a custom policy containing permissions for analytics

1. If you need to first create an IAM role, follow the steps at [Creating a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").
2. Follow the steps at [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") to create a policy using the following JSON object. To enable analytics access to specific bots for the IAM role, add the ARN of each bot to the `Resource` field. Replace the `region`, `account-id`, and `BOTID` with the values corresponding to the bots. You can also replace the statement identifier, `AnalyticsActions`, with a name of your choice.
3. Attach the policy you created to the role that you want to grant analytics permissions by following the steps at [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").
4. The role should now have permissions to view analytics for the bots you specified.
