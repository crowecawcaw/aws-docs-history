

# Amazon OpenSearch Service ML connectors for AWS services
<a name="ml-amazon-connector"></a>

When you use Amazon OpenSearch Service machine learning (ML) connectors with another AWS service, you need to set up an IAM role to securely connect OpenSearch Service to that service. AWS services that you can set up a connector to include Amazon SageMaker AI and Amazon Bedrock. In this tutorial, we cover how to create a connector from OpenSearch Service to SageMaker Runtime. For more information about connectors, see [Supported connectors](https://opensearch.org/docs/latest/ml-commons-plugin/remote-models/connectors/#supported-connectors).

**Topics**
+ [Prerequisites](#connector-sagemaker-prereq)
+ [Create an OpenSearch Service connector](#connector-sagemaker-create)

## Prerequisites
<a name="connector-sagemaker-prereq"></a>

To create a connector, you must have an Amazon SageMaker AI Domain endpoint and an IAM role that grants OpenSearch Service access. 

### Set up an Amazon SageMaker AI domain
<a name="connector-sagemaker"></a>

See [Deploy a Model in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html) in the *Amazon SageMaker AI Developer Guide* to deploy your machine learning model. Note the endpoint URL for your model, which you need in order to create an AI connector.

### Create an IAM role
<a name="connector-sagemaker-iam"></a>

Set up an IAM role to delegate SageMaker Runtime permissions to OpenSearch Service. To create a new role, see [Creating an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html#roles-creatingrole-user-console) in the *IAM User Guide*. Optionally, you could use an existing role as long as it has the same set of privileges. If you do create a new role instead of using an AWS managed role, replace `opensearch-sagemaker-role` in this tutorial with the name of your own role.

1. Attach the following managed IAM policy to your new role to allow OpenSearch Service to access to your SageMaker AI endpoint. To attach a policy to a role, see [Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console). 

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {   
               "Action": [
                   "sagemaker:InvokeEndpointAsync",
                   "sagemaker:InvokeEndpoint"
               ],
               "Effect": "Allow",
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Follow the instructions in [Modifying a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy) to edit the trust relationship of the role. In the following policy, replace {{service-principal}} with one of the following service principals for OpenSearch Service or OpenSearch Serverless:  
**For OpenSearch Service**  
`opensearchservice.amazonaws.com` or `es.amazonaws.com`  
**For OpenSearch Serverless**  
`ml.opensearchservice.amazonaws.com`

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Action": [
                   "sts:AssumeRole"
               ],
               "Effect": "Allow",
               "Principal": {
                   "Service": [
                       "ml.opensearchservice.amazonaws.com"
                   ]
               }
           }
       ]
   }
   ```

------

   We recommend that you use the `aws:SourceAccount` and `aws:SourceArn` condition keys to limit access to a specific domain. The `SourceAccount` is the AWS account ID that belongs to the owner of the domain, and the `SourceArn` is the ARN of the domain. For example, you can add the following condition block to the trust policy: 

   ```
   "Condition": {
       "StringEquals": {
           "aws:SourceAccount": "{{account-id}}"
       },
       "ArnLike": {
           "aws:SourceArn": "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}"
       }
   }
   ```

### Configure permissions
<a name="connector-sagemaker-permissions"></a>

In order to create the connector, you need permission to pass the IAM role to OpenSearch Service. You also need access to the `es:ESHttpPost` action. To grant both of these permissions, attach the following policy to the IAM role whose credentials are being used to sign the request:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/opensearch-sagemaker-role"
        },
        {
            "Effect": "Allow",
            "Action": "es:ESHttpPost",
            "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*"
        }
    ]
}
```

------

If your user or role doesn't have `iam:PassRole` permissions to pass your role, you might encounter an authorization error when you try to register a repository in the next step.

### Map the ML role in OpenSearch Dashboards (if using fine-grained access control)
<a name="connector-sagemaker-fgac"></a>

Fine-grained access control introduces an additional step when setting up a connector. Even if you use HTTP basic authentication for all other purposes, you need to map the `ml_full_access` role to your IAM role that has `iam:PassRole` permissions to pass `opensearch-sagemaker-role`.

1. Navigate to the OpenSearch Dashboards plugin for your OpenSearch Service domain. You can find the Dashboards endpoint on your domain dashboard on the OpenSearch Service console. 

1. From the main menu choose **Security**, **Roles**, and select the **ml\_full\_access** role.

1. Choose **Mapped users**, **Manage mapping**. 

1. Under **Backend roles**, add the ARN of the role that has permissions to pass `opensearch-sagemaker-role`.

   ```
   arn:aws:iam::{{account-id}}:role/{{role-name}}
   ```

1. Select **Map** and confirm the user or role shows up under **Mapped users**.

## Create an OpenSearch Service connector
<a name="connector-sagemaker-create"></a>

To create a connector, send a `POST` request to the OpenSearch Service domain endpoint. You can use curl, the sample Python client, Postman, or another method to send a signed request. Note that you can't use a `POST` request in the Kibana console. The request takes the following format:

```
POST {{domain-endpoint}}/_plugins/_ml/connectors/_create
{
   "name": "sagemaker: embedding",
   "description": "Test connector for Sagemaker embedding model",
   "version": 1,
   "protocol": "aws_sigv4",
   "credential": {
      "roleArn": "arn:aws:iam::{{account-id}}:role/opensearch-sagemaker-role"
   },
   "parameters": {
      "region": "{{region}}",
      "service_name": "sagemaker"
   },
   "actions": [
      {
         "action_type": "predict",
         "method": "POST",
         "headers": {
            "content-type": "application/json"
         },
         "url": "https://runtime.sagemaker.{{region}}.amazonaws.com/endpoints/{{endpoint-id}}/invocations",
         "request_body": "{ \"inputs\": { \"question\": \"${parameters.question}\", \"context\": \"${parameters.context}\" } }"
      }
   ]
}
```

If your domain resides within a virtual private cloud (VPC), your computer must be connected to the VPC for the request to successfully create the AI connector. Accessing a VPC varies by network configuration, but usually involves connecting to a VPN or corporate network. To check that you can reach your OpenSearch Service domain, navigate to `https://{{your-vpc-domain}}.{{region}}.es.amazonaws.com` in a web browser and verify that you receive the default JSON response.

### Sample Python client
<a name="connector-sagemaker-python"></a>

The Python client is simpler to automate than a HTTP request and has better re-usability. To create the AI connector with the Python client, save the following sample code to a Python file. The client requires the [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/), [`requests`](https://requests.readthedocs.io/en/latest/), and [`requests-aws4auth`](https://pypi.org/project/requests-aws4auth/) packages. 

```
import boto3
import requests 
from requests_aws4auth import AWS4Auth

host = '{{domain-endpoint}}/'
region = '{{region}}'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository
path = '_plugins/_ml/connectors/_create'
url = host + path

payload = {
   "name": "sagemaker: embedding",
   "description": "Test connector for Sagemaker embedding model",
   "version": 1,
   "protocol": "aws_sigv4",
   "credential": {
      "roleArn": "arn:aws:iam::{{account-id}}:role/opensearch-sagemaker-role"
   },
   "parameters": {
      "region": "{{region}}",
      "service_name": "sagemaker"
   },
   "actions": [
      {
         "action_type": "predict",
         "method": "POST",
         "headers": {
            "content-type": "application/json"
         },
         "url": "https://runtime.sagemaker.{{region}}.amazonaws.com/endpoints/{{endpoint-id}}/invocations",
         "request_body": "{ \"inputs\": { \"question\": \"${parameters.question}\", \"context\": \"${parameters.context}\" } }"
      }
   ]
}
headers = {"Content-Type": "application/json"}

r = requests.post(url, auth=awsauth, json=payload, headers=headers)
print(r.status_code)
print(r.text)
```

### Register the model for semantic search
<a name="connector-sagemaker-register-model"></a>

If you plan to use the connected model for semantic search, you must include the `model_config` parameter when registering the model. Without this parameter, semantic field index creation will fail with the error "Model config is null for the remote model [{{model\_id}}]".

Include a `model_config` object in your register model request:

```
POST _plugins/_ml/models/_register
{
  "name": "Bedrock embedding model",
  "function_name": "remote",
  "connector_id": "{{connector_id}}",
  "model_config": {
    "model_type": "TEXT_EMBEDDING",
    "embedding_dimension": 1536,
    "framework_type": "SENTENCE_TRANSFORMERS",
    "additional_config": {
      "space_type": "l2"
    }
  }
}
```

Replace `embedding_dimension` with the dimension of your model's output (for example, 1536 for Amazon Titan Embeddings). For information about supported space types, see [k-NN search in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html).