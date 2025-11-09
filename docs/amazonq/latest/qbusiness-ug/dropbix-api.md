# Connecting Amazon Q Business to Dropbox

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Dropbox JSON schema

The following is the Dropbox JSON schema:

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
        "file": {
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
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
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
        "paper": {
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
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
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
        "papert": {
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
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
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
        "shortcut": {
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
                          "STRING_LIST",
                          "LONG",
                          "DATE"
                        ]
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
    "enableIdentityCrawler": {
      "type": "boolean"
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
        "crawlFile": {
          "type": "boolean"
        },
        "crawlPaper": {
          "type": "boolean"
        },
        "crawlPapert": {
          "type": "boolean"
        },
        "crawlShortcut": {
          "type": "boolean"
        }
      }
    },
    "type": {
      "type": "string",
      "pattern": "DROPBOX"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL",
        "CHANGE_LOG"
      ]
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

| Configuration                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                               | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `repositoryEndpointMetadata`                                            | The endpoint information for the data source. This data source doesn't specify an<br>endpoint in `repositoryEndpointMetadata`. Rather, the connection information<br>is included in an AWS Secrets Manager secret that you provide the<br>`secretArn`.                                                                                                                                                                                                                           |
| `repositoryConfigurations`                                              | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                          |
| • `file`<br>• `paper`<br>• `papert`<br>• `shortcut`                     | A list of objects that map the attributes or field names of your<br>Dropbox files, Dropbox Paper, and shortcuts to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                   |
| `enableIdentityCrawler`                                                 | Specify `true` to use the Amazon Q identity crawler to sync<br>identity/principal information on users and groups with access to specific documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `secretARN`                                                             | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Dropbox. The secret must<br>contain a JSON structure with the following keys:<br>``<br>{<br>"appKey": `"Dropbox app key"`,<br>"appSecret": `"Dropbox app secret"`,<br>"accesstoken": `"access token (short live)"`,<br>"refreshtoken": `"refresh token (offline-access)"`<br>}<br>``                                                            |
| `additionalProperties`                                                  | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `maxFileSizeInMegaBytes`                                                | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                        |
| `isCrawlAcl`                                                            | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                          |
| `fieldForUserId`                                                        | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `inclusionFileTypePatterns`                                             | A list of regular expression patterns to \*include<br>• specific file<br>types in your Dropbox data source. Files that match the patterns are<br>included in the index. Files that don't match the patterns are excluded from the index.<br>If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                       |
| `exclusionFileTypePatterns`                                             | A list of regular expression patterns to \*exclude<br>• specific file<br>types in your Dropbox data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the index.<br>If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                       |
| `exclusionFileNamePatterns`                                             | A list of regular expression patterns to \*exclude<br>• specific file<br>names in your Dropbox data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the index.<br>If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                       |
| `exclusionFileNamePatterns`                                             | A list of regular expression patterns to \*exclude<br>• specific file<br>names in your Dropbox data source. Files that match the patterns are<br>excluded from the index. Files that don't match the patterns are included in the index.<br>If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                       |
| • `crawlFile`<br>• `crawlPaper`<br>• `crawlPapert`<br>• `crawlShortcut` | `true` to index files in your Dropbox,<br>Dropbox Paper documents, Dropbox Paper templates, and<br>webpage shortcuts stored in your Dropbox.                                                                                                                                                                                                                                                                                                                                     |
| `type`                                                                  | The type of data source. Specify `DROPBOX` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `useChangeLog`                                                          | `true` to use the Dropbox change log to determine which<br>documents require adding, updating, or deleting in the index. Depending on the change<br>log's size, it may take longer for Amazon Q to use the change log than to<br>scan all of your documents in your Dropbox.                                                                                                                                                                                                     |
| `version`                                                               | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                         |
