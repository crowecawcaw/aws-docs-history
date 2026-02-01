Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER EXTERNAL SCHEMA

Alters an existing external schema in the current database. Only schema owners, super-users,
or users with ALTER privileges on the schema can alter it. Only external schemas created from
DATA CATALOG, KAFKA, or MSK can be altered.

The owner of this schema is the issuer of the CREATE EXTERNAL SCHEMA command. To transfer
ownership of an external schema, use ALTER SCHEMA to change the owner. To grant access to the
schema to other users or user groups, use the GRANT command.

You can't use the GRANT or REVOKE commands for permissions on an external table. Instead,
grant or revoke the permissions on the external schema.

For more information, see the following:

- [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md")
- [GRANT](r_GRANT.md "r_GRANT.md")
- [REVOKE](r_REVOKE.md "r_REVOKE.md")
- [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md")
- [Enabling mTLS authentication for an existing external schema](materialized-view-streaming-ingestion-mtls.md#materialized-view-streaming-ingestion-mtls-alter "materialized-view-streaming-ingestion-mtls.md#materialized-view-streaming-ingestion-mtls-alter")
  To view details for external schemas, query the SVV_EXTERNAL_SCHEMAS system view. For more
  information, see [SVV_EXTERNAL_SCHEMAS](r_SVV_EXTERNAL_SCHEMAS.md "r_SVV_EXTERNAL_SCHEMAS.md").

## Syntax

```
ALTER EXTERNAL SCHEMA schema_name
[ IAM_ROLE [ default | 'SESSION' | 'arn:aws:iam::<account-id>:role/<role-name>' ] ]
[ AUTHENTICATION [ none | iam | mtls] ]
[ AUTHENTICATION_ARN 'acm-certificate-arn' | SECRET_ARN 'asm-secret-arn' ]
[ URI 'Kafka bootstrap URL' ]

```

If you have an existing external schema that you use for streaming ingestion and you want to implement mutual TLS for authentication, you can run a command such as the following, which specifies mTLS authentication and the ACM certificate ARN in ACM.

```
ALTER EXTERNAL SCHEMA schema_name
AUTHENTICATION mtls
AUTHENTICATION_ARN 'arn:aws:acm:us-east-1:444455556666:certificate/certificate_ID';
```

Or you can modify mTLS authentication, with reference to the secret ARN in Secrets Manager.

```
ALTER EXTERNAL SCHEMA schema_name
AUTHENTICATION mtls
SECRET_ARN 'arn:aws:secretsmanager:us-east-1:012345678910:secret:myMTLSSecret';
```

The following example shows how to modify the URI for ALTER EXTERNAL SCHEMA:

```
ALTER EXTERNAL SCHEMA schema_name
URI 'lkc-ghidef-67890.centralus.azure.glb.confluent.cloud:9092';
```

The following example shows how to modify the IAM role for ALTER EXTERNAL SCHEMA:

```
ALTER EXTERNAL SCHEMA schema_name
IAM_ROLE 'arn:aws:iam::012345678901:role/testrole';
```

## Parameters

IAM_ROLE[ default | 'SESSION' | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ]

Use the `default` keyword to have Amazon Redshift use the IAM role that is set as default.

Use `'SESSION'` if you connect to your Amazon Redshift cluster using a federated
identity and access the tables from the external schema created using this command.

See [CREATE EXTERNAL
SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.

AUTHENTICATION

The authentication type defined for streaming ingestion. Streaming ingestion
with authentication types works with Apache Kafka, Confluent Cloud, and Amazon Managed Streaming for Apache Kafka.
See [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.

AUTHENTICATION_ARN

The ARN of the AWS Certificate Manager certificate used by Amazon Redshift for mtls authentication
with Apache Kafka, Confluent Cloud, or Amazon Managed Streaming for Apache Kafka (Amazon MSK). The ARN is available in the ACM console when you choose the
issued certificate.

SECRET_ARN

The Amazon Resource Name (ARN) of a supported
secret created using AWS Secrets Manager. For information about how to create and retrieve
an ARN for a secret, see [Manage secrets with AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md") in the
_AWS Secrets Manager User Guide_, and [Retrieving the Amazon Resource Name (ARN) of the secret in Amazon Redshift](../mgmt/redshift-secrets-manager-integration-retrieving-secret.md "../mgmt/redshift-secrets-manager-integration-retrieving-secret.md").

URI

The bootstrap URL of the Apache Kafka, Confluent Cloud or Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster.
The endpoint must be reachable (routable) from the Amazon Redshift cluster.
See [CREATE EXTERNAL
SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.
