# Connecting using the legacy

Microsoft Teams connector (Console)

The legacy Microsoft Teams connector provides comprehensive configuration options including entity type selection, field mappings, and VPC settings. Use this procedure to connect Amazon Q Business to Microsoft Teams using the legacy connector.

###### To connect Amazon Q to Microsoft Teams using the legacy connector

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **Microsoft Teams** data source to your Amazon Q application.
5. Then, on the **Microsoft Teams** data source page, enter
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

7. In **Source**, enter the following information:
   1. **Tenant ID** – Enter your Tenant ID.

   ###### Note

   Your Microsoft Tenant ID is a globally unique identifier that's
   necessary to configure each connector instance. Your Tenant ID is
   different from your organization name or domain and can be found in
   the **Properties** section of your Azure
   Active Directory Portal.

8. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 9. For **Authentication**, in **AWS Secrets Manager**
– Choose between **Create and add new secret** and
**Use existing secrets**.

    1. If you choose **Use existing secrets**, select an
     existing secret.


    If you choose **Create and add a new secret**, enter
     the following information in the **Create AWS Secrets Manager
     secret** section:


    	1. **Secret name** – A name for your
    	 secret.
    	2. **Client ID** – Enter the Client ID
    	 you generated after registering your application for use. You
    	 can find this Client ID in **App
    	 registrations** in your Azure Active
    	 Directory Portal.
    	3. **Client Secret** – Enter the client
    	 secret that you generated from your Teams
    	 account.

10. **Payment model** – Choose the payment model
    associated with your Microsoft Teams account. Model A payment models are
    restricted to licensing and payment models that require security compliance.
    Model B payment models are suitable for licensing and payment models that don't
    require security compliance.
11. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](teams-connector.md#teams-iam "teams-connector.md#teams-iam"). 12. **Sync scope** – Choose the content you want to
sync.

    1. Choose **All** to crawl and sync all your
     documents.
    2. For **Chat**, choose from the following
     options:


    	1. Choose **Chat** to crawl and sync all chats.
    	 If you choose this option, Amazon Q Business also crawls
    	 **Chat messages** and **Chat
    	 files** by default.
    	2. Choose **Chat messages** to crawl and sync
    	 only all chat messages.
    	3. Choose **Chat files** to crawl and sync only
    	 all chat files.
    3. For **Teams**, choose from the following
     options:


    	1. Choose **Teams** to crawl and sync all teams.
    	 If you choose this option, Amazon Q Business also crawls
    	 **Channel posts**, **Channel files
    	 and folders** and **Channel wiki**
    	 by default.
    	2. Choose **Channel posts** to crawl and sync
    	 only all channel posts.
    	3. Choose **Channel files and folders** to crawl
    	 and sync only all channel files and folders.
    	4. Choose **Channel wiki** to crawl and sync
    	 only all channel wikis.
    4. For **Calendar**, choose from the following
     options:


    	1. Choose **Calendar** to crawl and sync your
    	 calendar. If you choose this option, Amazon Q Business
    	 also crawls **Meetings**, **Meeting
    	 chats**, **Meeting files** and
    	 **Meeting notes** by default.
    	2. Choose **Meetings** to crawl and sync only
    	 all meetings.
    	3. Choose **Meeting chats** to crawl and sync
    	 only all meeting chats.
    	4. Choose **Meeting files** to crawl and sync
    	 only all meeting files.
    	5. Choose **Meeting notes** to crawl and sync
    	 only all meeting notes.
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

13. For **Maximum file size** – Specify the file size
    limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files
    within the size limit you define. The default file size is 50MB. The maximum
    file size should be greater than 0MB and less than or equal to 50MB.
14. In **Additional configuration –
    _optional_**, configure the following comprehensive options:
    - **Calendar crawling** – Enter the date range for
      which the connector will crawl your calendar content.
    - **User email** – Enter the emails of the users
      you want to include in your application.
    - **Team names** – Add patterns to include or
      exclude teams found in Microsoft Teams from your application.
    - **Channel names** – Add patterns to include or
      exclude channels found in Microsoft Teams from your
      application.
    - **Attachment regex patterns** – Add regular
      expression patterns to include or exclude certain attachment for all
      supported entities. You can add up to 100 patterns.

15. **Field mappings** – A list of data source document
    attributes to map to your index fields.

###### Note

Add or update the fields from the **Data
source details** page after you finish adding your data source.

You can choose from two types of fields:

    1. **Default** – Automatically created by
     Amazon Q on your behalf based on common fields in your data source. You
     can't edit these.
    2. **Custom** – Automatically created by
     Amazon Q on your behalf based on common fields in your data source. You
     can edit these. You can also create and add new custom fields.


    ###### Note

    Support for adding custom fields varies by connector. You
     won't see the **Add field** option if your
     connector doesn't support adding custom fields.For more information, see [Field mappings](connector-concepts.md#connector-field-mappings "connector-concepts.md#connector-field-mappings").

16. **Configure VPC and security group –
    _optional_** – Choose
    whether you want to use a VPC. If you do, enter the following
    information:
    1.  **Subnets** – Select up to 6
        repository subnets that define the subnets and IP ranges
        the repository instance uses in the selected VPC.
    2.  **VPC security groups** –
        Choose up to 10 security groups that allow access to
        your data source. Ensure that the security group allows
        incoming traffic from Amazon EC2 instances and
        devices outside your VPC. For databases, security group
        instances are required.For more information, see [VPC](connector-concepts.md#connector-vpc "connector-concepts.md#connector-vpc").

17. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
18. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
19. In **Data source details**, choose **Sync
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
