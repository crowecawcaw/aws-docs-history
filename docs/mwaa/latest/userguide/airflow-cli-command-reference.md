

# Apache Airflow CLI command reference
<a name="airflow-cli-command-reference"></a>

This topic describes the supported and unsupported Apache Airflow CLI commands on Amazon Managed Workflows for Apache Airflow.

**Tip**  
REST API is more modern than the CLI and is designed for programmatic integration with external systems. REST is the preferred way of interacting with Apache Airflow.

**Contents**
+ [Prerequisites](#airflow-cli-command-prereqs)
  + [Access](#access-airflow-ui-prereqs-access)
  + [AWS CLI](#access-airflow-ui-prereqs-cli)
+ [What changed?](#airflow-cli-command-changed)
+ [Supported CLI commands](#airflow-cli-commands)
  + [Supported commands](#airflow-cli-commands-supported)
  + [Using commands that parse DAGs](#parsing-support)
+ [Sample code](#airflow-cli-command-examples)
  + [Set, get or delete an Apache Airflow v2 variable](#example-airflow-cli-commands-bash)
  + [Add a configuration when triggering a DAG](#example-airflow-cli-commands-trigger)
  + [Run CLI commands on an SSH tunnel to a bastion host](#example-airflow-cli-commands-private)

## Prerequisites
<a name="airflow-cli-command-prereqs"></a>

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

## What changed?
<a name="airflow-cli-command-changed"></a>
+ **v3: Airflow architecture**. Apache Airflow v3 introduces breaking architectural changes to provide improved security and scalability, and to make maintainance easier. To learn more, refer to [Upgrading To Airflow 3](https://airflow.apache.org/docs/apache-airflow/stable/installation/upgrading_to_airflow3.html).
+ **v2: Airflow CLI command structure**. The Apache Airflow v2 CLI is organized so that related commands are grouped together as subcommands, which means you need to update Apache Airflow v1 scripts if you want to upgrade to Apache Airflow v2. For example, `unpause` in Apache Airflow v1 is `dags unpause` in Apache Airflow v2. To learn more, refer to [Airflow CLI changes in 2.0](http://airflow.apache.org/docs/apache-airflow/2.0.2/upgrading-to-2.html#airflow-cli-changes-in-2-0).

## Supported CLI commands
<a name="airflow-cli-commands"></a>

The following section lists the Apache Airflow CLI commands available on Amazon MWAA.

### Supported commands
<a name="airflow-cli-commands-supported"></a>

------
#### [ Apache Airflow v3 ]


| Minor versions | Command | 
| --- | --- | 
| v3.0.6, v3.2.1, v3.3.1 | [assets details](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#details) | 
| v3.0.6, v3.2.1, v3.3.1 | [assets list](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#list) | 
| v3.0.6, v3.2.1, v3.3.1 | [assets materialize](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#materialize) | 
| v3.0.6, v3.2.1, v3.3.1 | [backfill create](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#create) | 
| v3.0.6, v3.2.1, v3.3.1 | [cheat-sheet](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#cheat-sheet) | 
| v3.0.6, v3.2.1, v3.3.1 | [connections add](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#add) | 
| v3.0.6, v3.2.1, v3.3.1 | [connections delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete_repeat1) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat2) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags list-jobs](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list-jobs) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags list-import-errors](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#list-import-errors) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags list-runs](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list-runs) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags next-execution](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#next-execution) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags pause](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#pause) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags report](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#report) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags reserialize](https://airflow.apache.org/docs/apache-airflow/2.4.3/cli-and-env-variables-ref.html#reserialize) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags show](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#show) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags state](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#state) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags test](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#test) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags trigger](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#trigger) | 
| v3.0.6, v3.2.1, v3.3.1 | [dags unpause](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#unpause) | 
| v3.0.6, v3.2.1, v3.3.1 | [db clean](https://airflow.apache.org/docs/apache-airflow/2.4.3/cli-and-env-variables-ref.html#clean) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers behaviours](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#behaviours) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers get](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#get_repeat2) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers hooks](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#hooks) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers links](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#links) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat4) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers notifications](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#notifications) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers secrets](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#secrets) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers triggerer](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#triggerer) | 
| v3.0.6, v3.2.1, v3.3.1 | [providers widgets](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#widgets) | 
| v3.0.6, v3.2.1, v3.3.1 | [roles add-perms](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#add-perms) | 
| v3.0.6, v3.2.1, v3.3.1 | [roles del-perms](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#del-perms) | 
| v3.0.6, v3.2.1, v3.3.1 | [roles create](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#create) | 
| v3.0.6, v3.2.1, v3.3.1 | [roles list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat5) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks clear](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#clear) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks failed-deps](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#failed-deps) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat6) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks render](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#render) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks state](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#state_repeat1) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks states-for-dag-run](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#states-for-dag-run) | 
| v3.0.6, v3.2.1, v3.3.1 | [tasks test](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#test_repeat1) | 
| v3.0.6, v3.2.1, v3.3.1 | [variables delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete_repeat4) | 
| v3.0.6, v3.2.1, v3.3.1 | [variables get](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#get_repeat3) | 
| v3.0.6, v3.2.1, v3.3.1 | [variables set](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#set_repeat1) | 
| v3.0.6, v3.2.1, v3.3.1 | [variables list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat8) | 
| v3.0.6, v3.2.1, v3.3.1 | [version](http://airflow.apache.org/docs/apache-airflow/1.10.12/cli-ref.html#version) | 

------
#### [ Apache Airflow v2 ]


| Minor versions | Command | 
| --- | --- | 
| v2.0\+ | [cheat-sheet](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#cheat-sheet) | 
| v2.0\+ | [connections add](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#add) | 
| v2.0\+ | [connections delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete) | 
| v2.2\+ ([note](#parsing-support)) | [dags backfill](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#backfill) | 
| v2.0\+ | [dags delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete_repeat1) | 
| v2.2\+ ([note](#parsing-support)) | [dags list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat2) | 
| v2.0\+ | [dags list-jobs](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list-jobs) | 
| v2.6\+ | [dags list-import-errors](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#list-import-errors) | 
| v2.2\+ ([note](#parsing-support)) | [dags list-runs](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list-runs) | 
| v2.2\+ ([note](#parsing-support)) | [dags next-execution](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#next-execution) | 
| v2.0\+ | [dags pause](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#pause) | 
| v2.0\+ | [dags report](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#report) | 
| v2.4\+ | [dags reserialize](https://airflow.apache.org/docs/apache-airflow/2.4.3/cli-and-env-variables-ref.html#reserialize) | 
| v2.0\+ | [dags show](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#show) | 
| v2.0\+ | [dags state](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#state) | 
| v2.0\+ | [dags test](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#test) | 
| v2.0\+ | [dags trigger](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#trigger) | 
| v2.0\+ | [dags unpause](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#unpause) | 
| v2.4\+ | [db clean](https://airflow.apache.org/docs/apache-airflow/2.4.3/cli-and-env-variables-ref.html#clean) | 
| v2.0\+ | [providers behaviours](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#behaviours) | 
| v2.0\+ | [providers get](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#get_repeat2) | 
| v2.0\+ | [providers hooks](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#hooks) | 
| v2.0\+ | [providers links](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#links) | 
| v2.0\+ | [providers list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat4) | 
| v2.8\+ | [providers notifications](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#notifications) | 
| v2.6\+ | [providers secrets](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#secrets) | 
| v2.7\+ | [providers triggerer](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#triggerer) | 
| v2.0\+ | [providers widgets](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#widgets) | 
| v2.6\+ | [roles add-perms](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#add-perms) | 
| v2.6\+ | [roles del-perms](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#del-perms) | 
| v2.6\+ | [roles create](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#create) | 
| v2.0\+ | [roles list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat5) | 
| v2.0\+ | [tasks clear](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#clear) | 
| v2.0\+ | [tasks failed-deps](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#failed-deps) | 
| v2.0\+ | [tasks list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat6) | 
| v2.0\+ | [tasks render](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#render) | 
| v2.0\+ | [tasks run](https://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#run) | 
| v2.0\+ | [tasks state](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#state_repeat1) | 
| v2.0\+ | [tasks states-for-dag-run](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#states-for-dag-run) | 
| v2.0\+ | [tasks test](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#test_repeat1) | 
| v2.0\+ | [variables delete](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#delete_repeat4) | 
| v2.0\+ | [variables get](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#get_repeat3) | 
| v2.0\+ | [variables set](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#set_repeat1) | 
| v2.0\+ | [variables list](http://airflow.apache.org/docs/apache-airflow/2.2.2/cli-and-env-variables-ref.html#list_repeat8) | 
| v2.0\+ | [version](http://airflow.apache.org/docs/apache-airflow/1.10.12/cli-ref.html#version) | 

------

### Using commands that parse DAGs
<a name="parsing-support"></a>

If your environment is running Apache Airflow v2.0.2, CLI commands that parse DAGs will fail if the DAG uses plugins that depend on packages installed through a `requirements.txt`:

**Apache Airflow v2.0.2**
+ `dags backfill`
+ `dags list`
+ `dags list-runs`
+ `dags next-execution`

You can use these CLI commands if your DAGs do not use plugins that depend on packages installed through a `requirements.txt`.

## Sample code
<a name="airflow-cli-command-examples"></a>

The following section contains examples of different ways to use the Apache Airflow CLI.

### Set, get or delete an Apache Airflow v2 variable
<a name="example-airflow-cli-commands-bash"></a>

You can use the following sample code to set, get or delete a variable in the format of `<script> <mwaa env name> get | set | delete <variable> <variable value> </variable> </variable>`.

```
[ $# -eq 0 ] && echo "Usage: $0 MWAA environment name " && exit

if [[ $2 == "" ]]; then
    dag="variables list"

elif  [ $2 == "get" ] ||  [ $2 == "delete" ] ||  [ $2 == "set" ]; then
    dag="variables $2 $3 $4 $5"

else
    echo "Not a valid command"
    exit 1
fi

CLI_JSON=$(aws mwaa --region $AWS_REGION create-cli-token --name $1) \
    && CLI_TOKEN=$(echo $CLI_JSON | jq -r '.CliToken') \
    && WEB_SERVER_HOSTNAME=$(echo $CLI_JSON | jq -r '.WebServerHostname') \
    && CLI_RESULTS=$(curl --request POST "https://$WEB_SERVER_HOSTNAME/aws_mwaa/cli" \
    --header "Authorization: Bearer $CLI_TOKEN" \
    --header "Content-Type: text/plain" \
    --data-raw "$dag" ) \
    && echo "Output:" \
    && echo $CLI_RESULTS | jq -r '.stdout' | base64 --decode \
    && echo "Errors:" \
    && echo $CLI_RESULTS | jq -r '.stderr' | base64 --decode
```

### Add a configuration when triggering a DAG
<a name="example-airflow-cli-commands-trigger"></a>

You can use the following sample code with Apache Airflow v2 to add a configuration when triggering a DAG, such as `airflow trigger_dag 'dag_name' —conf '{"key":"value"}'`.

```
import boto3
import json
import requests 
import base64
				
  mwaa_env_name = '{{YOUR_ENVIRONMENT_NAME}}'
  dag_name = '{{YOUR_DAG_NAME}}'
  key = "{{YOUR_KEY}}"
  value = "{{YOUR_VALUE}}"
  conf = "{\"" + key + "\":\"" + value + "\"}"
				
  client = boto3.client('mwaa')
				
  mwaa_cli_token = client.create_cli_token(
    Name=mwaa_env_name
  )
				
  mwaa_auth_token = 'Bearer ' + mwaa_cli_token['CliToken']
  mwaa_webserver_hostname = 'https://{0}/aws_mwaa/cli'.format(mwaa_cli_token['WebServerHostname'])
  raw_data = "trigger_dag {0} -c '{1}'".format(dag_name, conf)
				
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

### Run CLI commands on an SSH tunnel to a bastion host
<a name="example-airflow-cli-commands-private"></a>

Use the following example to run Airflow CLI commands using an SSH tunnel proxy to a Linux Bastion Host.

**Using curl**

1. 

   ```
   ssh -D 8080 -f -C -q -N {{YOUR_USER}}@{{YOUR_BASTION_HOST}}
   ```

1. 

   ```
   curl -x socks5h://0:8080 --request POST https://{{YOUR_HOST_NAME}}/aws_mwaa/cli --header {{YOUR_HEADERS}} --data-raw {{YOUR_CLI_COMMAND}}
   ```