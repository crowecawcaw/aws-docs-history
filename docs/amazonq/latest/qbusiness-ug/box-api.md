

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Box using APIs
<a name="box-api"></a>

You use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) action to connect a data source to your Amazon Q application. You can also use the [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) action to modify an existing data source configuration.

Then, you use the `configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) in the Amazon Q API Reference.

## Box JSON schema
<a name="box-json"></a>

The following is the Box JSON schema:

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
            "enterpriseId": {
              "type": "string",
              "minLength": 1,
              "maxLength": 64
            }
          },
          "required": [
            "enterpriseId"
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
        "file": {
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
                        "STRING_LIST",
                        "DATE",
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
                        "STRING_LIST",
                        "DATE",
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
                        "STRING_LIST",
                        "DATE",
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
        "webLink": {
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
                        "STRING_LIST",
                        "DATE",
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
        "isCrawlAcl": {
          "type": "boolean"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "fieldForUserId": {
          "type": "string"
        },
        "crawlComments": {
          "type": "boolean"
        },
        "crawlTasks": {
          "type": "boolean"
        },
        "crawlWebLinks": {
          "type": "boolean"
        },
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
        }
      },
      "required": []
    },
    "type": {
      "type": "string",
      "pattern": "BOX"
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
    "type",
    "enableIdentityCrawler"

  ]
}
```

The following table provides information about important JSON keys to configure.


| Configuration | Description | 
| --- | --- | 
| connectionConfiguration | Configuration information for the endpoint for the data source. | 
| repositoryEndpointMetadata | The endpoint information for the data source. | 
| enterpriseId | The Box enterprise id. | 
| repositoryConfigurations | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. | 
|  +  `file` <br />+  `task` <br />+  `comment` <br />+  `webLink`   | A list of objects that map the attributes or field names of your Box files, tasks, comments, and webLinks to Amazon Q index field names. | 
| additionalProperties | Additional configuration options for your content in your data source. | 
| maxFileSizeInMegaBytes | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB. | 
| isCrawlAcl | Specify true to crawl access control information from documents.  Amazon Q Business crawls ACL information by default to ensure responses are generated only from documents your end users have access to. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.  | 
| fieldForUserId | Specify field to use for UserId for ACL crawling. | 
| crawlComments | Specify true to crawl assets. | 
| crawlTasks | Specify true to crawl pages. | 
| crawlWebLinks | Specify true to crawl pages. | 
|  +  `InclusionPatterns` <br />+  `ExclusionPatterns`   | A list of regular expression patterns to include or exclude specific content from your Box data source. Content that matches the patterns are included in the index. Content that doesn't match the patterns are excluded from the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the content isn't included in the index. | 
| type | The type of data source. Specify BOX as your data source type. | 
| enableIdentityCrawler | Specify true to use the Amazon Q identity crawler to sync identity/principal information on users and groups with access to specific documents.  Amazon Q Business crawls identity information from your data source by default to ensure responses are generated only from documents end users have access to. For more information, see [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler).  | 
| syncMode | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. You can choose between the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index. <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index. <br />+  Use `CHANGE_LOG` to incrementally crawl only new and modified content each time your data source syncs with your index.  | 
| secretArn | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key-value pairs required to connect to your Box. The secret must contain a JSON structure with the following keys:<pre>{<br />    "clientID": "{{client-id}}",<br />    "clientSecret": "{{client-secret}}",<br />    "publicKeyID": "{{public-key-id}}",<br />    "privateKey": "{{private-key}}",<br />    "passphrase": "{{pass-phrase}}"<br />}</pre> | 
| version | The version of this template that's currently supported. | 