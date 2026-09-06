

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Confluence (Cloud) using AWS CloudFormation
<a name="confluence-cloud-cfn"></a>

You use the [`AWS::QBusiness::DataSource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html) resource to connect a data source to your Amazon Q application.

Use the [`configuration`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-applicationid) property to provide a JSON or YAML schema with the necessary configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) in the *CloudFormation User Guide*.

**Topics**
+ [Confluence configuration properties](#confluence-configuration-keys)
+ [Confluence (Cloud) JSON schema for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-json)
+ [Confluence (Cloud) YAML schema for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml)

## Confluence configuration properties
<a name="confluence-configuration-keys"></a>

The following provides information about important configuration properties required in the schema.


| Configuration | Description | Type | Required | 
| --- | --- | --- | --- | 
| `connectionConfiguration` | Configuration information for the endpoint for the data source. | `object`<br />This property has a sub-property called `repositoryEndpointMetadata`. | Yes | 
| `repositoryEndpointMetadata` | This is the endpoint information for the data source. This is a sub-property for the connectionConfiguration. | `object`<br />This property has the following sub-properties.+  `hostUrl` <br />+  `type` <br />+  `authType`  | Yes | 
| `hostUrl` | The URL for your Confluence instance. For example, {{https://example.confluence.com}}. | `string`<br />Specify the URL in the pattern `https://*` | Yes | 
| `type` | The hosting method for your Confluence instance. | `string`<br />The allowed values are `SAAS` or `ON_PREM`. | Yes | 
| `authType` | The authentication method for your Confluence instance. | `string`<br />The allowed values are `Basic` or `OAuth2`. | Yes | 
| `repositoryConfigurations` | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. | `object`<br />This property has the following sub-properties.+  `space` <br />+  `page` <br />+  `blog` <br />+  `comment` <br />+  `attachment`  | Yes | 
|  +  `space` <br />+  `page` <br />+  `blog` <br />+  `comment` <br />+  `attachment`   | A list of objects that map the attributes or field names of your Confluence spaces, pages, blogs, comments, and attachments to Amazon Q index field names. | `object`<br />These properties have the following sub-properties.+  `indexFieldName` <br />+  `indexFieldType` <br />+  `dataSourceFieldName` <br />+  `dateFieldFormat`  | No | 
| `indexFieldName` | The field name of your Confluence spaces, pages, blogs, comments, or attachments. | `string` | Yes | 
| `indexFieldType` | The field type of your Confluence spaces, pages, blogs, comments, or attachments. | `string`<br />The allowed values are `STRING`, `STRING_LIST`, and `DATE`. | Yes | 
| `dataSourceFieldName` | The data source field name of your Confluence spaces, pages, blogs, comments, or attachments. | `string` | Yes | 
| `dateFieldFormat` | The date format of your Confluence spaces, pages, blogs, comments, or attachments. | `string`<br />Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'` | No | 
| `additionalProperties` | Additional configuration options for your content in your data source. | `object`<br />This property has the following sub-properties.+  `isCrawlAcl` <br />+  `isRotateSecret` <br />+  `isCrawlPersonalSpace` <br />+  `isCrawlArchivedSpace` <br />+  `isCrawlArchivedPage` <br />+  `isCrawlPage` <br />+  `isCrawlBlog` <br />+  `isCrawlPageComment` <br />+  `isCrawlPageAttachment` <br />+  `isCrawlBlogComment` <br />+  `isCrawlBlogAttachment` <br />+  `fieldForUserId` <br />+  `maxFileSizeInMegaBytes` <br />+  `inclusionSpaceKeyFilter` <br />+  `exclusionSpaceKeyFilter` <br />+  `pageTitleRegEX` <br />+  `blogTitleRegEX` <br />+  `commentTitleRegEX` <br />+  `attachmentTitleRegEX` <br />+  `inclusionFileTypePatterns` <br />+  `exclusionFileTypePatterns` <br />+  `inclusionUrlPatterns` <br />+  `exclusionUrlPatterns`  | Yes | 
| `isCrawlAcl` | Specify true to crawl access control information from documents. | `boolean` | No | 
| `isRotateSecret` | Specify true if you want to automatically rotate the secret. | `boolean` | No | 
| `fieldForUserId` | Specify field to use for UserId for ACL crawling. | `string` | No | 
| `proxyHost` | The host where the web proxy is required. The host name should be without protocol (http:// or https://). | `string` | Yes | 
| `proxyPort` | Port used by the host URL transport protocol. The port number should be a numeric value between 0 and 65535. | `string` | Yes | 
| `maxFileSizeInMegaBytes` | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB. | `string`<br />The allowed values are numbers between greater than 0 and less than or equal to 50. | No | 
| +  `inclusionSpaceKeyFilter` <br />+  `exclusionSpaceKeyFilter` <br />+  `pageTitleRegEX` <br />+  `blogTitleRegEX` <br />+  `commentTitleRegEX` <br />+  `attachmentTitleRegEX` <br />+  `inclusionFileTypePatterns` <br />+  `exclusionFileTypePatterns` <br />+  `inclusionUrlPatterns` <br />+  `exclusionUrlPatterns`  | A list of regular expression patterns to include and/or exclude certain files in your Confluence data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index. | `array (string)` | No | 
|  +  `isCrawlPersonalSpace` <br />+  `isCrawlArchivedSpace` <br />+  `isCrawlArchivedPage` <br />+  `isCrawlPage` <br />+  `isCrawlBlog` <br />+  `isCrawlPageComment` <br />+  `isCrawlPageAttachment` <br />+  `isCrawlBlogComment` <br />+  `isCrawlBlogAttachment`   | Specify true to index files in your Confluence personal spaces, pages, blogs, page comments, page attachments, blog comments, and blog attachments. | `boolean` | No | 
| `type` | The type of data source. We recommend that you use CONFLUENCEV2 as your data source type. | `string`<br />Valid values are `CONFLUENCEV2` and `CONFLUENCE`. | Yes | 
| `enableIdentityCrawler` | Specify `true` to activate identity crawler. Identity crawler is activated by default. See [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler) for more information. | `boolean` | Yes | 
| `syncMode` | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents.  | `string`<br />Valid values are `FORCED_FULL_CRAWL` and `FULL_CRAWL`. You can choose between the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index  | Yes | 
| `secretARN` | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs required to connect to your Confluence instance. | `string`<br />The minimum length is 20 and the maximum length is 2,048 characters. If you use basic authentication, the secret must contain a JSON structure with the following keys: <pre>{<br />    "username": "{{Confluence account user name}}",<br />    "password": "{{Confluence API token}}"<br />}</pre>If you use OAuth 2.0 authentication, the secret must contain a JSON structure with the following keys: <pre>{<br />    "confluenceAppKey": "{{app key for your Confluence account}}",<br />    "confluenceAppSecret": "{{app secret from your Confluence token}}",<br />    "confluenceAccessToken": "{{access token created in Confluence}}",<br />    "confluenceRefreshToken": "{{refresh token created in Confluence}}"<br />}</pre> | Yes | 
| `version` | The version of this template that's currently supported. | `string` | No | 

## Confluence (Cloud) JSON schema for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-json"></a>

The following is the Confluence (Cloud) JSON schema and examples for the configuration property for AWS CloudFormation.

**Topics**
+ [Confluence (Cloud) JSON schema for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-json-schema)
+ [Confluence (Cloud) JSON schema example for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-json-example)

### Confluence (Cloud) JSON schema for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-json-schema"></a>

The following is the Confluence (Cloud) JSON schema for the configuration property for CloudFormation

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

### Confluence (Cloud) JSON schema example for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-json-example"></a>

The following is the Confluence (Cloud) JSON schema example for the configuration property for CloudFormation

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

## Confluence (Cloud) YAML schema for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-yaml"></a>

The following is the Confluence (Cloud) YAML schema and examples for the configuration property for AWS CloudFormation:

**Topics**
+ [Confluence (Cloud) YAML schema for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml-schema)
+ [Confluence (Cloud) YAML schema example for using the configuration property with AWS CloudFormation](#confluence-cloud-cfn-yaml-example)

### Confluence (Cloud) YAML schema for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-yaml-schema"></a>

The following is the Confluence (Cloud) YAML schema for the configuration property for CloudFormation.

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

### Confluence (Cloud) YAML schema example for using the configuration property with AWS CloudFormation
<a name="confluence-cloud-cfn-yaml-example"></a>

The following is the Confluence (Cloud) YAML example for the Configuration property for CloudFormation:

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