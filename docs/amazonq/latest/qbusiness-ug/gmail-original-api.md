

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to Gmail using the original connector (API)
<a name="gmail-original-api"></a>

You use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) action to connect a data source to your Amazon Q application. You can also use the [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) action to modify an existing data source configuration.

Then, you use the `configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) in the Amazon Q API Reference.

## Original Gmail connector JSON schema
<a name="gmail-original-json"></a>

The following is the original Gmail connector JSON schema:

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "message": {
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
                      "type": "string"
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
        "attachments": {
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
                      "enum": ["STRING"]
                    },
                    "dataSourceFieldName": {
                      "type": "string"
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
      },
      "required": []
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "isCrawlAcl": {
          "type": "boolean"
        },
        "fieldForUserId": {
          "type": "string"
        },
        "inclusionLabelNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionLabelNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
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
        "inclusionSubjectFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionSubjectFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "isSubjectAnd": {
          "type": "boolean"
        },
        "inclusionFromFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFromFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionToFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionToFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionCcFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionCcFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionBccFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionBccFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "beforeDateFilter": {
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
        "afterDateFilter": {
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
        "isCrawlAttachment": {
          "type": "boolean"
        },
        "shouldCrawlDraftMessages": {
          "type": "boolean"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
        }
      },
      "required": [
        "isCrawlAttachment",
        "shouldCrawlDraftMessages"
      ]
    },
    "type" : {
      "type" : "string",
      "pattern": "GMAIL"
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
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
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
    "syncMode",
    "secretArn",
    "type"
  ]
}
```

The following table provides information about important JSON keys to configure.


| Configuration | Description | 
| --- | --- | 
| connectionConfiguration | Configuration information for the endpoint for the data source. | 
| repositoryConfigurations | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. Specify the type of data source and the secret ARN. | 
|  +  `message` <br />+  `attachments`   |  A list of objects that map the attributes or field names of your Gmail messages and attachments to Amazon Q index field names. | 
| additionalProperties | Additional configuration options for your content in your data source. | 
| isCrawlAcl | Specify true to crawl access control information from documents.  Amazon Q Business crawls ACL information by default to ensure responses are generated only from documents your end users have access to. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.  | 
| fieldForUserId | Specify field to use for UserId for ACL crawling. | 
|  +  `inclusionLabelNamePatterns` <br />+  `exclusionLabelNamePatterns` <br />+  `inclusionAttachmentTypePatterns` <br />+  `exclusionAttachmentTypePatterns` <br />+  `inclusionAttachmentNamePatterns` <br />+  `exclusionAttachmentNamePatterns` <br />+  `inclusionSubjectFilter` <br />+  `exclusionSubjectFilter` <br />+  `inclusionFromFilter` <br />+  `exclusionFromFilter` <br />+  `inclusionToFilter` <br />+  `exclusionToFilter` <br />+  `inclusionCcFilter` <br />+  `exclusionCcFilter` <br />+  `inclusionBccFilter` <br />+  `exclusionBccFilter`   |  A list of regular expression patterns to include or exclude messages with specific subject names in your Gmail data source. Files that match the patterns are included in the index. If a file matches both an inclusion and an exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index. | 
| isSubjectAnd | true to index. | 
| beforeDateFilter | Specify messages and attachments to be included before a certain date.  | 
| afterDateFilter | Specify messages and attachments to be included after a certain date. | 
| isCrawlAttachment | A Boolean value to choose whether you want to crawl attachments. Messages are automatically crawled. | 
| maxFileSizeInMegaBytes | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB. | 
| type | The type of data source. Specify GMAIL as your data source type. | 
| shouldCrawlDraftMessages | A Boolean value to choose whether you want to crawl draft messages. | 
| syncMode | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents. You can choose from the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index   Because there is no API to update permanently deleted Gmail messages, a **New, modified, or deleted content sync** does *not* do the following:   Remove messages that were permanently deleted from Gmail from your Amazon Q index   Sync changes in Gmail email labels   <br />To sync your Gmail data source label changes and permanently deleted email messages to your Amazon Q index, you must run full crawls periodically.   | 
| enableIdentityCrawler | Specify true to use the Amazon Q identity crawler to sync identity/principal information on users and groups with access to specific documents.  Amazon Q Business crawls identity information from your data source by default to ensure responses are generated only from documents end users have access to. For more information, see [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler).  | 
| secretARN | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs required to connect to your Gmail. The secret must contain a JSON structure with the following keys: <pre>{<br />    "adminAccountEmailId": {{"${adminAccountEmailId}"}},<br />    "clientEmailId": {{"${clientEmailId}"}},<br />    "privateKey": {{"${privateKey}"}}<br />}</pre> | 
| version | The version of the template that's currently supported. | 