

# Configure Machine Learning on Amazon OpenSearch Serverless

## Machine Learning
<a name="serverless-configure-machine-learning-what-is"></a>

Machine Learning (ML) provides ML capabilities in the form of ML algorithms and remote models. With access to these models, you can run several AI workflows such as RAG or semantic search. ML supports experimentation and production deployment of generative AI use cases using the latest externally hosted models that you can configure with connectors. After you configure a connector, you must configure it to a model and then deploy it to perform prediction.

## Connectors
<a name="serverless-configure-machine-learning-connectors"></a>

Connectors facilitate access to models hosted on third-party ML platforms. They serve as the gateway between your OpenSearch cluster and a remote model. For more information, see the following documentation:
+ [Creating connectors for third-party ML platforms](https://docs.opensearch.org/latest/ml-commons-plugin/remote-models/connectors/) on the *OpenSearch Documentation* website
+ [Connectors for external platforms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-external-connector.html)
+ [Connectors for AWS services](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html)
**Important**  
When you create a trust policy, add **ml.opensearchservice.amazonaws.com** as the OpenSearch service principal. Other service principals, such as `opensearchservice.amazonaws.com`, `es.amazonaws.com`, or `aoss.amazonaws.com`, don't work for collections. Predictions fail with an `sts:AssumeRole` authorization error, and neural queries fail with a `403` error.
Skip the steps on the [Connectors](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html) page that display how to configure a domain in the policy. Don't add the domain `aws:SourceArn` condition to the trust policy, and don't add the `es:ESHttpPost` permission. Instead, grant `aoss:APIAccessAll` in an IAM policy and the permissions in [Configure permissions for Machine Learning](#serverless-configure-machine-learning-permissions) in a data access policy.
Add the `iam:PassRole` statement in the [Configure permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html#connector-sagemaker-prereq) step.
Skip the **Map the ML role** step in OpenSearch Dashboards. Backend role configuration is not required. This applies to [Connectors for AWS services](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html), and to [Connectors for external platforms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-external-connector.html).
In your SigV4 request to the collection endpoint, set the service name to **aoss** instead of **es**.

## Models
<a name="serverless-configure-machine-learning-models"></a>

A model is the core functionality that's used across various AI workflows. Generally, you associate the connector with a model to perform prediction using the connector. After a model is in the deployed state, you can run prediction. For more information, see [Register a model hosted on a third-party platform](https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/register-model/#register-a-model-hosted-on-a-third-party-platform) on the *OpenSearch Documentation* website.

**Note**  
Not all model features are supported on OpenSearch Serverless, such as local models. For more information, see [Unsupported Machine Learning APIs and features](serverless-machine-learning-unsupported-features.md).

## Run predictions
<a name="serverless-configure-machine-learning-predict"></a>

With a remote model, you can run a prediction by sending the model input in the `parameters` object. The parameter names depend on the request body that the connector defines. To run predictions, you need the `aoss:ExecuteMLResource` permission.

```json
POST /_plugins/_ml/models/{{model_id}}/_predict
{
    "parameters": {
        "inputText": "{{What is the meaning of life?}}"
    }
}
```

To pass `text_docs` to a remote text embedding model, add the `algorithm=text_embedding` query parameter. Without this parameter, `text_docs` is ignored and the request can fail with a `Some parameter placeholder not filled in payload` error. The connector's `pre_process_function`, such as `connector.pre_process.bedrock.embedding`, must convert `text_docs` into the parameters that the connector's request body uses.

```json
POST /_plugins/_ml/models/{{model_id}}/_predict?algorithm=text_embedding
{
    "text_docs": ["{{What is the meaning of life?}}"]
}
```

OpenSearch Serverless doesn't support the `POST /_plugins/_ml/_predict/{{algorithm}}/{{model_id}}` route.

## Delete models and connectors
<a name="serverless-configure-machine-learning-delete"></a>

To undeploy and delete a model, you need `aoss:UpdateMLResource` and `aoss:DeleteMLResource` on the model. To delete a connector, you need `aoss:DeleteMLResource` on `model/{{collection_name}}/*`.

You can't delete a deployed model, and you can't delete a connector that a model still uses. Delete the resources in the following order:

1. Undeploy the model. This requires the `aoss:UpdateMLResource` permission.

   ```
   POST /_plugins/_ml/models/{{model_id}}/_undeploy
   ```

1. Delete the model.

   ```
   DELETE /_plugins/_ml/models/{{model_id}}
   ```

1. Delete the connector. If you delete the connector right after the model, the request can return a `409` error for up to about 30 seconds. Wait, and then retry the request.

   ```
   DELETE /_plugins/_ml/connectors/{{connector_id}}
   ```

**Note**  
Changes to a data access policy can take a few minutes to take effect. If you add a missing permission, such as `aoss:UpdateMLResource`, wait before you retry the request.

## Configure permissions for Machine Learning
<a name="serverless-configure-machine-learning-permissions"></a>

The following section describes the collection data access policies required for Machine Learning (ML). Replace the {{placeholder values}} with your specific information. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

```JSON
{
    "Rules": [
        {
            "Resource": [
                "model/{{collection_name}}/*"
            ],
            "Permission": [
                "aoss:DescribeMLResource",
                "aoss:CreateMLResource",
                "aoss:UpdateMLResource",
                "aoss:DeleteMLResource",
                "aoss:ExecuteMLResource"
            ],
            "ResourceType": "model"
        }
    ],
    "Principal": [
        "arn:aws:iam::{{account_id}}:role/{{role_name}}"
    ],
    "Description": "ML full access policy for {{collection_name}}"
}
```

Use the wildcard resource `model/{{collection_name}}/*`. You need it to work with connectors, model groups, and tasks, to search models, and to run workflow steps.
+ **aoss:DescribeMLResource** – Grants permission to search and query connectors, models, and model groups.
+ **aoss:CreateMLResource** – Grants permission to create connectors, models, and model groups.
+ **aoss:UpdateMLResource** – Grants permission to update connectors, models, and model groups, and to deploy and undeploy models, including with the `deploy_model` workflow step. Without this permission, you can't undeploy a deployed model, so you can't delete it. For more information, see [Delete models and connectors](#serverless-configure-machine-learning-delete).
+ **aoss:DeleteMLResource** – Grants permission to delete connectors, models, and model groups.
+ **aoss:ExecuteMLResource** – Grants permission to perform predictions on models. For more information, see [Run predictions](#serverless-configure-machine-learning-predict).

To limit a principal to specific models, use separate policy statements for the wildcard resource and the model names. A policy statement can contain only one rule for the `model` resource type. Don't add the wildcard and a model name to the same rule, because the wildcard applies the rule's permissions to every model in the collection. The following policy lets a role search connectors, model groups, and models, and run predictions on and deploy only the model `{{model_name}}`.

```JSON
[
    {
        "Rules": [
            {
                "Resource": [
                    "model/{{collection_name}}/*"
                ],
                "Permission": [
                    "aoss:DescribeMLResource"
                ],
                "ResourceType": "model"
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account_id}}:role/{{role_name}}"
        ],
        "Description": "Search ML resources in {{collection_name}}"
    },
    {
        "Rules": [
            {
                "Resource": [
                    "model/{{collection_name}}/{{model_name}}"
                ],
                "Permission": [
                    "aoss:UpdateMLResource",
                    "aoss:ExecuteMLResource"
                ],
                "ResourceType": "model"
            }
        ],
        "Principal": [
            "arn:aws:iam::{{account_id}}:role/{{role_name}}"
        ],
        "Description": "Deploy and run predictions on {{model_name}}"
    }
]
```