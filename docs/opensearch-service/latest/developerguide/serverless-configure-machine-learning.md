

# Configure Machine Learning on Amazon OpenSearch Serverless
<a name="serverless-configure-machine-learning"></a>

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
When you create a trust policy, add **ml.opensearchservice.amazonaws.com** as the OpenSearch Service principle.
Skip the steps on the [Connectors](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html) page that display how to configure a domain in the policy.
Add the `iam:PassRole` statement in the [Configure permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html#connector-sagemaker-prereq) step.
Skip the **Map the ML role** step in OpenSearch Dashboards. Backend role configuration is not required. This applies to [Connectors for AWS services](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-amazon-connector.html), and to [Connectors for external platforms](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ml-external-connector.html).
In your SigV4 request to the collection endpoint, set the service name to **aoss** instead of **es**.

## Models
<a name="serverless-configure-machine-learning-models"></a>

A model is the core functionality that's used across various AI workflows. Generally, you associate the connector with a model to perform prediction using the connector. After a model is in the deployed state, you can run prediction. For more information, see [Register a model hosted on a third-party platform](https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/register-model/#register-a-model-hosted-on-a-third-party-platform) on the *OpenSearch Documentation* website.

**Note**  
Not all model features are supported on OpenSearch Serverless, such as local models. For more information, see [Unsupported Machine Learning APIs and features](serverless-machine-learning-unsupported-features.md).

## Configure permissions for Machine Learning
<a name="serverless-configure-machine-learning-permissions"></a>

The following section describes the collection data access policies required for Machine Learning (ML). Replace the {{placeholder values}} with your specific information. For more information, see [Supported policy permissions](serverless-data-access.md#serverless-data-supported-permissions).

```
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
+ **aoss:DescribeMLResource** – Grants permission to search and query connectors, models, and model groups.
+ **aoss:CreateMLResource** – Grants permission to create connectors, models, and model groups.
+ **aoss:UpdateMLResource** – Grants permission to update connectors, models, and model groups.
+ **aoss:DeleteMLResource** – Grants permission to delete connectors, models, and model groups.
+ **aoss:ExecuteMLResource** – Grants permission to perform predictions on models.