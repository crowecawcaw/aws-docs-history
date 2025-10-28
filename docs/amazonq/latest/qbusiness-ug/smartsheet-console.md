# Connecting Amazon Q Business to

Smartsheet using the console

The following procedure outlines how to connect Amazon Q Business to
Smartsheet using the AWS Management Console.

###### Note

Before you begin adding your data source, make sure you've created an Amazon Q Business application, and added an index and retriever to it.

###### Connecting Amazon Q to Smartsheet

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Smartsheet** data source to your Amazon Q application.
5. Then, on the **Smartsheet** data source page, enter
   the following information:
6. **Name and description**, do the following:
   - For **Data source name** – Name your data
     source for easy tracking.

   ###### Note

   You can include hyphens (-) but
   not spaces. Maximum of 1,000 alphanumeric characters.
   - **Description –
     _optional_** – Add an optional
     description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

7. In **User type** – Choose the user type in your
   Smartsheet account. You can choose between **System
   Admin** and **Non-System Admin**. System Admins
   can ingest sheets, folders, and workspaces into Amazon Q Business.
   Non-System Admins can ingest only sheets.
8. **Authentication** – Enter the following information
   for your **AWS Secrets Manager secret**.
   1. **Secret name** – A name for your
      secret.
   2. For **Smartsheet API access token** –
      Enter the value for the access token you created in your
      Smartsheet account.

9. **IAM role** – Choose
   an existing IAM role or create an IAM role to access your repository credentials and
   index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](smartsheet-connector.md#smartsheet-iam "smartsheet-connector.md#smartsheet-iam"). 10. In **Sync scope**, enter the following information:

    1. In **Select specific sheets, folders, and
     workspaces**, for **ID type** –
     Select content to sync using a specific **Sheet ID**,
     **Folder ID**, and **Workspace
     ID**.
    2. For **Select attachments and conversations**, select
     from the following options:




    	* **All attachments** – Select to
    	 include all attachments.
    	* **All conversations** – Select to
    	 include all conversations.
    3. In **Additional configuration –
     *optional*, select from the following
     options:**




    	* **Sheet and folder regex patterns** –
    	 Choose to include or exclude specific sheet and folder names
    	 using regex patterns.
    	* **Attachment regex patterns** – Choose
    	 to include or exclude specific files by name and type using
    	 regex patterns.
    4. For **Maximum file size** – Specify the file
     size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only
     the files within the size limit you define. The default file size is
     50MB. The maximum file size should be greater than 0MB and less than or
     equal to 50MB.
    5. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.


    To extract audio transcriptions and video content, enable processing for the following file types:
    6. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion
     safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

11. For **Sync mode**, choose how you want to update your index
    when your data source content changes. When you sync your data source with
    Amazon Q for the first time, all content is synced by
    default.
    - **Full sync**—Sync all content regardless of
      the previous sync status.
    - **New, modified, or deleted content
      sync**—Sync only new, modified, and deleted
      documents.

12. In **Sync run schedule**, for **Frequency**
    – Choose how often Amazon Q will sync with your data source.
    For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run").

###### Note

The Amazon Q Business Smartsheet connector doesn't support
hourly syncs. For optimal performance, choose to sync your data during a
time window outside of 11am UTC to 11pm UTC. 13. **Tags - _optional_** –
Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details. 14. **Field mappings** – A list of data source document
attributes to map to your index fields. Add the fields from the **Data
source details** page after you finish adding your data source.

You can choose from two types of fields:

    1. **Default** – Automatically created by Amazon Q on your behalf based on common fields in your data
     source. You can't edit these.
    2. **Custom** – Automatically created by Amazon Q on your behalf based on common fields in your data
     source. You can edit these. You can also create and add new custom
     fields.


    ###### Note

    Support for adding custom fields varies by connector. You
     won't see the **Add field** option if your
     connector doesn't support adding custom fields.For more information, see [Field mappings](connector-concepts.md#connector-field-mappings "connector-concepts.md#connector-field-mappings").

15. In **Data source details**, choose **Sync
    now** to allow Amazon Q to begin syncing (crawling and
    ingesting) data from your data source. When the sync job finishes, your data
    source is ready to use.

###### Note

View CloudWatch logs for your data source sync job by selecting **View
CloudWatch logs**. If you encounter a `Resource not found
 exception` error, wait and try again as logs may not be available
immediately.

You can also view a detailed document-level report by selecting
**View Report**. This report shows the status of each
document during the crawl, sync, and index stages, including any errors. If
the report is empty for an in-progress job, check back later as data is
emitted to the report as events occur during the sync process.

For more information, see [Troubleshooting data source
connectors](troubleshooting-data-sources.md#troubleshooting-data-sources-not-indexed "troubleshooting-data-sources.md#troubleshooting-data-sources-not-indexed").
