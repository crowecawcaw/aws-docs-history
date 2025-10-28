Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authentication with mTLS for Redshift

streaming ingestion from Apache Kafka sources

Mutual transport-layer security (mTLS) provides the means for a server to authenticate a client it's
sending information to, and for the client to authenticate the
server. The benefit of using mTLS is to provide trusted authentication for a
variety of use cases in several industry-vertical applications. These include use cases in financial,
retail, government and healthcare industries. In the case of streaming ingestion to Redshift, authentication
occurs between a server, which can be Amazon MSK, Apache Kafka, or Confluent Cloud, and an Amazon Redshift provisioned cluster
or an Amazon Redshift Serverless workgroup.

This topic provides procedures and SQL-command examples that show ways to create an external
schema that uses mTLS to authenticate between the Redshift client and any Apache Kafka server.
The steps in this topic complement the full set of steps
for setting up streaming ingestion from Apache Kafka sources.
For more information, see [Getting started with streaming ingestion
from Apache Kafka sources](materialized-view-streaming-ingestion-getting-started-MSK.md "materialized-view-streaming-ingestion-getting-started-MSK.md").

## Prerequisites for

using mTLS for streaming ingestion

This section provides prerequisite steps for using mTLS for streaming ingestion with either
AWS Certificate Manager or AWS Secrets Manager.

As a preliminary step, you must have or create a private certificate authority (PCA), which
you can use to issue certificates that, among other functions, enable
secure communication through secure communication channels. AWS Private Certificate Authority
(Private CA) is an available service that performs this
function. For more information, see
[Creating a private CA](../../../privateca/latest/userguide/create-CA.md "../../../privateca/latest/userguide/create-CA.md") in the _AWS Private Certificate Authority
User Guide_. After creating the Private CA, export the root CA certificate and save it to a file with a .pem extension.

To create a cluster that uses the CA certificate, do the following:

Amazon MSK

