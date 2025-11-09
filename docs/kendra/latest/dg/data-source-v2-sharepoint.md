# SharePoint connector

V2.0

SharePoint is a collaborative website building service that you can use to
customize web content and create pages, sites, document libraries, and lists. You can
use Amazon Kendra to index your SharePoint data source.

Amazon Kendra currently supports SharePoint Online and SharePoint
Server (2013, 2016, 2019, and Subscription Edition).

###### Note

SharePoint connector V1.0 / SharePointConfiguration API ended in 2023. We recommend
migrating to or using SharePoint connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra SharePoint data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v2-sharepoint "#supported-features-v2-sharepoint")
- [Prerequisites](#prerequisites-v2-sharepoint "#prerequisites-v2-sharepoint")
- [Connection
  instructions](#data-source-procedure-v2-sharepoint "#data-source-procedure-v2-sharepoint")
- [Notes](#sharepoint-notes "#sharepoint-notes")

## Supported features

Amazon Kendra SharePoint data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your SharePoint data
source, make these changes in your SharePoint and AWS
accounts.

You are required to provide authentication credentials, which you securely store
in an AWS Secrets Manager secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

**In SharePoint Online, make sure you
have:**

- Copied your SharePoint instance URLs. The format for the host URL
  you enter is `https://yourdomain.com/sites/mysite`.
  Your URL must start with `https`.
- Copied the domain name of your SharePoint instance URL.
- Noted your basic authentication credentials containing the user name and
  password with site admin permissions to connect to SharePoint
  Online.
- Deactivated **Security Defaults** in your Azure portal
  using an administrative user. For more information on managing security
  default settings in the Azure portal, see [Microsoft documentation on how to enable/disable security
  defaults](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-conditional-access?view=o365-worldwide&tabs=secdefaults#security-defaults-1 "https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-conditional-access?view=o365-worldwide&tabs=secdefaults#security-defaults-1").
- Deactivated multi-factor authentication (MFA) in your SharePoint
  account, so that Amazon Kendra is not blocked from crawling your
  SharePoint content.
- **If using authentication type other than Basic
  authentication:** Copied the tenant ID of your
  SharePoint instance. For details on how to find your tenant ID, see
  [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id").
- If you need to migrate to cloud user authentication with Microsoft Entra,
  see [Microsoft documentation on cloud authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication "https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication").
- **For OAuth 2.0 authentication and OAuth 2.0 refresh
  token authentication:** Noted your **Basic
  authentication** credentials containing the user name and
  password you use to connect to SharePoint Online and the client ID
  and client secret generated after registering SharePoint with Azure
  AD.
  - **If you're not using ACL**, added
    the following permissions:

  | **Microsoft<br>Graph**                                                                                                               | **SharePoint**                                                    |
  | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
  | • Notes.Read.All (Application)—Read all<br>OneNote notebooks<br>• Sites.Read.All (Application)—Read<br>items in all site collections | • AllSites.Read (Delegated)—Read items<br>in all site collections |

  ###### Note

  Note.Read.All and Sites.Read.All are required only if you want
  to crawl OneNote Documents.

  If you want to crawl specific sites, the permission can be
  restricted to specific sites rather than all sites available in
  the domain. You configure **Sites.Selected
  (Application)** permission. With this API
  permission, you need to set access permission on every site
  explicitly through Microsoft Graph API. For more information,
  see [Microsoft's blog on Sites.Selected
  permissions](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476 "https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476").
  - **If you're using ACL**, added the
    following permissions:

  | **Microsoft<br>Graph**                                                                                                                                                                                                                                                                                                                                                   | **SharePoint**                                                    |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
  | • Group.Member.Read.All<br>(Application)—Read all group<br>memberships<br>• Notes.Read.All (Application)—Read all<br>OneNote notebooks<br>• Sites.FullControl.All<br>(Delegated)—Required to retrieve ACLs of<br>the documents<br>• Sites.Read.All (Application)—Read<br>items in all site collections<br>• User.Read.All (Application)—Read all<br>users' full profiles | • AllSites.Read (Delegated)—Read items<br>in all site collections |

  ###### Note

  GroupMember.Read.All and User.Read.All are required only if
  **Identity crawler** is activated.

  If you want to crawl specific sites, the permission can be
  restricted to specific sites rather than all sites available in
  the domain. You configure **Sites.Selected
  (Application)** permission. With this API
  permission, you need to set access permission on every site
  explicitly through Microsoft Graph API. For more information,
  see [Microsoft's blog on Sites.Selected
  permissions](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476 "https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476").

- **For Azure AD App-Only authentication:**
  Private key and the Client ID you generated after registering
  SharePoint with Azure AD. Also note the X.509 certificate.
  - **If you're not using ACL**, added
    the following permissions:

  | **SharePoint**                                                                                  |
  | ----------------------------------------------------------------------------------------------- |
  | • Sites.Read.All (Application)—Required<br>to access items and lists in all site<br>collections |

  ###### Note

  If you want to crawl specific sites, the permission can be
  restricted to specific sites rather than all sites available in
  the domain. You configure **Sites.Selected
  (Application)** permission. With this API
  permission, you need to set access permission on every site
  explicitly through Microsoft Graph API. For more information,
  see [Microsoft's blog on Sites.Selected
  permissions](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476 "https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476").
  - **If you're using ACL**, added the
    following permissions:

  | **SharePoint**                                                                         |
  | -------------------------------------------------------------------------------------- |
  | • Sites.FullControl.All<br>(Application)—Required to retrieve ACLs of<br>the documents |

  ###### Note

  If you want to crawl specific sites, the permission can be
  restricted to specific sites rather than all sites available in
  the domain. You configure **Sites.Selected
  (Application)** permission. With this API
  permission, you need to set access permission on every site
  explicitly through Microsoft Graph API. For more information,
  see [Microsoft's blog on Sites.Selected
  permissions](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476 "https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476").

- **For SharePoint App-Only
  authentication:** Noted your SharePoint client ID and
  client secret generated while granting permission to SharePoint App
  Only, and your Client ID and Client secret generated when you registered
  your SharePoint app with Azure AD.

###### Note

SharePoint App-Only Authentication is _not_
supported for SharePoint 2013 version.

    + **(Optional) If you're crawling OneNote
     documents and using **Identity
     crawler****, added the following
     permissions:




    | **Microsoft<br>Graph** |
    | --- |
    | • GroupMember.Read.All<br>(Application)—Read all group<br>memberships<br>• Notes.Read.All (Application)—Read all<br>OneNote notebooks<br>• Sites.Read.All (Application)—Read<br>items in all site collections<br>• User.Read.All (Application)—Read all<br>users' full profiles |

###### Note

No API permissions are required for crawling entities using
**Basic authentication** and SharePoint
**App-only authentication**.

**In SharePoint Server, make sure you
have:**

- Copied your SharePoint instance URLs and the domain name of your
  SharePoint URLs. The format for the host URL you enter is
  `https://yourcompany/sites/mysite`. Your URL
  must start with `https`.

###### Note

(On-premise/server) Amazon Kendra checks if the endpoint information included in
AWS Secrets Manager is the same the endpoint information specified in your data source
configuration details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a
security issue where a user doesn’t have permission to perform an action but uses
Amazon Kendra as a proxy to access the configured secret and perform the action. If you
later change your endpoint information, you must create a new secret to sync this
information.

- Deactivated multi-factor authentication (MFA) in your SharePoint
  account, so that Amazon Kendra is not blocked from crawling your
  SharePoint content.
- If using **SharePoint App-Only authentication** for
  access control:

      + Copied the SharePoint client ID generated when you
       registered App Only at Site Level. Client ID format is
       ClientId@TenantId. For example,
       `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe`.
      + Copied the SharePoint client secret generated when you
       registered App Only at Site Level.

  **Note:** Because client IDs and client
  secrets are generated for single sites only when you register
  SharePoint Server for App Only authentication, only one site URL is
  supported for SharePoint App Only authentication.

###### Note

SharePoint App-Only Authentication is _not_
supported for SharePoint 2013 version.

- If using **Email ID with Custom Domain** for access
  control:
  - Noted your custom email domain value—for example:
    "`amazon.com`".

- If using **Email ID with Domain from IDP** authorization,
  copied your:
  - LDAP Server Endpoint (endpoint of LDAP server including protocol
    and port number). For example:
    `ldap://example.com:389`.
  - LDAP Search Base (search base of the LDAP user). For example:
    `CN=Users,DC=sharepoint,DC=com`.
  - LDAP user name and LDAP password.

- Either configured NTLM authentication credentials **or** configured Kerberos authentication credentials containing
  a user name (SharePoint account user name) and password
  (SharePoint account password).

**In your AWS account, make sure you
have:**

- [Created
  an Amazon Kendra index](create-index.md "create-index.md") and, if using the API, noted the index
  ID.
- [Created an IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if
  using the API, noted the ARN of the IAM role.

###### Note

If you change your authentication type and credentials, you must
update your IAM role to access the correct AWS Secrets Manager secret ID.

- Stored your SharePoint authentication credentials in an
  AWS Secrets Manager secret and, if using the API, noted the ARN of the
  secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

If you don’t have an existing IAM role or secret, you can use the
console to create a new IAM role and Secrets Manager secret when you
connect your SharePoint data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection

instructions

To connect Amazon Kendra to your SharePoint data source, you must
provide details of your SharePoint credentials so that Amazon Kendra
can access your data. If you have not yet configured SharePoint for Amazon Kendra see [Prerequisites](#prerequisites-v2-sharepoint "#prerequisites-v2-sharepoint").

Console: SharePoint Online
**To connect Amazon Kendra to
SharePoint Online**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **SharePoint connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **SharePoint connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security**
    page, enter the following information:
    1. **Hosting Method**—Choose
       **SharePoint
       Online**.
    2. **Site URLs specific to your
       SharePoint
       repository**—Enter the
       SharePoint host URLs. The format for the
       host URLs you enter is
       `https://yourdomain.sharepoint.com/sites/mysite`.
       The URL must start with `https` protocol.
       Separate URLs with a new line. You can add up to 100
       URLs.
    3. **Domain**—Enter the
       SharePoint domain. For example, the domain
       in the URL
       `https://yourdomain.sharepoint.com/sites/mysite`
       is `yourdomain`.
    4. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").

    You can also choose the type of user ID, whether
    the user principal name or the user email fetched
    from the Azure Portal. If you don't specify, email
    is used by default. 5. **Authentication**—Choose
    either basic, OAuth 2.0, Azure AD App-Only
    authentication, SharePoint App-Only
    authentication, or OAuth 2.0 refresh token
    authentication. You either choose an existing
    AWS Secrets Manager secret to store your
    authentication credentials, or create a
    secret.

        1. If using **Basic
         Authentication**, your secret must
         include a secret name, SharePoint user
         name and password.
        2. If using **OAuth 2.0
         authentication**, your secret must
         include the SharePoint tenant ID, secret
         name, SharePoint user name, password,
         Azure AD client ID generated when you register
         SharePoint in Azure AD, and Azure AD
         client secret generated when you register
         SharePoint in Azure AD.
        3. If using **Azure AD App-Only
         authentication**, your secret must
         include the SharePoint tenant ID, Azure AD
         self-signed X.509 certificate, secret name, Azure
         AD client ID generated when you register
         SharePoint in Azure AD, and private key to
         authenticate the connector for Azure AD.
        4. If using **SharePoint
         App-Only authentication**, your secret
         must include the SharePoint tenant ID,
         secret name, SharePoint client ID you
         generated when you registered App Only at Tenant
         Level, SharePoint client secret generated
         when your register for App Only at Tenant Level,
         Azure AD client ID generated when you register
         SharePoint in Azure AD, and Azure AD
         client secret generated when you register
         SharePoint to Azure AD.


        The SharePoint client ID format is
         `ClientID@TenantId`. For
         example,
         `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe`.
        5. If using **OAuth 2.0 refresh token
         authentication**, your secret must
         include the SharePoint tenant ID, secret
         name, unique Azure AD client ID generated when you
         register SharePoint in Azure AD, Azure AD
         client secret generated when you register
         SharePoint to Azure AD, refresh token
         generated to connect Amazon Kendra to
         SharePoint.

    6. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    7. **Identity crawler**—Specify whether to turn on
       Amazon Kendra’s identity crawler. The identity crawler uses the access control list
       (ACL) information for your documents to filter search results based on the user or their
       group access to documents. If you have an ACL for your documents and choose to use your ACL,
       you can then also choose to turn on Amazon Kendra’s identity crawler to configure
       [user
       context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
       all documents can be publicly searched. If you want to use access control for your documents
       and identity crawler is turned off, you can alternatively use the
       [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
       API to upload user and group access information for user context filtering.

    You can also choose to crawl local group mapping
    or Azure Active Directory group mapping.

    ###### Note

    AD Group mapping crawling is available only
    for OAuth 2.0, OAuth 2.0 refresh token, and
    SharePoint App Only authentication. 8. **IAM role**—Choose an existing IAM
    role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 9. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. In **Sync scope**, choose from
       the following options :
       1. **Select
          entities**—Choose the entities you
          want to crawl. You can select to crawl
          **All** entities or any
          combination of **Files**,
          **Attachments**,
          **Links**
          **Pages**,
          **Events**,
          **Comments**, and **List
          Data**.
       2. In **Additional
          configuration**, for **Entity
          regex patterns**—Add regular
          expression patterns for
          **Links**,
          **Pages**, and
          **Events** to include specific
          entities instead of syncing all your
          documents.
       3. **Regex
          patterns**—Add regular expression
          patterns to include or exclude files by
          **File path**, **File
          name**, **File type**,
          **OneNote section name**, and
          **OneNote page name** instead of
          syncing all your documents. You can add up to
       4.

       ###### Note

       OneNote crawling is available only for OAuth
       2.0, OAuth 2.0 refresh token, and
       SharePoint App Only authentication.

    2. For **Sync mode** choose how you
       want to update your index when your data source
       content changes. When you sync your data source with
       Amazon Kendra for the first time, all content
       is synced by default.
       - **Full sync**—Sync
         all content regardless of the previous sync
         status.
       - **New or modified documents
         sync**—Sync only new or modified
         documents.
       - **New, modified, or deleted
         documents sync**—Sync only new,
         modified, and deleted documents.

    3. In **Sync run schedule**, for
       **Frequency**—Choose how
       often to sync your data source content and update
       your index.
    4. Choose **Next**.

8.  On the **Set field mappings** page, enter
    the following information:
    1. **Default data source
       fields**—Select from the Amazon Kendra generated default data source fields
       that you want to map to your index.
    2. **Add field**—To add custom
       data source fields to create an index field name to
       map to and the field data type.
    3. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

Console: SharePoint Server
**To connect Amazon Kendra to
SharePoint**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **SharePoint connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **SharePoint connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security**
    page, enter the following information:
    1. **Hosting Method**—Choose
       **SharePoint
       Server**.
    2. **Choose SharePoint
       Version**—Choose either
       **SharePoint 2013**,
       **SharePoint 2016**,
       **SharePoint 2019**, and
       **SharePoint (Subscription
       Edition)**.
    3. **Site URLs specific to your
       SharePoint
       repository**—Enter the
       SharePoint host URLs. The format for the
       host URLs you enter is
       `https://yourcompany/sites/mysite`.
       The URL must start with `https` protocol.
       Separate URLs with a new line. You can add up to 100
       URLs.
    4. **Domain**—Enter the
       SharePoint domain. For example, the domain
       in the URL
       `https://yourcompany/sites/mysite`
       is `yourcompany`
    5. **SSL certificate
       location**—Enter the Amazon S3 path to your SSL certificate file.
    6. (Optional) For **Web
       proxy**—Enter the host name (without
       the `http://` or `https://`
       protocol), and the port number used by the host URL
       transport protocol. The numeric value of the port
       number must be between 0 and 65535.
    7. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").

    For SharePoint Server you can choose from
    the following ACL options:

        1. **Email ID with Domain from
         IDP**—User ID is based on email
         IDs with their domains fetched from the underlying
         identity provider (IDP). You provide the IDP
         connection details in your Secrets Manager
         secret as part of
         **Authentication**.
        2. **Email ID with Custom
         Domain**—User ID is based on the
         custom email domain value. For example,
         "`amazon.com`". The email
         domain will be used to construct the email ID for
         access control. You must enter your custom email
         domain.
        3. **Domain\User with
         Domain**—User ID is constructed
         using a Domain\User ID format. You need to provide
         a valid domain name. For example:
         `"sharepoint2019"` to
         construct access control.

    8.  For **Authentication**, choose
        either SharePoint App-Only authentication,
        NTLM authentication, or Kerberos authentication. You
        either choose an existing AWS Secrets Manager
        secret to store your authentication credentials, or
        create a secret.
        1. If using **NTLM
           authentication** or **Kerberos
           authentication**, you secret must include
           a secret name, SharePoint user name and
           password.

        If using **Email ID with Domain from
        IDP**, also enter your:

            * **LDAP Server
             Endpoint**—Endpoint of LDAP
             server, including protocol and port number. For
             example:
             `ldap://example.com:389`.
            * **LDAP Search
             Base**—Search base of LDAP user.
             For example:
             `CN=Users,DC=sharepoint,DC=com`.
            * **LDAP
             username**—Your LDAP user
             name.
            * **LDAP
             Password**—Your LDAP
             password.

        2. If using **SharePoint
           App-Only authentication**, your secret
           must include a secret name, SharePoint
           client ID you generated when you registered App
           Only at Site Level, SharePoint client
           secret generated when your register for App Only
           at Site Level.

        The SharePoint client ID format is
        `ClientID@TenantId`. For
        example,
        `ffa956f3-8f89-44e7-b0e4-49670756342c@888d0b57-69f1-4fb8-957f-e1f0bedf82fe`.

        **Note:**
        Because client IDs and client secrets are
        generated for single sites only when you register
        SharePoint Server for App Only
        authentication, only one site URL is supported for
        SharePoint App Only authentication.

        If using **Email ID with Domain from
        IDP**, also enter your:

            * **LDAP Server
             Endpoint**—Endpoint of LDAP
             server, including protocol and port number. For
             example:
             `ldap://example.com:389`.
            * **LDAP Search
             Base**—Search base of LDAP user.
             For example:
             `CN=Users,DC=sharepoint,DC=com`.
            * **LDAP
             username**—Your LDAP user
             name.
            * **LDAP
             Password**—Your LDAP
             password.

    9.  **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
        so, you must add **Subnets** and **VPC security groups**.
    10. **Identity crawler**—Specify whether to turn on
        Amazon Kendra’s identity crawler. The identity crawler uses the access control list
        (ACL) information for your documents to filter search results based on the user or their
        group access to documents. If you have an ACL for your documents and choose to use your ACL,
        you can then also choose to turn on Amazon Kendra’s identity crawler to configure
        [user
        context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
        all documents can be publicly searched. If you want to use access control for your documents
        and identity crawler is turned off, you can alternatively use the
        [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
        API to upload user and group access information for user context filtering.

    You can also choose to crawl local group mapping
    or Azure Active Directory group mapping.

    ###### Note

    AD Group mapping crawling is available only
    SharePoint App Only authentication. 11. **IAM role**—Choose an existing IAM
    role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 12. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. In **Sync scope**, choose from
       the following options :
       1. **Select
          entities**—Choose the entities you
          want to crawl. You can select to crawl
          **All** entities or any
          combination of **Files**,
          **Attachments**,
          **Links**
          **Pages**,
          **Events**, and **List
          Data**.
       2. In **Additional
          configuration**, for **Entity
          regex patterns**—Add regular
          expression patterns for
          **Links**,
          **Pages**, and
          **Events** to include specific
          entities instead of syncing all your
          documents.
       3. **Regex
          patterns**—Add regular expression
          patterns to include or exclude files by
          **File path**
          **File name**
          **File type**, **OneNote
          section name**, and **OneNote
          page name** instead of syncing all your
          documents. You can add up to 100.

       ###### Note

       OneNote crawling is available only for
       SharePoint App Only authentication.

    2. **Sync mode**—Choose how
       you want to update your index when your data source
       content changes. When you sync your data source with
       Amazon Kendra for the first time, all content
       is crawled and indexed by default. You must run a
       full sync of your data if your initial sync failed,
       even if you don't choose full sync as your sync mode
       option.
       - Full sync: Freshly index all content,
         replacing existing content each time your data
         source syncs with your index.
       - New, modified sync: Index only new and
         modified content each time your data source syncs
         with your index. Amazon Kendra can use your
         data source's mechanism for tracking content
         changes and index content that changed since the
         last sync.
       - New, modified, deleted sync: Index only new,
         modified, and deleted content each time your data
         source syncs with your index. Amazon Kendra
         can use your data source's mechanism for tracking
         content changes and index content that changed
         since the last sync.

    3. In **Sync run schedule**, for
       **Frequency**—Choose how
       often to sync your data source content and update
       your index.
    4. Choose **Next**.

8.  On the **Set field mappings** page, enter
    the following information:
    1. **Default data source
       fields**—Select from the Amazon Kendra generated default data source fields
       that you want to map to your index.
    2. **Add field**—To add custom
       data source fields to create an index field name to
       map to and the field data type.
    3. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
SharePoint**

You must specify a JSON of the [data source
schema](ds-schemas.md "ds-schemas.md") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the
following information:

- **Data
  source**—Specify the data source type as
  `SHAREPOINTV2` when you
  use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Repository Endpoint
  Metadata**—Specify the
  `tenantID`
  `domain` and `siteUrls` of your
  SharePoint instance.
- **Sync mode**—Specify
  how Amazon Kendra should update your index when your
  data source content changes. When you sync your data source
  with Amazon Kendra for the first time, all content is
  crawled and indexed by default. You must run a full sync of
  your data if your initial sync failed, even if you don't
  choose full sync as your sync mode option. You can choose
  between:
  - `FORCED_FULL_CRAWL` to freshly index
    all content, replacing existing content each time
    your data source syncs with your index.
  - `FULL_CRAWL` to index only new,
    modified, and deleted content each time your data
    source syncs with your index. Amazon Kendra can
    use your data source’s mechanism for tracking
    content changes and index content that changed since
    the last sync.
  - `CHANGE_LOG` to index only new and
    modified content each time your data source syncs
    with your index. Amazon Kendra can use your
    data source’s mechanism for tracking content changes
    and index content that changed since the last
    sync.

- **Identity crawler**—Specify whether to turn on
  Amazon Kendra’s identity crawler. The identity crawler uses the access control list
  (ACL) information for your documents to filter search results based on the user or their
  group access to documents. If you have an ACL for your documents and choose to use your ACL,
  you can then also choose to turn on Amazon Kendra’s identity crawler to configure
  [user
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
  all documents can be publicly searched. If you want to use access control for your documents
  and identity crawler is turned off, you can alternatively use the
  [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
  API to upload user and group access information for user context filtering.

###### Note

Identity crawler is available only when you set
`crawlAcl` to `true`.

- **Repository Additional
  Properties**—Specify the:
  - (For Azure AD) `s3bucketName` and
    `s3certificateName` you use to store
    your Azure AD self-signed X.509 certificate.
  - Authentication type (`auth_Type`) you
    use, whether `OAuth2`,
    `OAuth2App`,
    `OAuth2Certificate`,
    `Basic`,
    `OAuth2_RefreshToken`, `NTLM`,
    and `Kerberos`.
  - Version (`version`) you use, whether
    `Server` or `Online`. If you
    use `Server` you can futher specify the
    `onPremVersion` as `2013`,
    `2016`, `2019`, or
    `SubscriptionEdition`.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource Name
  (ARN) of a Secrets Manager secret that contains the
  authentication credentials you created in your
  SharePoint account.

If you use SharePoint Online, you can choose
between Basic, OAuth 2.0, Azure AD App-only and
SharePoint App Only authentication. The following
are the minimum JSON structure that must be in your secret
for each authentication option:

    + **Basic
     authentication**



    ```
    {
        "userName": "`SharePoint account user name`",
        "password": "`SharePoint account password`"
    }
    ```
    + **OAuth 2.0
     authentication**



    ```
    {
        "clientId": "`client id generated when registering SharePoint with Azure AD`",
        "clientSecret": "`client secret generated when registering SharePoint with Azure AD`",
        "userName": "`SharePoint account user name`",
        "password": "`SharePoint account password`"
    }
    ```
    + **Azure AD App-Only
     authentication**



    ```
    {
        "clientId": "`client id generated when registering SharePoint with Azure AD`",
        "privateKey": "`private key to authorize connection with Azure AD`"
    }
    ```
    + **SharePoint App-Only
     authentication**



    ```
    {
        "clientId": "`client id generated when registering SharePoint for App Only at Tenant Level`",
        "clientSecret": "`client secret generated when registering SharePoint for App Only at Tenant Level`",
        "adClientId": "`client id generated while registering SharePoint with Azure AD`",
        "adClientSecret": "`client secret generated while registering SharePoint with Azure AD`"
    }
    ```
    + **OAuth 2.0 refresh token
     authentication**



    ```
    {
        "clientId": "`client id generated when registering SharePoint with Azure AD`",
        "clientSecret": "`client secret generated when registering SharePoint with Azure AD`",
        "refreshToken": "`refresh token generated to connect to SharePoint`"
    }
    ```

If you use SharePoint Server, you can choose
between SharePoint App-Only authentication, NTLM
authentication, and Kerberos authentication. The following
are the minimum JSON structure that must be in your secret
for each authentication option:

    + **SharePoint App-Only
     authentication**



    ```
    {
        "siteUrlsHash": "`Hash representation of SharePoint site URLs`",
        "clientId": "`client id generated when registering SharePoint for App Only at Site Level`",
        "clientSecret": "`client secret generated when registering SharePoint for App Only at Site Level`"
    }
    ```
    + **SharePoint App-Only
     authentication with domain from IDP
     authorization**



    ```
    {
        "siteUrlsHash": "`Hash representation of SharePoint site URLs`",
        "clientId": "`client id generated when registering SharePoint for App Only at Site Level`",
        "clientSecret": "`client secret generated when registering SharePoint for App Only at Site Level`",
        "ldapUrl": "`LDAP Account url eg. ldap://example.com:389`",
        "baseDn": "`LDAP Account base dn eg. CN=Users,DC=sharepoint,DC=com`",
        "ldapUser": "`LDAP account user name`",
        "ldapPassword": "`LDAP account password`"
    }
    ```
    + **(Server only) NTLM or
     Kerberos authentication**



    ```
    {
        "siteUrlsHash": "`Hash representation of SharePoint site URLs`",
        "userName": "`SharePoint account user name`",
        "password": "`SharePoint account password`"
    }
    ```
    + **(Server only) NTLM or
     Kerberos authentication with domain from IDP
     authorization**



    ```
    {
        "siteUrlsHash": "`Hash representation of SharePoint site URLs`",
        "userName": "`SharePoint account user name`",
        "password": "`SharePoint account password`",
        "ldapUrl": "`ldap://example.com:389`",
        "baseDn": "`CN=Users,DC=sharepoint,DC=com`",
        "ldapUser": "`LDAP account user name`",
        "ldapPassword": "`LDAP account password`"
    }
    ```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the SharePoint connector and Amazon Kendra.
  For more information, see [IAM roles for SharePoint
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion
  filters**—You can specify whether to
  include or exclude certain files, OneNotes, and other
  content.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field mappings**—Choose to map your SharePoint
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [SharePoint template schema](ds-schemas.md#ds-schema-sharepoint "ds-schemas.md#ds-schema-sharepoint").

## Notes

- The connector supports custom field mappings only for the
  **Files** entity.
- For all SharePoint Server versions, the ACL token must be in lower
  case. For **Email with Domain from IDP** and
  **Email ID with Custom Domain** ACL, for example:
  `user@sharepoint2019.com`. For
  **Domain\User with Domain** ACL, for example:
  `sharepoint2013\user`.
- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to SharePoint API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
- The connector does not support change log mode/**New or modified
  content sync** for SharePoint 2013.
- If an entity name has a `%` character in its name, the
  connector will skip these files due to API limitations.
- OneNote can only be crawled by the connector using a Tenant ID, and with
  OAuth 2.0, OAuth 2.0 refresh token, or SharePoint App Only
  authentication activated for SharePoint Online.
- The connector crawls the first section of a OneNote document using its
  default name only, even if the document is renamed.
- The connector crawls links in SharePoint 2019, SharePoint
  Online, and Subscription Edition, only if **Pages** and
  **Files** are selected as entities to be crawled in
  addition to **Links**.
- The connector crawls links in SharePoint 2013 and
  SharePoint 2016 if **Links** is selected as an
  entity to be crawled.
- The connector crawls list attachments and comments only when
  **List Data** is also selected as an entity to be
  crawled.
- The connector crawls event attachments only when
  **Events** is also selected as an entity to be
  crawled.
- For SharePoint Online version, the ACL token will be in lower
  case. For example, if **User principal name** is
  `MaryMajor@domain.com` in Azure portal, the ACL
  token in the SharePoint Connector will be
  `marymajor@domain.com`.
- In **Identity Crawler** for SharePoint Online and
  Server, if you want to crawl nested groups, you have to activate Local as
  well as AD Group Crawling.
- If you're using SharePoint Online, and the User Principal Name in
  your Azure Portal is a combination of upper case and lower case, the
  SharePoint API internally converts it to lower case. Because of
  this, the Amazon Kendra SharePoint connector sets ACL in lower
  case.
