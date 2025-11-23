# Query a knowledge base and retrieve data

###### Important

Guardrails are applied only to the input and the generated response from the LLM. They are not applied to the references
retrieved from Knowledge Bases at runtime.

After your knowledge base is set up, you can query it and retrieve chunks from your source data that is relevant to the query by using the [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") API operation. You can also [use a reranking model](rerank.md "rerank.md") instead of the default Amazon Bedrock Knowledge Bases ranker to rank source chunks for relevance during retrieval.

To learn how to query your knowledge base, choose the tab for your preferred method, and then follow the steps:

Console

###### To test your knowledge base

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. In the left navigation pane, choose **Knowledge bases**.
3. In the **Knowledge bases** section, do one of the following actions:
   - Choose the radio button next to the knowledge base you want to test and select **Test knowledge base**. A test window expands from the right.
   - Choose the knowledge base that you want to test. A test window expands from the right.

4. In the test window, clear **Generate responses for your query** to return information retrieved directly from your knowledge base.
5. (Optional) Select the configurations icon (

![Three horizontal sliders with adjustable circular controls for settings or parameters.](images/icons/configurations.png)

) to open up **Configurations**. For information about configurations, see [Configure and customize queries and response
generation](kb-test-config.md "kb-test-config.md"). 6. Enter a query in the text box in the chat window and select **Run** to return responses from the knowledge base. 7. The source chunks are returned directly in order of relevance. Images extracted from your data source can also be returned as a source chunk. 8. To see details about the returned chunks, select **Show source details**.

    * To see the configurations that you set for query, expand **Query configurations**.
    * To view details about a source chunk, expand it by choosing the right arrow (

     ![Play button icon with a triangular shape pointing to the right.](images/icons/caret-right-filled.png)

     ) next to it. You can see the following information:




    	+ The raw text from the source chunk. To copy this text, choose the copy icon (

    	 ![Icon representing a crop or resize function, with two overlapping rectangles.](images/icons/copy.png)

    	 ). If you used Amazon S3 to store your data, choose the external link icon (

    	 ![Icon of a square with an arrow pointing outward from its top-right corner.](images/icons/external.png)

    	 ) to navigate to the S3 object containing the file.
    	+ The metadata associated with the source chunk, if you used Amazon S3 to store your data. The attribute/field keys and values are defined in the `.metadata.json` file that's associated with the source document. For more information, see the **Metadata and filtering** section in [Configure and customize queries and response
    	 generation](kb-test-config.md "kb-test-config.md").

###### Chat options

- Switch to generating responses based on the retrieved source chunks by turning on **Generate responses**. If you change the setting, the text in the chat window will be completely cleared.
- To clear the chat window, select the broom icon (

![Magnifying glass icon with a checkmark inside, symbolizing search or inspection.](/images/bedrock/latest/userguide/images/icons/broom.png)

).

- To copy all the output in the chat window, select the copy icon (

![Icon representing a crop or resize function, with two overlapping rectangles.](images/icons/copy.png)

).

