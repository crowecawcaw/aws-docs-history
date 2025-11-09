# Run interactive workloads with EMR

Serverless through an Apache Livy endpoint

With Amazon EMR releases 6.14.0 and higher, create and enable an Apache Livy endpoint when creating an EMR Serverless
application and run interactive workloads through your self-hosted notebooks or with a custom client. An Apache Livy endpoint
offers the following benefits:

- You can securely connect to an Apache Livy endpoint through Jupyter notebooks and manage
  Apache Spark workloads with Apache Livy's REST interface.
- Use the Apache Livy REST API operations for interactive web applications that use data from Apache Spark workloads.

## Prerequisites

To use an Apache Livy endpoint with EMR Serverless, meet the following requirements:

- Complete the steps in [Getting started with Amazon EMR Serverless](getting-started.md "getting-started.md").
- To run interactive workloads through Apache Livy endpoints, you need certain permissions and roles.
  For more information, refer to [Required permissions for interactive workloads](interactive-workloads.md#interactive-permissions "interactive-workloads.md#interactive-permissions").

## Required permissions

In addition to the required permissions to access EMR Serverless, also add the
following permissions to your IAM role to access an Apache Livy endpoint and run applications:

- `emr-serverless:AccessLivyEndpoints` – grants permission to access and connect to the Livy-enabled
  application that you specify as `Resource`. You need this permission to run the REST API operations available from the Apache
  Livy endpoint.
- `iam:PassRole` – grants permission to access the IAM execution role when creating the Apache Livy
  session. EMR Serverless will use this role to execute your workloads.
- `emr-serverless:GetDashboardForJobRun` – grants permission to generate the Spark Live UI and driver
  log links and provides access to the logs as part of the Apache Livy session results.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EMRServerlessInteractiveAccess",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:AccessLivyEndpoints"
 ],
 "Resource": [
 "arn:aws:emr-serverless:*:123456789012:/applications/*"
 ]
 },
 {
 "Sid": "EMRServerlessRuntimeRoleAccess",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRServerlessExecutionRole"
 ],
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "emr-serverless.amazonaws.com"
 }
 }
 },
 {
 "Sid": "EMRServerlessDashboardAccess",
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetDashboardForJobRun"
 ],
 "Resource": [
 "arn:aws:emr-serverless:*:123456789012:/applications/*"
 ]
 }
 ]
}`

```

## Getting started

To create an Apache Livy-enabled application and run it, follow these steps.

1. To create an Apache Livy-enabled application, run the following command.

```
 aws emr-serverless create-application \
--name `my-application-name` \
--type '`application-type`' \
 --release-label <Amazon EMR-release-version>
--interactive-configuration '{"livyEndpointEnabled": true}'
```

2. After EMR Serverless creates your application, start the application to make the
   Apache Livy endpoint available.

```
 aws emr-serverless start-application \
 --application-id `application-id`
```

Use the following command to check whether the status of your application. Once the status becomes
`STARTED`, access the Apache Livy endpoint.

```
aws emr-serverless get-application \
--region `<AWS_REGION>` --application-id `>application_id>`
```

3. Use the following URL to access the endpoint:

```
https://_`<application-id>`_.livy.emr-serverless-services._`<AWS_REGION>`_.amazonaws.com
```

Once the endpoint is ready, submit workloads based on your use case. You must sign every request to the endpoint
with [the SIGv4 protocol](../../../IAM/latest/UserGuide/create-signed-request.md "../../../IAM/latest/UserGuide/create-signed-request.md") and pass in an authorization header.
You can use the following methods to run workloads:

- HTTP client – submit your Apache Livy endpoint API operations with a custom HTTP client.
- Sparkmagic kernel – run the sparkmagic kernel locally and submit interactive queries
  with Jupyter notebooks.

### HTTP clients

To create an Apache Livy session, submit `emr-serverless.session.executionRoleArn`
in the `conf` parameter of your request body. The following example is a sample `POST /sessions` request.

```
{
    "kind": "pyspark",
    "heartbeatTimeoutInSecond": 60,
    "conf": {
        "emr-serverless.session.executionRoleArn": "`<executionRoleArn>`"
    }
}
```

The following table describes all of the available Apache Livy API operations.

