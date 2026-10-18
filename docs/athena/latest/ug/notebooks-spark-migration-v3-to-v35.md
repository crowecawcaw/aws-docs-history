

# Migrating to Amazon Athena Apache Spark version 3.5
<a name="notebooks-spark-migration-v3-to-v35"></a>

Amazon Athena for Apache Spark has two release versions: PySpark engine version 3 (the earlier version) and Apache Spark version 3.5 (the current version). This guide helps you migrate from PySpark engine version 3 to Apache Spark version 3.5.

Amazon Athena for Apache Spark release version PySpark engine version 3 reaches end of life on April 1, 2027. After that date, you can no longer create PySpark engine version 3 workgroups, and existing PySpark engine version 3 workgroups can no longer run sessions or calculations. Additionally, there are benefits to migrating to Apache Spark version 3.5. For more information, see [Release versions](notebooks-spark-release-versions.md).

This guide walks you through moving your PySpark engine version 3 notebooks to Apache Spark version 3.5 and using Amazon SageMaker Unified Studio Data Agent to assist with migration.

You migrate in two phases:
+ **Onboard Athena notebooks to SageMaker Unified Studio** – A CLI migration script exports your Athena notebooks attached to the PySpark engine version 3 workgroups and imports them into your SageMaker Unified Studio project.
+ **Upgrade the notebooks** – Once imported, you prompt the SageMaker Unified Studio Data Agent to upgrade each notebook to Amazon Athena for Apache Spark 3.5 and to fix any compatibility issues.

SageMaker Unified Studio brings data preparation, analytics, and machine learning into a single governed experience. Amazon Apache Spark version 3.5 is the default Spark runtime and is automatically available in SageMaker Unified Studio notebooks. You can migrate Apache Spark (PySpark) notebooks running in Amazon Athena Spark workgroups (PySpark engine version 3) to SageMaker Unified Studio projects. Migrating preserves your work while unlocking the latest Spark capabilities, integrated AI assistance, and project-level governance.

**Note**  
You might also see PySpark engine version 3 referred to as Amazon Athena PySpark engine version 3 or Athena Spark version 3. The Athena console and API show it as PySpark engine version 3, and this guide uses that name throughout.

## Prerequisites
<a name="notebooks-spark-migration-prerequisites"></a>

Before proceeding with the migration, ensure you have:
+ An understanding of Amazon SageMaker Unified Studio. For more information, see [What is Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html).
+ A SageMaker Unified Studio domain and project created and ready. See [Set up your domain as an administrator](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/gs-admin-setup.html).
**Note**  
You need both the domain ID and project ID as required inputs to the [Athena notebook migration script](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena-notebook-migration) on the GitHub website. Find the domain ID and project ID on the **Project Overview** page. See [View project details](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/view-project-details.html).
+ An understanding of the potential cost differences:
  + [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/) for costs per domain and project.
  + [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/) for initial executors.
+ One or more Athena Spark (PySpark engine version 3) enabled workgroups with notebooks you intend to migrate.
+ Python 3.10 or later. The migration script is built with Python 3.10\+ features for AWS API calls.
+ AWS CLI configured.

### Timeline
<a name="notebooks-spark-migration-timeline"></a>


| When | What happens | What you should do | 
| --- | --- | --- | 
| Now | Apache Spark version 3.5 is available. PySpark engine version 3 continues to work as it does today. | Plan your migration and test on Apache Spark version 3.5. | 
| Before April 1, 2027 | Both release versions are available. | Migrate, validate, and cut over. | 
| April 1, 2027 | PySpark engine version 3 reaches end of life. Its workgroups can no longer run sessions or calculations. | Finish migrating before this date. | 
| After April 1, 2027 | Your notebooks remain available for you to export or migrate. | Migrate or export any remaining notebooks. | 

## Migrate
<a name="notebooks-spark-migration-migrate"></a>

### Step 1: Find PySpark engine version 3 workgroups
<a name="notebooks-spark-migration-step-1"></a>

