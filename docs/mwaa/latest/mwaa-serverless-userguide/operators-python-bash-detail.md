

# Using Python and Bash operators
<a name="operators-python-bash-detail"></a>

With Amazon MWAA Serverless, you can run custom Python code and shell scripts as workflow tasks using `PythonOperator` and `BashOperator` from the Apache Airflow standard provider package.
+ `PythonOperator` runs a Python callable. You can specify this operator as `airflow.providers.standard.operators.python.PythonOperator` (the current form in Apache Airflow 3) or `airflow.operators.python.PythonOperator` (also supported). This operator requires the `python_callable` task parameter.
+ `BashOperator` runs Bash commands or scripts. You can specify this operator as `airflow.providers.standard.operators.bash.BashOperator` (the current form in Apache Airflow 3) or `airflow.operators.bash.BashOperator` (also supported). This operator requires the `bash_command` task parameter.

**Note**  
`PythonOperator` and `BashOperator` tasks are considered AWS Managed Tasks, and the same billing applies. For more information about pricing, see [AWS pricing for Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/).

To use these operators, provide your code files when creating or updating a workflow.

## Prerequisites
<a name="operators-python-bash-prereqs"></a>

For instructions on getting started, see [Get started with Amazon MWAA Serverless](get-started.md). Before using Python or Bash operators, you need the following:
+ An Amazon S3 bucket for storing code and DAG files
+ An execution role with permissions to access your Amazon S3 bucket

## Code location and limits
<a name="operators-python-bash-code-location"></a>

Your code is separate from your workflow definition. The workflow definition is the YAML DAG that declares your tasks and their order, which you provide through the `DefinitionS3Location` parameter. Your code is the Python modules and shell scripts that the `PythonOperator` and `BashOperator` tasks run, which you provide separately through the `Code` parameter as described in this section.

