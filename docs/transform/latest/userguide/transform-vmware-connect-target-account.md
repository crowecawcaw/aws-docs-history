# Connect

target account

The target account is where your network will be deployed and where your migrated
servers and applications will reside in AWS. For more information, see [Target account connector](transform-app-vmware-acct-connections.md#transform-app-vmware-target-acct "transform-app-vmware-acct-connections.md#transform-app-vmware-target-acct").

###### Important

- AWS Transform will create an Amazon S3 bucket on your behalf in this target
  AWS account. This bucket won't have `SecureTransport` enabled by
  default. If you want the bucket policy to include secure transport, you must
  update the policy yourself. For more information, see [Security best
  practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

###### To use an existing target account connector

1. In the **Job Plan** pane, expand **Choose target
   account**, and then choose **Create or select
   connectors**.
2. In the **Collaboration** tab, select an existing
   connector if your workspace already has connectors, and then choose
   **Use connector**. In the list of available connectors,
   if a connector is grayed out, that means its version isn't compatible with
   the job type that you selected earlier.

###### Important

If you specify a connector with a target AWS Region that is
different from the discovery AWS Region, that means AWS Transform will be
transferring your data across AWS Regions. 3. Choose **Continue**.

###### To create a new connector

1. In the **Job Plan** pane, expand **Connect target
   account**, and then choose **Create or select
   connectors**.
2. Specify the AWS account and AWS Region that you want to use as your
   target, and then choose **Next**.

###### Important

If you specify a target AWS Region that is different from the
discovery AWS Region, that means AWS Transform will be transferring your
data across AWS Regions. 3. Choose whether you want to use Amazon S3 managed keys for encryption. If you
specify your own KMS key, you can use the default key policy. However, if
you want a less permissive key policy, the following is an example. For
information about how to create a KMS key, see [Create a KMS
key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

AWS Transform uses the `kms:DescribeKey` permission to make sure
the key exists. It uses the `kms:GenerateDataKey` and
`kms:Decrypt` permissions to encrypt and decrypt the
transformation job data in the Amazon S3 bucket.

AWS Transform uses default Amazon S3 encryption. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") 4. Choose **Continue**. 5. Copy the verification link, share it with an administrator of the target
AWS account, and ask them to approve the connection request. 6. After the administrator of the AWS account approves the request, select
the newly created connector from the list of connectors in the
**Collaboration** tab, and then choose **Use
connector**. 7. Choose **Send to AWS Transform**.
If you plan to modify the AWS Application Migration Service template to enable post-launch actions, add
the following permission to the target connector role. You can find the name of that
role in the **Collaboration** tab after the connector is created.
For information about how to add permissions to a role, see [Update
permissions for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md") in the
_IAM User Guide_.

```
{
      "Sid": "MGNPostLaunchActions",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": "arn:aws:iam::`target-account-ID`:role/service-role/AWSApplicationMigrationLaunchInstanceWithSsmRole"
}
```