| API operation                                                  | Description                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| GET /sessions                                                  | Returns a list of all of the active interactive sessions.    |
| POST /sessions                                                 | Creates a new interactive session via spark or pyspark.      |
| GET /sessions/<`sessionId`>                                    | Returns the session information.                             |
| GET /sessions/<`sessionId`>/state                              | Returns the state of session.                                |
| DELETE /sessions/<`sessionId`>                                 | Stops and deletes the session.                               |
| GET /sessions/<`sessionId`>/statements                         | Returns all the statements in a session.                     |
| POST /sessions/<`sessionId`>/statements                        | Runs a statement in a session.                               |
| GET /sessions/<`sessionId`>/statements/<`statementId`>         | Returns the details of the specified statement in a session. |
| POST /sessions/<`sessionId`>/statements/<`statementId`>/cancel | Cancels the specified statement in this session.             |

#### Sending requests to the Apache Livy endpoint

You can also send requests directly to the Apache Livy endpoint from an HTTP client. Doing so
lets you remotely run code for your use cases outside of a notebook.

Before you start sending requests to the endpoint, make sure that you've installed the following libraries:

```
pip3 install botocore awscrt requests
```

The following is a sample Python script to send HTTP requests directly to an endpoint:

```
from botocore import crt
import requests
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
import botocore.session
import json, pprint, textwrap

endpoint = 'https://`<application_id>`.livy.emr-serverless-services.`<AWS_REGION>`.amazonaws.com'
headers = {'Content-Type': 'application/json'}

session = botocore.session.Session()
signer = crt.auth.CrtS3SigV4Auth(session.get_credentials(), 'emr-serverless', '`<AWS_REGION>`')


### Create session request

data = {'kind': 'pyspark', 'heartbeatTimeoutInSecond': 60, 'conf': { 'emr-serverless.session.executionRoleArn': 'arn:aws:iam::123456789012:role/role1'}}

request = AWSRequest(method='POST', url=endpoint + "/sessions", data=json.dumps(data), headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r = requests.post(prepped.url, headers=prepped.headers, data=json.dumps(data))

pprint.pprint(r.json())


### List Sessions Request

request = AWSRequest(method='GET', url=endpoint + "/sessions", headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r2 = requests.get(prepped.url, headers=prepped.headers)
pprint.pprint(r2.json())


### Get session state

session_url = endpoint + r.headers['location']

request = AWSRequest(method='GET', url=session_url, headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r3 = requests.get(prepped.url, headers=prepped.headers)

pprint.pprint(r3.json())


### Submit Statement

data = {
      'code': "1 + 1"
}

statements_url = endpoint + r.headers['location'] + "/statements"

request = AWSRequest(method='POST', url=statements_url, data=json.dumps(data), headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r4 = requests.post(prepped.url, headers=prepped.headers, data=json.dumps(data))

pprint.pprint(r4.json())

### Check statements results

specific_statement_url = endpoint + r4.headers['location']

request = AWSRequest(method='GET', url=specific_statement_url, headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r5 = requests.get(prepped.url, headers=prepped.headers)

pprint.pprint(r5.json())


### Delete session


session_url = endpoint + r.headers['location']

request = AWSRequest(method='DELETE', url=session_url, headers=headers)

request.context["payload_signing_enabled"] = False

signer.add_auth(request)

prepped = request.prepare()

r6 = requests.delete(prepped.url, headers=prepped.headers)

pprint.pprint(r6.json())

```

### Sparkmagic kernel

Before you install sparkmagic, make sure that you have configured AWS credentials in the instance
in which you want to install sparkmagic

