

# Using governed UDFs with Lake Formation on Amazon EMR on EC2

With `emr-spark-8.2.0` and higher, you can call governed user-defined functions (UDFs) from Spark jobs on clusters with Lake Formation fine-grained access control. A governed UDF is a Data Catalog function that Lake Formation controls. Its code is a JAR file in Amazon S3, the *custom code artifact*. A step cannot declare governed UDFs until two administrators turn them on:
+ The data lake administrator creates the governed UDF and grants `EXECUTE` on it to the job runtime role.
+ The cluster administrator turns on governed UDFs in the security configuration and lists the approved governed UDFs.

Lake Formation fine-grained access control on Amazon EMR on EC2 requires runtime roles. The job runtime role needs the permissions for governed UDFs. For the runtime role setup, see [Prerequisites](emr-lake-formation.md#prerequisites).

This page shows the Amazon EMR on EC2 steps only. For all other information, see [Using governed UDFs with Lake Formation fine-grained access control](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-fgac-governed-udfs.html) in the *Amazon EMR Release Guide*.

## Turn on governed UDFs in the security configuration
<a name="emr-lf-governed-udfs-secconfig"></a>

Add the `CustomArtifactConfiguration` section to the security configuration that you use for Lake Formation.

**Important**  
You cannot change a security configuration, so create a new one. `CustomArtifactConfiguration` requires `LakeFormationConfiguration`, so a security configuration for full table access cannot turn on governed UDFs.

1. Copy the JSON of your current Lake Formation security configuration to a file.

1. Add the `CustomArtifactConfiguration` section, as the following JSON example shows. Replace {{region}}, {{111122223333}}, {{sales\_db}}, and {{mask\_name}} with your values.

   ```json
   "CustomArtifactConfiguration": {
     "UdfEnabled": true,
     "ApprovedUdfArns": [
       "arn:aws:glue:{{region}}:{{111122223333}}:userDefinedFunction/{{sales_db}}/{{mask_name}}"
     ]
   }
   ```

   The following table describes the fields.


**CustomArtifactConfiguration fields**  

<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>UdfEnabled</code></td><td>Set to <code>true</code> to let steps declare governed UDFs. The default is <code>false</code>.</td></tr>
  <tr><td><code>ApprovedUdfArns</code></td><td>The governed UDF ARNs that steps can declare. Use exact <code>userDefinedFunction</code> ARNs. The list can have up to 100 ARNs. Do not include empty or duplicate entries.</td></tr>
</tbody>
</table>


1. Use the AWS CLI to create the security configuration.

   ```bash
   aws emr create-security-configuration \
     --name lf-governed-udfs \
     --security-configuration file://lf-governed-udfs-sec-cfg.json
   ```

1. Launch the cluster with the new security configuration.

## Declare governed UDFs in a step
<a name="emr-lf-governed-udfs-step"></a>

A step must declare each governed UDF that it calls. Amazon EMR compares the declaration with `ApprovedUdfArns`.

1. Set `spark.aws.lakeformation.artifacts` to a comma-separated list of governed UDF ARNs.

1. In your Spark code, call each UDF by its database-qualified name.

1. Use the AWS CLI to add the step, as the following example shows. Replace {{j-XXXXXXXXXXXXX}}, {{region}}, {{111122223333}}, {{JobRuntimeRole}}, {{sales\_db}}, {{mask\_name}}, and {{amzn-s3-demo-bucket}} with your values.

   ```bash
   aws emr add-steps \
     --cluster-id {{j-XXXXXXXXXXXXX}} \
     --execution-role-arn arn:aws:iam::{{111122223333}}:role/{{JobRuntimeRole}} \
     --steps '[{
       "Type": "CUSTOM_JAR",
       "Name": "governed-udf-query",
       "ActionOnFailure": "CONTINUE",
       "Jar": "command-runner.jar",
       "Args": ["spark-submit",
                "--conf", "spark.aws.lakeformation.artifacts=arn:aws:glue:{{region}}:{{111122223333}}:userDefinedFunction/{{sales_db}}/{{mask_name}}",
                "s3://{{amzn-s3-demo-bucket}}/scripts/query.py"]
     }]'
   ```

   The example uses the JSON form of `--steps`. Use this form when you declare more than one ARN, because the shorthand form splits the value at each comma.

Amazon EMR checks the declaration when you call `RunJobFlow` or `AddJobFlowSteps`. If the check fails, Amazon EMR does not create the cluster or the step. The response shows one of these errors:
+ `Lake Formation artifacts were declared, but the cluster's security configuration does not enable custom artifacts (UDFs).` Set `UdfEnabled` to `true`. Amazon EMR also shows this error when the account or the release does not support governed UDFs.
+ `Lake Formation artifact {{arn}} is not in the approved artifact list of the cluster's security configuration.` Add the exact ARN to `ApprovedUdfArns`.

Amazon EMR checks only the ARNs in the step arguments. If you declare governed UDFs in a different way, for example through Livy, the cluster checks the declaration when the Spark driver starts.

## Find governed UDF errors
<a name="emr-lf-governed-udfs-logs"></a>

Errors from system space start and security validation errors appear in the step `stderr` log, in `{{LogUri}}/{{cluster-id}}/steps/{{step-id}}/`. In cluster mode, look in the log of the YARN application master container of your application. The step `FailureDetails` can show only `Unknown Error.` Search the log for these texts:
+ `System driver failed to start:`
+ `SECURITY ERROR. EXITING JVM.`
+ `reason = SparkSecurityValidationException`
+ `Multi Dialect View` and `SQL contains unsupported operations`

Usually the step log is sufficient. When a step shows `Spark FGAC experienced an internal error({{id}})`, give the ID to the cluster administrator. As the cluster administrator, search the system space logs on the core nodes for the ID:

```bash
sudo grep -rl {{id}} /var/log/hadoop-yarn/containers/system
```

Amazon EMR also copies these logs to `{{LogUri}}/{{cluster-id}}/containers/system/`. The copy can take a few minutes. The logs can contain row-level security (RLS) filter expressions and view definitions. Give read access to the `LogUri` location only to cluster administrators.