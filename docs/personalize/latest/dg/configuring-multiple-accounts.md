# Configuring permissions when resources are in different

accounts

If your OpenSearch Service and Amazon Personalize resources are in separate accounts, you create an IAM role in each account and grant the role
access to the resources in the account.

###### To set up permissions for multiple accounts

1. In the account where your Amazon Personalize campaign exists, create an IAM role that has permission to get a personalized
   ranking from your Amazon Personalize campaign. When you configure the plugin, you specify the ARN for this role in the
   `external_account_iam_role_arn` parameter of the `personalized_search_ranking` response
   processor. For more information, see [Creating a pipeline in Amazon OpenSearch Service](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md").

For a policy example, see [Permissions policy example](service-role-managed.md#opensearch-granting-access-managed-permissions-policy "service-role-managed.md#opensearch-granting-access-managed-permissions-policy"). 2. In the account where your OpenSearch Service domain exists, create a role with a trust policy that grants OpenSearch Service
`AssumeRole` permissions. When you configure the plugin, you specify the ARN for this role in the
`iam_role_arn` parameter of the `personalized_search_ranking` response
processor. For more information, see [Creating a pipeline in Amazon OpenSearch Service](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md").

For a trust policy example, see [Trust policy example](service-role-managed.md#opensearch-granting-access-managed-trust-policy "service-role-managed.md#opensearch-granting-access-managed-trust-policy"). 3. Modify each role to grant the other role `AssumeRole` permissions. For example, for the role that has access to your Amazon Personalize resources,
its IAM policy would grant the role in the account with the OpenSearch Service domain assume role permissions as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "",
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/roleName"

 }]
}`

```

4. In the account where your OpenSearch Service domain exists, grant the user or role that's accessing your OpenSearch Service domain `PassRole` permissions for the
   OpenSearch Service service role you just created. For more information, see [Configuring Amazon OpenSearch Service domain security](domain-user-managed.md "domain-user-managed.md").