If you have Athena workgroups that use the PySpark engine version 3 release version, you must migrate them.
+ **AWS Health Dashboard** – Open the [planned lifecycle event](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html) for this change and choose the **Affected resources** tab. A workgroup drops off the list within 24 hours after you delete it.
+ **AWS CLI** – Run the following command in each Region where you use Athena for Apache Spark to find affected resources:

  ```
  aws athena list-work-groups --region <region> \
    --query "WorkGroups[?EngineVersion.EffectiveEngineVersion=='PySpark engine version 3'].Name" \
    --output text
  ```

### Step 2: Prepare the target environment
<a name="notebooks-spark-migration-step-2"></a>

For notebooks, set up SageMaker Unified Studio:

1. Create a SageMaker Unified Studio domain and project in a Region that supports Apache Spark version 3.5. See [Set up your domain as an administrator](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/gs-admin-setup.html).

1. Record the domain ID and project ID. Both appear on the project overview page.

1. Creating a project automatically creates an Athena workgroup and an execution role, with Athena Spark (Apache Spark version 3.5) as the default connection. Migrated notebooks run under that execution role.

1. Decide how to group notebooks across projects, for example one project per team or per source workgroup. Be aware of SageMaker Unified Studio [Project limits](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/quotas.html).

**Important**  
Give the new execution role access to your data before you migrate. The migration does not copy IAM permissions, Amazon Simple Storage Service (Amazon S3) bucket policies, AWS Key Management Service (AWS KMS) key policies, or AWS Lake Formation grants.

### Step 3: Grant the project execution role access to your data
<a name="notebooks-spark-migration-step-3-grant-access"></a>

Compare the SageMaker Unified Studio project execution role with your existing Athena Spark workgroup execution role, and add any missing data-access permissions before you migrate.

1. Verify that the SageMaker Unified Studio project execution role has the same data-access permissions (Amazon S3, AWS Glue, and Lake Formation) as the execution role on your Athena Spark (PySpark engine version 3) workgroups. The migration script does not copy or grant these permissions.

1. Find your Athena Spark (PySpark engine version 3) workgroup execution role and its policies:

   ```
   aws athena get-work-group --work-group <your-original-athena-workgroup> --region <region> \
     --query 'WorkGroup.Configuration.ExecutionRole' --output text
   
   aws iam list-attached-role-policies --role-name <original-role-name>
   aws iam list-role-policies --role-name <original-role-name>
   ```

1. Find your SageMaker Unified Studio project's execution role. List the project's environments, then get the environment to find its execution role. The execution role ARN appears among the environment's provisioned resources (you can also find it on the project's details page in the SageMaker Unified Studio console).

   ```
   aws datazone list-environments --domain-identifier <domain-id> \
     --project-identifier <project-id> --region <region>
   
   aws datazone get-environment --domain-identifier <domain-id> \
     --identifier <environment-id> --region <region>
   ```

1. List the policies attached to the SageMaker Unified Studio project execution role, using the role name from the ARN that you found:

   ```
   aws iam list-attached-role-policies --role-name <smus-project-role-name>
   aws iam list-role-policies --role-name <smus-project-role-name>
   ```

1. Compare the two roles and add any missing data-access permissions to the SageMaker Unified Studio project execution role.

**Warning**  
If the new role is missing access, notebooks still import, but cells fail with access-denied errors when they run, for example from the AWS Glue Data Catalog, Amazon S3, AWS KMS, Lake Formation, or other services your code uses.

### Step 4: Onboard notebooks to SageMaker Unified Studio
<a name="notebooks-spark-migration-step-4"></a>

The Athena notebook migration script copies notebooks from your PySpark engine version 3 workgroups into SageMaker Unified Studio projects. For each notebook, it:

1. Exports the notebook from Athena. The source notebook is never modified.

1. Clears cell outputs, converts `%%sql` cells to `spark.sql(...)`, and adds a banner cell with migration details and a suggested Data Agent prompt.

