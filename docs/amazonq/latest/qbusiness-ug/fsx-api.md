# Connecting Amazon Q Business to Amazon FSx (Windows) using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Amazon FSx JSON schema

The following is the Amazon FSx JSON schema:

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
            "fileSystemId": {
              "type": "string",
              "pattern": "fs-.*"
            },
            "fileSystemType": {
              "type": "string",
              "pattern": "WINDOWS"
            }
          },
          "required": ["fileSystemId", "fileSystemType"]
        }
      }
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "All": {
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
        }
      },
      "required": ["All"]
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
        "exclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionPatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": []
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "type" : {
      "type" : "string",
      "pattern": "FSX"
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
    "secretArn",
    "enableIdentityCrawler",
    "additionalProperties",
    "type"
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to
configure.

| Configuration                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`    | Configuration information for the endpoint for the data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `repositoryEndpointMetadata` | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `fileSystemId`               | The identifier of the Amazon FSx (Windows) file system. You can find<br>your file system ID on the File Systems dashboard in the<br>Amazon FSx (Windows) console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `fileSystemType`             | The type of Amazon FSx you use: Amazon FSx (Windows) file<br>system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `repositoryConfigurations`   | Configuration information for the content of the data source. For<br>example, configuring specific types of content and field<br>mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| • `All`                      | A list of objects that map the attributes or field names of your<br>Amazon FSx (Windows) pages and assets to Amazon Q index field<br>names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `additionalProperties`       | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `isCrawlAcl`                 | Specify `true` to crawl access control information from<br>documents. NoteAmazon Q Business crawls ACL information by default to<br>ensure responses are generated only from documents your end<br>users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more<br>details.                                                                                                                                                                                                                                                                      |
| `maxFileSizeInMegaBytes`     | Specify the maximum single file size limit in MBs that Amazon Q will<br>crawl. Amazon Q will crawl only the files within the size limit you<br>define. The default file size is 50MB. The maximum file size should be<br>greater than 0MB and less than or equal to 50MB.                                                                                                                                                                                                                                                                                                                                                             |
| • `inclusionPatterns`        | A list of regular expression patterns to include specific content<br>from you Amazon FSx (Windows) data source. Content that match the patterns<br>are included in the index. Content that doesn't match the patterns are<br>excluded from the index. If content matches both an inclusion and<br>exclusion pattern, the exclusion pattern takes precedence, and the<br>content isn't included in the index.                                                                                                                                                                                                                          |
| • `exclusionPatterns`        | A list of regular expression patterns to exclude specific content<br>from your Amazon FSx (Windows) data source. Content that match the<br>patterns are excluded from the index. Content that doesn't match the<br>patterns are included in the index. If content matches both an inclusion<br>and exclusion pattern, the exclusion pattern takes precedence, and the<br>content isn't included in the index.                                                                                                                                                                                                                         |
| `enableIdentityCrawler`      | `true` to activate identity crawler. Identity crawler is<br>activated by default. Crawling identity information on users and groups<br>with access to specific documents is useful for user context filtering.<br>Search results are filtered based on the user or their group access to<br>documents. NoteAmazon Q Business crawls identity information from your<br>data source by default to ensure responses are generated only<br>from documents end users have access to. For more information,<br>see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `syncMode`                   | Specify whether Amazon Q should update your index by<br>syncing all documents or only new, modified, and deleted documents. You<br>can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data<br>source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only<br>new, modified, and deleted content each time your data<br>source syncs with your index                                                                                                                                                             |
| `type`                       | The type of data source. Specify `FSX` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `version`                    | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
