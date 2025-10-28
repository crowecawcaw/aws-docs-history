# Setting up encryption in AWS Glue

The following example workflow highlights the options to configure when you use encryption
with AWS Glue. The example demonstrates the use of specific AWS Key Management Service (AWS KMS) keys, but you might
choose other settings based on your particular needs. This workflow highlights only the options
that pertain to encryption when setting up AWS Glue.

1. If the user of the AWS Glue console doesn't use a permissions policy that allows all
   AWS Glue API operations (for example, `"glue:*"`), confirm that the following
   actions are allowed:
   - `"glue:GetDataCatalogEncryptionSettings"`
   - `"glue:PutDataCatalogEncryptionSettings"`
   - `"glue:CreateSecurityConfiguration"`
   - `"glue:GetSecurityConfiguration"`
   - `"glue:GetSecurityConfigurations"`
   - `"glue:DeleteSecurityConfiguration"`

2. Any client that accesses or writes to an encrypted catalog—that is, any console
   user, crawler, job, or development endpoint—needs the following permissions.
3. Any user or role that accesses an encrypted connection password needs the following
   permissions.
4. The role of any extract, transform, and load (ETL) job that writes encrypted data to
   Amazon S3 needs the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 }
}`

```

5. Any ETL job or crawler that writes encrypted Amazon CloudWatch Logs requires the following
   permissions in the key and IAM policies.

In the key policy (not the IAM policy):

```
{
 	"Effect": "Allow",
 	"Principal": {
 		"Service": "logs.region.amazonaws.com"
 	},
 	"Action": [
 		"kms:Encrypt*",
 		"kms:Decrypt*",
 		"kms:ReEncrypt*",
 		"kms:GenerateDataKey*",
 		"kms:Describe*"
 	],
 	"Resource": "`<arn of key used for ETL/crawler cloudwatch encryption>`"
 }

```

For more information about key policies, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

In the IAM policy attach the `logs:AssociateKmsKey` permission:

```
{
 	"Effect": "Allow",
 	"Principal": {
 		"Service": "logs.region.amazonaws.com"
 	},
 	"Action": [
 		"logs:AssociateKmsKey"
 	],
 	"Resource": "`<arn of key used for ETL/crawler cloudwatch encryption>`"
 }

```

6. Any ETL job that uses an encrypted job bookmark needs the following
   permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/*"
 }
}`

```

7. On the AWS Glue console, choose **Settings** in the navigation
   pane.
   1. On the **Data catalog settings** page, encrypt your Data Catalog by
      selecting **Metadata encryption**. This option encrypts all the objects
      in the Data Catalog with the AWS KMS key that you choose.
   2. For **AWS KMS key**, choose **aws/glue**. You can
      also choose a AWS KMS key that you created.

###### Important

AWS Glue supports only symmetric customer master keys (CMKs). The **AWS KMS
key** list displays only symmetric keys. However, if you
select **Choose a AWS KMS key ARN**, the console lets you
enter an ARN for any key type. Ensure that you enter only ARNs for
symmetric keys.

When encryption is enabled, the client that is accessing the Data Catalog must have AWS KMS
permissions. 8. In the navigation pane, choose **Security configurations**. A
security configuration is a set of security properties that can be used to configure AWS Glue
processes. Then choose **Add security configuration**. In the
configuration, choose any of the following options:

    1. Select **S3 encryption**. For **Encryption
     mode**, choose **SSE-KMS**. For the **AWS KMS
     key**, choose **aws/s3** (ensure that the user has
     permission to use this key). This enables data written by the job to Amazon S3 to use the AWS
     managed AWS Glue AWS KMS key.
    2. Select **CloudWatch logs encryption**, and choose a CMK. (Ensure
     that the user has permission to use this key). For more information, see
     [Encrypt Log Data in CloudWatch Logs Using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the *AWS Key Management Service Developer Guide*.


    ###### Important

    AWS Glue supports only symmetric customer master keys (CMKs). The **AWS KMS
     key** list displays only symmetric keys. However, if you
     select **Choose a AWS KMS key ARN**, the console lets you
     enter an ARN for any key type. Ensure that you enter only ARNs for
     symmetric keys.
    3. Choose **Advanced properties**, and select **Job bookmark
     encryption**. For the **AWS KMS key**, choose
     **aws/glue** (ensure that the user has permission to use this key).
     This enables encryption of job bookmarks written to Amazon S3 with the AWS Glue AWS KMS
     key.

9. In the navigation pane, choose **Connections**.
   1. Choose **Add connection** to create a connection to the Java
      Database Connectivity (JDBC) data store that is the target of your ETL job.
   2. To enforce that Secure Sockets Layer (SSL) encryption is used, select
      **Require SSL connection**, and test your connection.

10. In the navigation pane, choose **Jobs**.
    1. Choose **Add job** to create a job that transforms data.
    2. In the job definition, choose the security configuration that you created.

11. On the AWS Glue console, run your job on demand. Verify that any Amazon S3 data written by the
    job, the CloudWatch Logs written by the job, and the job bookmarks are all
    encrypted.
