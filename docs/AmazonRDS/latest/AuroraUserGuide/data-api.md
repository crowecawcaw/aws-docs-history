# Authorizing access to the Amazon RDS Data API

Users can invoke Amazon RDS Data API (Data API) operations only if they are authorized to
do so. You can give a user permission to use Data API by attaching an AWS Identity and Access Management (IAM)
policy that defines their privileges. You can also attach the policy to a role if
you're using IAM roles. An AWS managed policy,
`AmazonRDSDataFullAccess`, includes permissions for Data API.

The `AmazonRDSDataFullAccess` policy also includes permissions for the
user to get the value of a secret from AWS Secrets Manager. Users need to use Secrets Manager to store
secrets that they can use in their calls to Data API. Using secrets means that users
don't need to include database credentials for the resources that they target in
their calls to Data API. Data API transparently calls Secrets Manager, which allows (or denies)
the user's request for the secret. For information about setting up secrets to use
with Data API, see [Storing database credentials in AWS Secrets Manager](#data-api.secrets "#data-api.secrets").

The `AmazonRDSDataFullAccess` policy provides complete access
(through Data API) to resources. You can narrow the scope by defining your own policies
that specify the Amazon Resource Name (ARN) of a resource.

For example, the following policy shows an example of the minimum required
permissions for a user to access Data API for the DB cluster identified by its ARN. The
policy includes the needed permissions to access Secrets Manager and get authorization to the
DB instance for the user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SecretsManagerDbCredentialsAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "`arn:aws:secretsmanager:*:*:secret:rds-db-credentials/*`"
 },
 {
 "Sid": "RDSDataServiceAccess",
 "Effect": "Allow",
 "Action": [
 "rds-data:BatchExecuteStatement",
 "rds-data:BeginTransaction",
 "rds-data:CommitTransaction",
 "rds-data:ExecuteStatement",
 "rds-data:RollbackTransaction"
 ],
 "Resource": "`arn:aws:rds:us-east-2:111122223333:cluster:prod`"
 }
 ]
}`

```

We recommend that you use a specific ARN for the "Resources" element in
your policy statements (as shown in the example) rather than a wildcard (\*).

## Working with tag-based

authorization

RDS Data API (Data API) and Secrets Manager both support tag-based authorization.
_Tags_ are key-value pairs that label a
resource, such as an RDS cluster, with an additional string value, for
example:

- `environment:production`
- `environment:development`

You can apply tags to your resources for cost allocation, operations support, access control, and many other reasons.
(If you don't already have tags on your resources and you want to apply them, you can learn more at [Tagging Amazon RDS
resources](USER_Tagging.md "USER_Tagging.md").) You can use the tags in your policy statements to limit access to the RDS clusters
that are labeled with these tags. As an example,
an Aurora DB cluster might have tags that identify its environment as
either production or development.

The following example shows how you can use tags in your policy statements. This
statement requires that both the cluster and the secret passed in the Data API
request have an `environment:production` tag.

Here's how the policy is applied: When a user makes a call using Data API,
the request is sent to the service. Data API first verifies that the cluster ARN
passed in the request is tagged with `environment:production`. It then
calls Secrets Manager to retrieve the value of the user's secret in the request.
Secrets Manager also verifies that the user's secret is tagged with
`environment:production`. If so, Data API then uses the retrieved
value for the user's DB password. Finally, if that's also correct, the
Data API request is invoked successfully for the user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SecretsManagerDbCredentialsAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "`arn:aws:secretsmanager:*:*:secret:rds-db-credentials/*`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": [
 "production"
 ]
 }
 }
 },
 {
 "Sid": "RDSDataServiceAccess",
 "Effect": "Allow",
 "Action": [
 "rds-data:*"
 ],
 "Resource": "`arn:aws:rds:us-east-2:111122223333:cluster:*`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": [
 "production"
 ]
 }
 }
 }
 ]
}`

```

The example shows separate actions for `rds-data` and
`secretsmanager` for Data API and Secrets Manager. However, you can
combine actions and define tag conditions in many different ways to support your
specific use cases. For more information, see
[Using identity-based policies (IAM policies) for Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access_identity-based-policies.md#permissions_grant-limited-condition "../../../secretsmanager/latest/userguide/auth-and-access_identity-based-policies.md#permissions_grant-limited-condition").

In the "Condition" element of the policy, you can choose tag keys from
among the following:

- `aws:TagKeys`
- `aws:ResourceTag/${TagKey}`

To learn more about resource tags and how to use `aws:TagKeys`, see [Controlling
access to AWS resources using resource tags](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys").

###### Note

Both Data API and AWS Secrets Manager authorize users. If you don't have permissions for all
actions defined in a policy, you get an `AccessDeniedException`
error.

## Storing database credentials in AWS Secrets Manager

When you call the Amazon RDS Data API (Data API), you pass credentials for the Aurora DB
cluster by using a secret in Secrets Manager. To pass credentials in this way, you specify the
name of the secret or the Amazon Resource Name (ARN) of the secret.

###### To store DB cluster credentials in a secret

1. Use Secrets Manager to create a secret that contains credentials for the Aurora DB cluster.

For instructions, see
[Create a database secret](../../../secretsmanager/latest/userguide/create_database_secret.md "../../../secretsmanager/latest/userguide/create_database_secret.md")
in the _AWS Secrets Manager User Guide_. 2. Use the Secrets Manager console to view the details for the secret you created, or run the `aws secretsmanager describe-secret` AWS CLI command.

Note the name and ARN of the secret. You can use them in calls to Data
API.

For more information about using Secrets Manager,
see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

To understand how Amazon Aurora manages identity and access management, see [How
Amazon Aurora works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

For more information about creating an IAM policy, see [Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in
the _IAM User Guide_. For information about adding an IAM policy
to a user, see
[Adding and Removing IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
in the _IAM User Guide_.
