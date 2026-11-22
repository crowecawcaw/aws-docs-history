

# Setting up the Databricks integration

Two administrators set up the integration in four steps. Each step hands values to the next.

![Setup flow across two administrators. The HealthLake administrator prepares Lake Formation (Step 1). The Databricks administrator deploys the OpenSharing server and shares the app identity (Step 2). The HealthLake administrator creates and authorizes the IAM role (Step 3). The Databricks administrator adds the catalogs and runs a test query (Step 4).](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-databricks-setup-flow.png)


## Prerequisites
<a name="integrating-databricks-prerequisites"></a>

Before you begin, make sure that you have the following in AWS:
+ One or more `ACTIVE` HealthLake data stores. HealthLake shares each data store into your account as an AWS Glue resource link whose name ends in `_healthlake_view`, for example `{{data-store-name}}_{{data-store-id}}_healthlake_view`.
+ An IAM user or role that is a data lake administrator in Lake Formation, in the same AWS account and Region as the data store. For more information, see [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin) in the *AWS Lake Formation Developer Guide*.
+ Permission to create an IAM role and an IAM OIDC identity provider, and to grant Lake Formation permissions on the resource links.
+ The AWS CLI (version 2), configured with credentials for the data lake administrator.

In the commands in this topic, replace {{us-east-1}} with the AWS Region of your data store.

You also need the following in Databricks:
+ A Databricks workspace that supports Databricks Apps, where you can create a service principal (the hosting workspace).
+ `CREATE PROVIDER` and `CREATE CATALOG` on the Unity Catalog metastore where you want the catalogs. This can be a different workspace and metastore from the hosting workspace.
+ The Databricks CLI (version 1.17 or later), authenticated to the hosting workspace.

