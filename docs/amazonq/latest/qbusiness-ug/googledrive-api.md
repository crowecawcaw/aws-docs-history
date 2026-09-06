

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Connecting Amazon Q Business to GoogleDrive using APIs
<a name="googledrive-api"></a>

You use the [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) action to connect a data source to your Amazon Q application. You can also use the [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) action to modify an existing data source configuration.

Then, you use the `configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html) in the Amazon Q API Reference.

**Topics**
+ [Google Drive configuration properties](#google-configuration-keys)
+ [Google Drive JSON schema](#googledrive-json)
+ [GoogleDrive JSON schema example](#s3-api-json-example)

## Google Drive configuration properties
<a name="google-configuration-keys"></a>

The following provides information about important configuration properties required in the schema.


| Configuration | Description | Type | Required | 
| --- | --- | --- | --- | 
| connectionConfiguration | Configuration information for the data source. | `object`<br />This property has the following sub-property: `repositoryEndpointMetadata`. | Yes | 
| repositoryEndpointMetadata | The endpoint information for the data source. This data source doesn't specify an endpoint. You choose your authentication type: serviceAccount and OAuth2. The connection information is included in an AWS Secrets Manager secret that you provide the secretArn. | `object`<br />This property has the following sub-property: `authType`. | Yes | 
| authType | Choose between serviceAccount and OAuth2, based on your use case. | `string` | Yes | 
| repositoryConfigurations | Configuration information for the content of the data source. For example, configuring specific types of content and field mappings. | `object`<br />This property has the following sub-properties: `file` and `comment`. | Yes | 
|  +  `file` <br />+  `comment`   | A list of objects that map the attributes or field names of your Google Drive to Amazon Q index field names.  | `object`<br />`object`<br />These properties have the following sub-properties.+  `indexFieldName` <br />+  `indexFieldType` <br />+  `dataSourceFieldName` <br />+  `dateFieldFormat`  | No | 
| `indexFieldName` | The field name of your Google Drive to Amazon Q index field names. | `string` | Yes | 
| `indexFieldType` | The field type of your Google Drive to Amazon Q index field names. | `string`<br />The allowed values are `STRING`, `STRING_LIST`, and `DATE`. | Yes | 
| `dataSourceFieldName` | The data source field name of your Google Drive to Amazon Q index field names. | `string` | Yes | 
| `dateFieldFormat` | The date format of your Google Drive to Amazon Q index field names. | `string`<br />Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'` | No | 
| additionalProperties | Additional configuration options for your content in your data source | `object`<br />This property has the following sub-properties.+  `isCrawlAcl` <br />+  `isCrawlMyDriveAndSharedWithMe` <br />+  `isCrawlSharedDrives` <br />+  `isCrawlComment` <br />+  `fieldForUserId` <br />+  `maxFileSizeInMegaBytes` <br />+  `excludeUserAccounts` <br />+  `excludeSharedDrives` <br />+  `excludeMimeTypes` <br />+  `includeUserAccounts` <br />+  `includeSharedDrives` <br />+  `includeMimeTypes` <br />+  `includeTargetAudienceGroup` <br />+  `inclusionFileTypePatterns` <br />+  `inclusionFileNamePatterns` <br />+  `exclusionFileTypePatterns` <br />+  `exclusionFileNamePatterns` <br />+  `inclusionFilePathFilter` <br />+  `exclusionFilePathFilter`  | Yes | 
| isCrawlAcl | Specify true to crawl access control information by default from documents.  Amazon Q Business crawls ACL information to ensure responses are generated only from documents your end users have access to. See [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization) for more details.  | `boolean` | No | 
| fieldForUserId | Specify field to use for UserId for ACL crawling. | `string` | No | 
| maxFileSizeInMegaBytes | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50 MB. The maximum file size should be greater than 0MB and less than or equal to 50 MB. You can use up to 10 GB (10240 MB) if you set videoExtractionStatus to ENABLED in mediaExtractionConfiguration.videoExtractionConfiguration when using CreateDatasource or UpdateDatasource API. Otherwise, you can use up to 2 GB (2048 MB) if you set audioExtractionStatus to ENABLED in  mediaExtractionConfiguration.audioExtractionConfiguration  when using the CreateDatasource or UpdateDatasource API. | `string` | No | 
|  +  `iscrawlComment`   | true to index comments in your Google Drive data source. | `boolean` | No | 
|  +  `isCrawlMyDriveAndSharedWithMe`   | true to index MyDrive and Shared With Me Drives in your Google Drive data source. | `boolean` | No | 
|  +  `isCrawlSharedDrives`   | true to index Shared Drives in your Google Drive data source. | `boolean` | No | 
|  +  `excludeUserAccounts` <br />+  `excludeSharedDrives` <br />+  `excludeMimeTypes` <br />+  `exclusionFileTypePatterns` <br />+  `exclusionFileNamePatterns` <br />+  `exclusionFilePathFilter`   | A list of regular expression patterns to exclude specific files in your Google Drive data source. Files that match the patterns are excluded from the index. Files that don't match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index. | `array` | No | 
|  +  `includeUserAccounts` <br />+  `includeSharedDrives` <br />+  `includeMimeTypes` <br />+  `includeTargetAudienceGroup` <br />+  `inclusionFileTypePatterns` <br />+  `inclusionFileNamePatterns` <br />+  `inclusionFilePathFilter`   | A list of regular expression patterns to include specific files in your Google Drive data source. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence, and the file isn't included in the index. | `array` | No | 
| type | The type of data source. We recommend GOOOGLEDRIVEV2 as your data source type. | `string`<br />Valid values are `GOOOGLEDRIVEV2` and `GOOGLEDRIVE`. | No | 
| enableIdentityCrawler | true to activate identity crawler. Identity crawler is activated by default. Crawling identity information on users and groups with access to certain documents is useful for user context filtering. Search results are filtered based on the user or their group access to documents.  Amazon Q Business crawls identity information from your data source by default to ensure responses are generated only from documents end users have access to. For more information, see [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler).  | `boolean` | Yes | 
| syncMode | Specify whether Amazon Q should update your index by syncing all documents or only new, modified, and deleted documents.  | `string`<br />You can choose between the following options:+  Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace existing content each time your data source syncs with your index <br />+  Use `FULL_CRAWL` to incrementally crawl only new, modified, and deleted content each time your data source syncs with your index <br />+  Use `CHANGE_LOG` to incrementally crawl only new and modified content each time your data source syncs with your index.  | Yes | 
| secretARN | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key-value pairs required to connect to your Google Drive. | `string`<br /> The secret must contain a JSON structure with the following keys:<br />If using Google Service Account authentication:<pre>{<br />    "clientEmail": {{"user account email",}}<br />    "adminAccountEmail": {{"service account email",}}<br />    "privateKey": {{"private key"}}<br />}</pre><br />If using OAuth 2.0 authentication:<pre>{<br />    "clientID": {{"OAuth client ID",}}<br />    "clientSecret": {{"client secret",}}<br />    "refreshToken": {{"refresh token"}}<br />}</pre> | Yes | 
| version | The version of this template that's currently supported. | `string` | No | 

