# Registering an encrypted Amazon S3 location across AWS

accounts

AWS Lake Formation integrates with [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") (AWS KMS) to enable you to more easily set up other integrated services
to encrypt and decrypt data in Amazon Simple Storage Service (Amazon S3) locations.

Both customer managed keys and AWS managed keys are supported.
Client-side encryption/decryption is not supported.

###### Important

Avoid registering an Amazon S3 bucket that has **Requester pays** enabled.
For buckets registered with Lake Formation, the role used to register the bucket is always viewed
as the requester. If the bucket is accessed by another AWS account, the bucket owner
is charged for data access if the role belongs to the same account as the bucket
owner.

This section explains how to register an Amazon S3 location under the following
circumstances:

- The data in the Amazon S3 location is encrypted with a KMS key created in AWS KMS.
- The Amazon S3 location is not in the same AWS account as the AWS Glue Data Catalog.
- The KMS key either is or is not in the same AWS account as the Data Catalog.
  Registering an AWS KMS–encrypted Amazon S3 bucket in AWS account B using an AWS Identity and Access Management
  (IAM) role in AWS account A requires the following permissions:

- The role in account A must grant permissions on the bucket in account B.
- The bucket policy in account B must grant access permissions to the role in
  Account A.
- If the KMS key is in account B, the key policy must grant access to the role in
  account A, and the role in account A must grant permissions on the KMS key.
  In the following procedure, you create a role in the AWS account that contains the Data Catalog
  (account A in the previous discussion). Then, you use this role to register the location.
  Lake Formation assumes this role when accessing underlying data in Amazon S3. The assumed role has the
  required permissions on the KMS key. As a result, you don't have to grant permissions on the KMS key
  to principals accessing underlying data with ETL jobs or with integrated services such as
  Amazon Athena.

###### Important

You can't use the Lake Formation service-linked role to register a location in another account.
You must use a user-defined role instead. The role must meet the requirements in [Requirements for roles used to register
locations](registration-role.md "registration-role.md"). For more information about the service-linked role,
see [Service-linked role permissions for
Lake Formation](service-linked-roles.md#service-linked-role-permissions "service-linked-roles.md#service-linked-role-permissions").

###### Before You Begin

Review the [requirements for the role used to
register the location](registration-role.md "registration-role.md").

###### To register an encrypted Amazon S3 location across AWS accounts

1. In the same AWS account as the Data Catalog, sign into the AWS Management Console and open the
   IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a new role or view an existing role that meets the requirements in [Requirements for roles used to register
   locations](registration-role.md "registration-role.md"). Ensure that the role includes a policy that
   grants Amazon S3 permissions on the location.
3. If the KMS key is not in the same account as the Data Catalog, add to the role an inline policy
   that grants the required permissions on the KMS key. The following is an example policy.
   Replace Region and
   account ID with the region and account
   number of the KMS key. Replace `<key-id>` with the key
   ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`<key-id>`"
 }
 ]
}`

```

4. On the Amazon S3 console, add a bucket policy granting the required Amazon S3 permissions to
   the role. The following is an example bucket policy. Replace the account ID with the AWS
   account number of the Data Catalog, `<role-name>` with the name of
   your role, and `<bucket-name>` with the name of the
   bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Principal": {
 "AWS":"arn:aws:iam::`111122223333`:role/`<role-name>`"
 },
 "Action":"s3:ListBucket",
 "Resource":"arn:aws:s3:::`<bucket-name>`"
 },
 {
 "Effect":"Allow",
 "Principal": {
 "AWS":"arn:aws:iam::`111122223333`:role/`<role-name>`"
 },
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource":"arn:aws:s3:::`<bucket-name>`/*"
 }
 ]
}`

```

5. In AWS KMS, add the role as a user of the KMS key.
   1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"). Then, sign in as an administrator user or
      as a user who can modify the key policy of the KMS key used to encrypt the
      location.
   2. In the navigation pane, choose **Customer managed keys**, and then
      choose the name of the KMS key.
   3. On the KMS key details page, under the **Key policy** tab, if the JSON
      view of the key policy is not showing, choose **Switch to policy
      view**.
   4. In the **Key policy** section, choose **Edit**,
      and add the Amazon Resource Name (ARN) of the role to the `Allow use of
the key` object, as shown in the following example.

   ###### Note

   If that object is missing, add it with the permissions shown in the
   example.

   ```
           ...
           {
               "Sid": "Allow use of the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       **"arn:aws:iam::`<catalog-account-id>`:role/`<role-name>`"**
                   ]
               },
               "Action": [
                   "kms:Encrypt",
                   "kms:Decrypt",
                   "kms:ReEncrypt*",
                   "kms:GenerateDataKey*",
                   "kms:DescribeKey"
               ],
               "Resource": "*"
           },
           ...

   ```

   For more information, see [Allowing Users in Other Accounts to Use a KMS key](https://docs.amazonaws.cn/en_us/kms/latest/developerguide/key-policy-modifying-external-accounts.html "https://docs.amazonaws.cn/en_us/kms/latest/developerguide/key-policy-modifying-external-accounts.html") in the
   _AWS Key Management Service Developer Guide_.

6. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign into the Data Catalog AWS
   account as the data lake administrator.
7. In the navigation pane, under **Administration**, choose
   **Data lake locations**.
8. Choose **Register location**.
9. On the **Register location page**, for **Amazon S3
   path**, enter the location path as
   `s3://`<bucket>`/`<prefix>``.
Replace `<bucket>`with the name of the bucket and`<prefix>` with the rest of the path for the
   location.

###### Note

You must type the path because cross-account buckets do not appear in the list
when you choose **Browse**. 10. For **IAM role**, choose the role from Step 2. 11. Choose **Register location**.
