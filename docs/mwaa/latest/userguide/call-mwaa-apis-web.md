

# Create a Apache Airflow webserver access token
<a name="call-mwaa-apis-web"></a>

You can use the commands on this page to create a web server access token. An access token provides access to your Amazon MWAA environment. For example, you can get a token, then deploy DAGs programmatically using Amazon MWAA APIs. The following section includes the steps to create an Apache Airflow web login token using the AWS CLI, a bash script, a POST API request, or a Python script. The token returned in the response is valid for 60 seconds.

**Important**  
Effective August 19, 2025, Amazon MWAA added support for IPv6 endpoints, and now supports IPv4 and IPv6 endpoints. As of this date, all newly created environments will use `.on.aws` domains for the Airflow user interface (UI). Customers must migrate their Airflow UI from `.amazonaws.com` to `.on.aws` domains for these newly created environments. Virtual Private Cloud (VPC) endpoint services for webserver and database will maintain their current `.amazonaws.com` domains with no required changes.

**Contents**
+ [Prerequisites](#call-mwaa-apis-web-prereqs)
  + [Access](#access-airflow-ui-prereqs-access)
  + [AWS CLI](#access-airflow-ui-prereqs-cli)
+ [Using the AWS CLI](#create-web-login-token-cli)
+ [Using a bash script](#create-web-login-token-bash)
+ [Using a Python script](#create-web-login-token-python)
+ [What's next?](#mwaa-webcli-next-up)

## Prerequisites
<a name="call-mwaa-apis-web-prereqs"></a>

The following section describes the preliminary steps required to use the commands and scripts on this page.

### Access
<a name="access-airflow-ui-prereqs-access"></a>
+ AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy in [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access).
+ AWS account access in AWS Identity and Access Management (IAM) to the Amazon MWAA permissions policy [Full API and console access policy: AmazonMWAAFullApiAccess](access-policies.md#full-access-policy).

### AWS CLI
<a name="access-airflow-ui-prereqs-cli"></a>

The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:
+ [AWS CLI – Install version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
+ [AWS CLI – Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

## Using the AWS CLI
<a name="create-web-login-token-cli"></a>

The following example uses the [create-web-login-token](https://docs.aws.amazon.com/cli/latest/reference/mwaa/create-web-login-token.html) command in the AWS CLI to create an Apache Airflow web login token.

```
aws mwaa create-web-login-token --name {{YOUR_ENVIRONMENT_NAME}}
```

## Using a bash script
<a name="create-web-login-token-bash"></a>

The following example uses a bash script to call the [create-web-login-token](https://docs.aws.amazon.com/cli/latest/reference/mwaa/create-web-login-token.html) command in the AWS CLI to create an Apache Airflow web login token.

1. Copy the contents of the following code sample and save locally as `get-web-token.sh`.

   ```
   #!/bin/bash
   HOST={{YOUR_HOST_NAME}}
   YOUR_URL=https://$HOST/aws_mwaa/aws-console-sso?login=true#
   WEB_TOKEN=$(aws mwaa create-web-login-token --name {{YOUR_ENVIRONMENT_NAME}} --query WebToken --output text)
   echo $YOUR_URL$WEB_TOKEN
   ```

1. Substitute the placeholders in {{red}} for `YOUR_HOST_NAME` and `YOUR_ENVIRONMENT_NAME`. For example, a host name for a public network resembles (without the *https://)*:

   ```
   123456a0-0101-2020-9e11-1b159eec9000.c2.{{us-east-1}}.airflow.amazonaws.com
   ```

1. (optional) macOS and Linux users might need to run the following command to ensure the script is executable.

   ```
   chmod +x get-web-token.sh
   ```

1. Run the following script to get a web login token.

   ```
   ./get-web-token.sh
   ```

   Your command prompt displays:

   ```
   https://123456a0-0101-2020-9e11-1b159eec9000.c2.{{us-east-1}}.airflow.amazonaws.com/aws_mwaa/aws-console-sso?login=true#{{{your-web-login-token}}}
   ```

## Using a Python script
<a name="create-web-login-token-python"></a>

The following example uses the [boto3 create\_web\_login\_token](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA.Client.create_web_login_token) method in a Python script to create an Apache Airflow web login token. You can run this script outside of Amazon MWAA. The only thing you need to do is install the boto3 library. You might want to create a virtual environment to install the library. It assumes you have [configured AWS authentication credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) for your account.

1. Copy the contents of the following code sample and save locally as `create-web-login-token.py`.

   ```
   import boto3
     mwaa = boto3.client('mwaa')
     response = mwaa.create_web_login_token(
       Name="{{YOUR_ENVIRONMENT_NAME}}"
     )
     webServerHostName = response["WebServerHostname"]
     webToken = response["WebToken"]
     airflowUIUrl = 'https://{0}/aws_mwaa/aws-console-sso?login=true#{1}'.format(webServerHostName, webToken)
     print("Here is your Airflow UI URL: ")
     print(airflowUIUrl)
   ```

1. Substitute the placeholder in {{red}} for `YOUR_ENVIRONMENT_NAME`.

1. Run the following script to get a web login token.

   ```
   python3 create-web-login-token.py
   ```

## What's next?
<a name="mwaa-webcli-next-up"></a>
+ Explore the Amazon MWAA API operation used to create a web login token at [CreateWebLoginToken](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateWebLoginToken.html).