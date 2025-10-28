# Create a collection (CLI)

Use the procedures in this section to create an OpenSearch Serverless collection using the AWS CLI.

###### Topics

- [Before you
  begin](#serverless-create-cli-before-you-begin "#serverless-create-cli-before-you-begin")
- [Creating a collection](#serverless-create-cli-creating "#serverless-create-cli-creating")
- [Creating a
  collection with an automatic semantic enrichment index](#serverless-create-cli-automatic-semantic-enrichment "#serverless-create-cli-automatic-semantic-enrichment")

## Before you

begin

Before you create a collection using the AWS CLI, use the following procedure to
create required policies for the collection.

###### Note

In each of the following procedures, when you specify a name for a
collection, the name must meet the following criteria:

- Is unique to your account and AWS Region
- Contains only lowercase letters a-z, the numbers 0–9, and
  the hyphen (-)
- Contains between 3 and 32 characters

###### To create required policies for a collection

1. Open the AWS CLI and run the following command to create an [encryption policy](serverless-encryption.md "serverless-encryption.md") with a
   resource pattern that matches the intended name of the collection.

```
aws opensearchserverless create-security-policy \
  --name `policy name` \
  --type encryption --policy "{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/`collection name`\"]}],\"AWSOwnedKey\":true}"
```

For example, if you plan to name your collection
_logs-application_, you might create an
encryption policy like this:

```
aws opensearchserverless create-security-policy \
  --name logs-policy \
  --type encryption --policy "{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/logs-application\"]}],\"AWSOwnedKey\":true}"
```

If you plan to use the policy for additional collections, you can make
the rule more broad, such as `collection/logs*` or
`collection/*`. 2. Run the following command to configure network settings for the
collection using a [network
policy](serverless-network.md "serverless-network.md"). You can create network policies after you create a
collection, but we recommend doing it beforehand.

```
aws opensearchserverless create-security-policy \
  --name `policy name` \
  --type network --policy "[{\"Description\":\"`description`\",\"Rules\":[{\"ResourceType\":\"dashboard\",\"Resource\":[\"collection\/`collection name`\"]},{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/`collection name`\"]}],\"AllowFromPublic\":true}]"
```

Using the previous _logs-application_ example, you
might create the following network policy:

```
aws opensearchserverless create-security-policy \
  --name logs-policy \
  --type network --policy "[{\"Description\":\"Public access for logs collection\",\"Rules\":[{\"ResourceType\":\"dashboard\",\"Resource\":[\"collection\/logs-application\"]},{\"ResourceType\":\"collection\",\"Resource\":[\"collection\/logs-application\"]}],\"AllowFromPublic\":true}]"
```

## Creating a collection

The following procedure uses the [CreateCollection](../ServerlessAPIReference/API_CreateCollection.md "../ServerlessAPIReference/API_CreateCollection.md") API action to create a collection of type
`SEARCH` or `TIMESERIES`. If you don't specify a
collection type in the request, it defaults to `TIMESERIES`. For more
information about these types, see [Choosing a collection type](serverless-overview.md#serverless-usecase "serverless-overview.md#serverless-usecase"). To create a _vector
search_ collection, see [Working with vector search collections](serverless-vector-search.md "serverless-vector-search.md").

If your collection is encrypted with an AWS owned key, the
`kmsKeyArn` is `auto` rather than an ARN.

###### Important

After you create a collection, you won't be able to access it unless it
matches a data access policy. For more information, see [Data access control for Amazon OpenSearch Serverless](serverless-data-access.md "serverless-data-access.md").

###### To create a collection

1. Verify that you created required policies described in [Before you
   begin](#serverless-create-cli-before-you-begin "#serverless-create-cli-before-you-begin").
2. Run the following command. For `type` specify either
   `SEARCH` or `TIMESERIES`.

```
aws opensearchserverless create-collection --name "`collection name`" --type `collection type` --description "`description`"
```

## Creating a

collection with an automatic semantic enrichment index

Use the following procedure to create a new OpenSearch Serverless collection with an index
that is configured for [automatic semantic enrichment](serverless-semantic-enrichment.md "serverless-semantic-enrichment.md"). The procedure uses the OpenSearch Serverless [CreateIndex](../ServerlessAPIReference/API_CreateIndex.md "../ServerlessAPIReference/API_CreateIndex.md") API action.

**To create a new collection with an index configured for
automatic semantic enrichment**

Run the following command to create the collection and an index.

```
aws opensearchserverless create-index \
--region `Region ID` \
--id `collection name` --index-name `index name` \
--index-schema \
'`mapping in json`'
```

Here's an example.

```
aws opensearchserverless create-index \
--region us-east-1 \
--id conversation_history --index-name conversation_history_index \
--index-schema \
'{
    "mappings": {
        "properties": {
            "age": {
                "type": "integer"
            },
            "name": {
                "type": "keyword"
            },
            "user_description": {
                "type": "text"
            },
            "conversation_history": {
                "type": "text",
                "semantic_enrichment": {
                    "status": "ENABLED",
                    // Specifies the sparse tokenizer for processing multi-lingual text
                    "language_option": "MULTI-LINGUAL",
                    // If embedding_field is provided, the semantic embedding field will be set to the given name rather than original field name + "_embedding"
                    "embedding_field": "conversation_history_user_defined"
                }
            },
            "book_title": {
                "type": "text",
                "semantic_enrichment": {
                    // No embedding_field is provided, so the semantic embedding field is set to "book_title_embedding"
                    "status": "ENABLED",
                    "language_option": "ENGLISH"
                }
            },
            "abstract": {
                "type": "text",
                "semantic_enrichment": {
                    // If no language_option is provided, it will be set to English.
                    // No embedding_field is provided, so the semantic embedding field is set to "abstract_embedding"
                    "status": "ENABLED"
                }
            }
        }
    }
}'
```
