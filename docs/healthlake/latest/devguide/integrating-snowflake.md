

# Snowflake integration

Snowflake queries the tables in your HealthLake data stores in place, through a read-only path that uses the AWS Glue Iceberg REST endpoint and Lake Formation credential vending. Snowflake doesn't modify HealthLake data.

**Important**  
After HealthLake data is read into Snowflake, you govern that data in Snowflake, including any protected health information (PHI). Don't put protected health information (PHI) in object names, integration names, role names, comments, query tags, or logs. Restrict access to AWS CloudTrail, Snowflake query history, and other audit records. For more information, see the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

**Note**  
Snowflake and Snowflake catalog integrations are third-party products that AWS doesn't provide or support. For information about catalog integrations, see [Configure a catalog integration for AWS Glue Iceberg REST](https://docs.snowflake.com/en/user-guide/tables-iceberg-configure-catalog-integration-rest-glue) in the Snowflake documentation.

## How it works
<a name="integrating-snowflake-how-it-works"></a>

HealthLake keeps an Apache Iceberg table for each FHIR resource type and keeps it current. For more information about how analytics access works, see [How analytics access works](integrating-analytics.md#integrating-analytics-how-it-works). Snowflake reads these tables through a catalog integration that assumes an IAM role in your account and gets temporary, table-scoped credentials from Lake Formation.

![Snowflake users query a catalog-backed Iceberg table. The Snowflake catalog integration assumes an IAM role in your AWS account that trusts only the Snowflake identity and external ID. It signs requests to the AWS Glue Iceberg REST endpoint with SigV4, resolves the HealthLake resource link, and gets temporary credentials from AWS Lake Formation. Snowflake then reads the HealthLake Iceberg table files directly from Amazon S3.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-snowflake-architecture.png)


The following steps describe the request flow when a Snowflake user runs a query:

1. The Snowflake catalog integration assumes the IAM role in your account with its external ID, and signs requests to the AWS Glue Iceberg REST endpoint with SigV4.

1. The endpoint resolves the resource link in your account to the HealthLake target database.

1. Lake Formation evaluates `DESCRIBE` and `SELECT` on the named target table and `DESCRIBE` on the resource link database.

1. If authorization succeeds, Lake Formation vends temporary credentials, and Snowflake reads the Iceberg table files directly from Amazon S3.

## Limitations and considerations
<a name="integrating-snowflake-considerations"></a>

The integration has the following limitations:
+ **Read-only.** Snowflake reads HealthLake tables in place and never modifies HealthLake data.
+ **One table for each grant.** You create one Snowflake Iceberg table for each HealthLake table that you grant. This procedure grants named tables, not all tables.
+ **Credential lifetime.** Snowflake uses the credential expiration that the catalog provider supplies. If none is supplied, Snowflake assumes that credentials expire 60 minutes after receipt. For how revocation interacts with credential lifetime, see [Revoking access](integrating-analytics-getting-started.md#integrating-analytics-granting-revoke).
+ **AWS Regions.** Keep your Snowflake catalog integration and the HealthLake data store in the same AWS Region.
+ **Isolation.** Use separate IAM roles and catalog integrations for workloads with different authorization boundaries.
+ **External ID.** Recreating the catalog integration can change the external ID. If you recreate it, describe it again and replace the trust policy with the current values.

**Topics**
+ [How it works](#integrating-snowflake-how-it-works)
+ [Limitations and considerations](#integrating-snowflake-considerations)
+ [Setting up](integrating-snowflake-setting-up.md)
+ [Troubleshooting](integrating-snowflake-troubleshooting.md)