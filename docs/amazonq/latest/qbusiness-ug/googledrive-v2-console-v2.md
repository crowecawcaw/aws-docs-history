# Connecting Amazon Q Business to Google Drive using the console

The following procedure outlines how to connect Amazon Q Business to Google Drive new using the AWS Management Console.

###### Connecting Amazon Q to Google Drive new

1.  Sign in to the AWS Management Console and open the Amazon Q Business
    console.
2.  From the left navigation menu, choose **Data
    sources**.
3.  From the **Data sources** page, choose
    **Add data source**.
4.  Then, on the **Add data sources** page, from
    **Data sources**, add the **Google Drive** data source to your Amazon Q application.
5.  Then, on the **Google Drive** data source page, enter
    the following information:
6.  **Name and description**, do the following:
    - For **Data source name** – Name your data
      source for easy tracking.

    ###### Note

    You can include hyphens (-) but
    not spaces. Maximum of 1,000 alphanumeric characters.
    - **Description –
      _optional_** – Add an optional
      description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

7.  In **Authorization**, configure access control settings:
    Amazon Q Business crawls ACL information by default to ensure responses are
    generated only from documents your end users have access to. If supported
    for your connector, you can manage ACLs by selecting _Enable
    ACLs_ to enable ACLs or _Disable ACLs_ to
    disable them. To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for
    more details. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")for more details.
8.  **AWS Secrets Manager secret** – Choose an existing secret
    or create a secret to store your GoogleDrive authentication credentials. If
    you choose to create a secret, an AWS Secrets Manager secret window opens.
    1. If you choose **Existing**, select an existing
       secret for **Select secret**.

    If you choose **New**, enter the following
    information in the **New AWS Secrets Manager secret**
    section:

        1. **Secret name** – A name for your
         secret.
        2. Enter the following information:




        	* **Secret Name** – A name
        	 for your secret.
        	* **Admin account email** –
        	 The email ID of the admin user (the email used by
        	 the Service Account User) in your
        	 Google service account
        	 configuration.
        	* **Client email** – The
        	 email ID of the service account.
        	* **Private Key** – The
        	 private key created in your service account.
        Then, choose **Save and add
         secret**.

9.  In **Identity crawler**, configure identity crawling settings:
    1. **Identity crawling has been turned on for your connector as the ACLs are enabled** – This notification appears when ACLs are enabled.
    2. **Manage identity crawling logs** – When enabled, CloudWatch logs will show identities associated with local groups, as crawled during each sync job. If you disable this option post sync job completion (or partial run), you'll need to manually delete any associated identity crawling logs already generated.
       - **Enable identity crawling logs** – Identities crawled during data source sync will be logged.
       - **Disable identity crawling logs** – Identities crawled during data source sync will not be logged.

10. **IAM role** – Amazon Q Business requires an IAM role to access repository credentials and application content:
    1. **Choose an option** – Select an existing IAM role or create a new one.

11. In **Sync scope**, configure which content to sync:
    1. **Sync contents** – Choose the following options to select contents to sync. To further limit the contents that you want to sync for specific folders or files use the 'Entity regex patterns':
       - **My Drive** – Selected by
         default. Use this option if you want the files in all of
         your users’ My Drives to be included.
       - **Shared with me** – Selected by
         default. Use this option if you want the files from 'Shared
         with me' to be included.
       - **Shared Drives** – Selected by
         default. Use this option if you want to include shared
         drives. You can use the shared drive filter (see below) to
         sync files from specific shared drives.

    2. For **Maximum file size** – You can
       specify the file size limit in GB for Amazon Q crawling. Amazon Q
       crawls only files within the defined size limit. The default file
       size is 50MB. The maximum file size limit is 10 GB. Files must be
       larger than 0 MB and no larger than 10 GB. You can go up to 10 GB
       (10240 MB) if you enable **Video files** in
       **Multi-media content** configuration, and up
       to 2 GB (2048 MB) if you enable **Audio files** in
       **Multi-media content configuration**.

12. In **Additional configuration - _optional_**, configure additional filtering options. All content will be indexed by default. However, you can also limit the scope with these additional options:
    1. **Date filter** – Add a date range to filter content based on the last modified date:
       - **Start date** – Enter the start date in YYYY/MM/DD format.
       - **End date - _optional_** – Enter the end date in YYYY/MM/DD format.

    2. **Shared drives** – Add IDs of shared drives you want to include or exclude in your application:
       - **Include shared drives** – Add shared drive IDs to include.
       - **Exclude shared drives** – Add shared drive IDs to exclude.

    3. **Mime types** – Add Mime types to include or exclude in Google Drive account:
       - **Include mime types** – Add MIME types to include (e.g., `application/vnd.google-apps.document` for Google Docs, `application/pdf` for PDF files).
       - **Exclude mime types** – Add MIME types to exclude.

    4. **Multi-media content configuration – optional** –
       To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**. For more information, see [Extracting semantic meaning from embedded images and visuals](extracting-meaning-from-images.md "extracting-meaning-from-images.md").

    To extract audio transcriptions and video content, enable **Audio Files**. To extract video content, enable **Video files**. For more information, see [Extracting semantic meaning from audio and video Content](Audio-video-extraction.md "Audio-video-extraction.md"). 5. **Advanced settings**

    **Document deletion safeguard** - _optional_–To safeguard
    your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
    the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
    delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
    [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

13. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
14. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
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
