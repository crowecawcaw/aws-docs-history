# Invoking DAGs with a Lambda function

The following code example uses an [AWS Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") function to get an Apache Airflow CLI
token and invoke a directed acyclic graph (DAG) in an Amazon MWAA environment.

###### Topics

- [Version](#samples-lambda-version "#samples-lambda-version")
- [Prerequisites](#samples-lambda-prereqs "#samples-lambda-prereqs")
- [Permissions](#samples-lambda-permissions "#samples-lambda-permissions")
- [Dependencies](#samples-lambda-dependencies "#samples-lambda-dependencies")
- [Code example](#samples-lambda-code "#samples-lambda-code")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use this code example, you must:

- Use the [public network
  access mode](configuring-networking.md#webserver-options-public-network-onconsole "configuring-networking.md#webserver-options-public-network-onconsole") for your [Amazon MWAA environment](get-started.md "get-started.md").
- Have a [Lambda function](../../../lambda/latest/dg/lambda-python.md "../../../lambda/latest/dg/lambda-python.md") using the latest Python runtime.

###### Note

If the Lambda function and your Amazon MWAA environment are in the same VPC, you can use this
code on a private network. For this configuration, the Lambda function's execution role needs
permission to call the Amazon Elastic Compute Cloud (Amazon EC2) **CreateNetworkInterface** API
operation. You can provide this permission using the [`AWSLambdaVPCAccessExecutionRole`](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole$jsonEditor") AWS-managed policy.

## Permissions

To use the code example on this page, your Amazon MWAA environment's execution role needs
access to perform the `airflow:CreateCliToken` action. You can provide this
permission using the `AmazonMWAAAirflowCliAccess` AWS-managed policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "airflow:CreateCliToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, refer to [Apache Airflow CLI policy: AmazonMWAAAirflowCliAccess](access-policies.md#cli-access "access-policies.md#cli-access").

## Dependencies

To use this code example with Apache Airflow v2 and later, no additional dependencies are required. Use
[aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") to install Apache Airflow.

## Code example

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose your Lambda function from the **Functions** list.
3. On the function page, copy the following code and replace the following with the names of your resources:
   - `YOUR_ENVIRONMENT_NAME` – The name of your Amazon MWAA
     environment.
   - `YOUR_DAG_NAME` – The name of the DAG that you want to
     invoke.

```
import boto3
import http.client
import base64
import ast
mwaa_env_name = 'YOUR_ENVIRONMENT_NAME'
dag_name = 'YOUR_DAG_NAME'
mwaa_cli_command = 'dags trigger'
​
client = boto3.client('mwaa')
​
def lambda_handler(event, context):
    # get web token
    mwaa_cli_token = client.create_cli_token(
        Name=mwaa_env_name
    )

    conn = http.client.HTTPSConnection(mwaa_cli_token['WebServerHostname'])
    payload = mwaa_cli_command + " " + dag_name
    headers = {
      'Authorization': 'Bearer ' + mwaa_cli_token['CliToken'],
      'Content-Type': 'text/plain'
    }
    conn.request("POST", "/aws_mwaa/cli", payload, headers)
    res = conn.getresponse()
    data = res.read()
    dict_str = data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    return base64.b64decode(mydata['stdout'])
```

4. Choose **Deploy**.
5. Choose **Test** to invoke your function using the Lambda console.
6. To verify that your Lambda successfully invoked your DAG, use the Amazon MWAA console to navigate to your environment's Apache Airflow UI, then do the following:
   1. On the **DAGs** page, locate your new target DAG in the list of DAGs.
   2. Under **Last Run**, check the timestamp for the latest DAG run. This timestamp should closely match the latest timestamp for
      `invoke_dag` in your other environment.
   3. Under **Recent Tasks**, check that the last run was successful.
