# Chat with your document without a knowledge base configured

The **Chat with your document** feature in the Amazon Bedrock console allows you to easily
test play a knowledge base without the need to configure a knowledge base. You can load a
document or drag-and-drop a document in the console chat window to then start asking questions.
**Chat with your document** uses your document to answer questions, make an
analysis, create a summary, itemize fields in a numbered list, or rewrite content. **Chat
with your document** doesn't store your document or its data after use.

###### Note

The **Chat with your document** feature is currently best supported with
Anthropic Sonnet models. See [Supported models for
knowledge bases](knowledge-base-supported.md "knowledge-base-supported.md") for more information about how to access and use knowledge base models.

You can't use a reranker model when chatting with your document.

You can also easily prototype a chat or flow application without the need to configure a
knowledge base. Using [Amazon Bedrock Studio](br-studio.md "br-studio.md"), you can upload a document from your computer to provide the data or
'data source' for your application. Amazon Bedrock Studio, renamed to Amazon Bedrock IDE, is now available in Amazon
SageMaker Unified Studio. For more information, see [Amazon Bedrock IDE](../../../sagemaker-unified-studio/latest/userguide/bedrock.md "../../../sagemaker-unified-studio/latest/userguide/bedrock.md").

To use the **Chat with your document** feature as part of knowledge bases,
select the tab below and follow the steps.

Console

###### To chat with your document in Amazon Bedrock:

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/").
2. From the left navigation pane, select **Knowledge base** and choose **Chat with your document**.
3. In the **Chat with your document tab**, Select **Select a model** under **Model**.
4. Choose the model you want to use for document analysis and select **Apply**.
5. Enter a system prompt on the **Chat with your document** tab.
6. Under **Data** select **Your computer** or **S3**.
7. Choose **Select document** to upload your document. You can also drag-and-drop the document in the chat console in the box that says **Write a query**.

###### Note

File types: PDF, MD, TXT, DOC, DOCX, HTML, CSV, XLS, XLSX. There is a preset fixed token limit when using a file under 10MB. A text-heavy file that is smaller than 10MB can potentially be larger than the token limit. 8. Enter a custom prompt in the box that says **Write a query**. You can enter a custom prompt or use the default prompt. The loaded document and the prompt appear the bottom of the chat window. 9. Select **Run**. The response produces search results with an option **Show source chunks** that show the source material information for the answer. 10. To load a new file, select the X to delete the current file loaded into the chat window and drag and drop and new file. Enter a new prompt and select **Run**.

###### Note

Selecting a new file will wipe out previous queries and responses and will start a new session.