Amazon MWAA Serverless versions your code together with your workflow definition. Each time you create or update a workflow, the service captures both as a new, immutable workflow version. For more information, see [Workflow versioning](mwaas-concepts.md#workflow-versioning).

When you create or update a workflow, specify your code location using the [Code](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html#mwaaserverless-CreateWorkflow-request-Code) parameter. This parameter takes an `S3Location` structure identifying the Amazon S3 object that holds your code, with the following fields:
+ `Bucket` – The name of your Amazon S3 bucket.
+ `ObjectKey` – The path to the code object in the bucket.
+ `VersionId` – (Optional) The version ID of the Amazon S3 object.

The following file types are accepted:
+ A single `.py` Python file
+ A single `.sh` shell script
+ A `.zip` archive containing multiple files

The following limits apply to code packages:
+ Maximum code file size: 250 MB
+ Maximum uncompressed size of a zip archive: 250 MB
+ Total code storage across all workflows in your account: 75 GB

For a single Python file or shell script, upload it directly to Amazon S3 without zipping.

## Preparing a zip package
<a name="operators-python-bash-zip"></a>

When you need multiple Python modules or third-party dependencies, package your code as a zip archive. All source files and dependency packages must be at the root level of the zip.

### Without dependencies
<a name="operators-python-bash-zip-no-deps"></a>

If your code consists of one or more files with no third-party dependencies, zip them with modules at the root level:

```
zip my_package.zip my_module.py helper.py
```

The resulting structure looks like the following:

```
my_package.zip/
  my_module.py
  helper.py
```

### With dependencies
<a name="operators-python-bash-zip-with-deps"></a>

If your code requires third-party libraries, stage your source files and their dependencies together in a single directory, then create the zip from the contents of that directory so that every file sits at the top level of the archive.

You do not need to bundle packages that are already pre-installed in the execution environment. For the list of pre-installed packages, see [Pre-installed packages](#operators-python-bash-preinstalled).

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

The `zip` command records paths relative to your current directory, so you run it from inside the `my_package` directory to place files at the root of the archive. Writing the archive to `../my_package.zip` puts it one level up, outside the directory being zipped, so the archive does not include itself. The `-x` option excludes compiled Python bytecode from the archive.

The `--platform`, `--python-version`, and `--only-binary` flags make pip download Linux x86\_64 wheels built for Python 3.12, which is what the Amazon MWAA Serverless worker runs. Without these flags, pip installs packages built for your local machine, and imports will fail at run time.

The resulting structure looks like the following:

```
my_package.zip/
  my_module.py
  requests/
  urllib3/
  ...
```

**Important**  
Keep the following requirements in mind when creating zip packages:  
Source files must be at the root of the zip archive.
Dependency packages must also be at the root, not nested in subdirectories.
All dependencies must be compatible with Python 3.12 and Linux x86\_64.
The total uncompressed size must not exceed 250 MB.
Do not include `__pycache__` directories in your code package, because Python bytecode compiled on a different operating system or architecture might not be compatible with the execution environment.

## Pre-installed packages
<a name="operators-python-bash-preinstalled"></a>

The Amazon MWAA Serverless execution environment already includes the following Python packages. Your tasks can import these packages without bundling them in a code package.


| Package | Version | 
| --- | --- | 
| apache-airflow | 3.0.6 | 
| apache-airflow-providers-amazon | 9.32.0 | 
| boto3 | 1.43.1 | 
| botocore | 1.43.1 | 
| dag-factory | 1.0.0 | 
| pyyaml | Not pinned | 
| lz4 | 4.4.4 | 
| aws-encryption-sdk | 4.0.3 or later | 
| aws-cryptographic-material-providers | 1.11.1 or later | 
| aws-cryptography-internal-kms | 1.11.1 or later | 
| aws-cryptography-internal-dynamodb | 1.11.1 or later | 
| aws-cryptography-internal-primitives | 1.11.1 or later | 

**Important**  
Pre-installed packages take precedence over the same package bundled in your code package. If you bundle a different version of any package listed in the preceding table, your bundled version is not used — the pre-installed version is imported instead. Design your code against these versions, and only bundle packages that are not already pre-installed.

## Limitations
<a name="operators-python-bash-limitations"></a>

**Important**  
Tasks run without internet access by default. If your code needs external network connectivity (for example, to call third-party APIs or download packages at runtime), provide a Amazon VPC with internet access using the `NetworkConfiguration` parameter when creating the workflow. For more information about network configuration, see [Networking](networking.md).

If Amazon MWAA Serverless cannot extract your code package, or if the package contains a corrupt Python environment, the workflow run fails. Review the workflow logs for specific error messages.

## Workspace directory
<a name="operators-python-bash-workspace"></a>

Each task runs on an Apache Airflow worker with the following configuration:
+ **Operating system/Architecture**: Linux/x86\_64
+ **CPU \| Memory**: 1 vCPU \| 3 GiB
+ **Runtime**: Python 3.12

Amazon MWAA Serverless extracts your code to `/usr/local/airflow/dags` in the worker container. This directory is the Apache Airflow DAGs directory, so Python modules at the root of your code package can be imported directly by your tasks.

`BashOperator` scripts execute with `/usr/local/airflow/dags` as the working directory.

## AWS credentials
<a name="operators-python-bash-credentials"></a>

Your workflow execution role credentials are available in the Amazon MWAA Serverless execution environment. AWS SDKs, including the pre-installed `boto3`, resolve these credentials automatically through the default credential provider chain, so you do not need to configure credentials in your code.

## Creating and running a workflow with custom code
<a name="operators-python-bash-cli"></a>

Use the AWS CLI to create a workflow that includes your code. The following example shows a YAML DAG definition that uses both `PythonOperator` and `BashOperator`:

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

For more information about the YAML workflow definition format, see [YAML support](mwaas-concepts.md#yaml-dag-authoring).

**Note**  
The `python_callable` value uses the format `{{module_name}}.{{function_name}}`.

To create a workflow with this definition and a code package, run the following command:

```
aws mwaa-serverless create-workflow \
    --name {{my-workflow}} \
    --definition-s3-location '{"Bucket": "DOC-EXAMPLE-BUCKET", "ObjectKey": "{{dags/my_dag.yaml}}", "VersionId": "{{definition-version-id}}"}' \
    --code '{"S3Location": {"Bucket": "DOC-EXAMPLE-BUCKET", "ObjectKey": "{{code/my_package.zip}}", "VersionId": "{{code-version-id}}"}}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --region {{us-east-1}}
```

**Note**  
The `VersionId` field is optional in both the `--definition-s3-location` and `--code` parameters. Include it to pin the workflow to an exact Amazon S3 object version; omit it to use the latest version of the object at the time you create or update the workflow. Amazon S3 object versions exist only when versioning is enabled on the bucket.

To update the code for an existing workflow, use the `update-workflow` command with the `--code` and `--definition-s3-location` parameters:

```
aws mwaa-serverless update-workflow \
    --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
    --definition-s3-location '{"Bucket": "DOC-EXAMPLE-BUCKET", "ObjectKey": "{{dags/my_dag.yaml}}", "VersionId": "{{definition-version-id}}"}' \
    --code '{"S3Location": {"Bucket": "DOC-EXAMPLE-BUCKET", "ObjectKey": "{{code/my_package.zip}}", "VersionId": "{{code-version-id}}"}}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --region {{us-east-1}}
```

To start a workflow run, use the `start-workflow-run` command:

```
aws mwaa-serverless start-workflow-run \
    --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
    --region {{us-east-1}}
```

## Code versioning
<a name="operators-python-bash-versioning"></a>

When you call [GetWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflow.html), the response includes a `Code` object containing an `S3Location` structure describing the Amazon S3 object, with the following fields:
+ `Bucket` – The Amazon S3 bucket name.
+ `ObjectKey` – The path to the code object.
+ `VersionId` – The version ID of the Amazon S3 object.

The response also includes a separate, top-level `CodeSnapshottedAt` field – a timestamp indicating when the service captured the code for that workflow version.

To track exactly which code version your workflow uses, enable Amazon S3 versioning on your bucket and include the `VersionId` in the `S3Location` of the `Code` parameter when creating or updating the workflow.

Amazon MWAA Serverless snapshots your code when you create or update a workflow. If you omit `VersionId`, the service captures the latest version of the Amazon S3 object at that time. The workflow keeps running against this snapshot, so changing the Amazon S3 object afterward does not affect the workflow until you update it again.

**Note**  
We recommend that you enable Amazon S3 versioning for production workflows to ensure reproducible deployments and deterministic outcomes of your workflows.

## Troubleshooting
<a name="operators-python-bash-troubleshooting"></a>

### Viewing task logs
<a name="operators-python-bash-troubleshooting-logs"></a>

You can find task logs in CloudWatch Logs under the following log group:

```
/aws/mwaa-serverless/{{my-workflow-a1b2c3d4e5}}/
```

The Amazon MWAA Serverless service appends a unique identifier to the workflow name you pass in `--name`. The full workflow name is the segment after `workflow/` in the `WorkflowArn` that `create-workflow` returns. For example, if you pass `--name my-workflow`, the returned ARN might end in `workflow/my-workflow-a1b2c3d4e5`, making the full workflow name `my-workflow-a1b2c3d4e5`. Use this full name in the log group path, not the bare value you passed to `--name`.

If you set a `LogGroupName` in the `LoggingConfiguration` when creating the workflow, logs go to that log group instead.

Logs can take a few minutes to appear in CloudWatch Logs after a run starts.

### Checking run status
<a name="operators-python-bash-troubleshooting-status"></a>

Use `get-workflow-run` to check the status and view task instance details:

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

In the response, `RunState`, `TaskInstances`, and `Duration` are returned inside the `RunDetail` object. `RunId` and `RunType` are at the top level. Possible values for `RunState` are STARTING, QUEUED, RUNNING, SUCCESS, FAILED, TIMEOUT, STOPPING, and STOPPED. `TaskInstances` lists the individual task instances for the run.