# Connecting Amazon Q Business to Microsoft Teams (Original connector)

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Microsoft Teams configuration

properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`                                                                                                                                                                                                                           | Configuration information for endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `object`<br>This property has the following sub-property:<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                                                                                                        | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `object`<br>This property has the following sub-property:<br>`tenantId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `tenantId`                                                                                                                                                                                                                                          | The Microsoft 365 tenant ID. You can find your tenant ID in the Properties of your<br>Azure Active Directory Portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>The string must be 36 characters long and in in the pattern:<br>^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `repositoryConfigurations`                                                                                                                                                                                                                          | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `object`<br>This property has the following sub-properties:<br>• `chatMessage`<br>• `chatAttachment`<br>• `channelPost`<br>• `channelWiki`<br>• `channelAttachment`<br>• `meetingChat`<br>• `meetingFile`<br>• `meetingNote`<br>• `calendarMeeting`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| • `chatMessage`<br>• `chatAttachment`<br>• `channelPost`<br>• `channelWiki`<br>• `channelAttachment`<br>• `meetingChat`<br>• `meetingFile`<br>• `meetingNote`<br>• `calendarMeeting`                                                                | A list of objects that map the attributes or field names of your Microsoft<br>Teams content to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `object`<br>These properties have the following sub-properties: `indexFieldName`,<br>`indexFieldType`, `dataSourceFieldName`, and<br>`dateFieldFormat`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `indexFieldName`                                                                                                                                                                                                                                    | The field name of your Microsoft Teams assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `indexFieldType`                                                                                                                                                                                                                                    | The field type of your Microsoft Teams assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`<br>The allowed values are `STRING`, `STRING_LIST`,<br>`DATE`, and `LONG`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes      |
| `dataSourceFieldName`                                                                                                                                                                                                                               | The data source field name of your Microsoft Teams assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `dateFieldFormat`                                                                                                                                                                                                                                   | The date format of your Microsoft Teams assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `additionalProperties`                                                                                                                                                                                                                              | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `object`<br>This property has the following sub-properties.<br>• `isCrawlAcl`<br>• `isCrawlChatMessage`<br>• `isCrawlChatAttachment`<br>• `isCrawlChannelPost`<br>• `isCrawlChannelAttachment`<br>• `isCrawlChannelWiki`<br>• `isCrawlCalendarMeeting`<br>• `isCrawlMeetingChat`<br>• `isCrawlMeetingFile`<br>• `isCrawlMeetingNote`<br>• `startCalendarDateTime`<br>• `endCalendarDateTime`<br>• `fieldForUserId`<br>• `paymentModel`<br>• `maxFileSizeInMegaBytes`<br>• `inclusionTeamNameFilter`<br>• `exclusionTeamNameFilter`<br>• `inclusionChannelNameFilter`<br>• `exclusionChannelNameFilter`<br>• `inclusionFileNamePatterns`<br>• `exclusionFileNamePatterns`<br>• `inclusionFileTypePatterns`<br>• `exclusionFileTypePatterns`<br>• `inclusionUserEmailFilter` | Yes      |
| `isCrawlAcl`                                                                                                                                                                                                                                        | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                                 | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `maxFileSizeInMegaBytes`                                                                                                                                                                                                                            | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `fieldForUserId`                                                                                                                                                                                                                                    | Specify the field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| • `isCrawlChatMessage`<br>• `isCrawlChatAttachment`<br>• `isCrawlChannelPost`<br>• `isCrawlChannelAttachment`<br>• `isCrawlChannelWiki`<br>• `isCrawlCalendarMeeting`<br>• `isCrawlMeetingChat`<br>• `isCrawlMeetingFile`<br>• `isCrawlMeetingNote` | Specify `true` to index this content in your<br>Microsoft Teams data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| • `inclusionTeamNameFilter`<br>• `inclusionChannelNameFilter`<br>• `inclusionFileNamePatterns`<br>• `inclusionFileTypePatterns`<br>• `inclusionUserEmailFilter`                                                                                     | A list of regular expression patterns to include specific content in your<br>Microsoft Teams data source. Content that matches the patterns are included in the<br>index. Content that doesn't match the patterns are excluded from the index. If any<br>content matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the content isn't included in the index.                                                                                                                                                                               | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| • `exclusionTeamNameFilter`<br>• `exclusionChannelNameFilter`<br>• `exclusionFileNamePatterns`<br>• `exclusionFileTypePatterns`                                                                                                                     | A list of regular expression patterns to exclude specific content in your<br>Microsoft Teams data source. Content that matches the patterns are excluded from the<br>index. Content that doesn't match the patterns are included in the index. If any content<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence,<br>and the content isn't included in the index.                                                                                                                                                                               | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| • `startCalendarDateTime`<br>• `endCalendarDateTime`                                                                                                                                                                                                | You can choose to configure a `startCalendarDateTime` and<br>`endCalendarDateTime` parameters so that the Microsoft Teams connector<br>crawls content based on a specific date range.                                                                                                                                                                                                                                                                                                                                                                                                   | `string`<br>Specify the date in the form<br>`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `paymentModel`                                                                                                                                                                                                                                      | Specifies what type of payment model to use with your Teams data<br>source. Model A payment models are restricted to licensing and payment models that<br>require security compliance. Model B payment models are suitable for licensing and<br>payment models that don't require security compliance.                                                                                                                                                                                                                                                                                  | `string`<br>Valid values are `A`, `B`, and `Evaluation<br>Mode`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No       |
| `syncMode`                                                                                                                                                                                                                                          | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.<br>• Use `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index.                                                                                                                                                                                                                                                                                   | Yes      |
| `secretARN`                                                                                                                                                                                                                                         | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your<br>Microsoft Teams.                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>The secret must contain a JSON structure with the following keys:<br>``<br>{<br>"clientId": `String`,<br>"clientSecret": `String`<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `type`                                                                                                                                                                                                                                              | The type of data source. Specify `MSTEAMS` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| `enableIdentityCrawler`                                                                                                                                                                                                                             | `true` to activate identity crawler.Crawling identity information<br>on users and groups with access to specific documents is useful for user context<br>filtering. Search results are filtered based on the user or their group access to<br>documents.<br>NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `version`                                                                                                                                                                                                                                           | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |

## Microsoft Teams JSON schema

The following is the Microsoft Teams JSON schema:

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "pattern": "MSTEAMS"
    },
    "syncMode": {
      "type": "string",
      "enum": ["FORCED_FULL_CRAWL", "FULL_CRAWL", "CHANGE_LOG"]
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
            }
          },
          "required": ["tenantId"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "chatMessage": {
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
        "chatAttachment": {
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
        "channelPost": {
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
        "channelWiki": {
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
        "channelAttachment": {
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
        "meetingChat": {
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
        "meetingFile": {
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
        "meetingNote": {
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
                      "enum": ["STRING", "DATE"]
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
        "calendarMeeting": {
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
                      "enum": ["STRING", "DATE"]
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
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "fieldForUserId": {
          "type": "string"
        },
        "paymentModel": {
          "type": "string",
          "enum": ["A", "B", "Evaluation Mode"]
        },
        "inclusionTeamNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionTeamNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionChannelNameFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionChannelNameFilter": {
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
        "inclusionUserEmailFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isCrawlChatMessage": {
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
        "isCrawlChatAttachment": {
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
        "isCrawlChannelPost": {
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
        "isCrawlChannelAttachment": {
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
        "isCrawlChannelWiki": {
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
        "isCrawlCalendarMeeting": {
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
        "isCrawlMeetingChat": {
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
        "isCrawlMeetingFile": {
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
        "isCrawlMeetingNote": {
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
        "startCalendarDateTime": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
        },
        "endCalendarDateTime": {
          "anyOf": [
            {
              "type": "string",
              "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
            },
            {
              "type": "string",
              "pattern": ""
            }
          ]
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
}
```

