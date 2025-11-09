# Connecting Amazon Q Business to Web Crawler

using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _AWS CloudFormation User Guide_.

###### Topics

- [Web Crawler configuration
  properties](#web-crawler-configuration-keys "#web-crawler-configuration-keys")
- [Web Crawler JSON schema for using the
  configuration property with AWS CloudFormation](#web-crawler-cfn-json "#web-crawler-cfn-json")
- [Web Crawler YAML schema for using the
  configuration property with AWS CloudFormation](#web-crawler-cfn-yaml "#web-crawler-cfn-yaml")

## Web Crawler configuration

properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `type`                                                         | The type of data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>The only allowed values are<br>• `WEBCRAWLERV2`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `syncMode`                                                     | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `connectionConfiguration`                                      | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `object`<br>This property has the sub-property `repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `repositoryEndpointMetadata`                                   | The endpoint information for the data source. This is a sub-property for the<br>`connectionConfiguration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `object`<br>This property has the following sub-properties<br>• `authentication`<br>• `seedUrlConnections`<br>• `s3SeedUrl`<br>• `siteMapUrls`<br>• `s3SiteMapUrl`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `authentication`                                               | The authentication type if your websites require the same authentication.<br>This is a sub-property for the `repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`<br>Depending on your connection type, the allowed values are<br>`NoAuthentication`, `BasicAuth`, `NTLM_Kerberos`,<br>`Form`, `SAML`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `seedUrlConnections`                                           | The list of seed or starting point URLs for the websites that you want to<br>crawl. You can list up to 100 seed URLs. This is a sub-property for the<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `array`<br>This is an array of `seedUrl`s. Use the pattern:<br>[`https://.*`].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No       |
| `seedUrl`                                                      | The seed or starting point URL for the websites that you want to crawl. This<br>is a sub-property for the `seedUrlConnections`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `string`<br>Use the pattern: [`https://.*`].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `s3SeedUrl`                                                    | The S3 path to the text file that stores the list of seed or starting point<br>URLs. This is a sub-property for the `repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string`<br>Use the pattern _`s3://bucket-name/directory/`_. Each URL in the text file must be formatted on a separate line. You can<br>list up to 100 seed URLs in a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |
| `siteMapUrls`                                                  | The list of sitemap URLs for the websites that you want to crawl. This is a<br>sub-property for the `repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `array`<br>This is an array of `siteMapUrls`. You can list up to three sitemap<br>URLs. Use the pattern: [`https://.*`].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `s3SiteMapUrl`                                                 | The S3 path to the sitemap XML files. This is a sub-property for the<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>Use the pattern, _s3://bucket-name/directory/_.<br>You can list up to three sitemap XML files. You can club together multiple sitemap<br>files into a .zip file and store the .zip file in your Amazon S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `repositoryConfigurations`                                     | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `object`<br>This property has the following sub-properties<br>• `webPage`<br>• `attachment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| • `webPage`<br>• `attachments`                                 | A list of objects that map the attributes or field names of your webpages and<br>attachments to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `object`<br>These properties has the following sub-properties<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |
| `indexFieldName`                                               | The name of the index field. This is a sub-property for `webPage`<br>and `attachments`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `indexFieldType`                                               | The type of the index field. This is a sub-property for `webPage`<br>and `attachments`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `string`<br>The only allowed value are<br>• `STRING`<br>• `DATE`<br>• `LONG`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `dataSourceFieldName`                                          | The field name of the data source. This is a sub-property for<br>`webPage` and `attachments`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `dateFieldFormat`                                              | The field date of the data source. This is a sub-property for<br>`webPage` and `attachments`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`<br>Use the pattern `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No       |
| `additionalProperties`                                         | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `object`This property has the following<br>sub-properties that are not required<br>• `rateLimit`<br>• `metadataFilesPrefix`.<br>• `maxFileSize`<br>• `maxFileSizeInMegaBytes`<br>• `crawlDepth`<br>• `maxLinksPerUrl`<br>• `honorRobots`<br>• `crawlSubDomain`<br>• `crawlAllDomain`<br>• `crawlAttachments`<br>• `maxFileSizeInMegaBytes`<br>• `inclusionURLCrawlPatterns`<br>• `exclusionURLCrawlPatterns`<br>• `inclusionURLIndexPatterns`<br>• `exclusionURLIndexPatterns`<br>• `inclusionFileIndexPatterns`<br>• `exclusionFileIndexPatterns`<br>• `proxy`                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `rateLimit`                                                    | The maximum number of URLs crawled per website host per minute. This is a<br>sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`<br>The default value is `300`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `maxFileSize`                                                  | The maximum size (in MB) of a webpage or attachment to crawl. This is a<br>sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`<br>The default value is `50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `crawlDepth`                                                   | The number of levels from the seed URL to crawl. This is a sub-property of<br>`additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>The seed URL page is depth `1` and any hyperlinks on this page that are<br>also crawled are depth `2`. The default value is<br>`2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `maxLinksPerUrl`                                               | The maximum number of URLs on a webpage to include when crawling a website.<br>This number is per webpage. As a website's webpages are crawled, any URLs that the<br>webpages link to also are crawled. URLs on a webpage are crawled in order of<br>appearance. This is a sub-property of<br>`additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>The default value is `100`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes      |
| `honorRobots`                                                  | `true` to respect the robots.txt directives of the websites that<br>you want to crawl. These directives control how Amazon Q Web Crawler crawls<br>the websites, and whether Amazon Q can crawl only specific content or not<br>crawl any content. This is a sub-property of `additionalProperties`.NoteThe `honorRobots` feature is currently only available if you use the<br>API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes      |
| `crawlSubDomain`                                               | `true` to crawl the website domains with subdomains only. This is<br>a sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `boolean`<br>If the seed URL is "abc.example.com", then<br>"a.abc.example.com" and "b.abc.example.com" are also<br>crawled. If you don't set `crawlSubDomain` or<br>`crawlAllDomain` to `true`, then Amazon Q only crawls the domains of the websites that you want to<br>crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `crawlAllDomain`                                               | Crawl the website domains with subdomains and other domains the web pages<br>link to. This is a sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `boolean`<br>If you don't set `crawlSubDomain` or<br>`crawlAllDomain` to `true`, then Amazon Q only crawls the domains of the websites that you want to<br>crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `crawlAttachments`                                             | `true` to crawl files that the webpages link to. This is a<br>sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes      |
| `maxFileSizeInMegaBytes`                                       | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. This is a<br>sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>The default value is `50`. The maximum file size should be greater than<br>`0` and less than or equal to `50`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| • `inclusionURLCrawlPatterns`<br>• `inclusionURLIndexPatterns` | These are sub-properties of `additionalProperties`. A list of regular<br>expression patterns to \*include<br>• crawling certain URLs and indexing<br>any hyperlinks on these URL webpages. URLs that match the patterns are included in the<br>index. URLs that don't match the patterns are excluded from the index. If a URL<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the URL and website's webpages aren't included in the<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `array`(`string`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| • `exclusionURLCrawlPatterns`<br>• `exclusionURLIndexPatterns` | These are sub-properties of `additionalProperties`. A list of<br>regular expression patterns to \*exclude<br>• crawling certain URLs and<br>indexing any hyperlinks on these URL webpages. URLs that match the patterns are<br>excluded from the index. URLs that don't match the patterns are included in the index.<br>If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the URL/website's webpages aren't included in the<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `array`(`string`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `inclusionFileIndexPatterns`                                   | This is a sub-property of `additionalProperties`. A list of<br>regular expression patterns to \*include<br>• certain web page files.<br>Files that match the patterns are included in the index. Files that don't match the<br>patterns are excluded from the index. If a file matches both an inclusion and<br>exclusion pattern, the exclusion pattern takes precedence, and the file isn't included<br>in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `array`(`string`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `exclusionFileIndexPatterns`                                   | This is a sub-property of `additionalProperties`. A list of<br>regular expression patterns to \*exclude<br>• certain webpage files.<br>Files that match the patterns are excluded from the index. Files that don't match the<br>patterns are included in the index. If a file matches both an inclusion and exclusion<br>pattern, the exclusion pattern takes precedence, and the file isn't included in the<br>index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `array`(`string`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `proxy`                                                        | This is a sub-property of `additionalProperties`. Configuration<br>information required to connect to your internal websites through a web<br>proxy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `host`                                                         | This is a sub-property of `proxy`. The host name of the proxy<br>server that you want to use to connect to internal websites.For example,<br>the host name of \*https://a.example.com/page1.html<br>• is `a.example.com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `port`                                                         | This is a sub-property of `proxy`. The port number of the proxy<br>server that you want to use to connect to internal websites.For example,<br>the port 443 would be `443`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `secretArn`                                                    | This is a sub-property of `proxy`. If web proxy credentials are<br>required to connect to a website host, you can create an AWS Secrets Manager secret<br>that stores the credentials. Provide the Amazon Resource Name (ARN) of the<br>secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `string`<br>The minimum length is 20and the maximum length is 2,048 characters<br>The JSON structure for this is<br>`<br>{<br>"userName": string,<br>"password": string<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `secretArn`                                                    | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that's used if<br>your websites require authentication to access the websites. You store the<br>authentication credentials for the website in the secret that contains JSON key-value<br>pairs.<br>If you use basic, or NTLM/Kerberos, enter the username and password. The JSON keys<br>in the secret must be `userName` and<br>`password`. NTLM authentication protocol includes<br>password hashing, and Kerberos authentication protocol includes password<br>encryption.<br>If you use SAML or form authentication, enter the username and password, XPath for<br>the username field (and username button if using SAML), XPaths for the password field<br>and button, and the login page URL. The JSON keys in the secret must be<br>`userName`, `password`,<br>`userNameFieldXpath`,<br>`userNameButtonXpath`,<br>`passwordFieldXpath`,<br>`passwordButtonXpath`, and<br>`loginPageUrl`. You can find the XPaths (XML Path<br>Language) of elements using your web browser's developer tools. XPaths usually follow<br>this format: `//tagname[@Attribute='Value']`.<br>Amazon Q also checks if the endpoint information (seed URLs) included<br>in the secret is the same the endpoint information specified in your data source<br>endpoint configuration details. | If you use `seedUrlConnections` or `s3SeedUrl` as the<br>connection type, you can choose from all authentication values<br>(`NoAuthentication`, `BasicAuth`, `NTLM_Kerberos`,<br>`Form`, `SAML`) depending on the use case.<br>If you use `siteMapUrls` or `s3SiteMapUrl` as connection<br>type, the `authentication` should be `NoAuthentication`.<br>You must use the following JSON structure for your `authentication`<br>values.<br>• For `BasicAuth`/`NTLM_Kerberos`<br>`<br>{<br>"userName": String,<br>"password": String<br>}<br>`<br>• For `Form`/`SAML`<br>`<br>{<br>"loginPageUrl": String,<br>"userName": String,<br>"password": String,<br>"userNameFieldXpath": String,<br>"passwordFieldXpath": String,<br>"userNameButtonXpath": String,<br>"passwordButtonXpath": String<br>}<br>`<br>NoteXML Path Language (XPaths) of elements can be found using the web browser's<br>developer tools. XPaths usually follow this format:<br>`//tagname[@Attribute='Value'`]. | No       |
| `version`                                                      | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>The default value is `1.0.0`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No       |
| `implicitWaitDuration`                                         | Specifies how long the connector will wait, in seconds, before crawling a<br>webpage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Range: 0-10<br>eg. "implicitWaitDuration": "5"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |          |

## Web Crawler JSON schema for using the

configuration property with AWS CloudFormation

The following is the Web Crawler JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Web Crawler JSON schema for using the
  configuration property with AWS CloudFormation](#web-crawler-cfn-json-schema "#web-crawler-cfn-json-schema")
- [Web Crawler JSON schema example for
  using the configuration property with AWS CloudFormation](#web-crawler-cfn-json-example "#web-crawler-cfn-json-example")

### Web Crawler JSON schema for using the

configuration property with AWS CloudFormation

The following is the Web Crawler JSON schema for the configuration property for
AWS CloudFormation

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": ["WEBCRAWLERV2"]
    },
    "syncMode": {
      "type": "string",
      "enum": ["FORCED_FULL_CRAWL", "FULL_CRAWL"]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "siteMapUrls": {
              "type": "array",
              "items": {
                "type": "string",
                "pattern": "https://.*"
              }
            },
            "s3SeedUrl": {
              "type": ["string", "null"],
              "pattern": "s3:.*"
            },
            "s3SiteMapUrl": {
              "type": ["string", "null"],
              "pattern": "s3:.*"
            },
            "seedUrlConnections": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "seedUrl": {
                      "type": "string",
                      "pattern": "https://.*"
                    }
                  },
                  "required": ["seedUrl"]
                }
              ]
            },
            "authentication": {
              "type": "string",
              "enum": [
                "NoAuthentication",
                "BasicAuth",
                "NTLM_Kerberos",
                "Form",
                "SAML"
              ]
            }
          }
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "webPage": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "DATE", "LONG"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": ["fieldMappings"]
        },
        "attachment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "indexFieldName": {
                      "type": "string"
                    },
                    "indexFieldType": {
                      "type": "string",
                      "enum": ["STRING", "DATE", "LONG"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
                    },
                    "dateFieldFormat": {
                      "type": "string",
                      "pattern": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                    }
                  },
                  "required": [
                    "indexFieldName",
                    "indexFieldType",
                    "dataSourceFieldName"
                  ]
                }
              ]
            }
          },
          "required": ["fieldMappings"]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "rateLimit": {
          "type": "string",
          "default": "300"
        },
        "maxFileSize": {
          "type": "string",
          "default": "50"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "crawlDepth": {
          "type": "string",
          "default": "2"
        },
        "maxLinksPerUrl": {
          "type": "string",
          "default": "100"
        },
        "crawlSubDomain": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ],
          "default": false
        },
        "crawlAllDomain": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ],
          "default": false
        },
        "honorRobots": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ],
          "default": false
        },
        "crawlAttachments": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ],
          "default": false
        },
        "inclusionURLCrawlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionURLCrawlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionURLIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionURLIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileIndexPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "proxy": {
          "type": "object",
          "properties": {
            "host": {
              "type": "string"
            },
            "port": {
              "type": "string"
            },
            "secretArn": {
              "type": "string",
              "minLength": 20,
              "maxLength": 2048
            }
          }
        },
        "enableDeletionProtection": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ],
          "default": false
        },
        "deletionProtectionThreshold": {
          "type": "string",
          "default": "15"
        }
      },
      "required": [
        "rateLimit",
        "maxFileSize",
        "crawlDepth",
        "crawlSubDomain",
        "crawlAllDomain",
        "maxLinksPerUrl",
        "honorRobots"
      ]
    }
  },
  "version": {
    "type": "string",
    "anyOf": [
      {
        "pattern": "1.0.0"
      }
    ]
  },
  "required": [
    "type",
    "syncMode",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

[Show moreShow less](# "#")

### Web Crawler JSON schema example for

using the configuration property with AWS CloudFormation

The following is the Web Crawler JSON schema example for the configuration
property for AWS CloudFormation

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "CloudFormation Web Crawler Data Source Template",
  "Resources": {
    "DataSourceWebCrawler": {
      "Type": "AWS::QBusiness::DataSource",
      "Properties": {
        "ApplicationId": "app12345-1234-1234-1234-123456789012",
        "IndexId": "indx1234-1234-1234-1234-123456789012",
        "DisplayName": "MyWebCrawlerDataSource",
        "RoleArn": "arn:aws:iam::123456789012:role/qbusiness-data-source-role",
        "Configuration": {
          "type": "WEBCRAWLERV2",
          "syncMode": "FULL_CRAWL",
          "secretArn": "arn:aws:secretsmanager:us-west-2:0123456789012:secret",
          "connectionConfiguration": {
            "repositoryEndpointMetadata": {
              "siteMapUrls": ["https://example.com/sitemap.xml"],
              "s3SeedUrl": "s3://bucket/seed-url",
              "s3SiteMapUrl": "s3://bucket/sitemap-url",
              "seedUrlConnections": [
                {
                  "seedUrl": "https://example.com"
                }
              ],
              "authentication": "BasicAuth"
            }
          },
          "repositoryConfigurations": {
            "webPage": {
              "fieldMappings": [
                {
                  "indexFieldName": "title",
                  "indexFieldType": "STRING",
                  "dataSourceFieldName": "page_title",
                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                }
              ]
            },
            "attachment": {
              "fieldMappings": [
                {
                  "indexFieldName": "attachment_title",
                  "indexFieldType": "STRING",
                  "dataSourceFieldName": "attachment_name",
                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
                }
              ]
            }
          },
          "additionalProperties": {
            "rateLimit": "300",
            "maxFileSize": "50",
            "crawlDepth": "2",
            "maxLinksPerUrl": "100",
            "crawlSubDomain": "true",
            "crawlAllDomain": "true",
            "honorRobots": "true"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")

## Web Crawler YAML schema for using the

configuration property with AWS CloudFormation

The following is the Web Crawler YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Web Crawler YAML schema for using the
  configuration property with AWS CloudFormation](#web-crawler-cfn-yaml-schema "#web-crawler-cfn-yaml-schema")
- [Web Crawler YAML schema example for
  using the configuration property with AWS CloudFormation](#web-crawler-cfn-yaml-example "#web-crawler-cfn-yaml-example")

### Web Crawler YAML schema for using the

configuration property with AWS CloudFormation

The following is the Web Crawler YAML schema for the configuration property for
AWS CloudFormation.

```
type: object
properties:
  type:
    type: string
    enum:
      - WEBCRAWLERV2
  syncMode:
    type: string
    enum:
      - FORCED_FULL_CRAWL
      - FULL_CRAWL
  secretArn:
    type: string
    minLength: 20
    maxLength: 2048
  connectionConfiguration:
    type: object
    properties:
      repositoryEndpointMetadata:
        type: object
        properties:
          siteMapUrls:
            type: array
            items:
              type: string
              pattern: https://.*
          s3SeedUrl:
            type:
              - string
              - null
            pattern: s3:.*
          s3SiteMapUrl:
            type:
              - string
              - null
            pattern: s3:.*
          seedUrlConnections:
            type: array
            items:
              type: object
              properties:
                seedUrl:
                  type: string
                  pattern: https://.*
              required:
                - seedUrl
          authentication:
            type: string
            enum:
              - NoAuthentication
              - BasicAuth
              - NTLM_Kerberos
              - Form
              - SAML
    required:
      - repositoryEndpointMetadata
  repositoryConfigurations:
    type: object
    properties:
      webPage:
        type: object
        properties:
          fieldMappings:
            type: array
            items:
              type: object
              properties:
                indexFieldName:
                  type: string
                indexFieldType:
                  type: string
                  enum:
                    - STRING
                    - DATE
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: yyyy-MM-dd'T'HH:mm:ss'Z'
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
      attachment:
        type: object
        properties:
          fieldMappings:
            type: array
            items:
              type: object
              properties:
                indexFieldName:
                  type: string
                indexFieldType:
                  type: string
                  enum:
                    - STRING
                    - DATE
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: yyyy-MM-dd'T'HH:mm:ss'Z'
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
  additionalProperties:
    type: object
    properties:
      rateLimit:
        type: string
        default: "300"
      maxFileSize:
        type: string
        default: "50"
      maxFileSizeInMegaBytes:
        type: string
      crawlDepth:
        type: string
        default: "2"
      maxLinksPerUrl:
        type: string
        default: "100"
      crawlSubDomain:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
        default: false
      crawlAllDomain:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
        default: false
      honorRobots:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
        default: false
      crawlAttachments:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
        default: false
      inclusionURLCrawlPatterns:
        type: array
        items:
          type: string
      exclusionURLCrawlPatterns:
        type: array
        items:
          type: string
      inclusionURLIndexPatterns:
        type: array
        items:
          type: string
      exclusionURLIndexPatterns:
        type: array
        items:
          type: string
      inclusionFileIndexPatterns:
        type: array
        items:
          type: string
      exclusionFileIndexPatterns:
        type: array
        items:
          type: string
      proxy:
        type: object
        properties:
          host:
            type: string
          port:
            type: string
          secretArn:
            type: string
            minLength: 20
            maxLength: 2048
      enableDeletionProtection:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
        default: false
      deletionProtectionThreshold:
        type: string
        default: "15"
    required:
      - rateLimit
      - maxFileSize
      - crawlDepth
      - crawlSubDomain
      - crawlAllDomain
      - maxLinksPerUrl
      - honorRobots
version:
  type: string
  anyOf:
    - pattern: 1.0.0
required:
  - type
  - syncMode
  - connectionConfiguration
  - repositoryConfigurations
  - additionalProperties
```

[Show moreShow less](# "#")

### Web Crawler YAML schema example for

using the configuration property with AWS CloudFormation

The following is the Web Crawler YAML example for the Configuration property for
AWS CloudFormation:

```
AWSTemplateFormatVersion: 2010-09-09
Description: CloudFormation Web Crawler Data Source Template
Resources:
  DataSourceWebCrawler:
    Type: AWS::QBusiness::DataSource
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MyWebCrawlerDataSource
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: WEBCRAWLERV2
        syncMode: FULL_CRAWL
        secretArn: arn:aws:secretsmanager:us-west-2:0123456789012:my-webcrawler-secret
        connectionConfiguration:
          repositoryEndpointMetadata:
            siteMapUrls:
              - https://example.com/sitemap.xml
            s3SeedUrl: s3://bucket/seed-url
            s3SiteMapUrl: s3://bucket/sitemap-url
            seedUrlConnections:
              - seedUrl: https://example.com
            authentication: BasicAuth
        repositoryConfigurations:
          webPage:
            fieldMappings:
              - indexFieldName: title
                indexFieldType: STRING
                dataSourceFieldName: page_title
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          attachment:
            fieldMappings:
              - indexFieldName: attachment_title
                indexFieldType: STRING
                dataSourceFieldName: attachment_name
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
        additionalProperties:
          rateLimit: "300"
          maxFileSize: "50"
          crawlDepth: "2"
          maxLinksPerUrl: "100"
          crawlSubDomain: "true"
          crawlAllDomain: "true"
          honorRobots: "true"
```

[Show moreShow less](# "#")
