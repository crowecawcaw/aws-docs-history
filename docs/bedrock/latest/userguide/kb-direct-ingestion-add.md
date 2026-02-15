# Ingest documents directly into a knowledge base

This topic describes how to ingest documents directly into a knowledge base. Restrictions apply for the types of documents that you can directly ingest depending on your data source. Refer to the following table for restrictions on the methods that you can use to specify the documents to ingest:

| Data source type | Document defined in-line                                                     | Document in Amazon S3 location                                   |
| ---------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Amazon S3        | Red circular icon with an X symbol, indicating cancellation or denial.<br>No | Green circular icon with a white checkmark symbol inside.<br>Yes |
| Custom           | Green circular icon with a white checkmark symbol inside.<br>Yes             | Green circular icon with a white checkmark symbol inside.<br>Yes |

Expand the section that corresponds your use case:

###### Note

When you use the console, you can ingest up to 10 documents directly into your knowledge
base. If you use the `IngestKnowledgeBaseDocuments` API instead, you can ingest up to
25 documents into your knowledge base. For more information about this quota, see the [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock")
in the _AWS General Reference guide_.

To add or modify documents directly in the AWS Management Console, do the following:

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Knowledge bases** section, select the knowledge base to ingest documents into.
4. In the **Data source** section, select the data source for which you want to add, modify, or delete documents.
5. In the **Documents** section, choose **Add documents**. Then, do one of the following:
   - To add or modify a document directly, select **Add documents directly**. Then, do the following:
     1. In the **Document identifier** field, specify a unique name for the document. If you specify a name that already exists in the data source, the document will be replaced.
     2. To upload a document, select **Upload**. To define a document inline, select **Add document inline**, choose a format, and enter the text of the document in the box.
     3. (Optional) To associate metadata with the document, select **Add metadata** and enter a key, type, and value.

   - To add or modify a document by specifying its S3 location, select **Add S3 documents**. Then, do the following:
     1. In the **Document identifier** field, specify a unique name for the document. If you specify a name that already exists in the data source, the document will be replaced.
     2. Specify whether the **S3 location** of the document is in your current AWS account or a different one. Then specify the S3 URI of the document.
     3. (Optional) To associate metadata with the document, choose a **Metadata source**. Specify the S3 URI of the metadata or select **Add metadata** and enter a key, type, and value.

6. To ingest the document and any associated metadata, choose **Add**.
   To ingest documents directly into a knowledge base using the Amazon Bedrock API, send an [IngestKnowledgeBaseDocuments](../APIReference/API_agent_IngestKnowledgeBaseDocuments.md "../APIReference/API_agent_IngestKnowledgeBaseDocuments.md")
   request with an [Agents for Amazon Bedrock build-time endpoint](../../../general/latest/gr/bedrock.md#bra-bt "../../../general/latest/gr/bedrock.md#bra-bt") and specify the ID of the knowledge base and of the data source that
   it's connected to.

###### Note

If you specify a document identifier or S3 location that already exists in the knowledge base, the document will be overwritten with the new content.

The request body contains one field, `documents`, that maps to an array of [KnowledgeBaseDocument](../APIReference/API_agent_KnowledgeBaseDocument.md "../APIReference/API_agent_KnowledgeBaseDocument.md") objects, each of which represents the content and optional metadata of a document to add to the data source and to ingest into the knowledge base. A [KnowledgeBaseDocument](../APIReference/API_agent_KnowledgeBaseDocument.md "../APIReference/API_agent_KnowledgeBaseDocument.md") object contains the following fields:

- content – Maps to a [DocumentContent](../APIReference/API_agent_DocumentContent.md "../APIReference/API_agent_DocumentContent.md") object containing information about the content of the document to add.
- metadata – (Optional) Maps to a [DocumentMetadata](../APIReference/API_agent_DocumentMetadata.md "../APIReference/API_agent_DocumentMetadata.md") object containing information about the metadata of the document to add. For more information about how to use metadata during retrieval, see the **Metadata and filtering** section in [Configure and customize queries and response
  generation](kb-test-config.md "kb-test-config.md").
  Select a topic to learn how to ingest documents for different data source types or to see examples:

###### Topics

- [Ingest a document into a knowledge base connected to a custom data source](#kb-direct-ingestion-add-custom "#kb-direct-ingestion-add-custom")
- [Ingest a document into a knowledge base connected to an Amazon S3 data source](#kb-direct-ingestion-add-s3 "#kb-direct-ingestion-add-s3")
- [Example request bodies](#w2aac28c10c23c19c17c11b3c19 "#w2aac28c10c23c19c17c11b3c19")

### Ingest a document into a knowledge base connected to a custom data source

If the `dataSourceId` you specify belongs to a custom data source, you can add content and metadata for each [KnowledgeBaseDocument](../APIReference/API_agent_KnowledgeBaseDocument.md "../APIReference/API_agent_KnowledgeBaseDocument.md") object in the `documents` array.

The content of a document added to a custom data source can be defined in the following ways:

You can define the following types of documents in-line:

Text
If the document is text, the [DocumentContent](../APIReference/API_agent_DocumentContent.md "../APIReference/API_agent_DocumentContent.md") object should be in the following format:

```
{
    "custom": {
        "customDocumentIdentifier": {
            "id": "string"
        },
        "inlineContent": {
            "textContent": {
                "data": "string"
            },
            "type": "TEXT"
        },
        "sourceType": "IN_LINE"
    },
    "dataSourceType": "CUSTOM"
}
```

Include an ID for the document in the `id` field and the text of the document in the `data` field.

Bytes
If the document contains more than text, convert it into a
Base64-string. The [DocumentContent](../APIReference/API_agent_DocumentContent.md "../APIReference/API_agent_DocumentContent.md") object should then be in the
following format:

```
{
    "custom": {
        "customDocumentIdentifier": {
            "id": "string"
        },
        "inlineContent": {
            "byteContent": {
                "data": blob,
                "mimeType": "string"
            },
            "type": "BYTE"
        },
        "sourceType": "IN_LINE"
    },
    "dataSourceType": "CUSTOM"
}
```

Include an ID for the document in the `id` field, the Base64-encoded document in the `data` field, and the MIME type in the `mimeType` field.

If you're ingesting a document from an S3 location, the [DocumentContent](../APIReference/API_agent_DocumentContent.md "../APIReference/API_agent_DocumentContent.md") object in the `content` field should be of the following form:

```
{
    "custom": {
        "customDocumentIdentifier": {
            "id": "string"
        },
        "s3Location": {
            "bucketOwnerAccountId": "string",
            "uri": "string"
        },
        "sourceType": "S3"
    },
    "dataSourceType": "CUSTOM"
}
```

Include an ID for the document in the `id` field, the owner of the S3 bucket that contains the document in `bucketOwnerAccountId` field, and the S3 URI of the document in the `uri` field.

The metadata for a document can be defined in the following ways:

If you define the metadata inline, the [DocumentMetadata](../APIReference/API_agent_DocumentMetadata.md "../APIReference/API_agent_DocumentMetadata.md") object in the `metadata` field should be in the following format:

```
{
    "inlineAttributes": [
        {
            "key": "string",
            "value": {
                "stringValue": "string",
                "booleanValue": boolean,
                "numberValue": number,
                "stringListValue": [ "string" ],
                "type": "STRING" | "BOOLEAN" | "NUMBER" | "STRING_LIST"
            }
        }
    ],
    "type": "IN_LINE_ATTRIBUTE"
}
```

For each attribute that you add, define the key in the `key` field. Specify the data type of the value in the `type` field and include the field that corresponds to the data type. For example, if you include a string, the attribute would be in the following format:

```
{
    "key": "string",
    "value": {
        "stringValue": "string",
        "type": "STRING"
    }
}
```

You can also ingest metadata from a file with the extension `.metadata.json` in an S3 location. For more information about the format of a metadata file, see the **Document metadata fields** section in [Connect to Amazon S3 for your knowledge base](s3-data-source-connector.md "s3-data-source-connector.md").

If the metadata is from an S3 file, the [DocumentMetadata](../APIReference/API_agent_DocumentMetadata.md "../APIReference/API_agent_DocumentMetadata.md") object in the `metadata` field should be in the following format:

```
{
    "s3Location": {
        "bucketOwnerAccountId": "string",
        "uri": "string"
    },
        "type": "S3_LOCATION"
    }
 }
```

Include the owner of the S3 bucket that contains the metadata file in `bucketOwnerAccountId` field, and the S3 URI of the metadata file in the `uri` field.

###### Warning

If you defined the content inline, you must define the metadata inline.

### Ingest a document into a knowledge base connected to an Amazon S3 data source

If the `dataSourceId` you specify belongs to an S3 data source, you can add content and metadata for each [KnowledgeBaseDocument](../APIReference/API_agent_KnowledgeBaseDocument.md "../APIReference/API_agent_KnowledgeBaseDocument.md") object in the `documents` array.

###### Note

For S3 data sources, you can add content and metadata only from an S3
location.

The content of an S3 document to add to S3 should be added to a [DocumentContent](../APIReference/API_agent_DocumentContent.md "../APIReference/API_agent_DocumentContent.md") object in the following format:

```
{
    "dataSourceType": "string",
    "s3": {
        "s3Location": {
            "uri": "string"
        }
    }
}
```

Include the owner of the S3 bucket that contains the document in `bucketOwnerAccountId` field, and the S3 URI of the document in the `uri` field.

The metadata for a document added to a custom data source can be defined in the following format:

```
{
    "s3Location": {
        "bucketOwnerAccountId": "string",
        "uri": "string"
    },
        "type": "S3_LOCATION"
    }
 }
```

###### Warning

Documents that you ingest directly into a knowledge base connected to an S3 data source aren't added to the S3 bucket itself. We recommend that you add these documents to the S3 data source as well so that they aren't removed or overwritten if you sync your data source.

### Example request bodies

Expond the following sections to see request bodies for different use cases with `IngestKnowledgeBaseDocuments`:

The following example shows the addition of one text document to a custom data source:

```
PUT /knowledgebases/`KB12345678`/datasources/`DS12345678`/documents HTTP/1.1
Content-type: application/json

{
   "documents": [
      {
         "content": {
            "dataSourceType": "CUSTOM",
            "custom": {
               "customDocumentIdentifier": {
                  "id": "MyDocument"
               },
               "inlineContent": {
                  "textContent": {
                     "data": "Hello world!"
                  },
                  "type": "TEXT"
               },
               "sourceType": "IN_LINE"
            }
         }
     }
   ]
}
```

The following example shows the addition of a PDF document to a custom data source:

```
PUT /knowledgebases/`KB12345678`/datasources/`DS12345678`/documents HTTP/1.1
Content-type: application/json

{
   "documents": [
      {
         "content": {
            "dataSourceType": "CUSTOM",
            "custom": {
               "customDocumentIdentifier": {
                  "id": "MyDocument"
               },
               "inlineContent": {
                  "byteContent": {
                     "data": "<Base64-encoded string>",
                     "mimeType": "application/pdf"
                  },
                  "type": "BYTE"
               },
               "sourceType": "IN_LINE"
            }
         }
     }
   ]
}
```

The following example shows the addition of one text document to a custom data source from an S3 location:

```
PUT /knowledgebases/`KB12345678`/datasources/`DS12345678`/documents HTTP/1.1
Content-type: application/json

{
   "documents": [
      {
         "content": {
            "dataSourceType": "CUSTOM",
            "custom": {
               "customDocumentIdentifier": {
                  "id": "MyDocument"
               },
               "s3": {
                "s3Location": {
                    "uri": "amzn-s3-demo-bucket"
                }
               },
               "sourceType": "S3"
            }
         }
     }
   ]
}
```

The following example shows the inline addition to a custom data source of a document alongside metadata containing two attributes:

```
PUT /knowledgebases/`KB12345678`/datasources/`DS12345678`/documents HTTP/1.1
Content-type: application/json

{
   "documents": [
      {
         "content": {
            "dataSourceType": "CUSTOM",
            "custom": {
               "customDocumentIdentifier": {
                  "id": "MyDocument"
               },
               "inlineContent": {
                  "textContent": {
                     "data": "Hello world!"
                  },
                  "type": "TEXT"
               },
               "sourceType": "IN_LINE"
            }
         },
         "metadata": {
            "inlineAttributes": [
               {
                  "key": "genre",
                  "value": {
                     "stringValue": "pop",
                     "type": "STRING"
                  }
               },
               {
                  "key": "year",
                  "value": {
                     "numberValue": 1988,
                     "type": "NUMBER"
                  }
               }
            ],
            "type": "IN_LINE_ATTRIBUTE"
         }
     }
   ]
}
```

The following example shows the addition of a document alongside metadata
to an S3 data source. You can include the metadata only through S3:

```
PUT /knowledgebases/`KB12345678`/datasources/`DS12345678`/documents HTTP/1.1
Content-type: application/json

{
    "documents": [
        {
            "content": {
                "dataSourceType": "S3",
                "s3": {
                "s3Location": {
                    "uri": "amzn-s3-demo-bucket"
                }
            }
        },
        "metadata": {
            "s3Location": {
                "bucketOwnerId": "111122223333",
                "uri": "amzn-s3-demo-bucket"
            },
                "type": "S3_LOCATION"
            }
        }
    ]
}
```
