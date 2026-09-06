

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Asana using APIs (Preview)
<a name="Asana-api"></a>

You use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) action to connect a data source to your Amazon Q application. You can also use the [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) action to modify an existing data source configuration.

Then, you use the `configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) in the Amazon Q API Reference.

## JSON schema
<a name="Asana-json"></a>

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

The following table provides information about important JSON keys to configure.


| Configuration | Description | 
| --- | --- | 
| connectionConfiguration | Configuration information for the endpoint of the data source. | 
| repositoryEndpointMetadata | The endpoint information for the data source. | 
| repositoryConfigurations  | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. | 
|  +  `project` <br />+  `task` <br />+  `comment`   | A list of Asana objects and their metadata attributes that Amazon Q crawls and maps to Amazon Q index field names. The Asana data source field names must exist in your Asana custom metadata. | 
| secretARN | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key-value pairs required to connect to your Asana. | 
| additionalProperties +  `workspaceIds` <br />+  `projectIds`   | Additional configuration options for your content in your data source. | 
| fieldForUserId | Specify field to use for UserId for ACL crawling. | 
| inclusionProjectNamePatterns | A list of regular expression patterns to include specific projects in your Asana data source. projects that match the patterns are included in the index. Projects that don't match the patterns are excluded from the index. If a project matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index. | 
| exclusionProjectNamePatterns | A list of regular expression patterns to exclude specific projects in your Asana data source. Projects that match the patterns are excluded from the index. Projects that don't match the patterns are included in the index. If a project matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index. | 
| isCrawlComments | Input true to index these types of content. | 
| isCrawlACL | Input must be False as Asana does not support document crawling with ACL. | 
| type | Specify ASANA as your data source type. | 
| syncMode | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. You can choose between the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index. <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index. <br />+  Use `CHANGE_LOG` to incrementally crawl only new and modified content each time your data source syncs with your index.  | 
| enableIdentityCrawler | This will always be false as Asana does not support Identity Crawling. Identity crawler is activated by default. Crawling identity information on users and groups with access to certain documents is useful for user context filtering. Search results are filtered based on the user or their group access to documents.  Amazon Q Business crawls identity information from your data source by default to ensure responses are generated only from documents end users have access to. For more information, see [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler).  | 
| version | The version of the template that's currently supported. | 