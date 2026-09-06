

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting using the Latest Microsoft Exchange Connector (Console)
<a name="exchange-console-new"></a>

The latest Microsoft Exchange connector provides a simplified configuration experience with essential features. The following procedure shows how to connect Amazon Q Business to Microsoft Exchange using the latest connector.

**Connecting Amazon Q to Microsoft Exchange using the latest connector**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add data source**.

1. Then, on the **Add data sources** page, from **Data sources**, add the **Microsoft Exchange (latest)** data source to your Amazon Q application.

1. Then, on the **Microsoft Exchange** data source page, enter the following information:

1. **Name and description**, do the following:
   + For **Data source name** – Name your data source for easy tracking.
**Note**  
You can include hyphens (-) but not spaces. Maximum of 1,000 alphanumeric characters.
   + **Description – *optional*** – Add an optional description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

1. In **Source**, enter the following information:
   +  **Tenant ID** – Enter your tenant ID. Your Microsoft tenant ID is a globally unique identifier required to configure each connector instance. You can find your tenant ID in the properties section of your Microsoft account dashboard.

1. For **Authentication**, choose between **New** and **Existing**.

   1. If you choose **Existing**, choose an existing secret for **Select secret**.

     If you choose **New**, enter the following information in the **New AWS Secrets Manager secret** section:

     1. **Secret name** – Enter a name for your secret.

     1. For **Client ID** and **Client secret**, enter the authentication credential values that you generated from your Exchange account. 

1. **IAM role** – Choose an existing IAM role or create an IAM role to access your repository credentials and index content.
**Note**  
Creating a new service IAM role is recommended.

   For more information, see [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/exchange-connector.html#exchange-iam).

1. For **Additional configuration – *optional***, configure the following options:
   + **Date Range** – Enter the date range for crawling your email content. The end date is optional.
**Note**  
**Simplified configuration:** The latest connector automatically crawls email content only with ACL enabled by default. Entity type selection and attachment filtering are not available to keep configuration simple and reliable.

1. **Advanced settings**

   **Document deletion safeguard** - *optional*–To safeguard your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard).

1. In **Sync run schedule**, for **Frequency** – Choose how often Amazon Q will sync with your data source. For more details, see [Sync run schedule](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-run). To learn how to start a data sync job, see [Starting data source connector sync jobs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html#start-datasource-sync-jobs).

1. **Tags - *optional*** – Add tags to search and filter your resources or track your AWS costs. See [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html) for more details.

1. In **Data source details**, choose **Sync now** to allow Amazon Q to begin syncing (crawling and ingesting) data from your data source. When the sync job finishes, your data source is ready to use.
**Note**  
View CloudWatch logs for your data source sync job by selecting **View CloudWatch logs**. If you encounter a `Resource not found exception` error, wait and try again as logs may not be available immediately.  
You can also view a detailed document-level report by selecting **View Report**. This report shows the status of each document during the crawl, sync, and index stages, including any errors. If the report is empty for an in-progress job, check back later as data is emitted to the report as events occur during the sync process.  
For more information, see [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html#troubleshooting-data-sources-not-indexed).