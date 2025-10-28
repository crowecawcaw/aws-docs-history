# Registering an Amazon S3 location in another AWS

account

AWS Lake Formation enables you to register Amazon Simple Storage Service (Amazon S3) locations across AWS accounts. For
example, if the AWS Glue Data Catalog is in account A, a user in account A can register an Amazon S3 bucket in
account B.

Registering an Amazon S3 bucket in AWS account B using an AWS Identity and Access Management (IAM) role in AWS
account A requires the following permissions:

- The role in account A must grant permissions on the bucket in account B.
- The bucket policy in account B must grant access permissions to the role in Account
  A.

###### Important

Avoid registering an Amazon S3 bucket that has **Requester pays** enabled. For
buckets registered with Lake Formation, the role used to register the bucket is always viewed as the
requester. If the bucket is accessed by another AWS account, the bucket owner is charged for
data access if the role belongs to the same account as the bucket owner.

You can't use the Lake Formation service-linked role to register a location in another account. You
must use a user-defined role instead. The role must meet the requirements in [Requirements for roles used to register
locations](registration-role.md "registration-role.md"). For more information about the service-linked role, see [Service-linked role permissions for
Lake Formation](service-linked-roles.md#service-linked-role-permissions "service-linked-roles.md#service-linked-role-permissions").

###### Before you begin

Review the [requirements for the role used to register
the location](registration-role.md "registration-role.md").

###### To register a location in another AWS account

###### Note

If the location is encrypted, follow the instructions in [Registering an encrypted Amazon S3 location across AWS
accounts](register-cross-encrypted.md "register-cross-encrypted.md") instead.

The following procedure assumes that a principal in account 1111-2222-3333, which
contains the Data Catalog, wants to register the Amazon S3 bucket `awsexamplebucket1`, which
is in account 1234-5678-9012.

1. In account 1111-2222-3333, sign in to the AWS Management Console and open the IAM console
   at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a new role or view an existing role that meets the requirements in [Requirements for roles used to register
   locations](registration-role.md "registration-role.md"). Ensure that the role grants Amazon S3 permissions on
   `awsexamplebucket1`.
3. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). Sign in with
   account 1234-5678-9012.
4. In the **Bucket name** list, choose the bucket name,
   `awsexamplebucket1`.
5. Choose **Permissions**.
6. On the **Permissions** page, choose **Bucket
   Policy**.
7. In the **Bucket policy editor**, paste the following policy. Replace
   `<role-name>` with the name of your role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Principal": {
 "AWS":"arn:aws:iam::111122223333:role/`<role-name>`"
 },
 "Action":"s3:ListBucket",
 "Resource":"arn:aws:s3:::awsexamplebucket1"
 },
 {
 "Effect":"Allow",
 "Principal": {
 "AWS":"arn:aws:iam::111122223333:role/`<role-name>`"
 },
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource":"arn:aws:s3:::awsexamplebucket1/*"
 }
 ]
}`

```

8. Choose **Save**.
9. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in to account 1111-2222-3333 as the data
   lake administrator or as a user with sufficient permissions to register locations.
10. In the navigation pane, under **Administration**, choose **Data lake locations**.
11. On **Data lake locations** page, choose **Register location**.
12. On the **Register location page**, for **Amazon S3
    path**, enter the bucket name `s3://awsexamplebucket1`.

###### Note

You must type the bucket name because cross-account buckets do not appear in the list
when you choose **Browse**. 13. For **IAM role**, choose your role. 14. Choose **Register location**.