1. Imports the notebook into your project.

**Get the script.** Download it from the [Athena notebook migration script](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena-notebook-migration) on the GitHub website. The script's README lists the supported Python and AWS SDK versions, the IAM policy the script needs, and all of its options. Check the README before each migration, because the script is updated over time. The following are sample commands:

**Check Inventory.** List workgroups and notebooks. This pass is read-only.

```
python3 athena_notebook_migration.py --inventory --region <region>
```

**Dry run (single workgroup).** The dry run validates migration scope and destination on a single workgroup without modifying anything.

```
python3 athena_notebook_migration.py \
  --region <region> --domain-id <domain-id> --project-id <project-id> \
  --workgroups <workgroup-name> --dry-run
```

**Migrate one workgroup at a time.** Imports all PySpark engine version 3 notebooks in the supplied workgroup into the SageMaker Unified Studio domain and project.

```
python3 athena_notebook_migration.py \
  --region <region> --domain-id <domain-id> --project-id <project-id> \
  --workgroups <workgroup-name>
```

**Migrate all workgroups.** Imports all PySpark engine version 3 notebooks in every workgroup into the SageMaker Unified Studio domain and project.

```
python3 athena_notebook_migration.py \
  --region <region> --domain-id <domain-id> --project-id <project-id> \
  --all-workgroups
```

The script prints a summary and generates a report. The report lists each notebook with its result and new notebook ID, and you can use it to resume an interrupted run. To confirm the migration, open the project in SageMaker Unified Studio and check that the notebooks are imported under the **Notebooks** section in the project.

Note the following:
+ Cell outputs aren't migrated. Rerun the notebook to regenerate them.
+ Imports are subject to SageMaker Unified Studio notebook size, cell, and per-project limits. See [Quotas for SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/quotas.html). If a project reaches its quota, send the remaining notebooks to another project.
+ If two workgroups contain notebooks with the same name, migrate them into different projects.
+ To undo a migration, delete the imported notebooks in SageMaker Unified Studio. Your Athena notebooks are unchanged.

### Step 5: Update notebook code using SageMaker Unified Studio Data Agent
<a name="notebooks-spark-migration-step-5"></a>

Migrated notebooks contain your original code. Use the SageMaker Unified Studio Data Agent to update each notebook for Apache Spark version 3.5.

1. Open a migrated notebook. Its default compute is the project's Athena Spark connection. A session starts when you run the first cell, and session compute charges apply from then on.

1. Ask the SageMaker Unified Studio Data Agent to [upgrade the notebook](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-agent-basic-usage.html). The banner cell at the top of the notebook contains a suggested prompt.

1. Review the proposed changes. The Data Agent doesn't run anything until you choose to. Typical changes include:
   + Replacing Athena magic commands.
   + Fixing Spark and Python library incompatibilities.
   + Installing libraries that are no longer preinstalled.
   + A summary cell that lists the changes and anything you should review.

1. Accept, run, or reject each change. If a cell still fails, ask the Data Agent again or use **Fix with AI** on the cell.

1. Move any custom JARs, packages, or Python files to Spark properties (`spark.jars`, `spark.jars.packages`, `spark.submit.pyFiles`) on the project's Athena Spark connection. Rebuild JARs for the new runtime if needed.

For details, see [Using the Data Agent](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-agent-getting-started.html).

## Optional steps
<a name="notebooks-spark-migration-optional-steps"></a>

The following steps are optional. Complete them if they apply to your migration.

### Move applications from calculations to Spark Connect
<a name="notebooks-spark-migration-calculations-to-spark-connect"></a>

If your applications or scripts call `StartCalculationExecution` to submit code blocks, move that code to Spark Connect, because the Calculation APIs aren't supported on Apache Spark version 3.5. Run the same code over Spark Connect instead. You can also connect your own notebook client or IDE this way. For current connection details, see [Spark Connect support](notebooks-spark-connect.md).

