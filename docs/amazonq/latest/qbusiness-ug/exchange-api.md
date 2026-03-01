# Connecting Amazon Q Business to Microsoft Exchange using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Microsoft Exchange JSON schema

The following shows the Microsoft Exchange JSON schema:

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
            "tenantId": {
              "type": "string",
              "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
              "minLength": 36,
              "maxLength": 36
            }
          },
          "required": ["tenantId"]
        }
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "email": {
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
          "required": [
            "fieldMappings"
          ]
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
                      "enum": ["STRING", "DATE","LONG"]
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
        "calendar": {
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
          "required": [
            "fieldMappings"
          ]
        },
        "contacts": {
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
          "required": [
            "fieldMappings"
          ]
        },
        "notes": {
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
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": ["email"
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "exclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "s3bucketName": {
          "type": "string"
        },
        "inclusionUsersFileName": {
          "type": "string"
        },
        "exclusionUsersFileName": {
          "type": "string"
        },
        "inclusionDomainUsers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionDomainUsers": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "crawlCalendar": {
          "type": "boolean"
        },
        "crawlNotes": {
          "type": "boolean"
        },
        "crawlContacts": {
          "type": "boolean"
        },
        "crawlFolderAcl": {
          "type": "boolean"
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
        "subject": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "emailFrom": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "emailTo": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "email"
          }
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        }
      },
      "required": []
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "MSEXCHANGE"
    },
    "secretArn": {
      "type": "string"
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

| Configuration                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                                                               | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `repositoryEndpointMetadata`                                                                            | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tenantId`                                                                                              | The Microsoft 365 tenant ID. You can find your tenant ID in the Properties of your<br>Azure Active Directory Portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `repositoryConfigurations`                                                                              | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| • `email`<br>• `attachment`<br>• `calendar`<br>• `contacts`<br>• `notes`                                | A list of objects that map the attributes or field names of your Microsoft<br>Exchange data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `secretARN`                                                                                             | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Exchange data source. This includes your<br>client ID and your client secret.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `additionalProperties`                                                                                  | Additional configuration options for content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `inclusionPatterns`<br>• `inclusionUsersList`<br>• `inclusionUsersFileName`<br>• `inclusionDomainUsers` | A list of regular expression patterns to \*include<br>• specific<br>files in your Exchange data source. Files that match the patterns are included in the<br>index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence<br>and the file isn't included in the index.                                                                                                                                                                                                                                          |
| `exclusionPatterns`<br>• `exclusionUsersList`<br>• `exclusionUsersFileName`<br>• `exclusionDomainUsers` | A list of regular expression patterns to \*exclude<br>• specific<br>files in your Exchange data source. Files that match the patterns are excluded from the<br>index. Files that don't match the patterns are included in the index. If a file matches<br>both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the<br>file isn't included in the index.                                                                                                                                                                                                                                          |
| `startCalendarDateTime`                                                                                 | Use to specify the date and time for Calendar content to be crawled by Amazon Q.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `endCalendarDateTime`                                                                                   | Use to specify the date and time for Calendar content to be crawled by Amazon Q.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `subject`                                                                                               | Use to specify email subject lines to be crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `emailFrom`                                                                                             | Use to specify emails to be crawled based on sender.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `emailTo`                                                                                               | Use to specify emails to be crawled based on recipient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `maxFileSizeInMegaBytes`                                                                                | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                                                                                                                                                                       |
| • `crawlCalendar`<br>• `crawlNotes`<br>• `crawlContacts`<br>• `crawlFolderAcl`                          | `true` to index this content in your Microsoft Exchange data source. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                                                                       |
| `syncMode`                                                                                              | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents. You can choose between the<br>following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and<br>deleted content each time your data source syncs with your index<br>• Use `CHANGE_LOG` to incrementally crawl only new and modified<br>content each time your data source syncs with your index                              |
| `type`                                                                                                  | The type of data source. Specify `MSEXCHANGE` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `enableIdentityCrawler`                                                                                 | `true` to activate identity crawler. Identity crawler is activated by<br>default. Crawling identity information on users and groups with access to specific<br>documents is useful for user context filtering. Search results are filtered based on the<br>user or their group access to documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `version`                                                                                               | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
