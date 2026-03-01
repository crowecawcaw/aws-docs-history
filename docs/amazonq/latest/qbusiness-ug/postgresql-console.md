# Connecting Amazon Q Business to PostgreSQL using the console

The following procedure outlines how to connect Amazon Q Business to
PostgreSQL using the AWS Management Console.

###### Connecting Amazon Q to PostgreSQL

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **PostgreSQL** data source to your Amazon Q application.
5. Then, on the **PostgreSQL** data source page, enter
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
   1. **Host** – Enter the database host URL.
   2. **Port** – Enter the database port, for example,
      `5432`.
   3. **Instance** – Enter the database instance, for
      example `postgres`.
   4. **Enable SSL certificate location** – Choose
      to enter the Amazon S3 path to your SSL certificate file.

8. **Authorization** – Amazon Q Business crawls ACL information by default to ensure responses are generated only from
   documents your end users have access to. If supported for your connector, you can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs** to disable them.
   To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details.

See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. 9. In **Authentication** – Enter the following
information for your **AWS Secrets Manager secret**.

    1. **Secret name** – A name for your
     secret.
    2. For **Database username**, and
     **Password** – Enter the authentication
     credential values you copied from your database.
    3. Choose **Save**.

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

For more information, see [IAM role](postgresql-connector.md#postgresql-iam "postgresql-connector.md#postgresql-iam"). 12. In **Sync scope**, enter the following information:

    * **SQL query** – Enter SQL query statements
     like SELECT and JOIN operations. SQL queries must be less than 1000
     characters and not contain any semi-colons (;). Amazon Q will
     crawl all database content that matches your query.
    * **Primary key column** – Provide the primary
     key for the database table. This identifies the row in the table for
     which your SQL query is written. The connector uses the primary key
     column value to identify rows, detect changes, and crawl data.
    * **Title column** – Provide the name of the
     column in your database table that you want to designate as the column
     with document titles.
    * **Body column** – Provide the name of the
     column in your database table that you want to designate as the column
     with document body text.


    Your SQL query can include multiple columns in your table concatenated
     into a single body column with an assigned alias.

13. **Advanced settings**

**Document deletion safeguard** - _optional_–To safeguard
your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
[Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard"). 14. In **Additional configuration –
_optional_** – Configure the following
settings:

    * **Change-detecting columns** – Enter the names
     of the columns that Amazon Q will use to detect content
     changes. Amazon Q will re-index content when there is a
     change in any of these columns.
    * **Users' IDs column** – Enter the name of the
     column which contains User IDs to be allowed access to content.
    * **Groups column** – Enter the name of the
     column that contains groups to be allowed access to content.
    * **Source URLs column** – Enter the name of the
     column which contains Source URLs to be indexed.
    * **Time stamps column** – Enter the name of the
     column which contains time stamps. Amazon Q uses time stamp
     information to detect changes in your content and sync only changed
     content.
    * **Time zones column** – Enter the name of the
     column which contains time zones for the content to be crawled.
    * **Time stamps format** – Enter the name of the
     column which contains time stamp formats to use to detect content
     changes and re-sync your content.

15. In **Sync mode**, choose how you
    want to update your index when your data source
    content changes. When you sync your data source with
    Amazon Q for the first time, all content
    is synced by default.

        * **Full sync** – Sync
         all content regardless of the previous sync
         status.
        * **New or modified content
         sync** – Sync only new and modified
         documents.
        * **New, modified, or deleted
         content sync** – Sync only new,
         modified, and deleted documents.

    For more details, see [Sync mode](connector-concepts.md#connector-sync-mode "connector-concepts.md#connector-sync-mode").

16. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
17. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
18. **Field mappings** – A list of data source document
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
