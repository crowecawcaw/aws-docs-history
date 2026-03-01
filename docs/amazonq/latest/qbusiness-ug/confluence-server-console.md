# Connecting Amazon Q Business to Confluence (Server/Data Center) using the console

On the **Confluence** page, enter the following information:

1. **Name and description**, do the following:
   - For **Data source name** – Name your data
     source for easy tracking.

   ###### Note

   You can include hyphens (-) but
   not spaces. Maximum of 1,000 alphanumeric characters.
   - **Description –
     _optional_** – Add an optional
     description for your data source. This text is viewed only by Amazon Q Business administrators and can be edited later.

2. In **Source**, enter the following information:
   1. In **Source**, for **Hosting
      Method** – Choose **Confluence Server/Data
      Center**.
   2. **Confluence URL** – Enter the Confluence host URLs.
      The format for the host URL that you enter is
      `https://example.confluence.com`.

   ###### Important

   If you change or update your Confluence (Server/Data Center) data source URL,
   you also need to update your Secrets Manager secret to ensure a secure
   connection. 3. **SSL certificate location** – Enter the file
   path to an SSL certificate stored in an Amazon S3 bucket.

3. **Web proxy – _optional_**, enter
   the following information:
   1. **Host name** – Host name for your Confluence
      account.
   2. **Port number** – Port used by the host URL
      transport protocol.

4. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 5. For **Authentication** – Choose between
**Basic authentication**, **Oauth 2.0
authentication**, and **Personal Access Token
authentication** based on your use case. 6. **AWS Secrets Manager secret** – Choose an existing secret or
create a Secrets Manager secret to store your Confluence authentication
credentials. If you choose to create a secret, an AWS Secrets Manager secret window opens.
Enter the following information in the window:

    1. **Secret name** – A name for your
     secret.
    2. If using **Basic Authentication** – Enter the
     **Secret name**
    **Username**, and **Password** (
     Confluence Server/Data Center password) that you generated and downloaded
     from your Confluence account.


    If using **OAuth2.0 Authentication** – Enter
     the **Secret name**, **App key**,
     **App secret**, **Access token**,
     and **Refresh token** you created in your Confluence
     account.


    If using **Personal Access Token authentication**
     – Enter the **Secret name** and the **Confluence Server PAT token** that you created in your Confluence
     Server account.


    ###### Note

    Select **Rotate secret** if you want Amazon Q to rotate the secret automatically so that you don’t
     have to manually update the secret every time you sync.
    3. Choose **Save and add secret**.

7. **Configure VPC and security group –
   _optional_** – Choose
   whether you want to use a VPC. If you do, enter the following
   information:
   1. **Subnets** – Select up to 6
      repository subnets that define the subnets and IP ranges
      the repository instance uses in the selected VPC.
   2. **VPC security groups** –
      Choose up to 10 security groups that allow access to
      your data source. Ensure that the security group allows
      incoming traffic from Amazon EC2 instances and
      devices outside your VPC. For databases, security group
      instances are required.For more information, see [VPC](connector-concepts.md#connector-vpc "connector-concepts.md#connector-vpc").

8. **IAM role** – Choose
   an existing IAM role or create an IAM role to access your repository credentials and
   index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](confluence-server-connector.md#confluence-server-iam "confluence-server-connector.md#confluence-server-iam"). 9. In **Sync scope**, choose from the following options:

    1. In **Sync scope**, for **sync
     contents**, choose to sync from the following entity types:
     **Pages**, **Page comments**,
     **Page attachments**, **Blogs**,
     **Blog comments**, **Blog
     attachments**, **Personal spaces**, and
     **Archived spaces**.


    ###### Note


    **Page comments** and **Page
     attachments** can only be selected if you choose to
     sync **Pages**. **Blog comments**
     and **Blog attachments** can only be selected if
     you choose to sync **Blogs**.


    ###### Important

    You can crawl **Pages** and
     **Blogs** from one of more specific
     **Spaces**. If you don't specify a
     **Space key** regex pattern in
     **Additional configuration**, all
     **Pages** and **Blogs** will
     be crawled by default. If no **Space** is specified
     in the filter, all spaces will be crawled.
    2. For **Maximum file size** – Specify the file
     size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only
     the files within the size limit you define. The default file size is
     50MB. The maximum file size should be greater than 0MB and less than or
     equal to 50MB.
    3. In **Additional configuration –
     *optional***, for **Space
     and regex patterns**, specify whether to include or exclude
     specific spaces, URLs, or file types in your index using the
     following:




    	* **Space key** – For example,
    	 `my-space-123`. Select
    	 **Add** after entering each space key you
    	 want to add.


    	###### Note

    	If you don't specify a **Space key**
    	 regex pattern in **Additional
    	 configuration**, all **Pages**
    	 and **Blogs** will be crawled by default.
    	 If no **Space** is specified in the filter,
    	 all spaces will be crawled.
    	* **URL** – For example,
    	 `.*/MySite/MyDocuments/`. Select
    	 **Add** after entering each URL you want to
    	 add.
    	* **File type** – For example,
    	 `.*\.pdf` or
    	 `.*\.txt`. Select
    	 **Add** after entering each file type you
    	 want to add.


    	* For **Entity title regex patterns** –
    	 Specify regular expression patterns to include or exclude
    	 certain **Blogs**, **Pages**,
    	 **Comments**, and
    	 **Attachments** by titles.
    ###### Note

    If you want to crawl a specific page or subpage, you can use page
     title regex patterns to either include or exclude this page.
    4. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.


    To extract audio transcriptions and video content, enable processing for the following file types:
    5. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

10. For **Sync mode**, choose how you want to update your index
    when your data source content changes. When you sync your data source with
    Amazon Q for the first time, all content is synced by
    default.
    - **Full sync** – Sync all content regardless of
      the previous sync status.
    - **New, modified, or deleted content sync** –
      Sync only new, modified, and deleted documents.

11. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
12. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
13. **Field mappings** – A list of data source document
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

14. In **Data source details**, choose **Sync
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
