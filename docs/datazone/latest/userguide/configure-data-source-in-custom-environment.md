# Configure a data source in

an AWS service environment

Complete the following procedure to configure a data source in an AWS service
environment.

1. Sign in to the AWS Management Console and open the Amazon DataZone management
   console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose the **Blueprints** tab and then choose the custom
   AWS service blueprint.
3. Under **Created environments**, choose the AWS service
   environment where you want to configure a data source.
4. Choose the **Data sources** tab, choose
   **Add**, specify the following, and then choose
   **Add**.
   - **Name** - data source name.
   - **Resource** - choose either AWS Glue or Amazon
     Redshift.
     - For AWS Glue, specify the resource database.
     - For Amazon Redshift, choose either
       **Cluster** or
       **Serverless**, and then specify the
       **Redshift Credentials**, including a new
       or existing AWS secret, a cluster or serverless workgroup you
       want to use when creating environments, the database you want to
       use when creating environments, and the schema within the
       specified database.

   - **Permissions** - specify a manage access role that
     will provide Amazon DataZone with authorization to ingest and manage access
     to tables in AWS Lake Formation (for AWS Glue) or that will provide
     Amazon DataZone with authorization to ingest and manage access to tables in
     Amazon Redshift.
   - **Use for data consumption** - in Amazon DataZone, project
     members can consume data through subscription targets which Amazon DataZone
     uses to enable the access to the data for which you have subscribed in
     your projects. Specify whether to also add this data source as a
     subscription target.
