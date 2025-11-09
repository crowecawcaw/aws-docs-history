# Connecting Amazon Q Business to Smartsheet

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## JSON schema

The following is the Smartsheet JSON schema:

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
            "authType": {
              "type": "string",
              "enum": [
                "APIToken"
              ]
            }
          },
          "required": [
            "authType"
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
        "sheet": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "sheetAttachment": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "sheetConversation": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "sheetConversationAttachment": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "rowAttachment": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "rowConversation": {
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
          },
          "required": [
            "fieldMappings"
          ]
        },
        "rowConversationAttachment": {
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
        "workspaceIds": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "maxItems": 20
        },
        "sheetIds": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "maxItems": 20
        },
        "folderIds": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "maxItems": 20
        },
        "fieldForUserId": {
          "type": "string"
        },
        "userType": {
          "type": "string"
        },
        "isCrawlAcl": {
          "type": "boolean"
        },
        "isCrawlSheets": {
          "type": "boolean"
        },
        "isCrawlSheetAttachments": {
          "type": "boolean"
        },
        "isCrawlSheetConversations": {
          "type": "boolean"
        },
        "isCrawlSheetConversationAttachments": {
          "type": "boolean"
        },
        "isCrawlRows": {
          "type": "boolean"
        },
        "isCrawlRowAttachments": {
          "type": "boolean"
        },
        "isCrawlRowConversations": {
          "type": "boolean"
        },
        "isCrawlRowConversationAttachments": {
          "type": "boolean"
        },
        "isCrawlRowProofs": {
          "type": "boolean"
        },
        "isMetadataAppended": {
          "type": "boolean"
        },
        "isConversationAppended": {
          "type": "boolean"
        },
        "inclusionAttachmentTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionAttachmentTypePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionAttachmentNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionAttachmentNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFolderNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFolderNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionSheetNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionSheetNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "enableDeletionProtection": {
          "type": "boolean",
          "default": false
        },
        "deletionProtectionThreshold": {
          "type": "string",
          "default": "15"
        }
      },
      "not": {
        "properties": {
          "workspaceIds": { "maxItems": 0 },
          "sheetIds": { "maxItems": 0 },
          "folderIds": { "maxItems": 0 }
        }
      }
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "type": {
      "type": "string",
      "pattern": "SMARTSHEET"
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
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure.

| Configuration                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required                  |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| `connectionConfiguration`                                     | Configuration details for connecting to the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `connectionConfiguration.repositoryEndpointMetadata`          | Metadata for the repository endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `connectionConfiguration.repositoryEndpointMetadata.authType` | The authentication type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`<br>The only allowed value is:<br>• `APIToken`                                                                                                                                                                                                                                                                                                                                                                                                             | Yes                       |
| `repositoryConfigurations`                                    | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `repositoryConfigurations.sheet`                              | Configuration for Smartsheet sheets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.sheet.fieldMappings`                | Field mappings for Smartsheet sheets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `array` of `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes (if sheet is present) |
| `repositoryConfigurations.sheetAttachment`                    | Configuration for Smartsheet sheet attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.sheetConversation`                  | Configuration for Smartsheet sheet conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.sheetConversationAttachment`        | Configuration for Smartsheet sheet conversation attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.row`                                | Configuration for Smartsheet rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.rowAttachment`                      | Configuration for row attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.rowConversation`                    | Configuration for Smartsheet row conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.rowConversationAttachment`          | Configuration for Smartsheet row conversation attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.proofAttachment`                    | Configuration for Smartsheet proof attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.proofConversation`                  | Configuration for Smartsheet proof conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `repositoryConfigurations.proofConversationAttachment`        | Configuration for Smartsheet proof conversation attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `additionalProperties`                                        | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `object`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `additionalProperties.workspaceIds`                           | List of Smartsheet workspace IDs to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.sheetIds`                               | List of Smartsheet sheet IDs to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.folderIds`                              | List of Smartsheet folder IDs to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.fieldForUserId`                         | Field for user ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `additionalProperties.userType`                               | User type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `additionalProperties.isCrawlAcl`                             | Whether to crawl ACL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlSheets`                          | Whether to crawl Smartsheet sheets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlSheetAttachments`                | Whether to crawl Smartsheet sheet attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlSheetConversations`              | Whether to crawl Smartsheet sheet conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlSheetConversationAttachments`    | Whether to crawl Smartsheet sheet conversation attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlRows`                            | Whether to crawl Smartsheet rows.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlRowAttachments`                  | Whether to crawl Smartsheet row attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlRowConversations`                | Whether to crawl Smartsheet row conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlRowConversationAttachments`      | Whether to crawl Smartsheet row conversation attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isCrawlRowProofs`                       | Whether to crawl Smartsheet row proofs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isMetadataAppended`                     | Whether to append Smartsheet metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.isConversationAppended`                 | Whether to append Smartsheet conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.inclusionAttachmentTypePatterns`        | Patterns for including Smartsheet attachment types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.exclusionAttachmentTypePatterns`        | Patterns for excluding Smartsheet attachment types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.inclusionAttachmentNamePatterns`        | Patterns for including Smartsheet attachment names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.exclusionAttachmentNamePatterns`        | Patterns for excluding Smartsheet attachment names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.inclusionFolderNamePatterns`            | Patterns for including Smartsheet folder names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.exclusionFolderNamePatterns`            | Patterns for excluding Smartsheet folder names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.inclusionSheetNamePatterns`             | Patterns for including Smartsheet sheet names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.exclusionSheetNamePatterns`             | Patterns for excluding Smartsheet sheet names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `array` of `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                        |
| `additionalProperties.enableDeletionProtection`               | Whether to enable deletion protection. To learn more, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard").                                                                                                                                                                                                                                                                                                                                                                                                                                   | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `additionalProperties.deletionProtectionThreshold`            | Threshold for deletion protection. To learn more, see [Document deletion safeguard](connector-concepts.md#document-deletion-safeguard "connector-concepts.md#document-deletion-safeguard")                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                        |
| `enableIdentityCrawler`                                       | Whether to enable the identity crawler. Identity crawler is activated by default.<br>Crawling identity information on users and groups with access to certain documents is<br>useful for user context filtering. Search results are filtered based on the user or<br>their group access to documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                        |
| `syncMode`                                                    | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`<br>The allowed values are:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.<br>• Use `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index. | Yes                       |
| `secretArn`                                                   | The ARN of the secret containing the Smartsheet credentials required to<br>connect Amazon Q Business to Smartsheet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `string`<br>The minimum length is 20 and the maximum length is 2,048 characters.                                                                                                                                                                                                                                                                                                                                                                                   | Yes                       |
| `type`                                                        | The type of the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `string`<br>The only allowed value is:<br>• `SMARTSHEET`                                                                                                                                                                                                                                                                                                                                                                                                           | Yes                       |
| `version`                                                     | The version of the template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string`<br>Must match the pattern "1.0.0".                                                                                                                                                                                                                                                                                                                                                                                                                        | No                        |
