# Configuring permissions when resources are in the same

account

If your OpenSearch Service and
Amazon Personalize resources are in the same account, you must create an IAM service role for OpenSearch Service. This role must have permission to get
a personalized ranking from your Amazon Personalize campaign. The following is required to grant your OpenSearch Service service role permission
to get a personalized ranking from your Amazon Personalize campaign:

- The role's trust policy must grant `AssumeRole` permissions for OpenSearch Service. For a trust policy example,
  see [Trust policy example](#opensearch-granting-access-managed-trust-policy "#opensearch-granting-access-managed-trust-policy").
- The role must have permission to get a personalized ranking from your Amazon Personalize campaign. For a policy example, see
  [Permissions policy example](#opensearch-granting-access-managed-permissions-policy "#opensearch-granting-access-managed-permissions-policy").
  For information about creating an IAM role, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the _IAM User Guide_. For information on attaching an IAM policy to role, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

After you create an IAM service role for OpenSearch Service, you must grant the user or role that's accessing your OpenSearch Service domain `PassRole` permissions for the
OpenSearch Service service role. For more information, see [Configuring Amazon OpenSearch Service domain security](domain-user-managed.md "domain-user-managed.md").

###### Topics

- [Trust policy example](#opensearch-granting-access-managed-trust-policy "#opensearch-granting-access-managed-trust-policy")
- [Permissions policy example](#opensearch-granting-access-managed-permissions-policy "#opensearch-granting-access-managed-permissions-policy")

## Trust policy example

The following trust policy example grants `AssumeRole` permissions for OpenSearch Service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "",
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Principal": {
 "Service": [
 "es.amazonaws.com"
 ]
 }
 }]
}`

```

## Permissions policy example

The following policy example grants the role the minimum permissions to get a personalized ranking from your
Amazon Personalize campaign. For `Campaign ARN`, specify the Amazon Resource Name (ARN) of your Amazon Personalize campaign.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "personalize:GetPersonalizedRanking"
 ],
 "Resource": "arn:aws:personalize:`us-east-1`:`111122223333`:campaign/`YourResourceId`"
 }
 ]
}`

```
