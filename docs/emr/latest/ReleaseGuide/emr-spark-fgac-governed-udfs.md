

# Using governed UDFs with Lake Formation fine-grained access control

A *governed UDF* is a user-defined function in the AWS Glue Data Catalog that Lake Formation controls. The function code is in a JAR file in Amazon S3. This JAR file is the *custom code artifact* of the governed UDF. When a Spark job declares a governed UDF, Spark loads its custom code artifact in user space and in system space. Your queries, Lake Formation row-level security (RLS) policies, and multi-dialect views can then call the function.

Three roles work together:
+ The **data lake administrator** creates the governed UDF in the Data Catalog and grants the Lake Formation `EXECUTE` permission on it. For more information, see [Governing user-defined functions](https://docs.aws.amazon.com/lake-formation/latest/dg/governing-user-defined-functions.html) in the *Lake Formation Developer Guide*.
+ On Amazon EMR on EC2, the **cluster administrator** also turns on governed UDFs in the security configuration and lists the approved UDFs. On Amazon EMR on EC2, a step cannot declare governed UDFs until the cluster administrator does this.
+ The **job** declares the governed UDFs that it uses. With fine-grained access control, Spark loads only the declared UDFs.

Where a governed UDF runs depends on what calls it:
+ When your query calls a governed UDF, the UDF runs in user space. It sees only the rows and columns that the runtime role can access.
+ When an RLS policy or a multi-dialect view calls a governed UDF, the UDF runs in system space. It runs on the data before Lake Formation filters it.

A governed UDF that your query calls sees filtered data. A governed UDF that a Lake Formation policy or view calls sees unfiltered data.

The declaration is necessary because the `--jars` option adds a JAR to user space only. System space does not load JARs from `--jars`. The declaration loads the custom code artifact in both spaces. Thus, with the declaration, Hive UDFs work with fine-grained access control, and RLS policies can call your functions. This is the only way to use Hive UDFs with fine-grained access control.

For information about user space and system space, see [How fine-grained access control works in Spark](emr-spark-fgac.md#emr-spark-fgac-how-it-works).

## Supported platforms and releases
<a name="emr-spark-fgac-governed-udfs-availability"></a>

You can use governed UDFs on the following platforms and releases. Governed UDFs work with fine-grained access control and with full table access.


**Governed UDF support**  

| Platform | Releases | 
| --- | --- | 
| EMR Serverless | Amazon EMR 7.14.0 and higher 7.x releases, and emr-spark-8.2.0 and higher | 
| Amazon EMR on EC2 | emr-spark-8.2.0 and higher | 
| AWS Glue ETL | AWS Glue 6.1 and higher | 
| Amazon EMR on EKS | Not supported | 

Amazon EMR 7.14.0 runs Spark 3.5 with Scala 2.12. `emr-spark-8.2.0` and AWS Glue 6.1 run Spark 4 with Scala 2.13 on Java 17.

With full table access (FTA), Spark gets the UDF JAR in one of two ways. If the job declares the governed UDF and the runtime role has `EXECUTE` on it, Lake Formation provides the credentials to read the JAR. If the job does not declare it, Spark loads the UDF as a regular Hive function. Then the runtime role needs Amazon S3 read access to the JAR. That Amazon S3 access lets FTA jobs run the UDF without `EXECUTE`, so grant it only to roles that may run the UDF.

On Amazon EMR on EC2, FTA clusters cannot declare governed UDFs. A governed UDF runs as a regular Hive function, and the runtime role needs Amazon S3 read access to the JAR.

## Supported UDF types
<a name="emr-spark-fgac-governed-udfs-types"></a>

The class that the governed UDF names must be one of these supported types. Spark checks the class when the job starts.
+ Hive UDF (extends `org.apache.hadoop.hive.ql.exec.UDF`)
+ Hive GenericUDF (extends `org.apache.hadoop.hive.ql.udf.generic.GenericUDF`)

Other UDF types are not supported.

A custom code artifact is always a JAR file. Python code cannot be a governed UDF. If a governed UDF points to a Python file, the job fails when it starts. Python UDFs, for example `udf` and `pandas_udf`, do not need a governed UDF. They run in user space and see only filtered data.

Compile the classes for Java 17 or lower. We recommend Java 8 bytecode (`javac --release 8`) for Hive UDFs, because it runs on all supported releases.

## Where you can use governed UDFs
<a name="emr-spark-fgac-governed-udfs-where"></a>

Always call a governed UDF by its database-qualified name, for example `sales_db.mask_name(name)`. Spark does not find a governed UDF by its function name alone.


**Where you can call a governed UDF**  

| Caller | Support and rules | 
| --- | --- | 
| Queries in your job | Supported. The UDF runs in user space on filtered data. | 
| Lake Formation RLS policies | Supported. The UDF runs in system space. Create the governed UDF before you create the policy. In the filter expression, use = and OR. Lake Formation does not accept a function call on the left side of IN. For example, write sales\_db.norm(region) = 'WEST' OR sales\_db.norm(region) = 'EAST'. The job must declare every governed UDF that the policies on the table call. | 
| Multi-dialect views (protected Data Catalog views) | Supported for the Spark dialect, dialect version 1.0. The job must declare every governed UDF that the view calls. | 
| Lake Formation data cells filters | Not supported. Lake Formation does not accept a function call in the row filter expression of a data cells filter. Use an RLS policy instead. | 

## Permissions for governed UDFs
<a name="emr-spark-fgac-governed-udfs-permissions"></a>

The job runtime role needs IAM permissions and Lake Formation permissions. Lake Formation fine-grained access control on Amazon EMR on EC2 requires runtime roles. For more information, see [Prerequisites](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lake-formation.html#prerequisites) in the *Amazon EMR Management Guide*.

Add the following statements to the runtime role policy. Replace the {{placeholder}} values with your own.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LakeFormationGovernedUdfAccess",
      "Effect": "Allow",
      "Action": [
        "lakeformation:GetDataAccess",
        "lakeformation:GetTemporaryGlueFunctionCredentials"
      ],
      "Resource": "*"
    },
    {
      "Sid": "GlueGovernedUdfRead",
      "Effect": "Allow",
      "Action": "glue:GetUserDefinedFunction",
      "Resource": [
        "arn:aws:glue:{{region}}:{{111122223333}}:catalog",
        "arn:aws:glue:{{region}}:{{111122223333}}:database/{{sales_db}}",
        "arn:aws:glue:{{region}}:{{111122223333}}:userDefinedFunction/{{sales_db}}/{{mask_name}}"
      ]
    }
  ]
}
```
+ The runtime role needs `lakeformation:GetTemporaryGlueFunctionCredentials` and `lakeformation:GetDataAccess`. Use `"Resource": "*"` for these actions. Their IAM resource is the Lake Formation catalog, not a AWS Glue resource ARN.
+ The runtime role needs `glue:GetUserDefinedFunction` on the catalog, the database, and each governed UDF.
+ These IAM actions do not give access to a governed UDF. Lake Formation also checks the `EXECUTE` permission on each governed UDF.
+ For a governed UDF, Lake Formation gives read-only credentials only for the `ArtifactLocation` prefix of that UDF. These credentials give access to every JAR file under the prefix. Thus, use one `ArtifactLocation` prefix for each governed UDF.
+ With fine-grained access control, the runtime role does not need Amazon S3 permissions on the custom code artifact. Spark downloads the JAR with temporary credentials from Lake Formation. For full table access, see [Supported platforms and releases](#emr-spark-fgac-governed-udfs-availability).

The data lake administrator grants these Lake Formation permissions:
+ `EXECUTE` on each governed UDF, to the runtime role.
+ `SELECT` on tables, to each governed UDF. When you create a governed UDF, Lake Formation grants the UDF `SELECT` on all tables in its catalog. Every declared UDF needs `SELECT` on each table that the job reads with fine-grained access control. It does not need `SELECT` on tables that the runtime role reads in full. To restrict access, revoke the catalog-wide table `SELECT` from the UDF, and grant `SELECT` on each table. The governed UDF ARN is the principal of these grants. If a grant is missing, the error is `Insufficient Lake Formation permission(s): SELECT on {{table}} for user defined function`. For more information, see [Governing user-defined functions](https://docs.aws.amazon.com/lake-formation/latest/dg/governing-user-defined-functions.html) in the *Lake Formation Developer Guide*.

## Declare governed UDFs in a job
<a name="emr-spark-fgac-governed-udfs-declare"></a>

A job declares governed UDFs as a comma-separated list of governed UDF ARNs. A governed UDF ARN has this format:

```
arn:aws:glue:{{region}}:{{account-id}}:userDefinedFunction/{{database}}/{{function}}
```

Replace these values:
+ {{region}}: the AWS Region of the Data Catalog.
+ {{account-id}}: the ID of the account that owns the Data Catalog.
+ {{database}} and {{function}}: the names of the database and the governed UDF.

Declare only the governed UDFs that the job needs. The job fails when it starts if a declared UDF has an unsupported class, even if the query does not call that UDF.


**How to declare governed UDFs**  

| Platform | Declaration | 
| --- | --- | 
| EMR Serverless | Spark property spark.aws.lakeformation.artifacts, for example in sparkSubmitParameters: --conf spark.aws.lakeformation.artifacts={{udf-arn-1}},{{udf-arn-2}}. A job can declare up to 10 governed UDFs. | 
| Amazon EMR on EC2 | Spark property spark.aws.lakeformation.artifacts in the spark-submit command of the step. The cluster security configuration must also turn on governed UDFs and list each ARN. For more information, see [Using governed UDFs with Lake Formation on Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-governed-udfs.html) in the Amazon EMR Management Guide. | 
| AWS Glue ETL | Job parameter --lakeformation-artifacts with the value {{udf-arn-1}},{{udf-arn-2}}. A job can declare up to 10 governed UDFs. Do not use the Spark property on AWS Glue. Only the job parameter makes the UDFs available in system space. | 

EMR Serverless Spark Connect sessions and Livy sessions can use governed UDFs with the same `spark.aws.lakeformation.artifacts` property. Amazon EMR on EC2 Livy sessions with runtime roles can use governed UDFs with the same property. AWS Glue interactive sessions can use governed UDFs with the same `--lakeformation-artifacts` parameter.

### Cross-account governed UDFs and resource links
<a name="emr-spark-fgac-governed-udfs-declare-cross-account"></a>

Governed UDFs work across accounts and through resource links. Declare the ARN that matches the name that your SQL uses:
+ For `{{producer_db}}.{{fn}}`, declare the ARN in the producer account.
+ For `{{link_db}}.{{fn}}`, declare the resource link ARN in your account.
+ If the job uses both names, declare both ARNs.

On Amazon EMR on EC2, list the same ARNs in `ApprovedUdfArns`.

The runtime role needs `EXECUTE` on the governed UDF in the producer account. The producer account can grant it directly to the runtime role. Or the producer account can grant it to the consumer account with the grant option. Then the data lake administrator of the consumer account grants it again to the runtime role. A grant to the consumer account alone is not sufficient.

A governed UDF of the consumer account that runs on a shared table needs `SELECT` on that table. The consumer account grants this permission.

An RLS policy in the producer account can call a governed UDF of the producer account. The policy works when the job declares that UDF.

## Configure a custom code artifact with fgac-config.yaml
<a name="emr-spark-fgac-governed-udfs-fgac-config"></a>

`fgac-config.yaml` is an optional file in the custom code artifact. It lists the Spark properties and classes that the artifact needs in system space. Most UDFs do not need the file. A JAR without the file is valid.

Add the file when one of these conditions applies:
+ The UDF reads a Spark property that the job sets. System space ignores Spark properties that it does not accept. Executors then do not get the property, also in user space.
+ The UDF sends its own classes between the drivers and the executors, for example its own exception class.

Put the file at `META-INF/fgac-config.yaml` in the JAR. Spark ignores the file at other paths. Spark reads the file only from declared custom code artifacts, and only with fine-grained access control. With full table access, Spark does not read the file.

### Field reference
<a name="emr-spark-fgac-governed-udfs-fgac-config-fields"></a>

All fields are optional. Spark rejects keys that this table does not list.


**fgac-config.yaml fields**  

| Field | Type | Description | 
| --- | --- | --- | 
| version | Integer or string | Schema version. The only valid value is 1. | 
| spark\_configs | Map of string to value | Spark properties that Spark sets for the whole job, in system space and on the user executors. Each key needs a value. | 
| system\_space\_allowed\_configuration.keys | List of strings | Exact names of Spark properties that the job can set and pass to system space. | 
| system\_space\_allowed\_configuration.keys\_common\_prefix | List of strings | Property name prefixes. A prefix matches names that continue after it with a period, at any depth. It does not match the prefix name itself. | 
| system\_space\_allowed\_configuration.keys\_with\_validation | Map of string to list of strings | Property names, each with the values that the job can set. | 
| system\_space\_allowed\_configuration.catalog\_conf | List of strings | Properties of a catalog that the job can set and pass to system space. Write each name with %s in place of the catalog name, for example spark.sql.catalog.%s.cache-enabled. Use %s one time in each name. Spark accepts the property only for a catalog that the job sets to a catalog class that system space accepts, for example org.apache.iceberg.spark.SparkCatalog. | 
| system\_space\_allowed\_configuration.keys\_wildcard | List of strings | Property name patterns. %s matches one or more characters, also periods. The pattern must match the whole name. Only emr-spark-8.2.0 and higher and AWS Glue 6.1 and higher accept this key. Amazon EMR 7.x releases reject it. | 
| driver\_class.allowed | List of strings | Fully qualified names of classes that can pass between the user driver and the system driver. | 
| executor\_class.allowed | List of strings | Fully qualified names of classes that can pass between the executors and system space. | 

Classes that are used only inside your UDF do not need an entry. Add `driver_class` or `executor_class` entries for your classes whose objects cross between Spark processes, for example exception classes that your UDF throws.

When a job declares several custom code artifacts, Spark merges their files. If two declared artifacts set the same `spark_configs` key to different values, the job does not start. The driver log shows `Conflicting spark_configs value for '{{key}}' across approved artifacts: '{{value-1}}' and '{{value-2}}'`. Two artifacts can set the same key to the same value. On the executors, a `spark_configs` value overrides a value that the job sets with `--conf` for the same key.

### Examples
<a name="emr-spark-fgac-governed-udfs-fgac-config-examples"></a>

**Example: Pass a Spark property to the UDF**  
The job sets `--conf spark.example.greeting=hello`, and the UDF reads the property on the executors. Without this file, the UDF does not get the value. The following YAML lets the job pass the property to system space:

```yaml
version: 1
system_space_allowed_configuration:
  keys:
    - spark.example.greeting
