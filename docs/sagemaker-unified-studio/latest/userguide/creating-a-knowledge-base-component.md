# Create an Amazon Bedrock Knowledge Base component

You can create a knowledge base as a component in an Amazon Bedrock in SageMaker Unified Studio project. You then add
the knowledge base to an chat agent app or flow app. Alternatively, you can create a
knowledge base when you [design](create-chat-app-with-components.md#chat-app-add-data-source "create-chat-app-with-components.md#chat-app-add-data-source") the app. When
you create a knowledge base, you choose a data source, such as a local file or web crawler.

In this section you learn about the various data sources that you can use and how to create
a knowledge base component.

###### Topics

- [Use a Local file as a data source](data-source-document.md "data-source-document.md")
- [Use a web crawler as a data source](data-source-document-web-crawler.md "data-source-document-web-crawler.md")
- [Use project data as a data source](data-source-project.md "data-source-project.md")
- [Understanding security boundaries with structured data sources in an Amazon Bedrock knowledge
  base](kb-security-boundaries.md "kb-security-boundaries.md")
- [Chunking and parsing with knowledge bases](kb-chunking-parsing.md "kb-chunking-parsing.md")
  You can create a Knowledge base as a component in an Amazon Bedrock in SageMaker Unified Studio project. If you are
  creating an app, you can also create a Knowledge Base when you configure the app. When you create
  a Knowledge Base, you choose your data source, an embeddings model for transforming your data into vectors,
  and a vector store to store and manage the vectors. You can also specify how the Knowledge Base should preprocess data from the data source, either through chunking or parsing.
  The following procedure demonstrates how to create a Knowledge Base in Amazon Bedrock in SageMaker Unified Studio.

###### To create a Knowledge Base

1.  Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2.  Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3.  Choose the **Build** menu at the top of the page.
4.  In the **MACHINE LEARNING & GENERATIVE AI** section, choose
    **My apps**.
5.  In the **Select or create a new project to continue** dialog box, select the project that you want to use.
6.  In the left pane, choose **Asset gallery**.
7.  Choose **My components**.
8.  In the **Components** section, choose **Create
    component** and then **Knowledge Base**. The **Create
    Knowledge Base** pane is shown.
9.  For **Name**, enter a name for the Knowledge Base.
10. For **Description**, enter a description for the Knowledge
    Base.
11. In **Add data sources**, do one of the following:
    - Use a document as a data source by doing the following:

          1. Choose **Local file**.
          2. Choose **Click to upload** and upload the document that you want the
           Knowledge Base to use. Alternatively, add your source documents by dragging and dropping
           the document from your computer.

      For more information, see [Use a Local file as a data source](data-source-document.md "data-source-document.md").

    - Use a web crawler as a data source by doing the following:
      1. Choose **Web crawler**.
      2. Provide the **Source URLs** of the URLs you want to crawl. You can
         add up to 9 additional URLs by selecting **Add Source URLs**. By
         providing a source URL, you are confirming that you are authorized to crawl its
         domain.
      3. (Optional) Choose **Specify web crawler configs** to make the
         following optional configuration changes:
         - **Website domain range**. Set the domain that you want the
           Knowledge Base to crawl. For more information, see [Website domain range for crawling URLs](data-source-document-web-crawler.md#ds-sync-scope "data-source-document-web-crawler.md#ds-sync-scope").
         - **Maximum throttling of crawling speed**. Set the speed at which
           the Knowledge Base crawls through the source URLs. For more information, see [Throttle crawling speed](data-source-document-web-crawler.md#ds-throttle-crawling "data-source-document-web-crawler.md#ds-throttle-crawling").
         - **URL regex filter**. Set regex filters for including
           (**Include patterns**) or excluding **Exclude
           patterns** URLS from the web crawl. For more information, see [Use a URL regex filter to include or exclude URLs](data-source-document-web-crawler.md#ds-inclusion-exclusion "data-source-document-web-crawler.md#ds-inclusion-exclusion").
         - Choose **Back** to leave the web crawler configuration pane.

12. In **Configurations**, under **Data storage and processing**, do the following:
    1. For **Embeddings model**, select a foundation model from the drop down to use for transforming your data into vector embeddings.
    2. For **Embedding type** and **Vector dimensions**, select an option from the dropdown to optimize accuracy, cost, and latency.
       Your options for embedding types and vector dimensions may be limited depending on the embeddings model that you chose.

    ###### Note

    Amazon OpenSearch Serverless is the only vector store that supports binary vector embeddings. Floating-point vector embeddings are supported by all available vector stores. 3. For **Vector store** choose from one of the following options:

        * **Vector engine for Amazon OpenSearch Serverless** ‐ Provides contextually relevant responses across billions of vectors in milliseconds.
         Supports searches combined with text-based keywords for hybrid requests.
        * **Amazon S3 vectors** ‐ Optimizes cost-effectiveness, durability, and latency for storage of large, long-term vector data sets. Amazon S3 vector buckets do not support web crawler data sources.
        * **Amazon Neptune Analytics (GraphRAG)** ‐ Provides high-performance graph analytics and graph-based Retrieval Augmented Generation (GraphRAG) solutions. You must have access to Claude 3 Haiku in order to use this vector store. Contact your administrator if you do not have the necessary permissions.

    ###### Note

    Support for Amazon S3 vectors is in preview release for Amazon Bedrock in SageMaker Unified Studio and is subject to change.

    Once you select an option for your vector store, Amazon Bedrock in SageMaker Unified Studio will create the vector store on your behalf. 4. For **Chunking strategy**, choose either **Default**, **Fixed sized**, **Hierarchical**, **Semantic**, or **None**.
    These options represent different methods for breaking down data into smaller segments before embedding. 5. For **Parsing strategy**, choose either **Bedrock default parser** or **Foundation model as a parser**. If you choose **Foundation model as a parser**, do the following:

        1. For **Choose a foundation model for parsing** select your preferred
         foundation model. You can only choose models that your administrator has enabled for
         parsing. If you don't see a suitable model, contact your administrator.
        2. (Optional) Overwrite the **Instructions for the parser** to suit your
         specific needs.

13. Choose **Create** to create the Knowledge Base.
14. Use the Knowledge Base in an app, by doing one of the following:
    - If your app is a chat agent app, do [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md").
    - If your app is a flow app, do [Add a Knowledge Base component to a flow app](add-kb-component-prompt-flow-app.md "add-kb-component-prompt-flow-app.md").
