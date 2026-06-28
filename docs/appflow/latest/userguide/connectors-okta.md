# Okta connector for Amazon AppFlow

Okta is an identity and access management solution. If you you're an
Okta user, your account contains data about your Okta objects, such as your users,
groups, devices and applications. You can use Amazon AppFlow to transfer data from
Okta to certain AWS services or other supported applications.

## Amazon AppFlow support for Okta

Amazon AppFlow supports Okta as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Okta.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Okta.

## Before you begin

To use Amazon AppFlow to transfer data from Okta to supported destinations, you must meet these
requirements:

- You have an account with Okta that contains the data that you want to transfer. For more
  information about the Okta data objects that Amazon AppFlow supports, see [Supported objects](#okta-objects "#okta-objects").
- In your account , you've created either of the following resources for Amazon AppFlow. These
  resources provide credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account.

  - An OIDC app integration to support OAuth 2.0 authentication. For the steps to create an
    app integration, see [Create OIDC app integrations](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm "https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm") in the Okta Help Center.
  - An API token. For the steps to create one, see [Create an API
    token](https://developer.okta.com/docs/guides/create-an-api-token/main/ "https://developer.okta.com/docs/guides/create-an-api-token/main/") in the Okta Help Center.

- If you created an OIDC app integration, you've configured it with the following
  settings:

  - The application type is _Web Application_.
  - The activated grant types include _Authorization Code_
    and _Refresh Token_.
  - The sign-in redirect URIs include one or more URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from Okta. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - The following scopes are permitted:

    - `okta.apps.read`
    - `okta.devices.read`
    - `okta.groups.read`
    - `okta.users.read`
    - `okta.userTypes.read`

If you created an OIDC app integration, note the client ID and client secret . If you
created an API token, note the token value. You provide these values to Amazon AppFlow when you connect
to your Okta account.

## Connecting Amazon AppFlow to your Okta account

To connect Amazon AppFlow to your Okta account, provide the client credentials from
your app integration, or provide an API token. If you haven't yet configured your
Okta account for Amazon AppFlow integration, see [Before you begin](#okta-prereqs "#okta-prereqs").

###### To connect to Okta

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Okta**.
4. Choose **Create connection**.
5. In the **Connect to Okta** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your Okta
   account when it requests to access your data:

   - Choose **OAuth2** to authenticate Amazon AppFlow with the client credentials
     from an OIDC app integration. Then, specify the following:

     - **Authorization tokens URL** and **Authorization code
       URL** – For each of these fields, do the following:

       1. Choose the format of your Okta Org URL. For more information, see
          [Org
          URLs](https://developer.okta.com/docs/concepts/okta-organizations/#org-urls "https://developer.okta.com/docs/concepts/okta-organizations/#org-urls") in the Okta Developer documentation.
       2. Enter your Okta subdomain. For the steps to look up your subdomain,
          see [Find your
          Okta domain](https://developer.okta.com/docs/guides/find-your-domain/main/ "https://developer.okta.com/docs/guides/find-your-domain/main/") in the Okta Developer documentation..

     - **Client ID** – The client ID from your app
       integration.
     - **Client secret** – The client secret from your app
       integration.

   - Choose **Okta\_API\_Token** to authenticate Amazon AppFlow with an API token.
     Then, enter the token value for **Okta API Token**.

6. For **Your Okta Domain URL**, enter your domain URL, such as
   ``my-domain`.okta.com`. For the steps to find
   your domain, see [Find your Okta domain](https://developer.okta.com/docs/guides/find-your-domain/main/ "https://developer.okta.com/docs/guides/find-your-domain/main/") in the Okta Developer documentation.
7. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 8. For **Connection name**, enter a name for your connection. 9. Choose **Continue**. 10. In the window that appears, sign in to your Okta account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Okta as the data source, you can select this connection.

## Transferring data from Okta with a flow

To transfer data from Okta, create an Amazon AppFlow flow, and choose Okta as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Okta, see [Supported objects](#okta-objects "#okta-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#okta-destinations "#okta-destinations").

## Supported destinations

When you create a flow that uses Okta as the data source, you can set the destination to any of the following connectors:

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

## Supported objects

When you create a flow that uses Okta as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                             | **Field**     | **Data type**                                                                                                 | **Supported filters**                                                                                         |
| -------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Application                            | Accessibility | Struct                                                                                                        |                                                                                                               |
| Created                                | DateTime      |                                                                                                               |
| Credentials                            | Struct        |                                                                                                               |
| Credentials Signing Key ID             | String        | EQUAL\_TO                                                                                                     |
| Embedded                               | Struct        |                                                                                                               |
| Features                               | List          |                                                                                                               |
| Group ID                               | String        | EQUAL\_TO                                                                                                     |
| ID                                     | String        |                                                                                                               |
| Label                                  | String        |                                                                                                               |
| Last Updated                           | DateTime      |                                                                                                               |
| Links                                  | Struct        |                                                                                                               |
| Name                                   | String        | EQUAL\_TO                                                                                                     |
| Profile                                | Struct        |                                                                                                               |
| Request Object Signing Alg             | String        |                                                                                                               |
| Settings                               | Struct        |                                                                                                               |
| Status                                 | String        | EQUAL\_TO                                                                                                     |
| User ID                                | String        | EQUAL\_TO                                                                                                     |
| Visibility                             | Struct        |                                                                                                               |
| signOnMode                             | String        |                                                                                                               |
| Device                                 | Created       | DateTime                                                                                                      |                                                                                                               |
| Display Name                           | String        | EQUAL\_TO                                                                                                     |
| ID                                     | String        | EQUAL\_TO                                                                                                     |
| IMEI                                   | String        | EQUAL\_TO                                                                                                     |
| Last Updated                           | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Links                                  | Struct        |                                                                                                               |
| Manufacturer                           | String        | EQUAL\_TO                                                                                                     |
| Mobile Equipment Identifier (MEID)     | String        | EQUAL\_TO                                                                                                     |
| Model                                  | String        | EQUAL\_TO                                                                                                     |
| OS Version                             | String        | EQUAL\_TO                                                                                                     |
| Platform                               | String        | EQUAL\_TO                                                                                                     |
| Profile                                | Struct        |                                                                                                               |
| Registered                             | Boolean       | EQUAL\_TO                                                                                                     |
| Resource Alternate ID                  | String        |                                                                                                               |
| Resource Display Name                  | Struct        |                                                                                                               |
| Resource ID                            | String        |                                                                                                               |
| Resource Type                          | String        |                                                                                                               |
| Secure Hardware Present                | Boolean       | EQUAL\_TO                                                                                                     |
| Serial Number                          | String        | EQUAL\_TO                                                                                                     |
| Status                                 | String        | EQUAL\_TO                                                                                                     |
| Windows Security identifier (SID)      | String        | EQUAL\_TO                                                                                                     |
| macOS UDID                             | String        | EQUAL\_TO                                                                                                     |
| tpmPublicKeyHash                       | String        | EQUAL\_TO                                                                                                     |
| Group                                  | Created       | DateTime                                                                                                      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Embedded                               | Struct        |                                                                                                               |
| GUID (objectGUID) of the Windows Group | String        | EQUAL\_TO                                                                                                     |
| Group Description                      | String        | EQUAL\_TO                                                                                                     |
| Group Name                             | String        | EQUAL\_TO                                                                                                     |
| ID                                     | String        | EQUAL\_TO                                                                                                     |
| Last Membership Updated                | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Last Updated                           | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Links                                  | Struct        |                                                                                                               |
| Object Class                           | List          |                                                                                                               |
| Profile                                | Struct        |                                                                                                               |
| SAM Account Name                       | String        | EQUAL\_TO                                                                                                     |
| Source ID                              | String        | EQUAL\_TO                                                                                                     |
| Type                                   | String        | EQUAL\_TO                                                                                                     |
| Windows Domain Qualified Name          | String        | EQUAL\_TO                                                                                                     |
| Windows Group Distinguished Name       | String        | EQUAL\_TO                                                                                                     |
| User                                   | Activated     | DateTime                                                                                                      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| City                                   | String        | EQUAL\_TO                                                                                                     |
| Cost Center                            | String        | EQUAL\_TO                                                                                                     |
| Country Code                           | String        | EQUAL\_TO                                                                                                     |
| Created                                | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Credentials                            | Struct        |                                                                                                               |
| Department                             | String        | EQUAL\_TO                                                                                                     |
| Display Name                           | String        | EQUAL\_TO                                                                                                     |
| Division                               | String        | EQUAL\_TO                                                                                                     |
| Email                                  | String        | EQUAL\_TO                                                                                                     |
| Embedded Resources                     | Struct        |                                                                                                               |
| Employee Number                        | String        | EQUAL\_TO                                                                                                     |
| First Name                             | String        | EQUAL\_TO                                                                                                     |
| Honorific Prefix                       | String        | EQUAL\_TO                                                                                                     |
| Honorific Suffix                       | String        | EQUAL\_TO                                                                                                     |
| ID                                     | String        | EQUAL\_TO                                                                                                     |
| Last Login                             | DateTime      |                                                                                                               |
| Last Name                              | String        | EQUAL\_TO                                                                                                     |
| Last Updated                           | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Links                                  | Struct        |                                                                                                               |
| Locale                                 | String        | EQUAL\_TO                                                                                                     |
| Manager Display Name                   | String        | EQUAL\_TO                                                                                                     |
| Manager ID                             | String        | EQUAL\_TO                                                                                                     |
| Middle Name                            | String        | EQUAL\_TO                                                                                                     |
| Mobile Phone                           | String        | EQUAL\_TO                                                                                                     |
| Nickname                               | String        | EQUAL\_TO                                                                                                     |
| Occupation                             | String        | EQUAL\_TO                                                                                                     |
| Organization                           | String        | EQUAL\_TO                                                                                                     |
| Password Changed                       | DateTime      |                                                                                                               |
| Postal Address                         | String        | EQUAL\_TO                                                                                                     |
| Preferred Language                     | String        | EQUAL\_TO                                                                                                     |
| Primary Phone                          | String        | EQUAL\_TO                                                                                                     |
| Profile                                | Struct        |                                                                                                               |
| Profile URL                            | String        | EQUAL\_TO                                                                                                     |
| Second Email                           | String        | EQUAL\_TO                                                                                                     |
| State                                  | String        | EQUAL\_TO                                                                                                     |
| Status                                 | String        | EQUAL\_TO                                                                                                     |
| Status Changed                         | DateTime      | EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO |
| Street Address                         | String        | EQUAL\_TO                                                                                                     |
| Timezone                               | String        | EQUAL\_TO                                                                                                     |
| Title                                  | String        | EQUAL\_TO                                                                                                     |
| Transitioning to status                | String        |                                                                                                               |
| Type                                   | Struct        |                                                                                                               |
| Type ID                                | String        | EQUAL\_TO                                                                                                     |
| User Type                              | String        | EQUAL\_TO                                                                                                     |
| Username                               | String        | EQUAL\_TO                                                                                                     |
| Zip Code                               | String        | EQUAL\_TO                                                                                                     |
| User Type                              | Created       | DateTime                                                                                                      |                                                                                                               |
| Created By                             | String        |                                                                                                               |
| Default                                | Boolean       |                                                                                                               |
| Description                            | String        |                                                                                                               |
| Display Name                           | String        |                                                                                                               |
| ID                                     | String        |                                                                                                               |
| Last Updated                           | DateTime      |                                                                                                               |
| Last Updated By                        | String        |                                                                                                               |
| Links                                  | Struct        |                                                                                                               |
| Name                                   | String        |                                                                                                               |
