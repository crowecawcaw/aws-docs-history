# Add an Amazon Bedrock Knowledge Base component to a chat agent app

In this procedure, you add a Knowledge Base component to an existing [chat agent app](create-chat-app.md "create-chat-app.md").

After adding a Knowledge Base component, you can make the following configuration changes.

###### Search type

You can select a strategy for searching data sources in your knowledge base. Default
search chooses the best option between hybrid search and semantic search for your vector
store. You can override the the default search type and choose to
use a hybrid search (semantic and text) or semantic search. Hybrid search combines
relevancy scores from semantic and text search to provide greater accuracy. Semantic
search Uses vector embeddings to deliver relevant results. For more information, see
[Amazon Bedrock Knowledge Bases now supports hybrid search](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-hybrid-search/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-hybrid-search/").

###### Maximum number of source chunks

When you query a knowledge base, the model returns up to five results in the response
by default. Each result corresponds to a source chunk. You can edit the maximum number
of retrieved results to return from the vector store. For more information, see [Chunking](kb-chunking-parsing.md#kb-chunking "kb-chunking-parsing.md#kb-chunking").

###### To add a Knowledge Base component to a chat agent app

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. If the project that you want to use isn't already open, do the following:
   1. Choose the current project at the top of the page. If a project isn't already open, choose **Select a project**.
   2. Select **Browse all projects**.
   3. In **Projects** select the project that you want
      to use.

4. Choose the **Build** menu option at the top of the page.
5. In **MACHINE LEARNING & GENERATIVE AI** choose **My apps**.
6. In **Apps** choose the chat agent app that you want to add the knowledge base component to.
7. In the **Configs** pane, choose **Data**.
8. Select **Use Knowledge Base**.
9. For **Select Knowledge Base**, select the Knowledge Base
   component that you want to use. To create a Knowledge Base component, see [Create an Amazon Bedrock Knowledge Base component](creating-a-knowledge-base-component.md "creating-a-knowledge-base-component.md").
10. (Optional) Choose **Edit advanced search configs** to set advanced
    search configurations.
    1. In **Search type**, turn on **Overide default
       search** to choose a different search type. You can choose from
       **Hybrid search** (Combines relevancy scores from
       semantic and text search to provide greater accuracy) or **Semantic
       search** (Uses vector embeddings to deliver relevant
       results).
    2. (Optional) In **Maximum number of source chunks**, choose
       the maximum number of source chunks to use.

11. Choose **Save** to save your changes.
