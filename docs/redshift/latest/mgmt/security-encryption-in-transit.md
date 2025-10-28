Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Encryption in transit

You can configure your environment to protect the confidentiality and integrity of data in transit.

The following details apply to encryption of data in transit between an Amazon Redshift cluster and
SQL clients over JDBC/ODBC:

- You can connect to Amazon Redshift clusters from SQL client tools over Java Database
  Connectivity (JDBC) and Open Database Connectivity (ODBC) connections.
- Amazon Redshift supports Secure Sockets Layer (SSL) connections to encrypt data and
  server certificates to validate the server certificate that the client connects to. The client
  connects to the leader node of an Amazon Redshift cluster. For more information, see
  [Configuring security options for
  connections](connecting-ssl-support.md "connecting-ssl-support.md").
- To support SSL connections, Amazon Redshift creates and installs AWS Certificate Manager (ACM)
  issued certificates on each cluster. For more information, see [Transitioning to ACM
  certificates for SSL connections](connecting-transitioning-to-acm-certs.md "connecting-transitioning-to-acm-certs.md").
- To protect your data in transit within the AWS Cloud, Amazon Redshift uses hardware accelerated SSL
  to communicate with Amazon S3 or Amazon DynamoDB for COPY, UNLOAD, backup, and restore
  operations.
  The following details apply to encryption of data in transit between an Amazon Redshift cluster and
  Amazon S3 or DynamoDB:

- Amazon Redshift uses hardware accelerated SSL to communicate with Amazon S3 or
  DynamoDB for COPY, UNLOAD, backup, and restore operations.
- Redshift Spectrum supports the Amazon S3 server-side encryption (SSE) using your account's default key
  managed by the AWS Key Management Service (KMS).
- You can encrypt Amazon Redshift loads with Amazon S3 and AWS KMS. For more information, see [Encrypt Your Amazon Redshift Loads with Amazon S3 and AWS KMS](https://aws.amazon.com/blogs/big-data/encrypt-your-amazon-redshift-loads-with-amazon-s3-and-aws-kms/ "https://aws.amazon.com/blogs/big-data/encrypt-your-amazon-redshift-loads-with-amazon-s3-and-aws-kms/").
  The following details apply to encryption and signing of data in transit between AWS CLI,
  SDK, or API clients and Amazon Redshift endpoints:

- Amazon Redshift provides HTTPS endpoints for encrypting data in transit.
- To protect the integrity of API requests to Amazon Redshift, API calls must be signed
  by the caller. Calls are signed by an X.509 certificate or the
  customer's AWS secret access key according to the Signature Version 4
  Signing Process (Sigv4). For more information, see [Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the
  _AWS General Reference_.
- Use the AWS CLI or one of the AWS SDKs to make requests to AWS. These
  tools automatically sign the requests for you with the access key that you
  specify when you configure the tools.
  The following details apply to encryption of data in transit between Amazon Redshift clusters and
  Amazon Redshift query editor v2:

- Data is transmitted between query editor v2 and Amazon Redshift clusters over a TLS-encrypted channel.
