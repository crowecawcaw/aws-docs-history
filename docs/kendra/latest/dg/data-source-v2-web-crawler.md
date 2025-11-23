# Amazon Kendra Web Crawler

connector v2.0

You can use Amazon Kendra Web Crawler to crawl and index web pages.

You can only crawl public facing websites or internal company websites that use the
secure communication protocol Hypertext Transfer Protocol Secure (HTTPS). If you receive
an error when crawling a website, it could be that the website is blocked from crawling.
To crawl internal websites, you can set up a web proxy. The web proxy must be public
facing. You can also use authentication to access and crawl websites.

Amazon Kendra Web Crawler v2.0 uses the Selenium web crawler package and a
Chromium driver. Amazon Kendra automatically updates the version of Selenium and
the Chromium driver using Continuous Integration (CI).

_When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") and all
other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler
to index your own web pages, or web pages that you have authorization to index. To
learn how to stop Amazon Kendra Web Crawler from indexing your website(s),
please see [Configuring the robots.txt file for
Amazon Kendra Web Crawler](stop-web-crawler.md "stop-web-crawler.md")._. Abusing Amazon Kendra Web Crawler to aggressively crawl
websites or web pages you don't own is **not** considered
acceptable use.

For troubleshooting your Amazon Kendra web crawler data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Note

Web Crawler connector v2.0 does _not_ support crawling web site
lists from AWS KMS encrypted Amazon S3 buckets. It supports only
server-side encryption with Amazon S3 managed keys.

###### Important

Web Crawler v2.0 connector creation is not supported by CloudFormation. Use
the Web Crawler v1.0 connector if you need CloudFormation support.

###### Topics

