# Configuring job properties for Python shell jobs in AWS Glue

You can use a Python shell job to run Python scripts as a shell in AWS Glue. With a Python
shell job, you can run scripts that are compatible with Python 3.6 or Python 3.9.

###### Note

Support for Pyshell v3.6 will end on March 1, 2026. To migrate your workloads, see
[Migrate from AWS Glue Python shell jobs](pyshell-migration.md "pyshell-migration.md").
If you wish to continue with Python shell v3.9 see
[Migrating from Python shell 3.6 to Python shell 3.9](#migrating-version-pyshell36-to-pyshell39 "#migrating-version-pyshell36-to-pyshell39").

###### Topics

- [Limitations](#python-shell-limitations "#python-shell-limitations")
- [Execution environment](#python-shell-execution-environment "#python-shell-execution-environment")
- [Defining job properties for Python shell jobs](#create-job-python-properties "#create-job-python-properties")
- [Supported libraries for Python shell jobs](#python-shell-supported-library "#python-shell-supported-library")
- [Providing your own Python library](#create-python-extra-library "#create-python-extra-library")
- [Use AWS CloudFormation with Python shell jobs in
  AWS Glue](#python-shell-jobs-cloudformation "#python-shell-jobs-cloudformation")
- [Migrating from Python shell 3.6 to Python shell 3.9](#migrating-version-pyshell36-to-pyshell39 "#migrating-version-pyshell36-to-pyshell39")
- [Migrate from AWS Glue Python shell jobs](pyshell-migration.md "pyshell-migration.md")

## Limitations

Note the following limitations of Python Shell jobs:

- You can't use job bookmarks with Python shell jobs.
- You can't package any Python libraries as `.egg` files in Python 3.9+.
  Instead, use `.whl`.
- The `--extra-files` option cannot be used, because of a limitation on temporary copies of S3 data.

## Execution environment

Python shell jobs run in a managed execution environment that provides access to local storage for temporary data processing:

**Local temporary storage**

The `/tmp` directory is available for temporary storage during job execution.
This directory provides approximately 14 GiB of free space that you can use for:

- Temporary file processing
- Intermediate data storage
- Caching small datasets

###### Note

The `/tmp` directory is ephemeral and is cleaned up after job completion.
Do not use it for persistent storage of important data.

## Defining job properties for Python shell jobs

These sections describe defining job properties in AWS Glue Studio, or using the AWS CLI.

### AWS Glue Studio

When you define your Python shell job in AWS Glue Studio,
you provide some of the following properties:

**IAM role**

Specify the AWS Identity and Access Management (IAM) role that is used for authorization to
resources that are used to run the job and access data stores. For more
information about permissions for running jobs in AWS Glue, see [Identity and access management for AWS Glue](security-iam.md "security-iam.md").

**Type**

Choose **Python shell** to run a Python script with the
job command named `pythonshell`.

**Python version**

Choose the Python version. The default is Python 3.9. Valid versions are Python 3.6 and Python 3.9.

**Load common analytics libraries (Recommended)**

Choose this option to include common libraries for Python 3.9 in the Python shell.

If your libraries are either custom or they conflict with the pre-installed ones, you can choose not to install common libraries. However, you can install additional libraries besides the common libraries.

When you select this option, the `library-set` option is set to `analytics`. When you de-select this option, the `library-set` option is set to `none`.

**Script filename and Script path**

The code in the script defines your job's procedural logic.
You provide the script name and location in Amazon Simple Storage Service
(Amazon S3). Confirm that there isn't a file with the same name as the script
directory in the path. To learn more about using scripts, see [AWS Glue programming guide](edit-script.md "edit-script.md").

**Script**

The code in the script defines your job's procedural logic. You can code
the script in Python 3.6 or Python 3.9. You can edit a script in AWS Glue Studio.

**Data processing units**

The maximum number of AWS Glue data processing units (DPUs) that can be
allocated when this job runs. A DPU is a relative measure of processing
power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For
more information, see [AWS Glue
pricing](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/").

You can set the value to 0.0625 or 1. The default is 0.0625. In either case, the local disk for the instance will be 20GB.

### CLI

You can also create a **Python shell** job using the AWS CLI, as in the
following example.

```

 aws glue create-job --name python-job-cli --role Glue_DefaultRole
     --command '{"Name" :  "pythonshell", "PythonVersion": "3.9", "ScriptLocation" : "s3://amzn-s3-demo-bucket/scriptname.py"}'
     --max-capacity 0.0625

```

###### Note

You don't need to specify the version of AWS Glue since the parameter `--glue-version`
doesn't apply for AWS Glue shell jobs. Any version specified will be ignored.

Jobs that you create with the AWS CLI default to Python 3. Valid Python versions are 3 (corresponding to 3.6), and 3.9.
To specify Python 3.6, add this tuple to the `--command` parameter: `"PythonVersion":"3"`

To specify Python 3.9, add this tuple to the `--command` parameter: `"PythonVersion":"3.9"`

To set the maximum capacity used by a Python shell job, provide the
`--max-capacity` parameter. For Python shell jobs, the
`--allocated-capacity` parameter can't be used.

## Supported libraries for Python shell jobs

In Python shell using Python 3.9, you can choose the library set to use pre-packaged library sets for your needs.
You can use the `library-set` option to choose the library set. Valid values are `analytics`,
and `none`.

The environment for running a Python shell job supports the following libraries:

| Python version     | Python 3.6 | Python 3.9    |
| ------------------ | ---------- | ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Library set**    | **N/A**    | **analytics** | **none** |
| avro               |            | 1.11.0        |          |
| awscli             | 116.242    | 1.23.5        | 1.23.5   |
| awswrangler        |            | 2.15.1        |          |
| botocore           | 1.12.232   | 1.24.21       | 1.23.5   |
| boto3              | 1.9.203    | 1.21.21       |          |
| elasticsearch      |            | 8.2.0         |          |
| numpy              | 1.16.2     | 1.22.3        |          |
| pandas             | 0.24.2     | 1.4.2         |          |
| psycopg2           |            | 2.9.3         |          |
| pyathena           |            | 2.5.3         |          |
| PyGreSQL           | 5.0.6      |               |          |
| PyMySQL            |            | 1.0.2         |          |
| pyodbc             |            | 4.0.32        |          |
| pyorc              |            | 0.6.0         |          |
| redshift-connector |            | 2.0.907       |          |
| requests           | 2.22.0     | 2.27.1        |          |
| scikit-learn       | 0.20.3     | 1.0.2         |          |
| scipy              | 1.2.1      | 1.8.0         |          |
| SQLAlchemy         |            | 1.4.36        |          |
| s3fs               |            | 2022.3.0      |          | You can use the `NumPy` library in a Python shell job for scientific computing. For more information, see [NumPy](http://www.numpy.org "http://www.numpy.org"). The following example shows a NumPy script that can be used in a Python shell job. The script prints "Hello world" and the results of several mathematical calculations. `import numpy as np print("Hello world") a = np.array([20,30,40,50]) print(a) b = np.arange( 4 ) print(b) c = a-b print(c) d = b**2 print(d)` ## Providing your own Python library ### Using PIP Python shell using Python 3.9 lets you provide additional Python modules or different versions at the job level. You can use the `--additional-python-modules` option with a list of comma-separated Python modules to add a new module or change the version of an existing module. You cannot provide custom Python modules hosted on Amazon S3 with this parameter when using Python shell jobs. For example to update or to add a new `scikit-learn` module use the following key and value: `"--additional-python-modules", "scikit-learn==0.21.3"`. AWS Glue uses the Python Package Installer (pip3) to install the additional modules. You can pass additional pip3 options inside the `--additional-python-modules` value. For example, `"scikit-learn==0.21.3 -i https://pypi.python.org/simple/"`. Any incompatibilities or limitations from pip3 apply. ###### Note To avoid incompatibilities in the future, we recommend that you use libraries built for Python 3.9. ### Using an Egg or Whl file You might already have one or more Python libraries packaged as an `.egg` or a `.whl` file. If so, you can specify them to your job using the AWS Command Line Interface (AWS CLI) under the "`--extra-py-files`" flag, as in the following example. ``aws glue create-job --name python-redshift-test-cli --role `role` --command '{"Name" :  "pythonshell", "ScriptLocation" : "s3://MyBucket/python/library/redshift_test.py"}' --connections Connections=`connection-name` --default-arguments '{"--extra-py-files" : ["s3://amzn-s3-demo-bucket/EGG-FILE", "s3://amzn-s3-demo-bucket/WHEEL-FILE"]}'`` If you aren't sure how to create an `.egg` or a `.whl` file from a Python library, use the following steps. This example is applicable on macOS, Linux, and Windows Subsystem for Linux (WSL). ###### To create a Python .egg or .whl file 1. Create an Amazon Redshift cluster in a virtual private cloud (VPC), and add some data to a table. 2. Create an AWS Glue connection for the VPC-SecurityGroup-Subnet combination that you used to create the cluster. Test that the connection is successful. 3. Create a directory named `redshift_example`, and create a file named `setup.py`. Paste the following code into `setup.py`. `from setuptools import setup setup( name="redshift_module", version="0.1", packages=['redshift_module'] )` 4. In the `redshift_example` directory, create a `redshift_module` directory. In the `redshift_module` directory, create the files `__init__.py` and `pygresql_redshift_common.py`. 5. Leave the `__init__.py` file empty. In `pygresql_redshift_common.py`, paste the following code. Replace `port`, `db_name`, `user`, and `password_for_user` with details specific to your Amazon Redshift cluster. Replace `table_name` with the name of the table in Amazon Redshift. ``import pg def get_connection(host): rs_conn_string = "host=%s port=%s dbname=%s user=%s password=%s" % ( host, `port`, `db_name`, `user`, `password_for_user`) rs_conn = pg.connect(dbname=rs_conn_string) rs_conn.query("set statement_timeout = 1200000") return rs_conn def query(con): statement = "Select * from `table_name`;" res = con.query(statement) return res`` 6. If you're not already there, change to the `redshift_example` directory. 7. Do one of the following: <br>• To create an `.egg` file, run the following command. `python setup.py bdist_egg` <br>• To create a `.whl` file, run the following command. `python setup.py bdist_wheel` 8. Install the dependencies that are required for the preceding command. 9. The command creates a file in the `dist` directory: <br>• If you created an egg file, it's named `redshift_module-0.1-py2.7.egg`. <br>• If you created a wheel file, it's named `redshift_module-0.1-py2.7-none-any.whl`. Upload this file to Amazon S3. In this example, the uploaded file path is either `s3://amzn-s3-demo-bucket/EGG-FILE` or `s3://amzn-s3-demo-bucket/WHEEL-FILE`. 10. Create a Python file to be used as a script for the AWS Glue job, and add the following code to the file. ``from redshift_module import pygresql_redshift_common as rs_common con1 = rs_common.get_connection(`redshift_endpoint`) res = rs_common.query(con1) print "Rows in the table cities are: " print res`` 11. Upload the preceding file to Amazon S3. In this example, the uploaded file path is `s3://amzn-s3-demo-bucket/scriptname.py`. 12. Create a Python shell job using this script. On the AWS Glue console, on the **Job properties** page, specify the path to the `.egg/.whl` file in the **Python library path** box. If you have multiple `.egg/.whl` files and Python files, provide a comma-separated list in this box. When modifying or renaming `.egg` files, the file names must use the default names generated by the "python setup.py bdist_egg" command or must adhere to the Python module naming conventions. For more information, see the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/ "https://www.python.org/dev/peps/pep-0008/"). Using the AWS CLI, create a job with a command, as in the following example. `aws glue create-job --name python-redshift-test-cli --role Role --command '{"Name" :  "pythonshell", "ScriptLocation" : "s3://amzn-s3-demo-bucket/scriptname.py"}' --connections Connections="connection-name" --default-arguments '{"--extra-py-files" : ["s3://amzn-s3-demo-bucket/EGG-FILE", "s3://amzn-s3-demo-bucket/WHEEL-FILE"]}'` When the job runs, the script prints the rows created in the `table_name` table in the Amazon Redshift cluster. ## Use AWS CloudFormation with Python shell jobs in AWS Glue You can use AWS CloudFormation with Python shell jobs in AWS Glue. The following is an example: `AWSTemplateFormatVersion: 2010-09-09 Resources: Python39Job: Type: 'AWS::Glue::Job' Properties: Command: Name: pythonshell PythonVersion: '3.9' ScriptLocation: 's3://bucket/location' MaxRetries: 0 Name: python-39-job Role: RoleName` The Amazon CloudWatch Logs group for Python shell jobs output is `/aws-glue/python-jobs/output`. For errors, see the log group `/aws-glue/python-jobs/error`. ## Migrating from Python shell 3.6 to Python shell 3.9 To migrate your Python shell jobs to the latest AWS Glue version: 1. In the AWS Glue console ([https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/")), choose your existing Python shell job. 2. In the **Job** details tab, set the Python version to `Python 3.9` and choose **Save**. 3. Ensure that your job script is compatible with Python 3.9 and that it runs successfully. |
