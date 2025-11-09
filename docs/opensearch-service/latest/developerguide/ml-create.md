# Creating ML connectors in OpenSearch Service

Amazon OpenSearch Service flow framework templates allow you to configure and install ML connectors
by utilizing the create connector API offered in ml-commons. You can use ML
connectors to connect OpenSearch Service to other AWS services or third party platforms. For
more information on this, see [Creating connectors for third-party ML platforms](https://opensearch.org/docs/2.13/ml-commons-plugin/remote-models/connectors/ "https://opensearch.org/docs/2.13/ml-commons-plugin/remote-models/connectors/"). The Amazon OpenSearch Service flow
framework API allows you to automate OpenSearch Service setup and preprocessing tasks and can be
used to create ML connectors.

Before you can create a connector in OpenSearch Service, you must do the following:

- Create an Amazon SageMaker AI domain.
- Create an IAM role.
- Configure pass role permission.
- Map the flow-framework and ml-commons roles in OpenSearch Dashboards.
  For more information on how to setup ML connectors for AWS services, see [Amazon OpenSearch Service ML connectors for AWS services](ml-amazon-connector.md#connector-sagemaker-prereq "ml-amazon-connector.md#connector-sagemaker-prereq"). To learn more about using
  OpenSearch Service ML connectors with third-party platforms, see [Amazon OpenSearch Service ML connectors for third-party platforms](ml-amazon-connector.md#connector-sagemaker-prereq "ml-amazon-connector.md#connector-sagemaker-prereq").

## Creating a connector through a flow-framework

service

To create a flow-framework template with connector, you will need to send a
`POST` request to your OpenSearch Service domain endpoint. You can use cURL, a
sample Python client, Postman, or another method to send a signed request. The
`POST` request takes the following format:

```
POST /_plugins/_flow_framework/workflow
{
  "name": "Deploy Claude Model",
  "description": "Deploy a model using a connector to Claude",
  "use_case": "PROVISION",
  "version": {
    "template": "1.0.0",
    "compatibility": [
      "2.12.0",
      "3.0.0"
    ]
  },
  "workflows": {
    "provision": {
      "nodes": [
        {
          "id": "create_claude_connector",
          "type": "create_connector",
          "user_inputs": {
            "name": "Claude Instant Runtime Connector",
            "version": "1",
            "protocol": "aws_sigv4",
            "description": "The connector to Bedrock service for Claude model",
            "actions": [
              {
                "headers": {
                  "x-amz-content-sha256": "required",
                  "content-type": "application/json"
                },
                "method": "POST",
                "request_body": "{ \"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }",
                "action_type": "predict",
                "url": "https://bedrock-runtime.us-west-2.amazonaws.com/model/anthropic.claude-instant-v1/invoke"
              }
            ],
            "credential": {
                "roleArn": "arn:aws:iam::account-id:role/opensearch-secretmanager-role"
             },
            "parameters": {
              "endpoint": "bedrock-runtime.us-west-2.amazonaws.com",
              "content_type": "application/json",
              "auth": "Sig_V4",
              "max_tokens_to_sample": "8000",
              "service_name": "bedrock",
              "temperature": "0.0001",
              "response_filter": "$.completion",
              "region": "us-west-2",
              "anthropic_version": "bedrock-2023-05-31"
            }
          }
        }
      ]
    }
  }
}
```

If your domain resides within a virtual private cloud (Amazon VPC), you must be
connected to the Amazon VPC for the request to successfully create the AI connector.
Accessing an Amazon VPC varies by network configuration, but usually involves
connecting to a VPN or corporate network. To check that you can reach your OpenSearch Service
domain, navigate to
`https://`your-vpc-domain`.`region`.es.amazonaws.com`
in a web browser and verify that you receive the default JSON response. (Replace
the `placeholder text` with your own values.

### Sample Python client

The Python client is simpler to automate than a `HTTP` request
and has better re-usability. To create the AI connector with the Python
client, save the following sample code to a Python file. The client requires
the [AWS SDK for Python (Boto3)](ml-amazon-connector.md#connector-sagemaker-prereq "ml-amazon-connector.md#connector-sagemaker-prereq"), [Requests:HTTP for Humans](ml-amazon-connector.md#connector-sagemaker-prereq "ml-amazon-connector.md#connector-sagemaker-prereq"), and [requests-aws4auth
1.2.3](https://pypi.org/project/requests-aws4auth/ "https://pypi.org/project/requests-aws4auth/") packages.

```
import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'domain-endpoint/'
region = 'region'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

path = '_plugins/_flow_framework/workflow'
url = host + path

payload = {
  "name": "Deploy Claude Model",
  "description": "Deploy a model using a connector to Claude",
  "use_case": "PROVISION",
  "version": {
    "template": "1.0.0",
    "compatibility": [
      "2.12.0",
      "3.0.0"
    ]
  },
  "workflows": {
    "provision": {
      "nodes": [
        {
          "id": "create_claude_connector",
          "type": "create_connector",
          "user_inputs": {
            "name": "Claude Instant Runtime Connector",
            "version": "1",
            "protocol": "aws_sigv4",
            "description": "The connector to Bedrock service for Claude model",
            "actions": [
              {
                "headers": {
                  "x-amz-content-sha256": "required",
                  "content-type": "application/json"
                },
                "method": "POST",
                "request_body": "{ \"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }",
                "action_type": "predict",
                "url": "https://bedrock-runtime.us-west-2.amazonaws.com/model/anthropic.claude-instant-v1/invoke"
              }
            ],
            "credential": {
                "roleArn": "arn:aws:iam::account-id:role/opensearch-secretmanager-role"
             },
            "parameters": {
              "endpoint": "bedrock-runtime.us-west-2.amazonaws.com",
              "content_type": "application/json",
              "auth": "Sig_V4",
              "max_tokens_to_sample": "8000",
              "service_name": "bedrock",
              "temperature": "0.0001",
              "response_filter": "$.completion",
              "region": "us-west-2",
              "anthropic_version": "bedrock-2023-05-31"
            }
          }
        }
      ]
    }
  }
}

headers = {"Content-Type": "application/json"}

r = requests.post(url, auth=awsauth, json=payload, headers=headers)
print(r.status_code)
print(r.text)
```

#### Pre-defined workflow templates

Amazon OpenSearch Service provides several workflow templates for some common machine
learning (ML) use cases. Using a template simplifies complex setups and
provides many default values for use cases like semantic or
conversational search. You can specify a workflow template when you call
the Create Workflow API.

- To use an OpenSearch Service provided workflow template, specify the template
  use case as the `use_case` query parameter.
- To use a custom workflow template, provide the complete template
  in the request body. For an, example of a custom template, see an
  example JSON template or an example YAML template.

#### Template Use Cases

This table provides an overview of the different templates available,
a description of the templates, and the required parameters.

| Template use case                                      | Description                                                                                                                                                                                                             | Required Parameters                                                               |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `bedrock_titan_embedding_model_deploy`                 | Creates and deploys an Amazon Bedrock embedding model (by<br>default,<br>`titan-embed-text-v1`                                                                                                                          | `create_connector.credential.roleArn`                                             |
| `bedrock_titan_embedding_model_deploy`                 | Creates and deploys an Amazon Bedrock multimodal<br>embedding model (by default,<br>`titan-embed-text-v1`                                                                                                               | `create_connector.credential.roleArn`                                             |
| `cohere_embedding_model_deploy`                        | Creates and deploys a Cohere embedding model<br>(by default, embed-english-v3.0).                                                                                                                                       | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `cohere_chat_model_deploy`                             | Creates and deploys a Cohere chat model (by<br>default, Cohere Command).                                                                                                                                                | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `open_ai_embedding_model_deploy`                       | Creates and deploys an OpenAI embedding model<br>(by default, text-embedding-ada-002).                                                                                                                                  | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `openai_chat_model_deploy`                             | Creates and deploys an OpenAI chat model (by<br>default, gpt-3.5-turbo).                                                                                                                                                | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `semantic_search_with_cohere_embedding`                | Configures semantic search and deploys a Cohere<br>embedding model. You must provide the API key for<br>the Cohere model.                                                                                               | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `semantic_search_with_cohere_embedding_query_enricher` | Configures semantic search and deploys a Cohere<br>embedding model. Adds a query_enricher search<br>processor that sets a default model ID for neural<br>queries. You must provide the API key for the Cohere<br>model. | `create_connector.credential.roleArn`,<br>`create_connector.credential.secretArn` |
| `multimodal_search_with_bedrock_titan`                 | Deploys an Amazon Bedrock multimodal model and configures<br>an ingestion pipeline with a text_image_embedding<br>processor and a k-NN index for multimodal search.<br>You must provide your AWS<br>credentials.        | `create_connector.credential.roleArn`                                             |

###### Note

For all templates that require a secret ARN, the default is to store
the secret with a key name of "key" in AWS Secrets Manager.

## Default templates with pretrained models

Amazon OpenSearch Service offers two additonal default workflow templates not available in the
opensource OpenSearch Service.

| Template use case                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `semantic_search_with_local_model` | Configures [semantic search](https://opensearch.org/docs/2.14/search-plugins/semantic-search/ "https://opensearch.org/docs/2.14/search-plugins/semantic-search/") and deploys a pretrained model<br>(`msmarco-distilbert-base-tas-b`). Adds a<br>[`neural_query_enricher`](https://opensearch.org/docs/2.14/search-plugins/search-pipelines/neural-query-enricher/ "https://opensearch.org/docs/2.14/search-plugins/search-pipelines/neural-query-enricher/") search<br>processor that sets a default model ID for neural queries<br>and creates a linked k-NN index called<br>'my-nlp-index'. |
| `hybrid_search_with_local_model`   | Configures [hybrid search](https://opensearch.org/docs/2.14/search-plugins/hybrid-search/ "https://opensearch.org/docs/2.14/search-plugins/hybrid-search/") and deploys a pretrained model<br>(`msmarco-distilbert-base-tas-b`). Adds a<br>[`neural_query_enricher`](https://opensearch.org/docs/2.14/search-plugins/search-pipelines/neural-query-enricher/ "https://opensearch.org/docs/2.14/search-plugins/search-pipelines/neural-query-enricher/") search<br>processor that sets a default model ID for neural queries<br>and creates a linked k-NN index called<br>'my-nlp-index'.       |
