

# Setting up the Snowflake integration

Two administrators set up the integration in five steps. Each step hands values to the next.

![Two administrators complete five steps. The HealthLake administrator prepares the HealthLake data in step 1 and creates the IAM role with a temporary trust policy in step 2, then sends the role ARN to the Snowflake administrator. The Snowflake administrator creates the catalog integration in step 3, confirms that Snowflake is still blocked, and sends the Snowflake IAM user ARN and external ID back. The HealthLake administrator grants Lake Formation permissions and replaces the trust policy in step 4. The Snowflake administrator creates the Iceberg table and runs a test query in step 5.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-snowflake-setup-flow.png)


The role name `snowflake-healthlake-reader` is fixed, so the role ARN `arn:aws:iam::{{111122223333}}:role/snowflake-healthlake-reader` is known before you create the role.

## Prerequisites
<a name="integrating-snowflake-prerequisites"></a>

Before you begin, make sure that you have the following in AWS:
+ One or more `ACTIVE` HealthLake data stores whose analytical Iceberg tables are available through an AWS Glue resource link in your account.
+ An IAM user or role that is a data lake administrator in Lake Formation, in the same AWS account and Region as the data store. For more information, see [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin) in the *AWS Lake Formation Developer Guide*.
+ Permission to create and update IAM roles, and to grant Lake Formation permissions on the resource links.
+ The AWS CLI (version 2), configured with credentials for the data lake administrator. Run `aws sts get-caller-identity` and confirm the account and principal before you make changes.

