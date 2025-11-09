# Connecting Amazon Q Business to GitHub (Cloud)

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

###### Topics

- [GitHub (Cloud) configuration
  properties](#github-cloud-configuration-keys "#github-cloud-configuration-keys")
- [GitHub (Cloud) JSON schema](#github-cloud-json "#github-cloud-json")
- [GitHub (Cloud) JSON schema example](#s3-api-json-example "#s3-api-json-example")

## GitHub (Cloud) configuration

properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`                                                                                                                                           | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                          | `object`<br>This property has a sub-property called<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                        | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                            | `object`<br>This property has the following sub-properties.<br>• `hostUrl`<br>• `type`<br>• `organizationName`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `hostUrl`                                                                                                                                                           | The GitHub (Cloud) host URL. For example, if you use GitHub (Cloud)<br>Enterprise Cloud: *https://api.github.com*.                                                                                                                                                                                                                                                                                       | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `type`                                                                                                                                                              | The hosting method for your GitHub instance.                                                                                                                                                                                                                                                                                                                                                             | `string`<br>The only allowed value is `SAAS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes      |
| `organizationName`                                                                                                                                                  | You can find your organization name when you log in to GitHub (Cloud) desktop<br>and go to \*_Your organizations_<br>• under your profile picture<br>dropdown.                                                                                                                                                                                                                                           | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `repositoryConfigurations`                                                                                                                                          | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                  | `array`<br>This property has the following sub-properties:<br>• `ghRepository`<br>• `ghCommit`<br>• `ghIssueDocument`<br>• `ghIssueComment`<br>• `ghIssueAttachment`<br>• `ghPRDocument`<br>• `ghPRComment`<br>• `ghPRAttachment`                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| • `ghRepository`<br>• `ghCommit`<br>• `ghIssueDocument`<br>• `ghIssueComment`<br>• `ghIssueAttachment`<br>• `ghPRDocument`<br>• `ghPRComment`<br>• `ghPRAttachment` | A list of objects that map the attributes or field names of your<br>GitHub (Cloud) pages and assets to Amazon Q index field<br>names.                                                                                                                                                                                                                                                                    | `object`<br>These properties have the following sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                                                                                                                                                                                                                                            | No       |
| `indexFieldName`                                                                                                                                                    | The field name of your GitHub (Cloud) pages and assets.                                                                                                                                                                                                                                                                                                                                                  | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `indexFieldType`                                                                                                                                                    | The field type of your GitHub (Cloud) pages and assets.                                                                                                                                                                                                                                                                                                                                                  | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and<br>`DATE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes      |
| `dataSourceFieldName`                                                                                                                                               | The data source field name of your GitHub (Cloud) pages and<br>assets.                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `dateFieldFormat`                                                                                                                                                   | The date format of your GitHub (Cloud) pages and assets.                                                                                                                                                                                                                                                                                                                                                 | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No       |
| `additionalProperties`                                                                                                                                              | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                   | `object`<br>This property has the following sub-properties.<br>• `isCrawlAcl`<br>• `crawlRepository`<br>• `crawlRepositoryDocuments`<br>• `crawlIssue`<br>• `crawlIssueComment`<br>• `crawlIssueCommentAttachment`<br>• `crawlPullRequest`<br>• `crawlPullRequestComment`<br>• `crawlPullRequestCommentAttachment`<br>• `fieldForUserId`<br>• `maxFileSizeInMegaBytes`<br>• `repositoryFilter`<br>• `inclusionFolderNamePatterns`<br>• `inclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`<br>• `exclusionFolderNamePatterns`<br>• `exclusionFileTypePatterns`<br>• `exclusionFileNamePatterns` | Yes      |
| `isCrawlAcl`                                                                                                                                                        | Specify `true` to crawl access control information from<br>documents.                                                                                                                                                                                                                                                                                                                                    | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `maxFileSizeInMegaBytes`                                                                                                                                            | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                | `string`<br>The allowed values are numbers between greater than 0 and less than or equal to<br>50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |
| `fieldForUserId`                                                                                                                                                    | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                      | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| repositoryFilter                                                                                                                                                    | A list of names of the specific repositories and branch names you want to<br>index.                                                                                                                                                                                                                                                                                                                      | `object`<br>This property has the following sub-properties: `repositoryName` and<br>`branchNameList`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `repositoryName`                                                                                                                                                    | The list of repository names that you want to index.                                                                                                                                                                                                                                                                                                                                                     | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `branchNameList`                                                                                                                                                    | The list of branch names that you want to index.                                                                                                                                                                                                                                                                                                                                                         | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| `crawlRepository`                                                                                                                                                   | Specify `true` to crawl repositories.                                                                                                                                                                                                                                                                                                                                                                    | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlRepositoryDocuments`                                                                                                                                          | Specify `true` to crawl repository documents.                                                                                                                                                                                                                                                                                                                                                            | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlIssue`                                                                                                                                                        | Specify `true` to crawl issues.                                                                                                                                                                                                                                                                                                                                                                          | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlIssueComment`                                                                                                                                                 | Specify `true` to crawl issue comments.                                                                                                                                                                                                                                                                                                                                                                  | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlIssueCommentAttachment`                                                                                                                                       | Specify `true` to crawl issue comment attachments.                                                                                                                                                                                                                                                                                                                                                       | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlPullRequest`                                                                                                                                                  | Specify `true` to crawl pull requests.                                                                                                                                                                                                                                                                                                                                                                   | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlPullRequestComment`                                                                                                                                           | Specify `true` to crawl pull request comments.                                                                                                                                                                                                                                                                                                                                                           | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `crawlPullRequestCommentAttachment`                                                                                                                                 | Specify `true` to crawl pull request comment attachments.                                                                                                                                                                                                                                                                                                                                                | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| • `inclusionFolderNamePatterns`<br>• `inclusionFileTypePatterns`<br>• `inclusionFileNamePatterns`                                                                   | A list of regular expression patterns to include specific content in your<br>GitHub (Cloud) data source. Content that matches the patterns are<br>included in the index. Content that doesn't match the patterns are excluded from the<br>index. If any content matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the content isn't included in the index. | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| • `exclusionFolderNamePatterns`<br>• `exclusionFileTypePatterns`<br>• `exclusionFileNamePatterns`                                                                   | A list of regular expression patterns to exclude specific content in your<br>GitHub (Cloud) data source. Content that matches the patterns are<br>included in the index. Content that doesn't match the patterns are excluded from the<br>index. If any content matches both an inclusion and exclusion pattern, the exclusion<br>pattern takes precedence, and the content isn't included in the index. | `array (string)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| `type`                                                                                                                                                              | The type of data source. Specify `GITHUB` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `enableIdentityCrawler`                                                                                                                                             | Specify `true` to use the Amazon Q identity crawler to sync<br>identity/principal information on users and groups with access to specific<br>documents.                                                                                                                                                                                                                                                  | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `syncMode`                                                                                                                                                          | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                              | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.<br>• Use `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index.                                                                                                                 | Yes      |
| `secretArn`                                                                                                                                                         | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your GitHub (Cloud).                                                                                                                                                                                                                                                         | `string`<br>The secret must contain a JSON structure with the following keys:<br>``<br>{<br>"personalToken": "`token`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |
| `version`                                                                                                                                                           | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                 | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |

## GitHub (Cloud) JSON schema

The following is the GitHub (Cloud) JSON schema:

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "pattern": "GITHUB"
    },
    "syncMode": {
      "type": "string",
      "enum": ["FULL_CRAWL", "FORCED_FULL_CRAWL", "CHANGE_LOG"]
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
            "type": {
              "type": "string"
            },
            "hostUrl": {
              "type": "string",
              "pattern": "https://.*"
            },
            "organizationName": {
              "type": "string"
            }
          },
          "required": ["type", "hostUrl", "organizationName"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "ghRepository": {
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
        "ghCommit": {
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
        "ghIssueDocument": {
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
        "ghIssueComment": {
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
        "ghIssueAttachment": {
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
        "ghPRDocument": {
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
        "ghPRComment": {
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
        "ghPRAttachment": {
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
        "crawlRepository": {
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
        "crawlRepositoryDocuments": {
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
        "crawlIssue": {
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
        "crawlIssueComment": {
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
        "crawlIssueCommentAttachment": {
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
        "crawlPullRequest": {
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
        "crawlPullRequestComment": {
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
        "crawlPullRequestCommentAttachment": {
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
        "repositoryFilter": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "repositoryName": {
                  "type": "string"
                },
                "branchNameList": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                }
              }
            }
          ]
        },
        "inclusionFolderNamePatterns": {
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
        "exclusionFolderNamePatterns": {
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
    }
  },
  "required": [
    "syncMode",
    "enableIdentityCrawler",
    "connectionConfiguration",
    "repositoryConfigurations",
    "additionalProperties"
  ]
}
```

[Show moreShow less](# "#")

## GitHub (Cloud) JSON schema example

The following is the GitHub (Cloud) JSON schema example:

```
{
  "type": "GITHUB",
  "syncMode": "FULL_CRAWL",
  "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-github-secret",
  "enableIdentityCrawler": "true",
  "sslCertificatePath": {
    "bucket": "my-github-bucket",
    "key": "certificates/my-cert.pem"
  },
  "connectionConfiguration": {
    "repositoryEndpointMetadata": {
      "type": "GitHub",
      "hostUrl": "https://api.github.com",
      "organizationName": "my-org"
    }
  },
  "repositoryConfigurations": {
    "ghRepository": {
      "fieldMappings": [
        {
          "indexFieldName": "repo_name",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "name",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'"
        }
      ]
    },
    "ghCommit": {
      "fieldMappings": [
        {
          "indexFieldName": "commit_id",
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
    "crawlRepository": "true",
    "crawlIssue": "true",
    "repositoryFilter": [
      {
        "repositoryName": "my-repo",
        "branchNameList": ["main", "develop"]
      }
    ],
    "inclusionFileTypePatterns": ["*.md", "*.txt"],
    "exclusionFileNamePatterns": ["*draft*"],
    "enableDeletionProtection": "false",
    "deletionProtectionThreshold": "15"
  },
  "version": "1.0.0"
}
```

[Show moreShow less](# "#")
