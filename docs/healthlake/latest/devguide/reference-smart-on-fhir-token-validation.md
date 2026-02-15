# Token validation using

AWS Lambda

When you create a HealthLake SMART on FHIR enabled data store, you must provide the ARN of the
AWS Lambda function in the `CreateFHIRDatastore` request. The ARN of the Lambda
function is specified in `IdentityProviderConfiguration` object using the
`IdpLambdaArn` parameter.

You must create the Lambda function prior to creating your SMART on FHIR enabled data
store. Once you create the data store, the Lambda ARN cannot be changed. To see the Lambda
ARN you specified when the data store was created, use the
`DescribeFHIRDatastore` API action.

###### For a FHIR REST request to succeed on a SMART on FHIR enabled data store, your

Lambda function must do the following:

- Return a response in less than 1 second to the HealthLake data store endpoint.
- Decode the access token provided in the authorization header of the REST API
  request sent by the client application.
- Assign an IAM service role that has sufficient permissions to carry out the FHIR
  REST API request.
- The following claims are required to complete a FHIR REST API request. To learn
  more, see [Required claims](reference-smart-on-fhir-authentication.md#server-response "reference-smart-on-fhir-authentication.md#server-response").

      + `nbf`
      + `exp`
      + `isAuthorized`
      + `aud`
      + `scope`

  When working with Lambda, you need to create an execution role and a resource-based policy
  in addition to your Lambda function. A Lambda's function's execution role is an IAM role
  that grants the function permission to access AWS services and resources needed at run time.
  The resource-based policy you provide must allow HealthLake to invoke your function on your
  behalf.

The sections in this topic describe an example request from a client application and
decoded response, the steps needed to create an AWS Lambda function, and how to create a
resource-based policy that HealthLake can assume.

- [Part 1: Creating a Lambda
  function](#smart-on-fhir-lambda-create "#smart-on-fhir-lambda-create")
- [Part 2: Creating a HealthLake service
  role used by the AWS Lambda function](#smart-on-fhir-lambda-service-role "#smart-on-fhir-lambda-service-role")
- [Part 3: Updating
  the Lambda function's execution role](#smart-on-fhir-lambda-service-role-execution-role "#smart-on-fhir-lambda-service-role-execution-role")
- [Part 4: Adding a resource
  policy to your Lambda function](#smart-on-fhir-lambda-invoke-healthlake "#smart-on-fhir-lambda-invoke-healthlake")
- [Part 5: Provisioning
  concurrency for your Lambda function](#smart-on-fhir-lambda-function-scaling "#smart-on-fhir-lambda-function-scaling")

## Creating an AWS Lambda function

The Lambda function created in this topic is triggered when HealthLake receives a requests
to a SMART on FHIR enabled data store. The request from the client application contains
a REST API call, and an authorization header containing an access token.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/
Authorization: Bearer i8hweunweunweofiwweoijewiwe
```

The example Lambda function in this topic uses AWS Secrets Manager to obscure credentials related
to the authorization server. We strongly recommend not providing authorization server
login details directly in a Lambda function.

###### Example validating a FHIR REST request containing an authorization bearer token

The example Lambda function shows you how to validate an FHIR REST request sent to
a SMART on FHIR enabled data store. To see step-by-steps directions on how to
implement this Lambda function, see [Creating a Lambda function using the
AWS Management Console](#create-lambda-console "#create-lambda-console").

If the FHIR REST API request does not contain a valid data store endpoint, access
token, and REST operation the Lambda function will fail. To learn more about the
required authorization server elements, see [Required claims](reference-smart-on-fhir-authentication.md#server-response "reference-smart-on-fhir-authentication.md#server-response").

```
import base64
import boto3
import logging
import json
import os
from urllib import request, parse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

## Uses Secrets manager to gain access to the access key ID and secret access key for the authorization server
client = boto3.client('secretsmanager', region_name="region-of-datastore")
response = client.get_secret_value(SecretId='name-specified-by-customer-in-secretsmanager')
secret = json.loads(response['SecretString'])
client_id = secret['client_id']
client_secret = secret['client_secret']


unencoded_auth = f'{client_id}:{client_secret}'
headers = {
  'Authorization': f'Basic {base64.b64encode(unencoded_auth.encode()).decode()}',
  'Content-Type': 'application/x-www-form-urlencoded'
}

auth_endpoint = os.environ['auth-server-base-url'] # Base URL of the Authorization server
user_role_arn = os.environ['iam-role-arn'] # The IAM role client application will use to complete the HTTP request on the datastore

def lambda_handler(event, context):
    if 'datastoreEndpoint' not in event or 'operationName' not in event or 'bearerToken' not in event:
    return {}

    datastore_endpoint = event['datastoreEndpoint']
    operation_name = event['operationName']
    bearer_token = event['bearerToken']
    logger.info('Datastore Endpoint [{}], Operation Name: [{}]'.format(datastore_endpoint, operation_name))

    ## To validate the token
    auth_response = auth_with_provider(bearer_token)
    logger.info('Auth response: [{}]'.format(auth_response))
    auth_payload = json.loads(auth_response)
    ## Required parameters needed to be sent to the datastore endpoint for the HTTP request to go through
    auth_payload["isAuthorized"] = bool(auth_payload["active"])
    auth_payload["nbf"] = auth_payload["iat"]
    return {"authPayload": auth_payload, "iamRoleARN": user_role_arn}

## access the server
def auth_with_provider(token):
    data = {'token': token, 'token_type_hint': 'access_token'}
    req = request.Request(url=auth_endpoint + '/v1/introspect', data=parse.urlencode(data).encode(), headers=headers)
    with request.urlopen(req) as resp:
    return resp.read().decode()
```

The following procedure assumes you've already created the service role that
you want HealthLake to assume when handling a FHIR REST API request on a
SMART on FHIR enabled data store. If you have not created the service role, you
can still create the Lambda function. You must add the ARN of service role before
the Lambda function will work. To learn more about creating a service role and
specifying it in the Lambda function, see [Creating a HealthLake service role for
use in the AWS Lambda function used to decode a JWT](#smart-on-fhir-lambda-service-role "#smart-on-fhir-lambda-service-role")

###### To create a Lambda function (AWS Management Console)

1. Open the [Functions
   page](https://console.aws.amazon.com/lambda/home/functions "https://console.aws.amazon.com/lambda/home/functions") of the Lambda console.
2. Choose **Create function**.
3. Select **Author from scratch**.
4. Under **Basic information** enter a
   **Function name**. Under
   **Runtime** choose a python based runtime.
5. For **Execution role**, choose **Create a new
   role with basic Lambda permissions**.

Lambda creates an [execution
role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") that grants the function permission to upload logs to
Amazon CloudWatch. The Lambda function assumes the execution role when you invoke
your function, and uses the execution role to create credentials for the
AWS SDK. 6. Choose the **Code** tab, and add the sample Lambda
function.

If you've not yet created the service role for the Lambda function to
use you'll need to create it before the sample Lambda function will work.
To learn more about creating a service role for the Lambda function, see
[Creating a HealthLake service role for
use in the AWS Lambda function used to decode a JWT](#smart-on-fhir-lambda-service-role "#smart-on-fhir-lambda-service-role").

```
import base64
import boto3
import logging
import json
import os
from urllib import request, parse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

## Uses Secrets manager to gain access to the access key ID and secret access key for the authorization server
client = boto3.client('secretsmanager', region_name="region-of-datastore")
response = client.get_secret_value(SecretId='name-specified-by-customer-in-secretsmanager')
secret = json.loads(response['SecretString'])
client_id = secret['client_id']
client_secret = secret['client_secret']


unencoded_auth = f'{client_id}:{client_secret}'
headers = {
  'Authorization': f'Basic {base64.b64encode(unencoded_auth.encode()).decode()}',
  'Content-Type': 'application/x-www-form-urlencoded'
}

auth_endpoint = os.environ['auth-server-base-url'] # Base URL of the Authorization server
user_role_arn = os.environ['iam-role-arn'] # The IAM role client application will use to complete the HTTP request on the datastore

def lambda_handler(event, context):
    if 'datastoreEndpoint' not in event or 'operationName' not in event or 'bearerToken' not in event:
    return {}

    datastore_endpoint = event['datastoreEndpoint']
    operation_name = event['operationName']
    bearer_token = event['bearerToken']
    logger.info('Datastore Endpoint [{}], Operation Name: [{}]'.format(datastore_endpoint, operation_name))

    ## To validate the token
    auth_response = auth_with_provider(bearer_token)
    logger.info('Auth response: [{}]'.format(auth_response))
    auth_payload = json.loads(auth_response)
    ## Required parameters needed to be sent to the datastore endpoint for the HTTP request to go through
    auth_payload["isAuthorized"] = bool(auth_payload["active"])
    auth_payload["nbf"] = auth_payload["iat"]
    return {"authPayload": auth_payload, "iamRoleARN": user_role_arn}

## Access the server
def auth_with_provider(token):
    data = {'token': token, 'token_type_hint': 'access_token'}
    req = request.Request(url=auth_endpoint + '/v1/introspect', data=parse.urlencode(data).encode(), headers=headers)
    with request.urlopen(req) as resp:
    return resp.read().decode()
```

### Modifying a Lambda function's

execution role

After creating the Lambda function, you need to update the execution role to
include the necessary permissions to call Secrets Manager. In Secrets Manager, each secret you create
has an ARN. To apply the least privilege, the execution role should only have access
to the resources needed for the Lambda function to execute.

You can modify a Lambda function's execution role by searching for it in the IAM
console or by choosing **Configuration** in the Lambda console. To
learn more about managing your Lambda functions execution role, see [Lambda execution
role](#smart-on-fhir-lambda-service-role-execution-role "#smart-on-fhir-lambda-service-role-execution-role").

###### Example Lambda function execution role that grants access to

`GetSecretValue`

Adding the IAM action `GetSecretValue` to execution role grants
the necessary permission for the sample Lambda function to work.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:secret-name-DKodTA"
 }
 ]
}`

```

At this point you've created a Lambda function that can be used to validate the access
token provided as part of the FHIR REST request sent to your SMART on FHIR enabled data
store.

## Creating a HealthLake service role for

use in the AWS Lambda function used to decode a JWT

###### Persona: IAM Administrator

A user who can add or remove IAM policies, and create new IAM
identities.

**Service role**

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

After the JSON Web Token (JWT) is decoded the authorization Lambda needs to also
return an IAM role ARN. This role must have the necessary permissions to carry out the
REST API request or it will fail due to insufficient permissions.

When setting up a custom policy using IAM it is best to grant the minimum
permissions required. To learn more, see [Apply
least-privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the
_IAM User Guide_.

Creating a HealthLake service role to designate in the authorization Lambda function
requires two steps.

- First, you need to create IAM policy. The policy must specify access to the
  FHIR resources that you have provided scopes for in the authorization
  server.
- Second, you need to create the service role. When you create the role you
  designate a trust relationship and attach the policy you created in step one.
  The trust relationship designates HealthLake as the service principal. You need to
  specify a HealthLake data store ARN and a AWS account ID in this step.

### Creating a new IAM policy

The scopes you define in your authorization server determine what FHIR resources
an authenticated user has access to in a HealthLake data store.

The IAM policy you create can be tailored to match the scopes you've
defined.

The following actions in the `Action` element of an IAM policy
statement can be defined. For each `Action` in the table you can define a
`Resource types`. In HealthLake a data store is the only supported
resource type that can be defined in the `Resource` element of an IAM
permission policy statement.

Individual FHIR resources are not a resource that you can define as an element in
a IAM permission policy.

| Actions defined by HealthLake | Actions                                                  | Description | Access level                                                                                      | Resource type (Required) |
| ----------------------------- | -------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------- | ------------------------ |
| CreateResource                | Grants permission to a create resource                   | Write       | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| DeleteResource                | Grants permission to delete resource                     | Write       | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| ReadResource                  | Grants permission to read resource                       | Read        | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| SearchWithGet                 | Grants permission to search resources with GET<br>method | Read        | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| SearchWithPost                | Grants permission to search resources with POST method   | Read        | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| StartFHIRExportJobWithPost    | Grants permission to begin a FHIR Export job with<br>GET | Write       | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |
| UpdateResource                | Grants permission to update resource                     | Write       | Datastore ARN: arn:aws:healthlake:`your-region`:`111122223333`:datastore/fhir/`your-datastore-id` |

To get started, you can use `AmazonHealthLakeFullAccess`. This policy would grant
read, write, search, and export on all FHIR resources found in a data store. To
grant read-only permissions on a data store use
`AmazonHealthLakeReadOnlyAccess`.

To learn more about creating a custom policy using the AWS Management Console, AWS CLI, or IAM
SDKs, see [Creating IAM](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")
policies in the _IAM User Guide_.

### Creating a service role for HealthLake

(IAM console)

Use this procedure to create a service role. When you create a service you will
also need to designate an IAM policy.

###### To create the service role for HealthLake (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**.
3. Then, choose **Create role**.
4. On the **Select trust entity** page, choose
   **Custom trust policy**.
5. Next, under **Custom trust policy** update the sample
   policy as follows. Replace `your-account-id` with your
   account number, and add the ARN of the data store you want to use in your
   import or export jobs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Principal": {
 "Service": "healthlake.amazonaws.com"
 },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:healthlake:`us-east-1`:`123456789012`:datastore/fhir/`your-datastore-id`"
 }
 }
 }
 ]
}`

```

6. Then, choose **Next**.
7. On the **Add permissions** page, choose the policy that
   you want the HealthLake service to assume. To find your policy, search for it
   under **Permissions policies**.
8. Then, choose **Attach policy**.
9. Then on the **Name, review, and create** page under
   **Role name** enter a name.
10. (Optional)Then under **Description**, add a short
    description for your role.
11. If possible, enter a role name or role name suffix to help you identify
    the purpose of this role. Role names must be unique within your
    AWS account. They are not distinguished by case. For example, you cannot
    create roles named both `PRODROLE` and
    `prodrole`. Because various entities might
    reference the role, you cannot edit the name of the role after it has been
    created.
12. Review the role details, and then choose **Create
    role**.

To learn how to specify the role ARN in the sample Lambda function, see [Creating an AWS Lambda function](#smart-on-fhir-lambda-create "#smart-on-fhir-lambda-create").

## Lambda execution

role

A Lambda function's execution role is an IAM role that grants the function permission
to access AWS services and resources. This page provides information on how to create,
view, and manage a Lambda function's execution role.

By default, Lambda creates an execution role with minimal permissions when you create a
new Lambda function using the AWS Management Console. To manage the permissions granted in the
execution role, see [Creating an execution role in the IAM console](../../../lambda/latest/dg/lambda-intro-execution-role.md#permissions-executionrole-console "../../../lambda/latest/dg/lambda-intro-execution-role.md#permissions-executionrole-console") in the _Lambda
Developer Guide_.

The sample Lambda function provided in this topic uses Secrets Manager to obscure the
authorization server's credentials.

As with any IAM role you create it is important to follow the least privilege best
practice. During the development phrase, you might sometimes grant permissions beyond
what is required. Before publishing your function in the production environment, as a
best practice, adjust the policy to include only the required permissions. For more
information, see [Apply
least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the _IAM User Guide_.

## Allow HealthLake to trigger your

Lambda function

So HealthLake can invoke the Lambda function on your behalf, you must do following:

- You need to set `IdpLambdaArn` equal to the ARN of the Lambda
  function you want HealthLake to invoke in the `CreateFHIRDatastore`
  request.
- You need a resource-based policy allowing HealthLake to invoke the Lambda function
  on your behalf.

When HealthLake receives a FHIR REST API request on a SMART on FHIR enabled data store, it
needs permissions to invoke the Lambda function specified at data store creation on your
behalf. To grant HealthLake access, you'll use a resource-based policy. To learn more about
creating a resource-based policy for a Lambda function, see [Allowing an AWS service to call a Lambda function](../../../lambda/latest/dg/access-control-resource-based.md#permissions-resource-serviceinvoke "../../../lambda/latest/dg/access-control-resource-based.md#permissions-resource-serviceinvoke") in the
_AWS Lambda Developer Guide_.

## Provisioning concurrency for

your Lambda function

###### Important

HealthLake requires that the maximum run time for your Lambda function be less than one
second (1000 milliseconds).

If you Lambda function exceeds the run time limit you get a
**`TimeOut`** exception.

To avoid getting this exception, we recommend configuring provisioned concurrency. By
allocating provisioned concurrency before an increase in invocations, you can ensure
that all requests are served by initialized instances with low latency. To learn more
about configuring provisioned concurrency, see [Configuring provisioned
concurrency](../../../ambda/latest/dg/provisioned-concurrency.md "../../../ambda/latest/dg/provisioned-concurrency.md") in the _Lambda Developer Guide_

To see the average run time for your Lambda function currently use the
**Monitoring** page for your Lambda function on the Lambda console.
By default, the Lambda console provides a **Duration** graph which shows
you the average, minimum, and maximum amount of time your function code spends
processing an event. To learn more about monitoring Lambda functions, see [Monitoring functions in the Lambda console](../../../lambda/latest/dg/monitoring-functions-access-metrics.md#monitoring-console-graph-types "../../../lambda/latest/dg/monitoring-functions-access-metrics.md#monitoring-console-graph-types") in the _Lambda Developer
Guide_.

If you have already provisioned concurrency for your Lambda function and want to
monitor it, see [Monitoring concurrency](../../../lambda/latest/dg/monitoring-concurrency.md "../../../lambda/latest/dg/monitoring-concurrency.md") in
the _Lambda Developer Guide_.
