# View AWS account identifiers

AWS assigns the following unique identifiers to each AWS account:

**[AWS account ID](#FindAccountId "#FindAccountId")**

A 12-digit number, such as 012345678901, that uniquely identifies an
AWS account. Many AWS resources include the account ID in their [Amazon Resource Names
(ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). The account ID portion distinguishes resources in one
account from the resources in another account. If you're an AWS Identity and Access Management (IAM)
user, you can sign in to the AWS Management Console using either the account ID or account
alias. While account IDs, like any identifying information, should be used and
shared carefully, they are not considered secret, sensitive, or confidential
information.

**[Canonical user ID](#FindCanonicalId "#FindCanonicalId")**

An alpha-numeric identifier, such as
`79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`,
that is an obfuscated form of the AWS account ID. You can use this ID to
identify an AWS account when granting cross-account access to buckets and
objects using Amazon Simple Storage Service (Amazon S3). You can retrieve the canonical user ID for your
AWS account as either the [root user](root-user.md "root-user.md") or an IAM
user.

You must be authenticated with AWS to view these identifiers.

###### Warning

Do not provide your AWS credentials (including passwords and access keys) to a third
party that needs your AWS account identifiers to share AWS resources with you. Doing
so would give them the same access to the AWS account that you have.

## Find your AWS account ID

You can find the AWS account ID using either the AWS Management Console or the AWS Command Line Interface (AWS CLI).
In the console, the location of the account ID depends on whether you're signed in as
the root user or an IAM user. The account ID is the same whether you're signed in as the
root user or an IAM user.

### Finding your account ID as the root user

AWS Management Console

###### To find your AWS account ID when signed in as the

root user

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- When you sign in as the root user, you don't need any
  IAM permissions.

1. In the navigation bar on the upper right, choose your account
   name or number and then choose **Security
   credentials**.

###### Tip

If you don't see the **Security
credentials** option, you might be signed in as
a federated user with an IAM role, instead of as an IAM
user. In this case, look for the entry
**Account** and the account ID number
next to it. 2. Under the **Account details** section, the
account number appears next to **AWS account
ID**.

AWS CLI & SDKs
**To find your AWS account ID using the
AWS CLI**

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- When you run the command as the root user, you don't need any
  IAM permissions.

Use the [get-caller-identity](../../../cli/latest/reference/sts/get-caller-identity.md "../../../cli/latest/reference/sts/get-caller-identity.md") command as follows.

```
`$` `aws sts get-caller-identity \
 --query Account \
 --output text``123456789012`
```

### Find your account ID as an IAM

user

AWS Management Console

###### To find your AWS account ID when signed in as an IAM

user

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- `account:GetAccountInformation`

1. In the navigation bar on the upper right, choose your user
   name and then choose **Security
   credentials**.

###### Tip

If you don't see the **Security
credentials** option, you might be signed in as
a federated user with an IAM role, instead of as an IAM
user. In this case, look for the entry
**Account** and the account ID number
next to it. 2. At the top of the page, under **Account
details**, the account number appears next to
**AWS account ID**.

AWS CLI & SDKs
**To find your AWS account ID using the
AWS CLI**

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- When you run the command as an IAM user or role, then
  you must have:
  - `sts:GetCallerIdentity`

Use the [get-caller-identity](../../../cli/latest/reference/sts/get-caller-identity.md "../../../cli/latest/reference/sts/get-caller-identity.md") command as follows.

```
`$` `aws sts get-caller-identity \
 --query Account \
 --output text``123456789012`
```

## Find the canonical user ID for your

AWS account

You can find the canonical user ID for your AWS account using the AWS Management Console or the
AWS CLI. The canonical user ID for an AWS account is specific to that account. You can
retrieve the canonical user ID for your AWS account as the root user, a federated user,
or an IAM user.

### Find the canonical ID as the root user or IAM

user

AWS Management Console

###### To find the canonical user ID for your account when signed in to

the console as the root user or an IAM user

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- When you run the command as the root user, you don't need
  any IAM permissions.
- When you sign in as an IAM user, then you must
  have:
  - `account:GetAccountInformation`

1. Sign in to the AWS Management Console as the root user or an IAM
   user.
2. In the navigation bar on the upper right, choose your account
   name or number and then choose **Security
   credentials**.

###### Tip

If you don't see the **Security
credentials** option, you might be signed in as
a federated user with an IAM role, instead of as an IAM
user. In this case, look for the entry
**Account** and the account ID number
next to it. 3. Under the **Account details** section, the
canonical user ID appears next to **Canonical user
ID**. You can use your canonical user ID to
configure Amazon S3 access control lists (ACLs).

AWS CLI & SDKs

###### To find the canonical user ID using the AWS CLI

The same AWS CLI and API command works for the AWS account root user, IAM
users, or IAM roles.

Use the [list-buckets](../../../cli/latest/reference/s3api/list-buckets.md "../../../cli/latest/reference/s3api/list-buckets.md") command as follows.

```
`$` `aws s3api list-buckets \
 --max-items 10 \
 --page-size 10 \
 --query Owner.ID \
 --output text``249fa2f1dc32c330EXAMPLE91b2778fcc65f980f9172f9cb9a5f50ccbEXAMPLE`
```

### Find the canonical ID as a

federated user with an IAM role

AWS Management Console

###### To find the canonical ID for your account when signed in to the

console as a federated user with an IAM role

###### Minimum permissions

- You must have permission to list and view an Amazon S3
  bucket.

1. Sign in to the AWS Management Console as a federated user with an IAM
   role.
2. In the Amazon S3 console, choose a bucket name to view details
   about a bucket.
3. Choose the **Permissions** tab.
4. In the **Access control list** section, under
   **Bucket owner**, the canonical ID for your
   AWS account appears.

AWS CLI & SDKs

###### To find the canonical user ID using the AWS CLI

The same AWS CLI and API command works for the AWS account root user, IAM
users, or IAM roles.

Use the [list-buckets](../../../cli/latest/reference/s3api/list-buckets.md "../../../cli/latest/reference/s3api/list-buckets.md") command as follows.

```
`$` `aws s3api list-buckets \
 --max-items 10 \
 --page-size 10 \
 --query Owner.ID \
 --output text``249fa2f1dc32c330EXAMPLE91b2778fcc65f980f9172f9cb9a5f50ccbEXAMPLE`
```
