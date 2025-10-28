# Connecting Amazon Q Business to

Alfresco (Cloud) using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Alfresco JSON schema

The following is the Alfresco JSON schema:

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "siteId": {
              "type": "string"
            },
            "repoUrl": {
              "type": "string"
            },
            "webAppUrl": {
              "type": "string"
            },
            "repositoryAdditionalProperties": {
              "type": "object",
              "properties": {
                "authType": {
                  "type": "string",
                  "enum": [
                    "OAuth2",
                    "Basic"
                  ]
                },
                "type": {
                  "type": "string",
                  "enum": [
                    "PAAS",
                    "ON_PREM"
                  ]
                },
                "crawlType": {
                  "type": "string",
                  "enum": [
                    "ASPECT",
                    "SITE_ID",
                    "ALL_SITES"
                  ]
                }
              }
            }
          }
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE",
                          "STRING_LIST",
                          "LONG"
                        ]
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
            }
          },
          "required": [
            "fieldMappings"
          ]
        },
        "comment": {
          "type": "object",
          "properties": {
            "fieldMappings": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "indexFieldName": {
                        "type": "string"
                      },
                      "indexFieldType": {
                        "type": "string",
                        "enum": [
                          "STRING",
                          "DATE",
                          "STRING_LIST",
                          "LONG"
                        ]
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
            }
          },
          "required": [
            "fieldMappings"
          ]
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "isCrawlAcl": {
          "type": "boolean"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "fieldForUserId": {
          "type": "string"
        },
        "aspectName": {
          "type": "string"
        },
        "aspectProperties": {
          "type": "array"
        },
        "enableFineGrainedControl": {
          "type": "boolean"
        },
        "isCrawlComment": {
          "type": "boolean"
        },
        "inclusionFileNamePatterns": {
          "type": "array"
        },
        "exclusionFileNamePatterns": {
          "type": "array"
        },
        "inclusionFileTypePatterns": {
          "type": "array"
        },
        "exclusionFileTypePatterns": {
          "type": "array"
        },
        "inclusionFilePathPatterns": {
          "type": "array"
        },
        "exclusionFilePathPatterns": {
          "type": "array"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "ALFRESCO"
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "enableIdentityCrawler": {
      "type": "boolean"
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
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "type",
    "secretArn"
  ]
}
```

The following table provides information about important JSON keys to
configure.

| Configuration                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                                                             | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                |
| `repositoryEndpointMetadata`                                                                          | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `siteId`                                                                                              | The identifier of the Alfresco site.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `repoUrl`                                                                                             | The URL of your Alfresco repository. You can get the repository URL from your Alfresco administrator. For example, if you use Alfresco Cloud (PaaS), the repository URL could be *https://company.alfrescocloud.com*. Or, if you use Alfresco On-Premises, the repository URL could be *https://company-alfresco-instance.company-domain.suffix:port*.                                                                                                         |
| `webAppUrl`                                                                                           | The URL of your Alfresco user interface. You can get the Alfresco user interface URL from your Alfresco administrator. For example, the user interface URL could be *https://example.com*.                                                                                                                                                                                                                                                                     |
| `repositoryAdditionalProperties`                                                                      | Additional properties for content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `isCrawlAcl`                                                                                          | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information to ensure responses are generated only from documents your end users have access to by default. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                           |
| `fieldForUserId`                                                                                      | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `authType`                                                                                            | The type of authentication that you use, whether `OAuth2` or `Basic`.                                                                                                                                                                                                                                                                                                                                                                                          |
| `type (deployment)`                                                                                   | The type of Alfresco that you use, whether `PAAS` or `ON-PREM`.                                                                                                                                                                                                                                                                                                                                                                                                |
| `crawlType`                                                                                           | The type of content that you want to crawl, whether `ASPECT` (content marked with 'Aspects' in Alfresco), `SITE_ID` (content within a specific Alfresco site), or `ALL_SITES` (content across all your Alfresco sites).                                                                                                                                                                                                                                        |
| `repositoryConfigurations`                                                                            | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                           |
| <br>• `document` <br>• `comment`                                                                      | A list of objects that map the attributes or field names of your Alfresco documents and comments to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                |
| `additionalProperties`                                                                                | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                         |
| `maxFileSizeInMegaBytes`                                                                              | Specify the Maximum file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB.                                                                                                                                                                                                      |
| `aspectProperties`                                                                                    | A list of specific 'Aspects' content that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `enableFineGrainedControl`                                                                            | `true` to crawl 'Aspects'.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `isCrawlComment`                                                                                      | `true` to index comments.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <br>• `inclusionFileNamePatterns` <br>• `inclusionFileTypePatterns` <br>• `inclusionFilePathPatterns` | A list of regular expression patterns to include certain files in your Alfresco data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index.                                                                                            |
| <br>• `exclusionFileNamePatterns` <br>• `exclusionFileTypePatterns` <br>• `exclusionFilePathPatterns` | A list of regular expression patterns to exclude certain files in your Alfresco data source. Files that match the patterns are excluded from the index. Files that don't match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index.                                                                                            |
| `type`                                                                                                | The type of data source. Specify `ALFRESCO` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                          |
| `secretArn`                                                                                           | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key-value pairs that are required to connect to your Alfresco. The secret must contain a JSON structure with the following keys: If using basic authentication: ``{ "username": "`username`", "password": "`password`" }`` If using OAuth 2.0 authentication: ``{ "clientId": "`client ID`", "clientSecret": "`client secret`", "tokenUrl": "`token URL`" }``                |
| `syncMode`                                                                                            | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. You can choose between the following options: <br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index. <br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index.    |
| `enableIdentityCrawler`                                                                               | `true` to use the Amazon Q identity crawler to sync identity/principal information on users and groups with access to certain documents. NoteAmazon Q Business crawls identity information from your data source to ensure responses are generated only from documents end users have access to by default. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `version`                                                                                             | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                       |
