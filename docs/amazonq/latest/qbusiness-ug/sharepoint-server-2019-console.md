# Connecting Amazon Q Business to SharePoint Server 2019 using the console

The following procedure outlines how to connect Amazon Q Business to
SharePoint Server 2019 using the AWS Management Console.

###### Connecting Amazon Q to SharePoint Server 2019

1.  Sign in to the AWS Management Console and open the Amazon Q Business
    console.
2.  From the left navigation menu, choose **Data
    sources**.
3.  From the **Data sources** page, choose
    **Add data source**.
4.  Then, on the **Add data sources** page, from
    **Data sources**, add the **SharePoint** data source to your Amazon Q application.
5.  Then, on the **SharePoint Server 2019** data source page, enter
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

7.  In **Source**, enter the following information:
    1. In **Source**, for **Hosting
       Method** – Choose **SharePoint
       Server**.
    2. **Choose SharePoint Version** –
       Choose **SharePoint 2019**.
    3. **Site URLs specific to your SharePoint repository**
       – Enter the SharePoint host URLs. The format for the host URLs
       you enter is
       `https://yourcompany/sites/mysite`. The URL
       must start with `https` protocol. Separate URLs with a new
       line. You can add up to 100 URLs.
    4. **Domain** – Enter the
       SharePoint domain.
    5. **SSL certificate location** – Enter the
       Amazon S3 path to your SSL certificate file.

8.  For **Web proxy – _optional_**
    – Enter the host name (without the `http://` or
    `https://` protocol), and the port number used by the host URL
    transport protocol. The numeric value of the port number must be between 0 and
9.
10. For **Authorization** – Amazon Q Business crawls
    ACL information by default to ensure responses are generated only from documents
    your end users have access to. You can manage ACLs by selecting **Enable ACLs** to enable ACLs or **Disable ACLs**
    to disable them. To manage ACLs, you need specific IAM permissions. See [Grant permission to create data sources with ACLs
    disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. For
    SharePoint Server, you can choose from the following ACL
    options:
    1. **Email ID with Domain from IDP** – Access
       control is based on email IDs that are extracted from email domains
       fetched from the underlying identity provider (IdP). You provide the IdP
       connection details in your Secrets Manager secret during
       **Authentication**.
    2. **Email ID with Custom Domain** – Access
       control is based on email IDs. Provide the email domain value. For
       example, `"amazon.com"`. The email domain is
       used to construct the email ID for access control. You must enter your
       email domain using **Add Email Domain**.See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.

11. For **Authentication**, choose between **SharePoint
    App-Only authentication**, **NTLM
    authentication**, and **Kerberos authentication**,
    based on your use case.
    1. Enter the following information for both **NTLM
       authentication** and **Kerberos
       authentication**:

    For **AWS Secrets Manager secret** – Choose an existing
    secret or create a Secrets Manager secret to store your
    SharePoint authentication credentials. If you choose
    to create a secret, an AWS Secrets Manager secret window opens. Enter the
    following information in the window:

        * **Secret name** – A name for your
         secret.
        * **Username** – Username for your
         SharePoint account.
        * **Password** – Password for your
         SharePoint account.

    If using **Email ID with Domain from IDP**, also
    enter your:

        * **LDAP Server Endpoint** – Endpoint of
         LDAP server, including protocol and port number. For example:
         `ldap://example.com:389`.
        * **LDAP Search Base** – Search base of
         LDAP user. For example:
         `CN=Users,DC=sharepoint,DC=com`.
        * **LDAP username** – Your LDAP
         username.
        * **LDAP Password** – Your LDAP
         password.

    2. Enter the following information for **SharePoint App-Only
       authentication**:

    For **AWS Secrets Manager secret** – Choose an existing
    secret or create a Secrets Manager secret to store your
    SharePoint authentication credentials. If you choose
    to create a secret, an AWS Secrets Manager secret window opens. Enter the
    following information in the window:

        * **Secret name** – A name for your
         secret.
        * **Client ID** – The
         SharePoint client ID that you generated when
         you registered App Only at Site Level. The ClientID format is
         ClientID@TenantId. For example,
         `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe`.
        * **SharePoint client secret** – The
         SharePoint client secret generated when your
         register for App Only at Site Level.


        **Note:** Because client IDs and
         client secrets are generated for single sites only when you
         register SharePoint Server for App Only authentication, only one
         site URL is supported for SharePoint App Only
         authentication.

    If using **Email ID with Domain from IDP**, also
    enter your:

        * **LDAP Server Endpoint** – Endpoint of
         LDAP server, including protocol and port number. For example:
         `ldap://example.com:389`.
        * **LDAP Search Base** – Search base of
         LDAP user. For example:
         `CN=Users,DC=sharepoint,DC=com`.
        * **LDAP username** – Your LDAP user
         name.
        * **LDAP Password** – Your LDAP
         password.

12. **Configure VPC and security group –
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

13. **Identity crawler** – Amazon Q crawls
    identity information from your data source by default to ensure responses are
    generated only from documents end users have access to. Only **Local
    Group Members** will be crawled by **Identity
    crawler**. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler").
14. **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](sharepoint-server-2019-connector.md#sharepoint-server-2019-iam "sharepoint-server-2019-connector.md#sharepoint-server-2019-iam"). 14. In **Sync scope**, choose from the following options :

    1. **Select entities** – Choose the entities that
     you want to crawl. You can select to crawl **All**
     entities or any combination of **Files**,
     **Attachments**, **Links**,
     **Pages**, **Events** and
     **List Data**.
    2. In **Additional configuration –
     *optional***, for **Entity
     regex patterns** – Add regular expression patterns
     for **Links**, **Pages**, and
     **Events** to include specific entities instead of
     syncing all your documents.
    3. **Regex patterns** – Add regular expression
     patterns to include or exclude files by **File path**,
     **File name**, **File type**,
     **OneNote section name**, and **OneNote
     page name** instead of syncing all your documents. You can
     add up to 100 patterns.


    ###### Note

    Any valid regex pattern is supported. For example, if you use the
     regex `^QBusiness*`, any content starting with the word
     `QBusiness` followed by any number of characters will
     be filtered (`QBusiness_doc1` or `QBusiness`,
     but not `doc1_QBusiness`).
    4. **Multi-media content configuration – optional** –
     To enable content extraction from embedded images and visuals in documents, choose **Visual content in documents**.


    To extract audio transcriptions and video content, enable processing for the following file types:
    5. **Advanced settings**


    **Document deletion safeguard** - *optional*–To safeguard
     your documents from deletion during a sync job, select **On** and enter an integer between 0 - 100. If
     the percentage of documents to be deleted in your sync job exceeds the percentage you selected, the
     delete phase will be skipped and no documents from this data source will be deleted from your index. For more information, see
     [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").

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
