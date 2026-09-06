

# Configuring AWS Glue interactive sessions for Jupyter and AWS Glue Studio notebooks
<a name="interactive-sessions-magics"></a>

## Introduction to Jupyter Magics
<a name="w2aac29c20b3"></a>

 Jupyter Magics are commands that can be run at the beginning of a cell or as a whole cell body. Magics start with `%` for line-magics and `%%` for cell-magics. Line-magics such as `%region` and `%connections` can be run with multiple magics in a cell, or with code included in the cell body like the following example. 

```
%region us-east-2
%connections my_rds_connection
dy_f = glue_context.create_dynamic_frame.from_catalog(database='rds_tables', table_name='sales_table')
```

 Cell magics must use the entire cell and can have the command span multiple lines. An example of `%%sql` is below. 

```
%%sql
select * from rds_tables.sales_table
```

## Magics supported by AWS Glue interactive sessions for Jupyter
<a name="interactive-sessions-supported-magics"></a><a name="interactive-sessions-magics2"></a>

 The following are magics that you can use with AWS Glue interactive sessions for Jupyter notebooks. 

 **Sessions magics** 


| Name | Type | Description | 
| --- | --- | --- | 
|  %help  |  n/a  |  Return a list of descriptions and input types for all magic commands.  | 
| %profile | String | Specify a profile in your AWS configuration to use as the credentials provider. | 
| %region | String | Specify the AWS Region; in which to initialize a session. Default from `~/.aws/configure.`<br />Example: `%region us-west-1` | 
| %idle\_timeout | Int |  The number of minutes of inactivity after which a session will timeout after a cell has been executed. The default idle timeout value for Spark ETL sessions is the default timeout, 2880 minutes (48 hours). For other session types, consult documentation for that session type.<br />Example: `%idle_timeout 3000` | 
| %session\_id | n/a | Return the session ID for the running session.  | 
| %session\_id\_prefix | String |  Define a string that will precede all session IDs in the format **[session\_id\_prefix]-[session\_id].** If a session ID is not provided, a random UUID will be generated. This magic is not supported when you run a Jupyter Notebook in AWS Glue Studio. <br />Example: `%session_id_prefix 001` | 
| %status |  | Return the status of the current AWS Glue session including its duration, configuration and executing user / role.  | 
| %stop\_session  |  | Stop the current session. | 
| %list\_sessions |  | Lists all currently running sessions by name and ID. | 
| %session\_type | String | Sets the session type to one of Streaming, ETL, or Ray. <br />Example: `%session_type Streaming` | 
| %glue\_version | String | The version of AWS Glue to be used by this session. <br />Example: `%glue_version 3.0` | 

 **Magics for selecting job types** 


| Name | Type | Description | 
| --- | --- | --- | 
| %streaming | String | Changes the session type to AWS Glue Streaming. | 
| %etl | String | Changes the session type to AWS Glue ETL. | 
| %glue\_ray | String | Changes the session type to AWS Glue for Ray. See [Magics supported by AWS Glue Ray interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/is-using-ray-configuration).  | 

 **AWS Glue for Spark config magics** 

 The `%%configure` magic is a json-formatted dictionary consisting of all configuration parameters for a session. Each parameter can be specified here or through individual magics. 