### Create a workgroup with the Apache Spark 3.5 engine
<a name="notebooks-spark-migration-workgroup-definitions"></a>

If you define workgroups or sessions in the API, CloudFormation, AWS CDK, or Terraform, update them as follows:


| Setting | PySpark engine version 3 | Apache Spark version 3.5 | 
| --- | --- | --- | 
| `EngineVersion.SelectedEngineVersion` | PySpark engine version 3 | Apache Spark version 3.5 | 
| Spark properties | `EngineConfiguration.SparkProperties` | `EngineConfiguration.Classifications`, using `spark-defaults` | 
| Coordinator and executor DPU sizes | Configurable | Remove. Tune with `spark.dynamicAllocation.*` properties. | 
| Query result location (`ResultConfiguration`) | Required | Remove | 
| Execution role | Required | Required. Athena checks at creation that it can assume the role. | 
| Logging | Not configurable | Optional. Set with `MonitoringConfiguration`. | 

**Important**  
Because you can't upgrade a workgroup in place, define the Apache Spark version 3.5 workgroup as a new resource alongside the existing one. Remove the old one only after cutover.

```
aws athena create-work-group \
  --region <region> \
  --name <workgroup-name> \
  --configuration '{
    "EngineVersion": { "SelectedEngineVersion": "Apache Spark version 3.5" },
    "ExecutionRole": "arn:aws:iam::<account-id>:role/<execution-role>",
    "EngineConfiguration": {
      "Classifications": [{
        "Name": "spark-defaults",
        "Properties": { "spark.dynamicAllocation.maxExecutors": "<max-executors>" }
      }]
    }
  }'
```

For current settings and defaults, see [Use Spark properties to specify custom configuration](notebooks-spark-custom-jar-cfg.md).

### Clean up
<a name="notebooks-spark-migration-clean-up"></a>

After cutover is stable:

1. Export any notebooks you want to keep outside SageMaker Unified Studio. In the Athena console, open the notebook explorer and choose **Export file**.
**Warning**  
Deleting a workgroup deletes its notebooks.

1. Delete your PySpark engine version 3 workgroups. Deleted workgroups drop off the AWS Health Dashboard **Affected resources** list.

   ```
   aws athena delete-work-group --work-group <v3-workgroup> --region <region> --recursive-delete-option
   ```

1. Delete the migration script's staged files from the project's Amazon S3 location. The README shows where they are. Don't delete the project bucket itself.

1. Remove unused infrastructure-as-code definitions and IAM permissions, such as permissions for the Calculation APIs.

## Troubleshooting
<a name="notebooks-spark-migration-troubleshooting"></a>

Use the following information to diagnose and fix issues that you might encounter when you migrate notebooks to SageMaker Unified Studio and run them on Apache Spark version 3.5.

### IllegalArgumentException: Unsupported format in USING
<a name="notebooks-spark-migration-troubleshooting-delta-hudi-formats"></a>

In SageMaker Unified Studio, `CREATE TABLE ... USING DELTA` fails with `IllegalArgumentException: Unsupported format in USING: DELTA`, and a Hudi `UPDATE` fails with `UPDATE TABLE is not supported temporarily`, even though the same notebooks run on the Athena console.

This occurs because the SageMaker Unified Studio Spark session registers an Iceberg catalog and SQL extension by default, so non-Iceberg formats have no catalog or extension. You can't reconfigure the session afterward, because the `%%configure` magic isn't available on Athena Spark compute.

To resolve the error, set the catalog and extension for your table format when the session starts:

1. Run `sparkutils.init(...)` in the first cell of the notebook, before you run any other cell. The session starts on the first cell you run.

1. Use one table format per session.

1. If a session has already started with the wrong configuration, restart the kernel (or start a new session), then run the `init()` cell first.

For Iceberg (the default):

