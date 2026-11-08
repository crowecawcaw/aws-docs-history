

# Data protection in the AWS assistant
<a name="data-protection"></a>

Don't put confidential or sensitive information in tags, resource names, or other free-form fields. Questions and responses can be included in service and diagnostic data as described in this chapter.

## Encryption at rest
<a name="encryption-at-rest"></a>

Data at rest is stored using Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3). It is encrypted by default with AWS owned AWS KMS keys.

You can use a customer managed key only for console chat and console error diagnosis.

## Encryption in transit
<a name="encryption-in-transit"></a>

Communication between customers, the AWS assistant, and its downstream dependencies uses TLS 1.2 or later.

## Key management
<a name="key-management"></a>

If you're an administrator, you can configure a symmetric customer managed AWS KMS key for workforce users with a Pro subscription. The key applies to console chat and console error diagnosis. To use the key, enter it in the Amazon Q Developer console. You need AWS KMS permissions to set up the key. The required permissions are in the example policy [Allow administrators to use the Amazon Q Developer console](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/id-based-policy-examples-admins.html#q-admin-setup-admin-users) in the *Amazon Q Developer User Guide*. For instructions on entering the key, see [Managing the encryption method in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/manage-encryption.html) in the *Amazon Q Developer User Guide*.

When you configure the key, the AWS assistant uses an AWS KMS grant to permit authorized use. Make sure that your users have permission for the AWS assistant to use the key. For an example policy, see [Allow the AWS assistant to access customer managed keys](security-iam-examples.md#iam-example-kms). If you see an error about AWS KMS grants, see [Error related to AWS KMS grants](troubleshooting.md#assistant-kms-grant-error).

If you change the AWS KMS key for console chat, start a new conversation. Conversations encrypted with the previous key aren't available unless the previous key is restored. If you change the key for diagnosis, start a new diagnosis session.