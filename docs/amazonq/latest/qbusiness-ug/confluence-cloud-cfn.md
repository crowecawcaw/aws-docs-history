# Connecting Amazon Q Business to Confluence (Cloud)

using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [Confluence configuration
  properties](#confluence-configuration-keys "#confluence-configuration-keys")
- [Confluence (Cloud) JSON schema for using the
  configuration property with AWS CloudFormation](#confluence-cloud-cfn-json "#confluence-cloud-cfn-json")
- [Confluence (Cloud) YAML schema for using the
  configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml "#confluence-cloud-cfn-yaml")

## Confluence configuration

properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`                                                                                                                                                                                                                                                             | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                 | `object`<br>This property has a sub-property called<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                                                                                                                                          | This is the endpoint information for the data source. This is a sub-property for<br>the `connectionConfiguration`.                                                                                                                                                                                                                                                                              | `object`<br>This property has the following sub-properties.<br>• `hostUrl`<br>• `type`<br>• `authType`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `hostUrl`                                                                                                                                                                                                                                                                             | The URL for your Confluence instance. For example,<br>`https://example.confluence.com`.                                                                                                                                                                                                                                                                                                         | `string`<br>Specify the URL in the pattern `https://*`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `type`                                                                                                                                                                                                                                                                                | The hosting method for your Confluence instance.                                                                                                                                                                                                                                                                                                                                                | `string`<br>The allowed values are `SAAS` or `ON_PREM`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `authType`                                                                                                                                                                                                                                                                            | The authentication method for your Confluence instance.                                                                                                                                                                                                                                                                                                                                         | `string`<br>The allowed values are `Basic` or `OAuth2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `repositoryConfigurations`                                                                                                                                                                                                                                                            | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                         | `object`<br>This property has the following sub-properties.<br>• `space`<br>• `page`<br>• `blog`<br>• `comment`<br>• `attachment`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes      |
| • `space`<br>• `page`<br>• `blog`<br>• `comment`<br>• `attachment`                                                                                                                                                                                                                    | A list of objects that map the attributes or field names of your<br>Confluence spaces, pages, blogs, comments, and attachments to Amazon Q index field names.                                                                                                                                                                                                                                   | `object`<br>These properties have the following sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No       |
| `indexFieldName`                                                                                                                                                                                                                                                                      | The field name of your Confluence spaces, pages, blogs, comments, or<br>attachments.                                                                                                                                                                                                                                                                                                            | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `indexFieldType`                                                                                                                                                                                                                                                                      | The field type of your Confluence spaces, pages, blogs, comments, or<br>attachments.                                                                                                                                                                                                                                                                                                            | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and<br>`DATE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `dataSourceFieldName`                                                                                                                                                                                                                                                                 | The data source field name of your Confluence spaces, pages, blogs,<br>comments, or attachments.                                                                                                                                                                                                                                                                                                | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `dateFieldFormat`                                                                                                                                                                                                                                                                     | The date format of your Confluence spaces, pages, blogs, comments,<br>or attachments.                                                                                                                                                                                                                                                                                                           | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `additionalProperties`                                                                                                                                                                                                                                                                | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                          | `object`<br>This property has the following sub-properties.<br>• `isCrawlAcl`<br>• `isRotateSecret`<br>• `isCrawlPersonalSpace`<br>• `isCrawlArchivedSpace`<br>• `isCrawlArchivedPage`<br>• `isCrawlPage`<br>• `isCrawlBlog`<br>• `isCrawlPageComment`<br>• `isCrawlPageAttachment`<br>• `isCrawlBlogComment`<br>• `isCrawlBlogAttachment`<br>• `fieldForUserId`<br>• `maxFileSizeInMegaBytes`<br>• `inclusionSpaceKeyFilter`<br>• `exclusionSpaceKeyFilter`<br>• `pageTitleRegEX`<br>• `blogTitleRegEX`<br>• `commentTitleRegEX`<br>• `attachmentTitleRegEX`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionUrlPatterns`<br>• `exclusionUrlPatterns`                                   | Yes      |
| `isCrawlAcl`                                                                                                                                                                                                                                                                          | Specify `true` to crawl access control information from<br>documents.                                                                                                                                                                                                                                                                                                                           | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `isRotateSecret`                                                                                                                                                                                                                                                                      | Specify `true` if you want to automatically rotate the secret.                                                                                                                                                                                                                                                                                                                                  | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `fieldForUserId`                                                                                                                                                                                                                                                                      | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                             | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `proxyHost`                                                                                                                                                                                                                                                                           | The host where the web proxy is required. The host name should be without protocol<br>(http:// or https://).                                                                                                                                                                                                                                                                                    | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `proxyPort`                                                                                                                                                                                                                                                                           | Port used by the host URL transport protocol. The port number should be a numeric<br>value between 0 and 65535.                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                                                                              | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                       | `string`<br>The allowed values are numbers between greater than 0 and less than or equal to<br>50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |
| • `inclusionSpaceKeyFilter`<br>• `exclusionSpaceKeyFilter`<br>• `pageTitleRegEX`<br>• `blogTitleRegEX`<br>• `commentTitleRegEX`<br>• `attachmentTitleRegEX`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionUrlPatterns`<br>• `exclusionUrlPatterns` | A list of regular expression patterns to include and/or exclude certain files in<br>your Confluence data source. Files that match the patterns are included<br>in the index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence<br>and the file isn't included in the index. | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No       |
| • `isCrawlPersonalSpace`<br>• `isCrawlArchivedSpace`<br>• `isCrawlArchivedPage`<br>• `isCrawlPage`<br>• `isCrawlBlog`<br>• `isCrawlPageComment`<br>• `isCrawlPageAttachment`<br>• `isCrawlBlogComment`<br>• `isCrawlBlogAttachment`                                                   | Specify `true` to index files in your Confluence personal<br>spaces, pages, blogs, page comments, page attachments, blog comments, and blog<br>attachments.                                                                                                                                                                                                                                     | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `type`                                                                                                                                                                                                                                                                                | The type of data source. We recommend that you use `CONFLUENCEV2` as<br>your data source type.                                                                                                                                                                                                                                                                                                  | `string`<br>Valid values are `CONFLUENCEV2` and<br>`CONFLUENCE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes      |
| `enableIdentityCrawler`                                                                                                                                                                                                                                                               | Specify `true` to activate identity crawler. Identity crawler is<br>activated by default. See [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler") for more information.                                                                                                                                                     | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `syncMode`                                                                                                                                                                                                                                                                            | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                     | `string`<br>Valid values are `FORCED_FULL_CRAWL` and `FULL_CRAWL`. You<br>can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and<br>deleted content each time your data source syncs with your index                                                                                                                                                                                                                                                                                                                | Yes      |
| `secretARN`                                                                                                                                                                                                                                                                           | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains<br>the key-value pairs required to connect to your Confluence<br>instance.                                                                                                                                                                                                                                             | `string`<br>The minimum length is 20 and the maximum length is 2,048 characters. If you<br>use basic authentication, the secret must contain a JSON structure with the following<br>keys:<br>``<br>{<br>"username": "`Confluence account user name`",<br>"password": "`Confluence API token`"<br>}<br>``<br>If you use OAuth 2.0 authentication, the secret must contain a JSON<br>structure with the following keys:<br>``<br>{<br>"confluenceAppKey": "`app key for your Confluence account`",<br>"confluenceAppSecret": "`app secret from your Confluence token`",<br>"confluenceAccessToken": "`access token created in Confluence`",<br>"confluenceRefreshToken": "`refresh token created in Confluence`"<br>}<br>`` | Yes      |
| `version`                                                                                                                                                                                                                                                                             | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |

## Confluence (Cloud) JSON schema for using the

configuration property with AWS CloudFormation

The following is the Confluence (Cloud) JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Confluence (Cloud) JSON schema for using the
  configuration property with AWS CloudFormation](#confluence-cloud-cfn-json-schema "#confluence-cloud-cfn-json-schema")
- [Confluence (Cloud) JSON schema example for
  using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-json-example "#confluence-cloud-cfn-json-example")

### Confluence (Cloud) JSON schema for using the

configuration property with AWS CloudFormation

The following is the Confluence (Cloud) JSON schema for the configuration property for
CloudFormation

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": ["CONFLUENCEV2", "CONFLUENCE"]
    },
    "syncMode": {
      "type": "string",
      "enum": ["FULL_CRAWL", "FORCED_FULL_CRAWL"]
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
            "hostUrl": {
              "type": "string",
              "pattern": "https:.*"
            },
            "type": {
              "type": "string",
              "enum": ["SAAS"]
            },
            "authType": {
              "type": "string",
              "enum": ["Basic", "OAuth2"]
            }
          },
          "required": ["hostUrl", "type", "authType"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "space": {
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
                      "enum": ["STRING", "STRING_LIST", "DATE", "LONG"]
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
        "blog": {
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
                      "enum": ["STRING", "STRING_LIST", "DATE", "LONG"]
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
                      "enum": ["STRING", "STRING_LIST", "DATE", "LONG"]
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
                      "enum": ["STRING", "STRING_LIST", "DATE", "LONG"]
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
        "isCrawlAcl": {
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
        "fieldForUserId": {
          "type": "string"
        },
        "inclusionSpaceKeyFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionSpaceKeyFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "pageTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "blogTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "commentTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "attachmentTitleRegEX": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlPersonalSpace": {
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
        "isCrawlArchivedSpace": {
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
        "isCrawlArchivedPage": {
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
        "isCrawlPage": {
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
        "isCrawlBlog": {
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
        "isCrawlPageComment": {
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
        "isCrawlPageAttachment": {
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
        "isCrawlBlogComment": {
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
        "isCrawlBlogAttachment": {
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
        "inclusionUrlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionUrlPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "proxyHost": {
          "type": "string"
        },
        "proxyPort": {
          "type": "string"
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
      "required": []
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
    "secretArn",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

[Show moreShow less](# "#")

### Confluence (Cloud) JSON schema example for

using the configuration property with AWS CloudFormation

The following is the Confluence (Cloud) JSON schema example for the configuration
property for CloudFormation

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "CloudFormation CONFLUENCE Data Source Template",
  "Resources": {
    "DataSourceConfluence": {
      "Type": "AWS::QBusiness::DataSource",
      "Properties": {
        "ApplicationId": "app12345-1234-1234-1234-123456789012",
        "IndexId": "indx1234-1234-1234-1234-123456789012",
        "DisplayName": "MyConfluenceDataSource",
        "RoleArn": "arn:aws:iam::123456789012:role/qbusiness-data-source-role",
        "Configuration": {
          "type": "CONFLUENCEV2",
          "syncMode": "FULL_CRAWL",
          "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-confluence-secret",
          "enableIdentityCrawler": "true",
          "connectionConfiguration": {
            "repositoryEndpointMetadata": {
              "hostUrl": "https://mycompany.atlassian.net",
              "type": "SAAS",
              "authType": "OAuth2"
            }
          },
          "repositoryConfigurations": {
            "space": {
              "fieldMappings": [
                {
                  "indexFieldName": "space_id",
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
            "blog": {
              "fieldMappings": [
                {
                  "indexFieldName": "blog_id",
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
            }
          },
          "additionalProperties": {
            "isCrawlAcl": "true",
            "fieldForUserId": "user_id",
            "inclusionSpaceKeyFilter": ["SPACE1", "SPACE2"],
            "exclusionSpaceKeyFilter": ["SPACE3"],
            "pageTitleRegEX": ["^.*$"],
            "blogTitleRegEX": ["^.*$"],
            "commentTitleRegEX": ["^.*$"],
            "attachmentTitleRegEX": ["^.*$"],
            "isCrawlPersonalSpace": "false",
            "isCrawlArchivedSpace": "false",
            "isCrawlArchivedPage": "true",
            "isCrawlPage": "true",
            "isCrawlBlog": "true",
            "isCrawlPageComment": "false",
            "isCrawlPageAttachment": "false",
            "isCrawlBlogComment": "true",
            "isCrawlBlogAttachment": "true",
            "maxFileSizeInMegaBytes": "50",
            "inclusionFileTypePatterns": ["*.pdf", "*.docx"],
            "exclusionFileTypePatterns": ["*.tmp"],
            "inclusionUrlPatterns": ["*"],
            "exclusionUrlPatterns": ["*.tmp"],
            "enableDeletionProtection": "false",
            "deletionProtectionThreshold": "15"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")

## Confluence (Cloud) YAML schema for using the

configuration property with AWS CloudFormation

The following is the Confluence (Cloud) YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Confluence (Cloud) YAML schema for using the
  configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml-schema "#confluence-cloud-cfn-yaml-schema")
- [Confluence (Cloud) YAML schema example for
  using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml-example "#confluence-cloud-cfn-yaml-example")

### Confluence (Cloud) YAML schema for using the

configuration property with AWS CloudFormation

The following is the Confluence (Cloud) YAML schema for the configuration property for
CloudFormation.

```
type: object
properties:
  type:
    type: string
    enum:
      - CONFLUENCEV2
      - CONFLUENCE
  syncMode:
    type: string
    enum:
      - FULL_CRAWL
      - FORCED_FULL_CRAWL
  secretArn:
    type: string
    minLength: 20
    maxLength: 2048
  enableIdentityCrawler:
    anyOf:
      - type: boolean
      - type: string
        enum:
          - "true"
          - "false"
  connectionConfiguration:
    type: object
    properties:
      repositoryEndpointMetadata:
        type: object
        properties:
          hostUrl:
            type: string
            pattern: "https:.*"
          type:
            type: string
            enum:
              - SAAS
          authType:
            type: string
            enum:
              - Basic
              - OAuth2
        required:
          - hostUrl
          - type
          - authType
    required:
      - repositoryEndpointMetadata
  repositoryConfigurations:
    type: object
    properties:
      space:
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
                    - STRING_LIST
                    - DATE
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
        required:
          - fieldMappings
      blog:
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
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
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
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
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
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
        required:
          - fieldMappings
  additionalProperties:
    type: object
    properties:
      isCrawlAcl:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      fieldForUserId:
        type: string
      inclusionSpaceKeyFilter:
        type: array
        items:
          type: string
      exclusionSpaceKeyFilter:
        type: array
        items:
          type: string
      pageTitleRegEX:
        type: array
        items:
          type: string
      blogTitleRegEX:
        type: array
        items:
          type: string
      commentTitleRegEX:
        type: array
        items:
          type: string
      attachmentTitleRegEX:
        type: array
        items:
          type: string
      isCrawlPersonalSpace:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlArchivedSpace:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlArchivedPage:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlPage:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlBlog:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlPageComment:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlPageAttachment:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlBlogComment:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      isCrawlBlogAttachment:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      maxFileSizeInMegaBytes:
        type: string
      inclusionFileTypePatterns:
        type: array
        items:
          type: string
      exclusionFileTypePatterns:
        type: array
        items:
          type: string
      inclusionUrlPatterns:
        type: array
        items:
          type: string
      exclusionUrlPatterns:
        type: array
        items:
          type: string
      proxyHost:
        type: string
      proxyPort:
        type: string
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
    required: []
version:
  type: string
  anyOf:
    - pattern: 1.0.0
required:
  - type
  - syncMode
  - secretArn
  - connectionConfiguration
  - repositoryConfigurations
  - additionalProperties
```

[Show moreShow less](# "#")

### Confluence (Cloud) YAML schema example for

using the configuration property with AWS CloudFormation

The following is the Confluence (Cloud) YAML example for the Configuration property for
CloudFormation:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation CONFLUENCE Data Source Template
Resources:
  DataSourceConfluence:
    Type: AWS::QBusiness::DataSource
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MyConfluenceDataSource
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: CONFLUENCEV2
        syncMode: FULL_CRAWL
        secretArn: arn:aws:secretsmanager:us-west-2:123456789012:secret:my-confluence-secret
        enableIdentityCrawler: "true"
        connectionConfiguration:
          repositoryEndpointMetadata:
            hostUrl: https://mycompany.atlassian.net
            type: SAAS
            authType: OAuth2
        repositoryConfigurations:
          space:
            fieldMappings:
              - indexFieldName: space_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          page:
            fieldMappings:
              - indexFieldName: page_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          blog:
            fieldMappings:
              - indexFieldName: blog_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          comment:
            fieldMappings:
              - indexFieldName: comment_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
          attachment:
            fieldMappings:
              - indexFieldName: attachment_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
        additionalProperties:
          isCrawlAcl: "true"
          fieldForUserId: user_id
          inclusionSpaceKeyFilter:
            - SPACE1
            - SPACE2
          exclusionSpaceKeyFilter:
            - SPACE3
          pageTitleRegEX:
            - "^.*$"
          blogTitleRegEX:
            - "^.*$"
          commentTitleRegEX:
            - "^.*$"
          attachmentTitleRegEX:
            - "^.*$"
          isCrawlPersonalSpace: "false"
          isCrawlArchivedSpace: "false"
          isCrawlArchivedPage: "true"
          isCrawlPage: "true"
          isCrawlBlog: "true"
          isCrawlPageComment: "false"
          isCrawlPageAttachment: "false"
          isCrawlBlogComment: "true"
          isCrawlBlogAttachment: "true"
          maxFileSizeInMegaBytes: "50"
          inclusionFileTypePatterns:
            - "*.pdf"
            - "*.docx"
          exclusionFileTypePatterns:
            - "*.tmp"
          inclusionUrlPatterns:
            - "*"
          exclusionUrlPatterns:
            - "*.tmp"
          enableDeletionProtection: "false"
          deletionProtectionThreshold: "15"
```

[Show moreShow less](# "#")
