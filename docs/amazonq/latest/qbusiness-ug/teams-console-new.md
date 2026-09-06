

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting using the latest Microsoft Teams connector (Console)
<a name="teams-console-new"></a>

The latest Microsoft Teams connector provides a simplified configuration experience with essential features. Use this procedure to connect Amazon Q Business to Microsoft Teams using the latest connector.

**To connect Amazon Q to Microsoft Teams using the latest connector**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add data source**.

1. Then, on the **Add data sources** page, from **Data sources**, add the **Microsoft Teams** data source to your Amazon Q application.

1. Then, on the **Microsoft Teams** data source page, enter the following information:

1. **Name and description**, do the following:
   + For **Data source name** – Name your data source for easy tracking.
**Note**  
You can include hyphens (-) but not spaces. Maximum of 1,000 alphanumeric characters.
   + **Description – *optional*** – Add an optional description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

1. In **Source**, enter the following information:

   1. **Tenant ID** – Enter your Tenant ID.
**Note**  
Your Microsoft Tenant ID is a globally unique identifier that's necessary to configure each connector instance. Your Tenant ID is different from your organization name or domain and can be found in the **Properties** section of your Azure Active Directory Portal.

1. For **Authentication**, in **AWS Secrets Manager** – Choose between **Create and add new secret** and **Use existing secrets**.

   1. If you choose **Use existing secrets**, select an existing secret.

     If you choose **Create and add a new secret**, enter the following information in the **Create AWS Secrets Manager secret** section:

     1. **Secret name** – A name for your secret.

     1. **Client ID** – Enter the Client ID you generated after registering your application for use. You can find this Client ID in **App registrations** in your Azure Active Directory Portal.

     1. **Client Secret** – Enter the client secret that you generated from your Teams account. 

1. **IAM role** – Choose an existing IAM role or create an IAM role to access your repository credentials and index content.
**Note**  
Creating a new service IAM role is recommended.

   For more information, see [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/teams-connector.html#teams-iam).

1. **Sync scope** – Choose the content you want to sync.

   1. Choose **All** to crawl and sync all your documents.

   1. For **Chat**, choose from the following options:

      1. Choose **Chat** to crawl and sync all chats. If you choose this option, Amazon Q Business also crawls **Chat messages** by default.

      1. Choose **Chat messages** to crawl and sync only all chat messages.

   1. For **Teams**, choose from the following options:

      1. Choose **Teams** to crawl and sync all teams. If you choose this option, Amazon Q Business also crawls **Channel posts** by default.

      1. Choose **Channel posts** to crawl and sync only all channel posts.

   1. **Advanced settings**

      **Document deletion safeguard** - *optional*–To safeguard your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard).

1. In **Additional configuration – *optional***, configure the following simplified options:
   + **Date Range** – Enter the date range for which the connector will crawl your content. End date is optional. Rolling window options available: Last [X] Days/Weeks/Months.
**Note**  
**Simplified configuration:** The latest connector automatically handles entity selection with ACL enabled by default to keep the configuration simple and reliable.

1. In **Sync run schedule**, for **Frequency** – Choose how often Amazon Q will sync with your data source. For more details, see [Sync run schedule](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-run). To learn how to start a data sync job, see [Starting data source connector sync jobs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html#start-datasource-sync-jobs).

1. **Tags - *optional*** – Add tags to search and filter your resources or track your AWS costs. See [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html) for more details.

1. In **Data source details**, choose **Sync now** to allow Amazon Q to begin syncing (crawling and ingesting) data from your data source. When the sync job finishes, your data source is ready to use.
**Note**  
View CloudWatch logs for your data source sync job by selecting **View CloudWatch logs**. If you encounter a `Resource not found exception` error, wait and try again as logs may not be available immediately.  
You can also view a detailed document-level report by selecting **View Report**. This report shows the status of each document during the crawl, sync, and index stages, including any errors. If the report is empty for an in-progress job, check back later as data is emitted to the report as events occur during the sync process.  
For more information, see [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html#troubleshooting-data-sources-not-indexed).