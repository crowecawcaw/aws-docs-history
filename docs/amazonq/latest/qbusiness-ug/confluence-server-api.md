

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Confluence (Server/Data Center) using APIs
<a name="confluence-server-api"></a>

You use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) action to connect a data source to your Amazon Q application. You can also use the [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) action to modify an existing data source configuration.

Then, you use the `configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) in the Amazon Q API Reference.

**Topics**
+ [Confluence (Server/Data Center) configuration properties](#confluence-server-configuration-keys)
+ [Confluence (Server/Data Center) JSON schema](#confluence-server-json)
+ [Confluence (Server/Data Center) JSON schema example](#confluence-server-api-json-example)

## Confluence (Server/Data Center) configuration properties
<a name="confluence-server-configuration-keys"></a>

The following provides information about important configuration properties required in the schema.


| Configuration | Description | Type | Required | 
| --- | --- | --- | --- | 
| `connectionConfiguration` | Configuration information for the endpoint for the data source. | `object`<br />This property has the following sub-property: `repositoryEndpointMetadata`. | Yes | 
| `repositoryEndpointMetadata` | The endpoint information for the data source. | `object`<br />This property has the following sub-properties: `hostUrl`, `type`, and `authType`. | Yes | 
| `hostUrl` | The URL for your Confluence instance. For example, {{https://example.confluence.com}}.  If you change or update your Confluence (Server/Data Center) data source URL, you also need to update your Secrets Manager secret to ensure a secure connection.  | `string`<br />Specify the URL in the pattern `https://*` | Yes | 
| `type` | The hosting method for your Confluence instance. | `string`<br />The allowed values are `SAAS` or `ON_PREM`. | Yes | 
| `authType` | The authentication method for your Confluence instance. | `string`<br />The allowed values are `Basic`, `OAuth2`, or `Personal-token`. | Yes | 
| `repositoryConfigurations` | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. | `object`<br />This property has the following sub-properties: `space`, `page`, `blog`, `comment`, and `attachment`. | Yes | 
|  +  `space` <br />+  `page` <br />+  `blog` <br />+  `comment` <br />+  `attachment`   | A list of objects that map the attributes or field names of your Confluence spaces, pages, blogs, comments, and attachments to Amazon Q index field names. | `object`<br />These properties have the following sub-properties.+  `indexFieldName` <br />+  `indexFieldType` <br />+  `dataSourceFieldName` <br />+  `dateFieldFormat`  | No | 
| `indexFieldName` | The field name of your Confluence spaces, pages, blogs, comments, or attachments. | `string` | Yes | 
| `indexFieldType` | The field type of your Confluence spaces, pages, blogs, comments, or attachments. | `string`<br />The allowed values are `STRING`, `STRING_LIST`, and `DATE`. | Yes | 
| `dataSourceFieldName` | The data source field name of your Confluence spaces, pages, blogs, comments, or attachments. | `string` | Yes | 
| `dateFieldFormat` | The date format of your Confluence spaces, pages, blogs, comments, or attachments. | `string`<br />Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'` | No | 
| `additionalProperties` | Additional configuration options for your content in your data source. | `object`<br />This property has the following sub-properties.+  `isCrawlAcl` <br />+  `isRotateSecret` <br />+  `isCrawlPersonalSpace` <br />+  `isCrawlArchivedSpace` <br />+  `isCrawlArchivedPage` <br />+  `isCrawlPage` <br />+  `isCrawlBlog` <br />+  `isCrawlPageComment` <br />+  `isCrawlPageAttachment` <br />+  `isCrawlBlogComment` <br />+  `isCrawlBlogAttachment` <br />+  `fieldForUserId` <br />+  `maxFileSizeInMegaBytes` <br />+  `inclusionSpaceKeyFilter` <br />+  `exclusionSpaceKeyFilter` <br />+  `pageTitleRegEX` <br />+  `blogTitleRegEX` <br />+  `commentTitleRegEX` <br />+  `attachmentTitleRegEX` <br />+  `inclusionFileTypePatterns` <br />+  `exclusionFileTypePatterns` <br />+  `inclusionUrlPatterns` <br />+  `exclusionUrlPatterns` <br />+  `proxyHost` <br />+  `proxyPort`  | Yes | 
| `isCrawlAcl` | Specify true to crawl access control information from documents.  Amazon Q Business crawls ACL information to ensure responses are generated only from documents your end users have access to by default. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.  | `boolean` | No | 
| `isRotateSecret` | Specify true if you want to automatically rotate the secret. | `boolean` | No | 
| `fieldForUserId` | Specify field to use for UserId for ACL crawling. | `string` | No | 
| `proxyHost` | The host where the web proxy is required. The host name should be without protocol (http:// or https://). | `string` | No | 
| `proxyPort` | Port used by the host URL transport protocol. The port number should be a numeric value between 0 and 65535. | `string` | No | 
| `maxFileSizeInMegaBytes` | Specify the file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB. | `string` | No | 
| +  `inclusionSpaceKeyFilter` <br />+  `exclusionSpaceKeyFilter` <br />+  `pageTitleRegEX` <br />+  `blogTitleRegEX` <br />+  `commentTitleRegEX` <br />+  `attachmentTitleRegEX` <br />+  `inclusionFileTypePatterns` <br />+  `exclusionFileTypePatterns` <br />+  `inclusionUrlPatterns` <br />+  `exclusionUrlPatterns`  | A list of regular expression patterns to include and/or exclude certain files in your Confluence data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index. | `array (string)` | No | 
|  +  `isCrawlPersonalSpace` <br />+  `isCrawlArchivedSpace` <br />+  `isCrawlArchivedPage` <br />+  `isCrawlPage` <br />+  `isCrawlBlog` <br />+  `isCrawlPageComment` <br />+  `isCrawlPageAttachment` <br />+  `isCrawlBlogComment` <br />+  `isCrawlBlogAttachment`   | `true` to index files in your Confluence personal spaces, pages, blogs, page comments, page attachments, blog comments, and blog attachments. | `boolean` | No | 
| `type` | The type of data source. We recommend that you use CONFLUENCEV2 as your data source type. | `string`<br />The allowed values are `CONFLUENCEV2` and `CONFLUENCE`. | Yes | 
| `enableIdentityCrawler` | `true` to activate identity crawler. Identity crawler is activated by default. Amazon Q Business crawls identity information from your data source to ensure responses are generated only from documents end users have access to by default. For more information, see [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler).  | `boolean` | Yes | 
| `syncMode` | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. | `string`<br />Valid values are `FORCED_FULL_CRAWL` and `FULL_CRAWL`. You can choose between the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index  | Yes | 
| `secretARN` | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs required to connect to your Confluence instance. | `string`<br />If you use OAuth 2.0 authentication, the secret must contain a JSON structure with the following keys:<pre>{<br />    "confluenceAppKey": "{{client ID for your Confluence account}}",<br />    "confluenceAppSecret": "{{client secret from your Confluence token}}",<br />    "confluenceAccessToken": "{{access token created in Confluence}}",<br />    "confluenceRefreshToken": "{{refresh token created in Confluence}}"<br />}</pre>(For Confluence Server/Data Center only) If you use basic authentication, the secret is stored in a JSON structure with the following keys: <pre>{<br />    "username": "{{Confluence Server/Data Center username}}",<br />    "password": "{{Confluence Server/Data Center password}}"<br />}</pre>(For Confluence Server/Data Center only) If you use Personal Access Token authentication, the secret is stored in a JSON structure with the following keys: <pre>{<br />    "hostUrl": "{{ Confluence  Server/Data Center host URL}}",<br />    "patToken": "{{ Confluence  token}}"<br />}</pre> | Yes | 
| `version` | The version of this template that's currently supported. | `string` | No | 

## Confluence (Server/Data Center) JSON schema
<a name="confluence-server-json"></a>

The following is the Confluence (Server/Data Center) JSON schema:

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
            "hostUrl": {
              "type": "string",
              "pattern": "https:.*"
            },
            "type": {
              "type": "string",
              "enum": ["ON_PREM"]
            },
            "authType": {
              "type": "string",
              "enum": ["Basic", "OAuth2", "Personal-token"]
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

## Confluence (Server/Data Center) JSON schema example
<a name="confluence-server-api-json-example"></a>

The following is the Confluence (Server/Data Center) JSON schema example:

```
{
  "type": "CONFLUENCEV2",
  "syncMode": "FULL_CRAWL",
  "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-confluence-secret",
  "enableIdentityCrawler": "true",
  "connectionConfiguration": {
    "repositoryEndpointMetadata": {
      "hostUrl": "https://mycompany.atlassian.net",
      "type": "ON_PREM",
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
```