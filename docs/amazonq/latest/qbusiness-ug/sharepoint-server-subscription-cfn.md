# Connecting Amazon Q Business to

SharePoint Server (Subscription Edition) using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [SharePoint Server (Subscription Edition)
  configuration properties](#sharepoint-server-subscription-configuration-keys "#sharepoint-server-subscription-configuration-keys")
- [SharePoint Server (Subscription Edition) JSON schema for using
  the configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-json "#sharepoint-server-subscription-cfn-json")
- [SharePoint Server (Subscription Edition) YAML schema for using the
  configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-yaml "#sharepoint-server-subscription-cfn-yaml")

## SharePoint Server (Subscription Edition)

configuration properties

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `connectionConfiguration`                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration information for the endpoint for the data<br>source.                                                                                                                                                                                                                                                                                                                                                                                       | `object`<br>This property has a sub-property called<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                                                                                                                                                                                                                                                                                                                     | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                            | `object`<br>This property has the following sub-properties.<br>• `siteUrls`<br>• `domain`<br>• `repositoryAdditionalProperties`<br>• `tenantId`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `tenantId`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The tenant id of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                | `string`<br>OAuth2 series required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `domain`                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The domain of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `siteUrls`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The host URLs of your SharePoint account.                                                                                                                                                                                                                                                                                                                                                                                                                | `array (string)`<br>Specify the URL in the pattern `https://*`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `repositoryAdditionalProperties`                                                                                                                                                                                                                                                                                                                                                                                                                                 | Additional properties to connect with your repository<br>endpoint.                                                                                                                                                                                                                                                                                                                                                                                       | `object`<br>This property has the following sub-properties.<br>• `version`<br>• `authType`<br>• `onPremVersion`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `authType`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The type of authentication you are using:<br>`NTLM`, `Kerberos`, or `OAuth2App`.                                                                                                                                                                                                                                                                                                                                                                         | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `version`                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The SharePoint version you are using:<br>`Sever`.                                                                                                                                                                                                                                                                                                                                                                                                        | `string (Server)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `onPremVersion`                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The SharePoint version that you are using.                                                                                                                                                                                                                                                                                                                                                                                                               | `string`<br>Valid values are (empty), `2013`, `2016`, `2019`, and `SubscriptionEdition`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `repositoryConfigurations`                                                                                                                                                                                                                                                                                                                                                                                                                                       | Configuration information for the content of the data source. For<br>example, configuring specific types of content and field<br>mappings.                                                                                                                                                                                                                                                                                                               | `object`<br>This property has the following sub-properties.<br>• `event`<br>• `page`<br>• `file`<br>• `link`<br>• `attachment`<br>• `comment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| • `event`<br>• `page`<br>• `file`<br>• `link`<br>• `attachment`<br>• `comment`                                                                                                                                                                                                                                                                                                                                                                                   | A list of objects that map the attributes or field names of your<br>SharePoint Server (Subscription Edition) pages and assets to Amazon Q index field<br>names.                                                                                                                                                                                                                                                                                          | `object`<br>These properties have the following sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `indexFieldName`                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The field name of your SharePoint Server (Subscription Edition) events, pages, files, links, attachments, or comments.                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `indexFieldType`                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The field type of your SharePoint Server (Subscription Edition) events, pages, files, links, attachments, or comments.                                                                                                                                                                                                                                                                                                                                   | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and `DATE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `dataSourceFieldName`                                                                                                                                                                                                                                                                                                                                                                                                                                            | The data source field name of your SharePoint Server (Subscription Edition) events, pages, files, links, attachments, or comments.                                                                                                                                                                                                                                                                                                                       | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                | The date format of your SharePoint Server (Subscription Edition) events, pages, files, links, attachments, or comments.                                                                                                                                                                                                                                                                                                                                  | `string`<br>Specify the date format in the form `yyyy-MM-dd"T"HH:mm:ss"Z"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No       |
| `additionalProperties`                                                                                                                                                                                                                                                                                                                                                                                                                                           | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                | `object`<br>This property has the following sub-properties:<br>• `crawlAcl`<br>• `crawlFiles`<br>• `crawlPages`<br>• `crawlEvents`<br>• `crawlComments`<br>• `crawlLinks`<br>• `crawlAttachments`<br>• `crawlListData`<br>• `isCrawlLocalGroupMapping`<br>• `isCrawlAdGroupMapping`<br>• `aclConfiguration`<br>• `emailDomain`<br>• `maxFileSizeInMegaBytes`<br>• `eventTitleFilterRegEx`<br>• `pageTitleFilterRegEx`<br>• `linkTitleFilterRegEx`<br>• `inclusionFilePath`<br>• `exclusionFilePath`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`<br>• `exclusionFileNamePatterns`<br>• `inclusionOneNoteSectionNamePatterns`<br>• `exclusionOneNoteSectionNamePatterns`<br>• `inclusionOneNotePageNamePatterns`<br>• `exclusionOneNotePageNamePatterns`<br>• `proxyHost`<br>• `proxyPort`                                | Yes      |
| • `eventTitleFilterRegEx`<br>• `pageTitleFilterRegEx`<br>• `linkTitleFilterRegEx`<br>• `inclusionFilePath`<br>• `exclusionFilePath`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`<br>• `exclusionFileNamePatterns`<br>• `inclusionOneNoteSectionNamePatterns`<br>• `exclusionOneNoteSectionNamePatterns`<br>• `inclusionOneNotePageNamePatterns`<br>• `exclusionOneNotePageNamePatterns`<br>• `emailDomain` | A list of regular expression patterns to include/exclude specific<br>files in your SharePoint data source. Files that match<br>the patterns are included in the index. File that don&t match the<br>patterns are excluded from the index. If a file matches both an<br>inclusion and exclusion pattern, the exclusion pattern takes precedence,<br>and the file isn&t included in the index.                                                             | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No       |
| `aclConfiguration`                                                                                                                                                                                                                                                                                                                                                                                                                                               | Specifes how your ACL is configured.                                                                                                                                                                                                                                                                                                                                                                                                                     | `string>`<br>Valid values are `ACLWithLDAPEmailFmt`, `ACLWithManualEmailFmt`, or `ACLWithUsernameFmt`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| `proxyHost`                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The host where the web proxy is required. The host name should be without protocol<br>(http:// or https://).                                                                                                                                                                                                                                                                                                                                             | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `proxyPort`                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Port used by the host URL transport protocol. The port number should be a numeric<br>value between 0 and 65535.                                                                                                                                                                                                                                                                                                                                          | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| • `crawlAcl`<br>• `crawlFiles`<br>• `crawlPages`<br>• `crawlEvents`<br>• `crawlComments`<br>• `crawlLinks`<br>• `crawlAttachments`<br>• `crawlListData`<br>• `isCrawlLocalGroupMapping`<br>• `isCrawlAdGroupMapping`                                                                                                                                                                                                                                             | Input `TRUE` to index.                                                                                                                                                                                                                                                                                                                                                                                                                                   | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No       |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                                                                                                                                                                                                                                                         | Specify the maximum single file size limit in MBs that Amazon Q will<br>crawl. Amazon Q will crawl only the files within the size limit you<br>define. The default file size is 50MB. The maximum file size should be<br>greater than 0MB and less than or equal to 50MB.                                                                                                                                                                                | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |
| `sslCertificatePath`                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration information to access the SSL certificate stored in your Amazon S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                              | `object`<br>This property has the following sub-properties.<br>• `bucket`<br>• `key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `bucket`                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The name of the Amazon S3 bucket that stores your Microsoft Entra ID (formerly Azure AD)<br>self-signed X.509 certificate.                                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `key`                                                                                                                                                                                                                                                                                                                                                                                                                                                            | The name of the SSL certificate stored in your Amazon S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                      | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `type`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | We recommend that you use `SHAREPOINTV2` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>Valid values are `SHAREPOINTV2` and `SHAREPOINT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `enableIdentityCrawler`                                                                                                                                                                                                                                                                                                                                                                                                                                          | `true` to activate identity crawler. Identity crawler is<br>activated by default. Crawling identity information on users and groups<br>with access to specific documents is useful for user context filtering.<br>Search results are filtered based on the user or their group access to<br>documents. See [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler") for more information. | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `syncMode`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Specify whether Amazon Q should update your index by<br>syncing all documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                              | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data<br>source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only<br>new, modified, and deleted content each time your data<br>source syncs with your index<br>• Use `CHANGE_LOG` to incrementally crawl only<br>new and modified content each time your data source syncs<br>with your index                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| `secretARN`                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret<br>that contains the key-value pairs required to connect to your<br>SharePoint. If you use OAuth2App authentication, provide the client ID, client secret, LDAP URL, LDAP base DN, LDAP user name, and LDAP password. If you use NTLM or Kerberos authentication, provide the user name, password, LDAP URL, Base DN, LDAP user, and LDAP password.                                      | `string`<br>The minimum length is 20 and the maximum length is 2,048 characters.<br>If you use Sharepoint App-Only authentication (`authType` should be `OAuth2App` authentication) the secret must contain a JSON structure with the following keys:<br>``<br>{<br>"clientId": "`client ID`",<br>"clientSecret": "`client secret`",<br>"ldapUrl": "`LDAP URL`",<br>"ldbaseDn": "`LDAP base DN`",<br>"ldapUser": "`LDAP user name`",<br>"ldapPassword": "`LDAP password`"<br>}<br>``<br>If you use NTLM authentication or Kerberos authentication, the secret must contain a JSON structure with the following keys:<br>``<br>{<br>"userName": "`SharePoint account user name`",<br>"password": "`SharePoint account password`",<br>"ldapUrl": "`LDAP URL`",<br>"baseDn": "`LDAP base DN`",<br>"ldapUser": "`LDAP user name`",<br>"ldapPassword": "`LDAP password`"<br>}<br>`` | Yes      |
| `version`                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The version of this template that&s currently supported.                                                                                                                                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |

## SharePoint Server (Subscription Edition) JSON schema for using

the configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) JSON schema and examples for the
configuration property for AWS CloudFormation.

###### Topics

- [SharePoint Server (Subscription Edition) JSON schema
  for using the configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-json-schema "#sharepoint-server-subscription-cfn-json-schema")
- [SharePoint Server (Subscription Edition) JSON schema
  example for using the configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-json-example "#sharepoint-server-subscription-cfn-json-example")

### SharePoint Server (Subscription Edition) JSON schema

for using the configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) JSON schema for the configuration
property for CloudFormation

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": ["SHAREPOINTV2", "SHAREPOINT"]
    },
    "syncMode": {
      "type": "string",
      "enum": ["FULL_CRAWL", "FORCED_FULL_CRAWL", "CHANGE_LOG"]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "enableIdentityCrawler": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "string",
          "enum": ["true", "false"]
        }
      ]
    },
    "sslCertificatePath": {
      "type": "object",
      "properties": {
        "bucket": {
          "type": "string",
          "pattern": "^[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$",
          "minLength": 3,
          "maxLength": 63
        },
        "key": {
          "type": "string",
          "minLength": 1,
          "maxLength": 10240
        }
      },
      "required": ["bucket", "key"]
    },
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "tenantId": {
              "type": "string",
              "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
              "minLength": 36,
              "maxLength": 36
            },
            "domain": {
              "type": "string"
            },
            "siteUrls": {
              "type": "array",
              "items": {
                "type": "string",
                "pattern": "https://.*"
              }
            },
            "repositoryAdditionalProperties": {
              "type": "object",
              "properties": {
                "authType": {
                  "type": "string",
                  "enum": ["OAuth2App", "NTLM", "Kerberos"]
                },
                "version": {
                  "type": "string",
                  "enum": ["Server"]
                },
                "onPremVersion": {
                  "type": "string",
                  "enum": ["", "2013", "2016", "2019", "SubscriptionEdition"]
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
              "required": ["authType", "version"]
            }
          },
          "required": ["siteUrls", "domain", "repositoryAdditionalProperties"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "event": {
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
                      "enum": ["STRING", "STRING_LIST", "DATE"]
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
        "page": {
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
        "file": {
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
        "link": {
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
                      "enum": ["STRING", "STRING_LIST", "DATE"]
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
                      "enum": ["STRING", "STRING_LIST", "DATE"]
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
        "comment": {
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
                      "enum": ["STRING", "STRING_LIST", "DATE"]
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
        "eventTitleFilterRegEx": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "pageTitleFilterRegEx": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "linkTitleFilterRegEx": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFilePath": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFilePath": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionOneNoteSectionNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionOneNoteSectionNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionOneNotePageNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionOneNotePageNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "crawlFiles": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "crawlPages": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "crawlEvents": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "crawlComments": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "crawlLinks": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
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
          ]
        },
        "crawlListData": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "crawlAcl": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "aclConfiguration": {
          "type": "string",
          "enum": [
            "ACLWithLDAPEmailFmt",
            "ACLWithManualEmailFmt",
            "ACLWithUsernameFmt"
          ]
        },
        "emailDomain": {
          "type": "string"
        },
        "isCrawlLocalGroupMapping": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "isCrawlAdGroupMapping": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": ["true", "false"]
            }
          ]
        },
        "proxyHost": {
          "type": "string"
        },
        "proxyPort": {
          "type": "string"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        }
      },
      "required": []
    },
    "version": {
      "type": "string",
      "anyOf": [
        {
          "pattern": "1.0.0"
        }
      ]
    }
  },
  "required": [
    "type",
    "secretArn",
    "syncMode",
    "enableIdentityCrawler",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

[Show moreShow less](# "#")

### SharePoint Server (Subscription Edition) JSON schema

example for using the configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) JSON schema example for the
configuration property for CloudFormation

```
{

  "AWSTemplateFormatVersion": "2010-09-09",

  "Description": "CloudFormation SHAREPOINT Data Source Template",

  "Resources": {

    "DataSourceSharePoint": {

      "Type": "AWS::QBusiness::DataSource",

      "Properties": {

        "ApplicationId": "app12345-1234-1234-1234-123456789012",

        "IndexId": "indx1234-1234-1234-1234-123456789012",

        "DisplayName": "MySharePointDataSource",

        "RoleArn": "arn:aws:iam::123456789012:role/qbusiness-data-source-role",

        "Configuration": {

          "type": "SHAREPOINTV2",

          "syncMode": "FULL_CRAWL",

          "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-sharepoint-secret",

          "enableIdentityCrawler": "true",

          "sslCertificatePath": {

            "bucket": "my-sharepoint-bucket",

            "key": "ssl/cert.pem"

          },

          "connectionConfiguration": {

            "repositoryEndpointMetadata": {

              "tenantId": "1234567a-890b-1234-567c-123456789012",

              "domain": "mycompany.sharepoint.com",

              "siteUrls": [
                "https://mycompany.sharepoint.com/sites/TeamSite"
              ],

              "repositoryAdditionalProperties": {

                "authType": "OAuth2",

                "version": "Server",

                "onPremVersion": "2019",

                "enableDeletionProtection": "false",

                "deletionProtectionThreshold": "15"

              }

            }

          },

          "repositoryConfigurations": {

            "event": {

              "fieldMappings": [

                {

                  "indexFieldName": "event_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            },

            "page": {

              "fieldMappings": [

                {

                  "indexFieldName": "page_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            },

            "file": {

              "fieldMappings": [

                {

                  "indexFieldName": "file_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            },

            "link": {

              "fieldMappings": [

                {

                  "indexFieldName": "link_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            },

            "attachment": {

              "fieldMappings": [

                {

                  "indexFieldName": "attachment_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            },

            "comment": {

              "fieldMappings": [

                {

                  "indexFieldName": "comment_id",

                  "indexFieldType": "STRING",

                  "dataSourceFieldName": "id",

                  "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

                }

              ]

            }

          },

          "additionalProperties": {

            "eventTitleFilterRegEx": [
              "^.*$"
            ],

            "pageTitleFilterRegEx": [
              "^.*$"
            ],

            "linkTitleFilterRegEx": [
              "^.*$"
            ],

            "inclusionFilePath": [
              "documents/"
            ],

            "exclusionFilePath": [
              "drafts/"
            ],

            "inclusionFileTypePatterns": [
              "*.pdf",
               "*.docx"
            ],

            "exclusionFileTypePatterns": [
              "*.tmp"
            ],

            "inclusionFileNamePatterns": [
              "*report*"
            ],

            "exclusionFileNamePatterns": [
              "*draft*"
            ],

            "inclusionOneNoteSectionNamePatterns": [
              "*"
            ],

            "exclusionOneNoteSectionNamePatterns": [
              "archived"
            ],

            "inclusionOneNotePageNamePatterns": [
              "*"
            ],

            "exclusionOneNotePageNamePatterns": [
              "test"
            ],

            "crawlFiles": "true",

            "crawlPages": "true",

            "crawlEvents": "true",

            "crawlComments": "true",

            "crawlLinks": "true",

            "crawlAttachments": "true",

            "crawlListData": "false",

            "crawlAcl": "true",

            "aclConfiguration": "ACLWithUsernameFmt",

            "emailDomain": "mycompany.com",

            "isCrawlLocalGroupMapping": "false",

            "isCrawlAdGroupMapping": "true",

            "proxyHost": "proxy.mycompany.com",

            "proxyPort": "8080",

            "maxFileSizeInMegaBytes": "50"

          }

        }

      }

    }

  }

}
```

[Show moreShow less](# "#")

## SharePoint Server (Subscription Edition) YAML schema for using the

configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) YAML schema and examples for the
configuration property for AWS CloudFormation:

###### Topics

- [SharePoint Server (Subscription Edition) YAML schema
  for using the configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-yaml-schema "#sharepoint-server-subscription-cfn-yaml-schema")
- [SharePoint Server (Subscription Edition) YAML schema
  example for using the configuration property with AWS CloudFormation](#sharepoint-server-subscription-cfn-yaml-example "#sharepoint-server-subscription-cfn-yaml-example")

### SharePoint Server (Subscription Edition) YAML schema

for using the configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) YAML schema for the configuration
property for CloudFormation.

```
type: object
properties:
  type:
    type: string
    enum:
      - SHAREPOINTV2
      - SHAREPOINT
  syncMode:
    type: string
    enum:
      - FULL_CRAWL
      - FORCED_FULL_CRAWL
      - CHANGE_LOG
  secretArn:
    type: string
    minLength: 20
    maxLength: 2048
  enableIdentityCrawler:
    anyOf:
      - type: boolean
      - type: string
        enum:
          - true
          - false
  sslCertificatePath:
    type: object
    properties:
      bucket:
        type: string
        pattern: '^[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$'
        minLength: 3
        maxLength: 63
      key:
        type: string
        minLength: 1
        maxLength: 10240
    required:
      - bucket
      - key
  connectionConfiguration:
    type: object
    properties:
      repositoryEndpointMetadata:
        type: object
        properties:
          tenantId:
            type: string
            pattern: "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
            minLength: 36
            maxLength: 36
          domain:
            type: string
          siteUrls:
            type: array
            items:
              type: string
              pattern: "https://.*"
          repositoryAdditionalProperties:
            type: object
            properties:
              authType:
                type: string
                enum:
                  - OAuth2App
                  - NTLM
                  - Kerberos
              version:
                type: string
                enum:
                  - Server
              onPremVersion:
                type: string
                enum:
                  - ""
                  - "2013"
                  - "2016"
                  - "2019"
                  - SubscriptionEdition
              enableDeletionProtection:
                anyOf:
                  - type: boolean
                  - type: string
                    enum:
                      - true
                      - false
                default: false
              deletionProtectionThreshold:
                type: string
                default: "15"
            required:
              - authType
              - version
        required:
          - siteUrls
          - domain
          - repositoryAdditionalProperties
    required:
      - repositoryEndpointMetadata
  repositoryConfigurations:
    type: object
    properties:
      event:
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
                    - STRING_LIST
                    - DATE
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
      page:
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
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
      file:
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
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
      link:
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
                    - STRING_LIST
                    - DATE
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
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
                    - STRING_LIST
                    - DATE
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
      comment:
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
                    - STRING_LIST
                    - DATE
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
    required: []
  additionalProperties:
    type: object
    properties:
      eventTitleFilterRegEx:
        type: array
        items:
          type: string
      pageTitleFilterRegEx:
        type: array
        items:
          type: string
      linkTitleFilterRegEx:
        type: array
        items:
          type: string
      inclusionFilePath:
        type: array
        items:
          type: string
      exclusionFilePath:
        type: array
        items:
          type: string
      inclusionFileTypePatterns:
        type: array
        items:
          type: string
      exclusionFileTypePatterns:
        type: array
        items:
          type: string
      inclusionFileNamePatterns:
        type: array
        items:
          type: string
      exclusionFileNamePatterns:
        type: array
        items:
          type: string
      inclusionOneNoteSectionNamePatterns:
        type: array
        items:
          type: string
      exclusionOneNoteSectionNamePatterns:
        type: array
        items:
          type: string
      inclusionOneNotePageNamePatterns:
        type: array
        items:
          type: string
      exclusionOneNotePageNamePatterns:
        type: array
        items:
          type: string
      crawlFiles:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlPages:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlEvents:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlComments:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlLinks:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlAttachments:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlListData:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      crawlAcl:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      aclConfiguration:
        type: string
        enum:
          - ACLWithLDAPEmailFmt
          - ACLWithManualEmailFmt
          - ACLWithUsernameFmt
      emailDomain:
        type: string
      isCrawlLocalGroupMapping:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      isCrawlAdGroupMapping:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      proxyHost:
        type: string
      proxyPort:
        type: string
      maxFileSizeInMegaBytes:
        type: string
    required: []
  version:
    type: string
    anyOf:
      - pattern: 1.0.0
required:
  - type
  - secretArn
  - syncMode
  - enableIdentityCrawler
  - connectionConfiguration
  - repositoryConfigurations
  - additionalProperties

```

[Show moreShow less](# "#")

### SharePoint Server (Subscription Edition) YAML schema

example for using the configuration property with AWS CloudFormation

The following is the SharePoint Server (Subscription Edition) YAML example for the Configuration
property for CloudFormation:

```
{

  "type": "SHAREPOINTV2",

  "syncMode": "FULL_CRAWL",

  "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-sharepoint-secret",

  "enableIdentityCrawler": "true",

  "sslCertificatePath": {

    "bucket": "my-sharepoint-bucket",

    "key": "ssl/cert.pem"

  },

  "connectionConfiguration": {

    "repositoryEndpointMetadata": {

      "tenantId": "1234567a-890b-1234-567c-123456789012",

      "domain": "mycompany.sharepoint.com",

      "siteUrls": [
        "https://mycompany.sharepoint.com/sites/TeamSite"
      ],

      "repositoryAdditionalProperties": {

        "authType": "OAuth2",

        "version": "Server",

        "onPremVersion": "2019",

        "enableDeletionProtection": "false",

        "deletionProtectionThreshold": "15"

      }

    }

  },

  "repositoryConfigurations": {

    "event": {

      "fieldMappings": [

        {

          "indexFieldName": "event_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    },

    "page": {

      "fieldMappings": [

        {

          "indexFieldName": "page_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    },

    "file": {

      "fieldMappings": [

        {

          "indexFieldName": "file_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    },

    "link": {

      "fieldMappings": [

        {

          "indexFieldName": "link_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    },

    "attachment": {

      "fieldMappings": [

        {

          "indexFieldName": "attachment_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    },

    "comment": {

      "fieldMappings": [

        {

          "indexFieldName": "comment_id",

          "indexFieldType": "STRING",

          "dataSourceFieldName": "id",

          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"

        }

      ]

    }

  },

  "additionalProperties": {

    "eventTitleFilterRegEx": [
      "^.*$"
    ],

    "pageTitleFilterRegEx": [
      "^.*$"
    ],

    "linkTitleFilterRegEx": [
      "^.*$"
    ],

    "inclusionFilePath": [
      "documents/"
    ],

    "exclusionFilePath": [
      "drafts/"
    ],

    "inclusionFileTypePatterns": [
      "*.pdf",
       "*.docx"
    ],

    "exclusionFileTypePatterns": [
      "*.tmp"
    ],

    "inclusionFileNamePatterns": [
      "*report*"
    ],

    "exclusionFileNamePatterns": [
      "*draft*"
    ],

    "inclusionOneNoteSectionNamePatterns": [
      "*"
    ],

    "exclusionOneNoteSectionNamePatterns": [
      "archived"
    ],

    "inclusionOneNotePageNamePatterns": [
      "*"
    ],

    "exclusionOneNotePageNamePatterns": [
      "test"
    ],

    "crawlFiles": "true",

    "crawlPages": "true",

    "crawlEvents": "true",

    "crawlComments": "true",

    "crawlLinks": "true",

    "crawlAttachments": "true",

    "crawlListData": "false",

    "crawlAcl": "true",

    "aclConfiguration": "ACLWithUsernameFmt",

    "emailDomain": "mycompany.com",

    "isCrawlLocalGroupMapping": "false",

    "isCrawlAdGroupMapping": "true",

    "proxyHost": "proxy.mycompany.com",

    "proxyPort": "8080",

    "maxFileSizeInMegaBytes": "50"

  },

  "version": "1.0.0"

}
```

[Show moreShow less](# "#")
