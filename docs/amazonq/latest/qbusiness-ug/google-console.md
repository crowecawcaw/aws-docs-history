

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Google Drive using the console
<a name="google-console"></a>

The following procedure outlines how to connect Amazon Q Business to Google Drive using the AWS Management Console.

**Connecting Amazon Q to Google Drive**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add data source**.

1. Then, on the **Add data sources** page, from **Data sources**, add the **Google Drive** data source to your Amazon Q application.

1. Then, on the **Google Drive** data source page, enter the following information:

1. **Name and description**, do the following:
   + For **Data source name** – Name your data source for easy tracking.
**Note**  
You can include hyphens (-) but not spaces. Maximum of 1,000 alphanumeric characters.
   + **Description – *optional*** – Add an optional description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

1. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from documents your end users have access to. If supported for your connector, you can manage ACLs by selecting ** Enable ACLs ** to enable ACLs or **Disable ACLs** to disable them. To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html#DisableAclOnDataSource) for more details. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.

1. For **Authentication** – Choose between **Google service account** and **OAuth 2.0 authentication**, based on your use case.

1. **AWS Secrets Manager secret** – Choose an existing secret or create a Secrets Manager secret to store your GoogleDrive authentication credentials. If you choose to create a secret, an AWS Secrets Manager secret window opens.

   1. If you choose **Existing**, select an existing secret for **Select secret**.

     If you choose **New**, enter the following information in the **New AWS Secrets Manager secret** section:

     1. **Secret name** – A name for your secret.

     1. If you chose **Google service account**, enter the following information:
        + **Secret Name** – A name for your secret.
        + **Admin account email** – The email ID of the admin user (the email used by the Service Account User) in your Google service account configuration.
        + **Client email** – The email ID of the service account.
        +  **Private Key** – The private key created in your service account.

        Then, choose **Save and add secret**.

     1. If you chose **OAuth 2.0 authentication**, enter the details of **Secret Name**, **Client ID**, **Client secret** and **Refresh token** that you created in your service account. Then, choose **Save and add secret**.

1. **Configure VPC and security group – *optional*** – Choose whether you want to use a VPC. If you do, enter the following information:

   1. **Subnets** – Select up to 6 repository subnets that define the subnets and IP ranges the repository instance uses in the selected VPC.

   1. **VPC security groups** – Choose up to 10 security groups that allow access to your data source. Ensure that the security group allows incoming traffic from Amazon EC2 instances and devices outside your VPC. For databases, security group instances are required. 

   For more information, see [VPC](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-vpc).

1. **IAM role** – Choose an existing IAM role or create an IAM role to access your repository credentials and index content.
**Note**  
Creating a new service IAM role is recommended.

   For more information, see [IAM role](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/google-connector.html#google-iam).

1. In **Sync scope**, for **Sync contents** – Choose from the following options to select content to index:
**Note**  
To further limit content to index, use **Entity regex patterns** in the **Additional configuration** section.
   + **My Drive & Shared with me** – **My Drive** contains a user's personal folders and documents. **Shared with me** contains all the folders and documents that have been shared with the user. Select this option to index both.
   + **Shared drives** – **Shared drives** are folders used to store, access, and share files with a team. Select this option to index these.
   + **Comments** – Select this option to index file comments.
**Note**  
If you add an inclusion pattern to include certain folder paths or files, you don't need to specify an exclude pattern to include the same folder paths or files. 

1. For **Maximum file size** – You can specify the file size limit in GB for Amazon Q crawling. Amazon Q crawls only files within the defined size limit. The default file size is 50MB. The maximum file size limit is 10 GB. Files must be larger than 0 MB and no larger than 10 GB. You can go up to 10 GB (10240 MB) if you enable **Video files** in **Multi-media content** configuration, and up to 2 GB (2048 MB) if you enable **Audio files** in **Multi-media content configuration**. 

1. In **Additional configuration - optional**, enter the following optional information:

   1. **User email** – Add the user email IDs whose drive files you want to include or exclude.

   1. **Shared drives** – The folders and files shared with a team. Add the shared drives that you want to include or exclude.

   1. **Mime types** – Add the MIME (Multipurpose Internet Mail Extensions) types that you want to include or exclude from your data sync.

   1. **Entity patterns** – Add regular expression patterns to include or exclude certain folders, files, and file types from **My drive**, **Shared with me**, and **Shared drives**. You can add up to 100 patterns.

       You can configure the Include/Exclude Regex patterns for File name, File type and File path. 
      + **File name** - The name of the file to include/exclude. For example, to index a file with name ’Team roaster.txt’, provide Team roaster.
      + **File type** - The type of the file to include/exclude. For example, .pdf .txt .docx
      + **File path** - The path of the file to include/exclude. For example, to index files only inside the folder ‘Products list’ of a drive, provide /Products list.

   1. **Multi-media content configuration – optional** – To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**. For more information, see [Extracting semantic meaning from embedded images and visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html).

      To extract audio transcriptions and video content, enable **Audio Files**. To extract video content, enable **Video files**. For more information, see [Extracting semantic meaning from audio and video Content](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Audio-video-extraction.html). 

   1. **Advanced settings**

      **Document deletion safeguard** - *optional*–To safeguard your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard).

1. In **Sync mode**, choose how you want to update your index when your data source content changes. When you sync your data source with Amazon Q for the first time, all content is synced by default.
   + **Full sync** – Sync all content regardless of the previous sync status.
   + **New or modified content sync** – Sync only new and modified documents.
   + **New, modified, or deleted content sync** – Sync only new, modified, and deleted documents.

   For more details, see [Sync mode](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-mode).

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

**Note**  
Documents shared to a specific company domain or with a permission set to **General access: Anyone with the link** must be accessed by at least one user before the documents become visible to users in search. 