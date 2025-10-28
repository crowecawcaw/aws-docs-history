# Amazon Kendra Web Crawler

You can use Amazon Kendra Web Crawler to crawl and index web pages.

You can only crawl public facing websites or internal company websites that use the secure
communication protocol Hypertext Transfer Protocol Secure (HTTPS). If you receive an error
when crawling a website, it could be that the website is blocked from crawling. To crawl
internal websites, you can set up a web proxy. The web proxy must be public facing. You can
also use authentication to access and crawl websites.

_When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/ "https://aws.amazon.com/aup/") and all other
Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index
your own web pages, or web pages that you have authorization to index. To learn how to
stop Amazon Kendra Web Crawler from indexing your website(s), please see [Configuring the robots.txt file for
Amazon Kendra Web Crawler](stop-web-crawler.md "stop-web-crawler.md")._

###### Note

Abusing Amazon Kendra Web Crawler to aggressively crawl websites or web pages you
don't own is **not** considered acceptable use.

Amazon Kendra has two versions of the web crawler connector.
Supported features of each version include:

**Amazon Kendra Web Crawler connector v1.0 / [WebCrawlerConfiguration](API_WebCrawlerConfiguration.md "API_WebCrawlerConfiguration.md") API**

- Web proxy
- Inclusion/exclusion filters
  **Amazon Kendra Web Crawler connector v2.0 / [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API**

- Field mappings
- Inclusion/exclusion filters
- Full and incremental content syncs
- Web proxy
- Basic, NTLM/Kerberos, SAML, and form authentication for your
  websites
- Virtual private cloud (VPC)

###### Important

Web Crawler v2.0 connector creation is not supported by AWS CloudFormation. Use the
Web Crawler v1.0 connector if you need AWS CloudFormation support.

For troubleshooting your Amazon Kendra web crawler data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Amazon Kendra Web Crawler
  connector v1.0](data-source-v1-web-crawler.md "data-source-v1-web-crawler.md")
- [Amazon Kendra Web Crawler
  connector v2.0](data-source-v2-web-crawler.md "data-source-v2-web-crawler.md")
- [Configuring the robots.txt file for
  Amazon Kendra Web Crawler](stop-web-crawler.md "stop-web-crawler.md")
