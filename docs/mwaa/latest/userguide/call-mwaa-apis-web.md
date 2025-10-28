# Create a Apache Airflow webserver access token

You can use the commands on this page to create a web server access token. An access token provides access to your Amazon MWAA environment. For example, you can get a token, then deploy DAGs programmatically using Amazon MWAA APIs. The following section includes the steps to create an Apache Airflow web login token using the AWS CLI, a bash script, a POST API request, or a Python script. The token returned in the response is valid for 60 seconds.

###### Important

Effective August 19, 2025, Amazon MWAA added support for IPv6 endpoints, and now supports IPv4 and IPv6 endpoints. As of this date, all newly created environments will use `.on.aws` domains for the Airflow user interface (UI). Customers must migrate their Airflow UI from `.amazonaws.com` to `.on.aws` domains for these newly created environments. Virtual Private Cloud (VPC) endpoint services for webserver and database will maintain their current `.amazonaws.com` domains with no required changes.

###### Contents

- [Prerequisites](call-mwaa-apis-web.md#call-mwaa-apis-web-prereqs "call-mwaa-apis-web.md#call-mwaa-apis-web-prereqs")
  - [Access](call-mwaa-apis-web.md#access-airflow-ui-prereqs-access "call-mwaa-apis-web.md#access-airflow-ui-prereqs-access")
  - [AWS CLI](call-mwaa-apis-web.md#access-airflow-ui-prereqs-cli "call-mwaa-apis-web.md#access-airflow-ui-prereqs-cli")

- [Using the AWS CLI](call-mwaa-apis-web.md#create-web-login-token-cli "call-mwaa-apis-web.md#create-web-login-token-cli")
- [Using a bash script](call-mwaa-apis-web.md#create-web-login-token-bash "call-mwaa-apis-web.md#create-web-login-token-bash")
- [Using a Python script](call-mwaa-apis-web.md#create-web-login-token-python "call-mwaa-apis-web.md#create-web-login-token-python")
- [What's next?](call-mwaa-apis-web.md#mwaa-webcli-next-up "call-mwaa-apis-web.md#mwaa-webcli-next-up")

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

The following example uses the [create-web-login-token](../../../cli/latest/reference/mwaa/create-web-login-token.md "../../../cli/latest/reference/mwaa/create-web-login-token.md") command in the AWS CLI to create an Apache Airflow web login token.

```
aws mwaa create-web-login-token --name `YOUR_ENVIRONMENT_NAME`
```

## Using a bash script

The following example uses a bash script to call the [create-web-login-token](../../../cli/latest/reference/mwaa/create-web-login-token.md "../../../cli/latest/reference/mwaa/create-web-login-token.md") command in the AWS CLI to create an Apache Airflow web login token.

1. Copy the contents of the following code sample and save locally as `get-web-token.sh`.

```
#!/bin/bash
HOST=`YOUR_HOST_NAME`
YOUR_URL=https://$HOST/aws_mwaa/aws-console-sso?login=true#
WEB_TOKEN=$(aws mwaa create-web-login-token --name `YOUR_ENVIRONMENT_NAME` --query WebToken --output text)
echo $YOUR_URL$WEB_TOKEN
```

2. Substitute the placeholders in `red` for `YOUR_HOST_NAME` and `YOUR_ENVIRONMENT_NAME`. For example, a host name for a public network resembles (without the _https://)_:

```
123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com
```

3. (optional) macOS and Linux users might need to run the following command to ensure the script is executable.

```
chmod +x get-web-token.sh
```

4. Run the following script to get a web login token.

```
./get-web-token.sh
```

Your command prompt displays:

```
https://123456a0-0101-2020-9e11-1b159eec9000.c2.`us-east-1`.airflow.amazonaws.com/aws_mwaa/aws-console-sso?login=true#`{your-web-login-token}`
```

## Using a Python script

The following example uses the [boto3 create_web_login_token](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_web_login_token "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_web_login_token") method in a Python script to create an Apache Airflow web login token. You can run this script outside of Amazon MWAA. The only thing you need to do is install the boto3 library. You might want to create a virtual environment to install the library. It assumes you have [configured AWS authentication credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration") for your account.

1. Copy the contents of the following code sample and save locally as `create-web-login-token.py`.

```
import boto3
  mwaa = boto3.client('mwaa')
  response = mwaa.create_web_login_token(
    Name="`YOUR_ENVIRONMENT_NAME`"
  )
  webServerHostName = response["WebServerHostname"]
  webToken = response["WebToken"]
  airflowUIUrl = 'https://{0}/aws_mwaa/aws-console-sso?login=true#{1}'.format(webServerHostName, webToken)
  print("Here is your Airflow UI URL: ")
  print(airflowUIUrl)
```

2. Substitute the placeholder in `red` for `YOUR_ENVIRONMENT_NAME`.
3. Run the following script to get a web login token.

```
python3 create-web-login-token.py
```

## What's next?

- Explore the Amazon MWAA API operation used to create a web login token at [CreateWebLoginToken](../API/API_CreateWebLoginToken.md "../API/API_CreateWebLoginToken.md").
