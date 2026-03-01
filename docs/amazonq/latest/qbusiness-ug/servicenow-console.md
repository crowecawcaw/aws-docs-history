# Connecting Amazon Q Business to ServiceNow Online using the console

The following procedure outlines how to connect Amazon Q Business to
ServiceNow Online using the AWS Management Console.

###### Connecting Amazon Q to ServiceNow Online

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **ServiceNow Online** data source to your Amazon Q application.
5. Then, on the **ServiceNow Online** data source page, enter
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
   - **ServiceNow host** – Enter your
     ServiceNow host name without the protocol. For
     example, `example.service-now.com`.

8. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 9. **Authentication** – Choose between **Basic
authentication** and **OAuth 2.0 authentication**
and then enter the following information for your **AWS Secrets Manager
secret**.

    1. **Secret name** – A name for your
     secret.
    2. Basic Authentication – Enter the **Secret
     name**, **Username**, and
     **Password** for your ServiceNow
     account.


    If using OAuth2 Authentication – Enter the **Secret
     name**, **Username**,
     **Password**, **Client ID**, and
     **Client Secret** that you created in your
     ServiceNow account.
    3. Choose **Save and add secret**.

10. **Configure VPC and security group –
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

11. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](servicenow-connector.md#servicenow-iam "servicenow-connector.md#servicenow-iam"). 12. **Sync scope** – Set the content that you want to
sync.

    1. For **Knowledge articles**, choose from the following
     options :




    	* **Knowledge articles** – Choose to index
    	 knowledge articles.
    	* **Knowledge article attachments** –
    	 Choose to index knowledge article attachments.
    	* **Type of knowledge articles** –
    	 Choose between **Only public articles** and
    	 **Knowledge articles based on
    	 ServiceNow filter query**, based
    	 on your use case. If you select **Include articles based
    	 on ServiceNow filter query**, you
    	 must enter a **Filter query** copied from your
    	 ServiceNow account. Example filter queries
    	 include: `workflow_state=draft^EQ`,
    	 `kb_knowledge_base=dfc19531bf2021003f07e2c1ac0739ab^text
    	 ISNOTEMPTY^EQ`, and
    	 `article_type=text^active=true^EQ`.


    	###### Important

    	 If you choose to crawl **Only public
    	 articles**, Amazon Q crawls only
    	 knowledge articles assigned a public access role in
    	 ServiceNow Online.
    	* **Include articles based on short description
    	 filter** – Specify regular expression
    	 patterns to include or exclude specific articles. For example,
    	 use `.*article[1,2].*` to include articles containing
    	 `article1` or `article2.` in their
    	 short descriptions. Use `(^mystart.*|.*endwith$)` to
    	 crawl articles with short descriptions starting with
    	 `mystart` or ending with
    	 `endwith`.
    2. For **Service catalog items**:




    	* **Service catalog items** – Choose to
    	 index service catalog items.
    	* **Service catalog item attachments** –
    	 Choose to index service catalog item attachments.
    	* **Active service catalog items** –
    	 Choose to index active service catalog items.
    	* **Inactive service catalog items** –
    	 Choose to index inactive service catalog items.
    	* **Filter query** – Choose to include
    	 service catalog items based on a filter defined in your
    	 ServiceNow instance. Example filter queries
    	 include:
    	 `short_descriptionLIKEAccess^category=2809952237b1300054b6a3549dbe5dd4^EQ`,
    	 `nameSTARTSWITHService^active=true^EQ`.
    	* **Include service catalog items based on short
    	 description filter** – Specify a regex
    	 pattern to include specific catalog items.
    3. For **Incidents**:




    	* **Incidents** – Choose to index
    	 service incidents.
    	* **Incident attachments** – Choose to
    	 index incident attachments.
    	* **Active incidents** – Choose to index
    	 active incidents.
    	* **Inactive incidents** – Choose to
    	 index inactive incidents.
    	* **Active incident type** – Choose
    	 between **All incidents**, **Open
    	 incidents**, **Open - unassigned
    	 incidents**, and **Resolved
    	 incidents**, depending on your use case.
    	* **Filter query** – Choose to include
    	 incidents based on a filter defined in your
    	 ServiceNow instance. Example filter queries
    	 include:
    	 `short_descriptionLIKETest^urgency=3^state=1^EQ`,
    	 and `priority=2^category=software^EQ` .
    	* **Include incidents based on short description
    	 filter** – Specify a regex pattern to
    	 include specific incidents.
    4. For **Maximum file size** – Specify the file
     size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only
     the files within the size limit you define. The default file size is
     50MB. The maximum file size should be greater than 0MB and less than or
     equal to 50MB.
    5. In **Additional configuration –
     *optional***:




    	* **Attachment regex patterns** – Add
    	 regular expression patterns to include or exclude specific
    	 attached files of catalogs, knowledge articles, and incidents.
    	 You can add up to 100 patterns.
    6. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.


    To extract audio transcriptions and video content, enable processing for the following file types:
    7. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

13. For **Sync mode**, choose how you want to update your index
    when your data source content changes. When you sync your data source with
    Amazon Q for the first time, all content is synced by
    default.
    - **Full sync** – Sync all content regardless of
      the previous sync status.
    - **New, modified, or deleted content sync** –
      Only sync new, modified, and deleted content.

14. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
15. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
16. **Field mappings** – A list of data source document
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

17. In **Data source details**, choose **Sync
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