[Show moreShow less](# "#")

## Microsoft Teams JSON schema

example

The following is the Microsoft Teams JSON schema example:

```
{
  "type": "MSTEAMS",
  "syncMode": "FULL_CRAWL",
  "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-teams-secret",
  "enableIdentityCrawler": "true",
  "connectionConfiguration": {
    "repositoryEndpointMetadata": {
      "tenantId": "123e4567-e89b-12d3-a456-426614174000"
    }
  },
  "repositoryConfigurations": {
    "chatMessage": {
      "fieldMappings": [
        {
          "indexFieldName": "message_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "chatAttachment": {
      "fieldMappings": [
        {
          "indexFieldName": "attachment_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "channelPost": {
      "fieldMappings": [
        {
          "indexFieldName": "post_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "channelWiki": {
      "fieldMappings": [
        {
          "indexFieldName": "wiki_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "channelAttachment": {
      "fieldMappings": [
        {
          "indexFieldName": "attachment_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "meetingChat": {
      "fieldMappings": [
        {
          "indexFieldName": "meeting_chat_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "meetingFile": {
      "fieldMappings": [
        {
          "indexFieldName": "meeting_file_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "meetingNote": {
      "fieldMappings": [
        {
          "indexFieldName": "meeting_note_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "calendarMeeting": {
      "fieldMappings": [
        {
          "indexFieldName": "calendar_meeting_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    }
  },
  "additionalProperties": {
    "isCrawlAcl": "true",
    "maxFileSizeInMegaBytes": "50",
    "fieldForUserId": "user_id",
    "paymentModel": "A",
    "inclusionTeamNameFilter": ["TeamA", "TeamB"],
    "exclusionTeamNameFilter": ["TeamC"],
    "inclusionChannelNameFilter": ["Channel1", "Channel2"],
    "exclusionChannelNameFilter": ["Channel3"],
    "inclusionFileNamePatterns": ["*.docx", "*.pdf"],
    "exclusionFileNamePatterns": ["*.tmp"],
    "inclusionFileTypePatterns": ["image/png", "image/jpeg"],
    "exclusionFileTypePatterns": ["application/octet-stream"],
    "inclusionUserEmailFilter": ["user@example.com"],
    "isCrawlChatMessage": "true",
    "isCrawlChatAttachment": "true",
    "isCrawlChannelPost": "true",
    "isCrawlChannelAttachment": "true",
    "isCrawlChannelWiki": "true",
    "isCrawlCalendarMeeting": "true",
    "isCrawlMeetingChat": "true",
    "isCrawlMeetingFile": "true",
    "isCrawlMeetingNote": "true",
    "startCalendarDateTime": "2023-01-01T00:00:00Z",
    "endCalendarDateTime": "2023-12-31T23:59:59Z",
    "enableDeletionProtection": "false",
    "deletionProtectionThreshold": "15"
  }
}
```

[Show moreShow less](# "#")