1. Create an Amazon MSK cluster that supports mtls client authentication. For more information about
   configuring an Amazon MSK cluster, see [Mutual TLS client authentication for Amazon MSK](../../../msk/latest/developerguide/msk-authentication.md#msk-authentication-cluster "../../../msk/latest/developerguide/msk-authentication.md#msk-authentication-cluster") in
   the _Amazon Managed Streaming for Apache Kafka Developer Guide_.
2. Edit the security settings for the Amazon MSK cluster, turning on TLS client authentication using AWS Certificate Manager (ACM) and selecting the AWS Private CA (PCA)
   you created previously. For more information, see [Updating security settings of a
   cluster](../../../msk/latest/developerguide/msk-update-security.md "../../../msk/latest/developerguide/msk-update-security.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.

Confluent Cloud

1. Create a dedicated Confluent Cloud cluster, preferably in the same
   AWS Region as your Amazon Redshift cluster. For information about creating a Confluent Cloud cluster, see
   [Create a Kafka cluster in Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/index.html#step-1-create-a-ak-cluster-in-ccloud "https://docs.confluent.io/cloud/current/get-started/index.html#step-1-create-a-ak-cluster-in-ccloud").
2. Upload the exported AWS Private CA root CA certificate pem file you created earlier. For more
   information, see
   [Manage certificate authority for mTLS authentication for Confluent Cloud](https://docs.confluent.io/cloud/current/security/authenticate/workload-identities/identity-providers/mtls/certificate-authority.html "https://docs.confluent.io/cloud/current/security/authenticate/workload-identities/identity-providers/mtls/certificate-authority.html").
   Confluent Cloud uses this certificate to verify the Amazon Redshift client certificate.

## Using mTLS for streaming ingestion with AWS Certificate Manager

The following procedure shows how to configure mTLS for Redshift streaming ingestion by using
AWS Certificate Manager (ACM) for certificate storage and management:

1. Request a private certificate through ACM. When you do this, select the PCA you created
   in the Prerequisites section as the certificate authority. ACM stores the signed certificate and attached private key
   for secure communication. For more information about managing certificates with ACM,
   see [Issuing and managing certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the _AWS Certificate Manager User Guide_.
2. For the IAM role that you use to manage your Redshift cluster or Amazon Redshift Serverless workgroup, attach the permission to export the
   certificate, which is **acm:ExportCertificate**. For more information
   about setting up the necessary IAM resources for streaming ingestion,
   see [Setting up streaming ingestion from Kafka](materialized-view-streaming-ingestion-getting-started-MSK.md#materialized-view-streaming-ingestion-getting-started-MSK-setup "materialized-view-streaming-ingestion-getting-started-MSK.md#materialized-view-streaming-ingestion-getting-started-MSK-setup"). Specify the
   same IAM role in the next step to create the external schema.

###### Note

Requests to AWS Certificate Manager require an Internet gateway (IGW) or a NAT gateway (NGW) in your
VPC. If your VPC doesn't have either an IGW or a NGW, do the following:

    * Use Secrets Manager instead of ACM to store your certificates.
    * Attach a Secrets Manager VPC endpoint to your VPC.For information about using Secrets Manager with mTLS for streaming ingestion, see [Using mTLS for streaming ingestion

with AWS Secrets Manager](#materialized-view-streaming-ingestion-mtls-secrets-manager "#materialized-view-streaming-ingestion-mtls-secrets-manager") following. 3. Get the bootstrap broker URI for the Amazon MSK, Apache Kafka, or Confluent Cloud cluster.
For information about getting the bootstrap broker URI for Amazon MSK, see
[Getting the bootstrap brokers for
an Amazon MSK cluster](../../../msk/latest/developerguide/msk-get-bootstrap-brokers.md "../../../msk/latest/developerguide/msk-get-bootstrap-brokers.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_. 4. Run a SQL command such as the following example to create an external schema that maps the
cluster to a Redshift external schema, using `mtls`.

Amazon MSK

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
IAM_ROLE 'arn:aws:iam::012345678901:role/my_role'
AUTHENTICATION mtls
URI 'b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094,b-2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094'
AUTHENTICATION_ARN 'arn:aws:acm:Region:444455556666:certificate/certificate_ID';
```

Apache Kafka or Confluent Cloud

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
IAM_ROLE 'arn:aws:iam::012345678901:role/my_role'
AUTHENTICATION mtls
URI 'lkc-2v531.domz6wj0p.us-west-1.aws.confluent.cloud:9092'
AUTHENTICATION_ARN 'arn:aws:acm:region:444455556666:certificate/certificate_ID';
```

Important parameters:

    * IAM\_ROLE – The IAM role associated with the cluster, for streaming ingestion.
    * URI – The bootstrap broker URI for the cluster. Note that for Amazon MSK,
     port 9094 is specified for communicating with brokers for TLS encryption.
    * AUTHENTICATION\_ARN – The ARN of the ACM certificate. The ARN is available in
     the ACM console when you choose the issued certificate.

After performing these configuration steps, you can create a Redshift materialized view that references
the schema defined in the sample and then
use REFRESH MATERIALIZED VIEW to stream data. For more information, see
[Getting started with streaming ingestion
from Apache Kafka sources](materialized-view-streaming-ingestion-getting-started-MSK.md "materialized-view-streaming-ingestion-getting-started-MSK.md").

## Using mTLS for streaming ingestion

with AWS Secrets Manager

You can configure mTLS for Redshift streaming ingestion by using
AWS Secrets Manager for certificate management if you don't want to reference the
certificate in AWS Certificate Manager. The following steps describe how to configure mTLS using Secrets Manager.

1. Create a certificate signing request and private key with your tool of choice. Then you can use the signing request to generate a signed certificate, using the same
   AWS Private CA (PCA) that you used to generate the certificate for the cluster. For more information about issuing a certificate,
   see [IssueCertificate](../../../privateca/latest/APIReference/API_IssueCertificate.md "../../../privateca/latest/APIReference/API_IssueCertificate.md") in the _AWS Private Certificate Authority
   API Reference_.
2. Extract the certificate using AWS Private Certificate Authority. For more information, see
   [Retrieve a private certificate](../../../privateca/latest/userguide/PcaGetCert.md "../../../privateca/latest/userguide/PcaGetCert.md")
   in the _AWS Private Certificate Authority User Guide_.
3. Store the certificate and private key generated in the previous step in AWS Secrets Manager.
   Choose `Other type of secret` and use the plaintext format. The key-value pairs should be in the format
   `{"certificate":"<cert value>","privateKey":"<pkey value>"}`, as in the following example. For more
   information about creating and managing secrets in AWS Secrets Manager,
   see [Create and manage secrets with AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the _AWS Secrets Manager
   User Guide_.

```
{"certificate":"-----BEGIN CERTIFICATE-----
klhdslkfjahksgdfkgioeuyihbflahabhbdslv6akybeoiwv1hoaiusdhbahsbdi
H4hAX8/eE96qCcjkpfT84EdvHzp6fC+/WwM0oXlwUEWlvfMCXNaG5D8SqRq3qA==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
klhdslkfjahksgdfkgioeuyihbflahabhbdslv6akybeoiwv1hoaiusdhbahsbdi
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
-----END CERTIFICATE-----",
"privateKey":"-----BEGIN PRIVATE KEY-----
klhdslkfjahksgdfkgioeuyihbflahabhbdslv6akybeoiwv1hoaiusdhbahsbdi
7OD4m1dBEs3Fj++hDMH9rYRp99RqtCOf0EWOUe139KOilOsW+cyhAoc9Ci2+Jo/k
17u2N1iGILMQEZuCRtnJOkFYkw==
-----END PRIVATE KEY-----"}
```

4. Attach the permission policy to retrieve the secret
   to the IAM role that you use to manage your Amazon Redshift cluster or Amazon Redshift Serverless workgroup.
   This permission is `secretsmanager:GetSecretValue`. For more information, see
   [Set
   up authentication](materialized-view-streaming-ingestion-getting-started-MSK.md#materialized-view-streaming-ingestion-getting-started-MSK-setup-auth "materialized-view-streaming-ingestion-getting-started-MSK.md#materialized-view-streaming-ingestion-getting-started-MSK-setup-auth").
   For more information about managing IAM policies, see
   [Edit IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md").
   Specify the same IAM role in the next step to create the external schema.
5. In Redshift, run the SQL command to create the external schema.
   You use the AUTHENTICATION type `mtls`. You also specify the URI of the cluster and the secret ARN in
   AWS Secrets Manager.

```
CREATE EXTERNAL SCHEMA my_schema
FROM KAFKA
IAM_ROLE 'arn:aws:iam::012345678901:role/my_role'
AUTHENTICATION mtls
URI 'b-1.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094,b-2.myTestCluster.123z8u.c2.kafka.us-west-1.amazonaws.com:9094'
SECRET_ARN 'arn:aws:secretsmanager:us-east-1:012345678910:secret:myMTLSSecret';
```

Important parameters:

- IAM_ROLE – The IAM role associated with the cluster, for streaming ingestion.
- URI – The bootstrap broker URI for the cluster. Note that
  for Amazon MSK, port 9094 is specified for communicating with brokers for TLS encryption.
- SECRET_ARN – The ARN of the secret from Secrets Manager, containing the certificate to use for mTLS.

## Enabling mTLS authentication for an existing external schema

If you have an existing external schema that you use for streaming ingestion and you want to implement
mutual TLS for authentication, you can run
a command such as the following, which specifies mTLS authentication and the ACM certificate ARN in ACM.

```
ALTER EXTERNAL SCHEMA schema_name
AUTHENTICATION mtls
AUTHENTICATION_ARN 'arn:aws:acm:Region:444455556666:certificate/certificate_ID';
```

Or you can specify mTLS authentication, with reference to the secret ARN in AWS Secrets Manager.

```
ALTER EXTERNAL SCHEMA schema_name
AUTHENTICATION mtls
SECRET_ARN 'arn:aws:secretsmanager:us-east-1:012345678910:secret:myMTLSSecret';
```

For information about the ALTER EXTERNAL SCHEMA command, see [ALTER EXTERNAL SCHEMA](r_ALTER_EXTERNAL_SCHEMA.md "r_ALTER_EXTERNAL_SCHEMA.md").
