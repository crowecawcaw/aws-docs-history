# Creating and using an IAM policy for

IAM database access

To allow a user or role to connect to your DB cluster,
you must create an IAM policy. After that, you attach the policy to a permissions set or role.

###### Note

To learn more about IAM policies, see [Identity and access management for Amazon Aurora](UsingWithRDS.md "UsingWithRDS.md").

The following example policy allows a user to connect to a DB
cluster using IAM database authentication.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:`111122223333`:dbuser:db-ABCDEFGHIJKL01234/db_user"
 ]
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:`111122223333`:dbuser:cluster-ABCDEFGHIJKL01234/db_user"
 ]
 }
 ]
}`

```

###### Important

A user with administrator permissions can access DB clusters without explicit
permissions in an IAM policy. If you want to restrict administrator access to DB
clusters, you can create an IAM role with the appropriate, lesser
privileged permissions and assign it to the administrator.

###### Note

Don't confuse the `rds-db:` prefix with other RDS API operation prefixes that begin with
`rds:`. You use the `rds-db:` prefix and the
`rds-db:connect` action only for IAM database authentication. They
aren't valid in any other context.

The example policy includes a single statement with the following elements:

- `Effect` – Specify `Allow` to grant access
  to the DB cluster.
  If you don't explicitly allow access, then access is denied by default.
- `Action` – Specify `rds-db:connect` to allow
  connections to the DB cluster.
- `Resource` – Specify an Amazon Resource Name (ARN) that
  describes one database account in one DB cluster.
  The ARN format is as follows.

```

arn:aws:rds-db:`region`:`account-id`:dbuser:`DbClusterResourceId`/`db-user-name`

```

In this format, replace the following:

    + ``region`` is the AWS Region for the DB cluster. In
     the example policy, the AWS Region is `us-east-2`.
    + ``account-id`` is the AWS account number for the DB
     cluster. In the example policy, the account number is
     `1234567890`. The user must be in the same account as the
     account for the DB cluster.


    To perform cross-account access, create an IAM role with the policy shown above in the account for
     the DB cluster
     and allow your other account to assume the role.
    + ``DbClusterResourceId``
     is the identifier for the DB cluster.
     This identifier is unique to an AWS Region and never changes. In the
     example policy, the identifier is
     `cluster-ABCDEFGHIJKL01234`.


    To find a DB cluster resource ID in the AWS Management Console for Amazon Aurora, choose
     the DB cluster to see its details.
     Then choose the **Configuration** tab. The **Resource
     ID** is shown in the **Configuration** section.


    Alternatively, you can use the AWS CLI command to list the identifiers
     and resource IDs for all of your DB cluster
     in the current AWS Region, as shown following.



    ```

    aws rds describe-db-clusters --query "DBClusters[*].[DBClusterIdentifier,DbClusterResourceId]"

    ```

    ###### Note

    If you are connecting to a database through RDS Proxy, specify the proxy resource ID, such as
     `prx-ABCDEFGHIJKL01234`. For information about using IAM database authentication with RDS Proxy, see
     [Connecting to a database using IAM authentication](rds-proxy-connecting.md#rds-proxy-connecting-iam "rds-proxy-connecting.md#rds-proxy-connecting-iam").
    + ``db-user-name`` is the name of
     the database account to associate with IAM authentication. In the
     example policy, the database account is `db_user`.

You can construct other ARNs to support various access patterns. The following policy
allows access to two different database accounts in a DB cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:123456789012:dbuser:db-ABCDEFGHIJKL01234/jane_doe",
 "arn:aws:rds-db:us-east-2:123456789012:dbuser:db-ABCDEFGHIJKL01234/mary_roe"
 ]
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:123456789012:dbuser:cluster-ABCDEFGHIJKL01234/jane_doe",
 "arn:aws:rds-db:us-east-2:123456789012:dbuser:cluster-ABCDEFGHIJKL01234/mary_roe"
 ]
 }
 ]
}`

```

The following policy uses the "\*" character to match all DB
clusters
and database accounts for a particular AWS account and AWS Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:`111122223333`:dbuser:*/*"
 ]
 }
 ]
}`

```

The following policy matches all of the DB clusters
for a particular AWS account and AWS Region. However, the policy only grants access to
DB
clusters that have a `jane_doe` database
account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-db:connect"
 ],
 "Resource": [
 "arn:aws:rds-db:us-east-2:123456789012:dbuser:*/jane_doe"
 ]
 }
 ]
}`

```

The user or role has access to only those databases that the database user
does. For example, suppose that your DB cluster has a database named
_dev_, and another database named _test_. If
the database user `jane_doe` has access only to _dev_, any
users or roles that access that DB cluster with the `jane_doe` user also
have access only to _dev_. This access restriction is also true for
other database objects, such as tables, views, and so on.

An administrator must create IAM policies that grant entities permission to perform
specific API operations on the specified resources they need. The administrator must then attach
those policies to the permission sets or roles that require those permissions. For examples of policies, see
[Identity-based policy
examples for Amazon Aurora](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Attaching an IAM policy

to a permission set or role

After you create an IAM policy to allow database authentication, you need to
attach the policy to a permission set or role. For a tutorial on this topic, see [Create and attach your first customer managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the
_IAM User Guide_.

As you work through the tutorial, you can use one of the policy examples shown in
this section as a starting point and tailor it to your needs. At the end of the
tutorial, you have a permission set with an attached policy that can make use of the
`rds-db:connect` action.

###### Note

You can map multiple permission sets or roles to the same database user account. For
example, suppose that your IAM policy specified the following resource
ARN.

```

arn:aws:rds-db:us-east-2:123456789012:dbuser:cluster-12ABC34DEFG5HIJ6KLMNOP78QR/jane_doe

```

If you attach the policy to _Jane_,
_Bob_, and _Diego_, then each of those
users can connect to the specified DB cluster
using the `jane_doe` database account.
