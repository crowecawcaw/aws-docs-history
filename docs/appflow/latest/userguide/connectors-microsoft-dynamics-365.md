# Microsoft Dynamics 365 connector for Amazon AppFlow

Microsoft Dynamics 365 is a portfolio of business applications for enterprise resource planning
(ERP) and customer relationship management (CRM). If you're a Microsoft Dynamics 365 user, your
account contains data about your business, such as your products, customers, business units, and
more. You can use Amazon AppFlow to transfer data from
Microsoft Dynamics 365 to certain AWS services or other supported applications.

## Amazon AppFlow support for Microsoft Dynamics 365

Amazon AppFlow supports Microsoft Dynamics 365 as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Microsoft Dynamics 365.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Microsoft Dynamics 365.

## Before you begin

To use Amazon AppFlow to transfer data from Microsoft Dynamics 365 to supported destinations, you must meet these
requirements:

- You have a Microsoft account, and you've used it to sign up for Microsoft Dynamics 365. Your
  Microsoft Dynamics 365 account contains the data that you want to transfer.
- In the Microsoft Azure portal, you've created an app registration for Amazon AppFlow. The
  registered app provides the client credentials that authenticate Amazon AppFlow when it accesses the
  data in your account. For the steps to register an app, see [Register an application
  with the Microsoft identity platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2 "https://learn.microsoft.com/en-us/graph/auth-register-app-v2") in the Microsoft Graph documentation.
- You've configured your registered app with the following settings:
  - In the authentication settings, you've added a platform, and you've set the platform
    application type to _web_. You've configured the platform
    with a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from Microsoft Dynamics 365. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._

  For the steps to add a platform and set the redirect URL, see [Add a
  redirect URI](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-a-redirect-uri "https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-a-redirect-uri") in the Microsoft Graph documentation.
  - You've created a client secret. For the steps to create one, see [Add a
    client secret](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-a-client-secret "https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-a-client-secret") in the Microsoft Graph documentation.

  ###### Notes

      - When you connect Amazon AppFlow to your Microsoft Dynamics 365 account, you provide the client
       secret *value*. You don't provide the client secret
       *ID*.
      - At the time that you create the client secret, you must store it's value somewhere
       that you can access later. After you leave the page where you create the client secret,
       Microsoft Azure never shows the value again.

  - In the app manifest, you've edited the following attributes to have a value of
    `true`:

        - `"allowPublicClient": true,`
        - `"oauth2AllowIdTokenImplicitFlow": true,`
        - `"oauth2AllowImplicitFlow": true,`

    For more information about these attributes, and for the steps to configure the app
    manifest, see [Azure Active Directory app manifest](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest "https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest") in the Microsoft identity platform
    documentation.

  - In the API permissions settings, you've set the following configurations:
    - The app permits the `user_impersonation` permission for the Dynamics CRM
      API.
    - The app permits the `User.Read` permission for the Microsoft Graph API. For
      information about this permission, see the [Microsoft Graph
      permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference "https://learn.microsoft.com/en-us/graph/permissions-reference") in the Microsoft Graph documentation.
    - You've turned on the option to grant admin consent. For more information, see [Admin consent](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#admin-consent "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#admin-consent") in the Microsoft identity platform documentation.

Note the following values because you'll need them when you connect Amazon AppFlow to your
Microsoft Dynamics 365 account:

- The application (client) ID of your registered app.
- The directory (tenant) ID of your registered app.
- The client secret value (not the client secret ID) of your registered app.
- The service root URL of your Dynamics 365 instance. You can find this value in the
  **Developer Resources** page in the Dynamics 365 web application. For
  information on how to access this page, see [Developer resources page](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/developer-resources-page?view=op-9-1 "https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/developer-resources-page?view=op-9-1") in the Dynamics 365 documentation.

The service root URL has the following format:

```
https://`instance-id`.api.crm.dynamics.com/api/data/v9.2/
```

You don't provide this URL to Amazon AppFlow directly. Instead, you provide segments of it for the
fields **Custom authorization code URL** and **Instance
URL**.

## Connecting Amazon AppFlow to your Microsoft Dynamics 365

account

To connect Amazon AppFlow to Microsoft Dynamics 365, provide details from your registered app in
Microsoft Azure so that Amazon AppFlow can access your data. If you haven't yet configured your Microsoft
account for Amazon AppFlow integration, see [Before you begin](#microsoft-dynamics-365-prereqs "#microsoft-dynamics-365-prereqs").

###### To connect to Microsoft Dynamics 365

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Microsoft Dynamics 365**.
4. Choose **Create connection**.
5. In the **Connect to Microsoft Dynamics 365** window, enter the following
   information:
   - **Custom authorization code URL** — From your service root URL,
     the segment ``instance-id`.api.crm.dynamics.com`.
   - **Client ID** — The application (client) ID of your registered
     app.
   - **Client secret** — The client secret value (not the client
     secret ID) of your registered app.
   - **Instance URL** — From your service root URL, the segment
     `https://`instance-id`.api.crm.dynamics.com`.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Microsoft Dynamics 365 account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Microsoft Dynamics 365 as the data source, you can select this connection.

## Transferring data from Microsoft Dynamics 365 with a flow

To transfer data from Microsoft Dynamics 365, create an Amazon AppFlow flow, and choose Microsoft Dynamics 365 as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

## Supported destinations

When you create a flow that uses Microsoft Dynamics 365 as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")
