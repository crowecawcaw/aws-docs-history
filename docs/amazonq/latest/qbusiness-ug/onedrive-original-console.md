# Using the console

The following procedure outlines how to connect Amazon Q Business to
Microsoft OneDrive using the original connector with the AWS Management Console.

###### Connecting Amazon Q to Microsoft OneDrive original connector

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

9. **Configure VPC and security group –
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

10. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](onedrive-connector.md#onedrive-iam "onedrive-connector.md#onedrive-iam"). 11. In **Sync scope**, for **Select OneDrive
users**, choose between the following options:

    * **Add a username file** – Choose to add a
     usernames file saved in an Amazon S3 bucket. Provide the path to
     the file by choosing **Browse**.


    ###### Note

    If you choose this option, the IAM role for the
     data source must have read permissions for the Amazon S3
     bucket where the file is stored.
    * **Add usernames here** – You can add a maximum
     of 10 users using this option. To add more than 10 users, please create
     a file containing the usernames and choose **Add a user name
     file**.

12. For **Additional configuration –
    _optional_**:
    - For **Filter Patterns** – Add filter
      patterns to include or exclude certain files. You can add up to 100
      patterns.

13. **Multi-media content configuration – optional** –
    To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.
14. **Advanced settings**

**Document deletion safeguard** - _optional_–To safeguard
your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
[Document deletion
safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard"). 15. For **Maximum file size** – Specify the file size
limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files
within the size limit you define. The default file size is 50MB. The maximum
file size should be greater than 0MB and less than or equal to 50MB. 16. For **Sync mode**, choose how you want to update your index
when your data source content changes. When you sync your data source with
Amazon Q for the first time, all content is synced by
default.

    * **Full sync** – Sync all content regardless of
     the previous sync status.
    * **New, modified, or deleted content sync** –
     Only sync new, modified, and deleted content.

17. In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
18. **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
19. **Field mappings** – A list of data source document
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

20. In **Data source details**, choose **Sync
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
