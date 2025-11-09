# Connecting Amazon Q Business to

Asana using APIs (Preview)

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## JSON schema

The following is the Asana JSON schema:

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
                "PAT",
                "ServiceAccount"
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
        "project": {
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
          }
        },
        "task": {
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
          }
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
          "minItems": 1,
          "maxItems": 1
        },
        "projectIds": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 12,
            "maxLength": 16
          },
          "maxItems": 20
        },
        "fieldForUserId": {
          "type": "string"
        },
        "isCrawlAcl": {
          "type": "boolean"
        },
        "isCrawlComments": {
          "type": "boolean"
        },
        "inclusionProjectNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionProjectNamePatterns": {
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
      }
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "type": {
      "type": "string",
      "pattern": "ASANA"
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
The following table provides information about important JSON keys to
configure.

| Configuration                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                    | Configuration information for the endpoint of the data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `repositoryEndpointMetadata`                                 | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `repositoryConfigurations`                                   | Configuration information for the content of the data source. For<br>example, configuring specific types of content and field<br>mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| • `project`<br>• `task`<br>• `comment`                       | A list of Asana objects and their metadata attributes<br>that Amazon Q crawls and maps to Amazon Q index<br>field names. The Asana data source field names must exist<br>in your Asana custom metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `secretARN`                                                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret<br>that contains the key-value pairs required to connect to your<br>Asana.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `additionalProperties`<br>• `workspaceIds`<br>• `projectIds` | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `fieldForUserId`                                             | Specify field to use for `UserId` for ACL<br>crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `inclusionProjectNamePatterns`                               | A list of regular expression patterns to _include_<br>specific projects in your Asana data source. projects that<br>match the patterns are included in the index. Projects that don't match<br>the patterns are excluded from the index. If a project matches both an<br>inclusion and exclusion pattern, the exclusion pattern takes precedence,<br>and the file isn't included in the index.                                                                                                                                                                                                                                                                         |
| `exclusionProjectNamePatterns`                               | A list of regular expression patterns to _exclude_<br>specific projects in your Asana data source. Projects that<br>match the patterns are excluded from the index. Projects that don't<br>match the patterns are included in the index. If a project matches both<br>an exclusion and inclusion pattern, the exclusion pattern takes<br>precedence, and the file isn't included in the index.                                                                                                                                                                                                                                                                         |
| `isCrawlComments`                                            | Input `true` to index these types of content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| isCrawlACL                                                   | Input must be `False` as Asana does not support document<br>crawling with ACL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `type`                                                       | Specify `ASANA` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `syncMode`                                                   | Specify whether Amazon Q should update your index by<br>syncing all documents or only new, modified, and deleted documents.<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to<br>freshly re-crawl all content and replace existing content<br>each time your data source syncs with your index.<br>• Use `FULL_CRAWL` to<br>incrementally crawl only new, modified, and deleted content<br>each time your data source syncs with your index.<br>• Use `CHANGE_LOG` to<br>incrementally crawl only new and modified content each time<br>your data source syncs with your index.                                                         |
| `enableIdentityCrawler`                                      | This will always be false as Asana does not support Identity<br>Crawling. Identity crawler is activated by default. Crawling identity<br>information on users and groups with access to certain documents is<br>useful for user context filtering. Search results are filtered based on<br>the user or their group access to documents. NoteAmazon Q Business crawls identity information from your<br>data source by default to ensure responses are generated only<br>from documents end users have access to. For more information,<br>see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `version`                                                    | The version of the template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
