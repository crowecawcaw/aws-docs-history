

# Connect Snowflake as a data source in Amazon DataZone
<a name="snowflake-data-source"></a>

Amazon DataZone supports Snowflake as a third-party data source. After you connect Snowflake to a Amazon DataZone project, the catalog can index your Snowflake databases and schemas, capture column-level lineage from Snowflake's query history, and let you query Snowflake tables from through federation. This page walks you through creating a Snowflake connection using the AWS CLI.

## Prerequisites
<a name="snowflake-data-source-prerequisites"></a>

Before you begin, confirm the following are in place:
+ A Amazon DataZone domain and a project where you want the Snowflake data to be cataloged. See [Domains and user access in Amazon DataZone](working-with-domains-users.md) and [Amazon DataZone projects and environments](working-with-projects.md).
+ A Snowflake account, with permission to create roles and grant privileges in the database, schema, and warehouse you want to catalog.
+ Access to AWS Secrets Manager in the same AWS account as your Amazon DataZone domain.
+ An Amazon S3 bucket for query spill, if you plan to query Snowflake data from .

You will perform the steps in this order: create a Snowflake role, store Snowflake credentials in AWS Secrets Manager, find your Amazon DataZone project environment ID, then call `aws datazone create-connection`.

## Step 1: Create a Snowflake role for Amazon DataZone
<a name="snowflake-data-source-step1"></a>

Amazon DataZone connects to Snowflake using a role you create and grant specific privileges to. The role grants fall into four categories:
+ **Metadata sync** — Amazon DataZone reads the structure of your tables and views to populate the catalog.
+ **Lineage sync** — Amazon DataZone reads Snowflake's QUERY\_HISTORY and ACCESS\_HISTORY to derive column-level lineage.
+ **Query access** — required for queries issued through Amazon DataZone, including from .
+ **Warehouse usage** — required for any query the role executes.

Run the following statements in Snowflake, replacing the placeholders with your values:

```
CREATE ROLE <role_name>;

-- Metadata: database and schema access
GRANT USAGE ON DATABASE <database_name> TO ROLE <role_name>;
GRANT USAGE ON SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;

-- Metadata: table and view structure (no data access)
GRANT REFERENCES ON ALL TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;
GRANT REFERENCES ON ALL VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;
GRANT REFERENCES ON FUTURE TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;
GRANT REFERENCES ON FUTURE VIEWS IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;

-- Lineage: access to QUERY_HISTORY and ACCESS_HISTORY
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE <role_name>;

-- Query access
GRANT SELECT ON ALL TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;

-- Optional: include tables created after the role is granted
GRANT SELECT ON FUTURE TABLES IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;

-- Warehouse access
GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE <role_name>;

-- Assign the role to the Snowflake user whose credentials DataZone will use
GRANT ROLE <role_name> TO USER <snowflake_username>;
```

**Important**  
`GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE` is required for lineage. Without it, the metadata sync succeeds but no lineage records are captured.

## Step 2: Store Snowflake credentials in AWS Secrets Manager
<a name="snowflake-data-source-step2"></a>

Create a secret in AWS Secrets Manager, in the same AWS account as your Amazon DataZone domain. Amazon DataZone supports two authentication methods: username and password, or key-pair.

For username and password authentication, use this JSON body:

```
{
  "username": "<snowflake_username>",
  "password": "<snowflake_password>"
}
```

For key-pair authentication, use this JSON body:

```
{
  "sfUser": "<snowflake_username>",
  "pem_private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----"
}
```

Tag the secret so that Amazon DataZone can discover it. Both tags are required:


| Tag key | Value | 
| --- | --- | 
| AmazonDataZoneDomain | Your Amazon DataZone domain ID | 
| AmazonDataZoneProject | Your Amazon DataZone project ID | 

Note the ARN of the secret. You will pass it to `create-connection` in Step 4.

## Step 3: Find your project environment ID
<a name="snowflake-data-source-step3"></a>

The `create-connection` API call requires the ID of the project environment where the connection lives. You can derive this from the project user role ARN.

The project user role ARN follows this pattern:

```
arn:aws:iam::<account_id>:role/datazone_usr_role_<project_id>_<environment_id>
```

The final segment, after the last underscore, is the environment ID. For example, in:

```
arn:aws:iam::123456789012:role/datazone_usr_role_a1b2c3dfadsf_58cjkfdsjfd
```

`58cjkfdsjfd` is the environment ID. This is the value to pass as `--environment-identifier` in Step 4. The environment ID corresponds to your project's Tooling environment.

## Step 4: Create the Snowflake connection
<a name="snowflake-data-source-step4"></a>

Run the following AWS CLI command, replacing the placeholders with your values:

```
aws datazone create-connection \
    --domain-identifier <domain_id> \
    --environment-identifier <environment_id> \
    --name "<connection_name>" \
    --description "<optional_description>" \
    --props '{
      "snowflakeProperties": {
        "connectivityProperties": {
          "connectionProperties": {
            "HOST": "<account>.snowflakecomputing.com",
            "PORT": "443",
            "DATABASE": "<database_name>",
            "WAREHOUSE": "<warehouse_name>",
            "SCHEMA": "<schema_name>",
            "ROLE_ARN": "<project_user_role_arn>",
            "CATALOG_CASING_FILTER": "UPPERCASE_ONLY"
          },
          "athenaProperties": {
            "spill_bucket": "<project_s3_bucket_name>",
            "spill_prefix": "<domain_id>/<project_id>/dev/sys/athena"
          },
          "authenticationConfiguration": {
            "authenticationType": "BASIC",
            "secretArn": "<secret_arn_from_step_2>"
          }
        },
        "snowflakeRole": "<role_name_from_step_1>",
        "identityMapping": {
          "usernameAttribute": "EMAIL"
        }
      }
    }'
```

### Connection properties reference
<a name="snowflake-data-source-connection-properties"></a>


| Property | Description | 
| --- | --- | 
| HOST | Your Snowflake account URL. | 
| PORT | The Snowflake port. Use 443. | 
| DATABASE | The Snowflake database to catalog. | 
| WAREHOUSE | The Snowflake warehouse Amazon DataZone uses to run queries. | 
| SCHEMA | The Snowflake schema to catalog. | 
| ROLE\_ARN | The project user role ARN (see Step 3). | 
| CATALOG\_CASING\_FILTER | Controls case normalization for cataloged identifiers. Valid values are UPPERCASE\_ONLY and LOWERCASE\_ONLY. If omitted, defaults to UPPERCASE\_ONLY. | 
| spill\_bucket | S3 bucket name for query spill. Required when querying Snowflake from . | 
| spill\_prefix | S3 prefix for spill, in the format <domain\_id>/<project\_id>/dev/sys/athena. | 
| authenticationType | BASIC for username/password or key-pair authentication. | 
| secretArn | The ARN of the secret created in Step 2. | 
| snowflakeRole | The Snowflake role name from Step 1. | 
| identityMapping.usernameAttribute | Set to EMAIL. | 

## Verifying the connection
<a name="snowflake-data-source-verify"></a>

Call `aws datazone get-connection` with your domain ID and the connection identifier returned by `create-connection`. After the first metadata sync run, cataloged Snowflake tables appear in the Amazon DataZone catalog for the project.