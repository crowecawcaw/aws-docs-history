

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Gmail using the legacy connector (Console)
<a name="gmail-console-original"></a>

The following procedure outlines how to connect Amazon Q Business to Gmail using the legacy connector and the AWS Management Console. The legacy connector provides full-featured configuration with advanced options.

**Connecting Amazon Q to Gmail using the legacy connector**

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

1. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from documents your end users have access to. If supported for your connector, you can manage ACLs by selecting ** Enable ACLs ** to enable ACLs or **Disable ACLs** to disable them. To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html#DisableAclOnDataSource) for more details. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.

1. In **Authentication**, for **AWS Secrets Manager secret** – Choose an existing secret or create a Secrets Manager secret to store your Gmail authentication credentials. If you choose to create a secret, an AWS Secrets Manager secret window opens.

   1. Enter the following information in the **Create an AWS Secrets Manager secret window**:

     1. **Secret Name** – A name for your secret.

     1. **Client email** – The client email address that you copied from your Google service account.

     1. **Admin account email** – The admin account email address that you would like to use.

     1. **Private key** – The private key that you copied from your Google service account.

     1. Choose **Save**.

1. **IAM role** – Choose an existing IAM role or create an IAM role to access your repository credentials and index content.
**Note**  
Creating a new service IAM role is recommended.

   For more information, see [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/gmail-connector.html#gmail-iam).

1. In **Sync scope**, choose from the following entity types:
   + **Message attachments** – Choose to crawl email attachments. Messages are crawled by default.

1. For **Maximum file size** – Specify the file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB.

1. For **Additional configuration – *optional***, configure the comprehensive filtering options available in the original connector:

   1. **Date range** – Enter a date range to specify the start and end date of email messages to be crawled.

   1. **Email domains** – Include or exclude email messages based on domains.

   1. **Keywords in subjects** – Include or exclude email messages based on keywords in their subjects.
**Note**  
You can also choose to include any documents that match all the subject keywords that you have entered.

   1. **Labels** – Add regular expression patterns to include or exclude specific labels. You can add up to 100 patterns.

   1. **Attachments** – Add regular expression patterns to include or exclude specific attachments. You can add up to 100 patterns.

1. **Multi-media content configuration – optional** – To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.

   To extract audio transcriptions and video content, enable processing for the following file types:

1. For **Sync mode**, choose how you want to update your index when your data source content changes. When you sync your data source with Amazon Q for the first time, all content is synced by default.
   + **Full sync** – Sync all content regardless of the previous sync status.
   + **New, modified, or deleted content sync** – Sync only new, modified, and deleted documents.

1. **Configure VPC and security group – *optional*** – Choose whether you want to use a VPC. If you do, enter the following information:

   1. **Subnets** – Select up to 6 repository subnets that define the subnets and IP ranges the repository instance uses in the selected VPC.

   1. **VPC security groups** – Choose up to 10 security groups that allow access to your data source. Ensure that the security group allows incoming traffic from Amazon EC2 instances and devices outside your VPC. For databases, security group instances are required. 

   For more information, see [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc).

1. In **Sync run schedule**, for **Frequency** – Choose how often Amazon Q will sync with your data source. For more details, see [Sync run schedule](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-run). To learn how to start a data sync job, see [Starting data source connector sync jobs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html#start-datasource-sync-jobs).

1. **Tags - *optional*** – Add tags to search and filter your resources or track your AWS costs. See [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html) for more details.

1. **Field mappings** – A list of data source document attributes to map to your index fields.
**Note**  
Add or update the fields from the **Data source details** page after you finish adding your data source. You can choose from two types of fields: 

   1. **Default** – Automatically created by Amazon Q on your behalf based on common fields in your data source. You can't edit these.

   1. **Custom** – Automatically created by Amazon Q on your behalf based on common fields in your data source. You can edit these. You can also create and add new custom fields.
**Note**  
Support for adding custom fields varies by connector. You won't see the **Add field** option if your connector doesn't support adding custom fields.

   For more information, see [Field mappings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-field-mappings).

1. In **Data source details**, choose **Sync now** to allow Amazon Q to begin syncing (crawling and ingesting) data from your data source. When the sync job finishes, your data source is ready to use.
**Note**  
View CloudWatch logs for your data source sync job by selecting **View CloudWatch logs**. If you encounter a `Resource not found exception` error, wait and try again as logs may not be available immediately.  
You can also view a detailed document-level report by selecting **View Report**. This report shows the status of each document during the crawl, sync, and index stages, including any errors. If the report is empty for an in-progress job, check back later as data is emitted to the report as events occur during the sync process.  
For more information, see [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html#troubleshooting-data-sources-not-indexed).