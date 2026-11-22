

# Troubleshooting governed UDFs

To find the cause of a problem quickly, test the UDF logic first with full table access. Then test the UDF with fine-grained access control. Then find the error text in the logs for your platform, and use the error table.

## Step 1: Test the UDF logic with full table access
<a name="emr-spark-fgac-governed-udfs-troubleshoot-fta"></a>

A full table access (FTA) job runs like a regular Amazon EMR Spark job, without the split into user space and system space. You see all driver and executor logs, including the original exceptions from your UDF. Use a table on which the runtime role has full access, with no row, column, or cell filters. For FTA setup, see the page for your platform:
+ [Lake Formation full table access for EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.html) in the *EMR Serverless User Guide*
+ [Lake Formation full table access for Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html) in the *Amazon EMR Management Guide*
+ [Using AWS Glue with Lake Formation for Full Table Access](https://docs.aws.amazon.com/glue/latest/dg/security-access-control-fta.html) in the *AWS Glue Developer Guide*

1. Start an FTA job that declares the governed UDF. On Amazon EMR on EC2, do not declare it. There, the governed UDF runs as a regular Data Catalog function.

1. On EMR Serverless and Amazon EMR on EC2, set the Data Catalog as the metastore with these properties.

   ```bash
   --conf spark.sql.catalogImplementation=hive
   --conf spark.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
   ```

1. Call the UDF on sample data, and compare the result with the expected result.

An FTA job shows that the class loads and that the UDF logic is correct. An FTA job does not test these items:
+ The `fgac-config.yaml` file. FTA does not read it.
+ The Spark properties and classes that system space accepts.
+ The restrictions on file and network access on the system driver.
+ RLS policies. FTA jobs cannot read tables with RLS policies.

FTA jobs check the `EXECUTE` permission only for declared governed UDFs. For how FTA jobs get the JAR, see [Supported platforms and releases](emr-spark-fgac-governed-udfs.md#emr-spark-fgac-governed-udfs-availability).

## Step 2: Test the UDF with fine-grained access control
<a name="emr-spark-fgac-governed-udfs-troubleshoot-fgac"></a>

1. Call the UDF from a query on a table without RLS policies.

1. If the query works, call the UDF from an RLS policy.

1. If a step fails, find the error text in the logs.

1. Find the error text in the error table, and apply the fix.

## Step 3: Find the error text
<a name="emr-spark-fgac-governed-udfs-troubleshoot-logs"></a>

Errors from system space start and security validation errors appear in logs in your account. For these errors, the job state does not show the cause. Search the driver log of the job for these texts:
+ `System driver failed to start:`
+ `System Driver reported startup failure:` (AWS Glue ETL)
+ `SECURITY ERROR. EXITING JVM.`
+ `reason = SparkSecurityValidationException`
+ `Multi Dialect View` and `SQL contains unsupported operations`


**Where errors appear**  

| Platform | Job state | Driver log with the cause | 
| --- | --- | --- | 
| EMR Serverless | The `stateDetails` field of the job run shows permission and integrity errors.<br />For a security validation error, `stateDetails` shows `Driver was shut down due to a security validation exception.` | SPARK\_DRIVER/stderr.gz in the log location of the job. | 
| AWS Glue ETL | The `StartJobRun` response shows permission errors.<br />The `ErrorMessage` of `GetJobRun` can show `BrokenPipeError: [Errno 32] Broken pipe`. This message does not show the cause. | The CloudWatch log group `/aws-glue/jobs/error`.<br />In FTA jobs, you can ignore `Failed to add s3://{{uri}} ... AccessDeniedException` when the job succeeds. | 
| Amazon EMR on EC2 | The `RunJobFlow` or `AddJobFlowSteps` response shows security configuration errors. Amazon EMR does not create the cluster or the step.<br />For other errors, the step `FailureDetails` can show `Unknown Error.` | The step stderr log in {{LogUri}}/{{cluster-id}}/steps/{{step-id}}/. In cluster mode, use the YARN application master container log (container\_\*\_01\_000001/stdout.gz) of your application. | 

Usually the driver log is sufficient. If you need the system space logs, use the method for your platform:
+ EMR Serverless: See [Debugging jobs and sessions](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable-debugging.html) in the *EMR Serverless User Guide*.
+ AWS Glue ETL: See [Debugging fine-grained access control (FGAC) jobs and sessions](https://docs.aws.amazon.com/glue/latest/dg/debugging-fgac-jobs-sessions.html) in the *AWS Glue Developer Guide*.
+ Amazon EMR on EC2: A cluster administrator can read the system space logs. The step `stderr` shows the system application ID in `spark.system.app.id=application_{{id}}`. The system driver log is on the core node that runs it, in `/var/log/hadoop-yarn/containers/system/{{system-app-id}}/`. Amazon EMR also copies the logs to `{{LogUri}}/{{cluster-id}}/containers/system/`. To find an error ID, search these logs for the ID.

**Tip**  
To get the system space logs while you debug, you can first test with a governed UDF and a catalog in the same account.

## Error reference
<a name="emr-spark-fgac-governed-udfs-troubleshoot-errors"></a>

In this table, {{db}}, {{fn}}, {{class}}, {{arn}}, and {{uri}} stand for your values.


**Governed UDF errors**  

| Error text | Cause | Fix | 
| --- | --- | --- | 
| Artifact UDF '{{db}}.{{fn}}' ({{class}}) could not be registered: the class is not a supported UDF type ... | The class is not a supported type. One such UDF stops the job, even if the query does not call it. | Use a supported type. See [Supported UDF types](emr-spark-fgac-governed-udfs.md#emr-spark-fgac-governed-udfs-types). | 
| Artifact UDF '{{db}}.{{fn}}' ({{class}}) could not be registered: the class could not be loaded as a UDF. | Spark cannot load the class. A common cause is a class file version that is higher than the Java version of the release. The message does not show the version. | Run javap -v on the class, and examine major version. Compile for Java 17 (61) or lower. Check the class name in the governed UDF. | 
| Spark FGAC experienced an internal error({{id}}) while executing this request for some input rows | The UDF threw an exception. Spark does not show the original message to user code. | Run the same input in an FTA job to see the message. Add the exception class to executor\_class.allowed. On AWS Glue ETL, the original message then appears in the error log. | 
| No error. The UDF gets no value for a Spark property, or the default value. | System space does not accept the property, so the executors do not get it. | Add the property to system\_space\_allowed\_configuration.keys in fgac-config.yaml. | 
| System driver failed to start: Failed to read fgac-config manifest from fgac-system-{{jar}}: while parsing a flow sequence (or other YAML parser text) | fgac-config.yaml is not valid YAML. | Check the file with a YAML parser. Rebuild and upload the JAR, then update the governed UDF. | 
| Failed to read fgac-config manifest from fgac-system-{{jar}}: Unrecognized key 'keys\_wildcard' in system\_space\_allowed\_configuration; expected one of [keys\_with\_validation, keys\_common\_prefix, catalog\_conf, keys] | Amazon EMR 7.x releases do not accept keys\_wildcard. | Use keys or keys\_common\_prefix. | 
| In the driver log: Failed to read fgac-config manifest from fgac-system-{{jar}}: Conflicting spark\_configs value for '{{key}}' across approved artifacts: '{{value-1}}' and '{{value-2}}' | Two declared custom code artifacts set the same spark\_configs key to different values. | Set the same value in both files, or remove the key from one file. Rebuild and upload the JAR, then update the governed UDF. | 
| No handler for UDF/UDAF/UDTF '{{class}}': ... SerializationSecurityException: Permission denied for ("java.io.FilePermission" "{{path}}" "read"), then SECURITY ERROR. EXITING JVM. | The system driver loaded the UDF while it validated a plan or view SQL. There, the UDF read a file outside the class path, the temporary directory, and the Java home, or it opened a network connection. | Do not read files or JAR resources, or open network connections, in the UDF constructor or initialize() method. See [Rules for governed UDF code](emr-spark-fgac-governed-udfs.md#emr-spark-fgac-governed-udfs-code-rules). | 
| EMR Serverless: IllegalArgumentException: Cannot parse synthetic types. | The query calls a governed UDF that the job does not declare. | Declare the UDF ARN in spark.aws.lakeformation.artifacts. | 
| Amazon EMR on EC2: java.io.FileNotFoundException: Jar {{uri}} not found, or NullPointerException: Cannot invoke "String.split(String)" because "errorClass" is null | The query calls a governed UDF that the job does not declare. | Declare the UDF ARN in spark.aws.lakeformation.artifacts, and approve it in the security configuration. | 
| AWS Glue: NullPointerException: Cannot invoke "String.split(String)" because "errorClass" is null, or IllegalArgumentException: Cannot parse synthetic types. | The query calls a governed UDF that the --lakeformation-artifacts job parameter does not declare. The second message appears when the job sets only the Spark property. | Declare the UDF ARN in the --lakeformation-artifacts job parameter. | 
| In the driver log: `reason = SparkSecurityValidationException, message = org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table {{table}}. Multi Dialect View {{db}}.{{table}} SQL contains unsupported operations`, then `SECURITY ERROR. EXITING JVM.`<br />In the job state:+ EMR Serverless `stateDetails`: `Driver was shut down due to a security validation exception.`<br />+ Amazon EMR on EC2 step `FailureDetails`: `Unknown Error.`<br />+ AWS Glue `ErrorMessage`: `BrokenPipeError: [Errno 32] Broken pipe` | An RLS policy on the table, or the view, calls a governed UDF that the job does not declare. The message does not name the UDF. The job state does not show the cause. | List the filter expressions of the RLS policies on the table, or the view SQL. Declare every governed UDF that they call. | 
| EMR Serverless: The job execution role or propagated identity is not authorized to run one or more of the declared Lake Formation artifacts. | The runtime role does not have EXECUTE on a declared governed UDF. The message does not name the UDF. | Grant EXECUTE on each declared UDF. | 
| AWS Glue: Lake Formation artifact authorization failed: Insufficient Lake Formation permission(s): Required EXECUTE on UserDefinedFunction: {{fn}} | The runtime role does not have EXECUTE on the governed UDF. | Grant EXECUTE on the UDF. In FTA jobs, the log can say Required DESCRIBE. EXECUTE is sufficient. | 
| EMR Serverless FTA jobs: Insufficient Lake Formation permission(s): Required EXECUTE on UserDefinedFunction: {{fn}}, then Failed to load custom code artifacts on the driver. | The FTA job declares a governed UDF, and the runtime role does not have EXECUTE on it. The job stops before it runs SQL. | Grant EXECUTE on the UDF. | 
| Artifact {{arn}} failed integrity verification: S3 object {{uri}} was modified after it was approved (approved LastModified {{time}}). Have the updated artifact re-approved. | The JAR in Amazon S3 changed after the last create or update of the governed UDF. Spark compares the last-modified time, not the content. An upload of the same file also causes this error. | Update the governed UDF with aws glue update-user-defined-function. Lake Formation then records the new time. | 
| Artifact {{arn}} failed integrity verification (no JAR ResourceUris). | The governed UDF has no JAR resource. For example, it points to a Python file. | Use a JAR. For Python code, use a Python UDF in your job instead. | 
| [UNRESOLVED\_ROUTINE] Cannot resolve function `{{fn}}` | The query calls the UDF without the database name. | Call the UDF as {{db}}.{{fn}}. | 
| `Artifact {{arn}} failed integrity verification (jar file name collides with a different artifact: ... Approved artifact jars must have distinct file names.)` in the driver log<br />AWS Glue `ErrorMessage`: `Failed to load custom code artifacts on the driver.` | Two declared governed UDFs have JAR files with the same file name, in different Amazon S3 locations. | Give each JAR a different file name. Upload the renamed JAR, then update the governed UDF. | 
|  + EMR Serverless: `A maximum of 10 Lake Formation artifacts can be declared.`<br />+ Amazon EMR on EC2: `A maximum of 10 Lake Formation artifacts can be declared, but {{n}} were provided.`<br />+ AWS Glue: `Number of Lake Formation artifact ARNs ({{n}}) exceeds the maximum allowed (10).`  | The job declares more than 10 governed UDFs. The service refuses the request before the run starts. | Declare 10 or fewer governed UDFs. | 
| Amazon EMR on EC2: Lake Formation artifact {{arn}} is not in the approved artifact list of the cluster's security configuration. | ApprovedUdfArns does not list the exact ARN. | Add the exact ARN to ApprovedUdfArns. | 