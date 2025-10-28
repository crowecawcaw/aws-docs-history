# Registering an encrypted Amazon S3 location

Lake Formation integrates with [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
(AWS KMS) to enable you to more easily set up other integrated services to encrypt and decrypt
data in Amazon Simple Storage Service (Amazon S3) locations.

Both customer managed AWS KMS keys and AWS managed keys are supported. Currently,
client-side encryption/decryption is supported only with Athena.

You must specify an AWS Identity and Access Management (IAM) role when you register an Amazon S3 location. For
encrypted Amazon S3 locations, either the role must have permission to encrypt and decrypt data
with the AWS KMS key, or the KMS key policy must grant permissions on the key to the role.

###### Important

Avoid registering an Amazon S3 bucket that has **Requester pays** enabled.
For buckets registered with Lake Formation, the role used to register the bucket is always viewed as
the requester. If the bucket is accessed by another AWS account, the bucket owner is
charged for data access if the role belongs to the same account as the bucket owner.

Lake Formation uses a service-linked role to register your data locations. However, this role has several [limitations](service-linked-role-limitations.md "service-linked-role-limitations.md").
Due to these constraints, we recommend creating and using a custom IAM role instead for more flexibility
and control. The custom
role you create to register the location must meets the requirements specified in [Requirements for roles used to register
locations](registration-role.md "registration-role.md").

###### Important

If you used an AWS managed key to encrypt the Amazon S3 location, you
can't use the Lake Formation service-linked role. You must use a custom role and add IAM permissions
on the key to the role. Details are provided later in this section.

The following procedures explain how to register an Amazon S3 location that is encrypted with
either a customer managed key or an AWS managed key.

- [Registering a location encrypted with a
  customer managed key](#proc-register-cust-cmk "#proc-register-cust-cmk")
- [Registering a location encrypted with an AWS managed key](#proc-register-aws-cmk "#proc-register-aws-cmk")

###### Before You Begin

Review the [requirements for the role used to register
the location](registration-role.md "registration-role.md").

###### To register an Amazon S3 location encrypted with a customer managed key

###### Note

If the KMS key or Amazon S3 location are not in the same AWS account as the Data Catalog, follow
the instructions in [Registering an encrypted Amazon S3 location across AWS
accounts](register-cross-encrypted.md "register-cross-encrypted.md") instead.

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms") and log in as an AWS Identity and Access Management (IAM) administrative user or as
   a user who can modify the key policy of the KMS key used to encrypt the location.
2. In the navigation pane, choose **Customer managed keys**, and then
   choose the name of the desired KMS key.
3. On the KMS key details page, choose the **Key policy** tab, and then do
   one of the following to add your custom role or the Lake Formation service-linked role as a KMS key
   user:
   - **If the default view is showing** (with
     **Key administrators**, **Key deletion**,
     **Key users**, and **Other AWS accounts**
     sections) – Under the **Key users** section, add your custom
     role or the Lake Formation service-linked role
     `AWSServiceRoleForLakeFormationDataAccess`.
   - **If the key policy (JSON) is showing** – Edit
     the policy to add your custom role or the Lake Formation service-linked role
     `AWSServiceRoleForLakeFormationDataAccess` to the object "Allow use of
     the key," as shown in the following example.

   ###### Note

   If that object is missing, add it with the permissions shown in the example. The
   example uses the service-linked role.

   ```
           ...
           {
               "Sid": "Allow use of the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       **"arn:aws:iam::111122223333:role/aws-service-role/lakeformation.amazonaws.com/AWSServiceRoleForLakeFormationDataAccess",**
                       "arn:aws:iam::111122223333:user/keyuser"
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

4. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as the data lake
   administrator or as a user with the `lakeformation:RegisterResource` IAM
   permission.
5. In the navigation pane, under **Administration**, choose
   **Data lake locations**.
6. Choose **Register location**, and then choose
   **Browse** to select an Amazon Simple Storage Service (Amazon S3) path.
7. (Optional, but strongly recommended) Choose **Review location
   permissions** to view a list of all existing resources in the selected Amazon S3
   location and their permissions.

Registering the selected location might result in your Lake Formation users gaining access to
data already at that location. Viewing this list helps you ensure that existing data
remains secure. 8. For **IAM role**, choose either the
`AWSServiceRoleForLakeFormationDataAccess` service-linked role (the default)
or your custom role that meets the [Requirements for roles used to register
locations](registration-role.md "registration-role.md"). 9. Choose **Register location**.
For more information about the service-linked role, see [Service-linked role permissions for
Lake Formation](service-linked-roles.md#service-linked-role-permissions "service-linked-roles.md#service-linked-role-permissions").

###### To register an Amazon S3 location encrypted with an AWS managed key

###### Important

If the Amazon S3 location is not in the same AWS account as the Data Catalog, follow the
instructions in [Registering an encrypted Amazon S3 location across AWS
accounts](register-cross-encrypted.md "register-cross-encrypted.md") instead.

1. Create an IAM role to use to register the location. Ensure that it meets the
   requirements listed in [Requirements for roles used to register
   locations](registration-role.md "registration-role.md").
2. Add the following inline policy to the role. It grants permissions on the key to the
   role. The `Resource` specification must designate the Amazon Resource Name
   (ARN) of the AWS managed key. You can obtain the ARN from the AWS KMS console. To get the
   correct ARN, ensure that you log in to the AWS KMS console with the same AWS account and
   Region as the AWS managed key that was used to encrypt the location.

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
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 ]
}`

```

You can use KMS key aliases instead of the key ID - `arn:aws:kms:region:account-id:key/alias/your-key-alias`

For more information, see [Aliases in AWS KMS](../../../kms/latest/developerguide/kms-alias.md "../../../kms/latest/developerguide/kms-alias.md") section in the AWS Key Management Service Developer Guide. 3. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as the data lake
administrator or as a user with the `lakeformation:RegisterResource` IAM
permission. 4. In the navigation pane, under **Administration**, choose
**Data lake locations**. 5. Choose **Register location**, and then choose
**Browse** to select an Amazon S3 path. 6. (Optional, but strongly recommended) Choose **Review location
permissions** to view a list of all existing resources in the selected Amazon S3
location and their permissions.

Registering the selected location might result in your Lake Formation users gaining access to
data already at that location. Viewing this list helps you ensure that existing data
remains secure. 7. For **IAM role**, choose the role that you created in Step 1. 8. Choose **Register location**.
