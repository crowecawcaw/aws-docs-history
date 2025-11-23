# Using both external

data and fine-grained data in Amazon SageMaker Unified Studio visual ETL jobs

When you use visual ETL, you must select a permission mode to use with your visual ETL
flow.

Permission mode is a configuration available to Spark compute resources such as Glue ETL or
EMR Serverless. It configures Spark to access different types of data based on the permissions
configured for that data. There are two configuration options for permission mode:

- Compatibility mode. This is a configuration for data managed using full-table access,
  meaning the compute engine can access all rows and columns in the data.
  Choosing this option enables your compute to work with data assets from AWS and from external systems.
- Fine-grained mode. This is a configuration for data managed using fine-grained access controls,
  meaning the compute engine can only access specific rows and columns from the full dataset.
  Choosing this option enables your Glue ETL
  to work with data asset subscriptions from Amazon SageMaker Catalog.
  In cases where you want to use both data configured with fine-grained access and data
  from external sources that you connect to your project, you can use two visual ETL jobs and
  orchestrate them to run together using workflows. To do this, complete the following
  steps.

###### Combining jobs with different kinds of data in visual ETL

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project you want to use visual ETL in.
3. Choose **Visual ETL** from the **Build**
   menu.
4. Choose **Create visual ETL job**.
5. Choose to configure the visual ETL job with full-table access using the AWS Glue ETL
   compute named **project.spark.fineGrained**.
6. Configure your visual ETL job to ingest the subscribed data to an Amazon S3 target used
   for temporary staging. This can be done by using the plus icon and adding an lakehouse architecture node
   as a data source and an Amazon S3 node as a data target, then connecting the nodes on the
   diagram.
7. Select the lakehouse architecture node and configure it to point to the data you want to use.
   1. Under **Database**, choose the name of the database you want to
      use.
   2. Under **Table**, choose the name of the table you want to
      use.

8. Configure the Amazon S3 node to point to a new location.
   1. Under **S3 URI**, create a new Amazon S3 folder name and note the
      location for later use.
   2. Under **Mode**, select **Overwrite** to clear
      the Amazon S3 bucket and overwrite it with new data when you are ready to use it
      again.
   3. (Optional) Configure the other settings as desired.

9. Save the flow and run it using **project.spark.fineGrained** to
   verify correctness of the results.
10. Create a new visual ETL job that uses the AWS Glue ETL compute named
    **project.spark.compatibility**.
11. Configure this second visual ETL job to combine the data from the staging S3
    location and the data accessible through full-table access to generate the final
    result.
    1. Select the plus icon. Under **Data sources**, select Amazon S3 and
       place the node on the diagram.
    2. Select the Amazon S3 node to configure it.
    3. Under **S3 URI**, enter the Amazon S3 folder location you used in
       the first visual ETL job.
    4. Use the plus icon, and under **Data sources**, select an
       external data source to add to your visual ETL job. Place the node on the
       diagram.
    5. Use the plus icon to add a data target and place the data target node on the
       diagram.
    6. Select the external data source and the data target to edit the configurations
       as desired and point to the locations you want to use.
    7. Use the plus icon, and under **Transforms**, select the
       **Join** transform. Place the transform on your diagram.
    8. Connect the Amazon S3 node containing the data from the first flow and the other data
       source to the data target using the **Join** transform.

12. Save the second flow and run it using
    **project.spark.compatibility** to verify correctness of the
    results.
13. Orchestrate these two visual ETL jobs using Amazon SageMaker Unified Studio workflows. For more
    information, see [Scheduling and running visual jobs in
    Identity Center-based domains](identity-center-schedule-visual-etl.md "identity-center-schedule-visual-etl.md") and [Create a code workflow](create-workflow.md#workflow-create "create-workflow.md#workflow-create").

Make sure that the workflow is configured so that the first visual ETL job finishes
running before the second visual ETL job runs. By default, they'll run in succession,
one after the other. This can also be configured using the
`wait_for_completion` param, as shown in [Sample code workflow](create-workflow.md#workflows-sample "create-workflow.md#workflows-sample").
