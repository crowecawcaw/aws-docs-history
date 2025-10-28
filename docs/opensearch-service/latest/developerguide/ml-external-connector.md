# Amazon OpenSearch Service ML connectors for third-party

platforms

In this tutorial, we cover how to create a connector from OpenSearch Service to Cohere. For more
information about connectors, see [Supported connectors](https://opensearch.org/docs/latest/ml-commons-plugin/remote-models/connectors/#supported-connectors "https://opensearch.org/docs/latest/ml-commons-plugin/remote-models/connectors/#supported-connectors").

When you use an Amazon OpenSearch Service machine learning (ML) connector with an external remote
model, you need to store your specific authorization credentials in AWS Secrets Manager. This
could be an API key, or a username and password combination. This means you also need to
create an IAM role that allows OpenSearch Service access to read from Secrets Manager.

###### Topics

- [Prerequisites](#connector-external-prereq "#connector-external-prereq")
- [Create an OpenSearch Service connector](#connector-external-create "#connector-external-create")

## Prerequisites

To create a connector for Cohere or any external provider with OpenSearch Service, you must have
an IAM role that grants OpenSearch Service access to AWS Secrets Manager, where you store your
credentials. You must also store your credentials in Secrets Manager.

### Create an IAM role

Set up an IAM role to delegate Secrets Manager permissions to OpenSearch Service. You can also
use the existing `SecretManagerReadWrite` role. To create a new role,
see [Creating an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console "../../../IAM/latest/UserGuide/id_roles_create_for-user.md#roles-creatingrole-user-console") in the
_IAM User Guide_. If you do create a new role instead
of using an AWS managed role, replace
`opensearch-secretmanager-role` in this tutorial with the name of
your own role.

1. Attach the following managed IAM policy to your new role to allow
   OpenSearch Service to access to your Secrets Manager values. To attach a policy to a role, see
   [Adding IAM Identity Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

2. Follow the instructions in [Modifying a role trust policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-managingrole_edit-trust-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-managingrole_edit-trust-policy") to edit the trust
   relationship of the role. In the following policy, replace
   `service-principle` with one of the
   following service principles for OpenSearch Service or OpenSearch Serverless:

**For OpenSearch Service**

`opensearchservice.amazonaws.com`

**For OpenSearch Serverless**

`ml.opensearchservice.amazonaws.com`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole"
 ],
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "`service-principle`"
 ]
 }
 }
 ]
}`

```

We recommend that you use the `aws:SourceAccount` and
`aws:SourceArn` condition keys to limit access to
specific domain. The `SourceAccount` is the AWS account ID
that belongs to the owner of the domain, and the `SourceArn`
is the ARN of the domain. For example, you can add the following
condition block to the trust policy:

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:es:`region`:`account-id`:domain/`domain-name`"
    }
}
```

### Configure permissions

In order to create the connector, you need permission to pass the IAM role
to OpenSearch Service. You also need access to the `es:ESHttpPost` action. To grant
both of these permissions, attach the following policy to the IAM role whose
credentials are being used to sign the request:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/opensearch-secretmanager-role"
 },
 {
 "Effect": "Allow",
 "Action": "es:ESHttpPost",
 "Resource": "arn:aws:es:`us-east-1`:`111122223333`:domain/`domain-name`/*"
 }
 ]
}`

