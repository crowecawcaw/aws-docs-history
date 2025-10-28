#

Setting up a crawler for Amazon S3 event notifications for a Data Catalog table

When you have a Data Catalog table, set up a crawler for Amazon S3 event notifications using the AWS Glue console:

1. Set your crawler properties. For more information, see
   [Setting Crawler Configuration Options on the AWS Glue console](crawler-configuration.md#crawler-configure-changes-console "crawler-configuration.md#crawler-configure-changes-console") .
2. In the section **Data source configuration**, you are asked _Is your data already mapped to AWS Glue tables?_

Select **Yes** to select existing tables from your Data Catalog as your data source. 3. In the section **Glue tables**, choose **Add tables**.

![Data source configuration interface with options to select existing Glue tables or add new ones.](images/crawler-s3-event-console1-cat.png) 4. In the **Add table** modal, configure the database and tables:

    * **Network connection** (Optional): Choose **Add new connection**.
    * **Database**: Select a database in the Data Catalog.
    * **Tables**: Select one or more tables from that database in the Data Catalog.
    * **Subsequent crawler runs**: Choose **Crawl based on events**
     to use Amazon S3 event notifications for your crawler.
    * **Include SQS ARN**: Specify the data store parameters including the a
     valid SQS ARN. (For example, `arn:aws:sqs:region:account:sqs`).
    * **Include dead-letter SQS ARN** (Optional): Specify a valid Amazon dead-letter
     SQS ARN. (For example, `arn:aws:sqs:region:account:deadLetterQueue`).
    * Choose **Confirm**.

![Add Glue tables dialog with network, database, tables, and crawler options.](images/crawler-s3-event-console2-cat.png)
