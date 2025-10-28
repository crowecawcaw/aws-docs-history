# Use a Local file as a data source

You can add a local file (document) as a data source. A document contains information that
you want the model to use when generating a response. By using a document as a data source
for a knowledge base, your app users can chat with a document. For example, they can use a
document to answers questions, make an analysis, create a summary, itemize fields in a
numbered list, or rewrite content.

You can use a document as a data source in a chat agent app and a flow app.

The document file must be in PDF, MD, TXT, DOC, DOCX, HTML, CSV, XLS or XLSX format. The
maximum file size is 50MB. You can upload up to 50 documents to a knowledge base.

###### To create a Knowledge Base with a local file

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. Choose the **Build** menu at the top of the page.
4. In the **MACHINE LEARNING & GENERATIVE AI** section, choose
   **My apps**.
5. In the **Select or create a new project to continue** dialog box, select the project that you want to use.
6. In the left pane, choose **Asset gallery**.
7. Choose **My components**.
8. In the **Components** section, choose **Create
   component** and then **Knowledge Base**. The **Create
   Knowledge Base** pane is shown.
9. For **Name**, enter a name for the Knowledge Base.
10. For **Description**, enter a description for the Knowledge
    Base.
11. In **Select data source type**, Select **Local file**:
12. Choose **Click to upload** and upload the document that you want the
    Knowledge Base to use. Alternatively, add your source documents by dragging and dropping
    the document from your computer.
13. For **parsing** Choose either **default** parsing or
    choose **parsing with foundation model**.
14. If you choose **parsing with foundation model**, do the following:
    1. For **Choose a foundation model for parsing** select your preferred
       foundation model. You can only choose models that your administrator has enabled for
       parsing. If you don't see a suitable model, contact your administrator.
    2. (Optional) Overwrite the **Instructions for the parser** to suit your
       specific needs. For more information,
       see [Chunking and parsing with knowledge bases](kb-chunking-parsing.md "kb-chunking-parsing.md").

15. (Optional) For **Chunking strategy** Choose a chunking strategy
    for your knowledge base. For more information, see [Chunking and parsing with knowledge bases](kb-chunking-parsing.md "kb-chunking-parsing.md").
16. (Optional) For **Embeddings model**, choose a model for converting your
    data into vector embeddings, or use the default model.
17. Choose **Create** to create the Knowledge Base.
18. Use the Knowledge Base in an app, by doing one of the following:
    - If your app is a chat agent app, do [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md").
    - If your app is a flow app, do [Add a Knowledge Base component to a flow app](add-kb-component-prompt-flow-app.md "add-kb-component-prompt-flow-app.md").
