

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Gmail using the latest connector (Console)
<a name="gmail-console-new"></a>

The following procedure outlines how to connect Amazon Q Business to Gmail using the latest connector and the AWS Management Console. The latest connector provides a simplified configuration experience with automatic ACL and identity crawling.

**Connecting Amazon Q to Gmail using the latest connector**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add data source**.

1. Then, on the **Add data sources** page, from **Data sources**, add the **Gmail** data source to your Amazon Q application.

1. Then, on the **Gmail** data source page, enter the following information:

1. **Name and description**, do the following:
   + For **Data source name** – Name your data source for easy tracking.
**Note**  
You can include hyphens (-) but not spaces. Maximum of 1,000 alphanumeric characters.
   + **Description – *optional*** – Add an optional description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

1. In **Authentication**, for **AWS Secrets Manager secret** – Choose an existing secret or create a Secrets Manager secret to store your Gmail authentication credentials. If you choose to create a secret, an AWS Secrets Manager secret window opens.

   1. Enter the following information in the **Create an AWS Secrets Manager secret window**:

     1. **Secret Name** – A name for your secret.

     1. **Client email** – The client email address that you copied from your Google service account. For example, it might look like this:

        ```
        "{"clientEmailId":"service-account@123.iam.gserviceaccount.com","adminAccountEmailId":"admin@accounthost.com",
        "privateKey":"-----BEGIN PRIVATE KEY-----PRIVATE KEY HERE-----END PRIVATE KEY-----\n"}"
        ```

     1. **Admin account email** – The admin account email address that you would like to use.

     1. **Private key** – The private key that you copied from your Google service account.

     1. Choose **Save**.

1. For **Additional configuration – *optional***, configure the date range filter:

   1. **Date range** – Configure the time period for crawling email messages. Choose from:
     + *Date range*: Specify start and end dates. **(optional)** - if not provided, the entire inbox is crawled.
     + *Start date onwards*: Specify only a start date to crawl from that date forward
**Note**  
**Simplified configuration:** The latest connector automatically crawls email content and allows configurable draft email crawling. Only date range filtering is available to keep the configuration simple and reliable.

1. In **Sync run schedule**, for **Frequency** – Choose how often Amazon Q will sync with your data source. For more details, see [Sync run schedule](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-run). To learn how to start a data sync job, see [Starting data source connector sync jobs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html#start-datasource-sync-jobs).

1. **Tags - *optional*** – Add tags to search and filter your resources or track your AWS costs. See [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html) for more details.

1. In **Data source details**, choose **Sync now** to allow Amazon Q to begin syncing (crawling and ingesting) data from your data source. When the sync job finishes, your data source is ready to use.
**Note**  
View CloudWatch logs for your data source sync job by selecting **View CloudWatch logs**. If you encounter a `Resource not found exception` error, wait and try again as logs may not be available immediately.  
You can also view a detailed document-level report by selecting **View Report**. This report shows the status of each document during the crawl, sync, and index stages, including any errors. If the report is empty for an in-progress job, check back later as data is emitted to the report as events occur during the sync process.  
For more information, see [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html#troubleshooting-data-sources-not-indexed).