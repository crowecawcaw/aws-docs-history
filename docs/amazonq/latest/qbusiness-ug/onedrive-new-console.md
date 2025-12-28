# Using the console

The following procedure outlines how to connect Amazon Q Business to
Microsoft OneDrive using the new connector with the AWS Management Console.

###### Connecting Amazon Q to Microsoft OneDrive new connector

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Microsoft OneDrive** data source to your Amazon Q application.
5. Then, on the **Microsoft OneDrive** data source page, enter
   the following information:
6. In **Source**, enter the following information:
   - **OneDrive Tenant ID** Enter your
     OneDrive Tenant ID without the protocol. You can find
     your OneDrive Tenant ID under Directory ID in the
     Microsoft Entra ID (formerly Azure AD) admin center.

7. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 8. In **Authentication** – Choose between
**New** and **Existing**.

    1. If you choose **Existing**, select an existing secret
     for **Select secret**.


    If you choose **New**, enter the following
     information in the **New AWS Secrets Manager secret**
     section:


    	1. **Secret name** – A name for your
    	 secret.
    	2. For **Client ID** and **Client
    	 secret** – Enter the authentication
    	 credential values from your OneDrive account
    	 and then choose **Save authentication**.

9. **IAM role** – Choose an existing
   IAM role or create an IAM role to access your
   repository credentials and index content.

###### Note

IAM roles used for applications can't be used for data
sources. If you are unsure if an existing role is used for an application,
choose **Create a new role** to avoid errors. 10. In **Sync scope**, configure which OneDrive users and content to sync:

    1. **Select OneDrive users** – Choose how to specify which users' content to sync:




    	* **All users** – Select this option to sync content for all users in the organization. This allows comprehensive content discovery across all user accounts.
    	* **Users from a user name file** – Choose this option to specify users via a file stored in an Amazon S3 bucket. Select the location of the user name file by choosing **Browse**.


    	###### Note

    	If you choose this option, the IAM role for the data source must have read permissions for the Amazon S3 bucket where the file is stored.
    	* **Specific users** – Choose this option to manually specify individual users. You can add a maximum of 10 users using this option. To add more than 10 users, create a file containing the usernames and choose **Users from a user name file**.
    2. **Maximum single file size** – Set the maximum file size for crawling.
     During this ingestion, there are file size limits depending on
     the file type. Video files have a limit of up to 10 GB/10,240 MB. Audio files have a 2
     GB/2,048 MB limit. PDF/Word/Powerpoint documents have a 500 MB limit. Excel and other
     supported file formats have a 50 MB limit. There are also limits to the amount of text extracted
     from these documents. CSV and Excel have a extracted text limit of 10MB, all other document
     formats have a limit of 30MB of extracted text.
    3. **Additional configuration - *optional*** – All content will be indexed by default. However, you can also limit the scope with these additional options:


    	1. **Date filter** – Add a date range to filter content based on the last modified date:




    		* **Start date** – Filter content modified after this date (YYYY/MM/DD format)
    		* **End date - optional** – Filter content modified before this date (YYYY/MM/DD format)
    	2. **Filter patterns** – Add file path patterns to include or exclude certain folders and files from OneDrive:




    		* **Include patterns** –
    		 Specify file paths to include in the sync. Enter the
    		 path pattern and choose
    		 **Add**.
    		* **Exclude patterns** –
    		 Specify file paths to exclude from the sync. Enter
    		 the path pattern and choose
    		 **Add**.


    		You can identify the path of a folder or file by
    		 following these instructions by (within OneDrive),
    		 navigating to the file or folder for which you want
    		 to apply a filte and clicking on the three-dot menu
    		 button next to the file/folder name and selecting
    		 "Details." In the following details panel, scroll
    		 down to the "Path" details and click on the "Copy"
    		 button next to the path. For shared folders and
    		 files, first click on “Open location” in the menu
    		 adjacent to the file or the folder name, and then
    		 follow the above directions.
    4. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**. For more information, see [Extracting semantic meaning from embedded images and visuals](extracting-meaning-from-images.md "extracting-meaning-from-images.md").


    To extract audio transcriptions and video content, enable **Audio Files**. To extract video content, enable **Video files**. For more information, see [Extracting semantic meaning from audio and video Content](Audio-video-extraction.md "Audio-video-extraction.md").
    5. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion
     safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

11. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
12. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
13. In **Data source details**, choose **Sync
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