## Google Drive JSON schema
<a name="googledrive-json"></a>

The following is the Google Drive JSON schema:

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": ["GOOGLEDRIVEV2", "GOOGLEDRIVE"]
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
            "authType": {
              "type": "string",
              "enum": ["serviceAccount", "OAuth2"]
            }
          },
          "required": ["authType"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
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
                      "enum": ["STRING", "DATE", "STRING_LIST", "LONG"]
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
                      "enum": ["STRING", "DATE", "STRING_LIST"]
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
        "maxFileSizeInMegaBytes": {
          "type": "string"
        },
        "isCrawlComment": {
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
        "isCrawlMyDriveAndSharedWithMe": {
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
        "isCrawlSharedDrives": {
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
        "fieldForUserId": {
          "type": "string"
        },
        "excludeUserAccounts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeSharedDrives": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "excludeMimeTypes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeUserAccounts": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeSharedDrives": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeMimeTypes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "includeTargetAudienceGroup": {
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
        "inclusionFileNamePatterns": {
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
        "exclusionFileNamePatterns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "inclusionFilePathFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionFilePathFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
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
      }
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
    "type",
    "syncMode",
    "secretArn",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

## GoogleDrive JSON schema example
<a name="s3-api-json-example"></a>

The following is the GoogleDrive JSON schema example:

```
{
  "type": "GOOGLEDRIVEV2",
  "syncMode": "FULL_CRAWL",
  "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-google-drive-secret",
  "enableIdentityCrawler": "true",
  "connectionConfiguration": {
    "repositoryEndpointMetadata": {
      "authType": "OAuth2"
    }
  },
  "repositoryConfigurations": {
    "file": {
      "fieldMappings": [
        {
          "indexFieldName": "file_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "comment": {
      "fieldMappings": [
        {
          "indexFieldName": "comment_id",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "id",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    }
  },
  "additionalProperties": {
    "maxFileSizeInMegaBytes": "10240",
    "isCrawlComment": "true",
    "isCrawlMyDriveAndSharedWithMe": "true",
    "isCrawlSharedDrives": "false",
    "isCrawlAcl": "true",
    "fieldForUserId": "user@example.com",
    "excludeUserAccounts": ["user1@example.com", "user2@example.com"],
    "excludeSharedDrives": ["SharedDrive1"],
    "excludeMimeTypes": ["application/vnd.google-apps.folder"],
    "includeUserAccounts": ["user3@example.com"],
    "includeSharedDrives": ["SharedDrive2"],
    "includeMimeTypes": [
      "application/pdf",
      "application/vnd.google-apps.document"
    ],
    "includeTargetAudienceGroup": ["group1@example.com"],
    "inclusionFileTypePatterns": ["*.pdf"],
    "inclusionFileNamePatterns": ["*report*"],
    "exclusionFileTypePatterns": ["*.tmp"],
    "exclusionFileNamePatterns": ["*draft*"],
    "inclusionFilePathFilter": ["documents/"],
    "exclusionFilePathFilter": ["drafts/"],
    "enableDeletionProtection": "true",
    "deletionProtectionThreshold": "15"

  }
}
```