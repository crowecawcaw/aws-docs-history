# Microsoft SharePoint Online connector for Amazon AppFlow

Microsoft SharePoint Online is a collaboration solution that teams use to share files, data, and other
resources throughout their organization. If you're a SharePoint user, you have sites with document
libraries that contain various types of documents, like PDFs, Microsoft Word documents, Microsoft
Excel files, and more. You can use Amazon AppFlow to transfer these documents to Amazon S3. When
you run a transfer, Amazon AppFlow also provides a file with descriptive metadata for each
document.

## Amazon AppFlow support for Microsoft SharePoint Online

Amazon AppFlow supports Microsoft SharePoint Online as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer documents and metadata from
Microsoft SharePoint Online.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Microsoft SharePoint Online.

**Supported destination for SharePoint Online data**

You can transfer only to Amazon S3.

**Supported SharePoint products**

Amazon AppFlow connects only to Microsoft SharePoint Online. It doesn't connect to the on-premises
SharePoint Server product.

## Before you begin

To use Amazon AppFlow to transfer data from Microsoft SharePoint Online to supported destinations, you must
meet the following requirements:

- You have a Microsoft account where you've signed up for Microsoft SharePoint Online. Your
  SharePoint account must have at least one site with a document library. The document library
  must have the documents that you want to transfer.
- You have your Azure AD tenant ID. You provide this ID to Amazon AppFlow when you connect to your
  Microsoft SharePoint Online account. For the steps to look up the ID, see [Find your Azure AD tenant](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-ad-tenant "https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-ad-tenant") in the Azure portal documentation.

If you meet those requirements, you're ready to create a connection between Amazon AppFlow and your
Sharepoint account. No additional steps are necessary in your Microsoft account because Amazon AppFlow
fulfills the remaining requirements with an _AWS managed client
app_.

### The AWS managed client app for

Sharepoint

The AWS managed client app for Sharepoint simplifies the connection setup. If you use it,
you don't have to provide the OAuth 2.0 credentials of a client ID and client secret. To get
those credentials, you would have to create an app registration in Microsoft Azure. Instead, the
only information that you must get from your Microsoft account is your Azure tenant ID. To
create the connection, you provide the tenant ID and, when Amazon AppFlow prompts you, you sign into
your Microsoft account and authorize Amazon AppFlow to access to your Sharepoint data.

Alternatively, you can choose to create a connection that uses OAuth 2.0 credentials from
your own app registration instead of the AWS managed client app. This option is more
complicated, but it gives you more control over the credentials. For example, you could use
Microsoft Azure to change the credentials, revoke them, or manage who can access them.

If you want to authorize Amazon AppFlow with the OAuth 2.0 credentials from your own app
registration, you must meet these requirements:

- In the Microsoft Azure portal, you've created an app registration for Amazon AppFlow. For the
  steps to register an app, see [Register an application
  with the Microsoft identity platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2 "https://learn.microsoft.com/en-us/graph/auth-register-app-v2") in the Microsoft Graph documentation.
- You've configured your registered app as follows:

      + You've added one or more redirect URLs for Amazon AppFlow.


      Redirect URLs have the following format:



      ```
      https://`region`.console.aws.amazon.com/appflow/oauth
      ```

      In this URL, *region* is the code for the AWS Region
       where you use Amazon AppFlow to transfer data from Microsoft SharePoint Online. For example, the code for the US East (N. Virginia)
       Region is `us-east-1`. For that Region, the URL is the following:



      ```
      https://us-east-1.console.aws.amazon.com/appflow/oauth
      ```

      For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
       in the *AWS General Reference.*
      + You've added the recommended permissions.
      + You've created a client secret.

  Note the following values from your registered app because you provide them to Amazon AppFlow when
  you connect to your Sharepoint account:

- Application (client) ID
- Client secret

#### Recommended permissions for the app

registration

Before Amazon AppFlow can securely access your data in Microsoft SharePoint Online, your registered app
must allow the necessary permissions for the Microsoft Graph API. We recommend that you allow
the following permissions so that Amazon AppFlow can access all supported resources.

You can add permissions to your registered app by using the API permissions page in the
Microsoft Azure portal. Configure your permissions as follows:

- Under **Microsoft APIs**, choose **Microsoft
  Graph**.
