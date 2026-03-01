# Connecting Amazon Q Business to SharePoint (Online) using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [SharePoint (Online) configuration properties](#sharepoint-cloud-configuration-keys "#sharepoint-cloud-configuration-keys")
- [SharePoint (Online) JSON schema for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-json "#sharepoint-cloud-cfn-json")
- [SharePoint (Online) YAML schema for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-yaml "#sharepoint-cloud-cfn-yaml")

## SharePoint (Online) configuration properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `object`<br>This property has a sub-property called<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `object`<br>This property has the following sub-properties.<br>• `siteUrls`<br>• `domain`<br>• `repositoryAdditionalProperties`<br>• `tenantId`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `tenantId`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The tenant id of your SharePoint (Online) account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`<br>OAuth2 series required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes      |
| `domain`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | The domain of your SharePoint (Online) account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `siteUrls`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The host URLs of your SharePoint (Online) account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `array (string)`<br>Specify the URL in the pattern `https://*`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `repositoryAdditionalProperties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Additional properties to connect with your repository endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `object`<br>This property has the following sub-properties.<br>• `version`<br>• `authType`<br>• `s3bucketName`<br>• `s3certificateName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes      |
| `s3bucketName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The name of the Amazon S3 bucket that stores your Azure AD self-signed<br>X.509 certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>Azure AD App-Only auth required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `s3certificateName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The name of the SSL certificate stored in your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`<br>Azure AD App-Only auth required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `authType`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | The type of authentication you are using: `OAuth2`,<br>`OAuth2Certificate`, `OAuth2App`, or `Basic`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The SharePoint version you are using: `Online`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string (Online)`<br>Azure AD App-Only auth required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `repositoryConfigurations`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `object`<br>This property has the following sub-properties.<br>• `event`<br>• `page`<br>• `file`<br>• `link`<br>• `attachment`<br>• `comment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes      |
| • `event`<br>• `page`<br>• `file`<br>• `link`<br>• `attachment`<br>• `comment`                                                                                                                                                                                                                                                                                                                                                                                                                                  | A list of objects that map the attributes or field names of your SharePoint (Online)<br>pages and assets to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `object`<br>These properties have the following sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No       |
| `indexFieldName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The field name of your SharePoint (Online) events, pages, files, links, attachments,<br>or comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `indexFieldType`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The field type of your SharePoint (Online) events, pages, files, links, attachments,<br>or comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and<br>`DATE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `dataSourceFieldName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The data source field name of your SharePoint (Online) events, pages, files, links,<br>attachments, or comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The date format of your SharePoint (Online) events, pages, files, links,<br>attachments, or comments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `additionalProperties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `object`<br>This property has the following sub-properties:<br>• `crawlAcl`<br>• `crawlFiles`<br>• `crawlPages`<br>• `crawlEvents`<br>• `crawlComments`<br>• `crawlLinks`<br>• `crawlAttachments`<br>• `crawlListData`<br>• `isCrawlLocalGroupMapping`<br>• `maxFileSizeInMegaBytes`<br>• `eventTitleFilterRegEx`<br>• `pageTitleFilterRegEx`<br>• `linkTitleFilterRegEx`<br>• `inclusionFilePath`<br>• `exclusionFilePath`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`<br>• `exclusionFileNamePatterns`<br>• `inclusionOneNoteSectionNamePatterns`<br>• `exclusionOneNoteSectionNamePatterns`<br>• `inclusionOneNotePageNamePatterns`<br>• `exclusionOneNotePageNamePatterns`                                                                                                                                                                                                                                                                                                                                                                                       | Yes      |
| • `eventTitleFilterRegEx`<br>• `pageTitleFilterRegEx`<br>• `linkTitleFilterRegEx`<br>• `inclusionFilePath`<br>• `exclusionFilePath`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`<br>• `exclusionFileNamePatterns`<br>• `inclusionOneNoteSectionNamePatterns`<br>• `exclusionOneNoteSectionNamePatterns`<br>• `inclusionOneNotePageNamePatterns`<br>• `exclusionOneNotePageNamePatterns`                                                                   | A list of regular expression patterns to include/exclude specific files in your<br>SharePoint (Online) data source. Files that match the patterns are included in the index.<br>File that don't match the patterns are excluded from the index. If a file matches both<br>an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file<br>isn't included in the index.                                                                                                                                                                                                                                 | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No       |
| • `crawlFiles`<br>• `crawlPages`<br>• `crawlEvents`<br>• `crawlComments`<br>• `crawlLinks`<br>• `crawlAttachments`<br>• `crawlListData`<br>• `crawlAcl`<br>NoteAmazon Q Business crawls ACL information by default to ensure<br>responses are generated only from documents your end users have access to. See<br>[Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.<br>• `isCrawlLocalGroupMapping`<br>• `isCrawlAdGroupMapping` | Input `TRUE` to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                                                                                                                                                                          | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | We recommend that you use `SHAREPOINTV2` as your data source<br>type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`<br>Valid values are `SHAREPOINTV2` and<br>`SHAREPOINT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes      |
| `enableIdentityCrawler`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `true` to activate identity crawler. Identity crawler is activated<br>by default. Crawling identity information on users and groups with access to specific<br>documents is useful for user context filtering. Search results are filtered based on<br>the user or their group access to documents.<br>NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `syncMode`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and<br>deleted content each time your data source syncs with your index<br>• Use `CHANGE_LOG` to incrementally crawl only new and modified<br>content each time your data source syncs with your index                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `secretARN`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your SharePoint. If you use basic<br>authentication, provide the username and password. If you use OAuth 2.0 authentication,<br>provide the username, password, client ID, and client secret.                                                                                                                                                                                                                                                                                                          | `string`<br>The minimum length is 20 and the maximum length is 2,048 characters. If you<br>use basic authentication (`authType` should be `Basic`), the secret must contain a JSON structure with the<br>following keys:<br>``<br>{<br>"username": "`SharePoint (Online) account user name`",<br>"password": "`SharePoint (Online) password`"<br>}<br>``<br>If you use Azure AD App-only authentication (`authType` should be<br>`OAuth2Certificate`), the secret must contain a JSON structure with the<br>following keys:<br>``<br>{<br>"clientId": "`SharePoint (Online) client ID`",<br>"privateKey": "`SharePoint (Online) private key`"<br>}<br>``<br>If you use OAuth2 authentication (`authType` should be<br>`OAuth`) or Sharepoint App-Only authentication (`authType`<br>should be `OAuth2App`) the secret must contain a JSON structure with the<br>following keys:<br>``<br>{<br>"clientId": "`SharePoint (Online) client ID`",<br>"clientSecret": "`SharePoint (Online) client secret`",<br>"userName": "`SharePoint (Online) account user name`",<br>"password": "`SharePoint (Online) password`"<br>}<br>`` | Yes      |
| `version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |

