

# Source configuration for Snowflake Platform

## Prerequisites
<a name="snowflake-platform-prerequisites"></a>

Before you begin, make sure you have the following:
+ A Snowflake account where you can use the `ACCOUNTADMIN` role to create a role and grant privileges.
+ An AWS account with [permissions](pipeline-iam-reference.md#api-caller-permissions) to create and manage CloudWatch pipelines.
+ An AWS account with [permissions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html#reference_iam-permissions) to create and manage secrets in AWS Secrets Manager.

## Integrating with Snowflake Platform
<a name="snowflake-platform-integration"></a>

CloudWatch pipelines use the Snowflake *Structured Query Language (SQL)* API (`POST /api/v2/statements`) to query audit data. The data comes from views in the `SNOWFLAKE.ACCOUNT_USAGE` schema and from the default event table, `SNOWFLAKE.TELEMETRY.EVENTS`.

The following table lists the `SNOWFLAKE.ACCOUNT_USAGE` views that you can collect data from, grouped by category.


| Category | Views | 
| --- | --- | 
| Query and access | QUERY\_HISTORY, ACCESS\_HISTORY | 
| Security and authentication | LOGIN\_HISTORY, SESSIONS, USERS, ROLES, GRANTS\_TO\_ROLES, GRANTS\_TO\_USERS | 
| Data movement | DATA\_TRANSFER\_HISTORY, STAGES, COPY\_HISTORY, LOAD\_HISTORY | 
| Policy and governance | NETWORK\_POLICIES, PASSWORD\_POLICIES, MASKING\_POLICIES, ROW\_ACCESS\_POLICIES, NETWORK\_RULES, SECRETS, TAGS | 
| Warehouse and replication | WAREHOUSE\_METERING\_HISTORY, REPLICATION\_USAGE\_HISTORY | 

For more information about these views, see [Account Usage](https://docs.snowflake.com/en/sql-reference/account-usage) on the Snowflake website.

## Setting up access to Snowflake
<a name="snowflake-platform-authentication"></a>

To read audit data, the pipeline signs in to your Snowflake account as a dedicated user with a dedicated role. The pipeline authenticates by using a *JSON Web Token (JWT)* key pair with the RS256 (*Rivest-Shamir-Adleman (RSA)* Signature with SHA-256) algorithm, which the Snowflake SQL API v2 requires. Run the SQL statements in these steps from a Snowsight SQL worksheet while you use the `ACCOUNTADMIN` role.

1. Create a role for the pipeline and grant it the Snowflake database roles that read the audit views. Replace {{role-name}}, {{warehouse-name}}, and {{user-name}} with your own values, and then run the following statements:

   ```sql
   CREATE ROLE {{role-name}};
   
   GRANT DATABASE ROLE SNOWFLAKE.GOVERNANCE_VIEWER TO ROLE {{role-name}};
   GRANT DATABASE ROLE SNOWFLAKE.SECURITY_VIEWER TO ROLE {{role-name}};
   GRANT DATABASE ROLE SNOWFLAKE.USAGE_VIEWER TO ROLE {{role-name}};
   GRANT DATABASE ROLE SNOWFLAKE.OBJECT_VIEWER TO ROLE {{role-name}};
   
   GRANT USAGE ON WAREHOUSE {{warehouse-name}} TO ROLE {{role-name}};
   
   GRANT ROLE {{role-name}} TO USER {{user-name}};
   ```

   The placeholders in the preceding statements are the following:
   + {{role-name}} – The name of the role for the pipeline
   + {{warehouse-name}} – The warehouse that runs the pipeline's queries
   + {{user-name}} – The Snowflake user that the pipeline signs in as

   For more information about database roles, see [SNOWFLAKE database roles](https://docs.snowflake.com/en/sql-reference/snowflake-db-roles) and [GRANT DATABASE ROLE](https://docs.snowflake.com/en/sql-reference/sql/grant-database-role) on the Snowflake website.

1. Grant the role access to the `ACCOUNT_USAGE` views and the default event table so that the pipeline can query them. Replace {{role-name}} with the role from the previous step, and then run the following statements:

   ```sql
   GRANT USAGE ON DATABASE SNOWFLAKE TO ROLE {{role-name}};
   GRANT USAGE ON SCHEMA SNOWFLAKE.ACCOUNT_USAGE TO ROLE {{role-name}};
   GRANT SELECT ON ALL VIEWS IN SCHEMA SNOWFLAKE.ACCOUNT_USAGE TO ROLE {{role-name}};
   GRANT APPLICATION ROLE SNOWFLAKE.EVENTS_ADMIN TO ROLE {{role-name}};
   ```

   The `SNOWFLAKE.EVENTS_ADMIN` application role grants `SELECT` on the default event table. For more information, see [Event table overview](https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up) on the Snowflake website.

1. Generate an RSA key pair of at least 2048 bits that the pipeline uses to sign in. In a terminal, run the following commands:

   ```bash
   $ openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
   $ openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
   ```

   These commands produce the following files:
   + `rsa_key.p8` – An unencrypted PKCS\#8 private key
   + `rsa_key.pub` – The matching public key

   To encrypt the private key instead, omit `-nocrypt` and enter a passphrase when prompted. You then provide that passphrase in the `private_key_passphrase` parameter.

1. Assign the public key to the Snowflake user so that Snowflake can verify the pipeline's sign-in requests. Replace {{user-name}} and {{public-key}} with your own values, and then run the following statement:

   ```sql
   ALTER USER {{user-name}} SET RSA_PUBLIC_KEY='{{public-key}}';
   ```

   The placeholders in the preceding statement are the following:
   + {{user-name}} – The Snowflake user that the pipeline signs in as
   + {{public-key}} – The contents of `rsa_key.pub`, without the `BEGIN` and `END` lines

1. Store the user name and private key in AWS Secrets Manager so that the pipeline can read them without exposing them in the configuration. Create a secret whose value is a *JavaScript Object Notation (JSON)* object. The object holds the Snowflake user name and the full *Privacy-Enhanced Mail (PEM)* content of the private key. Include the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.

   The pipeline configuration references each value with the syntax `${{aws_secrets:{{secret-name}}:{{key-name}}}}`. The following example shows the secret value for a secret named `snowflake-credentials`, which matches the pipeline configuration later in this topic:

   ```json
   {
     "user": "{{user-name}}",
     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBg...\n-----END PRIVATE KEY-----"
   }
   ```

   The following example shows the secret value for an encrypted private key, which also includes the passphrase:

   ```json
   {
     "user": "{{user-name}}",
     "private_key": "-----BEGIN ENCRYPTED PRIVATE KEY-----\n...\n-----END ENCRYPTED PRIVATE KEY-----",
     "private_key_passphrase": "{{passphrase}}"
   }
   ```

1. Find your Snowflake account identifier, which the pipeline uses to reach your account. The identifier uses the format `orgname-accountname`, such as `myorg-myaccount`, or `locator.region`, such as `xy12345.us-east-1`. You can find it in the Snowsight URL: `https://app.snowflake.com/{{orgname}}/{{accountname}}`. CloudWatch pipelines use this value to build the SQL API base URL, such as `https://xy12345.us-east-1.snowflakecomputing.com`.

1. Make sure that the warehouse from the first step is running or set to auto-resume, because the pipeline runs its queries on it.

After you complete these steps, the pipeline can sign in to your Snowflake account and query the audit data.

## Configuring the CloudWatch Pipeline
<a name="snowflake-platform-pipeline-config"></a>

When you configure the pipeline, choose **Snowflake Platform** as the data source. Provide the account identifier and the AWS Secrets Manager secret. Optionally, set a backfill duration such as `P7D` (the last 7 days) to control how far back the first run collects logs. After you create the pipeline, the pipeline writes data to the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="snowflake-platform-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and transforms the following events. Events that are not listed are not mapped to OCSF and are forwarded to the sink as raw logs.

### Datastore Activity (6005)
<a name="snowflake-platform-ocsf-datastore"></a>

Contains the following Account Usage views:
+ `QUERY_HISTORY`
+ `COPY_HISTORY`
+ `ACCESS_HISTORY`
+ `DATA_TRANSFER_HISTORY`

### Authentication (3002)
<a name="snowflake-platform-ocsf-authentication"></a>

Contains the following Account Usage views:
+ `LOGIN_HISTORY`
+ `SESSIONS`

### Entity Management (3004)
<a name="snowflake-platform-ocsf-entity-management"></a>

Contains the following Account Usage views:
+ `ROLES`
+ `STAGES`
+ `NETWORK_POLICIES`
+ `PASSWORD_POLICIES`
+ `MASKING_POLICIES`
+ `ROW_ACCESS_POLICIES`

### Group Management (3006)
<a name="snowflake-platform-ocsf-group-management"></a>

Contains the following view. For more information, see [GRANTS\_TO\_ROLES view](https://docs.snowflake.com/en/sql-reference/account-usage/grants_to_roles) on the Snowflake website.
+ `GRANTS_TO_ROLES`

### User Access Management (3005)
<a name="snowflake-platform-ocsf-user-access"></a>

Contains the following view. For more information, see [GRANTS\_TO\_USERS view](https://docs.snowflake.com/en/sql-reference/account-usage/grants_to_users) on the Snowflake website.
+ `GRANTS_TO_USERS`

### User Inventory Info (5003)
<a name="snowflake-platform-ocsf-user-inventory"></a>

Contains the following view. For more information, see [USERS view](https://docs.snowflake.com/en/sql-reference/account-usage/users) on the Snowflake website.
+ `USERS`