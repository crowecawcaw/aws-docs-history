#

Tutorial: Using the AWS Glue Connector for Elasticsearch

Elasticsearch is a popular open-source search and analytics engine for use cases such as log
analytics, real-time application monitoring, and clickstream analysis. You can use OpenSearch as a
data store for your extract, transform, and load (ETL) jobs by configuring the
AWS Glue Connector for Elasticsearch in AWS Glue Studio. This connector
is available for free from
[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6 "https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6").

###### Note

The [AWS Marketplace
Elasticsearch Spark Connector](https://aws.amazon.com/marketplace/pp/B08PPT2V5J "https://aws.amazon.com/marketplace/pp/B08PPT2V5J") has been deprecated. Please use the
[AWS Glue Connector for Elasticsearch](https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6 "https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6")
instead.

In this tutorial, we will show how to connect to your Amazon OpenSearch Service nodes with a minimal number of
steps.

###### Topics

- [Prerequisites](#tutorial-prerequisites "#tutorial-prerequisites")
- [Step 1: (Optional) Create an AWS secret for your OpenSearch
  cluster information](#tutorial-step1 "#tutorial-step1")
- [Step 2: Subscribe to the connector](#tutorial-step2 "#tutorial-step2")
- [Step 3: Activate the connector in AWS Glue Studio and create a
  connection](#tutorial-step3 "#tutorial-step3")
- [Step 4: Configure an IAM role for your ETL job](#tutorial-step4 "#tutorial-step4")
- [Step 5: Create a job that uses the OpenSearch connection](#tutorial-step5 "#tutorial-step5")
- [Step 6: Run the job](#tutorial-step6 "#tutorial-step6")

## Prerequisites

To use this tutorial, you must have the following:

- Access to AWS Glue Studio
- Access to an OpenSearch cluster in the AWS Cloud
- (Optional) Access to AWS Secrets Manager.

## Step 1: (Optional) Create an AWS secret for your OpenSearch

cluster information

To safely store and use your connection credential, save your credential in
AWS Secrets Manager. The secret you create will be used later in the tutorial by the
connection. The credential key-value pairs will be fed into the AWS Glue Connector for Elasticsearch
as normal connection options.

For more information about creating secrets, see [Creating and Managing Secrets with
AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the _AWS Secrets Manager User Guide_.

###### To create an AWS secret

1. Sign in to the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On either the service introduction page or the **Secrets** list page,
   choose **Store a new secret**.
3. On the **Store a new secret** page, choose **Other type of
   secret**. This option means that you must supply the structure and details of your
   secret.
4. Add a **Key** and **Value** pair
   for the OpenSearch cluster user name. For example:

`es.net.http.auth.user`: `username` 5. Choose **+ Add row**, and enter another key-value pair for the password.
For example:

`es.net.http.auth.pass`: `password` 6. Choose **Next**. 7. Enter a secret name. For example: **my-es-secret**. You can optionally
include a description.

Record the secret name, which is used later in this tutorial, and then choose
**Next**. 8. Choose **Next** again, and then choose **Store** to create
the secret.

### Next step

[Step 2: Subscribe to the connector](#tutorial-step2 "#tutorial-step2")

## Step 2: Subscribe to the connector

The AWS Glue Connector for Elasticsearch is available for free from
[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6#pdp-pricing "https://aws.amazon.com/marketplace/pp/prodview-v5ygernwn2gb6#pdp-pricing").

###### To subscribe to the AWS Glue Connector for Elasticsearch on AWS Marketplace

1. If you have not already configured your AWS account to use License Manager, do the
   following:
   1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager](https://console.aws.amazon.com/license-manager "https://console.aws.amazon.com/license-manager").
   2. Choose **Create customer managed license**.
   3. In the **IAM permissions (one-time setup)** window, choose **I
      grant AWS License Manager the required permissions**, and then choose
      **Grant permissions**.

   If you do not see this window, then you have already configured the necessary
   permissions.

2. Open the AWS Glue Studio console at
   [https://console.aws.amazon.com/gluestudio/](https://console.aws.amazon.com/gluestudio/ "https://console.aws.amazon.com/gluestudio/").
3. In the AWS Glue Studio console, expand the menu icon (
   ![3 short, horizontal lines in a vertical stack](images/nav-menu-icon.png)
   ), and then choose **Connectors** in the navigation
   pane.
4. On the **Connectors** page, choose **Go to
   AWS Marketplace**.
5. In AWS Marketplace, in the **Search AWS Glue Studio products** section, enter
   **AWS Glue Connector for Elasticsearch** in the search field, and then press
   Enter.
6. Choose the name of the connector, **AWS Glue Connector for Elasticsearch**.
7. On the product page for the connector, use the tabs to view information about the
   connector. When you're ready to continue, choose **Continue to
   Subscribe**.
8. Review the terms of use for the software. Click **Accept Terms**.
9. When the subscription process completes, you will see a notification: "Thank you for subscribing
   to this product! You can now configure your software." Above the banner will be the button
   **Continue to Configuration**. Choose **Continue to Configuration**.
10. Choose the Fulfillment option on the **Configure this software** page. You can either
    choose between AWS Glue 1.0/2.0 or AWS Glue 3.0.
    Then, choose **Continue to Launch**.

### Next step

[Step 3: Activate the connector in AWS Glue Studio and create a
connection](#tutorial-step3 "#tutorial-step3")

## Step 3: Activate the connector in AWS Glue Studio and create a

connection

After you choose **Continue to Launch**, you see the **Launch this software** page in AWS Marketplace.
After you use the link to activate the
connector in AWS Glue Studio, you create a connection.

###### To deploy the connector and create a connection in AWS Glue Studio

1. On the **Launch this software** page in the AWS Marketplace console, choose
   **Usage Instructions**, and then choose the link in the window that
   appears.

Your browser is redirected to the AWS Glue Studio console **Create marketplace
connection** page. 2. Enter a name for the connection. For example:
**my-es-connection**. 3. In the **Connection access** section, for **Connection credential
type**, choose **User name and password**. 4. For the **AWS secret**, enter the name of your secret. For example:
**my-es-secret**. 5. In the **Network options** section, enter the VPC information to connect
to OpenSearch cluster. 6. Choose **Create connection and activate connector**.

### Next step

[Step 4: Configure an IAM role for your ETL job](#tutorial-step4 "#tutorial-step4")

## Step 4: Configure an IAM role for your ETL job

When you create the AWS Glue ETL job, you specify an AWS Identity and Access Management (IAM) role for the
job to use. The role must grant access to all resources used by the job, including
Amazon S3 (for any sources, targets, scripts, driver files, and temporary directories),
and also AWS Glue Data Catalog objects.

The assumed IAM role for the AWS Glue ETL job must also have access to the secret that was
created in the previous section. By default, the AWS managed role `AWSGlueServiceRole`
does not have access to the secret. To set up access control for your secrets, see [Authentication
and Access Control for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access.md "../../../secretsmanager/latest/userguide/auth-and-access.md") and [Limiting Access to Specific Secrets](../../../secretsmanager/latest/userguide/auth-and-access_identity-based-policies.md#permissions_grant-limited-resources "../../../secretsmanager/latest/userguide/auth-and-access_identity-based-policies.md#permissions_grant-limited-resources").

###### To configure an IAM role for your ETL job

1. Configure the permissions described in [Review IAM permissions needed for ETL
   jobs](getting-started-min-privs-job.md "getting-started-min-privs-job.md").
2. Configure the additional permissions needed when using connectors with AWS Glue Studio, as
   described in [Permissions required for
   using connectors](getting-started-min-privs-job.md#getting-started-min-privs-connectors "getting-started-min-privs-job.md#getting-started-min-privs-connectors").

### Next step

[Step 5: Create a job that uses the OpenSearch connection](#tutorial-step5 "#tutorial-step5")

## Step 5: Create a job that uses the OpenSearch connection

After creating a role for your ETL job, you can create a job in AWS Glue Studio that uses the
connection and connector for Open Spark ElasticSearch.

If your job runs within a Amazon Virtual Private Cloud (Amazon VPC), make sure the VPC is configured correctly. For
more information, see [Configure a VPC for your ETL job](getting-started-vpc-config.md "getting-started-vpc-config.md").

###### To create a job that uses the Elasticsearch Spark Connector

1.  In AWS Glue Studio, choose **Connectors**.
2.  In the **Your connections** list, select the connection you just created
    and choose **Create job**.
3.  In the visual job editor, choose the Data source node. On the right, on the
    **Data source properties - Connector** tab, configure additional information for
    the connector.
    1.  Choose **Add schema** and enter the schema of the data set in the data
        source. Connections do not use tables stored in the Data Catalog, which means that AWS Glue Studio doesn't
        know the schema of the data. You must manually provide this schema information. For
        instructions on how to use the schema editor, see [Editing the schema in a custom transform
        node](transforms-custom.md#transforms-custom-editschema "transforms-custom.md#transforms-custom-editschema").
    2.  Expand **Connection options**.
    3.  Choose **Add new option** and enter the information needed for the
        connector that was not entered in the AWS secret:

            * **es.nodes**: https://*<OpenSearch domain endpoint>*
            * **es.port**: 443
            * **path**: test
            * **es.nodes.wan.only**: true

        For an explanation of these connection options, refer to: [https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html "https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html").

4.  Add a target node to the graph.

Your data target can be Amazon S3, or it can use information from an AWS Glue Data Catalog
or a connector to write data in a different location. For example, you can use a Data Catalog table
to write to a database in Amazon RDS, or you can use a connector as your data target to write to
data stores that are not natively supported in AWS Glue.

If you choose a connector for your data target, you must choose a connection created for
that connector. Also, if required by the connector provider, you must add options to provide
additional information to the connector. If you use a connection that contains information for
an AWS secret, then you don’t need to provide the user name and password authentication in the
connection options. 5. Optionally, add additional data sources and one or more transform nodes as described in
[Transform data with AWS Glue managed transforms](edit-jobs-transforms.md "edit-jobs-transforms.md"). 6. Configure the job properties as described in [Modify the job properties](managing-jobs-chapter.md#edit-jobs-properties "managing-jobs-chapter.md#edit-jobs-properties"),
starting with step 3, and save the job.

### Next step

[Step 6: Run the job](#tutorial-step6 "#tutorial-step6")

## Step 6: Run the job

After you save your job, you can run the job to perform the ETL operations.

###### To run the job you created for the AWS Glue Connector for Elasticsearch

1. Using the AWS Glue Studio console, on the visual editor page, choose
   **Run**.
2. In the success banner, choose **Run Details**, or you can choose the
   **Runs** tab of the visual editor to view information about the
   job run.
