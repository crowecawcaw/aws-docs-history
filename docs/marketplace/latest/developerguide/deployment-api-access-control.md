The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Access control for the AWS Marketplace Deployment API

To manage deployments in AWS Marketplace, you must ensure that you have the necessary AWS Identity and Access Management
(IAM) roles and permissions.

Before calling the `PutDeploymentParameter` action, buyers must create the
**AWSServiceRoleForMarketplaceDeployment**
service-linked role. This provides AWS Marketplace with the permissions required to create,
manage, and tag the necessary deployment parameter related resources in the buyer’s
account. Buyers create this role using prompts as they progress through the
configuration process for any Quick Launch experience. For more information, see [Using
roles to configure and launch products](../buyerguide/using-service-linked-roles-secrets.md "../buyerguide/using-service-linked-roles-secrets.md") in _AWS Marketplace
Buyer Guide_.

To call `PutDeploymentParameter`, sellers must have IAM permissions for the
following actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "aws-marketplace:PutDeploymentParameter",
 "aws-marketplace:TagResource"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

The `aws-marketplace:PutDeploymentParameter` action permits the user to
call the `PutDeploymentParameter` API. The API also accepts an optional
`tags` attribute. If the `tags` attribute is included in the
request, the caller must also have permissions for
`aws-marketplace:TagResource` on the relevant resource. For more
information about creating users, see [Creating a user in your AWS
account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the _IAM User Guide._ For more
information about creating and assigning policies, see [Changing permissions for
an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md").