```

If your user or role doesn't have `iam:PassRole` permissions to
pass your role, you might encounter an authorization error when you try to
register a repository in the next step.

### Set up AWS Secrets Manager

To store your authorization credentials in Secrets Manager, see [Create an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

After Secrets Manager accepts your key-value pair as a secret, you receive an ARN with
the format:
`arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret-a1b2c3`.
Keep a record of this ARN, as you use it and your key when you create a
connector in the next step.

### Map the ML role in OpenSearch Dashboards

(if using fine-grained access control)

Fine-grained access control introduces an additional step when setting up a
connector. Even if you use HTTP basic authentication for all other purposes, you
need to map the `ml_full_access` role to your IAM role that has
`iam:PassRole` permissions to pass
`opensearch-sagemaker-role`.

1. Navigate to the OpenSearch Dashboards plugin for your OpenSearch Service domain. You can
   find the Dashboards endpoint on your domain dashboard on the OpenSearch Service
   console.
2. From the main menu choose **Security**,
   **Roles**, and select the
   **ml_full_access** role.
3. Choose **Mapped users**, **Manage mapping**.
4. Under **Backend roles**, add the ARN of the role that
   has permissions to pass `opensearch-sagemaker-role`.

```
arn:aws:iam::`account-id`:role/`role-name`
```

5. Select **Map** and confirm the user or
   role shows up under **Mapped
   users**.

## Create an OpenSearch Service connector

To create a connector, send a `POST` request to the OpenSearch Service domain
endpoint. You can use curl, the sample Python client, Postman, or another method to
send a signed request. Note that you can't use a `POST` request in the
Kibana console. The request takes the following format:

```
POST `domain-endpoint`/_plugins/_ml/connectors/_create
{
    "name": "Cohere Connector: embedding",
    "description": "The connector to cohere embedding model",
    "version": 1,
    "protocol": "http",
    "credential": {
        "secretArn": "arn:aws:secretsmanager:`region`:`account-id`:secret:`cohere-key-id`",
        "roleArn": "arn:aws:iam::`account-id`:role/opensearch-secretmanager-role"
    },
    "actions": [
        {
            "action_type": "predict",
            "method": "POST",
            "url": "https://api.cohere.ai/v1/embed",
            "headers": {
                "Authorization": "Bearer ${credential.secretArn.`cohere-key-used-in-secrets-manager`}"
            },
            "request_body": "{ \"texts\": ${parameters.texts}, \"truncate\": \"END\" }"
        }
    ]
}
```

The request body for this request is different than that of an open-source
connector request in two ways. Inside the `credential` field, you pass
the ARN for the IAM role that permits OpenSearch Service to read from Secrets Manager, along with the ARN
for the what secret. In the `headers` field, you refer to the secret
using the secret key and the fact its coming from an ARN.

If your domain resides within a virtual private cloud (VPC), your computer must be
connected to the VPC for the request to successfully create the AI connetor.
Accessing a VPC varies by network configuration, but usually involves connecting to
a VPN or corporate network. To check that you can reach your OpenSearch Service domain, navigate
to
`https://`your-vpc-domain`.`region`.es.amazonaws.com`
in a web browser and verify that you receive the default JSON response.

### Sample Python client

The Python client is simpler to automate than a HTTP request and has better
re-usability. To create the AI connector with the Python client, save the
following sample code to a Python file. The client requires the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/"), [`requests`](https://requests.readthedocs.io/en/latest/ "https://requests.readthedocs.io/en/latest/"), and [`requests-aws4auth`](https://pypi.org/project/requests-aws4auth/ "https://pypi.org/project/requests-aws4auth/") packages.

```
import boto3
import requests
from requests_aws4auth import AWS4Auth

host = '`domain-endpoint`/'
region = '`region`'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

path = '_plugins/_ml/connectors/_create'
url = host + path

payload = {
    "name": "Cohere Connector: embedding",
    "description": "The connector to cohere embedding model",
    "version": 1,
    "protocol": "http",
    "credential": {
        "secretArn": "arn:aws:secretsmanager:`region`:`account-id`:secret:`cohere-key-id`",
        "roleArn": "arn:aws:iam::`account-id`:role/opensearch-secretmanager-role"
    },
    "actions": [
        {
            "action_type": "predict",
            "method": "POST",
            "url": "https://api.cohere.ai/v1/embed",
            "headers": {
                "Authorization": "Bearer ${credential.secretArn.`cohere-key-used-in-secrets-manager`}"
            },
            "request_body": "{ \"texts\": ${parameters.texts}, \"truncate\": \"END\" }"
        }
    ]
}

headers = {"Content-Type": "application/json"}

r = requests.post(url, auth=awsauth, json=payload, headers=headers)
print(r.status_code)
print(r.text)
```