| Name | Type | Description | 
| --- | --- | --- | 
|  %%configure  |  Dictionary  |  Specify a JSON-formatted dictionary consisting of all configuration parameters for a session. Each parameter can be specified here or through individual magics. <br /> For a list of parameters and examples on how to use `%%configure`, see [%%configure cell magic arguments](#interactive-sessions-magics-configure-arguments).  | 
| %iam\_role | String |  Specify an IAM role ARN to execute your session with. Default from \~/.aws/configure. <br /> Example: `%iam_role AWSGlueServiceRole`  | 
| %number\_of\_workers | Int | The number of workers of a defined worker\_type that are allocated when a job runs. `worker_type` must be set too. The default `number_of_workers` is 5.<br />Example: `%number_of_workers 2` | 
| %additional\_python\_modules | List | Comma separated list of additional Python modules to include in your cluster (can be from PyPI or S3).<br />Example: `%additional_python_modules pandas, numpy`. | 
| %%tags | String |  Adds tags to a session. Specify the tags within curly brackets { }. Each tag name pair is enclosed in parentheses (" ") and separated by a comma (,). <pre>%%tags<br />{"billing":"Data-Platform", "team":"analytics"}<br />                      </pre><br />Use the `%status` magic to view tags associated with the session.<pre>%status</pre><pre>Session ID: <sessionId><br /> Status: READY<br /> Role: <example-role><br /> CreatedOn: 2023-05-26 11:12:17.056000-07:00<br /> GlueVersion: 3.0<br /> Job Type: glueetl<br /> Tags: {'owner':'example-owner', 'team':'analytics', 'billing':'Data-Platform'}<br /> Worker Type: G.4X<br /> Number of Workers: 5<br /> Region: us-west-2<br /> Applying the following default arguments:<br /> --glue_kernel_version 0.38.0<br /> --enable-glue-datacatalog true<br /> Arguments Passed: ['--glue_kernel_version: 0.38.0', '--enable-glue-datacatalog: true']                <br />                </pre> | 
| %%assume\_role | Dictionary | Specify a json-formatted dictionary or an IAM role ARN string to create a session for cross-account access.<br />Example with ARN:<pre>%%assume_role<br />{<br />  'arn:aws:iam::XXXXXXXXXXXX:role/AWSGlueServiceRole'<br />}<br />                </pre><br />Example with credentials:<pre> %%assume_role<br />{{<br />    "aws_access_key_id" = "XXXXXXXXXXXX",<br />    "aws_secret_access_key" = "XXXXXXXXXXXX",<br />    "aws_session_token" = "XXXXXXXXXXXX"<br />}}</pre> | 

### %%configure cell magic arguments
<a name="interactive-sessions-magics-configure-arguments"></a>

 The `%%configure` magic is a json-formatted dictionary consisting of all configuration parameters for a session. Each parameter can be specified here or through individual magics. See below for examples for arguments supported by the `%%configure` cell magic. Use the `--` prefix for run arguments specified for the job. Example: 

```
%%configure
{
   "--user-jars-first": "true",
   "--enable-glue-datacatalog": "false"
}
```

 For more information on job parameters, see [Job parameters](aws-glue-programming-etl-glue-arguments.md). 

**Session Configuration**


| Parameter | Type | Description | 
| --- | --- | --- | 
| max\_retries | Int | The maximum number of times to retry this job if it fails.<pre>%%configure<br />{<br />  "max_retries": "0"<br />}                      <br />                          </pre> | 
| max\_concurrent\_runs | Int | The maximum number of concurrent runs allowed for a job. Example:<pre>%%configure<br />{<br />  "max_concurrent_runs": "3"<br />}</pre> | 

**Session parameters**


| Parameter | Type | Description | 
| --- | --- | --- | 
| --enable-spark-ui | Boolean | Enable Spark UI to monitor and debug AWS Glue ETL jobs. <pre>%%configure<br />{<br />  "--enable-spark-ui": "true"<br />}</pre> | 
| --spark-event-logs-path | String | Specifies an Amazon S3 path. When using the Spark UI monitoring feature. Example:<pre>%%configure<br />{<br />  "--spark-event-logs-path": "s3://path/to/event/logs/"<br />}                           <br />                          </pre> | 
| --script\_location | String | Specifies the S3 path to a script that executes a job. Example:<pre>%%configure <br />{<br />  "script_location": "s3://new-folder-here"<br />}                            <br />                          </pre> | 
| --SECURITY\_CONFIGURATION | String | The name of a AWS Glue security configuration<br />Example:<pre>%%configure<br />{<br />    "--security_configuration": {{{<br />"encryption_type": "kms",<br />"kms_key_id": "YOUR_KMS_KEY_ARN"<br />}}}<br />}<br />                  </pre> | 
| --job-language | String | The script programming language. Accepts a value of 'scala' or 'python'. Default is 'python'. Example:<pre>%%configure <br />{<br />  "--job-language": "scala"<br />}                            <br />                  </pre> | 
| --class | String | The Scala class that serves as the entry point for your Scala script. Default is null. Example:<pre>%%configure <br />{<br />  "--class": "className"<br />}                            <br />                  </pre> | 
| --user-jars-first | Boolean | Prioritizes the customer's extra JAR files in the classpath. Default is null. Example:<pre>%%configure <br />{<br />  "--user-jars-first": "true"<br />}                            <br />                  </pre> | 
| --use-postgres-driver | Boolean | Prioritizes the Postgres JDBC driver in the class path to avoid a conflict with the Amazon Redshift JDBC driver. Default is null. Example:<pre>%%configure <br />{<br />  "--use-postgres-driver": "true"<br />}                            <br />                  </pre> | 
| --extra-files | List(string) | The Amazon S3 paths to additional files, such as configuration files that AWS Glue copies to the working directory of your script before executing it. Example:<pre>%%configure <br />{<br />  "--extra-files": "s3://path/to/additional/files/"<br />}                            <br />                  </pre> | 
| --job-bookmark-option | String | Controls the behavior of a job bookmark. Accepts a value of 'job-bookmark-enable', 'job-bookmark-disable' or 'job-bookmark-pause'. Default is 'job-bookmark-disable'. Example:<pre>%%configure<br />{<br />  "--job-bookmark-option": "job-bookmark-enable"<br />}                            <br />                  </pre> | 
| --TempDir | String | Specifies an Amazon S3 path to a bucket that can be used as a temporary directory for the job. Default is null. Example:<pre>%%configure <br />{<br />  "--TempDir": "s3://path/to/temp/dir"<br />}                            <br />                  </pre> | 
| --enable-s3-parquet-optimized-committer | Boolean | Enables the EMRFS Amazon S3-optimized committer for writing Parquet data into Amazon S3. Default is 'true'. Example:<pre>%%configure <br />{<br />  "--enable-s3-parquet-optimized-committer": "false"<br />}                            <br />                  </pre> | 
| --enable-rename-algorithm-v2 | Boolean | Sets the EMRFS rename algorithm version to version 2. Default is 'true'. Example:<pre>%%configure <br />{<br />  "--enable-rename-algorithm-v2": "true"<br />}                            <br />                  </pre> | 
| --enable-glue-datacatalog | Boolean | Enables you to use the AWS Glue Data Catalog as an Apache Spark Hive metastore. Example:<pre>%%configure <br />{<br />  "--enable-glue-datacatalog": "true"<br />}                            <br />                  </pre> | 
| --enable-metrics | Boolean | Enables the collection of metrics for job profiling for job run. Default is 'false'. Example:<pre>%%configure <br />{<br />  "--enable-metrics": "true"<br />}                            <br />                  </pre> | 
| --enable-continuous-cloudwatch-log | Boolean | Enables real-time continuous logging for AWS Glue jobs. Default is 'false'. Example:<pre>%%configure <br />{<br />  "--enable-continuous-cloudwatch-log": "true"<br />}                            <br />                  </pre> | 
| --enable-continuous-log-filter | Boolean | Specifies a standard filter or no filter when you create or edit a job enabled for continuous logging. Default is 'true'. Example:<pre>%%configure <br />{<br />  "--enable-continuous-log-filter": "true"<br />}                            <br />                  </pre> | 
| --continuous-log-stream-prefix | String | Specifies a custom Amazon CloudWatch log stream prefix for a job enabled for continuous logging. Default is null. Example:<pre>%%configure <br />{<br />  "--continuous-log-stream-prefix": "prefix"<br />}                            <br />                  </pre> | 
| --continuous-log-conversionPattern | String | Specifies a custom conversion log pattern for a job enabled for continuous logging. Default is null. Example:<pre>%%configure <br />{<br />  "--continuous-log-conversionPattern": "pattern"<br />}                      <br />                  </pre> | 
| --conf | String | Controls Spark config parameters. It is for advanced use cases. Use --conf before each parameter. Example: <pre>%%configure<br />{<br />    "--conf": "spark.hadoop.hive.metastore.glue.catalogid=123456789012 --conf hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory --conf hive.metastore.schema.verification=false"<br />}       <br />        </pre>  | 
| timeout | Int | Determines the maximum amount of time that the Spark session should wait for a statement to complete before terminating it. <pre>%%configure <br />{<br />  "timeout": "30"<br />}</pre>  | 
| auto-scaling | Boolean | Determines whether or not to use auto-scaling. <pre>%%configure <br />{<br />  "––enable-auto-scaling": "true"<br />}</pre>  | 

### Spark jobs (ETL & streaming) magics
<a name="interactive-sessions-magics-spark-jobs"></a>


| Name | Type | Description | 
| --- | --- | --- | 
| %worker\_type | String | Standard, G.1X, G.2X, G.4X, G.8X, G.12X, G.16X, R.1X, R.2X, R.4X, or R.8X. number\_of\_workers must be set too. The default worker\_type is G.1X. | 
| %connections | List | Specify a comma-separated list of connections to use in the session. <br /> Example: <pre>%connections my_rds_connection<br />                    dy_f = glue_context.create_dynamic_frame.from_catalog(database='rds_tables', table_name='sales_table')</pre> | 
| %extra\_py\_files | List | Comma separated list of additional Python files from Amazon S3. | 
| %extra\_jars | List | Comma-separated list of additional jars to include in the cluster. | 
| %spark\_conf | String | Specify custom spark configurations for your session. For example, %spark\_conf spark.serializer=org.apache.spark.serializer.KryoSerializer. | 

### Magics for Ray jobs
<a name="interactive-sessions-magics-ray-jobs"></a>


| Name | Type | Description | 
| --- | --- | --- | 
| %min\_workers | Int |  The minimum number of workers that are allocated to a Ray job. Default: 1.  Example: `%min_workers 2`  | 
| %object\_memory\_head | Int | The percentage of free memory on the instance head node after a warm start. Minimum: 0. Maximum: 100. Example: `%object_memory_head 100` | 
| %object\_memory\_worker | Int | The percentage of free memory on the instance worker nodes after a warm start. Minimum: 0. Maximum: 100. Example: `%object_memory_worker 100` | 

### Action magics
<a name="interactive-sessions-magics-action"></a>


| Name | Type | Description | 
| --- | --- | --- | 
| %%sql | String |  Run SQL code. All lines after the initial `%%sql` magic will be passed as part of the SQL code. <br /> Example: `%%sql select * from rds_tables.sales_table`  | 
| %matplot | Matplotlib figure | Visualize your data using the matplotlib library.<br />Example:<pre>import matplotlib.pyplot as plt<br /><br /># Set X-axis and Y-axis values<br />x = [5, 2, 8, 4, 9]<br />y = [10, 4, 8, 5, 2]<br />  <br /># Create a bar chart <br />plt.bar(x, y)<br />  <br /># Show the plot<br />%matplot plt      <br />                </pre> | 
| %plotly | Plotly figure | Visualize your data using the plotly library.<br />Example:<pre>import plotly.express as px<br />                  <br />#Create a graphical figure<br />fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")<br /><br />#Show the figure<br />%plotly fig</pre> | 

## Naming sessions
<a name="interactive-sessions-naming-sessions"></a>

 AWS Glue interactive sessions are AWS resources and require a name. Names should be unique for each session and may be restricted by your IAM administrators. For more information, see [Interactive sessions with IAM](glue-is-security.md). The Jupyter kernel automatically generates unique session names for you. However sessions can be named manually in two ways: 

1.  Using the AWS Command Line Interface config file located at `~.aws/config`. See [Setting Up AWS Config with the AWS Command Line Interface](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html). 

1.  Using the `%session_id_prefix` magics. See [Magics supported by AWS Glue interactive sessions for Jupyter](#interactive-sessions-supported-magics). 

 A session name is generated as follows: 
+ When the prefix and session\_id are provided: the session name will be {prefix}-{UUID}.
+ When nothing is provided: the session name will be {UUID}.

Prefixing session names allows you to recognize your session when listing it in the AWS CLI or console.

## Specifying an IAM role for interactive sessions
<a name="iam-role-interactive-sessions"></a>

 You must specify an AWS Identity and Access Management (IAM) role to use with AWS Glue ETL code that you run with interactive sessions. 

 The role requires the same IAM permissions as those required to run AWS Glue jobs. See [Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html) for more information on creating a role for AWS Glue jobs and interactive sessions. 

 IAM roles can be specified in two ways: 
+  Using the AWS Command Line Interface config file located at `~.aws/config` (Recommended). For more information, see [ Configuring sessions with \~/.aws/config ](https://docs.aws.amazon.com/glue/latest/ug/interactive-sessions-magics.html#interactive-sessions-named-profiles). 
**Note**  
 When the `%profile` magic is used, the configuration for `glue_iam_role` of that profile is honored. 
+  Using the %iam\_role magic. For more information, see [Magics supported by AWS Glue interactive sessions for Jupyter](#interactive-sessions-supported-magics). 

## Configuring sessions with named profiles
<a name="interactive-sessions-named-profiles"></a>

 AWS Glue interactive sessions uses the same credentials as the AWS Command Line Interface or boto3, and interactive sessions honors and works with named profiles like the AWS CLI found in `~/.aws/config` (Linux and MacOS) or `%USERPROFILE%\.aws\config` (Windows). For more information, see [ Using named profiles ](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles). 

 Interactive sessions takes advantage of named profiles by allowing the AWS Glue Service Role and Session ID Prefix to be specified in a profile. To configure a profile role, add a line for the `iam_role` key and/or `session_id_prefix `to your named profile as shown below. The `session_id_prefix` does not require quotes. For example, if you want to add a ` session_id_prefix`, enter the value of the `session_id_prefix=myprefix`. 

```
[default]
region=us-east-1
aws_access_key_id=AKIAIOSFODNN7EXAMPLE 
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
glue_iam_role=arn:aws:iam::<AccountID>:role/<GlueServiceRole> 
session_id_prefix=<prefix_for_session_names>

[user1] 
region=eu-west-1
aws_access_key_id=AKIAI44QH8DHBEXAMPLE 
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
glue_iam_role=arn:aws:iam::<AccountID>:role/<GlueServiceRoleUser1> 
session_id_prefix=<prefix_for_session_names_for_user1>
```

 If you have a custom method of generating credentials, you can also configure your profile to use the `credential_process` parameter in your `~/.aws/config` file. For example: 

```
[profile developer]
region=us-east-1
credential_process = "/Users/Dave/generate_my_credentials.sh" --username helen
```

 You can find more details about sourcing credentials through the `credential_process` parameter here: [ Sourcing credentials with an external process](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html). 

 If a region or `iam_role` are not set in the profile that you are using, you must specify them using the `%region` and `%iam_role` magics in the first cell that you run. 