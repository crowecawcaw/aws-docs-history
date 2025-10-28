# Configure a

subscription target in an AWS service environment

Complete the following procedure to configure a subscription target in an AWS
service environment.

1. Sign in to the AWS Management Console and open the Amazon DataZone management
   console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone").
2. Choose the **Blueprints** tab and then choose the AWS
   service blueprint.
3. Under **Created environments**, choose the AWS service
   environment where you want to configure a subscription target.
4. Choose the **Subscription targets** tab, choose
   **Add**, specify the following, and then choose
   **Add**.
   - **Name** - subscription target name.
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
   - **Use for data consumption** - in Amazon DataZone, you can
     publish data to the data catalog through a data source that allows for
     metadata ingestion. Specify whether to also add this subscription target
     as a data source.
