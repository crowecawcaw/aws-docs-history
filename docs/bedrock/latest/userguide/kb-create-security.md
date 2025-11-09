# Set up security configurations for your knowledge base

After you've created a knowledge base, you might have to set up the following security configurations:

###### Topics

- [Set up data access policies for your knowledge base](#kb-create-security-data "#kb-create-security-data")
- [Set up network access policies for your Amazon OpenSearch Serverless knowledge base](#kb-create-security-network "#kb-create-security-network")

## Set up data access policies for your knowledge base

If you're using a [custom role](kb-permissions.md "kb-permissions.md"), set up security configurations for your newly created knowledge base. If you let Amazon Bedrock create a service role for you, you can skip this step. Follow the steps in the tab corresponding to the database that you set up.

Amazon OpenSearch Serverless
To restrict access to the Amazon OpenSearch Serverless collection to the knowledge base service role, create a data access policy. You can do so in the following ways:

- Use the Amazon OpenSearch Service console by following the steps at [Creating data access policies (console)](../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-console "../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-console") in the Amazon OpenSearch Service Developer Guide.
- Use the AWS API by sending a [CreateAccessPolicy](../../../opensearch-service/latest/ServerlessAPIReference/API_CreateAccessPolicy.md "../../../opensearch-service/latest/ServerlessAPIReference/API_CreateAccessPolicy.md") request with an [OpenSearch Serverless endpoint](../../../general/latest/gr/opensearch-service.md#opensearch-service-regions "../../../general/latest/gr/opensearch-service.md#opensearch-service-regions"). For an AWS CLI example, see [Creating data access policies (AWS CLI)](../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-cli "../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-cli").

Use the following data access policy, specifying the Amazon OpenSearch Serverless collection and your service role:

```
[
    {
        "Description": "`${data access policy description}`",
        "Rules": [
          {
            "Resource": [
              "index/`${collection_name}`/*"
            ],
            "Permission": [
                "aoss:DescribeIndex",
                "aoss:ReadDocument",
                "aoss:WriteDocument"
            ],
            "ResourceType": "index"
          }
        ],
        "Principal": [
            "arn:aws:iam::`${account-id}`:role/`${kb-service-role}`"
        ]
    }
]
```

Pinecone, Redis Enterprise Cloud or MongoDB Atlas
To integrate a Pinecone, Redis Enterprise Cloud, MongoDB Atlas vector index, attach the following identity-based policy to your knowledge base service role to allow it to access the AWS Secrets Manager secret for the vector index.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "bedrock:AssociateThirdPartyKnowledgeBase"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "bedrock:ThirdPartyKnowledgeBaseCredentialsSecretArn": "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`${secret-id}`"
 }
 }
 }]
}`

```

## Set up network access policies for your Amazon OpenSearch Serverless knowledge base

If you use a private Amazon OpenSearch Serverless collection for your knowledge base, it can only be accessed through an AWS PrivateLink VPC endpoint. You can create a private Amazon OpenSearch Serverless collection when you [set up your Amazon OpenSearch Serverless vector collection](knowledge-base-setup.md "knowledge-base-setup.md") or you can make an existing Amazon OpenSearch Serverless collection (including one that the Amazon Bedrock console created for you) private when you configure its network access policy.

The following resources in the Amazon OpenSearch Service Developer Guide will help you understand the setup required for a private Amazon OpenSearch Serverless collections:

- For more information about setting up a VPC endpoint for a private Amazon OpenSearch Serverless collection, see [Access Amazon OpenSearch Serverless using an interface endpoint (AWS PrivateLink)](../../../opensearch-service/latest/developerguide/serverless-vpc.md "../../../opensearch-service/latest/developerguide/serverless-vpc.md").
- For more information about network access policies in Amazon OpenSearch Serverless, see [Network access for Amazon OpenSearch Serverless](../../../opensearch-service/latest/developerguide/serverless-network.md "../../../opensearch-service/latest/developerguide/serverless-network.md").

To allow an Amazon Bedrock knowledge base to access a private Amazon OpenSearch Serverless collection, you must edit the network access policy for the Amazon OpenSearch Serverless collection to allow Amazon Bedrock as a source service. Choose the tab for your preferred method, and then follow the steps:

Console

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. From the left navigation pane, select **Collections**. Then choose your collection.
3. In the **Network** section, select the **Associated Policy**.
4. Choose **Edit**.
5. For **Select policy definition method**, do
   one of the following:
   - Leave **Select policy definition method** as **Visual editor** and configure the following settings in the **Rule 1** section:
     1. (Optional) In the **Rule
        name** field, enter a name for the
        network access rule.
     2. Under **Access collections from**, select **Private (recommended)**.
     3. Select **AWS service private access**. In the text box, enter `bedrock.amazonaws.com`.
     4. Unselect **Enable access to OpenSearch Dashboards.**

   - Choose **JSON** and paste the following policy in the **JSON editor**.

   ```
   [
       {
           "AllowFromPublic": false,
           "Description":"`${network access policy description}`",
           "Rules":[
               {
                   "ResourceType": "collection",
                   "Resource":[
                       "collection/`${collection-id}`"
                   ]
               }
           ],
           "SourceServices":[
               "bedrock.amazonaws.com"
           ]
       }
   ]
   ```

6. Choose **Update**.

API
To edit the network access policy for your Amazon OpenSearch Serverless collection, do the following:

1. Send a [GetSecurityPolicy](../../../opensearch-service/latest/ServerlessAPIReference/API_GetSecurityPolicy.md "../../../opensearch-service/latest/ServerlessAPIReference/API_GetSecurityPolicy.md") request with an [OpenSearch Serverless endpoint](../../../general/latest/gr/opensearch-service.md#opensearch-service-regions "../../../general/latest/gr/opensearch-service.md#opensearch-service-regions"). Specify the `name` of the policy and specify the `type` as `network`. Note the `policyVersion` in the response.
2. Send a [UpdateSecurityPolicy](../../../opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityPolicy.md "../../../opensearch-service/latest/ServerlessAPIReference/API_UpdateSecurityPolicy.md") request with an [OpenSearch Serverless endpoint](../../../general/latest/gr/opensearch-service.md#opensearch-service-regions "../../../general/latest/gr/opensearch-service.md#opensearch-service-regions"). Minimally, specify the following fields:

| Field         | Description                                                                      |
| ------------- | -------------------------------------------------------------------------------- |
| name          | The name of the policy                                                           |
| policyVersion | The `policyVersion`<br>returned to you from the<br>`GetSecurityPolicy` response. |
| type          | The type of security policy. Specify `network`.                                  |
| policy        | The policy to use. Specify the following JSON object                             |

```
[
    {
        "AllowFromPublic": false,
        "Description":"`${network access policy description}`",
        "Rules":[
            {
                "ResourceType": "collection",
                "Resource":[
                    "collection/`${collection-id}`"
                ]
            }
        ],
        "SourceServices":[
            "bedrock.amazonaws.com"
        ]
    }
]
```

For an AWS CLI example, see [Creating data access policies (AWS CLI)](../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-cli "../../../opensearch-service/latest/developerguide/serverless-data-access.md#serverless-data-access-cli").

- Use the Amazon OpenSearch Service console by following the steps at [Creating network policies (console)](../../../opensearch-service/latest/developerguide/serverless-network.md#serverless-network-console "../../../opensearch-service/latest/developerguide/serverless-network.md#serverless-network-console"). Instead of creating a network policy, note the **Associated policy** in the **Network** subsection of the collection details.
