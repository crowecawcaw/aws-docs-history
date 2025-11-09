# Connecting Amazon Q Business to Microsoft Yammer

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Yammer JSON schema

The following is the Yammer JSON schema:

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
        "community": {
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
                          "DATE"
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
        "user": {
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
                          "DATE"
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
        "message": {
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
                          "DATE"
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
        "attachment": {
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
                          "DATE"
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
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "sinceDate": {
          "type": "string",
          "pattern": "^(19|2[0-9])[0-9]{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])((\\+|-)(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]))?$"
        },
        "communityNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlMessage": {
          "type": "boolean"
        },
        "isCrawlAttachment": {
          "type": "boolean"
        },
        "isCrawlPrivateMessage": {
          "type": "boolean"
        }
      },
      "required": [
        "sinceDate"
      ]
    },
    "type": {
      "type": "string",
      "pattern": "YAMMER"
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "useChangeLog": {
      "type": "string",
      "enum": [
        "true",
        "false"
      ]
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
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
    "secretArn",
    "syncMode"
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure.

| Configuration                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `connectionConfiguration`                                                | Configuration information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `repositoryEndpointMetadata`                                             | The endpoint information for the data source. This data source doesn't specify an<br>endpoint in `repositoryEndpointMetadata`. Rather, the connection information<br>is included in an AWS Secrets Manager secret that you provide the<br>`secretArn`.                                                                                                                                                                                                                                                                                                                                                                         |
| `repositoryConfigurations`                                               | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| • `community`<br>• `user`<br>• `message`<br>• `attachment`               | A list of objects that map attributes or field names of Microsoft<br>Yammer objects to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `secretARN`                                                              | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Microsoft Yammer data<br>source. This includes your client ID and client secret.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `additionalProperties`                                                   | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `isCrawlAcl`                                                             | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                                                                        |
| `maxFileSizeInMegaBytes`                                                 | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                                                                                                                                                                      |
| `fieldForUserId`                                                         | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| • `isCrawlMessage`<br>• `isCrawlAttachment`<br>• `isCrawlPrivateMessage` | Input `TRUE` to index                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| • `sinceDate`                                                            | Use to specify the time from when Amazon Q should crawl your Microsoft<br>Yammer content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| • `communityNameFilter`                                                  | Use to specify community names to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `inclusionPatterns`                                                      | A list of regular expression patterns to \*include<br>• specific<br>files in your Yammer data source. Files that match the patterns are<br>included in the index. File that don't match the patterns are excluded from the index.<br>Files that match the patterns are included in the index. Files that don't match the<br>patterns are excluded from the index. If a file matches both an inclusion and exclusion<br>pattern, the exclusion pattern takes precedence and the file isn't included in the<br>index.                                                                                                            |
| `exclusionPatterns`                                                      | A list of regular expression patterns to \*exclude<br>• specific<br>files in your Yammer data source. Files that match the patterns are<br>excluded from the files in your data source. Files that match the patterns are excluded<br>from the index. Files that don't match the patterns are included in the index. If a file<br>matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence<br>and the file isn't included in the index.                                                                                                                                                         |
| `type`                                                                   | Specify `YAMMER` as your data source type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `useChangeLog`                                                           | `true` to use the Yammer change log to determine which<br>documents require adding, updating, or deleting in the index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `syncMode`                                                               | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents. You can choose between the<br>following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and<br>deleted content each time your data source syncs with your index<br>• Use `CHANGE_LOG` to incrementally crawl only new and modified<br>content each time your data source syncs with your index                             |
| `enableIdentityCrawler`                                                  | `true` to activate identity crawler. Identity crawler is activated by<br>default. Crawling identity information on users and groups with access to certain<br>documents is useful for user context filtering. Search results are filtered based on the<br>user or their group access to documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
