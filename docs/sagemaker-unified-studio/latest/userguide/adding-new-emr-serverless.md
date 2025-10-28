# Adding a new EMR Serverless application

As a data worker, you can make use of EMR Serverless applications by adding them to a
project in the Amazon SageMaker Unified Studio Studio. Within a project, you can use both existing and new applications.
You can use existing applications at any time. However, in order to create a new EMR Serverless application,
the admin must enable blueprints.

After your admin has enabled blueprints:

1. From inside the project management view, select **Compute** from the navigation bar.
2. In the Compute panel, select the **Data processing** tab.
3. To add an instance of an Amazon EMR Serverless, select the **Add compute** dropdown menu
   and then choose **New compute**.
4. In the **Add compute** modal, you can select the type of compute you would like to add
   to your project. Select **EMR Serverless**.
5. The **Add compute** dialog box allows you to specify the name of the EMR Serverless
   application, provide a description, and choose a release of EMR Serverless that you
   want your application to use.
6. Choose the permission mode option that supports the data you will be
   using with the compute resource.
   - Select **project.spark.fineGrained** for data managed using fine-grained access,
     meaning the compute engine can only access specific rows and columns from the full dataset. Choosing this option configures your compute
     to work with data asset subscriptions from Amazon SageMaker Catalog.
   - Select **project.spark.compatibility** to configure permission mode
     to be compatible with data managed using full-table access,
     meaning the compute engine can access all rows and columns in the data.
     Choosing this option configures your compute to work with data assets from AWS and from external systems that you
     connect to from your project.

7. After configuring these settings, select **Add compute**. After a short time, your serverless
   application running EMR Serverless should be added to your project.
