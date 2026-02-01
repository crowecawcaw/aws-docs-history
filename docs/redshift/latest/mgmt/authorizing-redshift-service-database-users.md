Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Restricting access to IAM

roles

By default, IAM roles that are available to an Amazon Redshift cluster are available to all
users on that cluster. You can choose to restrict IAM roles to specific Amazon Redshift database
users on specific clusters or to specific regions.

To permit only specific database users to use an IAM role, take the following
steps.

###### To identify specific database users

with access to an IAM role

1. Identify the Amazon Resource Name (ARN) for the database users in your Amazon Redshift
   cluster. The ARN for a database user is in the format:
   `arn:aws:redshift:`region`:`account-id`:dbuser:`cluster-name`/`user-name``.

For Amazon Redshift Serverless use the following ARN format.
`arn:aws:redshift:`region`:`account-id`:dbuser:serverless-`account-id`-`workgroup-id`/`user-name`` 2. Open the [IAM
console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home"). 3. In the navigation pane, choose **Roles**. 4. Choose the IAM role that you want to restrict to specific Amazon Redshift database
users. 5. Choose the **Trust Relationships** tab, and then choose
**Edit Trust Relationship**. A new IAM role that allows
Amazon Redshift to access other AWS services on your behalf has a trust relationship as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Add a condition to the `sts:AssumeRole` action section of the trust
   relationship that limits the `sts:ExternalId` field to values that
   you specify. Include an ARN for each database user that you want to grant access
   to the role. The external ID can be any unique string.

For example, the following trust relationship specifies that only database
users `user1` and `user2` on cluster
`my-cluster` in region `us-west-2` have permission to
use this IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "sts:ExternalId": [
 "arn:aws:redshift:us-west-2:123456789012:dbuser:my-cluster/user1",
 "arn:aws:redshift:us-west-2:123456789012:dbuser:my-cluster/user2"
 ]
 }
 }
 }]
}`

```

7. Choose **Update Trust Policy**.