You also need the following in Snowflake:
+ A Snowflake account that supports Iceberg REST catalog integrations and catalog-vended credentials.
+ An existing Snowflake virtual warehouse, database, and schema. The examples don't create these objects.
+ A Snowflake role with authority to grant the privileges in [Step 3: Create the catalog integration](#integrating-snowflake-step3).

If your AWS Glue Data Catalog encryption uses a customer managed AWS KMS key, also grant the IAM role the minimum decrypt permission for that key. That key policy is specific to your encryption configuration and isn't shown here.

In the commands in this topic, replace {{us-east-1}} with the AWS Region of your data store.

## Step 1: Prepare HealthLake data
<a name="integrating-snowflake-step1"></a>

**Persona: HealthLake administrator**

Find the resource link, turn on full table access, and confirm that the table you plan to grant exists.

**To prepare the HealthLake data**

1. Find the resource link, catalog ID, and target database for the data store by completing the steps in [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find).

1. Turn on full table access for external engines by completing the steps in [Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)](integrating-analytics-getting-started.md#integrating-analytics-full-table-access).

1. Confirm that the named table exists in the target catalog.

   ```bash
   aws glue get-table \
       --catalog-id {{444455556666}} \
       --database-name {{target-database-name}} \
       --name {{table-name}} \
       --region {{us-east-1}} \
       --query Table.Name \
       --output text
   ```

   Replace the following:
   + {{444455556666}} with the catalog ID (`CatalogId`) of the HealthLake service account that owns the target database, which you found in the first step of this procedure.
   + {{target-database-name}} with the target database of the resource link, which you found in the first step of this procedure.
   + {{table-name}} with the FHIR resource table to grant and query, for example `patient`.

   The output is the table name. If the lookup is denied, stop. Confirm that you're a Lake Formation data lake administrator with permission to inspect the shared HealthLake resources, and don't grant access based on an unverified table name.

**Result:** Full table access is on. Record the resource link name, catalog ID, target database name, and table name. You use them in Step 2, and you use the table name again in Step 5.

## Step 2: Create the IAM role
<a name="integrating-snowflake-step2"></a>

**Persona: HealthLake administrator**

Create the IAM role that Snowflake assumes, with a temporary trust policy and a scoped permissions policy.

**To create the IAM role**

1. Create a temporary trust policy, and save it as `bootstrap-trust-policy.json`. Snowflake's identity isn't known yet, so trust a stable IAM user or role, not an AWS STS assumed-role session ARN.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "arn:aws:iam::{{111122223333}}:role/{{setup-role-name}}"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

   Replace {{111122223333}} with your AWS account ID, and {{setup-role-name}} with the name of your stable IAM role. For an IAM user, use `user/` instead of `role/`.

1. Create a permissions policy that scopes AWS Glue access to the named resources in both accounts, and save it as `snowflake-healthlake-permissions.json`. AWS Glue catalog resources are hierarchical, so table access includes the table, database, and catalog in each path. `lakeformation:GetDataAccess` is isolated in its own statement because that action requires `Resource` set to `*`.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "ReadNamedGlueCatalogResources",
         "Effect": "Allow",
         "Action": [
           "glue:GetCatalog",
           "glue:GetDatabase",
           "glue:GetDatabases",
           "glue:GetTable",
           "glue:GetTables"
         ],
         "Resource": [
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/{{resource-link-name}}",
           "arn:aws:glue:{{us-east-1}}:{{111122223333}}:table/{{resource-link-name}}/{{table-name}}",
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:catalog",
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:database/{{target-database-name}}",
           "arn:aws:glue:{{us-east-1}}:{{444455556666}}:table/{{target-database-name}}/{{table-name}}"
         ]
       },
       {
         "Sid": "RequestLakeFormationCredentials",
         "Effect": "Allow",
         "Action": "lakeformation:GetDataAccess",
         "Resource": "*"
       }
     ]
   }
   ```

   Replace {{us-east-1}} with the AWS Region of your data store, and {{resource-link-name}} with the HealthLake resource link name from Step 1, which is also the catalog namespace.

1. Create the role and attach the policy.

   ```bash
   aws iam create-role \
       --role-name snowflake-healthlake-reader \
       --assume-role-policy-document file://bootstrap-trust-policy.json
   
   aws iam put-role-policy \
       --role-name snowflake-healthlake-reader \
       --policy-name snowflake-healthlake-read \
       --policy-document file://snowflake-healthlake-permissions.json
   ```

1. Get the role ARN.

   ```bash
   aws iam get-role \
       --role-name snowflake-healthlake-reader \
       --query Role.Arn \
       --output text
   ```

   If your role uses a path, include that path in the role ARN wherever you use it, including the Snowflake catalog integration.

**Result:** The role exists with a scoped permissions policy and a temporary trust policy. Record the role ARN. You use it in Step 3 and Step 4. Send the role ARN to the Snowflake administrator.

## Step 3: Create the catalog integration
<a name="integrating-snowflake-step3"></a>

**Persona: Snowflake administrator**

Grant the setup privileges, create the catalog integration, record the Snowflake identity values, and confirm that Snowflake is still blocked.

**To create the catalog integration**

1. Grant the setup privileges to a dedicated role before you create the integration.

   ```SQL
   CREATE ROLE IF NOT EXISTS HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT CREATE INTEGRATION ON ACCOUNT TO ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT USAGE ON WAREHOUSE {{warehouse-name}} TO ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT USAGE ON DATABASE {{snowflake-database}} TO ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT USAGE ON SCHEMA {{snowflake-database}}.{{snowflake-schema}} TO ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT CREATE ICEBERG TABLE ON SCHEMA {{snowflake-database}}.{{snowflake-schema}} TO ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   GRANT ROLE HEALTHLAKE_SNOWFLAKE_SETUP TO USER {{setup-user}};
   ```

   Replace the following:
   + {{warehouse-name}} with your existing Snowflake virtual warehouse.
   + {{snowflake-database}} with your existing Snowflake database.
   + {{snowflake-schema}} with your existing Snowflake schema.
   + {{setup-user}} with the Snowflake user who performs the setup.

   The role that creates the integration owns it, so `HEALTHLAKE_SNOWFLAKE_SETUP` can describe, verify, and use the integration without a separate grant.

1. Select the setup role and the existing Snowflake objects.

   ```SQL
   USE ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   USE WAREHOUSE {{warehouse-name}};
   USE DATABASE {{snowflake-database}};
   USE SCHEMA {{snowflake-database}}.{{snowflake-schema}};
   ```

1. Create the catalog integration. The catalog namespace is the resource link database in your account, not the target database name and not a Snowflake schema.

   ```SQL
   CREATE CATALOG INTEGRATION HEALTHLAKE_CATALOG
     CATALOG_SOURCE = ICEBERG_REST
     TABLE_FORMAT = ICEBERG
     CATALOG_NAMESPACE = '{{resource-link-name}}'
     REST_CONFIG = (
       CATALOG_URI = 'https://glue.{{us-east-1}}.amazonaws.com/iceberg'
       CATALOG_API_TYPE = AWS_GLUE
       CATALOG_NAME = '{{111122223333}}'
       ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
     )
     REST_AUTHENTICATION = (
       TYPE = SIGV4
       SIGV4_IAM_ROLE = 'arn:aws:iam::{{111122223333}}:role/snowflake-healthlake-reader'
       SIGV4_SIGNING_REGION = '{{us-east-1}}'
     )
     ENABLED = TRUE;
   ```

1. Describe the integration, and record the `GLUE_AWS_IAM_USER_ARN` and `GLUE_AWS_EXTERNAL_ID` values. If either value is absent or empty, stop and contact Snowflake Support.

   ```SQL
   DESCRIBE CATALOG INTEGRATION HEALTHLAKE_CATALOG;
   ```

1. Confirm that Snowflake can't assume the role yet, because you haven't trusted the Snowflake identity or granted access.

   ```SQL
   SELECT SYSTEM$VERIFY_CATALOG_INTEGRATION('HEALTHLAKE_CATALOG');
   ```

   Continue only when the result reports `success` as `false` and the error message identifies `sts:AssumeRole`. Any other failure is a setup error, such as a warehouse, endpoint, namespace, or privilege error. Correct it before you continue. If verification succeeds at this point, inspect the role trust policy for an unintended principal.

**Note**  
If a different role runs verification in [Step 5: Create the table and run a test query](#integrating-snowflake-step5), create that role and grant it use of the integration now. Skip this if `HEALTHLAKE_SNOWFLAKE_SETUP` also runs verification.  

```SQL
CREATE ROLE IF NOT EXISTS HEALTHLAKE_SNOWFLAKE_VERIFY;
GRANT USAGE ON INTEGRATION HEALTHLAKE_CATALOG TO ROLE HEALTHLAKE_SNOWFLAKE_VERIFY;
GRANT USAGE ON WAREHOUSE {{warehouse-name}} TO ROLE HEALTHLAKE_SNOWFLAKE_VERIFY;
GRANT USAGE ON DATABASE {{snowflake-database}} TO ROLE HEALTHLAKE_SNOWFLAKE_VERIFY;
GRANT USAGE ON SCHEMA {{snowflake-database}}.{{snowflake-schema}} TO ROLE HEALTHLAKE_SNOWFLAKE_VERIFY;
GRANT ROLE HEALTHLAKE_SNOWFLAKE_VERIFY TO USER {{verify-user}};
```
Replace {{verify-user}} with the Snowflake user who runs verification in Step 5.

**Important**  
Recreating the integration can generate a different external ID. If you recreate it, describe it again and replace the final IAM trust policy with the current values.

**Result:** The catalog integration exists and Snowflake is still blocked. Record the `GLUE_AWS_IAM_USER_ARN` and `GLUE_AWS_EXTERNAL_ID` values. You use them in Step 4. Send these values to the HealthLake administrator.

## Step 4: Authorize Snowflake
<a name="integrating-snowflake-step4"></a>

**Persona: HealthLake administrator**

Grant the role access to the named table, and replace the temporary trust policy with the Snowflake identity.

**To authorize Snowflake**

1. Grant the role `DESCRIBE` and `SELECT` on the named table by following [Step 2: Grant Lake Formation permissions](integrating-analytics-getting-started.md#integrating-analytics-getting-started-grant) using the AWS CLI tab with the Named tables option, with `arn:aws:iam::{{111122223333}}:role/snowflake-healthlake-reader` as the principal.

1. Create the final trust policy, and save it as `snowflake-trust-policy.json`. The external ID helps protect against the confused deputy problem.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "{{glue-aws-iam-user-arn}}"
         },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "sts:ExternalId": "{{glue-aws-external-id}}"
           }
         }
       }
     ]
   }
   ```

   Replace {{glue-aws-iam-user-arn}} and {{glue-aws-external-id}} with the values from [Step 3: Create the catalog integration](#integrating-snowflake-step3).

1. Apply the final trust policy.

   ```bash
   aws iam update-assume-role-policy \
       --role-name snowflake-healthlake-reader \
       --policy-document file://snowflake-trust-policy.json
   ```

1. Verify that only the Snowflake principal and external ID appear, and that the bootstrap principal is gone.

   ```bash
   aws iam get-role \
       --role-name snowflake-healthlake-reader \
       --query Role.AssumeRolePolicyDocument \
       --output json
   ```

**Result:** The role grants access to the named table and trusts only the Snowflake identity. Tell the Snowflake administrator that the role is ready.

## Step 5: Create the table and run a test query
<a name="integrating-snowflake-step5"></a>

**Persona: Snowflake administrator**

Verify the integration, create the catalog-backed table, and query it. IAM changes can take several seconds to propagate.

**To create the table and run a test query**

1. Verify the catalog integration.

   ```SQL
   USE ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
   USE WAREHOUSE {{warehouse-name}};
   SELECT SYSTEM$VERIFY_CATALOG_INTEGRATION('HEALTHLAKE_CATALOG');
   ```

   Continue only when the returned result reports `success` as `true`.

1. Create the catalog-backed Iceberg table in the existing database and schema.

   ```SQL
   USE DATABASE {{snowflake-database}};
   USE SCHEMA {{snowflake-database}}.{{snowflake-schema}};
   
   CREATE ICEBERG TABLE {{snowflake-database}}.{{snowflake-schema}}.PATIENT
     CATALOG = 'HEALTHLAKE_CATALOG'
     CATALOG_TABLE_NAME = '{{table-name}}'
     AUTO_REFRESH = TRUE;
   ```

1. (Optional) If a separate role runs verification, grant it `SELECT` on the table.

   ```SQL
   GRANT SELECT ON TABLE {{snowflake-database}}.{{snowflake-schema}}.PATIENT TO ROLE HEALTHLAKE_SNOWFLAKE_VERIFY;
   ```

1. Query a limited set of columns and rows.

   ```SQL
   SELECT id, gender, birthdate
   FROM {{snowflake-database}}.{{snowflake-schema}}.PATIENT
   LIMIT 10;
   ```

1. Confirm the integration, table, and grants.

   ```SQL
   SHOW INTEGRATIONS LIKE 'HEALTHLAKE_CATALOG';
   SHOW ICEBERG TABLES LIKE 'PATIENT' IN SCHEMA {{snowflake-database}}.{{snowflake-schema}};
   SHOW GRANTS ON TABLE {{snowflake-database}}.{{snowflake-schema}}.PATIENT;
   ```

   The row count includes every version of each resource, so it's higher than the number of current records. For more information, see [Resource versions](integrating-analytics.md#integrating-analytics-tables-versions).

**Result:** The query returns patient records from the HealthLake table through the authorized catalog path.

## Testing revocation (optional)
<a name="integrating-snowflake-revocation"></a>

**Persona: HealthLake and Snowflake administrators**

Test revocation only after issued credentials and sessions have expired. For why that wait is necessary, see [Revoking access](integrating-analytics-getting-started.md#integrating-analytics-granting-revoke).

**To test revocation**

1. Record the role's maximum session duration.

   ```bash
   aws iam get-role \
       --role-name snowflake-healthlake-reader \
       --query Role.MaxSessionDuration \
       --output text
   ```

1. Revoke `SELECT` on the named table by following [Revoking access](integrating-analytics-getting-started.md#integrating-analytics-granting-revoke), with the role ARN as the principal.

1. Disable result reuse for the Snowflake session.

   ```SQL
   ALTER SESSION SET USE_CACHED_RESULT = FALSE;
   ```

1. Wait until all credentials issued before the revoke have expired. Use the provider-supplied expiration when present. If none was supplied, wait at least 60 minutes after the last credential was received. Also wait until any AWS STS role session that existed before the change has expired, using the maximum session duration as the upper bound from its issue time.

1. Run a fresh query. Expect it to fail with an authorization or table-access error, because Lake Formation can't issue new credentials for `SELECT`.

   ```SQL
   SELECT id, gender, birthdate
   FROM {{snowflake-database}}.{{snowflake-schema}}.PATIENT
   LIMIT 10;
   ```

1. Restore result reuse, even when the expected query fails.

   ```SQL
   ALTER SESSION SET USE_CACHED_RESULT = TRUE;
   ```

1. If you aren't going on to remove the integration, re-grant `SELECT` on the named table by following [Step 2: Grant Lake Formation permissions](integrating-analytics-getting-started.md#integrating-analytics-getting-started-grant) using the AWS CLI tab with the Named tables option.

**Result:** The fresh query fails after both lifetimes expire, which confirms that revocation is effective.

## Removing the integration
<a name="integrating-snowflake-removing"></a>

To remove the integration, reverse the setup steps. Remove the Snowflake reference before you remove the AWS authorization.

**Persona: Snowflake administrator**

**To remove the Snowflake components**
+ Drop the table and the catalog integration.

  ```SQL
  USE ROLE HEALTHLAKE_SNOWFLAKE_SETUP;
  DROP TABLE IF EXISTS {{snowflake-database}}.{{snowflake-schema}}.PATIENT;
  DROP CATALOG INTEGRATION IF EXISTS HEALTHLAKE_CATALOG;
  ```

**Persona: HealthLake administrator**

**To remove the AWS resources**

1. Revoke the grants on the role by following [Revoking access](integrating-analytics-getting-started.md#integrating-analytics-granting-revoke).

1. Delete the inline policy and the role.

   ```bash
   aws iam delete-role-policy \
       --role-name snowflake-healthlake-reader \
       --policy-name snowflake-healthlake-read
   
   aws iam delete-role --role-name snowflake-healthlake-reader
   ```

1. Confirm that the role is absent. Accept only a `NoSuchEntity` response as proof of absence.

   ```bash
   aws iam get-role --role-name snowflake-healthlake-reader
   ```

1. (Optional) If no other engine depends on it, turn off full table access by following [Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)](integrating-analytics-getting-started.md#integrating-analytics-full-table-access) with the value set to `false`.

The HealthLake data store and its tables remain. Cleanup removes only the Snowflake reference and the authorization resources that this procedure created.