# Connecting Amazon Q Business to Slack

using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [Slack configuration
  properties](#slack-configuration-keys "#slack-configuration-keys")
- [Slack JSON schema for using the
  configuration property with AWS CloudFormation](#slack-cfn-json "#slack-cfn-json")
- [Slack YAML schema for using the
  configuration property with AWS CloudFormation](#slack-cfn-yaml "#slack-cfn-yaml")

## Slack configuration

properties

The following provides information about important configuration properties required in the
schema.

| Configuration                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                  | `object`<br>This property has the following sub-property:<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                               | Yes      |
| `repositoryEndpointMetadata` | The endpoint information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                    | `object`<br>This property has the following sub-property: `teamId`.                                                                                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `teamId`                     | The Slack team ID you copied from your Slack main page URL.                                                                                                                                                                                                                                                                                                                                                                                                                      | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `repositoryConfigurations`   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                          | `object`<br>This property has the following sub-property: `All`.                                                                                                                                                                                                                                                                                                                                                                                                                         | No       |
| `All`                        | A list of objects that map the attributes or field names of your<br>Slack pages and assets to Amazon Q index field<br>names.                                                                                                                                                                                                                                                                                                                                                     | `object`<br>This property has the following sub-properties: `indexFieldName`,<br>`indexFieldType`, `dataSourceFieldName`, and<br>`dateFieldFormat`.                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `indexFieldName`             | The field name of your Slack pages and assets.                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `indexFieldType`             | The field type of your Slack pages and assets.                                                                                                                                                                                                                                                                                                                                                                                                                                   | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and<br>`DATE`.                                                                                                                                                                                                                                                                                                                                                                                                               | Yes      |
| `dataSourceFieldName`        | The data source field name of your Slack pages and assets.                                                                                                                                                                                                                                                                                                                                                                                                                       | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `dateFieldFormat`            | The date format of your Slack pages and assets.                                                                                                                                                                                                                                                                                                                                                                                                                                  | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                                                                                                               | No       |
| `additionalProperties`       | Additional configuration options for your content in your data source.                                                                                                                                                                                                                                                                                                                                                                                                           | `object`<br>This property has the following sub-properties.<br>• `isCrawlAcl`<br>• `conversationType`<br>• `crawlBotMessages`<br>• `excludeArchived`<br>• `sinceDate`<br>• `lookBack`<br>• `fieldForUserId`<br>• `maxFileSizeInMegaBytes`<br>• `channelFilter`<br>• `channelIdFilter`<br>• `exclusionPatterns`<br>• `inclusionPatterns`                                                                                                                                                  | Yes      |
| `isCrawlAcl`                 | Specify `true` to crawl access control information from documents. NoteAmazon Q Business crawls ACL information by default to ensure responses<br>are generated only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                          | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `maxFileSizeInMegaBytes`     | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The default file<br>size is 50MB. The maximum file size should be greater than 0MB and less than or equal to<br>50MB.                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `fieldForUserId`             | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                              | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `inclusionPatterns`          | A list of regular expression patterns to include specific content in your<br>Slack data source. Content that matches the patterns are included in<br>the index. Content that doesn't match the patterns are excluded from the index. If any<br>content matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the content isn't included in the index.                                                                                  | `array`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `exclusionPatterns`          | A list of regular expression patterns to exclude specific content in your<br>Slack data source. Content that matches the patterns are excluded from<br>the index. Content that doesn't match the patterns are included in the index. If any<br>content matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence, and the content isn't included in the index.                                                                                  | `array`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `crawlBotMessages`           | `true` to crawl Slack bot messages.                                                                                                                                                                                                                                                                                                                                                                                                                                              | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `excludeArchived`            | `true` to exclude archived messages from crawl.                                                                                                                                                                                                                                                                                                                                                                                                                                  | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `conversationType`           | The type of conversation that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`<br>Valid values are `PUBLIC_CHANNEL`, `PRIVATE_CHANNEL`,<br>`GROUP_MESSAGE`, and `DIRECT_MESSAGE`.                                                                                                                                                                                                                                                                                                                                                                              | No       |
| `channelFilter`              | The type of channel that you want to index whether `private_channel` or<br>`public_channel`.                                                                                                                                                                                                                                                                                                                                                                                     | `object`<br>This property has the following sub-properties: `private_channel` and<br>`public_channel`.                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `private_channel`            | The IDs of the private channel that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                           | `array`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `public_channel`             | The IDs of public channel that you want to index.                                                                                                                                                                                                                                                                                                                                                                                                                                | `array`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `channelIdFilter`            | You can choose to crawl specific channels vy channel ID using the<br>`channelIdFilter`.                                                                                                                                                                                                                                                                                                                                                                                          | `array`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `sinceDate`                  | You can choose to configure a `sinceDate` parameter so that the<br>Slack connector crawls content based on a specific<br>`sinceDate`.                                                                                                                                                                                                                                                                                                                                            | `string`<br>Specify the date in the form<br>`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$` or as an empty<br>string.                                                                                                                                                                                                                                                                                                                                                         | No       |
| `lookBack`                   | You can choose to configure a `lookBack` parameter so that the<br>Slack connector crawls `lookBack` content.                                                                                                                                                                                                                                                                                                                                                                     | `string`<br>Specify the value in the form `^[0-9]*$`.                                                                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `syncMode`                   | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                      | `string`<br>You can choose between the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data source syncs with your<br>index.<br>• Use `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source syncs with your<br>index.<br>• Use `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index. | Yes      |
| `type`                       | The type of data source. Specify `SLACK` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                            | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `enableIdentityCrawler`      | Specify `true` to use the Amazon Q identity crawler to sync<br>identity/principal information on users and groups with access to specific documents. NoteAmazon Q Business crawls identity information from your data source by<br>default to ensure responses are generated only from documents end users have access<br>to. For more information, see [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler"). | `boolean`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `secretArn`                  | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Slack.                                                                                                                                                                                                                                                                                                                                          | `string`<br>The secret must contain a JSON structure with the following keys:<br>``<br>{<br>"slackToken": "`token`"<br>}<br>``                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `version`                    | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                         | `string`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |

## Slack JSON schema for using the

configuration property with AWS CloudFormation

The following is the Slack JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Slack JSON schema for using the
  configuration property with AWS CloudFormation](#slack-cfn-json-schema "#slack-cfn-json-schema")
- [Slack JSON schema example for
  using the configuration property with AWS CloudFormation](#slack-cfn-json-example "#slack-cfn-json-example")

### Slack JSON schema for using the

configuration property with AWS CloudFormation

The following is the Slack JSON schema for the configuration property for
CloudFormation

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "pattern": "SLACK"
    },
    "syncMode": {
      "type": "string",
      "enum": ["FORCED_FULL_CRAWL", "FULL_CRAWL", "CHANGE_LOG"]
    },
    "secretArn": {
      "type": "string"
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
            "teamId": {
              "type": "string"
            }
          },
          "required": ["teamId"]
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
                      "enum": ["STRING", "STRING_LIST", "DATE", "LONG"]
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
      "required": []
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
        },
        "crawlBotMessages": {
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
        "excludeArchived": {
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
        "conversationType": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PUBLIC_CHANNEL",
              "PRIVATE_CHANNEL",
              "GROUP_MESSAGE",
              "DIRECT_MESSAGE"
            ]
          }
        },
        "channelFilter": {
          "type": "object",
          "properties": {
            "private_channel": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "public_channel": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "channelIdFilter": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "sinceDate": {
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
        "lookBack": {
          "type": "string",
          "pattern": "^[0-9]*$"
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
    },
    "required": [
      "type",
      "secretArn",
      "syncMode",
      "enableIdentityCrawler",
      "connectionConfiguration",
      "repositoryConfigurations",
      "additionalProperties"
    ]
  }
}
```

[Show moreShow less](# "#")

### Slack JSON schema example for

using the configuration property with AWS CloudFormation

The following is the Slack JSON schema example for the configuration
property for CloudFormation

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "CloudFormation SLACK Data Source Template",
  "Resources": {
    "DataSourceSlack": {
      "Type": "AWS::QBusiness::DataSource",
      "Properties": {
        "ApplicationId": "app12345-1234-1234-1234-123456789012",
        "IndexId": "indx1234-1234-1234-1234-123456789012",
        "DisplayName": "MySlackDataSource",
        "RoleArn": "arn:aws:iam::123456789012:role/qbusiness-data-source-role",
        "Configuration": {
          "type": "SLACK",
          "syncMode": "FULL_CRAWL",
          "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-slack-secret",
          "enableIdentityCrawler": "true",
          "connectionConfiguration": {
            "repositoryEndpointMetadata": {
              "teamId": "T12345678"
            }
          },
          "repositoryConfigurations": {
            "All": {
              "fieldMappings": [
                {
                  "indexFieldName": "message_id",
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
            "fieldForUserId": "user_id",
            "exclusionPatterns": ["*.tmp"],
            "inclusionPatterns": ["*"],
            "crawlBotMessages": "false",
            "excludeArchived": "true",
            "conversationType": ["PUBLIC_CHANNEL", "PRIVATE_CHANNEL"],
            "channelFilter": {
              "private_channel": ["C12345678"],
              "public_channel": ["C87654321"]
            },
            "channelIdFilter": ["C12345678"],
            "sinceDate": "2023-01-01T00:00:00Z",
            "lookBack": "7",
            "enableDeletionProtection": "false",
            "deletionProtectionThreshold": "15"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")

## Slack YAML schema for using the

configuration property with AWS CloudFormation

The following is the Slack YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Slack YAML schema for using the
  configuration property with AWS CloudFormation](#slack-cfn-yaml-schema "#slack-cfn-yaml-schema")
- [Slack YAML schema example for
  using the configuration property with AWS CloudFormation](#slack-cfn-yaml-example "#slack-cfn-yaml-example")

### Slack YAML schema for using the

configuration property with AWS CloudFormation

The following is the Slack YAML schema for the configuration property for
CloudFormation.

```
type: object
properties:
  type:
    type: string
    pattern: SLACK
  syncMode:
    type: string
    enum:
      - FORCED_FULL_CRAWL
      - FULL_CRAWL
      - CHANGE_LOG
  secretArn:
    type: string
  enableIdentityCrawler:
    anyOf:
      - type: boolean
      - type: string
        enum:
          - true
          - false
  connectionConfiguration:
    type: object
    properties:
      repositoryEndpointMetadata:
        type: object
        properties:
          teamId:
            type: string
        required:
          - teamId
  repositoryConfigurations:
    type: object
    properties:
      All:
        type: object
        properties:
          fieldMappings:
            type: array
            items:
              type: object
              properties:
                indexFieldName:
                  type: string
                indexFieldType:
                  type: string
                  enum:
                    - STRING
                    - STRING_LIST
                    - DATE
                    - LONG
                dataSourceFieldName:
                  type: string
                dateFieldFormat:
                  type: string
                  pattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
              required:
                - indexFieldName
                - indexFieldType
                - dataSourceFieldName
        required:
          - fieldMappings
  additionalProperties:
    type: object
    properties:
      isCrawlAcl:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      maxFileSizeInMegaBytes:
        type: string
      fieldForUserId:
        type: string
      exclusionPatterns:
        type: array
        items:
          type: string
      inclusionPatterns:
        type: array
        items:
          type: string
      crawlBotMessages:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      excludeArchived:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
      conversationType:
        type: array
        items:
          type: string
          enum:
            - PUBLIC_CHANNEL
            - PRIVATE_CHANNEL
            - GROUP_MESSAGE
            - DIRECT_MESSAGE
      channelFilter:
        type: object
        properties:
          private_channel:
            type: array
            items:
              type: string
          public_channel:
            type: array
            items:
              type: string
      channelIdFilter:
        type: array
        items:
          type: string
      sinceDate:
        anyOf:
          - type: string
            pattern: "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
          - type: string
            pattern: ""
      lookBack:
        type: string
        pattern: "^[0-9]*$"
      enableDeletionProtection:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - true
              - false
        default: false
      deletionProtectionThreshold:
        type: string
        default: "15"
    required: []
  version:
    type: string
    anyOf:
      - pattern: 1.0.0
required:
  - type
  - secretArn
  - syncMode
  - enableIdentityCrawler
  - connectionConfiguration
  - repositoryConfigurations
  - additionalProperties
```

[Show moreShow less](# "#")

### Slack YAML schema example for

using the configuration property with AWS CloudFormation

The following is the Slack YAML example for the Configuration property for
CloudFormation:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation SLACK Data Source Template
Resources:
  DataSourceSlack:
    Type: AWS::QBusiness::DataSource
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MySlackDataSource
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: SLACK
        syncMode: FULL_CRAWL
        secretArn: arn:aws:secretsmanager:us-west-2:123456789012:secret:my-slack-secret
        enableIdentityCrawler: "true"
        connectionConfiguration:
          repositoryEndpointMetadata:
            teamId: T12345678
        repositoryConfigurations:
          All:
            fieldMappings:
              - indexFieldName: message_id
                indexFieldType: STRING
                dataSourceFieldName: id
                dateFieldFormat: yyyy-MM-dd'T'HH:mm:ss'Z'
        additionalProperties:
          isCrawlAcl: "true"
          maxFileSizeInMegaBytes: "50"
          fieldForUserId: user_id
          exclusionPatterns:
            - "*.tmp"
          inclusionPatterns:
            - "*"
          crawlBotMessages: "false"
          excludeArchived: "true"
          conversationType:
            - PUBLIC_CHANNEL
            - PRIVATE_CHANNEL
          channelFilter:
            private_channel:
              - C12345678
            public_channel:
              - C87654321
          channelIdFilter:
            - C12345678
          sinceDate: "2023-01-01T00:00:00Z"
          lookBack: "7"
          enableDeletionProtection: "false"
          deletionProtectionThreshold: "15"
```

[Show moreShow less](# "#")