For the full Databricks requirements, see [Prerequisites](https://github.com/databricks-industry-solutions/healthlake-opensharing#prerequisites) on the GitHub website.

## Planning your deployment
<a name="integrating-databricks-planning"></a>

Decide the following before Step 2, because you set them when you deploy the app.

The HealthLake OpenSharing server discovers data stores through the HealthLake API, and new data stores appear within a few minutes. Deploy one app per organization, and list one IAM role per account in its configuration. For all configuration settings, including multi-account setup, see [Configuration](https://github.com/databricks-industry-solutions/healthlake-opensharing#configuration) on the GitHub website.

Choose how data stores map to Unity Catalog with the layout setting.


**Unity Catalog layout options**  

| Layout | Result | Use when | 
| --- | --- | --- | 
| share (recommended) | One catalog per data store | You have many data stores or want to grant and organize each data store independently. Supports up to 1,000 catalogs per metastore. | 
| schema | One catalog, one schema per data store | You have a small number of data stores. Validated to about 5,000 tables (roughly 45 data stores at 108 tables each). | 

In testing, a single app loaded 1,080 tables across 101 data stores without errors or throttling. For hundreds of actively queried data stores, use a Large or larger app compute size. For sizing guidance, see [Scaling](https://github.com/databricks-industry-solutions/healthlake-opensharing#scaling) on the GitHub website.

## Step 1: Prepare HealthLake data
<a name="integrating-databricks-step1"></a>

**Persona: HealthLake administrator**

Identify the resource links that HealthLake created in your account, and turn on full table access so that the OpenSharing server can read the tables through Lake Formation.

Complete [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find) and [Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)](integrating-analytics-getting-started.md#integrating-analytics-full-table-access).

**Result:** Full table access is on, and you have the resource link name, catalog ID, and target database for each data store. Send them to whoever runs Step 3 (usually you).

## Step 2: Deploy the OpenSharing server
<a name="integrating-databricks-step2"></a>

**Persona: Databricks administrator**

Deploy the OpenSharing server as a Databricks App, and create the recipient service principal that Unity Catalog uses to connect to it.

**To deploy the OpenSharing server**

1. Create the recipient service principal. Unity Catalog connects to the server as this principal.

   ```bash
   databricks service-principals create \
       --display-name healthlake-opensharing-recipient -o json
   ```

   Record the `applicationId` from the output.

1. Deploy the app with the Databricks Asset Bundle. Set the AWS Region, the IAM role ARN that you create in [Step 3: Create and authorize the IAM role](#integrating-databricks-step3), the recipient service principal's application ID, and the app name. The role ARN has the form `arn:aws:iam::{{111122223333}}:role/healthlake-opensharing-reader`, where {{111122223333}} is your AWS account ID.

   For the deployment commands and settings, see [Deploy](https://github.com/databricks-industry-solutions/healthlake-opensharing#deploy) on the GitHub website.

1. After the app starts, get its identity from the startup logs.

   ```bash
   databricks apps logs {{app-name}} --tail-lines 500 | grep DATABRICKS_IDENTITY
   # DATABRICKS_IDENTITY {"iss": "https://{{workspace-host}}/oidc", "aud": ["{{workspace-id}}"], "sub": "{{app-client-id}}"}
   ```

   Replace {{app-name}} with the app name from the previous step. The command prints the app identity, which has three values that you use in the IAM trust policy in [Step 3: Create and authorize the IAM role](#integrating-databricks-step3):
   + `iss` is the issuer URL, `https://{{workspace-host}}/oidc`.
   + `aud` is the {{workspace-id}}.
   + `sub` is the {{app-client-id}}.

**Result:** The app is running. Record the `iss`, `aud`, and `sub` values, and send them to the HealthLake administrator for Step 3.

## Step 3: Create and authorize the IAM role
<a name="integrating-databricks-step3"></a>

**Persona: HealthLake administrator**

Create the IAM role that the app assumes, and grant it read access in Lake Formation. Create one role for each AWS account that holds data stores.

**To create the IAM role**

1. Trust the workspace as an OIDC identity provider. Skip this step if the account already has a provider for this workspace. To check whether the provider already exists, run the following command and look for the issuer in the output.

   ```bash
   aws iam list-open-id-connect-providers
   ```

   If the provider doesn't exist, create it.

   ```bash
   aws iam create-open-id-connect-provider \
       --url https://{{issuer}} \
       --client-id-list {{workspace-id}}
   ```

   Replace {{issuer}} with the `iss` value from [Step 2: Deploy the OpenSharing server](#integrating-databricks-step2), without the `https://` prefix.

1. Create a trust policy that allows only this app to assume the role. Save it as `trust-policy.json`.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/{{issuer}}"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "{{issuer}}:sub": "{{app-client-id}}",
             "{{issuer}}:aud": "{{workspace-id}}"
           }
         }
       }
     ]
   }
   ```

1. Create a permissions policy that allows the role to read Data Catalog metadata, request Lake Formation credentials, and list data stores. Save it as `permissions-policy.json`.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "GlueCatalogRead",
         "Effect": "Allow",
         "Action": [
           "glue:GetDatabase",
           "glue:GetDatabases",
           "glue:GetTable",
           "glue:GetTables"
         ],
         "Resource": "*"
       },
       {
         "Sid": "LakeFormationDataAccess",
         "Effect": "Allow",
         "Action": [
           "lakeformation:GetDataAccess",
           "lakeformation:GetTemporaryGlueTableCredentials"
         ],
         "Resource": "*"
       },
       {
         "Sid": "HealthLakeDiscovery",
         "Effect": "Allow",
         "Action": "healthlake:ListFHIRDatastores",
         "Resource": "*"
       }
     ]
   }
   ```

1. Create the role and attach the policy.

   ```bash
   aws iam create-role \
       --role-name healthlake-opensharing-reader \
       --assume-role-policy-document file://trust-policy.json
   
   aws iam put-role-policy \
       --role-name healthlake-opensharing-reader \
       --policy-name healthlake-opensharing \
       --policy-document file://permissions-policy.json
   ```

   If the role already exists, update its trust policy with `aws iam update-assume-role-policy --role-name healthlake-opensharing-reader --policy-document file://trust-policy.json`, and continue.

Grant the role access to every table of each data store by following [Step 2: Grant Lake Formation permissions](integrating-analytics-getting-started.md#integrating-analytics-getting-started-grant). Use the AWS CLI tab and the All tables option, with the role ARN `arn:aws:iam::{{111122223333}}:role/healthlake-opensharing-reader` as the principal.

**Note**  
The role needs both the IAM permissions in its policy and the Lake Formation grants. It has no Amazon S3 permissions, and reads data only through the short-lived credentials that Lake Formation vends for each table. HealthLake service accounts aren't part of your AWS Organizations organization, so don't use organization-based condition keys such as `aws:ResourceOrgID`.

**Result:** The role has the grants for every data store. Tell the Databricks administrator that the role is ready.

## Step 4: Add the catalogs and run a test query
<a name="integrating-databricks-step4"></a>

**Persona: Databricks administrator**

Connect Unity Catalog to the OpenSharing server, grant access to your users, and run a test query.

**To add the catalogs and run a test query**

1. Create a Unity Catalog provider that points to the app, authenticating as the recipient service principal from [Step 2: Deploy the OpenSharing server](#integrating-databricks-step2).

1. Create a catalog from the provider's share for each data store.

   For the commands that create the provider and catalogs, see [Deploy](https://github.com/databricks-industry-solutions/healthlake-opensharing#deploy) on the GitHub website.

1. Grant Unity Catalog permissions on the catalogs to the users and groups that need access. To restrict access to specific rows or columns, create views on the shared tables.

1. Run a test query, such as a row count on the `patient` table.

   ```SQL
   SELECT COUNT(*) FROM {{catalog-name}}.{{schema-name}}.patient;
   ```

   Replace {{catalog-name}} and {{schema-name}} with the Unity Catalog catalog and schema that you created for the data store in the previous steps.

   For catalog and schema names, see [Querying the data](https://github.com/databricks-industry-solutions/healthlake-opensharing#querying-the-data) on the GitHub website.

   The query returns the number of rows in the `patient` table. The count includes every version of each resource, so it matches the same `COUNT(*)` in Amazon Athena, not the number of patients. For the number of current patients, see [Resource versions](integrating-analytics.md#integrating-analytics-tables-versions).

   To validate the results, compare them with the same query in Amazon Athena. For more information, see [Step 3: Run a test query](integrating-athena.md#integrating-athena-query-sql).

**Result:** The test query returns rows. Next, see [Querying the tables](integrating-databricks.md#integrating-databricks-querying).

## Removing the integration
<a name="integrating-databricks-removing"></a>

To remove the integration, reverse the setup steps.

**Persona: Databricks administrator**

**To remove the Databricks components**
+ Delete the catalogs, the provider, the app, and the recipient service principal.

  For the removal commands, see [Uninstall](https://github.com/databricks-industry-solutions/healthlake-opensharing#uninstall) on the GitHub website.

**Persona: HealthLake administrator**

**To remove the AWS resources**

1. Revoke the role's grants on each data store by following [Revoking access](integrating-analytics-getting-started.md#integrating-analytics-granting-revoke), with the role ARN `arn:aws:iam::{{111122223333}}:role/healthlake-opensharing-reader` as the principal.

1. Delete the role policy and the role.

   ```bash
   aws iam delete-role-policy \
       --role-name healthlake-opensharing-reader \
       --policy-name healthlake-opensharing
   
   aws iam delete-role \
       --role-name healthlake-opensharing-reader
   ```

1. If no other role uses it, delete the OIDC identity provider.

   ```bash
   aws iam delete-open-id-connect-provider \
       --open-id-connect-provider-arn arn:aws:iam::{{111122223333}}:oidc-provider/{{issuer}}
   ```

1. (Optional) If no other external engine needs it, turn off full table access, as described in [Step 3: Turn on full table access (Spark on Amazon EMR, Databricks, and Snowflake)](integrating-analytics-getting-started.md#integrating-analytics-full-table-access).