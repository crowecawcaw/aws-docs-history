

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Web Crawler to Amazon Q Business
<a name="connector-webcrawler"></a>

An Amazon Q Business Web Crawler connector crawls and indexes either public facing websites or internal company websites that use HTTPS. With Amazon Q web crawler, you can create a generative AI web experience for your end users based on the website data you crawl using either the AWS Management Console or the [`CreateDataSource`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) API.

**Note**  
Amazon Q Web Crawler supports only HTTPS enabled sites. It doesn't support HTTP or self-signed certificate enabled websites.

**Important**  
When selecting websites to index, you must adhere to the [Amazon Acceptable Use Policy](https://aws.amazon.com/aup/) and all other Amazon terms. Remember that you must only use Amazon Q Web Crawler to index your own webpages, or webpages that you have authorization to index. To learn how to stop Amazon Q Web Crawler from indexing your websites, see [Configuring a `robots.txt` file for Amazon Q Business Web Crawler](stop-web-crawler.md).

If you receive an error when crawling a website, it could be that the website is blocked from crawling. To crawl internal websites, you can set up a web proxy. The web proxy must be public facing. You can also use authentication to access and crawl websites.

**Note**  
Amazon Q Web Crawler connector does *not* support AWS KMS encrypted Amazon S3 buckets. It supports only server-side encryption with Amazon S3 managed keys.

**Topics**
+ [Web Crawler connector overview](webcrawler-overview.md)
+ [Prerequisites for connecting Amazon Q Business to Web Crawler](webcrawler-prereqs.md)
+ [Retrieving XPaths (XML Path Language) for Web Crawler](webcrawler-retrieving-credentials.md)
+ [Connecting Amazon Q Business to Web Crawler using the console](webcrawler-console.md)
+ [Connecting Amazon Q Business to Web Crawler using APIs](web-crawler-api.md)
+ [Connecting Amazon Q Business to Web Crawler using AWS CloudFormation](web-crawler-cfn.md)
+ [Web Crawler data source connector field mappings](web-crawler-field-mappings.md)
+ [IAM role for Amazon Q Business Web Crawler connector](webcrawler-iam-role.md)
+ [Configuring a `robots.txt` file for Amazon Q Business Web Crawler](stop-web-crawler.md)

**Learn more**
+ For an overview of the Amazon Q web experience creation process using IAM Identity Center, see [Configuring an application using IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html).
+ For an overview of the Amazon Q web experience creation process using AWS Identity and Access Management, see [Configuring an application using IAM](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).
+ For an overview of connector features, see [Data source connector concepts](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html).
+ For information about connector configuration best practices, see [Connector configuration best practices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-best-practices.html).