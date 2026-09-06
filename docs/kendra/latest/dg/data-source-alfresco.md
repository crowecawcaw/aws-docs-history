

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Alfresco
<a name="data-source-alfresco"></a>

**Note**  
Alfresco connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the Amazon Kendra Custom Connector Framework[1], designed to support a broader range of enterprise use cases with enhanced flexibility.

Alfresco is a content management service that helps customers store and manage their content. You can use Amazon Kendra to index your Alfresco Document library, Wiki, and Blog.

Amazon Kendra supports Alfresco On-Premises and Alfresco Cloud (Platform as a Service).

You can connect Amazon Kendra to your Alfresco data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/) or the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_TemplateConfiguration.html) API.

For troubleshooting your Amazon Kendra Alfresco data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md).

**Topics**
+ [Supported features](#supported-features-alfresco)
+ [Prerequisites](#prerequisites-alfresco)
+ [Connection instructions](#data-source-procedure-alfresco)
+ [Learn more](#alfresco-learn-more)

## Supported features
<a name="supported-features-alfresco"></a>

Amazon Kendra Alfresco data source connector supports the following features:
+ Field mappings
+ User access control
+ Inclusion/exclusion filters
+ Full and incremental content syncs
+ OAuth 2.0 and basic authentication
+ Virtual private cloud (VPC)

## Prerequisites
<a name="prerequisites-alfresco"></a>

Before you can use Amazon Kendra to index your Alfresco data source, make these changes in your Alfresco and AWS accounts.

**In Alfresco, make sure you have:**
+ Copied your Alfresco repository URL and web application URL. If you only want to index a specific Alfresco site, then also copy the site ID.
+ Noted your Alfresco authentication credentials, which include a user name and password with at least read permissions. If you want to use OAuth 2.0 authentication, you should add the user to the Alfresco administrators group.
**Note**  
We recommend that you regularly refresh or rotate your credentials and secret. Provide only the necessary access level for your own security. We do **not** recommend that you re-use credentials and secrets across data sources, and connector versions 1.0 and 2.0 (where applicable).
+ **Optional**: Configured OAuth 2.0 credentials in Alfresco. The credentials include client ID, client secret, and token URL. For more information on how to configure clients for Alfresco On-Premises, see [Alfresco documentation](https://docs.alfresco.com/identity-service/latest/tutorial/sso/saml/). If you use Alfresco Cloud (PaaS), you must contact [Hyland support](https://community.hyland.com/) for Alfresco OAuth 2.0 authentication.
+ Checked each document is unique in Alfresco and across other data sources you plan to use for the same index. Each data source that you want to use for an index must not contain the same document across the data sources. Document IDs are global to an index and must be unique per index.

**In your AWS account, make sure you have:**
+ [Created an Amazon Kendra index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html) and, if using the API, noted the index ID.
+ [Created an IAM role](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds) for your data source and, if using the API, noted the ARN of the IAM role.
**Note**  
If you change your authentication type and credentials, you must update your IAM role to access the correct AWS Secrets Manager secret ID.
+ Stored your Alfresco authentication credentials in an AWS Secrets Manager secret and, if using the API, noted the ARN of the secret.
**Note**  
We recommend that you regularly refresh or rotate your credentials and secret. Provide only the necessary access level for your own security. We do **not** recommend that you re-use credentials and secrets across data sources, and connector versions 1.0 and 2.0 (where applicable).

If you don’t have an existing IAM role or secret, you can use the console to create a new IAM role and Secrets Manager secret when you connect your Alfresco data source to Amazon Kendra. If you are using the API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions
<a name="data-source-procedure-alfresco"></a>

To connect Amazon Kendra to your Alfresco data source, you must provide the necessary details of your Alfresco data source so that Amazon Kendra can access your data. If you have not yet configured Alfresco for Amazon Kendra, see [Prerequisites](#prerequisites-alfresco).

------
#### [ Console ]

**To connect Amazon Kendra to Alfresco**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/).

1. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.
**Note**  
You can choose to configure or edit your **User access control** settings under **Index settings**. 

1. On the **Getting started** page, choose **Add data source**.

1. On the **Add data source** page, choose **Alfresco connector**, and then choose **Add connector**. If using version 2 (if applicable), choose **Alfresco connector** with the "V2.0" tag.

1. On the **Specify data source details** page, enter the following information:

   1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.

   1. (Optional)** Description**—Enter an optional description for your data source.

   1. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise, the language defaults to English. Language specified in the document metadata overrides the selected language.

   1. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.

   1. Choose **Next**.

1. On the **Define access and security** page, enter the following information:

   1. **Alfresco type**—Choose whether you use Alfresco On-Premises/server or Alfresco Cloud (Platform as a Service).

   1. **Alfresco repository URL**—Enter your Alfresco repository URL. For example, if you use Alfresco Cloud (PaaS), the repository URL could be *https://company.alfrescocloud.com*. Or, if you use Alfresco On-Premises, the repository URL could be *https://company-alfresco-instance.company-domain.suffix:port*.

   1. **Alfresco user application. URL**—Enter your Alfresco user interface URL. You can get the repository URL from your Alfresco administrator. For example, the user interface URL could be *https://example.com*.

   1. **SSL certificate location**—Enter the path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to Alfresco On-Premises with a secure SSL connection.

   1. **Authorization**—Turn on or off access control list (ACL) information for your documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users and groups can access. The ACL information is used to filter search results based on the user or their group access to documents. For more information, see [User context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html#context-filter-user-incl-datasources).

   1. **Authentication**—Choose **Basic authentication** or **OAuth 2.0 authentication**. Then choose an existing Secrets Manager secret or create a new secret to store your Alfresco credentials. If you choose to create a new secret, an AWS Secrets Manager secret window opens.

      If you chose **Basic authentication**, enter a name for the secret, the Alfresco user name, and password.

      If you chose **OAuth 2.0 authentication**, enter a name for the secret, client ID, client secret, and token URL.

   1. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If so, you must add **Subnets** and **VPC security groups**.

   1. **Identity crawler**—Specify whether to turn on Amazon Kendra’s identity crawler. The identity crawler uses the access control list (ACL) information for your documents to filter search results based on the user or their group access to documents. If you have an ACL for your documents and choose to use your ACL, you can then also choose to turn on Amazon Kendra’s identity crawler to configure [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html#context-filter-user-incl-datasources) of search results. Otherwise, if identity crawler is turned off, all documents can be publicly searched. If you want to use access control for your documents and identity crawler is turned off, you can alternatively use the [PutPrincipalMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_PutPrincipalMapping.html) API to upload user and group access information for user context filtering.

   1. **IAM role**—Choose an existing IAM role or create a new IAM role to access your repository credentials and index content.
**Note**  
IAM roles used for indexes cannot be used for data sources. If you are unsure if an existing role is used for an index or FAQ, choose **Create a new role** to avoid errors.

   1. Choose **Next**.

1. On the **Configure sync settings** page, enter the following information:

   1. **Sync scope**—Set limits for crawling certain content and filter content using regex expression patterns.

   1. 

      1. **Content**—Choose whether to crawl content marked with 'Aspects' in Alfresco, content within a specific Alfresco site, or content across all your Alfresco sites.

      1. (Optional)**Additional configuration**—Set the following settings:
         + **Include comments**—Choose to include comments in Alfresco Document library and Blog.
         + **Regex patterns**—Regular expression patterns to include or exclude certain files.

   1. **Sync mode**—Choose how you want to update your index when your data source content changes. When you sync your data source with Amazon Kendra for the first time, all content is crawled and indexed by default. You must run a full sync of your data if your initial sync failed, even if you don't choose full sync as your sync mode option.
      + Full sync: Freshly index all content, replacing existing content each time your data source syncs with your index.
      + New, modified, deleted sync: Index only new, modified, and deleted content each time your data source syncs with your index. Amazon Kendra can use your data source's mechanism for tracking content changes and index content that changed since the last sync.

   1. In **Sync run schedule**, for **Frequency**—Choose how often to sync your data source content and update your index.

   1. Choose **Next**.

1. On the **Set field mappings** page, enter the following information:

   1. Select from the Amazon Kendra generated default data source fields that you want to map to your index.

   1. To add custom data source fields, create an index field name to map to and the field data type.

   1. Choose **Next**.

1. On the **Review and create** page, check that the information you have entered is correct and then select **Add data source**. You can also choose to edit your information from this page. Your data source will appear on the **Data sources** page after the data source has been added successfully.

------
#### [ API ]

**To connect Amazon Kendra to Alfresco**

You must specify a JSON of the [data source schema](https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html#ds-alfresco-schema) using the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_TemplateConfiguration.html) API. You must provide the following information:
+ **Data source**—Specify the data source type as `ALFRESCO` when you use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_TemplateConfiguration.html) JSON schema. Also specify the data source as `TEMPLATE` when you call the [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/dg/API_CreateDataSource.html) API.
+ **Alfresco site ID**—Specify the Alfresco site ID.
+ **Alfresco repository URL**—Specify the Alfresco repository URL. You can get the repository URL from your Alfresco administrator. For example, if you use Alfresco Cloud (PaaS), the repository URL could be *https://company.alfrescocloud.com*. Or, if you use Alfresco On-Premises, the repository URL could be *https://company-alfresco-instance.company-domain.suffix:port*.
+ **Alfresco web application URL**—Specify the Alfresco user interface URL. You can get the repository URL from your Alfresco administrator. For example, the user interface URL could be *https://example.com*.
+ **Authentication type**—Specify which type of authentication you want to use, whether `OAuth2` or `Basic`.
+ **Alfresco type**—Specify which type of Alfresco you use, whether `PAAS` (Cloud/Platform as a Service) or `ON_PREM` (On-Premises).
+ **Secret Amazon Resource Name (ARN)**—If you want to use basic authentication, you provide a secret that stores your authentication credentials of your user name and password. You provide the Amazon Resource Name (ARN) of an AWS Secrets Manager secret. The secret is stored in a JSON structure with the following keys:

  ```
  {
      "username": "{{user name}}",
      "password": "{{password}}"
  }
  ```

  If you want to use OAuth 2.0 authentication, the secret is stored in a JSON structure with the following keys:

  ```
  {
      "clientId": "{{client ID}}",
      "clientSecret": "{{client secret}}",
      "tokenUrl": "{{token URL}}"
  }
  ```
+ **IAM role**—Specify `RoleArn` when you call `CreateDataSource` to provide an IAM role with permissions to access your Secrets Manager secret and to call the required public APIs for the Alfresco connector and Amazon Kendra. For more information, see [IAM roles for Alfresco data sources](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html#iam-roles-ds).

You can also add the following optional features:
+  **Virtual Private Cloud (VPC)**—Specify `VpcConfiguration` when you call `CreateDataSource`. For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md).
+ **Content type**—The type of content that you want to crawl, whether content marked with 'Aspects' in Alfresco, content within a specific Alfresco site, or content across all your Alfresco sites. You can also list specific 'Aspects' content.
+ **Inclusion and exclusion filters**—Specify whether to include or exclude certain files.
**Note**  
Most data sources use regular expression patterns, which are inclusion or exclusion patterns referred to as filters. If you specify an inclusion filter, only content that matches the inclusion filter is indexed. Any document that doesn’t match the inclusion filter isn’t indexed. If you specify an inclusion and exclusion filter, documents that match the exclusion filter are not indexed, even if they match the inclusion filter.
+ **Sync mode**—Specify how Amazon Kendra should update your index when your data source content changes. When you sync your data source with Amazon Kendra for the first time, all content is crawled and indexed by default. You must run a full sync of your data if your initial sync failed, even if you don't choose full sync as your sync mode option. You can choose between:
  + `FORCED_FULL_CRAWL` to freshly index all content, replacing existing content each time your data source syncs with your index.
  + `FULL_CRAWL` to index only new, modified, and deleted content each time your data source syncs with your index. Amazon Kendra can use your data source’s mechanism for tracking content changes and index content that changed since the last sync.
+ **Identity crawler**—Specify whether to turn on Amazon Kendra’s identity crawler. The identity crawler uses the access control list (ACL) information for your documents to filter search results based on the user or their group access to documents. If you have an ACL for your documents and choose to use your ACL, you can then also choose to turn on Amazon Kendra’s identity crawler to configure [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html#context-filter-user-incl-datasources) of search results. Otherwise, if identity crawler is turned off, all documents can be publicly searched. If you want to use access control for your documents and identity crawler is turned off, you can alternatively use the [PutPrincipalMapping](https://docs.aws.amazon.com/kendra/latest/APIReference/API_PutPrincipalMapping.html) API to upload user and group access information for user context filtering.
+  **Field mappings**—Choose to map your Alfresco data source fields to your Amazon Kendra index fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html).
**Note**  
The document body field or the document body equivalent for your documents is required in order for Amazon Kendra to search your documents. You must map your document body field name in your data source to the index field name `_document_body`. All other fields are optional.

For a list of other important JSON keys to configure, see [Alfresco template schema](https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html#ds-alfresco-schema).

------

## Learn more
<a name="alfresco-learn-more"></a>

To learn more about integrating Amazon Kendra with your Alfresco data source, see:
+ [Intelligently search Alfresco content using Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/intelligently-search-alfresco-content-using-amazon-kendra/)