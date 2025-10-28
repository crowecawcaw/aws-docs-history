# Connect discovery

account

In this step, you create a connector to an AWS account and AWS Region that
AWS Transform can use for storing and analyzing discovery data. You can either use an
existing discovery connector if your workspace has one, or you can create a new
discovery connector. For information about the role of the discovery account in this
migration process, and for discovery Region considerations, see [Discovery account connector](transform-app-vmware-acct-connections.md#transform-app-vmware-disc-acct "transform-app-vmware-acct-connections.md#transform-app-vmware-disc-acct").

###### Important

AWS Transform will create an Amazon S3 bucket on your behalf in this discovery
AWS account. This bucket won't have `SecureTransport` enabled by
default. If you want the bucket policy to include secure transport, you must
update the policy yourself. For more information, see [Security best
practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

###### To use an existing discovery connector

1. In the **Job Plan** pane expand **Connect
   discovery account**, and then choose **Create or select
   connectors**.
2. In the **Collaboration** tab, select an existing
   connector from the list of available connectors, and then choose
   **Use connector**. If a connector is grayed out, that
   means its version isn't compatible with the job type that you selected
   earlier.
3. Choose **Send to AWS Transform**.

###### To create a new connector

1. In the **Job Plan** pane expand **Connect
   discovery account**, and then choose **Create or select
   connectors**.
2. If you have existing connectors in the current workspace, go to the
   **Collaboration** tab, and choose **Create new
   connector**.
3. In the **Collaboration** tab, enter the ID of the
   AWS account that you want to use for discovery, and then choose
   **Next**.
4. Choose whether you want to use Amazon S3 managed keys for encryption. If you
   specify your own KMS key, you can use the default key policy. However, if
   you want a less permissive key policy, the following is an example. For
   information about how to create a KMS key, see [Create a KMS
   key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

AWS Transform uses the `kms:DescribeKey` permission to make sure
the key exists. It uses the `kms:GenerateDataKey` and
`kms:Decrypt` permissions to encrypt and decrypt the
transformation job data in the Amazon S3 bucket.

AWS Transform uses default Amazon S3 encryption. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") 5. Choose **Continue**. 6. Copy the verification link, share it with an administrator of the
discovery AWS account, and ask them to approve the connection
request. 7. After the administrator of the AWS account approves the request, choose
**Send to AWS Transform**.
