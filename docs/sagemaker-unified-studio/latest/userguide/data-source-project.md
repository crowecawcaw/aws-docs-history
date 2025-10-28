# Use project data as a data source

You can configure an Amazon Bedrock knowledge base to use data sources that are already
configured for your project.

###### Topics

- [Project data sources](#data-source-project-data-sources "#data-source-project-data-sources")
- [Create a knowledge base with a project data source](#data-source-project-procedure "#data-source-project-procedure")

## Project data sources

You can include the following data sources from your project:

### Amazon S3 bucket

[Amazon S3](../../../s3.md "../../../s3.md") is an object storage service that
stores data as objects within buckets. You can use files in your project's bucket as a
data source for a knowledge base.

### Amazon Redshift

[Amazon Redshift](../../../redshift.md "../../../redshift.md") is a serverless data
warehouse service that automatically provisions and scales data warehouse capacity to
deliver high performance for demanding and unpredictable workloads without the need to
manage infrastructure.

You can include all data tables from an Amazon Redshift database or select up to 50 data
tables from the available schemas. After selecting the tables, you can select the
columms that you want include. You can also preview data from the database, based on the
selected columns.

### lakehouse architecture

[lakehouse architecture](../../../sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.md "../../../sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.md") unifies your data across Amazon S3 data
lakes and Amazon Redshift data warehouses.

## Create a knowledge base with a project data source

The following procedure shows how to create a knowledge base with an Amazon S3 bucket, an Amazon Redshift data warehouse,
or with lakehouse architecture.

###### To create a knowledge base with a project data source

1. Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator.
2. Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md").
3. Choose the **Build** menu at the top of the page.
4. In the **MACHINE LEARNING & GENERATIVE AI** section, choose
   **My apps**.
5. In the **Select or create a new project to continue** dialog box, select the project that you want to use.
6. In the left pane, choose **Asset gallery**.
7. Choose **My components**.
8. In the **Components** section, choose **Create
   component** and then **Knowledge Base**. The
   **Create Knowledge Base** pane is shown.
9. For **Name**, enter a name for the Knowledge Base.
10. For **Description**, enter a description for the Knowledge
    Base.
11. For **Select data source type**, select **Project data
    sources**.
12. In **Select data source**, select an
    existing data source (**S3**, **Redshift**, or
    **Lakehouse**). Alternatively choose to add a new connection.
    - **S3** – Do the following:
      1. For **S3 URI** enter the the Amazon S3 Uniform
         Resource Identifier (URI) of the file or folder that you want to use.
         Alternatively, choose **Browse** to browse the bucket
         and choose file or folder.
      2. Choose **Save** to save your changes.

    - **Redshift (Lakehouse)** – Do the
      following:
      1. For **Select a database** select the database
         that you want to use.
      2. Choose **Update data tables and columns** to
         choose the tables and columns that you want to use. To preview the
         data from the selections you made, you choose
         **Data**.
      3. Choose **Save** to save your changes.

    - **Lakehouse** – Do the following:
      1. For **Select catalog** select the catalog that
         you want to use.
      2. For **Select a database** select the database
         that you want to use.
      3. Choose **Update data tables and columns** to
         choose the tables and columns that you want to use. To preview the
         data from the selections you made, you choose
         **Data**.
      4. Choose **Save** to save your changes.

    - (Optional) For Amazon Redshift and lakehouse architecture data sources you can make the following configuration
      changes:
      - **Maximum query time** ‐ Limit the time that a query can take by setting a maximum query time, in seconds.
      - **Descriptions** ‐ Add descriptions and annotations to the names of tables and columns to improve the accuracy of responses from a chat agent app.
      - **Curated queries** ‐ Use curated queries that help guide the agent to create better responses. A
        curated query is an example question along with the matching SQL query for the
        question.

13. Choose **Create** to create the Knowledge Base.
14. Use the Knowledge Base in an app, by doing one of the following:
    - If your app is a chat agent app, do [Add an Amazon Bedrock Knowledge Base component to a chat agent app](add-kb-component-chat-app.md "add-kb-component-chat-app.md").
    - If your app is a flow app, do [Add a Knowledge Base component to a flow app](add-kb-component-prompt-flow-app.md "add-kb-component-prompt-flow-app.md").