- For the permissions type, choose **delegated**. For information about
  delegated permissions, see [Permission types](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#using-the-admin-consent-endpoint "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent#using-the-admin-consent-endpoint") in the Microsoft identity platform documentation.
- Add the following recommended permissions:

      + `offline_access`
      + `Sites.Read.All`
      + `User.Read`

  For information about these permissions, see the [Microsoft Graph
  permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference "https://learn.microsoft.com/en-us/graph/permissions-reference") in the Microsoft Graph documentation.

## Connecting Amazon AppFlow to your Microsoft SharePoint Online

account

To connect Amazon AppFlow to Microsoft SharePoint Online, provide details from your registered app in
Microsoft Azure so that Amazon AppFlow can access the documents in your SharePoint document libraries. If
you haven't yet configured your Microsoft account for Amazon AppFlow integration, see [Before you begin](#microsoft-sharepoint-online-prereqs "#microsoft-sharepoint-online-prereqs").

###### To connect to Microsoft SharePoint Online

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Microsoft SharePoint Online**.
4. Choose **Create connection**.
5. In the **Connect to Microsoft SharePoint Online** window, enter the following
   information about your registered app:
   - **Custom authorization tokens URL** – Your Azure AD tenant
     ID.
   - **Custom authorization code URL** – Azure AD tenant ID

6. By default, the **Use AWS managed client app** checkbox is activated.
   You can do either of the following:
   - If you want to use the AWS managed client app, keep the checkbox activated.
   - If you want to use your own client app (called an app registration in Microsoft Azure),
     choose the checkbox to deactivate it. Then, provide values for **Client ID**
     and **Client secret**.

7. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 8. For **Connection name**, enter a name for your connection. 9. Choose **Continue**. A window appears that asks if you want to allow
Amazon AppFlow to access your Microsoft SharePoint Online account. 10. Choose **Authorize**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Microsoft SharePoint Online as the data source, you can select this connection.

## Transferring data from Microsoft SharePoint Online with a flow

To transfer documents and metadata from Microsoft SharePoint Online to Amazon S3, create an Amazon AppFlow flow.
In the flow configuration, you set the data source by choosing a Microsoft SharePoint Online connection.
Specifically for flows that transfer from SharePoint, you also choose a SharePoint site that's
hosted in your account, and one or more SharePoint document libraries that belong to the site.
You also set the data destination by choosing an Amazon S3 bucket in your AWS account.

###### To configure a flow with Microsoft SharePoint Online as the data source

For the standard steps to create a flow, see [Create a flow using the AWS console](create-flow-console.md "create-flow-console.md"). Use the following steps only to configure the data
source and data destination details for a flow that transfers from SharePoint. You configure
these settings when you reach the **Configure flow** page in the flow creation
process.

1. Under **Source details**, for **Source name**, choose
   **Microsoft SharePoint Online**.
2. For **Choose Microsoft SharePoint Online connection**, choose the connection that
   you created. If you haven't created a connection yet, see [Connecting Amazon AppFlow to your Microsoft SharePoint Online
   account](#microsoft-sharepoint-online-connecting "#microsoft-sharepoint-online-connecting").
3. For **Choose API version**, choose **v1.0**.
4. For **Choose Microsoft SharePoint Online site**, choose the SharePoint site in
   your account that contains the documents that you want to transfer.
5. Under **Selected resources**, the console shows the document libraries
   that belong to the SharePoint site. Each document library is represented as a folder. If a
   folder contains subfolders or documents, you can expand the folder to show its contents.

Select the check box for one or more folders to pick the documents that your flow
transfers to Amazon S3. When you run the flow, Amazon AppFlow transfers the documents that are in the
folder, in addition to the documents that are in all of its subfolders.

For the limits that apply to how many folders and documents you can transfer, see [Quotas and limitations for the Microsoft SharePoint Online
connector](#microsoft-sharepoint-online-quotas "#microsoft-sharepoint-online-quotas"). 6. Under **Destination details**, for **Destination name**,
choose **Amazon S3**. Then, for **Bucket details**, choose the S3
bucket that stores the output from your flow. To organize your output, you can specify an
optional prefix, which becomes a folder in your S3 bucket.

After you configure your flow with a SharePoint document library and a destination S3
bucket, you can work through the remaining flow configuration steps in the console by using the
standard steps.

### Microsoft SharePoint Online output in Amazon S3

When you run a flow that transfers from SharePoint, Amazon AppFlow creates the following items in
the destination S3 bucket:

- A JSON file that contains metadata about every document that Amazon AppFlow transfers from your
  document libraries. For the metadata fields, see [Supported metadata fields
  for Microsoft SharePoint Online documents](#microsoft-sharepoint-online-objects "#microsoft-sharepoint-online-objects"). The name of the file is the execution
  ID of the flow run. To learn what flow run the execution ID is associated with, you can view a
  list of IDs under the **Run history** tab in the details page for a
  flow.
- A folder that contains the folders and documents that you transferred from the document
  libraries of your site. The name of this folder is also the execution ID of the flow
  run.

The scope of the output depends on whether you configured the flow to run on a schedule or
run on demand:

- If the flow runs on a schedule, Amazon AppFlow performs incremental data transfers. When the flow
  runs for the first time, Amazon AppFlow transfers every document in the document libraries that you
  chose in the data source configuration. Then, for all subsequent flow runs, Amazon AppFlow transfers
  only those files that you created or changed in SharePoint since the prior flow run.

To configure a flow to run on a schedule, you can use the console to set the schedule
settings under **Flow trigger** in the flow creation process.

- If the flow runs on demand, Amazon AppFlow performs full data transfers. For every flow run,
  Amazon AppFlow transfers every document in the document libraries that you chose in the data source
  configuration.

To configure a flow to run on demand, you can use the console to set this option under
**Flow trigger** in the flow creation process. After you create an on-demand
flow, you run the flow by choosing **Run flow** on the flow details
page.

## Supported metadata fields

for Microsoft SharePoint Online documents

When you run a flow that transfers documents from Microsoft SharePoint Online,
Amazon AppFlow creates a metadata file in the destination S3 bucket. The
metadata describes each document that Amazon AppFlow transferred for the flow
run.

The following table lists the metadata fields that Amazon AppFlow supports.
For each transferred document, Amazon AppFlow writes only those fields that
apply to the document type.

| **Metadata field**
| **Data type**
| **Supported filters**
|
| --- | --- | --- |
| Audio | Struct | |
| Bundle | Struct | |
| Created DateTime | DateTime | |
| CreatedBy | Struct | |
| Deleted | Struct | |
| Description | String | |
| Entity Content Tag | String | |
| Entity Tag | String | |
| File | Struct | |
| File System Info | Struct | |
| File Type | String | EQUAL_TO |
| Id | String | |
| Image | Struct | |
| Last Modified By | Struct | |
| Last Modified DateTime | DateTime | GREATER_THAN |
| Location | Struct | |
| Malware | Struct | |
| Name | String | |
| Package | Struct | |
| Parent Reference | Struct | |
| Pending Operations | Struct | |
| Photo | Struct | |
| Publication | Struct | |
| Remote Item | Struct | |
| Root | Struct | |
| Search Result | Struct | |
| SharePoint Ids | Struct | |
| Shared | Struct | |
| Size | Integer | |
| Special Folder | Struct | |
| Video | Struct | |
| Web Dav Url | String | |
| Web Url | String | | ## Quotas and limitations for the Microsoft SharePoint Online connector The following table lists the quotas that apply to flows that transfer from SharePoint.
| Resource | Quota | | --- | --- |
| The maximum number of SharePoint document library folders transferred by a flow | 17 | | The maximum size of any file transferred by a flow | 250 GB |
| The maximum number of files transferred by a flow run | 10,000 | | The maximum total data size transferred by a flow run | 250 GB | The following limitations also apply to flows that transfer from SharePoint: <br>• For scheduled flows, if a flow remains running when the next flow run is scheduled to start, then Amazon AppFlow skips the next flow run. Amazon AppFlow does this to allow the first flow run enough time to complete. <br>• Amazon AppFlow doesn't provide the option to catalog your output in the AWS Glue Data Catalog. Amazon AppFlow typically provides that option for flows that transfer to Amazon S3, but the option is available only for structured source data. The documents that you transfer from your SharePoint document libraries are unstructured data. <br>• Amazon AppFlow doesn't provide the data partitioning options that it typically provides for flows that transfer to Amazon S3. Amazon AppFlow partitions all SharePoint output only into folders that are named after the execution ID of the flow run.
