# Connecting Amazon Q Business to

SharePoint (Online) using the console

The following procedure outlines how to connect Amazon Q Business to
SharePoint (Online) using the AWS Management Console.

###### Connecting Amazon Q to SharePoint (Online)

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. From the left navigation menu, choose **Data
   sources**.
3. From the **Data sources** page, choose
   **Add data source**.
4. Then, on the **Add data sources** page, from
   **Data sources**, add the **SharePoint** data source to your Amazon Q application.
5. Then, on the **SharePoint (Online)** data source page, enter
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
   1. In **Source**, for **Hosting
      Method** – Choose **SharePoint
      Online**.
   2. **Site URLs specific to your SharePoint repository**
      – Enter the SharePoint host URLs. The format for the host URLs
      you enter is
      `https://yourcompany.sharepoint.com/sites/mysite`
      or `https://yourcompany.sharepoint.com`. The
      URL must start with `https` protocol. Separate URLs with a
      new line. You can add up to 100 URLs.
   3. **Domain** – Enter the
      SharePoint domain. For example, the domain in the URL
      `https://yourdomain.sharepoint.com/sites/mysite`
      is `yourdomain`. Note that the domain name in
      the URL and the domain name you're expected to enter in the domain field
      can be different.

8. **Authorization** – Choose whether Amazon Q
   will crawl user and group access control list (ACL) information from your data
   source. Amazon Q can use this information to only generate responses
   from documents your end users have access to. You can manage ACLs by selecting
   **Enable ACLs** to enable ACLs or **Disable
   ACLs** to disable them. To manage ACLs, you need specific IAM
   permissions. See [Grant permission to create data sources with ACLs
   disabled](setting-up.md#DisableAclOnDataSource "setting-up.md#DisableAclOnDataSource") for more details. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.

###### Note

Using ACL data to filter responses is not a replacement for user
authentication and authorization for your application. For information on
setting up identity management for Amazon Q, see [Integrating with an Identity Provider
(IdP)](idp-integration.md "idp-integration.md").

###### Important

If you don't specify a value, **Email** is considered as
the default value. 9. For **Authentication**, choose between
**Basic**, **Oauth 2.0**, **Azure
AD App-Only authentication**, and **SharePoint App-Only
authentication** based on your use case.

###### Note

OneNote can only be crawled by the connector using a Tenant ID, and with
OAuth 2.0, or SharePoint (Online) App Only authentication activated.

    1. If using **Microsoft Entra ID (formerly Azure AD) App-Only authentication**, enter
     the following information:




    	* **Tenant ID** – Tenant ID of your
    	 SharePoint account. To learn how to find your
    	 Tenant ID, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id "https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id")
    	 in Azure portal documentation.
    	* **Microsoft Entra ID (formerly Azure AD) self-signed X.509 certificate**
    	 – Certificate to authenticate the connector for Microsoft Entra ID (formerly Azure AD).
    	 For more information on how to do this, see [Granting access via Microsoft Entra ID (formerly Azure AD) App-Only](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread "https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread") and
    	 New-PnPAzureCertificate in *Microsoft
    	 developer documentation*.
    	* **Generate a certificate using OpenSSL**
    	 – As an example:



    	```
    	openssl req -x509 -newkey rsa:2048 -nodes -keyout /path/to/folder/private.key -out /path/to/folder/sharepoint.crt -days 365 -subj "/CN=ExampleCorp/emailAddress=example@domain.com
    	/C=US/ST=Texas/L=Dallas/O=ExampleCorp/OU=IT" -set_serial 1
    	```

    	###### Note


    	 Avoid using the -sha1 flag when generating certificates. SHA-1 is considered insecure and deprecated. Most modern browsers and
    	 systems reject certificates signed with SHA-1. By default, OpenSSL uses a secure algorithm such as SHA-256 when the -sha1 flag is omitted.
    	* For **AWS
    	 Secrets Manager secret** – Choose an
    	 existing secret or create a Secrets Manager secret to store
    	 your SharePoint authentication credentials. If you choose to
    	 create a secret, an AWS Secrets Manager secret window opens. Enter the
    	 following information in the window:




    		+ **Secret name** – A name for
    		 your secret.
    		+ **Client ID** – The Client ID
    		 generated when you complete Azure App registration for
    		 SharePoint (Online) in Entra
    		 ID.
    		+ **Private key** – A private
    		 key to authenticate the connector for Microsoft Entra ID (formerly Azure AD).
    		+ **Register a new app in the Microsoft Azure
    		 portal**:




    			1. Log in to the Azure Portal with your
    			 Microsoft account.
    			2. Choose New Registration:




    				1. Provide the name for your application. In
    				 the example we are using the name
    				 `TargetApp`. The Amazon Q Business
    				 application uses TargetApp to connect to the
    				 SharePoint Online site to crawl and index the
    				 data.
    				2. Choose "Accounts" in the organizational
    				 directory. (`Tenant name` only - Single
    				 tenant).
    				3. Choose "Register".
    				4. Note down the application (client ID and the
    				 directory (tenant) on the Overview page, as you'll
    				 need them when prompted for "TargetApp-ClientId"
    				 and "TenantId".
    				5. Choose API permissions under "Manage" in the
    				 navigation pane.
    				6. Choose "Add a permission" to allow the
    				 application to read data in your organization's
    				 directory regarding the signed-in user.
    				7. Choose "Sharepoint".
    				8. Choose "Application permissions".
    				9. Choose "Sites.FullControl.All" from the User
    				 section.
    				10. Choose "Add permissions".
    			3. On the options menu, choose to "Remove" a
    			 permssion.
    			4. Remove the original `User.Read -
    			 Delegated` permission.
    			5. Choose "Grant admin content" for the Default
    			 Directory.
    2. If using **SharePoint App-Only authentication**,
     enter the following information:




    	* **Tenant ID**–Tenant ID of your
    	 SharePoint account. To learn how to find your
    	 Tenant ID, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id "https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id")
    	 in Azure portal documentation.
    	* For **AWS Secrets Manager secret** — Choose an
    	 existing secret or create a Secrets Manager secret to store
    	 your SharePoint authentication credentials. If you choose to
    	 create a secret, an AWS Secrets Manager secret window opens. Enter the
    	 following information in the window:




    		+ **Secret name** – A name for
    		 your secret.
    		+ **SharePoint client ID** – The
    		 SharePoint client ID you generated
    		 when you registered App-Only at Tenant Level. ClientID
    		 format is `ClientID@TenantId`.
    		 For example,
    		 `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe.`
    		+ **SharePoint client secret** –
    		 The SharePoint client secret generated
    		 when your register for App-Only at Tenant Level.
    		+ **Client ID** – The Microsoft Entra ID (formerly Azure AD)
    		 client ID generated when you register
    		 SharePoint in Microsoft Entra ID (formerly Azure AD).
    		+ **Client secret** – The Microsoft Entra ID (formerly Azure AD)
    		 client secret generated when you register
    		 SharePoint to Microsoft Entra ID (formerly Azure AD).
    3. If using **OAuth 2.0 authentication**, you must
     disable MFA in SharePoint. This is not recommended, but if you choose to
     use OAuth 2.0 authentication anyway, enter the following
     information:




    	* **Tenant ID** – Tenant ID of your
    	 SharePoint account. To learn how to find your
    	 Tenant ID, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id "https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id")
    	 in Azure portal documentation.
    	* For **AWS Secrets Manager secret** – Choose an
    	 existing secret or create a Secrets Manager secret to store
    	 your SharePoint authentication credentials. If you choose to
    	 create a secret, an AWS Secrets Manager secret window opens. Enter the
    	 following information in the window:




    		+ **Secret name** – A name for
    		 your secret.
    		+ **Username** – Username for
    		 your SharePoint account.
    		+ **Password** – Password for
    		 your SharePoint account.
    		+ **Client ID** – The Client ID
    		 generated when you complete Azure App registration for
    		 SharePoint (Online) in Entra
    		 ID.
    		+ **Client secret** – The Client
    		 secret generated when you complete Azure App
    		 registration for SharePoint (Online) in
    		 Entra ID.
    4. If using **Basic Authentication**, you must disable
     MFA in SharePoint. This is not recommended, but if you choose to use
     Basic Auth anyway, enter the following information:




    	* For **AWS Secrets Manager secret** – Choose an
    	 existing secret or create a Secrets Manager secret to store
    	 your SharePoint authentication credentials. If you choose to
    	 create a secret, an AWS Secrets Manager secret window opens. Enter the
    	 following information in the window:




    		+ **Secret name** – A name for
    		 your secret.
    		+ **Username** – Username for your
    		 SharePoint account.
    		+ **Password** – Password for
    		 your SharePoint account.