```
from sagemaker_studio import sparkutils
spark = sparkutils.init(spark_conf={
    "spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
    "spark.sql.catalog.spark_catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
    "spark.sql.catalog.spark_catalog.io-impl": "org.apache.iceberg.aws.s3.S3FileIO",
    "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
})
```

For Delta:

```
from sagemaker_studio import sparkutils
spark = sparkutils.init(spark_conf={
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
})
```

For Hudi:

```
from sagemaker_studio import sparkutils
spark = sparkutils.init(spark_conf={
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
    "spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension",
})
```

To confirm the configuration, check that `spark.conf.get("spark.sql.catalog.spark_catalog")` and `spark.conf.get("spark.sql.extensions")` return the Delta or Hudi values. A Hudi `UPDATE` on an existing table can still be blocked — see [HoodieUpgradeDowngradeException: Please upgrade table from version FIVE to 6](#notebooks-spark-migration-troubleshooting-hudi-table-version).

### HoodieUpgradeDowngradeException: Please upgrade table from version FIVE to 6
<a name="notebooks-spark-migration-troubleshooting-hudi-table-version"></a>

A Hudi write or `UPDATE` in SageMaker Unified Studio fails with the following error:

```
org.apache.hudi.exception.HoodieUpgradeDowngradeException:
  Please upgrade table from version FIVE to 6 before upgrading to version EIGHT.
```

This error occurs when the table was created in Athena for Spark (PySpark engine version 3), which runs Hudi 0.12 and writes on-disk table version 5. If you then write to it from a SageMaker Unified Studio engine, which runs Hudi 1.0 (table version 8), the version mismatch triggers the error. Hudi upgrades a table one version at a time and refuses the v5-to-v8 jump, so you must first upgrade the table to v6. The following table shows the Hudi release for each table version.


| Hudi release | Table version | 
| --- | --- | 
| 0.12 (Athena PySpark engine version 3) | v5 | 
| 0.14 / 0.15 (AWS Glue 5.0 / Amazon EMR 6.15) | v6 | 
| 1.0 (all SageMaker Unified Studio engines) | v8 | 

To resolve the error, upgrade the table to v6 in the SageMaker Unified Studio session with the `upgrade_table` stored procedure, then rerun your write. Do the following in the SageMaker Unified Studio session:

1. Start a Hudi-configured session. Set `spark.sql.parquet.enableVectorizedReader` to `false` so that the session can read the v5 table (otherwise the read throws `ClassCastException: OnHeapColumnVector cannot be cast to ConstantColumnVector`).

   ```
   from sagemaker_studio import sparkutils
   spark = sparkutils.init(spark_conf={
       "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.hudi.catalog.HoodieCatalog",
       "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
       "spark.sql.extensions": "org.apache.spark.sql.hudi.HoodieSparkSessionExtension",
       "spark.sql.parquet.enableVectorizedReader": "false",
   })
   ```

1. Upgrade the table to v6:

   ```
   spark.sql("CALL upgrade_table(table => 'hudidb.noaa_hudi', to_version => 'SIX')").show()
   # result: true   (v5 -> v6)
   ```

1. Run your write. The Hudi 1.0 engine auto-steps the table from v6 to v8 and applies the update:

   ```
   spark.sql("UPDATE hudidb.noaa_hudi SET name='Sea-Tac' WHERE name='SEATTLE TACOMA AIRPORT, WA US'")
   ```

To confirm the upgrade, check that `hoodie.properties` shows `hoodie.table.version=8` and `hoodie.table.initial.version=6`, and that a `SELECT` returns the updated rows.

Note the following before you upgrade a table:
+ After the upgrade, the table is v8 and the native Hudi reader in Athena SQL (v6) can no longer read it. To keep Athena SQL readability, stay at v6: set `hoodie.write.table.version=6` and `hoodie.write.auto.upgrade=false` before writing so the `UPDATE` doesn't bump the table to v8.
+ The `upgrade_table` procedure changes table metadata and is effectively one-way (a `downgrade_table` counterpart exists; use it with care). For important tables, back up the Amazon S3 prefix and stop all writers during the upgrade.

### InvalidRequestException: The EngineConfiguration exceeds the maximum allowed limit of 5000 characters
<a name="notebooks-spark-migration-troubleshooting-engine-config-limit"></a>

Running a PySpark cell in SageMaker Unified Studio fails with the following error:

```
InvalidRequestException: An error occurred (InvalidRequestException) when calling the
StartSession operation: The EngineConfiguration passed in the StartSession request exceeds
the maximum allowed limit of 5000 characters.
```

This error occurs because SageMaker Unified Studio builds the Spark properties that it sends to the Athena `StartSession` operation. SageMaker Unified Studio adds about seven properties for every AWS Glue or Amazon S3 Tables catalog in the account. In accounts with many catalogs, the serialized properties exceed the 5,000-character `EngineConfiguration` limit and `StartSession` is rejected. To resolve the error, reduce the number of catalogs until the properties fit within the limit:

1. Run the following diagnostic script in a Python cell to check the size of the generated properties and see how much each catalog adds. The script doesn't start a Spark session, so it works even when `StartSession` is failing.

   ```
   # Inspect the Spark properties SMUS sends to Athena StartSession
   from sagemaker_studio.utils.spark.session.athena.athena_spark_session_manager import build_spark_configs
   from collections import defaultdict
   import boto3
   
   LIMIT = 5000
   
   # Account ID of the current credentials (no need to hard-code it)
   account_id = boto3.client("sts").get_caller_identity()["Account"]
   
   # Connection configs. Left empty here to show what SMUS adds by default.
   connection_configs = {}
   
   # User-provided Spark configs, if any were set on the lazy spark object
   user_configs = {}
   try:
       conf = getattr(spark, "_spark_conf", None)
       if conf:
           user_configs = dict(conf)
           print("User Spark configurations:")
           print("=" * 80)
           for k, v in user_configs.items():
               print(f"{k}: {v}")
       else:
           print("No user Spark configurations set.")
   except NameError:
       print("No 'spark' object in this kernel; using no user configs.")
   
   # Build the properties that would be sent to Athena
   spark_properties = build_spark_configs(
       account_id=account_id,
       connection_configs=connection_configs,
       user_configs=user_configs,
   )
   
   print("\nGenerated Spark properties:")
   print("=" * 80)
   for k, v in sorted(spark_properties.items()):
       print(f"{k}: {v}")
   
   size = len(str(spark_properties))
   print("\n" + "=" * 80)
   print(f"Total number of properties: {len(spark_properties)}")
   print(f"Approximate size when serialized: {size} characters")
   print(f"Within {LIMIT} character limit: {size <= LIMIT}")
   
   # Size added by each catalog (spark.sql.catalog.<name>[.*]), largest first
   per_catalog = defaultdict(int)
   prefix = "spark.sql.catalog."
   for k, v in spark_properties.items():
       if k.startswith(prefix):
           name = k[len(prefix):].split(".")[0]
           per_catalog[name] += len(repr(k)) + len(repr(v)) + 4  # approx. "'k': 'v', "
   
   print("\nApproximate characters per catalog:")
   print("=" * 80)
   for name, chars in sorted(per_catalog.items(), key=lambda x: -x[1]):
       note = "  (default - do not remove)" if name == "spark_catalog" else ""
       print(f"{name:45s} {chars:6d}{note}")
   
   if size > LIMIT:
       print(f"\nOver the limit by ~{size - LIMIT} characters. Remove unused catalogs "
             f"from the list above until the total is under {LIMIT}, then hard-reload the page.")
   ```

1. If the script reports `Within 5000 character limit: False`, remove or deregister catalogs that the project doesn't need, starting with the largest in the per-catalog list. Don't remove `spark_catalog`; it's the default session catalog.

1. Refresh the web browser SageMaker Unified Studio page (or close and reopen the project) so that SageMaker Unified Studio uses the regenerated, smaller configuration. Restarting the kernel alone isn't enough.

1. Run the script again to confirm `Within 5000 character limit: True` before you run a PySpark cell.

### A session doesn't default to the AWS Glue Data Catalog
<a name="notebooks-spark-migration-troubleshooting-default-catalog"></a>

When a session starts in SageMaker Unified Studio, a `CREATE DATABASE` statement (for example, `CREATE DATABASE IF NOT EXISTS sparkblogdb`) can create the database in an unexpected catalog, such as an Amazon S3 Tables catalog, instead of the AWS Glue Data Catalog. Running `spark.sql("SELECT current_catalog()").show()` after the statement returns the name of a registered Amazon S3 Tables catalog (for example, `v3-test`) rather than `spark_catalog`.

This happens because the session's `spark_catalog` is an Iceberg `SparkSessionCatalog` whose AWS Glue settings point at an Amazon S3 Tables catalog rather than the root AWS Glue Data Catalog. In the generated Spark configuration, the catalog's `glue.catalog-arn` includes an `/s3tablescatalog/<name>` suffix and its `warehouse` is an `s3tables` ARN, so statements resolve to Amazon S3 Tables:

```
spark.sql.catalog.spark_catalog.glue.catalog-arn = arn:aws:glue:<region>:<account-id>:catalog/s3tablescatalog/<name>
spark.sql.catalog.spark_catalog.warehouse       = arn:aws:s3tables:<region>:<account-id>:bucket/*
```

To create databases in the root AWS Glue Data Catalog instead, override the catalog configuration at session start with `sparkutils.init` so that it targets the root catalog:
+ Remove the `glue.catalog-arn` setting (or set it without the `/s3tablescatalog/<name>` suffix) so the catalog isn't scoped to an Amazon S3 Tables catalog.
+ Set `glue.id` to the plain account ID (for example, `012345678912`) rather than an `<account-id>:s3tablescatalog/<name>` value.
+ Set `warehouse` to a regular Amazon S3 path (for example, `s3://<your-bucket>/<prefix>/`) instead of an `s3tables` ARN.

```
from sagemaker_studio import sparkutils
spark = sparkutils.init(spark_conf={
    "spark.sql.catalog.spark_catalog": "org.apache.iceberg.spark.SparkSessionCatalog",
    "spark.sql.catalog.spark_catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
    "spark.sql.catalog.spark_catalog.io-impl": "org.apache.iceberg.aws.s3.S3FileIO",
    "spark.sql.catalog.spark_catalog.glue.id": "<account-id>",
    "spark.sql.catalog.spark_catalog.warehouse": "s3://<your-bucket>/<prefix>/",
    "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
})
```

To confirm which catalog and database a session resolves to, run `spark.sql("SELECT current_catalog(), current_database()").show()`.

## Appendix: Changes and what to do
<a name="notebooks-spark-migration-appendix"></a>

Use this list to estimate the work for each workgroup.


| Area | What changes | What to do | 
| --- | --- | --- | 
| Notebooks | Apache Spark version 3.5 doesn't support the Athena console notebook editor or the notebook APIs. | Move notebooks to SageMaker Unified Studio. | 
| Spark magic commands | `%%sql`, `%table`, `%matplot`, `%plotly`, and other Athena magics aren't supported. | Replace them with `spark.sql(...)`, `df.show()`, and standard plotting libraries. The migration script and the SageMaker Unified Studio Data Agent handle most cases. | 
| Calculation APIs | `StartCalculationExecution`, `GetCalculationExecution`, `ListCalculationExecutions`, and related APIs aren't supported. The session APIs continue to work. | Run your code over Spark Connect instead. | 
| Low-level Spark APIs | Spark Connect doesn't support `SparkContext` (`sc`), RDDs, `sc.addPyFile`, broadcast variables, or direct JVM access. | Rewrite that code with the DataFrame or SQL APIs. | 
| Spark properties | Properties move from `EngineConfiguration.SparkProperties` to `EngineConfiguration.Classifications` (the `spark-defaults` classification). You can't add JARs, packages, or Python files from a running session. | Move your properties, and set JARs, packages, and Python files on the workgroup or connection. | 
| Session sizing | Coordinator and executor DPU sizes aren't configurable. Sessions use larger default sizes and scale executors automatically. | Remove DPU size settings. Tune scaling with `spark.dynamicAllocation.*` properties if needed. | 
| Python libraries | The runtime uses newer library versions. Some libraries are no longer preinstalled, and some older APIs were removed, for example in pandas and NumPy. | Install what you need with `%pip install`, and update code that uses removed APIs. | 
| Custom JARs | The runtime uses a newer Java version. | Rebuild JARs for the new runtime, if needed. | 
| Spark behavior | Newer Spark releases changed some defaults. Some queries return different results without an error. | Compare outputs for critical jobs. Use `spark.sql.legacy.*` properties to restore old behavior where needed. See the [Spark SQL migration guide](https://spark.apache.org/docs/latest/sql-migration-guide.html) and the [PySpark migration guide](https://spark.apache.org/docs/latest/api/python/migration_guide/pyspark_upgrade.html). | 
| Permissions | Migrated notebooks run as a different execution role. | Give the new role access to your data before you migrate. | 
| Service Quotas | Apache Spark version 3.5 has its own service quotas and different default session sizes. | Review your quotas in [Service Quotas](service-limits.md) and request increases early. | 
| Costs | Review potential changes in costs. | Measure cost on representative workloads. See [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/) and [Amazon SageMaker pricing](https://aws.amazon.com/sagemaker/pricing/). | 

Your data doesn't move. AWS Glue Data Catalog tables and Amazon S3 data, including Apache Iceberg, Apache Hudi, and Delta Lake tables, remain where they are. Apache Spark version 3.5 reads them with newer library versions.

For current runtime versions and Regions, see [Release versions](notebooks-spark-release-versions.md) and [Considerations and limitations](notebooks-spark-considerations-and-limitations.md).

## Frequently asked questions
<a name="notebooks-spark-migration-faq"></a>

1. **What happens if I don't migrate by April 1, 2027?**

   Your PySpark engine version 3 workgroups can no longer run sessions or calculations, so jobs, notebooks, and applications that depend on them stop working. Your notebooks remain available to export or migrate.

1. **Can I upgrade my existing workgroup instead of creating a new one?**

   No. Use your SageMaker Unified Studio project's workgroup, or create a new Apache Spark version 3.5 workgroup.

1. **Do I have to use SageMaker Unified Studio?**

   No. SageMaker Unified Studio is the recommended home for notebooks and has a migration script. You can instead connect your own notebook client, IDE, or application to an Apache Spark version 3.5 workgroup with Spark Connect.

1. **Can I migrate gradually?**

   Yes. Both release versions run side by side until April 1, 2027. You can migrate one workgroup, team, or notebook at a time.

1. **Can I roll back?**

   Yes, until April 1, 2027. The migration never modifies your Athena notebooks. Keep your PySpark engine version 3 workgroups rather than deleting them until you're confident in the migration.

1. **Does the migration script copy permissions or notebook outputs?**

   No. Give the new execution role access to your data before you migrate. Rerun notebooks to regenerate outputs.

1. **Do I need to move or convert my data?**

   No. Your tables and Amazon S3 data stay where they are. Test reads and writes to Iceberg, Hudi, and Delta Lake tables before you migrate production jobs, especially tables that Athena SQL also reads.

1. **Is Apache Spark version 3.5 available in my Region?**

   It's available in every Region that supports PySpark engine version 3, and in additional Regions. See [Considerations and limitations](notebooks-spark-considerations-and-limitations.md).

1. **Where can I get help?**

   Contact [AWS Support](https://aws.amazon.com/support) or your AWS account team.