# Using Python libraries with AWS Glue

You can install additional Python modules and libraries for use with AWS Glue ETL. For AWS Glue 2.0 and above, AWS Glue uses the Python Package Installer (pip3)
to install additional modules used by AWS Glue ETL. AWS Glue provides multiple options to bring the additional Python modules to your AWS Glue job environment.
You can use the “—additional-python-modules" parameter to bring in modules using Python wheel files, Requirements file (requirement.txt,
AWS Glue 5.0 and above), or a list of comma-separated Python modules.

###### Topics

- [Installing additional Python modules with pip in AWS Glue 2.0 or later](#addl-python-modules-support "#addl-python-modules-support")
- [Including Python files with PySpark native features](#extra-py-files-support "#extra-py-files-support")
- [Programming scripts that use visual transforms](#aws-glue-programming-with-cvt "#aws-glue-programming-with-cvt")
- [Zipping libraries for inclusion](#aws-glue-programming-python-libraries-zipping "#aws-glue-programming-python-libraries-zipping")
- [Loading Python libraries in AWS Glue Studio notebooks](#aws-glue-programming-python-libraries-notebooks "#aws-glue-programming-python-libraries-notebooks")
- [Loading Python libraries in a development endpoint in AWS Glue 0.9/1.0](#aws-glue-programming-python-libraries-dev-endpoint "#aws-glue-programming-python-libraries-dev-endpoint")
- [Using Python libraries in a job or JobRun](#aws-glue-programming-python-libraries-job "#aws-glue-programming-python-libraries-job")
- [Proactively analyze Python dependencies](#aws-glue-programming-analyzing-python-dependencies "#aws-glue-programming-analyzing-python-dependencies")
- [Python modules already provided in AWS Glue](#glue-modules-provided "#glue-modules-provided")

| Glue Version Compatibility and Installation Methods | AWS Glue version | Python version                                                                                                                  | Base image | glibc version |
| --------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------- |
| 5.1                                                 | 3.11             | [Amazon Linux 2023 (AL2023)](https://aws.amazon.com/linux/amazon-linux-2023/ "https://aws.amazon.com/linux/amazon-linux-2023/") | 2.34       |
| 5.0                                                 | 3.11             | [Amazon Linux 2023 (AL2023)](https://aws.amazon.com/linux/amazon-linux-2023/ "https://aws.amazon.com/linux/amazon-linux-2023/") | 2.34       |
| 4.0                                                 | 3.10             | [Amazon Linux 2 (AL2)](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/")                         | 2.26       |
| 3.0                                                 | 3.7              | [Amazon Linux 2 (AL2)](https://aws.amazon.com/amazon-linux-2/ "https://aws.amazon.com/amazon-linux-2/")                         | 2.26       |
| 2.0                                                 | 3.7              | [Amazon Linux AMI (AL1)](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/")                   | 2.17       |
| 1.0                                                 | 3.6              | [Amazon Linux AMI (AL1)](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/")                   | 2.17       |
| 0.9                                                 | 2.7              | [Amazon Linux AMI (AL1)](https://aws.amazon.com/amazon-linux-ami/ "https://aws.amazon.com/amazon-linux-ami/")                   | 2.17       |

Under the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), you are responsible for the management of additional Python modules, libraries, and their dependencies
that you use with your AWS Glue ETL jobs. This includes applying updates and security patches.

AWS Glue does not support compiling native code in the job environment. However, AWS Glue jobs run within an Amazon-managed Linux environment.
You may be able to provide your native dependencies in a compiled form through a Python wheel file. Please refer to above table for AWS Glue version
compatibility details.

If your Python dependencies transitively depend on native, compiled code, you may run against the following limitation: AWS Glue does not support
compiling native code in the job environment. However, AWS Glue jobs run within an Amazon-managed Linux environment. You may be able to provide your
native dependencies in a compiled form through a wheel distribution. Please refer to above table for AWS Glue version compatibility details.

###### Important

Using incompatible dependencies can result in runtime issues, particularly for libraries with native extensions that must match the target
environment's architecture and system libraries. Each AWS Glue version runs on a specific Python version with pre-installed libraries and system
configurations.

## Installing additional Python modules with pip in AWS Glue 2.0 or later

AWS Glue uses the Python Package Installer (pip3) to install additional modules to be used by
AWS Glue ETL. You can use the `--additional-python-modules` parameter with a list of
comma-separated Python modules to add a new module or change the version of an existing module. You can install
custom distributions of a library by uploading the distribution to Amazon S3, then include the path to the Amazon S3 object
in your list of modules.

You can pass additional options to pip3 with the `--python-modules-installer-option` parameter. For
example, you could pass `"--upgrade"` to upgrade the packages specified by
`"--additional-python-modules"`. For more examples, see [Building Python modules from a wheel for Spark ETL workloads using AWS Glue 2.0](https://aws.amazon.com/blogs/big-data/building-python-modules-from-a-wheel-for-spark-etl-workloads-using-aws-glue-2-0/ "https://aws.amazon.com/blogs/big-data/building-python-modules-from-a-wheel-for-spark-etl-workloads-using-aws-glue-2-0/") .

AWS Glue supports installing custom Python packages using wheel (.whl) files stored in Amazon S3. To include wheel files in your AWS Glue jobs,
provide a comma-separated list of your wheel files stored in s3 to the `--additional-python-modules` job parameter.
For example:

```
--additional-python-modules s3://amzn-s3-demo-bucket/path/to/package-1.0.0-py3-none-any.whl,s3://your-bucket/path/to/another-package-2.1.0-cp311-cp311-linux_x86_64.whl
```

This approach also supports when you need custom distributions, or packages with native dependencies that are pre-compiled for the correct
operating system. For more examples, see
[Building Python modules from a wheel for Spark ETL workloads using AWS Glue 2.0](https://aws.amazon.com/blogs/big-data/building-python-modules-from-a-wheel-for-spark-etl-workloads-using-aws-glue-2-0/ "https://aws.amazon.com/blogs/big-data/building-python-modules-from-a-wheel-for-spark-etl-workloads-using-aws-glue-2-0/").

You specify the `--additional-python-modules` in the Job parameters field of the AWS Glue console or by altering the job arguments in
the AWS SDK. For more information about setting job parameters, see
[Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md").

In AWS Glue 5.0, you can provide the defacto-standard `requirements.txt` to manage Python library dependencies.
To do that, provide following two job parameters:

- Key: `--python-modules-installer-option`

Value: `-r`

- Key: `--additional-python-modules`

Value: `s3://path_to_requirements.txt`
AWS Glue 5.0 nodes initially load python libraries specified in `requirements.txt`.

Here's a sample requirements.txt:

```
awswrangler==3.9.1
elasticsearch==8.15.1
PyAthena==3.9.0
PyMySQL==1.1.1
PyYAML==6.0.2
pyodbc==5.2.0
pyorc==0.9.0
redshift-connector==2.1.3
scipy==1.14.1
scikit-learn==1.5.2
SQLAlchemy==2.0.36
```

###### Important

Please avoid unpinned library versions in your requirements.txt to ensure you have a reliable and deterministic AWS Glue environment
for your jobs.

When you use wheel for direct dependencies, you can bring in incompatible version of your transitive dependencies if they are not pinned correctly.
As a best practice, all library versions should be pinned for consistency in AWS Glue jobs. AWS Glue recommends packaging your python environment into a
wheel file to ensure consistency and reliability for your production workload.

To update or to add a new Python module AWS Glue allows passing `--additional-python-modules` parameter with a list of comma-separated
Python modules as values. For example to update/ add scikit-learn module use the following key/value: `"--additional-python-modules", 
 "scikit-learn==0.21.3"`. You have two options to directly configure the python modules.

- **Pinned Python Module (recommended)**

`"--additional-python-modules", "scikit-learn==0.21.3,ephem==4.1.6"`

- **Unpinned Python Module: (Not recommended for Production Workloads)**

`"--additional-python-modules", "scikit-learn>==0.20.0,ephem>=4.0.0"`

OR

`"--additional-python-modules", "scikit-learn,ephem"`

###### Important

When configuring the python modules directly in `--additional-python-modules`, AWS Glue recommends to use pinned library versions
to ensure consistency in AWS Glue job environment. Using unpinned library versions, pulls the latest version of the python modules, however this can
introduce breaking changes or bring in incompatible python module leading to job failure due to python installation failure in AWS Glue job environment.
We recommend customers to not use unpinned library versions for production workload. As a best practice, AWS Glue recommends packaging your
python environment into a wheel file to ensure consistency and reliability for your production workload.

## Including Python files with PySpark native features

AWS Glue uses PySpark to include Python files in AWS Glue ETL jobs. You will want to use
`--additional-python-modules` to manage your dependencies when available. You can use the
`--extra-py-files` job parameter to include Python files. Dependencies must be hosted in Amazon S3 and the
argument value should be a comma delimited list of Amazon S3 paths with no spaces. This functionality behaves like the
Python dependency management you would use with Spark. For more information on Python dependency management in
Spark, see [Using PySpark Native Features](https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-pyspark-native-features "https://spark.apache.org/docs/latest/api/python/tutorial/python_packaging.html#using-pyspark-native-features") page in Apache Spark documentation. `--extra-py-files` is useful
in cases where your additional code is not packaged, or when you are migrating a Spark program with an existing
toolchain for managing dependencies. For your dependency tooling to be maintainable, you will
have to bundle your dependencies before submitting.

## Programming scripts that use visual transforms

When you create a AWS Glue job using the AWS Glue Studio visual interface, you can transform your data with managed data
transform nodes and custom visual transforms. For more information about managed data transform nodes, see [Transform data with AWS Glue managed transforms](edit-jobs-transforms.md "edit-jobs-transforms.md"). For more information about custom visual transforms, see [Transform data with custom visual transforms](custom-visual-transform.md "custom-visual-transform.md") . Scripts using visual transforms can only be generated when your job
**Language** is set to use Python.

When generating a AWS Glue job using visual transforms, AWS Glue Studio will include these transforms in the runtime
environment using the `--extra-py-files` parameter in the job configuration. For more information about
job parameters, see [Using job parameters in AWS Glue jobs](aws-glue-programming-etl-glue-arguments.md "aws-glue-programming-etl-glue-arguments.md"). When making changes to a generated
script or runtime environment, you will need to preserve this job configuration for your script to run
successfully.

## Zipping libraries for inclusion

Unless a library is contained in a single `.py` file, it should be
packaged in a `.zip` archive. The package directory should be at the root
of the archive, and must contain an `__init__.py` file for the package.
Python will then be able to import the package in the normal way.

If your library only consists of a single Python module in one `.py`
file, you do not need to place it in a `.zip` file.

## Loading Python libraries in AWS Glue Studio notebooks

To specify Python libraries in AWS Glue Studio notebooks, see
[Installing additional Python modules.](manage-notebook-sessions.md#specify-default-modules "manage-notebook-sessions.md#specify-default-modules")

## Loading Python libraries in a development endpoint in AWS Glue 0.9/1.0

If you are using different library sets for different ETL scripts,
you can either set up a separate development endpoint for each set,
or you can overwrite the library `.zip` file(s) that your
development endpoint loads every time you switch scripts.

You can use the console to specify one or more library .zip files for
a development endpoint when you create it. After assigning a name and
an IAM role, choose **Script Libraries and job parameters
(optional)** and enter the full Amazon S3 path to your library
`.zip` file in the **Python library path** box.
For example:

```
s3://`bucket`/`prefix/`site-packages.zip
```

If you want, you can specify multiple full paths to files, separating them
with commas but no spaces, like this:

```
s3://bucket/prefix/lib_A.zip,s3://bucket_B/prefix/lib_X.zip
```

If you update these `.zip` files later, you can use the console
to re-import them into your development endpoint. Navigate to the developer
endpoint in question, check the box beside it, and choose **Update
ETL libraries** from the **Action** menu.

In a similar way, you can specify library files using the AWS Glue APIs.
When you create a development endpoint by calling [CreateDevEndpoint action (Python: create_dev_endpoint)](aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-CreateDevEndpoint "aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-CreateDevEndpoint"),
you can specify one or more full paths to libraries in the `ExtraPythonLibsS3Path`
parameter, in a call that looks this:

```

dep = glue.create_dev_endpoint(
             EndpointName="`testDevEndpoint`",
             RoleArn="`arn:aws:iam::123456789012`",
             SecurityGroupIds="`sg-7f5ad1ff`",
             SubnetId="`subnet-c12fdba4`",
             PublicKey="`ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtp04H/y...`",
             NumberOfNodes=`3`,
             ExtraPythonLibsS3Path="`s3://bucket/prefix/lib_A.zip,s3://bucket_B/prefix/lib_X.zip`")
```

When you update a development endpoint, you can also update the libraries it loads
using a [DevEndpointCustomLibraries](aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-DevEndpointCustomLibraries "aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-DevEndpointCustomLibraries") object
and setting the `UpdateEtlLibraries` parameter to `True`
when calling [UpdateDevEndpoint (update_dev_endpoint)](aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-UpdateDevEndpoint "aws-glue-api-dev-endpoint.md#aws-glue-api-dev-endpoint-UpdateDevEndpoint").

## Using Python libraries in a job or JobRun

When you are creating a new Job on the console, you can specify one or more library .zip files
by choosing **Script Libraries and job parameters (optional)** and entering
the full Amazon S3 library path(s) in the same way you would when creating a development endpoint:

```
s3://bucket/prefix/lib_A.zip,s3://bucket_B/prefix/lib_X.zip
```

If you are calling [CreateJob (create_job)](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-CreateJob"),
you can specify one or more full paths to default libraries using the `--extra-py-files`
default parameter, like this:

```
job = glue.create_job(Name='`sampleJob`',
                      Role='`Glue_DefaultRole`',
                      Command={'Name': 'glueetl',
                               'ScriptLocation': '`s3://my_script_bucket/scripts/my_etl_script.py`'},
                      DefaultArguments={'--extra-py-files': '`s3://bucket/prefix/lib_A.zip,s3://bucket_B/prefix/lib_X.zip`'})
```

Then when you are starting a JobRun, you can override the default library setting with a different one:

```
runId = glue.start_job_run(JobName='`sampleJob`',
                           Arguments={'--extra-py-files': '`s3://bucket/prefix/lib_B.zip`'})
```

## Proactively analyze Python dependencies

To proactively identify potential dependency issues before deploying to AWS Glue, you can use the dependency analysis tool to validate your Python
packages against your target AWS Glue environment.

AWS provides an open-source Python dependency analyzer tool specifically designed for AWS Glue environments. This tool is available in the AWS Glue samples
repository and can be used locally to validate your dependencies before deployment.

This analysis helps ensure your dependencies follow the recommended practice of pinning all library versions for consistent production deployments.
For more details, please see the tool's
[README](https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/glue_python_dependency_analyzer "https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/glue_python_dependency_analyzer") .

The AWS Glue Python Dependency Analyzer helps identify unpinned dependencies and version conflicts by simulating pip installation with platform-specific
constraints that match your target AWS Glue environment.

```
# Analyze a single Glue job
python glue_dependency_analyzer.py -j my-glue-job

# Analyze multiple jobs with specific AWS configuration
python glue_dependency_analyzer.py -j job1 -j job2 --aws-profile production --aws-region us-west-2
```

The tool will flag:

- Unpinned dependencies that could install different versions across job runs
- Version conflicts between packages
- Dependencies not available for your target AWS Glue environment

Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant that can help you understand, build, extend, and operate AWS applications. You can download it by following the instructions in the Getting started guide for Amazon Q.

Amazon Q Developer can be used to analyze and fix job failures due to python dependency. We suggest using the following prompt by replacing the job <Job-Name> placeholder with the name of your glue job.

```
I have an AWS Glue job named <Job-Name> that has failed due to Python module installation conflicts. Please assist in diagnosing and resolving this issue using the following systematic approach. Proceed once sufficient information is available.

Objective: Implement a fix that addresses the root cause module while minimizing disruption to the existing working environment.

Step 1: Root Cause Analysis
• Retrieve the most recent failed job run ID for the specified Glue job
• Extract error logs from CloudWatch Logs using the job run ID as a log stream prefix
• Analyze the logs to identify:
  • The recently added or modified Python module that triggered the dependency conflict
  • The specific dependency chain causing the installation failure
  • Version compatibility conflicts between required and existing modules

Step 2: Baseline Configuration Identification
• Locate the last successful job run ID prior to the dependency failure
• Document the Python module versions that were functioning correctly in that baseline run
• Establish the compatible version constraints for conflicting dependencies

Step 3: Targeted Resolution Implementation
• Apply pinning by updating the job's additional_python_modules parameter
• Pin only the root cause module and its directly conflicting dependencies to compatible versions, and do not remove python modules unless necessary
• Preserve flexibility for non-conflicting modules by avoiding unnecessary version constraints
• Deploy the configuration changes with minimal changes to the existing configuration and execute a validation test run. Do not change the Glue versions.

Implementation Example:
Scenario: Recently added pandas==2.0.0 to additional_python_modules
Error: numpy version conflict (pandas 2.0.0 requires numpy>=1.21, but existing job code requires numpy<1.20)
Resolution: Update additional_python_modules to "pandas==1.5.3,numpy==1.19.5"
Rationale: Use pandas 1.5.3 (compatible with numpy 1.19.5) and pin numpy to last known working version

Expected Outcome: Restore job functionality with minimal configuration changes while maintaining system stability.
```

The prompt instructs Q to:

1. Fetch the latest failed job run ID
2. Find associated logs and details
3. Find successful job runs to detect any changed Python packages
4. Make any configuration fixes and trigger another test run

## Python modules already provided in AWS Glue

To change the version of these provided modules, provide new versions with the `--additional-python-modules` job parameter.

AWS Glue version 5.0
AWS Glue version 5.0 includes the following Python modules out of the box:

- aiobotocore==2.13.1
- aiohappyeyeballs==2.3.5
- aiohttp==3.10.1
- aioitertools==0.11.0
- aiosignal==1.3.1
- appdirs==1.4.4
- attrs==24.2.0
- boto3==1.34.131
- botocore==1.34.131
- certifi==2024.7.4
- charset-normalizer==3.3.2
- contourpy==1.2.1
- cycler==0.12.1
- fonttools==4.53.1
- frozenlist==1.4.1
- fsspec==2024.6.1
- idna==2.10
- jmespath==0.10.0
- kaleido==0.2.1
- kiwisolver==1.4.5
- matplotlib==3.9.0
- multidict==6.0.5
- numpy==1.26.4
- packaging==24.1
- pandas==2.2.2
- pillow==10.4.0
- pip==23.0.1
- plotly==5.23.0
- pyarrow==17.0.0
- pyparsing==3.1.2
- python-dateutil==2.9.0.post0
- pytz==2024.1
- requests==2.32.2
- s3fs==2024.6.1
- s3transfer==0.10.2
- seaborn==0.13.2
- setuptools==59.6.0
- six==1.16.0
- tenacity==9.0.0
- tzdata==2024.1
- urllib3==1.25.10
- virtualenv==20.4.0
- wrapt==1.16.0
- yarl==1.9.4

AWS Glue version 4.0
AWS Glue version 4.0 includes the following Python modules out of the box:

- aiobotocore==2.4.1
- aiohttp==3.8.3
- aioitertools==0.11.0
- aiosignal==1.3.1
- async-timeout==4.0.2
- asynctest==0.13.0
- attrs==22.2.0
- avro-python3==1.10.2
- boto3==1.24.70
- botocore==1.27.59
- certifi==2021.5.30
- chardet==3.0.4
- charset-normalizer==2.1.1
- click==8.1.3
- cycler==0.10.0
- Cython==0.29.32
- fsspec==2021.8.1
- idna==2.10
- importlib-metadata==5.0.0
- jmespath==0.10.0
- joblib==1.0.1
- kaleido==0.2.1
- kiwisolver==1.4.4
- matplotlib==3.4.3
- mpmath==1.2.1
- multidict==6.0.4
- nltk==3.7
- numpy==1.23.5
- packaging==23.0
- pandas==1.5.1
- patsy==0.5.1
- Pillow==9.4.0
- pip==23.0.1
- plotly==5.16.0
- pmdarima==2.0.1
- ptvsd==4.3.2
- pyarrow==10.0.0
- pydevd==2.5.0
- pyhocon==0.3.58
- PyMySQL==1.0.2
- pyparsing==2.4.7
- python-dateutil==2.8.2
- pytz==2021.1
- PyYAML==6.0.1
- regex==2022.10.31
- requests==2.23.0
- s3fs==2022.11.0
- s3transfer==0.6.0
- scikit-learn==1.1.3
- scipy==1.9.3
- setuptools==49.1.3
- six==1.16.0
- statsmodels==0.13.5
- subprocess32==3.5.4
- sympy==1.8
- tbats==1.1.0
- threadpoolctl==3.1.0
- tqdm==4.64.1
- typing_extensions==4.4.0
- urllib3==1.25.11
- wheel==0.37.0
- wrapt==1.14.1
- yarl==1.8.2
- zipp==3.10.0

AWS Glue version 3.0
AWS Glue version 3.0 includes the following Python modules out of the box:,

- aiobotocore==1.4.2
- aiohttp==3.8.3
- aioitertools==0.11.0
- aiosignal==1.3.1
- async-timeout==4.0.2
- asynctest==0.13.0
- attrs==22.2.0
- avro-python3==1.10.2
- boto3==1.18.50
- botocore==1.21.50
- certifi==2021.5.30
- chardet==3.0.4
- charset-normalizer==2.1.1
- click==8.1.3
- cycler==0.10.0
- Cython==0.29.4
- docutils==0.17.1
- enum34==1.1.10
- frozenlist==1.3.3
- fsspec==2021.8.1
- idna==2.10
- importlib-metadata==6.0.0
- jmespath==0.10.0
- joblib==1.0.1
- kiwisolver==1.3.2
- matplotlib==3.4.3
- mpmath==1.2.1
- multidict==6.0.4
- nltk==3.6.3
- numpy==1.19.5
- packaging==23.0
- pandas==1.3.2
- patsy==0.5.1
- Pillow==9.4.0
- pip==23.0
- pmdarima==1.8.2
- ptvsd==4.3.2
- pyarrow==5.0.0
- pydevd==2.5.0
- pyhocon==0.3.58
- PyMySQL==1.0.2
- pyparsing==2.4.7
- python-dateutil==2.8.2
- pytz==2021.1
- PyYAML==5.4.1
- regex==2022.10.31
- requests==2.23.0
- s3fs==2021.8.1
- s3transfer==0.5.0
- scikit-learn==0.24.2
- scipy==1.7.1
- six==1.16.0
- Spark==1.0
- statsmodels==0.12.2
- subprocess32==3.5.4
- sympy==1.8
- tbats==1.1.0
- threadpoolctl==3.1.0
- tqdm==4.64.1
- typing_extensions==4.4.0
- urllib3==1.25.11
- wheel==0.37.0
- wrapt==1.14.1
- yarl==1.8.2
- zipp==3.12.0

AWS Glue version 2.0
AWS Glue version 2.0 includes the following Python modules out of the box:

- avro-python3==1.10.0
- awscli==1.27.60
- boto3==1.12.4
- botocore==1.15.4
- certifi==2019.11.28
- chardet==3.0.4
- click==8.1.3
- colorama==0.4.4
- cycler==0.10.0
- Cython==0.29.15
- docutils==0.15.2
- enum34==1.1.9
- fsspec==0.6.2
- idna==2.9
- importlib-metadata==6.0.0
- jmespath==0.9.4
- joblib==0.14.1
- kiwisolver==1.1.0
- matplotlib==3.1.3
- mpmath==1.1.0
- nltk==3.5
- numpy==1.18.1
- pandas==1.0.1
- patsy==0.5.1
- pmdarima==1.5.3
- ptvsd==4.3.2
- pyarrow==0.16.0
- pyasn1==0.4.8
- pydevd==1.9.0
- pyhocon==0.3.54
- PyMySQL==0.9.3
- pyparsing==2.4.6
- python-dateutil==2.8.1
- pytz==2019.3
- PyYAML==5.3.1
- regex==2022.10.31
- requests==2.23.0
- rsa==4.7.2
- s3fs==0.4.0
- s3transfer==0.3.3
- scikit-learn==0.22.1
- scipy==1.4.1
- setuptools==45.2.0
- six==1.14.0
- Spark==1.0
- statsmodels==0.11.1
- subprocess32==3.5.4
- sympy==1.5.1
- tbats==1.0.9
- tqdm==4.64.1
- typing-extensions==4.4.0
- urllib3==1.25.8
- wheel==0.35.1
- zipp==3.12.0
