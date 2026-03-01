# Connecting Amazon Q Business to Quip using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Quip JSON schema

The following is the Quip JSON schema:

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
                        "domain": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "domain"
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
                "thread": {
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
                                                "DATE"
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
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
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
                                            "enum": [
                                                "STRING",
                                                "STRING_LIST",
                                                "DATE"
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
                "folderIds": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "crawlFileComments": {
                    "type": "boolean"
                },
                "crawlChatRooms": {
                    "type": "boolean"
                },
                "crawlAttachments": {
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
            "pattern": "QUIP"
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

| Configuration                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connectionConfiguration`                                           | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `repositoryEndpointMetadata`                                        | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `domain`                                                            | Your Quip site domain. For example,<br>`https://quip-company.quipdomain.com/browse`<br>where `quipdomain` is the domain.                                                                                                                                                                                                                                                                                                                                                            |
| `repositoryConfigurations`                                          | Configuration information for the content of the data source. For<br>example, configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                             |
| • `thread`<br>• `message`<br>• `attachment`                         | A list of objects that map the attributes or field names of your<br>Quip pages and assets to Amazon Q index field<br>names.                                                                                                                                                                                                                                                                                                                                                         |
| `additionalProperties`                                              | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `isCrawlAcl`                                                        | Specify `true` to crawl access control information from<br>documents. NoteAmazon Q Business crawls ACL information by default to<br>ensure responses are generated only from documents your end users<br>have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more<br>details.                                                                                                                    |
| `maxFileSizeInMegaBytes`                                            | Specify the maximum single file size limit in MBs that Amazon Q will<br>crawl. Amazon Q will crawl only the files within the size limit you define.<br>The default file size is 50MB. The maximum file size should be greater than<br>0MB and less than or equal to 50MB.                                                                                                                                                                                                           |
| `fieldForUserId`                                                    | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `folderIds`                                                         | Specify folder IDs to crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| • `crawlFileComments`<br>• `crawlChatRooms`<br>• `crawlAttachments` | `true` to index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| • `inclusionPatterns`                                               | A list of regular expression patterns to include specific content in your<br>Quip data source. Content that matches the patterns are<br>included in the index. Content that doesn't match the pattern are excluded<br>from the index. If any content matches both an inclusion and exclusion<br>pattern, the exclusion pattern takes precedence, and the content isn't<br>included in the index.                                                                                    |
| • `exclusionPatterns`                                               | A list of regular expression patterns to exclude specific content in your<br>Quip data source. Content that matches the patterns are<br>excluded from the index. Content that doesn't match the patterns are<br>included in the index. If any content matches both an inclusion and<br>exclusion pattern, the exclusion pattern takes precedence, and the content<br>isn't included in the index.                                                                                   |
| `type`                                                              | The type of data source. Specify `QUIP` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `enableIdentityCrawler`                                             | Specify `true` to use the Amazon Q identity crawler<br>to sync identity/principal information on users and groups with access to<br>specific documents. NoteAmazon Q Business crawls identity information from your data<br>source by default to ensure responses are generated only from<br>documents end users have access to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). |
| `syncMode`                                                          | Specify whether Amazon Q should update your index by<br>syncing all documents or only new, modified, and deleted documents. You<br>can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly<br>re-crawl all content and replace existing content each time your<br>data source syncs with your index.<br>• Use `FULL_CRAWL` to incrementally<br>crawl only new, modified, and deleted content each time your<br>data source syncs with your index.         |
| `secretArn`                                                         | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret<br>that contains the key-value pairs required to connect to your<br>Quip. The secret must contain a JSON structure with<br>the following keys:<br>``<br>{<br>"accessToken": "`token`"<br>}<br>``                                                                                                                                                                                                                    |
| `version`                                                           | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                            |