1. Install sparkmagic by following the [installation steps](https://github.com/jupyter-incubator/sparkmagic?tab=readme-ov-file#installation "https://github.com/jupyter-incubator/sparkmagic?tab=readme-ov-file#installation").
   Note that you only perform the first four steps.
2. The sparkmagic kernel supports custom authenticators, so you can integrate an authenticator
   with the sparkmagic kernel so that every request is SIGv4 signed.
3. Install the EMR Serverless custom authenticator.

```
pip install emr-serverless-customauth
```

4. Now provide the path to the custom authenticator and the Apache Livy endpoint URL in the sparkmagic configuration json file.
   Use the following command to open the configuration file.

```
vim ~/.sparkmagic/config.json
```

The following is a sample `config.json` file.

```
{
"kernel_python_credentials" : {
    "username": "",
    "password": "",
    "url": "https://`<application-id>`.livy.emr-serverless-services.`<AWS_REGION>`.amazonaws.com",
    "auth": "Custom_Auth"
  },

  "kernel_scala_credentials" : {
    "username": "",
    "password": "",
    "url": "https://`<application-id>`.livy.emr-serverless-services.`<AWS_REGION>`.amazonaws.com",
    "auth": "Custom_Auth"
  },
  "authenticators": {
    "None": "sparkmagic.auth.customauth.Authenticator",
    "Basic_Access": "sparkmagic.auth.basic.Basic",
    "Custom_Auth": "emr_serverless_customauth.customauthenticator.EMRServerlessCustomSigV4Signer"
  },
  "livy_session_startup_timeout_seconds": 600,
  "ignore_ssl_errors": false
}
```

5. Start Jupyter lab. It should use the custom authentication that you set up in the last step.
6. You can then run the following notebook commands and your code to get started.

```
%%info //Returns the information about the current sessions.
```

```
%%configure -f //Configure information specific to a session. We supply executionRoleArn in this example. Change it for your use case.
{
    "driverMemory": "4g",
    "conf": {
          "emr-serverless.session.executionRoleArn": "arn:aws:iam::123456789012:role/`JobExecutionRole`"
    }
}
```

```
`<your code>`//Run your code to start the session
```

Internally, each instruction calls each of the Apache Livy API operations through the configured Apache Livy endpoint URL.
You can then write your instructions according to your use case.

## Considerations

Consider the following considerations when running interactive workloads through Apache Livy endpoints.

- EMR Serverless maintains session-level isolation using the caller principal.
  The caller principal that creates the session is the only one that can access that session.
  For more granular isolation, configure a source identity when you assume credentials.
  In this case, EMR Serverless enforces session-level isolation based on the caller principal and
  the source identity. For more information about source identity, refer to
  [Monitor and control actions taken with assumed roles](../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md#id_credentials_temp_control-access_monitor-specify-sourceid "../../../IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.md#id_credentials_temp_control-access_monitor-specify-sourceid").
- Apache Livy endpoints are supported with EMR Serverless releases 6.14.0 and higher.
- Apache Livy endpoints are supported only for the Apache Spark engine.
- Apache Livy endpoints support Scala Spark and PySpark.
- By default, `autoStopConfig` is enabled in your applications. This means that applications
  shut down after 15 minutes of being idle. You can change this configuration as part of your `create-application` or `update-application` request.
- You can run up to 25 concurrent sessions on a single Apache Livy endpoint-enabled application.
- For the best startup experience, we suggest that you configure pre-initialized
  capacity for drivers and executors.
- You must manually start your application before connecting to the Apache Livy endpoint.
- You must have sufficient vCPU service quota in your AWS account to run interactive workloads
  with the Apache Livy endpoint. We suggest at least 24 vCPU.
- The default Apache Livy session timeout is 1 hour.
  If you don't run statements for one hour, then Apache Livy
  deletes the session and releases the driver and executors. From release emr-7.8.0, this value can be set
  by specifying the `ttl` parameter as part of Livy `/sessions POST` request, for
  example, `2h`(hours), `120m`(minutes), `7200s`(seconds), `7200000ms`(milliseconds).

###### Note

This configuration cannot be changed prior to emr-7.8.0. The following is a sample
of a `POST /sessions` request body.

```
{
    "kind": "pyspark",
    "heartbeatTimeoutInSecond": 60,
    "conf": {
        "emr-serverless.session.executionRoleArn": "`executionRoleArn`"
    },
    "ttl": "2h"
}
```

- Starting with Amazon EMR release emr-7.8.0 for Applications with fine-grained access control via LakeFormation enabled, the setting can be disabled per
  session. For more information on enabling fine grained access control for an EMR Serverless application,
  refer to [Methods for fine-grained access control](emr-serverless-lf-enable.md#emr-serverless-lf-enable-config "emr-serverless-lf-enable.md#emr-serverless-lf-enable-config").

###### Note

Lake Formation cannot be enabled for a Session when it has not been enabled for an Application.
The following is a sample of a `POST /sessions` request body.

```
{
    "kind": "pyspark",
    "heartbeatTimeoutInSecond": 60,
    "conf": {
        "emr-serverless.session.executionRoleArn": "`executionRoleArn`"
    },
    "spark.emr-serverless.lakeformation.enabled" : "false"
}
```

- Only active sessions can interact with an Apache Livy endpoint. Once the session finishes, cancels, or terminates,
  you can't access it through the Apache Livy endpoint.
