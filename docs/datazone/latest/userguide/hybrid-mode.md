# Amazon DataZone integration with AWS Lake Formation

hybrid mode

Amazon DataZone is integrated with AWS Lake Formation hybrid mode. This integration
enables you to easily publish and share your AWS Glue tables through Amazon DataZone
without the need to register them in AWS Lake Formation first. Hybrid mode allows
you to start managing permissions on your AWS Glue tables through AWS Lake
Formation while continuing to maintain any existing IAM permissions on these tables.

To get started, you can enable the **Data location registration**
setting under the **DefaultDataLake** blueprint in the Amazon DataZone
management console.

###### Enable integration with AWS Lake Formation hybrid mode

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with your
   account credentials.
2. Choose **View domains** and choose the domain where you
   want to enable the integration with AWS Lake Formation hybrid mode.
3. On the domain details page, navigate to the
   **Blueprints** tab.
4. From the **Blueprints** list, choose the
   **DefaultDataLake** blueprint.
5. Make sure that the DefaultDataLake blueprint is enabled. If it’s not
   enabled, follow the steps in [Enable built-in blueprints in the AWS
   account that owns the Amazon DataZone domain](working-with-blueprints.md#enable-default-blueprint "working-with-blueprints.md#enable-default-blueprint") to enable it in your AWS
   Account.
6. On the DefaultDataLake details page, open the
   **Provisioning** tab and choose the
   **Edit** button in the top right corner of the page.
7. Under **Data location registration**, check the box to
   enable the data location registration.
8. For the data location management role, you can create a new IAM role or
   select an existing IAM role. Amazon DataZone uses this role to manage read/write
   access to the chosen Amazon S3 bucket(s) for Data Lake using AWS Lake
   Formation hybrid access mode. For more information, see [AmazonDataZoneS3Manage-<region>-<domainId>](AmazonDataZoneS3Manage.md "AmazonDataZoneS3Manage.md").
9. Optionally, you can choose to exclude certain Amazon S3 locations if you
   do not want Amazon DataZone to automatically register them in hybrid mode. For
   this, complete the following steps:
   - Choose the toggle button to exclude specified Amazon S3
     locations.
   - Provide the URI of the Amazon S3 bucket you want to exclude.
   - To add additional buckets, choose **Add S3
     location.**

   ###### Note

   Amazon DataZone only allows excluding a root S3 location. Any S3
   locations within the path of a root S3 location will be
   automatically excluded from registration.
   - Choose **Save changes**.
     Once you have enabled the data location registration setting in your AWS
     account, when a data consumer subscribes to an AWS Glue table managed through IAM
     permissions, Amazon DataZone will first register the Amazon S3 locations of this table in
     hybrid mode, and then grant access to the data consumer by managing permissions on
     the table through AWS Lake Formation. This ensures that IAM permissions on the
     table continue to exist with newly granted AWS Lake Formation permissions, without
     disrupting any existing workflows.

## How to handle encrypted Amazon S3

locations when enabling AWS Lake Formation hybrid mode integration in
Amazon DataZone

If you are using an Amazon S3 location encrypted with an Customer managed or
AWS Managed KMS key, the **AmazonDataZoneS3Manage** role must
have the permission to encrypt and decrypt data with the KMS key, or the KMS key
policy must grant permissions on the key to the role.

If your Amazon S3 location is encrypted with an AWS managed key, add the
following inline policy to the
**AmazonDataZoneDataLocationManagement** role:

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
 "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 }
 ]
}`

```

If your Amazon S3 location is encrypted with a customer managed key, do the
following:

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms") and log in as an AWS
   Identity and Access Management (IAM) administrative user or as a user
   who can modify the key policy of the KMS key used to encrypt the
   location.
2. In the navigation pane, choose **Customer managed
   keys**, and then choose the name of the desired KMS
   key.
3. On the KMS key details page, choose the **Key
   policy** tab, and then do one of the following to add your
   custom role or the Lake Formation service-linked role as a KMS key
   user:
   - If the default view is showing (with Key administrators, Key
     deletion, Key users, and Other AWS accounts sections) – under
     the **Key users** section, add the
     **AmazonDataZoneDataLocationManagement**
     role.
   - If the key policy (JSON) is showing – edit the policy to add
     **AmazonDataZoneDataLocationManagement**
     role to the object "Allow use of the key," as shown in the
     following example

   ```

   ...
           {
               "Sid": "Allow use of the key",
               "Effect": "Allow",
               "Principal": {
                   "AWS": [
                       "arn:aws:iam::111122223333:role/service-role/AmazonDataZoneDataLocationManage-<region>-<domain-id>"
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

###### Note

If the KMS key or Amazon S3 location are not in the same AWS account as
the data catalog, follow the instructions in [Registering an encrypted Amazon S3 location across AWS
accounts](../../../lake-formation/latest/dg/register-cross-encrypted.md "../../../lake-formation/latest/dg/register-cross-encrypted.md").