API
To query a knowledge base and only return relevant text from data sources,
send a [Retrieve](../APIReference/API_agent-runtime_Retrieve.md "../APIReference/API_agent-runtime_Retrieve.md") request with an [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt").

The following fields are required:

| Field                   | Basic description                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| knowledgeBaseId         | To specify the knowledge base to query.                                                                                      |
| retrievalQuery          | Contains a `text` field to specify the<br>query.                                                                             |
| guardrailsConfiguration | Include guardrailsConfiguration fields such as `guardrailsId` and `guardrailsVersion` to use your guardrail with the request |

The following fields are optional:

| Field                  | Use case                                                                                                                                                                                                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nextToken              | To return the next batch of responses (see response fields below).                                                                                                                                                                                                                                                                              |
| retrievalConfiguration | To include [query<br>configurations](kb-test-config.md "kb-test-config.md") for customizing the vector<br>search. See [KnowledgeBaseVectorSearchConfiguration](../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md "../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md") for more information. |

You can use a reranking model over the default Amazon Bedrock Knowledge Bases ranking model by including the `rerankingConfiguration` field in the [KnowledgeBaseVectorSearchConfiguration](../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md "../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md"). The `rerankingConfiguration` field maps to a [VectorSearchRerankingConfiguration](../APIReference/API_agent-runtime_VectorSearchRerankingConfiguration.md "../APIReference/API_agent-runtime_VectorSearchRerankingConfiguration.md") object, in which you can specify the reranking model to use, any additional request fields to include, metadata attributes to filter out documents during reranking, and the number of results to return after reranking. For more information, see [VectorSearchRerankingConfiguration](../APIReference/API_agent-runtime_VectorSearchRerankingConfiguration.md "../APIReference/API_agent-runtime_VectorSearchRerankingConfiguration.md").

###### Note

If you the `numberOfRerankedResults` value that you specify is greater than the `numberOfResults` value in the [KnowledgeBaseVectorSearchConfiguration](../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md "../APIReference/API_agent-runtime_KnowledgeBaseVectorSearchConfiguration.md"), the maximum number of results that will be returned is the value for `numberOfResults`. An exception is if you use query decomposition (for more information, see the **Query modifications** section in [Configure and customize queries and response
generation](kb-test-config.md "kb-test-config.md"). If you use query decomposition, the `numberOfRerankedResults` can be up to five times the `numberOfResults`.

The response returns the source chunks from the data source as an array of [KnowledgeBaseRetrievalResult](../APIReference/API_agent-runtime_KnowledgeBaseRetrievalResult.md "../APIReference/API_agent-runtime_KnowledgeBaseRetrievalResult.md") objects in the `retrievalResults` field. Each [KnowledgeBaseRetrievalResult](../APIReference/API_agent-runtime_KnowledgeBaseRetrievalResult.md "../APIReference/API_agent-runtime_KnowledgeBaseRetrievalResult.md") contains the following fields:

| Field    | Description                                                                                                                                                                                                                                                      |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content  | Contains a text source chunk in the `text` or an image source chunk in the `byteContent` field. If the content is an image, the data URI of the base64-encoded content is returned in the following format: `data:image/jpeg;base64,`${base64-encoded string}``. |
| metadata | Contains each metadata attribute as a key and the metadata value as a JSON value that the key maps to.                                                                                                                                                           |
| location | Contains the URI or URL of the document that the source chunk belongs to.                                                                                                                                                                                        |
| score    | The relevancy score of the document. You can use this score to analyze the ranking of results.                                                                                                                                                                   |

If the number of source chunks exceeds what can fit in the response, a value is returned in the `nextToken` field. Use that value in another request to return the next batch of results.

If the retrieved data contains images, the response also returns the following response headers, which contain metadata for source chunks returned in the response:

- `x-amz-bedrock-kb-byte-content-source` – Contains the Amazon S3 URI of the image.
- `x-amz-bedrock-kb-description` – Contains the base64-encoded string for the image.

###### Note

You can't filter on these metadata response headers when [configuring metadata filters](kb-test-config.md "kb-test-config.md").

###### Note

If you receive an error that the prompt exceeds the character limit while generating responses, you can shorten the prompt in the following ways:

- Reduce the maximum number of retrieved results (this shortens what is filled in for the $search\_results$ placeholder in the [Knowledge base prompt templates:
  orchestration & generation](kb-test-config.md#kb-test-config-prompt-template "kb-test-config.md#kb-test-config-prompt-template")).
- Recreate the data source with a chunking strategy that uses smaller chunks (this shortens what is filled in for the $search\_results$ placeholder in the [Knowledge base prompt templates:
  orchestration & generation](kb-test-config.md#kb-test-config-prompt-template "kb-test-config.md#kb-test-config-prompt-template")).
- Shorten the prompt template.
- Shorten the user query (this shortens what is filled in for the $query$ placeholder in the [Knowledge base prompt templates:
  orchestration & generation](kb-test-config.md#kb-test-config-prompt-template "kb-test-config.md#kb-test-config-prompt-template")).