```

The following YAML allows `spark.example.a.value` and `spark.example.a.b.value`. It does not allow `spark.example` or `spark.examplex.value`:

```yaml
version: 1
system_space_allowed_configuration:
  keys_common_prefix:
    - spark.example
```

On `emr-spark-8.2.0` and higher and on AWS Glue 6.1 and higher, you can use a pattern. The following YAML allows `spark.example.one.value` and `spark.example.a.b.value`. It does not allow `spark.example.one.other`:

```yaml
version: 1
system_space_allowed_configuration:
  keys_wildcard:
    - spark.example.%s.value
```

**Example: Pass a catalog property**  
The job configures an Iceberg catalog and sets one of its properties:

```bash
--conf spark.sql.catalog.my_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.my_catalog.cache-enabled=false
```

System space does not accept `cache-enabled` by default. The following YAML lets the job pass this property for each catalog that it configures:

```yaml
version: 1
system_space_allowed_configuration:
  catalog_conf:
    - spark.sql.catalog.%s.cache-enabled
```

**Example: Allow the exception class of the UDF**  
The UDF throws `com.example.udf.MaskException`. With the following YAML, system space can read the exception. On AWS Glue ETL, the original message then appears in the error log. User code still gets `Spark FGAC experienced an internal error({{id}})`. Use this YAML:

```yaml
version: 1
executor_class:
  allowed:
    - com.example.udf.MaskException
