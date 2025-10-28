Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Unloading encrypted data files

UNLOAD automatically creates files using Amazon S3 server-side encryption with
AWS managed encryption keys (SSE-S3). You can also specify server-side encryption
with an AWS Key Management Service key (SSE-KMS) or client-side encryption with a
customer managed key. UNLOAD doesn't support Amazon S3 server-side encryption
using a customer-supplied key. For more information, see [Protecting data using
server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").

To unload to Amazon S3 using server-side encryption with an AWS KMS key, use the
KMS_KEY_ID parameter to provide the key ID as shown in the following
example.

```
unload ('select venuename, venuecity from venue')
to 's3://amzn-s3-demo-bucket/encrypted/venue_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
KMS_KEY_ID '1234abcd-12ab-34cd-56ef-1234567890ab'
encrypted;
```

If
you want to provide your own encryption key, you can create client-side encrypted
data files in Amazon S3 by using the UNLOAD command with the ENCRYPTED option. UNLOAD
uses the same envelope encryption process that Amazon S3 client-side encryption uses.
You can then use the COPY command with the ENCRYPTED option to load the encrypted
files.

The process works like this:

1. You create a base64 encoded 256-bit AES key that you will use as your
   private encryption key, or _root symmetric
   key_.
2. You issue an UNLOAD command that includes your root symmetric key
   and the ENCRYPTED option.
3. UNLOAD generates a one-time-use symmetric key (called the _envelope symmetric key_) and an
   initialization vector (IV), which it uses to encrypt your data.
4. UNLOAD encrypts the envelope symmetric key using your root symmetric
   key.
5. UNLOAD then stores the encrypted data files in Amazon S3 and stores
   the encrypted envelope key and IV as object metadata with each file.
   The encrypted envelope key is stored as object metadata
   `x-amz-meta-x-amz-key` and the IV is stored as object
   metadata `x-amz-meta-x-amz-iv`.
   For more information about the envelope encryption process, see the [Client-side data
   encryption with the AWS SDK for Java and Amazon S3](https://aws.amazon.com/articles/2850096021478074 "https://aws.amazon.com/articles/2850096021478074") article.

To unload encrypted data files, add the root key value to the credentials string
and include the ENCRYPTED option. If you use the MANIFEST option, the manifest
file is also encrypted.

```
unload ('select venuename, venuecity from venue')
to 's3://amzn-s3-demo-bucket/encrypted/venue_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
master_symmetric_key '`<root_key>`'
manifest
encrypted;
```

To unload encrypted data files that are GZIP compressed, include the GZIP option
along with the root key value and the ENCRYPTED option.

```
unload ('select venuename, venuecity from venue')
to 's3://amzn-s3-demo-bucket/encrypted/venue_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
master_symmetric_key '`<root_key>`'
encrypted gzip;
```

To load the encrypted data files, add the MASTER_SYMMETRIC_KEY parameter with the
same root key value and include the ENCRYPTED option.

```
copy venue from 's3://amzn-s3-demo-bucket/encrypted/venue_'
iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
master_symmetric_key '`<root_key>`'
encrypted;
```
