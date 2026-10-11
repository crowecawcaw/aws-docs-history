

# Query a document without creating a knowledge base
<a name="knowledge-base-chatdoc"></a>

To query a single document without creating or configuring a knowledge base, use the [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) API operation with an external source. This workflow is available through the Agents for Amazon Bedrock Runtime API and AWS SDKs, rather than the Amazon Bedrock console.

The operation retrieves information from the document, uses a foundation model or inference profile to generate a response, and returns citations to the source. You can provide the document from an Amazon S3 location or include its byte content in the request.

**Note**  
You can include exactly one document in each request. If you include the document as byte content, the maximum file size is 10 MB.  
You can't use a reranker model when querying an external source.

Before you send a request, configure the permissions described in [Permissions to query external sources](kb-permissions.md#kb-permissions-chatdoc).

**To query an external document**

1. Prepare the document in one of the following ways:
   + Upload the document to Amazon S3.
   + Base64-encode the document to include it in the request.

1. Send a [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) request and configure the following fields:
   + Specify your query in `input.text`.
   + Set `retrieveAndGenerateConfiguration.type` to `EXTERNAL_SOURCES`.
   + In `externalSourcesConfiguration`, specify the model or inference profile ARN and the document source.

1. Use the `output` and `citations` fields from the response. For subsequent requests in the same conversation, include the `sessionId` returned by the first response.

The following example queries a document stored in Amazon S3:

```
{
    "input": {
        "text": "{{your query}}"
    },
    "retrieveAndGenerateConfiguration": {
        "type": "EXTERNAL_SOURCES",
        "externalSourcesConfiguration": {
            "modelArn": "{{model-or-inference-profile-arn}}",
            "sources": [
                {
                    "sourceType": "S3",
                    "s3Location": {
                        "uri": "s3://{{bucket-name}}/{{document-key}}"
                    }
                }
            ]
        }
    }
}
```

To include the document in the request instead, set `sourceType` to `BYTE_CONTENT` and replace `s3Location` with a `byteContent` object. Specify the file name in `identifier`, the MIME type in `contentType`, and the base64-encoded document in `data`.

You can optionally use `generationConfiguration` to customize the prompt, inference parameters, performance configuration, or guardrail. For field details, see [ExternalSourcesRetrieveAndGenerateConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ExternalSourcesRetrieveAndGenerateConfiguration.html) and [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html).