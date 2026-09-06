

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Using the console
<a name="s3-v2-console"></a>

The following procedure outlines how to connect Amazon Q Business to Amazon S3 using the AWS Management Console.

**Connecting Amazon Q to Amazon S3**

1. Sign in to the AWS Management Console and open the Amazon Q Business console.

1. From the left navigation menu, choose **Data sources**.

1. From the **Data sources** page, choose **Add data source**.

1. Then, on the **Add data sources** page, from **Data sources**, add the **Amazon S3** data source to your Amazon Q application.

1. Then, on the **Amazon S3** data source page, enter the following information:

1. **Name and description**, do the following:
   + For **Data source name** – Name your data source for easy tracking.
**Note**  
You can include hyphens (-) but not spaces. Maximum of 1,000 alphanumeric characters.
   + **Description – *optional*** – Add an optional description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

1. **IAM role** – Choose an existing IAM role or create an IAM role to access your repository credentials and index content.
**Note**  
IAM roles used for applications can't be used for data sources. If you are unsure if an existing role is used for an application, choose **Create a new role** to avoid errors.

1. **Data source location** – Choose the location of your Amazon S3 bucket:

   1. **This account** – Selected by default. Choose this option if your Amazon S3 bucket is in the same account as your Amazon Q Business application.

   1. **Other account** – Choose this option if your Amazon S3 bucket is in a different account.

      1. **Account ID** – Specify the ID for the other account that owns the bucket.

1. **Sync scope**, enter the following information:

   1. **Enter the data source location** – The path to the Amazon S3 bucket where your data is stored.
      + If you selected **This account**, you can select **Browse S3** to find and choose your bucket.
      + If you selected **Other account**, you must manually enter the bucket name as the browse option is not available for cross-account buckets.
**Note**  
Your bucket must be in the same AWS Region as your Amazon Q Business index.

   1. **Maximum file size - *optional*** – You can specify the file size limit in MB for Amazon Q crawling. Amazon Q crawls only files within the defined size limit. The default file size is 50MB. The maximum file size limit is 10 GB.

   1. **Access control list configuration file location - *optional*** – The path to the location of a file containing a JSON structure that specifies access settings for the files stored in your S3 data source.
      + If you selected **This account**, you can select **Browse S3** to locate your ACL file.
      + If you selected **Other account**, you must manually enter the file path as the browse option is not available for cross-account buckets.

   1. **Metadata files folder location - *optional*** – The path to the folder in which your metadata is stored.
      + If you selected **This account**, you can select **Browse S3** to locate your metadata folder.
      + If you selected **Other account**, you must manually enter the folder path as the browse option is not available for cross-account buckets.

   1. **Filter patterns** – Add regex patterns to include or exclude documents from your index. 

      To include or exclude files and folders, you can use a prefix filter (for example `Data/`, where `Data` is a folder containing documents in your S3 bucket). You can also filter using glob patterns and file types.

   1. **Multi-media content configuration – optional** – To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**. For more information, see [Extracting semantic meaning from embedded images and visuals](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html).

      To extract audio transcriptions and video content, enable **Audio Files**. To extract video content, enable **Video files**. For more information, see [Extracting semantic meaning from audio and video Content](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/Audio-video-extraction.html). 

   1. **Advanced settings**

      **Document deletion safeguard** - *optional*–To safeguard your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard).

1. In **Sync run schedule**, for **Frequency** – Choose how often Amazon Q will sync with your data source. For more details, see [Sync run schedule](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-sync-run). To learn how to start a data sync job, see [Starting data source connector sync jobs](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/supported-datasource-actions.html#start-datasource-sync-jobs).

1. **Tags - *optional*** – Add tags to search and filter your resources or track your AWS costs. See [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html) for more details.

1. In **Data source details**, choose **Sync now** to allow Amazon Q to begin syncing (crawling and ingesting) data from your data source. When the sync job finishes, your data source is ready to use.
**Note**  
View CloudWatch logs for your data source sync job by selecting **View CloudWatch logs**. If you encounter a `Resource not found exception` error, wait and try again as logs may not be available immediately.  
You can also view a detailed document-level report by selecting **View Report**. This report shows the status of each document during the crawl, sync, and index stages, including any errors. If the report is empty for an in-progress job, check back later as data is emitted to the report as events occur during the sync process.  
For more information, see [Troubleshooting data source connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/troubleshooting-data-sources.html#troubleshooting-data-sources-not-indexed).