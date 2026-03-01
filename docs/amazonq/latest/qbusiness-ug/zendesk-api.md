# Connecting Amazon Q Business to Zendesk using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## JSON schema

The following is the Zendesk JSON schema:

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
            "hostUrl": {
              "type": "string",
              "pattern": "https:.*"
            }
          },
          "required": [
            "hostUrl"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "ticket": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "ticketComment": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "ticketCommentAttachment": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "article": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "communityPostComment": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "articleComment": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "articleAttachment": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
        "communityTopic": {
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
                        "enum": ["STRING", "STRING_LIST", "LONG", "DATE"]
                      },
                      "dataSourceFieldName": {
                        "type": "string"
                      },
                      "dateFieldFormat": {
                        "type": "string",
                        "pattern": "dd-MM-yyyy HH:mm:ss"
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
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
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
        "organizationNameFilter": {
          "type": "array"
        },
        "sinceDate": {
          "type": "string",
          "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$"
        },
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "isCrawTicket": {
          "type": "string"
        },
        "isCrawTicketComment": {
          "type": "string"
        },
        "isCrawTicketCommentAttachment": {
          "type": "string"
        },
        "isCrawlArticle": {
          "type": "string"
        },
        "isCrawlArticleAttachment": {
          "type": "string"
        },
        "isCrawlArticleComment": {
          "type": "string"
        },
        "isCrawlCommunityTopic": {
          "type": "string"
        },
        "isCrawlCommunityPost": {
          "type": "string"
        },
        "isCrawlCommunityPostComment": {
          "type": "string"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "ZENDESK"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "enableIdentityCrawler": {
      "type": "boolean"
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
  "additionalProperties": false,
  "required": [
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties",
    "syncMode",
    "secretArn",
    "type"
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure.

| Configuration                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                                                                                                                                                                                                                          | Configuration information for the endpoint of the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `repositoryEndpointMetadata`                                                                                                                                                                                                                                       | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `hostURL`                                                                                                                                                                                                                                                          | The Zendesk host URL. For example,<br>*https://yoursubdomain.zendesk.com*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `repositoryConfigurations`                                                                                                                                                                                                                                         | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| • `ticket`<br>• `ticketComment`<br>• `ticketCommentAttachment`<br>• `article`<br>• `articleComment`<br>• `articleAttachment`<br>• `communityTopic`<br>• `communityPost`<br>• `communityPostComment`                                                                | A list of Zendesk objects and their metadata attributes that Amazon Q crawls and maps to Amazon Q index field names. The<br>Zendesk data source field names must exist in your Zendesk custom<br>metadata.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `secretARN`                                                                                                                                                                                                                                                        | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Zendesk. The secret must<br>contain a JSON structure with the following keys: host URL, client ID, client secret,<br>username, and password.                                                                                                                                                                                                                                                                                                                                                          |
| `additionalProperties`                                                                                                                                                                                                                                             | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `isCrawlAcl`                                                                                                                                                                                                                                                       | `true` to crawl Access Control Lists. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                                                                                                             |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                                                           | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                                                                                                                                                                              |
| `fieldForUserId`                                                                                                                                                                                                                                                   | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `organizationFilter`                                                                                                                                                                                                                                               | If you want, you can choose to index tickets that exist within a specific<br>**Organization**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sinceDate`                                                                                                                                                                                                                                                        | If you want, you can configure a `sinceDate` parameter so that the<br>Zendesk connector will crawl based on the `sinceDate`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `inclusionPatterns`                                                                                                                                                                                                                                                | A list of regular expression patterns to \*include<br>• specific<br>files in your Zendesk data source. Files that match the patterns are included<br>in the index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence,<br>and the file isn't included in the index.                                                                                                                                                                                                                                                 |
| `exclusionPatterns`                                                                                                                                                                                                                                                | A list of regular expression patterns to \*exclude<br>• specific<br>files in your Zendesk data source. Files that match the patterns are excluded<br>from the index. Files that don't match the patterns are included in the index. If a file<br>matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence,<br>and the file isn't included in the index.                                                                                                                                                                                                                                                 |
| • `isCrawlTicket`<br>• `isCrawlTicketComment`<br>• `isCrawlTicketCommentAttachment`<br>• `isCrawlArticle`<br>• `isCrawlArticleComment`<br>• `isCrawlArticleAttachment`<br>• `isCrawlCommunityTopic`<br>• `isCrawlCommunityPost`<br>• `isCrawlCommunityPostComment` | Input `true` to index these types of content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `type`                                                                                                                                                                                                                                                             | Specify `ZENDESK` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `syncMode`                                                                                                                                                                                                                                                         | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents. You can choose between the<br>following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.<br>• Use `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index.                            |
| `enableIdentityCrawler`                                                                                                                                                                                                                                            | Specify `true` to activate identity crawler. Identity crawler is<br>activated by default. Crawling identity information on users and groups with access to<br>certain documents is useful for user context filtering. Search results are filtered<br>based on the user or their group access to documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `version`                                                                                                                                                                                                                                                          | The version of the template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
