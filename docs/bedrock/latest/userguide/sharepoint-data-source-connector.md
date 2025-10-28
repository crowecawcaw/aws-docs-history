# Connect to Microsoft SharePoint for your

knowledge base

Microsoft SharePoint is a collaborative web-based service for working on documents, web pages,
web sites, lists, and more. You can connect to your SharePoint instance for your Amazon Bedrock
knowledge base by using either the [AWS Management
Console for Amazon Bedrock](https://console.aws.amazon.com/bedrock/home "https://console.aws.amazon.com/bedrock/home") or the [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") API (see Amazon Bedrock
[supported
SDKs and AWS CLI](../APIReference/welcome.md "../APIReference/welcome.md")).

###### Note

SharePoint data source connector is in preview release and is subject to change.

Microsoft SharePoint data sources don't support multimodal data, such as tables, charts, diagrams, or other images.

Amazon Bedrock supports connecting to SharePoint Online instances. Crawling OneNote documents is
currently not supported. Currently, only Amazon OpenSearch Serverless vector store is
available to use with this data source.

There are limits to how many files and MB per file that can be crawled. See [Quotas for knowledge
bases](quotas.md "quotas.md").

###### Topics

- [Supported features](#supported-features-sharepoint-connector "#supported-features-sharepoint-connector")
- [Prerequisites](#prerequisites-sharepoint-connector "#prerequisites-sharepoint-connector")
- [Connection configuration](#configuration-sharepoint-connector "#configuration-sharepoint-connector")

## Supported features

- Auto detection of main document fields
- Inclusion/exclusion content filters
- Incremental content syncs for added, updated, deleted content
- SharePoint App-Only authentication

## Prerequisites

### SharePoint

(Online)

**In your SharePoint (Online), complete the following steps
for using SharePoint App-Only authentication:**

- Take note of your SharePoint Online site URL/URLs. For example,
  `https://yourdomain.sharepoint.com/sites/mysite`.
  Your URL must start with `https` and contain
  `sharepoint.com`. Your site URL must be the
  actual SharePoint site, not `sharepoint.com/` or
  `sites/mysite/home.aspx`
- Take note of the domain name of your SharePoint Online instance
  URL/URLs.
- Copy your Microsoft 365 tenant ID. You can find your tenant ID in the
  Properties of your Microsoft Entra portal. For details, see [Find your Microsoft 365 tenant ID](https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id "https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id").

###### Note

For an example application, see [Register a client application in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application "https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application")
(formerly known as Azure Active Directory) on the Microsoft Learn
website.

- Configure SharePoint App-Only credentials.
- Copy the client ID and client secret value when granting permission to
  SharePoint App-Only. For more information, see [Granting access using SharePoint App-Only](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs "https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs").

###### Note

You do not need to setup any API permission for SharePoint
App-Only. However, you must configure APP permissions on the SharePoint side. For more information about the required APP permissions, see the Microsoft documentation on [Granting access using SharePoint App-Only](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs "https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs").

### AWS account

**In your AWS account, make sure you**:

- Store your authentication credentials in an [AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") and note the
  Amazon Resource Name (ARN) of the secret. Follow the **Connection configuration** instructions on this page to include
  the key-values pairs that must be included in your secret.
- Include the necessary permissions to connect to your data source in your
  AWS Identity and Access Management (IAM) role/permissions policy for your
  knowledge base. For information on the required permissions for this data source
  to add to your knowledge base IAM role, see
  [Permissions to access data sources](kb-permissions.md#kb-permissions-access-ds "kb-permissions.md#kb-permissions-access-ds").

###### Note

If you use the console, you can go to AWS Secrets Manager to add your secret or use an
existing secret as part of the data source configuration step. The IAM role
with all the required permissions can be created for you as part of the console steps for
creating a knowledge base. After you have configured your data source and other configurations,
the IAM role with all the required permissions are applied to your specific
knowledge base.

We recommend that you regularly refresh or rotate your credentials and secret. Provide
only the necessary access level for your own security. We do not recommend that you re-use
credentials and secrets across data sources.

## Connection configuration

To connect to your SharePoint instance, you must provide the necessary configuration
information so that Amazon Bedrock can access and crawl your data. You must also follow the [Prerequisites](#prerequisites-sharepoint-connector "#prerequisites-sharepoint-connector").

An example of a configuration for this data source is included in this section.

For more information about auto detection of document fields, inclusion/exclusion
filters, incremental syncing, secret authentication credentials, and how these work,
select the following:

The data source connector automatically detects and crawls all of the main metadata fields of your
documents or content. For example, the data source connector can crawl the document body
equivalent of your documents, the document title, the document creation or modification date,
or other core fields that might apply to your documents.

###### Important

If your content includes sensitive information, then Amazon Bedrock could
respond using sensitive information.

You can apply filtering operators to metadata fields to help you further improve the
relevancy of responses. For example, document "epoch_modification_time" or the number of seconds that’s passed
January 1 1970 for when the document was last updated. You can filter on the most recent data, where
"epoch_modification_time" is _greater than_ a certain number. For more information
on the filtering operators you can apply to your metadata fields, see [Metadata and filtering](kb-test-config.md "kb-test-config.md").

You can include or exclude crawling certain content. For example, you can specify an
exclusion prefix/regular expression pattern to skip crawling any file that contains
“private” in the file name. You could also specify an inclusion prefix/regular expression
pattern to include certain content entities or content types. If you specify an inclusion
and exclusion filter and both match a document, the exclusion filter takes
precedence and the document isn’t crawled.

An example of a regular expression pattern to exclude or filter out PDF files
that contain "private" in the file name:
_".\*private.\*\\.pdf"_

You can apply inclusion/exclusion filters on the following content
types:

- `Page`: Main page title
- `Event`: Event name
- `File`: File name with its extension for attachments and
  all document files
  Crawling OneNote documents is currently not supported.

The data source connector crawls new, modified, and deleted content each time your data
source syncs with your knowledge base. Amazon Bedrock can use your data source’s mechanism
for tracking content changes and crawl content that changed since the last sync. When you sync
your data source with your knowledge base for the first time, all content is crawled by default.

To sync your data source with your knowledge base, use the [StartIngestionJob](../APIReference/API_agent_StartIngestionJob.md "../APIReference/API_agent_StartIngestionJob.md")
API or select your knowledge base in the console and select **Sync** within the
data source overview section.

###### Important

All data that you sync from your data source becomes available to anyone with
`bedrock:Retrieve` permissions to retrieve the data. This can also include any
data with controlled data source permissions. For more
information, see [Knowledge base permissions](kb-permissions.md "kb-permissions.md").

When using SharePoint App-Only authentication, your secret authentication
credentials in AWS Secrets Manager must include these key-value pairs:

- `clientId`: `client ID associated with your
Microsoft Entra SharePoint application`
- `clientSecret`: `client secret associated with
your Microsoft Entra SharePoint application`
- `sharePointClientId`: `client ID generated when
registering your SharePoint app for App-Only
authentication`
- `sharePointClientSecret`: `client secret
generated when registering your SharePoint app for App-Only
authentication`

###### Note

Your secret in AWS Secrets Manager must use the same Region of your knowledge
base.

Console

###### Connect a SharePoint instance to your knowledge base

1. Follow the steps at [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](knowledge-base-create.md "knowledge-base-create.md") and choose
   **SharePoint** as the data source.
2. Provide a name and optional description for the data source.
3. Provide your SharePoint site URL/URLs. For example, for
   SharePoint Online,
   `https://yourdomain.sharepoint.com/sites/mysite`.
   Your URL must start with `https` and
   contain `sharepoint.com`. Your site URL
   must be the actual SharePoint site, not
   `sharepoint.com/` or
   `sites/mysite/home.aspx`
4. Provide the domain name of your SharePoint instance.
5. In the **Advanced settings** section, you can optionally configure the following:
   - **KMS key for transient data storage.** – You can encrypt the transient data while converting your data into embeddings with the default AWS managed key or your own KMS key. For more information, see [Encryption of transient data storage during data ingestion](encryption-kb.md#encryption-kb-ingestion "encryption-kb.md#encryption-kb-ingestion").
   - **Data deletion policy** – You can delete the vector embeddings for your data source that are stored in the vector store by default, or choose to retain the vector store data.

6. Provide the authentication information to connect to your
   SharePoint instance. For SharePoint App-Only
   authentication:
   1. Provide the tenant ID. You can find your tenant ID in the
      Properties of your Azure Active Directory portal.
   2. Go to AWS Secrets Manager to add your secret credentials or use an
      existing Amazon Resource Name (ARN) for the secret you
      created. Your secret must contain the SharePoint client ID
      and the SharePoint client secret generated when you
      registered the App-Only at the tenant level or the site
      level, and the Entra client ID and Entra client secret
      generated when you register the app in Entra.

7. (Optional) In the **Content parsing and chunking** section, you can customize how to parse and chunk your data. Refer to the following resources to learn more about these customizations:
   - For more information about parsing options, see [Parsing options for your data source](kb-advanced-parsing.md "kb-advanced-parsing.md").
   - For more information about chunking strategies, see [How content chunking works for knowledge bases](kb-chunking.md "kb-chunking.md").

   ###### Warning

   You can't change the chunking strategy after connecting to the data source.
   - For more information about how to customize chunking of your data and processing of your metadata with a Lambda function, see [Use a custom transformation Lambda function to define how your data is ingested](kb-custom-transformation.md "kb-custom-transformation.md").

8. Choose to use filters/regular expressions patterns to include or exclude certain content.
   All standard content is crawled otherwise.
9. Continue to choose an embeddings model and vector store. To see the remaining steps, return to [Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases](knowledge-base-create.md "knowledge-base-create.md") and continue from the step after connecting your data source.

API
The following is an example of a configuration for connecting to
SharePoint Online for your Amazon Bedrock knowledge base. You configure your data
source using the API with the AWS CLI or supported SDK, such as Python. After
you call [CreateKnowledgeBase](../APIReference/API_agent_CreateKnowledgeBase.md "../APIReference/API_agent_CreateKnowledgeBase.md"), you call [CreateDataSource](../APIReference/API_agent_CreateDataSource.md "../APIReference/API_agent_CreateDataSource.md") to create your data source with
your connection information in `dataSourceConfiguration`.

To learn about customizations that you can apply to ingestion by including the optional
`vectorIngestionConfiguration` field, see [Customize ingestion for a data source](kb-data-source-customize-ingestion.md "kb-data-source-customize-ingestion.md").

**AWS Command Line Interface**

```
aws bedrock-agent create-data-source \
 --name "SharePoint Online connector" \
 --description "SharePoint Online data source connector for Amazon Bedrock to use content in SharePoint" \
 --knowledge-base-id "your-knowledge-base-id" \
 --data-source-configuration file://sharepoint-bedrock-connector-configuration.json \
 --data-deletion-policy "DELETE"
```

**Contents of
`sharepoint-bedrock-connector-configuration.json`**

```
{
    "sharePointConfiguration": {
        "sourceConfiguration": {
            "tenantId": "888d0b57-69f1-4fb8-957f-e1f0bedf64de",
            "hostType": "ONLINE",
            "domain": "yourdomain",
            "siteUrls": [
                "https://yourdomain.sharepoint.com/sites/mysite"
            ],
            "authType": "OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS",
            "credentialsSecretArn": "arn:aws::secretsmanager:your-region:secret:AmazonBedrock-SharePoint"
        },
        "crawlerConfiguration": {
            "filterConfiguration": {
                "type": "PATTERN",
                "patternObjectFilter": {
                    "filters": [
                        {
                            "objectType": "File",
                            "inclusionFilters": [
                                ".*\\.pdf"
                            ],
                            "exclusionFilters": [
                                ".*private.*\\.pdf"
                            ]
                        }
                    ]
                }
            }
        }
    },
    "type": "SHAREPOINT"
}
```

###### Important

The OAuth2.0 authentication is not recommended. We recommend that you use SharePoint
App-Only authentication.

Using OAuth 2.0, you can authenticate and authorize access to SharePoint
resources for SharePoint connectors integrated with Knowledge Bases.

### Pre-requisites

**In SharePoint, for OAuth 2.0 authentication, make sure
you**:

- Take note of your SharePoint Online site URL/URLs. For example,
  `https://yourdomain.sharepoint.com/sites/mysite`.
  Your URL must start with `https` and contain
  `sharepoint.com`. Your site URL must be the
  actual SharePoint site, not `sharepoint.com/`
  or `sites/mysite/home.aspx`
- Take note of the domain name of your SharePoint Online instance
  URL/URLs.
- Copy your Microsoft 365 tenant ID. You can find your tenant ID in the
  Properties of your Microsoft Entra portal or in your OAuth
  application.

Take note of the username and password of the admin SharePoint
account, and copy the client ID and client secret value when registering
an application.

###### Note

For an example application, see [Register a client application in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application "https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application")
(formerly known as Azure Active Directory) on the Microsoft Learn
website.

- Certain read permissions are required to connect to SharePoint when
  you register an application.
  - SharePoint: AllSites.Read (Delegated) – Read items in all site
    collections

- You might need to turn off **Security Defaults** in
  your Azure portal using an admin user. For more information on managing
  security default settings in the Azure portal, see [Microsoft documentation on how to enable/disable security
  defaults](https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-conditional-access?view=o365-worldwide&tabs=secdefaults#security-defaults-1 "https://learn.microsoft.com/en-us/microsoft-365/business-premium/m365bp-conditional-access?view=o365-worldwide&tabs=secdefaults#security-defaults-1").
- You might need to turn off multi-factor authentication (MFA) in your
  SharePoint account, so that Amazon Bedrock is not blocked from crawling your
  SharePoint content.

To complete the pre-requisites, make sure that you've completed the steps in
[AWS account](#prerequisites-sharepoint-connector-account "#prerequisites-sharepoint-connector-account").

### Secret authentication

credentials

For connection configuration for OAuth2.0, you can perform the same steps for
the auto detection of the main document fields, inclusion/exclusion filters, and
incremental syncing as described in [Connection configuration](#configuration-sharepoint-connector "#configuration-sharepoint-connector").

**For OAuth 2.0 authentication, your secret authentication
credentials in AWS Secrets Manager must include these key-value
pairs**.

- `username`: `SharePoint admin
username`
- `password`: `SharePoint admin
password`
- `clientId`: `OAuth app client
ID`
- `clientSecret`: `OAuth app client
secret`

### Connect a SharePoint

instance to your knowledge base

To connect a SharePoint instance to your knowledge base when using
OAuth2.0:

- (console) In the console, follow the same steps as described in [Connect a SharePoint instance to your knowledge base](sharepoint-data-source-connector.md#connect-sharepoint-console "sharepoint-data-source-connector.md#connect-sharepoint-console"). When
  you want to provide the authentication information to connect to your
  SharePoint instance.
  - Provide the tenant ID. You can find your tenant ID in the
    Properties of your Azure Active Directory portal.
  - Go to AWS Secrets Manager to add your secret authentication credentials
    or use an existing Amazon Resource Name (ARN) for the secret you
    created. Your secret must contain the SharePoint admin username
    and password, and your registered app client ID and client
    secret. For an example application, see [Register a client application in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application "https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application")
    (formerly known as Azure Active Directory) on the Microsoft
    Learn website.

- (API) The following is an example of using the
  `CreateDataSource` API to create your data source with
  your connection information for OAuth2.0.

```
aws bedrock-agent create-data-source \
 --name "SharePoint Online connector" \
 --description "SharePoint Online data source connector for Amazon Bedrock to use content in SharePoint" \
 --knowledge-base-id "your-knowledge-base-id" \
 --data-source-configuration file://sharepoint-bedrock-connector-configuration.json \
 --data-deletion-policy "DELETE"
```

**Contents of
`sharepoint-bedrock-connector-configuration.json`**

```
{
    "sharePointConfiguration": {
        "sourceConfiguration": {
            "tenantId": "888d0b57-69f1-4fb8-957f-e1f0bedf64de",
            "hostType": "ONLINE",
            "domain": "yourdomain",
            "siteUrls": [
                "https://yourdomain.sharepoint.com/sites/mysite"
            ],
            "authType": "OAUTH2_CLIENT_CREDENTIALS",
            "credentialsSecretArn": "arn:aws::secretsmanager:your-region:secret:AmazonBedrock-SharePoint"
        },
        "crawlerConfiguration": {
            "filterConfiguration": {
                "type": "PATTERN",
                "patternObjectFilter": {
                    "filters": [
                        {
                            "objectType": "File",
                            "inclusionFilters": [
                                ".*\\.pdf"
                            ],
                            "exclusionFilters": [
                                ".*private.*\\.pdf"
                            ]
                        }
                    ]
                }
            }
        }
    },
    "type": "SHAREPOINT"
}
```