- [Supported features](#supported-features-v2-web-crawler "#supported-features-v2-web-crawler")
- [Prerequisites](#prerequisites-v2-web-crawler "#prerequisites-v2-web-crawler")
- [Connection
  instructions](#data-source-v2-procedure-web-crawler "#data-source-v2-procedure-web-crawler")

## Supported features

- Field mappings
- Inclusion/exclusion filters
- Full and incremental content syncs
- Web proxy
- Basic, NTLM/Kerberos, SAML, and form authentication for your
  websites
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your websites, check the details of
your websites and AWS accounts.

**For your websites, make sure you have:**

- Copied the seed or sitemap URLs of the websites you want to index. You can
  store the URLs in a text file and upload this to an Amazon S3
  bucket. Each URL in the text file must be formatted on a separate line. If
  you want to store your sitemaps in an Amazon S3 bucket, make sure
  you have copied the sitemap XML and saved this in an XML file. You can also
  club multiple sitemap XML files into a ZIP file.

###### Note

(On-premise/server) Amazon Kendra checks if the endpoint information included in
AWS Secrets Manager is the same the endpoint information specified in your data source
configuration details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a
security issue where a user doesn’t have permission to perform an action but uses
Amazon Kendra as a proxy to access the configured secret and perform the action. If you
later change your endpoint information, you must create a new secret to sync this
information.

- **For websites that require basic, NTLM, or Kerberos
  authentication**:
  - Noted your website authentication credentials, which include a
    user name and password.

  ###### Note

  Amazon Kendra Web Crawler v2.0 supports the NTLM
  authentication protocol that includes password hashing, and
  Kerberos authentication protocol that includes password
  encryption.

- **For websites that require SAML or login form
  authentication**:
  - Noted your website authentication credentials, which include a
    user name and password.
  - Copied the XPaths (XML Path Language) of the user name field (and
    the user name button if using SAML), password field and button, and
    copied the login page URL. You can find the XPaths of elements using
    your web browser’s developer tools. XPaths usually follow this
    format: `//tagname[@Attribute='Value']`.

  ###### Note

  Amazon Kendra Web Crawler v2.0 uses a headless Chrome
  browser and the information from the form to authenticate and
  authorize access with an OAuth 2.0 protected URL.

- **Optional**: Copied the host name and the
  port number of the web proxy server if you want to use a web proxy to
  connect to internal websites you want to crawl. The web proxy must be public
  facing. Amazon Kendra supports connecting to web proxy servers that are
  backed by basic authentication or you can connect with no
  authentication.
- **Optional**: Copied the virtual private
  cloud (VPC) subnet ID if you want to use a VPC to connect to internal
  websites you want to crawl. For more information, see [Configuring an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- Checked each web page document you want to index is unique and across
  other data sources you plan to use for the same index. Each data source that
  you want to use for an index must not contain the same document across the
  data sources. Document IDs are global to an index and must be unique per
  index.

**In your AWS account, make sure you
have:**

- [Created an Amazon Kendra index](create-index.md "create-index.md") and, if using the API,
  noted the index ID.
- [Created an IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the API,
  noted the Amazon Resource Name of the IAM role.

###### Note

If you change your authentication type and credentials, you must
update your IAM role to access the correct AWS Secrets Manager secret ID.

- For websites that require authentication, or if using a web proxy with
  authentication, stored your authentication credentials in an AWS Secrets Manager secret and, if using the API, noted the ARN of the
  secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

If you don't have an existing IAM role or secret, you can use the
console to create a new IAM role and Secrets Manager secret when
you connect your web crawler data source to Amazon Kendra. If you are using the API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection

instructions

To connect Amazon Kendra to your web crawler data
source, you must provide the necessary details of your
web crawler data source so that Amazon Kendra can
access your data. If you have not yet configured web crawler
for Amazon Kendra see [Prerequisites](#prerequisites-v2-web-crawler "#prerequisites-v2-web-crawler").

Console
**To connect Amazon Kendra to
web crawler**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **web crawler connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **web crawler connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security**
    page, enter the following information:
    1. **Source**—Choose either
       **Source URLs**, **Source
       sitemaps**, **Source URLs
       file**, **Source sitemaps
       file**. If you choose to use a text file
       that includes a list of up to 100 seed URLs, you
       specify the path to the Amazon S3 bucket
       where your file is stored. If you choose to use a
       sitemap XML file, you specify the path to the
       Amazon S3 bucket where your file is
       stored. You can also club multiple sitemap XML files
       into a ZIP file. Otherwise, you can manually enter
       up to 10 seed or starting point URLs, and up to
       three sitemap URLs.

    ###### Note

    If you want to crawl a sitemap, check that the
    base or root URL is the same as the URLs listed on
    your sitemap page. For example, if your sitemap
    URL is
    *https://example.com/sitemap-page.html*,
    the URLs listed on this sitemap page should also
    use the base URL
    "https://example.com/".

    If your websites require authentication to access
    the websites, you can choose ether basic,
    NTLM/Kerberos, SAML, or form authentication.
    Otherwise, choose the option for no
    authentication.

    ###### Note

    If you want to later edit your data source to
    change your seed URLs with authentication to
    sitemaps, you must create a new data source.
    Amazon Kendra configures the data source
    using the seed URLs endpoint information in the
    Secrets Manager secret for authentication, and
    therefore cannot re-configure the data source when
    changing to sitemaps.

        1. **AWS Secrets Manager
         secret**—If your websites require
         the same authentication to access the websites,
         choose an existing secret or create a new Secrets Manager secret to store your website
         credentials. If you choose to create a new secret,
         an AWS Secrets Manager secret window
         opens.


        If you chose **Basic** or
         **NTML/Kerberos** authentication,
         enter a name for the secret, plus the user name
         and password. NTLM authentication protocol
         includes password hashing, and Kerberos
         authentication protocol includes password
         encryption.


        If you chose **SAML** or
         **Form** authentication, enter a
         name for the secret, plus the user name and
         password. Use XPath for the user name field (and
         XPath for the user name button if using SAML). Use
         XPaths for the password field and button, and
         login page URL. You can find the XPaths (XML Path
         Language) of elements using your web browser's
         developer tools. XPaths usually follow this
         format:
         `//tagname[@Attribute='Value']`.

    2. (Optional) **Web
       proxy**—Enter the host name and the
       port number of the proxy sever you want to use to
       connect to internal websites. For example, the host
       name of
       *https://a.example.com/page1.html*
       is "a.example.com" and the port
       number is is 443, the standard port for HTTPS. If
       web proxy credentials are required to connect to a
       website host, you can create an AWS Secrets Manager that stores the credentials.
    3. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    4. **IAM role**—Choose an existing IAM
       role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 5. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. **Sync scope**—Set limits
       for crawling web pages including their domains, file
       sizes and links; and filter URLs using regex
       patterns.
       1. (Optional) **Crawl domain
          range**—Choose whether to crawl
          website domains only, domains with subdomains, or
          also crawl other domains that the web pages link
          to. By default, Amazon Kendra only crawls the
          domains of the websites you want to crawl.
       2. (Optional) **Additional
          configuration**—Set the following
          settings:
          - **Crawl depth**—The
            'depth' or number of levels from the seed level to
            crawl. For example, the seed URL page is depth 1
            and any hyperlinks on this page that are also
            crawled are depth 2.
          - **Maximum file
            size**—The maximum size in MB of a
            web page or attachment to crawl.
          - **Maximum links per
            page**—The maximum number of URLs
            on a single webpage to crawl.
          - **Maximum throttling of crawling
            speed**—The maximum number of URLs
            crawled per website host per minute.
          - **Files**—Choose to
            crawl files that the web pages link to.
          - **Crawl and index
            URLs**—Add regular expression
            patterns to include or exclude crawling certain
            URLs, and indexing any hyperlinks on these URL web
            pages.

    2. **Sync mode**—Choose how you want to update
       your index when your data source content changes. When you sync your
       data source with Amazon Kendra for the first time, all content
       is crawled and indexed by default. You must run a full sync of your
       data if your initial sync failed, even if you don't choose full sync
       as your sync mode option.
       - Full sync: Freshly index all content, replacing existing
         content each time your data source syncs with your index.
       - New, modified, deleted sync: Index only new, modified,
         and deleted content each time your data source syncs with
         your index. Amazon Kendra can use your data source's
         mechanism for tracking content changes and index content
         that changed since the last sync.

    3. **Sync run schedule**—For
       **Frequency**, choose how often
       Amazon Kendra will sync with your data
       source.
    4. Choose **Next**.

8.  On the **Set field mappings** page, enter
    the following information:
    1. Select from the Amazon Kendra generated
       default fields of web pages and files that you want
       to map to your index.
    2. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
web crawler**

You must specify a JSON of the [data source schema](ds-schemas.md#ds-web-crawler-schema "ds-schemas.md#ds-web-crawler-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `WEBCRAWLERV2` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **URLs**—Specify the
  seed or starting point URLs of the websites or the sitemap
  URLs of the websites you want to crawl. You can specify the
  path to an Amazon S3 bucket that stores your list of
  seed URLs. Each URL in the text file for seed URLs must be
  formatted on a separate line. You can also specify the path
  to an Amazon S3 bucket that stores your sitemap XML
  files. You can club together multiple sitemap files into a
  ZIP file and store the ZIP file in your Amazon S3
  bucket.

###### Note

If you want to crawl a sitemap, check that the base or
root URL is the same as the URLs listed on your sitemap
page. For example, if your sitemap URL is
*https://example.com/sitemap-page.html*,
the URLs listed on this sitemap page should also use the
base URL "https://example.com/".

- **Sync mode**—Specify
  how Amazon Kendra should update your index when your data source
  content changes. When you sync your data source with Amazon Kendra
  for the first time, all content is crawled and indexed by default.
  You must run a full sync of your data if your initial sync failed,
  even if you don't choose full sync as your sync mode option. You can
  choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content,
    replacing existing content each time your data source syncs with
    your index.
  - `FULL_CRAWL` to index only new, modified, and deleted
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.

- **Authentication**—If
  your websites require the same authentication, specify
  either `BasicAuth`,
  `NTLM_Kerberos`,
  `SAML`, or
  `Form` authentication. If
  your websites don't require authentication, specify
  `NoAuthentication`.
- **Secret Amazon Resource Name
  (ARN)**—If your websites require basic,
  NTLM, or Kerberos authentication, you provide a secret that
  stores your authentication credentials of your user name and
  password. You provide the Amazon Resource Name (ARN) of an
  AWS Secrets Manager secret. The secret is stored in a
  JSON structure with the following keys:

```
{
    "seedUrlsHash": "`Hash representation of all seed URLs`",
    "userName": "`user name`",
    "password": "`password`"
}
```

If your websites require SAML authentication, the secret
is stored in a JSON structure with the following
keys:

```
{
    "seedUrlsHash": "`Hash representation of all seed URLs`",
    "userName": "`user name`",
    "password": "`password`",
    "userNameFieldXpath": "`XPath for user name field`",
    "userNameButtonXpath": "`XPath for user name button`",
    "passwordFieldXpath": "`XPath for password field`",
    "passwordButtonXpath": "`XPath for password button`",
    "loginPageUrl": "`Full URL for website login page`"
}
```

If your websites require form authentication, the secret
is stored in a JSON structure with the following
keys:

```
{
    "seedUrlsHash": "`Hash representation of all seed URLs`",
    "userName": "`user name`",
    "password": "`password`",
    "userNameFieldXpath": "`XPath for user name field`",
    "passwordFieldXpath": "`XPath for password field`",
    "passwordButtonXpath": "`XPath for password button`",
    "loginPageUrl": "`Full URL for website login page`"
}
```

You can find the XPaths (XML Path Language) of elements
using your web browser's developer tools. XPaths usually
follow this format:
`//tagname[@Attribute='Value']`.

You can also provide web proxy credentials using and
AWS Secrets Manager secret.

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the web crawler connector and Amazon Kendra.
  For more information, see [IAM roles for web crawler
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Domain
  range**—Choose whether to crawl website
  domains with subdomains only, or also crawl other domains
  the web pages link to. By default, Amazon Kendra only
  crawls the domains of the websites you want to crawl.
- The 'depth' or number of levels from the seed level to
  crawl. For example, the seed URL page is depth 1 and any
  hyperlinks on this page that are also crawled are depth

2.

- The maximum number of URLs on a single web page to
  crawl.
- The maximum size in MB of a web page or attachment to
  crawl.
- The maximum number of URLs crawled per website host per
  minute.
- The web proxy host and port number to connect to and crawl
  internal websites. For example, the host name of
  *https://a.example.com/page1.html*
  is "a.example.com" and the port number is is
  443, the standard port for HTTPS. If web proxy credentials
  are required to connect to a website host, you can create an
  AWS Secrets Manager that stores the
  credentials.
- **Inclusion and exclusion
  filters**—Specify whether to include or
  exclude crawling certain URLs and indexing any hyperlinks on
  these URL web pages.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field
  mappings**—Choose to map the fields of web
  pages and web page files to your Amazon Kendra index
  fields. For more information, see [Mapping data
  source fields](field-mapping.md "field-mapping.md").

For a list of other important JSON keys to configure, see [Amazon Kendra Web Crawler template
schema](ds-schemas.md#ds-schema-web-crawler "ds-schemas.md#ds-schema-web-crawler").