## SharePoint (Online) JSON schema for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [SharePoint (Online) JSON schema for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-json-schema "#sharepoint-cloud-cfn-json-schema")
- [SharePoint (Online) JSON schema example for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-json-example "#sharepoint-cloud-cfn-json-example")

### SharePoint (Online) JSON schema for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) JSON schema for the configuration property for
CloudFormation

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
                "s3bucketName": {
                  "type": "string"
                },
                "s3certificateName": {
                  "type": "string"
                },
                "authType": {
                  "type": "string",
                  "enum": [
                    "OAuth2",
                    "OAuth2Certificate",
                    "OAuth2App",
                    "OAuth2_RefreshToken",
                    "Basic"
                  ]
                },
                "version": {
                  "type": "string",
                  "enum": ["Online"]
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
    "syncMode",
    "secretArn",
    "enableIdentityCrawler",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

[Show moreShow less](# "#")

### SharePoint (Online) JSON schema example for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) JSON schema example for the configuration
property for CloudFormation

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
          "connectionConfiguration": {
            "repositoryEndpointMetadata": {
              "tenantId": "1234567a-890b-1234-567c-123456789012",
              "domain": "example.sharepoint.com",
              "siteUrls": ["https://example.sharepoint.com/sites/mysite"],
              "repositoryAdditionalProperties": {
                "s3bucketName": "my-bucket",
                "s3certificateName": "my-certificate",
                "authType": "OAuth2",
                "version": "Online",
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
            }
          },
          "additionalProperties": {
            "eventTitleFilterRegEx": ["^.*$"],
            "pageTitleFilterRegEx": ["^.*$"],
            "linkTitleFilterRegEx": ["^.*$"],
            "inclusionFilePath": ["documents/"],
            "exclusionFilePath": ["drafts/"],
            "inclusionFileTypePatterns": ["\\.docx"],
            "exclusionFileTypePatterns": ["\\.tmp"],
            "inclusionFileNamePatterns": ["*report*"],
            "exclusionFileNamePatterns": ["*draft*"],
            "enableDeletionProtection": "false",
            "maxFileSizeInMegaBytes": "50"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")

## SharePoint (Online) YAML schema for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [SharePoint (Online) YAML schema for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-yaml-schema "#sharepoint-cloud-cfn-yaml-schema")
- [SharePoint (Online) YAML schema example for using the configuration property with AWS CloudFormation](#sharepoint-cloud-cfn-yaml-example "#sharepoint-cloud-cfn-yaml-example")

### SharePoint (Online) YAML schema for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) YAML schema for the configuration property for
CloudFormation.

```
$schema: http://json-schema.org/draft-04/schema#
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
              s3bucketName:
                type: string
              s3certificateName:
                type: string
              authType:
                type: string
                enum:
                  - OAuth2
                  - OAuth2Certificate
                  - OAuth2App
                  - OAuth2_RefreshToken
                  - Basic
              version:
                type: string
                enum:
                  - Online
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
      maxFileSizeInMegaBytes:
        type: string
    required: []
  version:
    type: string
    anyOf:
      - pattern: 1.0.0
required:
  - type
  - syncMode
  - secretArn
  - enableIdentityCrawler
  - connectionConfiguration
  - repositoryConfigurations
  - additionalProperties
```

[Show moreShow less](# "#")

### SharePoint (Online) YAML schema example for using the configuration property with AWS CloudFormation

The following is the SharePoint (Online) YAML example for the Configuration property for
CloudFormation:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation SHAREPOINT Data Source Template
Resources:
  DataSourceSharePoint:
    Type: AWS::QBusiness::DataSource
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MySharePointDataSource
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: SHAREPOINTV2
        syncMode: FULL_CRAWL
        secretArn: arn:aws:secretsmanager:us-west-2:123456789012:secret:my-sharepoint-secret
        enableIdentityCrawler: "true"
        connectionConfiguration:
          repositoryEndpointMetadata:
            tenantId: 1234567a-890b-1234-567c-123456789012
            domain: example.sharepoint.com
            siteUrls:
              - https://example.sharepoint.com/sites/mysite
            repositoryAdditionalProperties:
              s3bucketName: my-bucket
              s3certificateName: my-certificate
              authType: OAuth2
              version: Online
              enableDeletionProtection: "false"
              deletionProtectionThreshold: "15"
        repositoryConfigurations:
          event:
            fieldMappings:
              - indexFieldName: event_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          page:
            fieldMappings:
              - indexFieldName: page_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
        additionalProperties:
          eventTitleFilterRegEx:
            - "^.*$"
          pageTitleFilterRegEx:
            - "^.*$"
          linkTitleFilterRegEx:
            - "^.*$"
          inclusionFilePath:
            - documents/
          exclusionFilePath:
            - drafts/
          inclusionFileTypePatterns:
            - ".docx"
          exclusionFileTypePatterns:
            - ".tmp"
          inclusionFileNamePatterns:
            - "*report*"
          exclusionFileNamePatterns:
            - "*draft*"
          enableDeletionProtection: "false"
          maxFileSizeInMegaBytes: "50"
```

[Show moreShow less](# "#")
