Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Changing cluster encryption

You can modify an unencrypted cluster to use AWS Key Management Service (AWS KMS) encryption using either
an AWS-owned key or a customer managed key. When you modify your cluster to enable AWS KMS
encryption, Amazon Redshift automatically migrates your data to a new encrypted cluster. You can
also migrate an encrypted cluster to an unencrypted cluster by modifying the cluster
with the AWS CLI, but not with the AWS Management Console.

During the migration operation, your cluster is available in read-only mode, and the
cluster status appears as **resizing**.

If your cluster is configured to enable cross-AWS Region snapshot copy, you must
disable it before changing encryption. For more information, see [Copying a snapshot to another AWS
Region](cross-region-snapshot-copy.md "cross-region-snapshot-copy.md")
and [Configuring cross-Region snapshot copy
for an AWS KMS–encrypted cluster](xregioncopy-kms-encrypted-snapshot.md "xregioncopy-kms-encrypted-snapshot.md"). You can't enable hardware
security module (HSM) encryption by modifying the cluster. Instead, create a new,
HSM-encrypted cluster and migrate your data to the new cluster. For more information,
see [Migrating to an HSM-encrypted
cluster](migrating-to-an-encrypted-cluster.md "migrating-to-an-encrypted-cluster.md").

Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose the cluster that you want to modify encryption.
3. Choose **Properties**.
4. In the **Database configurations** section,
   choose **Edit**, then choose **Edit
   encryption**.
5. Choose one of the encryption options and choose **Save
   changes**.

AWS CLI
To modify your unencrypted cluster to use AWS KMS, run the
`modify-cluster` CLI command and specify
`–-encrypted`, as shown following. By default, your default
KMS key is used. To specify a customer managed key, include the
`--kms-key-id` option.

```
aws redshift modify-cluster --cluster-identifier <value> --encrypted --kms-key-id <value>
```

To remove encryption from your cluster, run the following CLI
command.

```
aws redshift modify-cluster --cluster-identifier <value> --no-encrypted
```
