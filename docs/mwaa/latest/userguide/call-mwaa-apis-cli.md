# Creating an Apache Airflow CLI token

###### Tip

REST API is more modern than the CLI and is designed for programmatic integration with external systems. REST is the preferred way of interacting with Apache Airflow.

You can use the commands on this page to generate a CLI token, and then make Amazon Managed Workflows for Apache Airflow API calls directly in your command shell. For example, you can get a token, then deploy DAGs programmatically using Amazon MWAA APIs. The following section includes the steps to create an Apache Airflow CLI token using the AWS CLI, a curl script, a Python script, or a bash script. The token returned in the response is valid for 60 seconds.

The AWS CLI token is intended as a replacement for synchronous shell actions, not asynchronous API commands. As such, available concurrency is limited. To ensure that the webserver remains responsive for users, we recommend not opening a new AWS CLI request until the previous one completes successfully.

###### Contents

- [Prerequisites](call-mwaa-apis-cli.md#call-mwaa-apis-cli-prereqs "call-mwaa-apis-cli.md#call-mwaa-apis-cli-prereqs")
  - [Access](call-mwaa-apis-cli.md#access-airflow-ui-prereqs-access "call-mwaa-apis-cli.md#access-airflow-ui-prereqs-access")
  - [AWS CLI](call-mwaa-apis-cli.md#access-airflow-ui-prereqs-cli "call-mwaa-apis-cli.md#access-airflow-ui-prereqs-cli")

- [Using the AWS CLI](call-mwaa-apis-cli.md#create-cli-token-cli "call-mwaa-apis-cli.md#create-cli-token-cli")
- [Using a curl script](call-mwaa-apis-cli.md#create-cli-token-curl "call-mwaa-apis-cli.md#create-cli-token-curl")
- [Using a bash script](call-mwaa-apis-cli.md#create-cli-token-bash "call-mwaa-apis-cli.md#create-cli-token-bash")
- [Using a Python script](call-mwaa-apis-cli.md#create-cli-token-python "call-mwaa-apis-cli.md#create-cli-token-python")
- [What's next?](call-mwaa-apis-cli.md#mwaa-cli-next-up "call-mwaa-apis-cli.md#mwaa-cli-next-up")

## Prerequisites

The following section describes the preliminary steps required to use the commands and scripts on this page.

### Access

- AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy in [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access "access-policies.md#web-ui-access").
- AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy [Full API and console access policy: AmazonMWAAFullApiAccess](access-policies.md#full-access-policy "access-policies.md#full-access-policy").

### AWS CLI

The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:

- [AWS CLI – Install version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").
- [AWS CLI – Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

## Using the AWS CLI

The following example uses the [create-cli-token](../../../cli/latest/reference/mwaa/create-cli-token.md "../../../cli/latest/reference/mwaa/create-cli-token.md") command in the AWS CLI to create an Apache Airflow CLI token.

```
aws mwaa create-cli-token --name `YOUR_ENVIRONMENT_NAME`
```

## Using a curl script

The following example uses a curl script to call the [create-web-login-token](../../../cli/latest/reference/mwaa/create-cli-token.md "../../../cli/latest/reference/mwaa/create-cli-token.md") command in the AWS CLI to invoke the Apache Airflow CLI through an endpoint on the Apache Airflow webserver.

Apache Airflow v3

1. Copy the curl statement from your text file and paste it in your command shell.

###### Note

After copying it to your clipboard, you might need to use **Edit > Paste** from your shell menu.

```
CLI_JSON=$(aws mwaa --region `us-east-1` create-cli-token --name `YOUR_ENVIRONMENT_NAME`) \
&& CLI_TOKEN=$(echo $CLI_JSON | jq -r '.CliToken') \
&& WEB_SERVER_HOSTNAME=$(echo $CLI_JSON | jq -r '.WebServerHostname') \
&& CLI_RESULTS=$(curl -L --request POST "https://$WEB_SERVER_HOSTNAME/aws_mwaa/cli" \
--header "Authorization: Bearer $CLI_TOKEN" \
--header "Content-Type: text/plain" \
--data-raw "dags trigger YOUR_DAG_NAME --logical-date $(date -u +"%Y-%m-%dT%H:%M:%SZ")") \
&& echo "Output:" \
&& echo $CLI_RESULTS | jq -r '.stdout' | base64 --decode \
&& echo "Errors:" \
&& echo $CLI_RESULTS | jq -r '.stderr' | base64 --decode
```

2. Substitute the placeholders in `red` for the AWS Region for your environment, `YOUR_DAG_NAME`, and `YOUR_ENVIRONMENT_NAME`.
   For example, a host name for a public network resembles (without the _https://)_:

```
123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com
```

Your command prompt displays:

```
{
  "stderr":"<STDERR of the CLI execution (if any), base64 encoded>",
  "stdout":"<STDOUT of the CLI execution, base64 encoded>"
}
```

Apache Airflow v2

1. Copy the curl statement from your text file and paste it in your command shell.

###### Note

After copying it to your clipboard, you might need to use **Edit > Paste** from your shell menu.

```
CLI_JSON=$(aws mwaa --region `us-east-1` create-cli-token --name `YOUR_ENVIRONMENT_NAME`) \
&& CLI_TOKEN=$(echo $CLI_JSON | jq -r '.CliToken') \
&& WEB_SERVER_HOSTNAME=$(echo $CLI_JSON | jq -r '.WebServerHostname') \
&& CLI_RESULTS=$(curl --request POST "https://$WEB_SERVER_HOSTNAME/aws_mwaa/cli" \
--header "Authorization: Bearer $CLI_TOKEN" \
--header "Content-Type: text/plain" \
--data-raw "dags trigger `YOUR_DAG_NAME`") \
&& echo "Output:" \
&& echo $CLI_RESULTS | jq -r '.stdout' | base64 --decode \
&& echo "Errors:" \
&& echo $CLI_RESULTS | jq -r '.stderr' | base64 --decode
```

2. Substitute the placeholders in `red` for the AWS Region for your environment, `YOUR_DAG_NAME`, and `YOUR_ENVIRONMENT_NAME`. For example, a host name for a public network resembles (without the _https://)_:

```
123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com
```

Your command prompt displays:

```
{
  "stderr":"<STDERR of the CLI execution (if any), base64 encoded>",
  "stdout":"<STDOUT of the CLI execution, base64 encoded>"
}
```

## Using a bash script

The following example uses a bash script to call the [create-cli-token](../../../cli/latest/reference/mwaa/create-cli-token.md "../../../cli/latest/reference/mwaa/create-cli-token.md") command in the AWS CLI to create an Apache Airflow CLI token.

Apache Airflow v3

1. Copy the contents of the following code sample and save locally as
   `get-cli-token.sh`.

```
# brew install jq
								aws mwaa create-cli-token --name `YOUR_ENVIRONMENT_NAME` | export CLI_TOKEN=$(jq -r .CliToken) && curl -L --request POST "https://`YOUR_HOST_NAME`/aws_mwaa/cli" \
								--header "Authorization: Bearer $CLI_TOKEN" \
								--header "Content-Type: text/plain" \
								--data-raw "dags trigger `YOUR_DAG_NAME` --logical-date $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
```

2. Substitute the placeholders in `red` for `YOUR_ENVIRONMENT_NAME`,
   `YOUR_HOST_NAME`, and `YOUR_DAG_NAME`. For example, a host name for a public
   network resembles (without the _https://)_:

```
123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com
```

3. (optional) macOS and Linux users might need to run the following command to ensure the script is executable.

```
chmod +x get-cli-token.sh
```

4. Run the following script to create an Apache Airflow CLI token.

```
./get-cli-token.sh
```

Apache Airflow v2

1. Copy the contents of the following code sample and save locally as `get-cli-token.sh`.

```
# brew install jq
aws mwaa create-cli-token --name `YOUR_ENVIRONMENT_NAME` | export CLI_TOKEN=$(jq -r .CliToken) && curl --request POST "https://`YOUR_HOST_NAME`/aws_mwaa/cli" \
--header "Authorization: Bearer $CLI_TOKEN" \
--header "Content-Type: text/plain" \
--data-raw "dags trigger `YOUR_DAG_NAME`"
```

2. Substitute the placeholders in `red` for `YOUR_ENVIRONMENT_NAME`, `YOUR_HOST_NAME`, and `YOUR_DAG_NAME`. For example, a host name for a public network resembles (without the _https://)_:

```
123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com
```

3. (optional) macOS and Linux users can run the following command to ensure the script is executable.

```
chmod +x get-cli-token.sh
```

4. Run the following script to create an Apache Airflow CLI token.

```
./get-cli-token.sh
```

## Using a Python script

The following example uses the [boto3 create_cli_token](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_cli_token "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_cli_token") method in a Python script to create an Apache Airflow CLI token and trigger a DAG. You can run this script outside of Amazon MWAA. The only thing you need to do is install the boto3 library. You might want to create a virtual environment to install the library. It assumes you have [configured AWS authentication credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration") for your account.

Apache Airflow v3

1. Copy the contents of the following code sample and save locally as `create-cli-token.py`.

```
"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import boto3
import json
import requests
import base64

mwaa_env_name = 'YOUR_ENVIRONMENT_NAME'
dag_name = 'YOUR_DAG_NAME'
mwaa_cli_command = 'dags trigger'

client = boto3.client('mwaa')

mwaa_cli_token = client.create_cli_token(
    Name=mwaa_env_name
)

mwaa_auth_token = 'Bearer ' + mwaa_cli_token['CliToken']
mwaa_webserver_hostname = 'https://{0}/aws_mwaa/cli'.format(mwaa_cli_token['WebServerHostname'])
raw_data = '{0} {1}'.format(mwaa_cli_command, dag_name)

mwaa_response = requests.post(
        mwaa_webserver_hostname,
        headers={
            'Authorization': mwaa_auth_token,
            'Content-Type': 'text/plain'
            },
        data=raw_data
        )

mwaa_std_err_message = base64.b64decode(mwaa_response.json()['stderr']).decode('utf8')
mwaa_std_out_message = base64.b64decode(mwaa_response.json()['stdout']).decode('utf8')

print(mwaa_response.status_code)
print(mwaa_std_err_message)
print(mwaa_std_out_message)
```

2. Substitute the placeholders for `YOUR_ENVIRONMENT_NAME` and `YOUR_DAG_NAME`.
3. Run the following script to create an Apache Airflow CLI token.

```
python3 create-cli-token.py
```

Apache Airflow v2

1. Copy the contents of the following code sample and save locally as `create-cli-token.py`.

```
"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import boto3
import json
import requests
import base64

mwaa_env_name = 'YOUR_ENVIRONMENT_NAME'
dag_name = 'YOUR_DAG_NAME'
mwaa_cli_command = 'dags trigger'

client = boto3.client('mwaa')

mwaa_cli_token = client.create_cli_token(
    Name=mwaa_env_name
)

mwaa_auth_token = 'Bearer ' + mwaa_cli_token['CliToken']
mwaa_webserver_hostname = 'https://{0}/aws_mwaa/cli'.format(mwaa_cli_token['WebServerHostname'])
raw_data = '{0} {1}'.format(mwaa_cli_command, dag_name)

mwaa_response = requests.post(
        mwaa_webserver_hostname,
        headers={
            'Authorization': mwaa_auth_token,
            'Content-Type': 'text/plain'
            },
        data=raw_data
        )

mwaa_std_err_message = base64.b64decode(mwaa_response.json()['stderr']).decode('utf8')
mwaa_std_out_message = base64.b64decode(mwaa_response.json()['stdout']).decode('utf8')

print(mwaa_response.status_code)
print(mwaa_std_err_message)
print(mwaa_std_out_message)
```

2. Substitute the placeholders for `YOUR_ENVIRONMENT_NAME` and `YOUR_DAG_NAME`.
3. Run the following script to create an Apache Airflow CLI token.

```
python3 create-cli-token.py
```

## What's next?

- Explore the Amazon MWAA API operation used to create a CLI token at [CreateCliToken](../API/API_CreateCliToken.md "../API/API_CreateCliToken.md").
