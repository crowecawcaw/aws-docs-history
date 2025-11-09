# Prerequisites for connecting Amazon Q Business to SharePoint (Online)

The following page outlines the prerequisites you need to complete before connecting
SharePoint (Online) to Amazon Q, based on the authentication mode of your
choice.

###### Note

For more information on connecting SharePoint (Online) to Amazon Q Business,
see [Connect Amazon Q Business to Microsoft SharePoint Online
using least privilege access controls](https://aws.amazon.com/blogs/machine-learning/connect-amazon-q-business-to-microsoft-sharepoint-online-using-least-privilege-access-controls/ "https://aws.amazon.com/blogs/machine-learning/connect-amazon-q-business-to-microsoft-sharepoint-online-using-least-privilege-access-controls/") and [Find answers accurately and quickly using Amazon Q Business with the
SharePoint Online connector](https://aws.amazon.com/blogs/machine-learning/find-answers-accurately-and-quickly-using-amazon-q-business-with-the-sharepoint-online-connector/ "https://aws.amazon.com/blogs/machine-learning/find-answers-accurately-and-quickly-using-amazon-q-business-with-the-sharepoint-online-connector/") in the _AWS Machine Learning
Blog_.

###### Topics

- [Prerequisites for using
  Microsoft Entra ID (formerly Azure AD) App-Only authentication](#sharepoint-cloud-prereqs-azure-app-only "#sharepoint-cloud-prereqs-azure-app-only")
- [Prerequisites for using OAuth 2.0
  authentication](#sharepoint-cloud-prereqs-oauth "#sharepoint-cloud-prereqs-oauth")
- [Prerequisites for
  using SharePoint App-Only authentication](#sharepoint-cloud-prereqs-sharepoint-app-only "#sharepoint-cloud-prereqs-sharepoint-app-only")
- [Prerequisites for using basic
  authentication](#sharepoint-cloud-prereqs-basic "#sharepoint-cloud-prereqs-basic")

## Prerequisites for using

Microsoft Entra ID (formerly Azure AD) App-Only authentication

**If you're using Microsoft Entra ID (formerly Azure AD) App-Only authentication, make sure
you've completed the following steps in SharePoint (Online):**

- Copied your SharePoint (Online) instance URLs. The format for the host URL
  you enter is
  `https://yourdomain.sharepoint.com/sites/mysite`
  or `https://yourcompany.sharepoint.com`. Your URL
  must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint (Online) instance URL.
- Copied the tenant ID of your Microsoft SharePoint (Online) instance. For
  details on how to find your tenant ID, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id") on the Microsoft
  website.
- Generated an X.509 certificate. For more information on how to create and
  configure an X.509 certificate, see [Granting access via Microsoft Entra ID (formerly Azure AD) App-Only](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread "https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azuread") and [New-PnPAzureCertificate](https://pnp.github.io/powershell/cmdlets/New-PnPAzureCertificate.html "https://pnp.github.io/powershell/cmdlets/New-PnPAzureCertificate.html") in _Microsoft
  developer documentation_.
- After generating the X.509 certificate, upload your .CRT file (the public
  certificate) to an Amazon S3 bucket. Note the file path to a X.509 certificate
  you have created and stored in an Amazon S3 bucket. (Ex.
  `s3://bucket-name/path/to/certificate.crt`). Ensure that your
  Amazon Q Business IAM role has permissions to read from this
  Amazon S3 bucket.
- Noted the private key and the Client ID you generated after
  SharePoint (Online) Azure App registration.
- Configured a Sharepoint (Online) Azure App using one of the two options
  below and noted its Client ID and Client secret.

###### Note

If you want to crawl specific sites, you can choose to restrict
permissions to specific sites rather than all sites available in the
domain. To do this, use the Sites.Selected (Application) permission.
With this API permission, you need to set access permission on every
site explicitly through the Microsoft Graph API. For more information,
see [Microsoft's blog on Sites.Selected permissions](https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476 "https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/develop-applications-that-use-sites-selected-permissions-for-spo/ba-p/3790476").

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint (Online) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

_Microsoft Entra ID (formerly Azure AD) App-Only Option 1: Global Read Access_

If you anticipate that you will be indexing several Sharepoint sites and would
like to simplify your setup process, you can take the following steps to provide the
Q Business Sharepoint connector global access. Otherwise, skip to section 2
below.

1.  Create a Sharepoint client app to which we will assign the permissions
    needed by your Q Business connector. To register the app:
    1.  Log in to the Azure Portal with your Microsoft account.
    2.  1. Provide the name for your application. In the example we
           are using the name TargetApp. The Amazon Q Business
           application uses TargetApp to connect to the SharePoint
           Online site to crawl and index the data.
        2. Choose "Accounts" in the organizational directory. (Tenant
           name only - Single tenant).
        3. Choose "Register".
        4. Note down the application (client ID and the directory
           (tenant) on the Overview page, as you'll need them when
           prompted for "TargetApp-ClientId" and "TenantId".
        5. Navigate to "Manage > API Permissions" in the navigation
           pane
        6. Navigate to "Add a permission > Sharepoint > Application
           permissions" to allow the application to read data in your
           organization's directory regarding the signed-in
           user.
        7. Search "AllSites.Read".
        8. Choose "Add permissions".
        9. Navigate to "Add a permission > Microsoft Graph >
           Application permissions"
        10. Search and add the following permissions:
            - "Notes.Read.All"
            - "Sites.Read.All"
            - "Sites.FullControl.All (Application)" (required only
              if you intend to enable ACLs)
            - "Sites.Read.All (Application)"(required only if
              you intend to enable ACLs)
            - "Sites.FullControl.All" (required only if you
              intend to enable ACLs)
            - "GroupMember.Read.All" (required only if you
              intend to enable ACLs)
            - "User.Read.All" (required only if you intend to
              enable ACLs)

        11. Navigate to "Remove permission"
        12. Remove the original "User.Read - Delegated"
            permission
        13. Choose "Grant admin consent" for the default
            directory
        14. Save the client ID generated from this app for when you
            configure the Sharepoint connector in the Q Business console
            or API

        The following tables summarize all the permissions your
        application should have.

            * If you're not using ACL, your application should
             have the permission:

        |                                                                         |                                                                      |
        | ----------------------------------------------------------------------- | -------------------------------------------------------------------- |
        | **Microsoft<br>Graph**                                                  | **Sharepoint**                                                       |
        | Notes.Read.All (Application) – Read all<br>OneNote notebooks            | AllSites.Read (Delegated)<br>• Read items in<br>all site collections |
        | Sites.Read.All (Application)<br>• Read items in<br>all site collections |                                                                      |

        ###### Note

        Read.All and Sites.Read.All are required only if you
        want to crawl OneNote Documents.

            * If you're using ACL, your application should have
             the following permissions:

        |                                                                                       |                                                                   |
        | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
        | Microsoft Graph                                                                       | Sharepoint                                                        |
        | GroupMember.Read.All (Application) –<br>Read all group memberships                    | AllSites.Read (Delegated) – Read<br>items in all site collections |
        | Notes.Read.All (Application) – Read<br>all OneNote notebooks                          |                                                                   |
        | Sites.FullControl.All (Application) –<br>Have full control of all site<br>collections |                                                                   |
        | Sites.Read.All (Application) – Read<br>items in all site collections                  |                                                                   |
        | User.Read.All (Application) – Read<br>all users' full profiles                        |                                                                   |

2.  Create a client secret for your Sharepoint App:
    1. Within your client App navigate to "Clients and secrets > Client
       secrets"
    2. Click on create a new secret.

3.  Generate a new Certificate to be shared between Q Business SharePoint
    Connector and Microsoft Entra ID (formerly Azure AD) App:
    1. Use the example command below to generate your own x509
       certificate.
    2. Run the following command:`openssl req -x509 -newkey rsa:2048
-noenc -sha1 -keyout /tmp/private.key -out /tmp/sharepoint.crt
-nodes -set_serial 1 -days 365 -subj
"/CN=amazon/emailAddress=example@aws.com/C=US/ST=Texas/L=Dallas/O=amazon/OU=amazon`
    3. Save the generated private key located in /tmp/private.key for
       later when you configure the Q Business Sharepoint connector via the
       Q Business console or API.

_Microsoft Entra ID (formerly Azure AD) App-Only Option 2: Read Access for only Selected
Sites_

If you anticipate that you will be indexing a manageable number of Sharepoint
sites and would prefer to limit the permissions of the Q Business connector to just
the Sharepoint sites you intend to index, you can take the following steps:

1.  Create a Sharepoint client app: Create a Sharepoint client app to which we
    will assign the permissions needed by your Q Business connector. To register
    the app:
    1.  Log in to the Azure Portal with your Microsoft account.
    2.  Choose "New Registration":
        1. Provide the name for your application. In the example we
           are using the name TargetApp. The Amazon Q Business
           application uses TargetApp to connect to the SharePoint
           Online site to crawl and index the data.
        2. Choose "Accounts" in the organizational directory. (Tenant
           name only - Single tenant).
        3. Choose "Register".
        4. Note down the application (client ID and the directory
           (tenant) on the Overview page, as you'll need them when
           prompted for "TargetApp-ClientId" and "TenantId".
        5. Navigate to "Manage > API Permissions" in the navigation
           pane
        6. Navigate to "Add a permission > Sharepoint > Application
           permissions" to allow the application to read data in your
           organization's directory regarding the signed-in
           user.
        7. Search "Sites.Selected".
        8. Choose "Add permissions".
        9. Navigate to "Add a permission > Microsoft Graph >
           Application permissions"
        10. Search and add the following permissions:
            - "Notes.Read.All"
            - "Sites.Selected"
            - "GroupMember.Read.All" (required only if you
              intend to enable ACLs)
            - "User.Read.All" (required only if you intend to
              enable ACLs)

        11. Navigate to "Remove permission"
        12. Remove the original "User.Read - Delegated"
            permission
        13. Choose "Grant admin consent" for the default
            directory
        14. Save the client ID generated from this app for when you
            configure the Sharepoint connector in the Q Business console
            or API

        The following tables summarize all the permissions your
        application should have.

            * If you're not using ACL, your application should
             have the permissions:




            |  |  |
            | --- | --- |
            | **Microsoft<br>Graph** | **Sharepoint** |
            | Notes.Read.All (Application) – Read all<br>OneNote notebooks | AllSites.Read (Delegated)<br>• Read items in<br>all site collections |
            | Site.Read.All (Application)<br>• Read items in<br>all site collections |  |


            ###### Note

            Read.All and Sites.Read.All are required only
             if you want to crawl OneNote Documents.




            	+ If you're using ACL, your application should
            	 have the following permissions:


            |  |  |
            | --- | --- |
            | Microsoft Graph | Sharepoint |
            | GroupMember.Read.All (Application) –<br>Read all group memberships | AllSites.Read (Delegated) – Read<br>items in all site collections |
            | Notes.Read.All (Application) – Read<br>all OneNote notebooks |  |
            | Sites.FullControl.All (Application) –<br>Have full control of all site<br>collections |  |
            | Sites.Read.All (Application) – Read<br>items in all site collections |  |
            | User.Read.All (Application) – Read<br>all users' full profiles |  |
            | Sites.Selected<br>• Have control of selected<br>sites |  |

2.  Create a client secret for your Sharepoint App:
    1. Within your client App navigate to "Clients and secrets > Client
       secrets"
    2. Click on create a new secret.

3.  Generate a new Certificate to be shared between Q Business SharePoint
    Connector and Microsoft Entra ID (formerly Azure AD) App:
    1. Run the following command: `openssl req -x509 -newkey
rsa:2048 -noenc -sha1 -keyout /tmp/private.key -out
/tmp/sharepoint.crt -nodes -set_serial 1 -days 365 -subj
"/CN=amazon/emailAddress=example@aws.com/C=US/ST=Texas/L=Dallas/O=amazon/OU=amazon"`
    2. Save the generated private key located in /tmp/private.key for
       later when you configure the Q Business Sharepoint connector via the
       Q Business console or API.
    3. Upload the generated certificate located in /tmp/sharepoint.crt to
       an S3 bucket so you can use it later when you configure the Q
       Business Sharepoint connector via the Q Business console or API. You
       will also need this certificate for the next step.

4.  Update your Sharepoint Client App’s Certificate:
    1. Navigate to the Sharepoint client app you created in step 1.
    2. Navigate to “Certificates and secrets > Certificates > Upload
       certificate” and upload the certificate (.crt file) you generated in
       step 4.

5.  Create a Sharepoint admin app: This app will be used to provide the
    necessary site read permissions for the client OAuth App you created in the
    previous step. You can delete this admin app after you have completed all
    the steps. To register the app:
    1. Log in to the Azure Portal with your Microsoft account.
    2. Choose “New Registration”:
       1. Provide the name for your application.
       2. Choose "Accounts" in the organizational directory. (Tenant
          name only - Single tenant).
       3. Choose "Register".
       4. Locate your app ID, app secret, and tenant ID for your
          admin app and save them for the next step.
       5. Navigate to "Manage > API Permissions" in the navigation
          pane
       6. Navigate to "Add a permission > Sharepoint > Application
          permissions" to allow the application to read data in your
          organization's directory regarding the signed-in
          user.
       7. Search "Sites.FullControl.All".
       8. Choose "Add permissions".
       9. Navigate to "Add a permission > Microsoft Graph >
          Application permissions"
       10. Search "Sites.Read.All".
       11. Choose "Add permissions".

6.  Generate an access token for your Sharepoint admin app: Now use the
    following code snippet to generate an access token for your app, but replace
    adminAppID, adminAppSecret, and tenantID with the values you saved from step
7.  1. ```
       adminAppId=$1
       adminAppSecret=$2
       tenantId=$3
       ```

    tokenResponse=$(curl -s --location \
	"https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode "grant_type=client_credentials" \
    --data-urlencode "client_id=$adminAppId" \
	--data-urlencode "client_secret=$adminAppSecret" \
    --data-urlencode "scope=offline_access https://graph.microsoft.com/.default")

    adminAppToken=$(echo $tokenResponse | jq -r '.access_token')
    echo $adminAppToken

    ```

    ```

8.  Obtain a Site ID for each of your Sharepoint sites: Repeat the following
    steps for each of the Sharepoint sites you want your Q Business connector to
    crawl:
    1. Visit
       `https://{yourcompany}.sharepoint.com/sites/{SiteName}`in
       a browser. Enter the appropriate login credentials if needed.
       Validate that you are able to see your SharePoint site
    2. Now append /\_api/site/id at the end of {SiteName}. You should see
       a response something similar to below containing your site id
       (96a47524-4b21-446f-bf96-96d2f6fe4aa7)

    ```
    <d:Id m:type="Edm.Guid" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:georss="http://www.georss.org/georss" xmlns:gml="http://www.opengis.net/gml" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">96a47524-4b21-446f-bf96-96d2f6fe4aa7</d:Id>
    ```

9.  Grant your Sharepoint client app permissions to your selected sites: Now
    that you have created your Sharepoint admin app, Sharepoint client app, and
    have a list of site ids, you are ready to grant your client app the
    necessary permissions to access these sites. Repeat the following steps for
    each of the site ids you obtained from step 4.
    1. Modify the code snippet below to provide the following:
       1. clientAppId: The Application (client) ID from step
       1.
       1. clientAppName: The display name of your Sharepoint client
          app from step 1.
       1. adminToken: The access token you generated in step
       1.
       1. siteId: One of the site ids you obtained from step
       1.

    2. Run the following command:

    ```
    clientAppId=$1
    clientAppName=$2
    clientAppId=$1
    clientAppName=$2
    adminToken=$3
    siteToGivePermissionTo=$4

    grantPermissionResponse=$(curl -s --location "https://graph.microsoft.com/v1.0/sites/$siteToGivePermissionTo/permissions" \
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer $adminToken" \
        --data '{
             "roles": ["fullcontrol"],
             "grantedToIdentities": [{
                "application": {
                  "id": "'${clientAppId}'",
                  "displayName": "'${clientAppName}'"
                }
              }]
            }')

    echo $grantPermissionResponse
    ```

    3. If the command was successful, you'll see a response as
       follows:

    ```
    {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('awsplatodemo.sharepoint.com%2C96a47524-4b21-446f-bf96-96d2f6fe4aa7')/permissions/$entity",
      "id": "aTowaS50fG1zLnNwLmV4dHxjMDY5YjhlMi03NGFhLTQzZTQtODljYi1kNmZkMzU4ZmVjZThAZjIwNDQ2OTItZGMwOS00MjZlLWFlMGQtNGFlZDljMTI3ODA2",
      "roles": [
        "fullcontrol"
      ],
      "grantedToIdentitiesV2": [
        {
          "application": {
            "displayName": "demo-client-app",
            "id": "c069b8e2-74aa-43e4-89cb-d6fd358fece8"
          }
        }
      ],
      "grantedToIdentities": [
        {
          "application": {
            "displayName": "demo-client-app",
            "id": "c069b8e2-74aa-43e4-89cb-d6fd358fece8"
          }
        }
      ]
    }
    ```

## Prerequisites for using OAuth 2.0

authentication

**If you're using OAuth 2.0 authentication, make sure you've
completed the following steps in SharePoint (Online):**

- Copied your SharePoint (Online) instance URLs. The format for the host URL
  you enter is
  `https://yourdomain.sharepoint.com/sites/mysite`
  or `https://yourcompany.sharepoint.com`. Your URL
  must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint (Online) instance URL.
- Copied the tenant ID of your Microsoft SharePoint (Online) instance. For
  details on how to find your tenant ID, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id") on the Microsoft
  website.
- Noted the username and password that you use to connect to
  SharePoint (Online).
- Noted the Client ID and Client secret generated after SharePoint (Online)
  Azure App registration.
- Deactivate multi-factor authentication (MFA) in your SharePoint account,
  so that Amazon Q is not blocked from crawling your SharePoint
  content.
- Configured a Sharepoint (Online) Azure App using one of the two options
  below and noted its Client ID and Client secret.

_OAuth2.0 Option 1: Global Read Access_

If you anticipate that you will be indexing several Sharepoint sites and would
like to simplify your setup process, you can take the following steps to provide the
Q Business Sharepoint connector global access. Otherwise, skip to section 2
below.

To register the app:

1.  Log in to the Azure Portal with your Microsoft account.
2.  Choose "New Registration":
    1. Provide the name for your application. In the example we are using
       the name TargetApp. The Amazon Q Business application uses
       TargetApp to connect to the SharePoint Online site to crawl and
       index the data.
    2. Choose "Accounts" in the organizational directory. (Tenant name
       only - Single tenant).
    3. Choose "Register".
    4. Note down the application (client ID and the directory (tenant) on
       the Overview page, as you'll need them when prompted for
       "TargetApp-ClientId" and "TenantId".
    5. Navigate to "Manage > API Permissions" in the navigation
       pane
    6. Navigate to "Add a permission > Sharepoint > Application
       permissions" to allow the application to read data in your
       organization's directory regarding the signed-in user.
    7. Search "AllSites.Read".
    8. Choose "Add permissions".
    9. Navigate to "Add a permission > Microsoft Graph > Application
       permissions"
    10. Search and add the following permissions:
        - "Notes.Read.All"
        - "Sites.Read.All"
        - "Sites.FullControl.All" (required only if you intend to
          enable ACLs)
        - "GroupMember.Read.All" (required only if you intend to
          enable ACLs)
        - "User.Read.All" (required only if you intend to enable
          ACLs)

    11. Navigate to "Remove permission".
    12. Remove the original "User.Read - Delegated" permission.
    13. Choose "Grant admin consent" for the default directory.
    14. Save the client ID generated from this app for when you configure
        the Sharepoint connector in the Q Business console or API.

    The following tables summarize all the permissions your
    application should have.

        * If you're not using ACL, your application should have the
         permissions:




        |  |  |
        | --- | --- |
        | **Microsoft<br>Graph** | **Sharepoint** |
        | Notes.Read.All (Application) – Read<br>all OneNote notebooks | AllSites.Read (Delegated)<br>• Read<br>items in all site collections |
        | Site.Read.All (Application)<br>• Read<br>items in all site collections |  |


        ###### Note

        Note.Read.All and Sites.Read.All are required only if
         you want to crawl OneNote Documents.
        * If you're using ACL, your application should have the
         following permissions:




        |  |  |
        | --- | --- |
        | **Microsoft<br>Graph** | **Sharepoint** |
        | GroupMember.Read.All (Application) –<br>Read all group memberships | AllSites.Read (Delegated) – Read<br>items in all site collections |
        | Notes.Read.All (Application) – Read<br>all OneNote notebooks |  |
        | Sites.FullControl.All (Application) –<br>Have full control of all site<br>collections |  |
        | Sites.Read.All (Application) – Read<br>items in all site collections |  |
        | User.Read.All (Application) – Read<br>all users' full profiles |  |


        ###### Note

        GroupMember.Read.All and User.Read.All are required
         only if Identity crawler is activated.

3.  Create a client secret for your Sharepoint App:
    1. Within your client App navigate to "Clients and secrets > Client
       secrets"
    2. Click on create a new secret.

_OAuth2.0 Option 2: Read Access Only for Selected Sites_

For organizations planning to index a manageable number of Sharepoint sites with
limited permissions, the following steps provide the necessary setup:

1. Create a Sharepoint client app for OAuth: Now create a Sharepoint client
   OAuth app to which we will assign the permissions needed by your Q Business
   connector. To register the app:
   1. Log in to the Azure Portal with your Microsoft account.
   2. Choose "New Registration":
      1. Provide the name for your application. In the example we
         are using the name TargetApp. The Amazon Q Business
         application uses TargetApp to connect to the SharePoint
         Online site to crawl and index the data.
      2. Choose "Accounts" in the organizational directory. (Tenant
         name only - Single tenant).
      3. Choose "Register".
      4. Note down the application (client ID and the directory
         (tenant) on the Overview page, as you'll need them when
         prompted for "TargetApp-ClientId" and "TenantId".
      5. Navigate to "Manage > API Permissions" in the navigation
         pane
      6. Navigate to "Add a permission > Sharepoint > Application
         permissions" to allow the application to read data in your
         organization's directory regarding the signed-in
         user.
      7. Search "Sites.Selected".
      8. Choose "Add permissions".
      9. Navigate to "Add a permission > Microsoft Graph >
         Application permissions"
      10. Search and add the following permissions:
          - "Notes.Read.All"
          - "Sites.Selected"
          - "GroupMember.Read.All" (required only if you
            intend to enable ACLs)
          - "User.Read.All" (required only if you intend to
            enable ACLs)

      11. Navigate to "Remove permission"
      12. Remove the original "User.Read - Delegated"
          permission
      13. Choose "Grant admin consent" for the default
          directory
      14. Save the client ID generated from this app for when you
          configure the Sharepoint connector in the Q Business console
          or APIThe following tables summarize all the permissions your
          application should have.
      - If you're not using ACL, your application should have the
        permissions:

      |                                                                              |                                                                              |
      | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
      | **Microsoft<br>Graph**                                                       | **Sharepoint**                                                               |
      | Notes.Read.All (Application) – Read<br>all OneNote notebooks                 | Sites.Selected (Application)<br>• Read<br>items in selected site collections |
      | Sites.Selected (Application)<br>• Read<br>items in selected site collections |                                                                              |

      ###### Note

      Note.Read.All and Sites.Read.All are required only if
      you want to crawl OneNote Documents.
      - If you're using ACL, your application should have the
        following permissions:

      |                                                                                       |                                                                   |
      | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
      | Microsoft Graph                                                                       | Sharepoint                                                        |
      | GroupMember.Read.All (Application) –<br>Read all group memberships                    | AllSites.Read (Delegated) – Read<br>items in all site collections |
      | Notes.Read.All (Application) – Read<br>all OneNote notebooks                          |                                                                   |
      | Sites.FullControl.All (Application) –<br>Have full control of all site<br>collections |                                                                   |
      | Sites.Read.All (Application) – Read<br>items in all site collections                  |                                                                   |
      | User.Read.All (Application) – Read<br>all users' full profiles                        |                                                                   |

      ###### Note

      Note. GroupMember.Read.All and User.Read.All are
      required only if Identity crawler is activated.

2. Create a client secret for your Sharepoint App:
   1. Within your client App navigate to "Clients and secrets > Client
      secrets"
   2. Click on create a new secret.

3. Create a Sharepoint admin app: This app will be used to provide the
   necessary site read permissions for the client OAuth App you created in the
   previous step. You can delete this admin app after you have completed all
   the steps. To register the app:
   1. Log in to the Azure Portal with your Microsoft account.
   2. Choose "New Registration":
      1. Provide the name for your application.
      2. Choose "Accounts" in the organizational directory. (Tenant
         name only - Single tenant).
      3. Choose "Register".
      4. Locate your app ID, app secret, and tenant ID for your
         admin app and save them for the next step.
      5. Navigate to "Manage > API Permissions" in the navigation
         pane
      6. Navigate to "Add a permission > Sharepoint > Application
         permissions" to allow the application to read data in your
         organization's directory regarding the signed-in
         user.
      7. Search "Sites.FullControl.All".
      8. Choose "Add permissions".
      9. Navigate to "Add a permission > Microsoft Graph >
         Application permissions"
      10. Search "Sites.Read.All".
      11. Choose "Add permissions".

4. Generate an access token for your Sharepoint admin app: Now use the
   following code snippet to generate an access token for your app, but replace
   adminAppID, adminAppSecret, and tenantID with the values you saved from step
5. 1. ```
      adminAppId=$1
      adminAppSecret=$2
      tenantId=$3
      ```

   tokenResponse=$(curl -s --location \
	"https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode "grant_type=client_credentials" \
   --data-urlencode "client_id=$adminAppId" \ 
	--data-urlencode "client_secret=$adminAppSecret" \
   --data-urlencode "scope=offline_access https://graph.microsoft.com/.default")

   adminAppToken=$(echo $tokenResponse | jq -r '.access_token')
   echo $adminAppToken

   ```

   ```

6. Obtain a Site ID for each of your Sharepoint sites: Repeat the following
   steps for each of the Sharepoint sites you want your Q Business connector to
   crawl:
   1. Visit https://{yourcompany}.sharepoint.com/sites/{SiteName} in a
      browser. Enter the appropriate login credentials if needed. Validate
      that you are able to see your SharePoint site
   2. Now append /\_api/site/id at the end of {SiteName}. You should see
      a response something similar to below containing your site id
      ([IP\_ADDRESS]a7)

   ```
   <d:Id m:type="Edm.Guid" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:georss="http://www.georss.org/georss" xmlns:gml="http://www.opengis.net/gml" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">[IP_ADDRESS]a7</d:Id>
   ```

7. Grant your Sharepoint client app permissions to your selected sites: Now
   that you have created your Sharepoint admin app, Sharepoint client app, and
   have a list of site ids, you are ready to grant your client app the
   necessary permissions to access these sites. Repeat the following steps for
   each of the site ids you obtained from step 4.
   1. Modify the code snippet below to provide the following:
      1. clientAppId: The Application (client) ID from step
         1
      2. clientAppName: The display name of your Sharepoint client
         app from step 1
      3. adminToken: The adminAppToken you generated in step
         3
      4. siteId: One of the site ids you obtained from step
      5.

   2. ```
      clientAppId=$1
      clientAppName=$2
      adminToken=$3
      siteToGivePermissionTo=$4
      ```

   grantPermissionResponse=$(curl -s --location "https://graph.microsoft.com/v1.0/sites/$siteToGivePermissionTo/permissions" \
   --header "Content-Type: application/json" \
   --header "Authorization: Bearer $adminToken" \ 
	--data '{ 
	"roles": ["fullcontrol"], 
	"grantedToIdentities": [{ 
	"application": { 
	"id": "'${clientAppId}'",
   "displayName": "'${clientAppName}'"
   }
   }]
   }')

   echo $grantPermissionResponse

   ```
   3. If the command was successful, you'll see a response as
    follows:



   ```

   {
   "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#sites('awsplatodemo.sharepoint.com%2C[IP_ADDRESS]a7')/permissions/$entity",
   "id": "aTowaS50fG1zLnNwLmV4dHxjMDY5YjhlMi03NGFhLTQzZTQtODljYi1kNmZkMzU4ZmVjZThAZjIwNDQ2OTItZGMwOS00MjZlLWFlMGQtNGFlZDljMTI3ODA2",
   "roles": [
   "fullcontrol"
   ],
   "grantedToIdentitiesV2": [
   {
   "application": {
   "displayName": "demo-client-app",
   "id": "c069b8e2-74aa-43e4-89cb-d6fd358fece8"
   }
   }
   ],
   "grantedToIdentities": [
   {
   "application": {
   "displayName": "demo-client-app",
   "id": "c069b8e2-74aa-43e4-89cb-d6fd358fece8"
   }
   }
   ]
   }

   ```

   ```

## Prerequisites for

using SharePoint App-Only authentication

**If you're using SharePoint App-Only authentication, make
sure you've completed the following steps in
SharePoint (Online):**

- Copied your SharePoint (Online) instance URLs. The format for the host URL
  you enter is
  `https://yourdomain.sharepoint.com/sites/mysite`
  or `https://yourcompany.sharepoint.com`. Your URL
  must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint (Online) instance URL.
- Copied the tenant ID of your Microsoft SharePoint (Online) instance. For
  details on how to find your tenant ID, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id") on the Microsoft
  website.
- Noted your SharePoint (Online) client ID and client secret generated while
  granting permission to SharePoint App-Only, and your Client
  ID and Client secret generated after SharePoint (Online) Azure App
  registration.
- **If you're crawling OneNote documents and using
  **Identity crawler\*\*\*\*, added the
  following permissions:

| **Microsoft<br>Graph**                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| + GroupMember.Read.All (Application) –<br>Read all group memberships<br>+ Notes.Read.All (Application) – Read all<br>OneNote notebooks<br>+ Sites.Read.All (Application) – Read<br>items in all site collections<br>+ User.Read.All (Application) – Read all<br>users' full profiles |

###### Note

No API permissions are required for crawling entities using
SharePoint (Online) **App-Only authentication**.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint (Online) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

## Prerequisites for using basic

authentication

**If you're using basic authentication, make sure you've
completed the following steps in SharePoint (Online):**

- Copied your SharePoint (Online) instance URLs. The format for the host URL
  you enter is
  `https://yourdomain.sharepoint.com/sites/mysite`
  or `https://yourcompany.sharepoint.com`. Your URL
  must start with `https` and contain
  `sharepoint.com`.
- Copied the domain name of your SharePoint (Online) instance URL.
- Noted your basic authentication credentials containing the username and
  password that you use to connect to SharePoint (Online) Online.
- Deactivated **Security Defaults** in your Azure portal
  using an administrative user. For more information on managing security
  default settings in the Azure portal, see [Microsoft documentation on how to enable/disable security
  defaults](https://learn.microsoft.com/en-us/answers/questions/101179/how-to-disable-the-two-factor-authentication-from "https://learn.microsoft.com/en-us/answers/questions/101179/how-to-disable-the-two-factor-authentication-from").
- Deactivated multi-factor authentication (MFA) in your SharePoint account,
  so that Amazon Q is not blocked from crawling your SharePoint
  content.

###### Note

No API permissions are required for crawling entities using **Basic
authentication**.

**In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your SharePoint (Online) authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.

For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").
