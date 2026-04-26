# Synchronize an Amazon Bedrock Knowledge Base

After you create a Knowledge Base data source, you synchronize your data so that the data can be
queried. Synchronization converts the raw data in your data source into vector embeddings, based
on the vector embeddings model and configurations you specified when you
[Created](creating-a-knowledge-base-component.md "creating-a-knowledge-base-component.md") the Knowledge Base.

If the data source is a web crawler, synchronization time can vary from minutes to hours,
depending on the URLs you define.

###### To synchronize a Knowledge Base

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. In the left navigation pane, under **Generative AI**, choose **AI apps**.
4. From the project selector dropdown at the top of the page, choose the project that you want to use.
5. In the left pane, choose **Asset gallery**.
6. In **Asset gallery**, choose **My components**.
7. Find the Knowledge Base that you want to synchronize, and choose the menu option
   and select **Sync**.
8. Wait until the Knoweledge Synchronization completes.
