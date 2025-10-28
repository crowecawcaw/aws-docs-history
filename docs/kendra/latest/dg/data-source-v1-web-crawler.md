# Amazon Kendra Web Crawler

connector v1.0

You can use Amazon Kendra Web Crawler to crawl and index web pages.

You can only crawl public facing websites and websites that use the secure
communication protocol Hypertext Transfer Protocol Secure (HTTPS). If you receive an
error when crawling a website, it could be that the website is blocked from crawling. To
crawl internal websites, you can set up a web proxy. The web proxy must be public
facing.

_When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") and all
other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler
to index your own web pages, or web pages that you have authorization to index. To
learn how to stop Amazon Kendra Web Crawler from indexing your website(s),
please see [Configuring the robots.txt file for
Amazon Kendra Web Crawler](stop-web-crawler.md "stop-web-crawler.md")._

###### Note

Abusing Amazon Kendra Web Crawler to aggressively crawl websites or web pages
you don't own is **not** considered acceptable
use.

For troubleshooting your Amazon Kendra web crawler data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-web-crawler "#supported-features-v1-web-crawler")
- [Prerequisites](#prerequisites-v1-web-crawler "#prerequisites-v1-web-crawler")
- [Connection
  instructions](#data-source-v1-procedure-web-crawler "#data-source-v1-procedure-web-crawler")
- [Learn more](#web-crawler-learn-more "#web-crawler-learn-more")

## Supported features

- Web proxy
- Inclusion/exclusion filters

## Prerequisites

Before you can use Amazon Kendra to index your websites, check the details of
your websites and AWS accounts.

**For your websites, make sure you have:**

- Copied the seed or sitemap URLs of the websites you want to index.
- **For websites that require basic
  authentication**: Noted the user name and password, and copied
  the host name of the website and the port number.
- **Optional:** Copied the host name of the
  website and the port number if you want to use a web proxy to connect to
  internal websites you want to crawl. The web proxy must be public facing.
  Amazon Kendra supports connecting to web proxy servers that are
  backed by basic authentication or you can connect with no
  authentication.
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
  noted the ARN of the IAM role.

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
for Amazon Kendra see [Prerequisites](#prerequisites-v1-web-crawler "#prerequisites-v1-web-crawler").

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
    1. For **Source**, choose between
       **Source URLs** and
       **Source sitemaps** depending on
       your use case and enter the values for each.

    You can add up to 10 source URLs and three
    sitemaps.

    ###### Note

    If you want to crawl a sitemap, check that the
    base or root URL is the same as the URLs listed on
    your sitemap page. For example, if your sitemap
    URL is
    *https://example.com/sitemap-page.html*,
    the URLs listed on this sitemap page should also
    use the base URL
    "https://example.com/". 2. (Optional) For **Web
    proxy**— enter the following
    information:

        1. **Host name**—The
         host name where web proxy is required.
        2. **Port number**—The
         port used by the host URL transport protocol. The
         port number should be a numeric value between 0
         and 65535.
        3. For **Web proxy
         credentials**—If your web proxy
         connection requires authentication, choose an
         existing secret or create a new secret to store
         your authentication credentials. If you choose to
         create a new secret an AWS Secrets Manager
         secret window opens.
        4. Enter the following information in the
         **Create an AWS Secrets Manager
         Secrets Manager secret
         window**:


        	1. **Secret name**—A
        	 name for your secret. The prefix
        	 ‘AmazonKendra-WebCrawler-’ is
        	 automatically added to your secret name.
        	2. For **User name** and
        	 **Password**—Enter these
        	 basic authentication credentials for your
        	 websites.
        	3. Choose **Save**.

    3. (Optional) **Hosts with
       authentication**—Select to add
       additional hosts with authentication.
    4. **IAM role**—Choose an existing IAM
       role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 5. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. **Crawl range**—Choose the
       kind of web pages you want to crawl.
    2. **Crawl depth**—Select
       number of levels from the seed URL that Amazon Kendra should crawl.
    3. **Advanced crawl settings** and
       **Additional configuration**enter
       the following information:
       1. **Maximum file
          size**—The maximum web page or
          attachment size to crawl. Minimum 0.000001 MB (1
          byte). Maximum 50 MB.
       2. **Maximum links per
          page**—The maximum number of links
          crawled per page. Links are crawled in order of
          appearance. Minimum 1 link/page. Maximum 1000
          links/page.
       3. **Maximum
          throttling**—The maximum number of
          URLs crawled per host name per minute. Minimum 1
          URLs/host name/minute. Maximum 300 URLs/host
          name/minute.
       4. **Regex
          patterns**—Add regular expression
          patterns to include or exclude certain URLs. You
          can add up to 100 patterns.

    4. In **Sync run schedule**, for
       **Frequency**—Choose how
       often Amazon Kendra will sync with your data
       source.
    5. Choose **Next**.

8.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
web crawler**

You must specify the following using the [WebCrawlerConfiguration](API_WebCrawlerConfiguration.md "API_WebCrawlerConfiguration.md") API:

- **URLs**—Specify the
  seed or starting point URLs of the websites or the sitemap
  URLs of the websites you want to crawl using [SeedUrlConfiguration](API_SeedUrlConfiguration.md "API_SeedUrlConfiguration.md") and
  [SiteMapsConfiguration](API_SiteMapsConfiguration.md "API_SiteMapsConfiguration.md").

###### Note

If you want to crawl a sitemap, check that the base or
root URL is the same as the URLs listed on your sitemap
page. For example, if your sitemap URL is
*https://example.com/sitemap-page.html*,
the URLs listed on this sitemap page should also use the
base URL "https://example.com/".

- **Secret Amazon Resource Name
  (ARN)**—If a website requires basic
  authentication, you provide the host name, port number and a
  secret that stores your basic authentication credentials of
  your user name and password. You provide the secret ARN
  using the [AuthenticationConfiguration](API_AuthenticationConfiguration.md "API_AuthenticationConfiguration.md")
  API. The secret is stored in a JSON structure with the
  following keys:

```
{
    "username": `"user name"`,
    "password": `"password"`
}
```

You can also provide web proxy credentials using an
AWS Secrets Manager secret. You use the [ProxyConfiguration](API_ProxyConfiguration.md "API_ProxyConfiguration.md") API to
provide the website host name and port number, and
optionally the secret that stores your web proxy
credentials.

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the web crawler connector and Amazon Kendra.
  For more information, see [IAM roles for web crawler
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Crawl mode**—Choose
  whether to crawl website host names only, or host names with
  subdomains, or also crawl other domains the web pages link
  to.
- The 'depth' or number of levels from the seed level to
  crawl. For example, the seed URL page is depth 1 and any
  hyperlinks on this page that are also crawled are depth

2.

- The maximum number of URLs on a single web page to
  crawl.
- The maximum size in MB of a web page to crawl.
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
- The authentication information to access and crawl
  websites that require user authentication.
- You can extract HTML meta tags as fields using the
  _Custom Document Enrichment_ tool.
  For more information, see [Customizing document metadata during the ingestion
  process](custom-document-enrichment.md "custom-document-enrichment.md"). For an example of extracting HTML meta
  tags, see [CDE examples](https://github.com/aws-samples/amazon-kendra-cde-examples "https://github.com/aws-samples/amazon-kendra-cde-examples").
- **Inclusion and exclusion
  filters**—Specify whether to include or
  exclude certain URLs.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

## Learn more

To learn more about integrating Amazon Kendra with your
web crawler data source, see:

- [Reimagine knowledge discovery using Amazon Kendra's Web
  Crawler](https://aws.amazon.com/blogs/machine-learning/reimagine-knowledge-discovery-using-amazon-kendras-web-crawler/ "https://aws.amazon.com/blogs/machine-learning/reimagine-knowledge-discovery-using-amazon-kendras-web-crawler/")