```

Package the file in the JAR, then check the path:

```bash
jar tf mask-udf-1.0.jar | grep fgac-config
META-INF/fgac-config.yaml
```

If the file is not valid YAML or has an unknown key, the job fails when it starts. The driver log shows `System driver failed to start: Failed to read fgac-config manifest from fgac-system-{{jar-name}}: {{reason}}`. Spark adds the prefix `fgac-system-` to the JAR name.

## Rules for governed UDF code
<a name="emr-spark-fgac-governed-udfs-code-rules"></a>

The rules for your UDF code depend on where the code runs.

**On the system driver**  
The system driver can load the UDF class and create the UDF while it validates plans and view SQL. This also occurs when your query calls the UDF. There, these limits apply to the UDF:
+ It can read files only on the class path, in the Java temporary directory, and in the Java home.
+ It cannot open network connections.

If the UDF does not obey these limits, Spark stops the job. The driver log shows `Permission denied for ("java.io.FilePermission" "{{path}}" "read")`, then `SECURITY ERROR. EXITING JVM.`

**In `evaluate()` on the executors**  
This applies to executors in user space and in system space. There, the UDF can read these items:
+ Resources in its JAR file.
+ Spark properties that `fgac-config.yaml` allows.
+ Values from `spark_configs` in `fgac-config.yaml`.
+ Amazon S3 objects, with the credentials of the job runtime role.

We recommend these practices:
+ Give configuration to the UDF in Spark properties that `fgac-config.yaml` allows, or in `spark_configs`.
+ Put default values in resources in the JAR file. Read them in `evaluate()`, not in the constructor or in `initialize()`.
+ Read external configuration in `evaluate()`, the first time that the UDF needs it. Then keep it in a cache. Do not read it in the constructor or in `initialize()`.

## Considerations and security notes
<a name="emr-spark-fgac-governed-udfs-considerations"></a>
+ A governed UDF that an RLS policy calls runs next to unfiltered rows, with the credentials of the job runtime role. Approve only trusted code. The data lake administrator is responsible for this approval. Review the code and the `fgac-config.yaml` file before you create the governed UDF.
+ The `fgac-config.yaml` file changes what system space accepts for every job that declares the artifact. List exact class names and property names. Prefer `keys` to `keys_common_prefix` and `keys_wildcard`.
+ Only the data lake administrator controls which governed UDFs exist and who can run them. A job submitter cannot add entries to `fgac-config.yaml` through job properties.
+ Give write access to the Amazon S3 location of the custom code artifacts only to the artifact authors. With fine-grained access control, job runtime roles do not need read access to this location. Spark gets the JAR with credentials from Lake Formation. With full table access, a job can run an undeclared governed UDF if the runtime role can read its JAR in Amazon S3. For more information, see [Supported platforms and releases](#emr-spark-fgac-governed-udfs-availability).
+ To change a custom code artifact, upload the new JAR to a new Amazon S3 key. Then update the governed UDF. If you replace the JAR at the same key, jobs fail until you update the governed UDF.
+ The system driver limits file and network access while it loads a governed UDF. For the rules, see [Rules for governed UDF code](#emr-spark-fgac-governed-udfs-code-rules).
+ On Amazon EMR on EC2, the system space logs in the cluster `LogUri` can contain RLS filter expressions and view definitions. Give read access to the `LogUri` location only to cluster administrators.
+ On Amazon EMR on EC2, keep `UdfEnabled` set to `false` until your steps need governed UDFs. List only the ARNs that your steps need.