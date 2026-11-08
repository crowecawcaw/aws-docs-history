

# Running custom code with Python, Bash, and custom operators
<a name="custom-code-operators"></a>

In addition to the AWS service operators that Amazon MWAA Serverless supports out of the box, you can run your own code as workflow tasks by providing a code package when you create or update a workflow. You can run the following kinds of code-based tasks:
+ `PythonOperator` runs a Python callable. You can specify this operator as `airflow.providers.standard.operators.python.PythonOperator` (the current form in Apache Airflow 3) or `airflow.operators.python.PythonOperator` (also supported). This operator requires the `python_callable` task parameter.
+ `BashOperator` runs Bash commands or scripts. You can specify this operator as `airflow.providers.standard.operators.bash.BashOperator` (the current form in Apache Airflow 3) or `airflow.operators.bash.BashOperator` (also supported). This operator requires the `bash_command` task parameter.
+ Operators from Apache Airflow provider packages that aren't pre-installed, such as the HTTP, Snowflake, or dbt providers. You install the provider into your code package and reference the operator by its full class path.
+ Your own operators, which you write by subclassing `BaseOperator`. For more information, see [Writing your own operators](#operators-custom).

You can also use the same code package to carry a custom secrets backend that your tasks use to look up Apache Airflow connections and variables. For more information, see [Option C: Your own secrets backend class](connections.md#connections-backend-custom).

Every kind of custom code follows the same two steps: prepare a code package, then create or update the workflow with it. The sections that follow describe how this works and then walk through each step.

## How custom code runs in Amazon MWAA Serverless
<a name="operators-python-bash-how-it-works"></a>

You store your workflow definition and your code separately. The workflow definition is the YAML DAG that declares your tasks and their order. Your code is the Python modules, shell scripts, provider packages, and custom operator classes that those tasks run. The following diagram shows how the two come together in four stages.

![Flow diagram of the four stages for running custom code in Amazon MWAA Serverless, from preparing your files to a task run on an Apache Airflow worker.](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/images/mwaas-custom-code-architecture.png)


The diagram reads from left to right. Each numbered box is one stage, and the labeled arrows show what moves between the components:

1. **You prepare.** The first box shows the two files that you create: a YAML workflow definition and a code package. The code package is a single `.py` file, a single `.sh` script, or a `.zip` archive with your modules, operators, and dependencies.

1. **Amazon S3 bucket.** The *upload* arrows show that you upload both files to an Amazon S3 bucket, where they become the workflow definition object and the code package object. The examples on this page use the object keys `dags/my_dag.yaml` for the workflow definition and `code/my_package.zip` for the code package.

1. **Amazon MWAA Serverless.** Both objects feed the `CreateWorkflow` or `UpdateWorkflow` operation, which creates a workflow version. You pass the definition in `DefinitionS3Location` and the code in `Code`. You can also pass environment variables in `Environment` and the execution role in `RoleArn`. Amazon MWAA Serverless snapshots the definition and code into a new, immutable workflow version. Later changes to the Amazon S3 objects don't affect the workflow until you update it again. For more information, see [Workflow versioning](mwaas-concepts.md#workflow-versioning).

1. **Each task run.** The *run or schedule* arrow shows that when a run starts, either from `StartWorkflowRun` or from a schedule, each task in the workflow version runs on an Apache Airflow worker. Amazon MWAA Serverless extracts your code to `/usr/local/airflow/dags`, which is on the task's import path. Amazon MWAA Serverless also injects your environment variables and provides the execution role credentials. The *connections and variables* arrow shows the worker looking up connections and variables in the secrets backend that you configure, such as Secrets Manager. The *task logs* arrow shows the worker writing task logs to CloudWatch Logs.

## Prerequisites
<a name="operators-python-bash-prereqs"></a>

For instructions on getting started, see [Get started with Amazon MWAA Serverless](get-started.md). Before running custom code, you need the following:
+ An Amazon S3 bucket for storing code and workflow definition files
+ An execution role with permissions to access your Amazon S3 bucket

## Preparing your code package
<a name="operators-python-bash-zip"></a>

Package preparation is the same for every kind of custom code. Choose the format that fits your code, then follow the matching instructions in this section.

### Supported formats and limits
<a name="operators-python-bash-code-location"></a>

Amazon MWAA Serverless accepts the following file types for a code package:
+ A single `.py` Python file
+ A single `.sh` shell script
+ A `.zip` archive containing multiple files

For a single Python file or shell script, upload it directly to Amazon S3 without zipping. Use a zip archive when you need multiple modules, folders, provider packages, or third-party dependencies. For size limits, see [Limitations](#operators-python-bash-limitations).

### Zip archive layout
<a name="operators-python-bash-zip-layout"></a>

Amazon MWAA Serverless extracts the archive onto the task's import path. You can place modules at the root of the archive, or organize them into folders that form Python packages. You import a module at the root by its file name, and a module inside a folder through that folder. For example, an archive with the following structure exposes the operator module as `my_operators.http`:

```
my_package.zip/
  my_dag_module.py
  my_operators/
    __init__.py
    http.py
```

**Note**  
Keep your files out of any extra top-level folder that isn't part of the import path. Suppose that you create the archive from a parent directory, so every file sits under a folder such as `code/`. Your import paths must then include that prefix, for example `code.my_operators.http`. To place your modules and packages at the archive root, create the archive from the *contents* of your staging directory.

### Packaging code without dependencies
<a name="operators-python-bash-zip-no-deps"></a>

If your code consists of one or more files with no third-party dependencies, zip them from the directory that contains them:

```
zip -r my_package.zip my_module.py helper.py my_operators -x "*__pycache__*" "*.pyc"
```

The resulting structure looks like the following:

```
my_package.zip/
  my_module.py
  helper.py
  my_operators/
    __init__.py
    http.py
```

### Packaging code with dependencies
<a name="operators-python-bash-zip-with-deps"></a>

If your code requires third-party libraries, stage your source files and their dependencies together in a single directory, then create the zip from the contents of that directory. You don't need to bundle packages that are already pre-installed. For the list, see [Pre-installed packages](#operators-python-bash-preinstalled).

```
# Stage your source files and dependencies in one directory
mkdir my_package
cp my_module.py my_package/

# Install dependencies into the same directory
pip install -r requirements.txt --target my_package \
    --platform manylinux2014_x86_64 \
    --python-version 3.12 \
    --only-binary=:all:

# Change to the package directory
cd my_package

# Create the zip one level up, with all files at the archive root
zip -r ../my_package.zip . -x "*__pycache__*" "*.pyc"
```

The `--platform`, `--python-version`, and `--only-binary` flags make pip download Linux x86\_64 wheels built for Python 3.12, which is what the Amazon MWAA Serverless worker runs. Without these flags, pip installs packages built for your local machine, and imports can fail at runtime.

The `zip` command records paths relative to your current directory, so you run it from inside the `my_package` directory to place files at the root of the archive. Writing the archive to `../my_package.zip` keeps the archive from including itself.

The resulting structure looks like the following:

```
my_package.zip/
  my_module.py
  requests/
  urllib3/
  ...
```

### Adding Apache Airflow provider packages
<a name="operators-provider-packages"></a>

Beyond the pre-installed providers, you can run operators from any Apache Airflow provider package, such as the HTTP, Snowflake, or dbt providers. Amazon MWAA Serverless doesn't use a `requirements.txt` file, so you install the provider into your code package instead.

Install the provider into your staging directory with the same platform flags as in [Packaging code with dependencies](#operators-python-bash-zip-with-deps). Also add the Apache Airflow constraints file that matches the pre-installed Apache Airflow version and Python version. The constraints file keeps the provider and its dependencies compatible with the pre-installed Apache Airflow release.

In the following command, replace `apache-airflow-providers-http` with the provider package that you need. If needed, update the Apache Airflow and Python versions in the constraints URL to match the pre-installed versions listed in [Pre-installed packages](#operators-python-bash-preinstalled).

```
pip install apache-airflow-providers-http --target my_package \
    --platform manylinux2014_x86_64 \
    --python-version 3.12 \
    --only-binary=:all: \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt"
```

Then zip the staging directory as described in [Packaging code with dependencies](#operators-python-bash-zip-with-deps). For an example that uses a provider operator, see [Example: an operator from a provider package](#operators-provider-example).

**Important**  
Keep the following requirements in mind when creating zip packages:  
Place source files at the root of the zip archive, or inside folders that form Python packages, and make sure your import paths match that layout.
Install dependencies with pip `--target` so that dependency packages are at the root of the archive, not nested in an extra top-level directory.
All dependencies must be compatible with Python 3.12 and Linux x86\_64.
Don't include `__pycache__` directories, because Python bytecode compiled on a different operating system or architecture might not be compatible with the execution environment.
Don't bundle a different version of a pre-installed package. The pre-installed version takes precedence.

## Creating, updating, and running the workflow
<a name="operators-python-bash-cli"></a>

These steps are the same for every kind of custom code. Only the task keys in your workflow definition differ. The following table shows how a task references each kind of custom code.


| Kind of code | How the task references your code | 
| --- | --- | 
| PythonOperator | python\_callable: {{module\_name}}.{{function\_name}} | 
| BashOperator | bash\_command, which can run a script from your code package. Scripts run with /usr/local/airflow/dags as the working directory. | 
| Provider operator | operator: set to the provider's full class path, such as airflow.providers.http.operators.http.HttpOperator. | 
| Custom operator | operator: set to your class path, such as my\_operators.http.MyHttpOperator. Amazon MWAA Serverless passes other task keys to its \_\_init\_\_ method. | 

For more information about the YAML workflow definition format, see [YAML support](mwaas-concepts.md#yaml-dag-authoring).

1. Upload the code package and the workflow definition to your Amazon S3 bucket. Replace the object keys with your own.

   ```
   aws s3 cp my_package.zip s3://amzn-s3-demo-bucket/{{code/my_package.zip}}
   aws s3 cp my_dag.yaml s3://amzn-s3-demo-bucket/{{dags/my_dag.yaml}}
   ```

1. Create the workflow, providing the code through the `--code` parameter. Replace {{my-workflow}} with your workflow name. Replace the object keys and version IDs with your own, the role ARN with your execution role ARN, and {{us-east-1}} with your Region.

   ```
   aws mwaa-serverless create-workflow \
       --name {{my-workflow}} \
       --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}", "VersionId": "{{definition-version-id}}"}' \
       --code '{"S3Location": {"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{code/my_package.zip}}", "VersionId": "{{code-version-id}}"}}' \
       --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
       --region {{us-east-1}}
   ```

   The [Code](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html#mwaaserverless-CreateWorkflow-request-Code) parameter takes an `S3Location` with `Bucket`, `ObjectKey`, and an optional `VersionId`. Include `VersionId` in either location to pin the workflow to an exact Amazon S3 object version, or omit it to use the latest version at the time you create or update the workflow. Amazon S3 object versions exist only when you enable versioning on the bucket.

1. To change the code or definition later, upload the new files and run `update-workflow` with both locations:

   ```
   aws mwaa-serverless update-workflow \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
       --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
       --code '{"S3Location": {"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{code/my_package.zip}}"}}' \
       --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
       --region {{us-east-1}}
   ```

1. Start a workflow run. The run can take a few minutes to complete.

   ```
   aws mwaa-serverless start-workflow-run \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
       --region {{us-east-1}}
   ```

1. Check the status of the run.

   ```
   aws mwaa-serverless get-workflow-run \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
       --run-id {{run-id}} \
       --region {{us-east-1}}
   ```

   ```
   {
       "RunId": "abc123XYZ",
       "RunType": "ON_DEMAND",
       "RunDetail": {
           "Duration": 127,
           "TaskInstances": [
               "..."
           ],
           "RunState": "SUCCESS"
       }
   }
   ```

   `RunState`, `TaskInstances`, and `Duration` are inside the `RunDetail` object. Possible values for `RunState` are `STARTING`, `QUEUED`, `RUNNING`, `SUCCESS`, `FAILED`, `TIMEOUT`, `STOPPING`, and `STOPPED`. To view task output, see [Viewing task logs](#operators-python-bash-troubleshooting-logs).

## Writing your own operators
<a name="operators-custom"></a>

When no existing operator fits your task, you can write your own. Subclass `BaseOperator` and implement an `execute` method:
+ Define `execute(self, context)`. Amazon MWAA Serverless calls this method when the task runs. Apache Airflow stores its return value in XCom, subject to the XCom data quota. For more information, see [Quotas for Amazon MWAA Serverless](mwaa-serverless-quotas.md).
+ Accept `**kwargs` in your `__init__` method and pass them to `super().__init__(**kwargs)` so that `task_id` and other standard arguments reach `BaseOperator`.

In your workflow definition, set the `operator` key to the operator's class path in the form `{{module}}.{{Class}}`, or `{{package}}.{{module}}.{{Class}}` for a module in a folder. Amazon MWAA Serverless passes the other keys under the task to your operator's `__init__` method as keyword arguments. For more information about the package layout, see [Zip archive layout](#operators-python-bash-zip-layout).

For more information about writing operators, see [Creating a custom Operator](https://airflow.apache.org/docs/apache-airflow/3.0.6/howto/custom-operator.html) in the Apache Airflow documentation. For a minimal example, see [Example: a minimal custom operator](#operators-custom-simple-example).

## Examples
<a name="operators-python-bash-examples"></a>

The following examples start with the simplest case and build up. Each example uses the steps in [Creating, updating, and running the workflow](#operators-python-bash-cli).

### Example: Python and Bash tasks
<a name="operators-python-bash-example"></a>

The following module defines a Python callable. Save it as `my_module.py`, and zip it with `zip my_package.zip my_module.py`.

```
# my_module.py
def hello_world():
    print("Hello from Python")
    return "done"
```

The following workflow definition runs the callable with `PythonOperator` and a command with `BashOperator`:

```
my_dag:
  start_date: "2024-01-01"
  schedule: null
  tasks:
    python_task:
      operator: airflow.providers.standard.operators.python.PythonOperator
      python_callable: my_module.hello_world
    bash_task:
      operator: airflow.providers.standard.operators.bash.BashOperator
      bash_command: "echo 'Hello from bash' && date"
```

Upload both files, create the workflow, and start a run as described in [Creating, updating, and running the workflow](#operators-python-bash-cli).

### Example: a minimal custom operator
<a name="operators-custom-simple-example"></a>

This example uses only a custom operator, with no connections, variables, or third-party dependencies. It also shows how to reference an operator that sits in a folder of the code package.

1. Create the following layout. The `__init__.py` file can be empty.

   ```
   my_operators/
     __init__.py
     greeting.py
   ```

1. Add the operator to `my_operators/greeting.py`. It takes a `name` argument, logs a greeting, and returns the greeting to XCom.

   ```
   # my_operators/greeting.py
   try:
       from airflow.sdk import BaseOperator  # Apache Airflow 3
   except ImportError:
       from airflow.models import BaseOperator
   
   
   class GreetingOperator(BaseOperator):
       def __init__(self, name, greeting="Hello", **kwargs):
           super().__init__(**kwargs)  # Pass kwargs through so that task_id and other arguments reach BaseOperator
           if not name:
               raise ValueError("name must be a non-empty string")
           self.name = name
           self.greeting = greeting
   
       def execute(self, context):
           message = f"{self.greeting}, {self.name}!"
           self.log.info(message)
           return message
   ```

   The operator accepts the following arguments:
   + `name` – (Required) the name to greet.
   + `greeting` – (Optional) the greeting word. The default is `Hello`.

1. Zip the folder from the directory that contains it, so that `my_operators/` is at the root of the archive:

   ```
   zip -r my_package.zip my_operators -x "*__pycache__*" "*.pyc"
   ```

1. Create a workflow definition named `greeting_dag.yaml`. The `operator` key includes the folder name, and the `name` key is passed to the operator's `__init__` method.

   ```
   greeting_dag:
     start_date: "2024-01-01"
     schedule: null
     tasks:
       greet:
         operator: my_operators.greeting.GreetingOperator
         name: "MWAA Serverless"
   ```

1. Upload both files, create the workflow, and start a run as described in [Creating, updating, and running the workflow](#operators-python-bash-cli). The task log contains the following line:

   ```
   Hello, MWAA Serverless!
   ```

### Example: an operator from a provider package
<a name="operators-provider-example"></a>

This example runs the `HttpOperator` from the `apache-airflow-providers-http` provider. Install the provider into your code package as described in [Adding Apache Airflow provider packages](#operators-provider-packages), then reference the operator by its full class path:

```
http_dag:
  start_date: "2024-01-01"
  schedule: null
  tasks:
    call_api:
      operator: airflow.providers.http.operators.http.HttpOperator
      http_conn_id: my_http
      endpoint: status
      method: GET
```

In this example, the task keys have the following meanings:
+ `http_conn_id` – the ID of an Apache Airflow connection that supplies the host and other connection details for the HTTP endpoint. For information about defining connections, see [Managing connections and variables](connections.md).
+ `endpoint` – the path that the operator appends to the connection's host.
+ `method` – the HTTP method of the request.

Because this operator calls an external endpoint, create the workflow with a Amazon VPC that can reach it. For more information, see [Networking](networking.md).

### Example: a custom operator that reads a connection and a variable
<a name="operators-custom-example"></a>

The following operator reads an Apache Airflow connection and a variable in its `execute` method, prints the connection fields, and returns a result to XCom. If the connection or variable doesn't exist, the operator fails the task with a message that names the missing key. Save it as `backend_conn_operator.py`.

```
# backend_conn_operator.py
from airflow.exceptions import AirflowException, AirflowNotFoundException

try:
    from airflow.sdk import BaseHook, BaseOperator, Variable  # Apache Airflow 3
except ImportError:
    from airflow.hooks.base import BaseHook
    from airflow.models import BaseOperator, Variable


class BackendConnOperator(BaseOperator):
    def __init__(self, conn_id="my_http", var_key="app_stage", **kwargs):
        super().__init__(**kwargs)  # Pass kwargs through so that task_id and other arguments reach BaseOperator
        self.conn_id = conn_id
        self.var_key = var_key

    def execute(self, context):
        try:
            conn = BaseHook.get_connection(self.conn_id)
        except AirflowNotFoundException as e:
            raise AirflowException(f"Connection {self.conn_id} not found") from e
        print(f"conn_type = {conn.conn_type}")
        print(f"host      = {conn.host}")
        print(f"port      = {conn.port}")
        print(f"schema    = {conn.schema}")

        try:
            var_val = Variable.get(self.var_key)
        except KeyError as e:
            raise AirflowException(f"Variable {self.var_key} not found") from e
        print(f"Variable {self.var_key} = {var_val}")
        return {"host": conn.host, "var": var_val}
```

The operator accepts the following arguments:
+ `conn_id` – the ID of the Apache Airflow connection to read.
+ `var_key` – the key of the Apache Airflow variable to read.

The following workflow definition runs the operator. Save it as `backend_conn_dag.yaml`.

```
backend_conn_dag:
  start_date: "2024-01-01"
  schedule: null
  tasks:
    read_connection_and_variable:
      operator: backend_conn_operator.BackendConnOperator
      conn_id: my_http
      var_key: app_stage
```

1. Store the `my_http` connection and the `app_stage` variable so that your task can read them. Because these particular values aren't sensitive, you can store them in either of the following ways:
   + In AWS Secrets Manager, with the Secrets Manager backend configured for the workflow. For more information, see [Using the Secrets Manager backend](connections.md#connections-secrets-manager). For the execution role permissions, see [Execution role permissions](connections.md#connections-permissions). In the following AWS CLI commands, replace the connection URI with your HTTP endpoint URL, {{prod}} with your variable value, and {{us-east-1}} with the Region of your workflow.

     ```
     aws secretsmanager create-secret \
         --name airflow/connections/my_http \
         --secret-string '{{http://api.example.com:8443/v1}}' \
         --region {{us-east-1}}
     
     aws secretsmanager create-secret \
         --name airflow/variables/app_stage \
         --secret-string '{{prod}}' \
         --region {{us-east-1}}
     ```
   + As environment variables, by setting `AIRFLOW_CONN_MY_HTTP` and `AIRFLOW_VAR_APP_STAGE` in the workflow's `Environment` block. For more information, see [Defining connections and variables with environment variables](connections.md#connections-environment-variables).

1. Upload the operator module and the workflow definition, then create the workflow and start a run as described in [Creating, updating, and running the workflow](#operators-python-bash-cli). Because the code is a single `.py` file, you don't need to create a zip archive. Pass the file directly in `--code`, for example `"ObjectKey": "code/backend_conn_operator.py"`.

1. View the task logs. The task prints output similar to the following, which shows that the custom operator read the connection and the variable:

   ```
   conn_type = http
   host      = api.example.com
   port      = 8443
   schema    = v1
   Variable app_stage = prod
   ```

## Execution environment reference
<a name="operators-python-bash-environment"></a>

### Worker configuration and workspace directory
<a name="operators-python-bash-workspace"></a>

Each task runs on an Apache Airflow worker with the following configuration:
+ **Operating system/Architecture**: Linux/x86\_64
+ **CPU and memory**: 1 vCPU and 3 GiB
+ **Runtime**: Python 3.12

Amazon MWAA Serverless extracts your code to `/usr/local/airflow/dags` in the worker container. This directory is the Apache Airflow DAGs directory and is on the task's import path, so your tasks can import the modules and packages in your code package. `BashOperator` scripts run with this directory as the working directory.

### AWS credentials
<a name="operators-python-bash-credentials"></a>

Your workflow execution role credentials are available in the Amazon MWAA Serverless execution environment. AWS SDKs, including the pre-installed `boto3`, resolve these credentials automatically through the default credential provider chain, so you don't need to configure credentials in your code.

### Pre-installed packages
<a name="operators-python-bash-preinstalled"></a>

The Amazon MWAA Serverless execution environment already includes the following Python packages. Your tasks can import these packages without bundling them in a code package.


| Package | Version | 
| --- | --- | 
| apache-airflow | 3.0.6 | 
| apache-airflow-providers-amazon | 9.38.0 | 
| apache-airflow-providers-duckdb | 0.2.1 | 
| duckdb | 2.0.0 | 
| boto3 | 1.43.1 | 
| botocore | 1.43.1 | 
| dag-factory | 1.0.0 | 
| pyyaml | Not pinned | 
| lz4 | 4.4.4 | 

### Code versioning
<a name="operators-python-bash-versioning"></a>

Amazon MWAA Serverless snapshots your code when you create or update a workflow. If you omit `VersionId`, the service captures the latest version of the Amazon S3 object at that time. The workflow keeps running against this snapshot, so changing the Amazon S3 object afterward doesn't affect the workflow until you update it again.

When you call [GetWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflow.html), the response includes a `Code` object with the `S3Location` (`Bucket`, `ObjectKey`, and `VersionId`) of the captured code. A separate, top-level `CodeSnapshottedAt` field shows when the service captured the code for that workflow version.

**Note**  
For production workflows, enable Amazon S3 versioning and pass `VersionId`. This makes your deployments reproducible and the outcomes of your workflows deterministic.

## Limitations
<a name="operators-python-bash-limitations"></a>

The following limitations apply to custom code and operators:
+ Maximum code file size: 250 MB. Maximum uncompressed size of a zip archive: 250 MB.
+ Total code storage across all workflows in your account: 75 GB.
+ Code runs on Linux x86\_64 with Python 3.12. Dependencies must be built for this platform.
+ Tasks run without internet access by default. If your code calls third-party APIs or downloads packages at runtime, provide a Amazon VPC with internet access by using the `NetworkConfiguration` parameter. For more information, see [Networking](networking.md).
+ Pre-installed packages take precedence over the same package in your code package. You can't replace `apache-airflow`, `apache-airflow-providers-amazon`, or any other pre-installed package with a different version.
+ Amazon MWAA Serverless doesn't validate custom or provider operator class paths or their arguments when you create or update a workflow. Apache Airflow resolves the class when the task runs, so errors appear in the task logs.
+ Deferrable operators, and the `deferrable` task parameter, aren't supported. For more information, see [Apache Airflow Parameter Support](supported-airflow-parameters.md).
+ Amazon MWAA Serverless captures code when you create or update a workflow. Changing the Amazon S3 object doesn't change a workflow until you update it.

## Troubleshooting custom code and operators
<a name="operators-python-bash-troubleshooting"></a>

### Viewing task logs
<a name="operators-python-bash-troubleshooting-logs"></a>

You can find task logs in CloudWatch Logs under the following log group:

```
/aws/mwaa-serverless/{{my-workflow-a1b2c3d4e5}}/
```

Amazon MWAA Serverless appends a unique identifier to the workflow name that you pass in `--name`. The full workflow name is the segment after `workflow/` in the `WorkflowArn` that `create-workflow` returns. For example, if you pass `--name my-workflow`, the returned ARN might end in `workflow/my-workflow-a1b2c3d4e5`. Use this full name in the log group path.

If you set a `LogGroupName` in the `LoggingConfiguration` when you create the workflow, logs go to that log group instead. Logs can take a few minutes to appear after a run starts.

### Common custom code errors
<a name="operators-custom-troubleshooting-errors"></a>

The following table lists common errors that you might see when you run custom code, along with their causes and fixes.


| Error or symptom | Cause | Fix | 
| --- | --- | --- | 
| ModuleNotFoundError for an operator, callable, or secrets backend | The class or module path doesn't match the layout of your code package, the archive has an extra top-level folder, a folder is missing \_\_init\_\_.py, or the --code parameter is missing. | Make sure the path matches where the module sits in the package, and that you provide the package through --code. For more information, see [Zip archive layout](#operators-python-bash-zip-layout). | 
| ImportError or an error about an invalid ELF header or missing shared library | A dependency was installed for your local platform instead of Linux x86\_64 and Python 3.12. | Reinstall dependencies with the --platform, --python-version, and --only-binary flags. For more information, see [Packaging code with dependencies](#operators-python-bash-zip-with-deps). | 
| A bundled package version isn't used, or a provider fails with a version conflict | The package is pre-installed, and the pre-installed version takes precedence. Or the provider was installed without the Apache Airflow constraints file. | Don't bundle pre-installed packages, and install providers with the constraints file. For more information, see [Adding Apache Airflow provider packages](#operators-provider-packages). | 
| TypeError: unexpected keyword argument | The task keys in your workflow definition don't match the arguments that the operator's \_\_init\_\_ method accepts. | Match the task keys in the YAML to the operator's \_\_init\_\_ parameters, or accept \*\*kwargs. | 
| The run fails before any task starts, with an extraction error | Amazon MWAA Serverless can't extract the code package, the archive is larger than 250 MB uncompressed, or it contains a corrupt Python environment. | Rebuild the archive with zip, check its uncompressed size, and review the workflow logs for the error message. | 
| Task times out or fails to connect to an external host | Tasks have no internet access by default. | Create the workflow with a Amazon VPC that can reach the host. For more information, see [Networking](networking.md). | 
| The workflow doesn't use updated code | Amazon MWAA Serverless snapshots your code when you create or update a workflow, so changing the Amazon S3 object alone doesn't update the workflow. | Upload the new code, then run update-workflow with the --code parameter. For more information, see [Code versioning](#operators-python-bash-versioning). | 
| Connection or variable not found | The secret name or prefix doesn't match the lookup key, or the execution role lacks permission to read it. | For causes and fixes, see [Troubleshooting connections and variables](connections.md#connections-troubleshooting). | 