# Migrate to a new Amazon MWAA environment

Explore the following steps to migrate your existing Apache Airflow workload to a new Amazon MWAA
environment. You can use these steps to migrate from an older version of Amazon MWAA to a new
version release, or migrate your self-managed Apache Airflow deployment to Amazon MWAA. This tutorial
assumes you are migrating from an existing Apache Airflow v1.10.12 to a new Amazon MWAA running Apache Airflow v2.5.1, but
you can use the same procedures to migrate from, or to different Apache Airflow versions.

###### Topics

- [Prerequisites](#migrating-to-new-mwaa-prerequisites "#migrating-to-new-mwaa-prerequisites")
- [Step one: Create a new Amazon MWAA environment running the latest supported Apache Airflow version](#migrating-to-new-mwaa-create-a-new-environment "#migrating-to-new-mwaa-create-a-new-environment")
- [Step two: Migrate your workflow resources](#migrating-to-new-mwaa-workflows "#migrating-to-new-mwaa-workflows")
- [Step three: Exporting the metadata from your existing environment](#migrating-to-new-mwaa-exporting-metadatadb "#migrating-to-new-mwaa-exporting-metadatadb")
- [Step four: Importing the metadata to your new environment](#migrating-to-new-mwaa-importing-metadatadb "#migrating-to-new-mwaa-importing-metadatadb")
- [Next steps](#migrating-to-new-mwaa-next-up "#migrating-to-new-mwaa-next-up")

## Prerequisites

To be able to complete the steps and migrate your environment, you'll need the following:

- An Apache Airflow deployment. This can be a self-managed or existing Amazon MWAA environment.
- [Docker installed](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") for your local operating system.
- [AWS Command Line Interface version 2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") installed.

## Step one: Create a new Amazon MWAA environment running the latest supported Apache Airflow version

You can create an environment using the detailed steps in [Getting started with Amazon MWAA](../userguide/get-started.md "../userguide/get-started.md")
in the _Amazon MWAA User Guide_, or by using an AWS CloudFormation template. If you're migrating from an existing Amazon MWAA environment, and used an AWS CloudFormation template to create your old environment, you can change the
`AirflowVersion` property to specify the new version.

```
MwaaEnvironment:
  Type: AWS::MWAA::Environment
  DependsOn: MwaaExecutionPolicy
  Properties:
    Name: !Sub "${AWS::StackName}-MwaaEnvironment"
    SourceBucketArn: !GetAtt EnvironmentBucket.Arn
    ExecutionRoleArn: !GetAtt MwaaExecutionRole.Arn
    AirflowVersion: `2.5.1`
    DagS3Path: dags
  NetworkConfiguration:
    SecurityGroupIds:
      - !GetAtt SecurityGroup.GroupId
    SubnetIds:
      - !Ref PrivateSubnet1
      - !Ref PrivateSubnet2
  WebserverAccessMode: PUBLIC_ONLY
  MaxWorkers: !Ref MaxWorkerNodes
  LoggingConfiguration:
    DagProcessingLogs:
      LogLevel: !Ref DagProcessingLogs
      Enabled: true
    SchedulerLogs:
      LogLevel: !Ref SchedulerLogsLevel
      Enabled: true
    TaskLogs:
      LogLevel: !Ref TaskLogsLevel
      Enabled: true
    WorkerLogs:
      LogLevel: !Ref WorkerLogsLevel
      Enabled: true
    WebserverLogs:
      LogLevel: !Ref WebserverLogsLevel
      Enabled: true
```

Alternatively, if migrating from an existing Amazon MWAA environment, you can copy the following Python script that uses the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html")
to clone your environment. You can also [download the script](../userguide/samples/clone_environment.md "../userguide/samples/clone_environment.md").

```
# This Python file uses the following encoding: utf-8
'''
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from __future__ import print_function
import argparse
import json
import socket
import time
import re
import sys
from datetime import timedelta
from datetime import datetime
import boto3
from botocore.exceptions import ClientError, ProfileNotFound
from boto3.session import Session
ENV_NAME = ""
REGION = ""

def verify_boto3(boto3_current_version):
    '''
    check if boto3 version is valid, must be 1.17.80 and up
    return true if all dependenceis are valid, false otherwise
    '''
    valid_starting_version = '1.17.80'
    if boto3_current_version == valid_starting_version:
        return True
    ver1 = boto3_current_version.split('.')
    ver2 = valid_starting_version.split('.')
    for i in range(max(len(ver1), len(ver2))):
        num1 = int(ver1[i]) if i < len(ver1) else 0
        num2 = int(ver2[i]) if i < len(ver2) else 0
        if num1 > num2:
            return True
        elif num1 < num2:
            return False
    return False


def get_account_id(env_info):
    '''
    Given the environment metadata, fetch the account id from the
    environment ARN
    '''
    return env_info['Arn'].split(":")[4]


def validate_envname(env_name):
    '''
    verify environment name doesn't have path to files or unexpected input
    '''
    if re.match(r"^[a-zA-Z][0-9a-zA-Z-_]*$", env_name):
        return env_name
    raise argparse.ArgumentTypeError("%s is an invalid environment name value" % env_name)


def validation_region(input_region):
    '''
    verify environment name doesn't have path to files or unexpected input
    REGION: example is us-east-1
    '''
    session = Session()
    mwaa_regions = session.get_available_regions('mwaa')
    if input_region in mwaa_regions:
        return input_region
    raise argparse.ArgumentTypeError("%s is an invalid REGION value" % input_region)


def validation_profile(profile_name):
    '''
    verify profile name doesn't have path to files or unexpected input
    '''
    if re.match(r"^[a-zA-Z0-9]*$", profile_name):
        return profile_name
    raise argparse.ArgumentTypeError("%s is an invalid profile name value" % profile_name)

def validation_version(version_name):
    '''
    verify profile name doesn't have path to files or unexpected input
    '''
    if re.match(r"[1-2].\d.\d", version_name):
        return version_name
    raise argparse.ArgumentTypeError("%s is an invalid version name value" % version_name)

def validation_execution_role(execution_role_arn):
    '''
    verify profile name doesn't have path to files or unexpected input
    '''
    if re.match(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', execution_role_arn):
        return execution_role_arn
    raise argparse.ArgumentTypeError("%s is an invalid execution role ARN" % execution_role_arn)

def create_new_env(env):
    '''
    method to duplicate env
    '''
    mwaa = boto3.client('mwaa', region_name=REGION)

    print('Source Environment')
    print(env)
    if (env['AirflowVersion']=="1.10.12") and (VERSION=="2.2.2"):
        if env['AirflowConfigurationOptions']['secrets.backend']=='airflow.contrib.secrets.aws_secrets_manager.SecretsManagerBackend':
            print('swapping',env['AirflowConfigurationOptions']['secrets.backend'])
            env['AirflowConfigurationOptions']['secrets.backend']='airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend'
    env['LoggingConfiguration']['DagProcessingLogs'].pop('CloudWatchLogGroupArn')
    env['LoggingConfiguration']['SchedulerLogs'].pop('CloudWatchLogGroupArn')
    env['LoggingConfiguration']['TaskLogs'].pop('CloudWatchLogGroupArn')
    env['LoggingConfiguration']['WebserverLogs'].pop('CloudWatchLogGroupArn')
    env['LoggingConfiguration']['WorkerLogs'].pop('CloudWatchLogGroupArn')
    env['AirflowVersion']=VERSION
    env['ExecutionRoleArn']=EXECUTION_ROLE_ARN
    env['Name']=ENV_NAME_NEW
    env.pop('Arn')
    env.pop('CreatedAt')
    env.pop('LastUpdate')
    env.pop('ServiceRoleArn')
    env.pop('Status')
    env.pop('WebserverUrl')
    if not env['Tags']:
        env.pop('Tags')
    print('Destination Environment')
    print(env)

    return mwaa.create_environment(**env)

def get_mwaa_env(input_env_name):

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.get_environment
    mwaa = boto3.client('mwaa', region_name=REGION)
    environment = mwaa.get_environment(
        Name=input_env_name
    )['Environment']

    return environment

def print_err_msg(c_err):
    '''short method to handle printing an error message if there is one'''
    print('Error Message: {}'.format(c_err.response['Error']['Message']))
    print('Request ID: {}'.format(c_err.response['ResponseMetadata']['RequestId']))
    print('Http code: {}'.format(c_err.response['ResponseMetadata']['HTTPStatusCode']))

#
# Main
#
# Usage:
# python3 clone_environment.py --envname MySourceEnv --envnamenew MyDestEnv --region us-west-2 --execution_role AmazonMWAA-MyDestEnv-ExecutionRole --version 2.2.2
#
# based on https://github.com/awslabs/aws-support-tools/blob/master/MWAA/verify_env/verify_env.py
#

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print("python2 detected, please use python3. Will try to run anyway")
    if not verify_boto3(boto3.__version__):
        print("boto3 version ", boto3.__version__, "is not valid for this script. Need 1.17.80 or higher")
        print("please run pip install boto3 --upgrade --user")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument('--envname', type=validate_envname, required=True, help="name of the source MWAA environment")
    parser.add_argument('--region', type=validation_region, default=boto3.session.Session().region_name,
                        required=False, help="region, Ex: us-east-1")
    parser.add_argument('--profile', type=validation_profile, default=None,
                        required=False, help="AWS CLI profile, Ex: dev")
    parser.add_argument('--version', type=validation_version, default="2.2.2",
                        required=False, help="Airflow destination version, Ex: 2.2.2")
    parser.add_argument('--execution_role', type=validation_execution_role, default=None,
                        required=True, help="New environment execution role ARN, Ex: arn:aws:iam::112233445566:role/service-role/AmazonMWAA-MyEnvironment-ExecutionRole")
    parser.add_argument('--envnamenew', type=validate_envname, required=True, help="name of the destination MWAA environment")

    args, _ = parser.parse_known_args()
    ENV_NAME = args.envname
    REGION = args.region
    PROFILE = args.profile
    VERSION = args.version
    EXECUTION_ROLE_ARN = args.execution_role
    ENV_NAME_NEW = args.envnamenew

    try:
        print("PROFILE",PROFILE)
        if PROFILE:
            boto3.setup_default_session(profile_name=PROFILE)
        env = get_mwaa_env(ENV_NAME)
        response = create_new_env(env)
        print(response)
    except ClientError as client_error:
        if client_error.response['Error']['Code'] == 'LimitExceededException':
            print_err_msg(client_error)
            print('please retry the script')
        elif client_error.response['Error']['Code'] in ['AccessDeniedException', 'NotAuthorized']:
            print_err_msg(client_error)
            print('please verify permissions used have permissions documented in readme')
        elif client_error.response['Error']['Code'] == 'InternalFailure':
            print_err_msg(client_error)
            print('please retry the script')
        else:
            print_err_msg(client_error)
    except ProfileNotFound as profile_not_found:
        print('profile', PROFILE, 'does not exist; check the profile name')
    except IndexError as error:
        print("Error:", error)


```

## Step two: Migrate your workflow resources

Apache Airflow v2 is a major version release. If you are migrating from Apache Airflow v1, you must prepare your workflow resources and verify the changes you make to your DAGs, requirements, and plugins. To do so,
we recommend configuring a _bridge_ version of Apache Airflow on your local operating system using Docker and the [Amazon MWAA local runner](https://github.com/aws/aws-mwaa-local-runner "https://github.com/aws/aws-mwaa-local-runner").
The Amazon MWAA local runner provides a command line interface (CLI) utility that replicates an Amazon MWAA environment locally.

Whenever you're changing Apache Airflow versions, ensure that you [reference the correct `--constraint`](../userguide/working-dags-dependencies.md#working-dags-dependencies-test-create "../userguide/working-dags-dependencies.md#working-dags-dependencies-test-create")
URL in your `requirements.txt`.

###### To migrate your workflow resources

1. Create a fork of the [aws-mwaa-local-runner](https://github.com/aws/aws-mwaa-local-runner "https://github.com/aws/aws-mwaa-local-runner") repository, and clone a copy of the Amazon MWAA local runner.
2. Checkout the `v1.10.15` branch of the aws-mwaa-local-runner repository. Apache Airflow released v1.10.15 as a _bridge release_ to assist in migrating to Apache Airflow v2, and although Amazon MWAA does not
   support v1.10.15, you can use the Amazon MWAA local runner to test your resources.
3. Use the Amazon MWAA local runner CLI tool to build the Docker image and run Apache Airflow locally. For more information, see the local runner
   [README](https://github.com/aws/aws-mwaa-local-runner/tree/v1.10.15#readme "https://github.com/aws/aws-mwaa-local-runner/tree/v1.10.15#readme") in the GitHub repository.
4. Using Apache Airflow running locally, follow the steps described in [Upgrading from 1.10 to 2](https://airflow.apache.org/docs/apache-airflow/stable/upgrading-from-1-10/index.html "https://airflow.apache.org/docs/apache-airflow/stable/upgrading-from-1-10/index.html") in the Apache Airflow documentation website.
   1. To update your `requirements.txt`, follow the best practices we recommend in
      [Managing Python dependencies](../userguide/best-practices-dependencies.md "../userguide/best-practices-dependencies.md"), in the _Amazon MWAA User Guide_.
   2. If you have bundled your custom operators and sensors with your plugins for your existing Apache Airflow v1.10.12 environment, move them to your DAG folder. For more information on module management best practices for Apache Airflow v2+,
      refer to [Module Management](https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html "https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html") in the Apache Airflow documentation website.

5. After you have made the required changes to your workflow resources, checkout the `v2.5.1` branch of the aws-mwaa-local-runner repository, and test your updated workflow DAGs, requirements, and custom plugins
   locally. If you're migrating to a different Apache Airflow version, you can use the appropriate local runner branch for your version, instead.
6. After you have successfully tested your workflow resources, copy your DAGs, `requirements.txt`, and plugins to the Amazon S3 bucket you configured with your new Amazon MWAA environment.

## Step three: Exporting the metadata from your existing environment

Apache Airflow metadata tables such as `dag`, `dag_tag`, and `dag_code` automatically populate when you copy the updated DAG files to your environment's Amazon S3 bucket and the scheduler parses them.
Permission related tables also populate automatically based on your IAM execution role permission. You do not need to migrate them.

You can migrate data related to DAG history, `variable`, `slot_pool`, `sla_miss`, and if needed, `xcom`, `job`, and `log` tables.
Task instance log is stored in the CloudWatch Logs under the `airflow-`{environment_name}`` log group. If you want to see the task instance logs for older runs,
those logs must be copied over to the new environment log group. We recommend that you move only a few days worth of logs in order to reduce associated costs.

If you're migrating from an existing Amazon MWAA environment, there is no direct access to the metadata database. You must run a DAG to export the metadata from your existing Amazon MWAA environment to an Amazon S3 bucket of your choice.
The following steps can also be used to export Apache Airflow metadata if you're migrating from a self-managed environment.

After the data is exported, you can then run a DAG in your new environment to import the data. During the export and the import process, all other DAGs are paused.

###### To export the metadata from your existing environment

1. Create an Amazon S3 bucket using the AWS CLI to store the exported data. Replace the `UUID` and `region` with your information.

```
`aws s3api create-bucket \
--bucket mwaa-migration-`{UUID}`\
--region `{region}``
```

###### Note

If you are migrating sensitive data, such as connections you store in variables, we recommend that you
[enable default encryption](../../../AmazonS3/latest/userguide/default-bucket-encryption.md "../../../AmazonS3/latest/userguide/default-bucket-encryption.md") for the Amazon S3 bucket. 2. ###### Note

Does not apply to migration from a self-managed environment.

Modify the execution role of the existing environment and add the following policy to grant write access to the bucket you created in step one.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject*"
 ],
 "Resource": [
 "arn:aws:s3:::mwaa-migration-`{UUID}`/*"
 ]
 }
 ]
}`

```

3. Clone the [amazon-mwaa-examples](https://github.com/aws-samples/amazon-mwaa-examples "https://github.com/aws-samples/amazon-mwaa-examples") repository, and navigate to the `metadata-migration` subdirectory for your migration scenario.

```
`git clone https://github.com/aws-samples/amazon-mwaa-examples.git`
`cd amazon-mwaa-examples/usecases/metadata-migration/`existing-version`-`new-version`/`
```

4. In `export_data.py`, replace the string value for `S3_BUCKET` with the Amazon S3 bucket you created to store exported metadata.

```
S3_BUCKET = 'mwaa-migration-`{UUID}`'
```

5. Locate the `requirements.txt` file in the `metadata-migration` directory. If you already have a requirements file for your existing environment,
   add the additional requirements specified in `requirements.txt` to your file. If you do not have an existing requirements file, you can simply use the one provided
   in the `metadata-migration` directory.
6. Copy `export_data.py` to the DAG directory of the Amazon S3 bucket associated with your existing environment. If migrating from a self-managed environment, copy `export_data.py`
   to your `/dags` folder.
7. Copy your updated `requirements.txt` to the Amazon S3 bucket associated with your existing environment, then edit the environment to specify the new `requirements.txt` version.
8. After the environment is updated, access the Apache Airflow UI, unpause the `db_export` DAG, and trigger the workflow to run.
9. Verify that the metadata is exported to `data/migration/`existing-version`_to_`new-version`/export/` in the `mwaa-migration-`{UUID}`` Amazon S3 bucket,
   with each table in it's own dedicated file.

## Step four: Importing the metadata to your new environment

###### To import the metadata to your new environment

1. In `import_data.py`, replace the string values for the following with your information.
   - For migration from an existing Amazon MWAA environment:

   ```
   S3_BUCKET = 'mwaa-migration-`{UUID}`'
   							OLD_ENV_NAME='`{old_environment_name}`'
   							NEW_ENV_NAME='`{new_environment_name}`'
   							TI_LOG_MAX_DAYS = `{number_of_days}`
   ```

   `MAX_DAYS` controls how many days worth of log files the workflow copies over to the new
   environment.
   - For migration from a self-managed environment:

   ```
   S3_BUCKET = 'mwaa-migration-`{UUID}`'
   							NEW_ENV_NAME='`{new_environment_name}`'
   ```

2. (Optional) `import_data.py` copies only failed task logs. If you want to copy all task logs, modify the `getDagTasks` function, and remove `ti.state = 'failed'`
   as shown in the following code snippet.

```
def getDagTasks():
					session = settings.Session()
					dagTasks = session.execute(f"select distinct ti.dag_id, ti.task_id, date(r.execution_date) as ed \
					from task_instance ti, dag_run r where r.execution_date > current_date - {TI_LOG_MAX_DAYS} and \
					ti.dag_id=r.dag_id and ti.run_id = r.run_id order by ti.dag_id, date(r.execution_date);").fetchall()
					return dagTasks
```

3. Modify the execution role of your new environment and add the following policy. The permission policy allows Amazon MWAA to read from the Amazon S3 bucket where you exported the Apache Airflow metadata, and to copy
   task instance logs from existing log groups. Replace all placeholders with your information.

###### Note

If you are migrating from a self-managed environment, you must remove CloudWatch Logs related permissions from the
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:GetLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:airflow-`{old_environment_name}`*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::mwaa-migration-`{UUID}`",
 "arn:aws:s3:::mwaa-migration-`{UUID}`/*"
 ]
 }
 ]
}`

```

4. Copy `import_data.py` to the DAG directory of the Amazon S3 bucket associated with your new environment,
   then access the Apache Airflow UI to unpause the `db_import` DAG and trigger the workflow. The new DAG will appear in the Apache Airflow UI in a few minutes.
5. After the DAG run completes, verify that your DAG run history is copied over by accessing each individual DAG.

## Next steps

- For more information about available Amazon MWAA environment classes and capabilities, refer to [Amazon MWAA environment class](../userguide/environment-class.md "../userguide/environment-class.md") in the
  _Amazon MWAA User Guide_.
- For more information about how Amazon MWAA handles autoscaling workers, refer to [Amazon MWAA automatic scaling](../userguide/mwaa-autoscaling.md "../userguide/mwaa-autoscaling.md") in the
  _Amazon MWAA User Guide_.
- For more information about the Amazon MWAA REST API, refer to the [Amazon MWAA REST API](../API/Welcome.md "../API/Welcome.md").