10. **Configure VPC and security group –
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

    The SharePoint connector supports Microsoft Entra ID (formerly Azure AD) groups associated with documents. In order
    for Microsoft Entra ID (formerly Azure AD) group members to search the data, you have to integrate Microsoft Entra ID (formerly Azure AD) with IAM
    Identity Center.

1.  **IAM role** – Choose
    an existing IAM role or create an IAM role to access your repository credentials and
    index content.

###### Note

Creating a new service IAM role is recommended.

For more information, see [IAM role](sharepoint-cloud-connector.md#sharepoint-cloud-iam "sharepoint-cloud-connector.md#sharepoint-cloud-iam"). 2. In **Sync scope**, choose from the following options :

    1. **Select entities** – Choose the entities that
     you want to crawl. You can select to crawl **All**
     entities or any combination of **Files**,
     **Attachments**, **Links**,
     **Pages**, **Events**,
     **Comments**, and **List
     Data**.
    2. For **Maximum file size** – Specify the file
     size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only
     the files within the size limit you define. The default file size is
     50MB. The maximum file size should be greater than 0MB and less than or
     equal to 50MB.
    3. In **Additional configuration –
     *optional***, for **Entity
     regex patterns** – Add regular expression patterns
     for **Links**, **Pages**, and
     **Events** to include specific entities instead of
     syncing all your documents.
    4. In **Additional configuration**, for **Regex
     patterns** – Add regular expression patterns to
     include or exclude files by **File path**,
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


    ###### Note

    OneNote crawling is available only for OAuth 2.0 and SharePoint
     App Only authentication.
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

3.  In **Sync mode**, choose how you
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

4.  In **Sync run schedule**, for
    **Frequency** – Choose how often
    Amazon Q will sync with your data
    source. For more details, see [Sync run schedule](connector-concepts.md#connector-sync-run "connector-concepts.md#connector-sync-run"). To learn how to start a data sync job,
    see [Starting data source connector sync jobs](supported-datasource-actions.md#start-datasource-sync-jobs "supported-datasource-actions.md#start-datasource-sync-jobs").
5.  **Tags - _optional_** –
    Add tags to search and filter your resources or track your AWS costs. See [Tags](tagging.md "tagging.md") for more details.
6.  **Field mappings** – A list of data source document
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

7. In **Data source details**, choose **Sync
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
