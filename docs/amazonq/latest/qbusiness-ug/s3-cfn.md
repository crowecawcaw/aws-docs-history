# Connecting Amazon Q Business to Amazon S3 using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [Amazon S3 configuration properties](#s3-configuration-keys "#s3-configuration-keys")
- [Amazon S3 JSON schema for using the configuration property with AWS CloudFormation](#s3-cfn-json "#s3-cfn-json")
- [Amazon S3 YAML schema for using the configuration property with AWS CloudFormation](#s3-cfn-yaml "#s3-cfn-yaml")

## Amazon S3 configuration properties

The following provides information about important configuration properties required in the
schema.

| Configuration                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                          | Required |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `type`                                                                                                                                                                     | The type of data source. Specify `S3` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                           | `string`<br>The only allowed value is `S3`.                                                                                                                                                                                                                                                                                                   | Yes      |
| `syncMode`                                                                                                                                                                 | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                  | `string`<br>You can choose from the following options:<br>• Use `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• Use `FULL_CRAWL` to incrementally crawl only new, modified, and<br>deleted content each time your data source syncs with your index | Yes      |
| `connectionConfiguration`                                                                                                                                                  | Configuration information for the endpoint for the data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                           | `object`<br>This property has a sub-property called<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                          | Yes      |
| `repositoryEndpointMetadata`                                                                                                                                               | This is the endpoint information for the data source. This is a sub-property<br>for the `connectionConfiguration`.                                                                                                                                                                                                                                                                                                                                                                                           | `object`<br>This property has a sub-property called `BucketName`.                                                                                                                                                                                                                                                                             | Yes      |
| `BucketName`                                                                                                                                                               | The name of your Amazon S3 bucket. This is a sub-property for the<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                                                                                                                           | `string`                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `repositoryConfigurations`                                                                                                                                                 | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                      | `object`<br>This property has a sub-property called `document`.                                                                                                                                                                                                                                                                               | Yes      |
| `document`                                                                                                                                                                 | This property has information related to the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `object`This property has a sub-property called<br>`fieldMappings`.                                                                                                                                                                                                                                                                           | Yes      |
| `fieldMappings`                                                                                                                                                            | This property has information related to the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `array`This property has the following<br>sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`                                                                                                                                                                                                              | Yes      |
| `indexFieldName`                                                                                                                                                           | The name of the index field. This is a sub-property for the<br>`fieldMappings`.                                                                                                                                                                                                                                                                                                                                                                                                                              | `string`                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `indexFieldType`                                                                                                                                                           | The type of the index field. This is a sub-property for the<br>`fieldMappings`.                                                                                                                                                                                                                                                                                                                                                                                                                              | `string`<br>The only allowed value is `STRING`.                                                                                                                                                                                                                                                                                               | Yes      |
| `dataSourceFieldName`                                                                                                                                                      | The field name of the data source. This is a sub-property for the<br>`fieldMappings`.                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `additionalProperties`                                                                                                                                                     | Additional configuration options for your content in your data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                    | `object`This property has the following<br>sub-properties that are not required<br>• `aclConfigurationFilePath`<br>• `metadataFilesPrefix`.<br>• `maxFileSizeInMegaBytes`<br>• `inclusionPatterns`<br>• `exclusionPatterns`<br>• `inclusionPrefixes`<br>• `exclusionPrefixes`                                                                 | No       |
| `aclConfigurationFilePath`                                                                                                                                                 | The path to the file that controls access control information for your<br>documents in an Amazon Q index. This is a sub-property of<br>`additionalProperties`.                                                                                                                                                                                                                                                                                                                                               | `string`                                                                                                                                                                                                                                                                                                                                      | No       |
| `metadataFilesPrefix`                                                                                                                                                      | The location, in your Amazon S3 bucket, of your document metadata<br>files. This is a sub-property of `additionalProperties`.                                                                                                                                                                                                                                                                                                                                                                                | `string`                                                                                                                                                                                                                                                                                                                                      | No       |
| `maxFileSizeInMegaBytes`                                                                                                                                                   | Specify the maximum single file size limit in MBs that Amazon Q will crawl.<br>Amazon Q will crawl only the files within the size limit you define. The<br>default file size is 50MB. The maximum file size should be greater than 0MB and less<br>than or equal to 50MB. You can go up to 10 GB (10240 MB) if you enable **Video<br>files\*<br>• in **Multi-media content*<br>• configuration, and up<br>to 2 GB (2048 MB) if you enable \*\*Audio files*<br>• in<br>**Multi-media content configuration**. | `string`<br>You can enter a value between `0` and<br>`10240`.                                                                                                                                                                                                                                                                                 | No       |
| All of these following are sub-properties of<br>`additionalProperties`<br>• `inclusionPatterns`<br>• `exclusionPatterns`<br>• `inclusionPrefixes`<br>• `exclusionPrefixes` | A list of regular expression patterns to include or exclude specific files in<br>your Amazon S3 data source. Files that match the patterns are included in the<br>index. Files that don't match the patterns are excluded from the index. If a file<br>matches both an inclusion and exclusion pattern, the exclusion pattern takes<br>precedence and the file isn't included in the index.                                                                                                                  | `array`                                                                                                                                                                                                                                                                                                                                       | No       |
| `version`                                                                                                                                                                  | The version of the template that's supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `string`<br>The default value is `1.0.0`.                                                                                                                                                                                                                                                                                                     | No       |

## Amazon S3 JSON schema for using the configuration property with AWS CloudFormation

The following is the Amazon S3 JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Amazon S3 JSON schema for using the configuration property with AWS CloudFormation](#s3-cfn-json-schema "#s3-cfn-json-schema")
- [Amazon S3 JSON schema example for using the configuration property with AWS CloudFormation](#s3-cfn-json-example "#s3-cfn-json-example")

### Amazon S3 JSON schema for using the configuration property with AWS CloudFormation

The following is the Amazon S3 JSON schema for the configuration property for
CloudFormation.

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "pattern": "S3"
    },
    "syncMode": {
      "type": "string",
      "enum": ["FULL_CRAWL", "FORCED_FULL_CRAWL"]
    },
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "BucketName": {
              "type": "string"
            }
          },
          "required": ["BucketName"]
        }
      },
      "required": ["repositoryEndpointMetadata"]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "document": {
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
          },
          "required": ["fieldMappings"]
        }
      },
      "required": ["document"]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "inclusionPatterns": {
          "type": "array"
        },
        "exclusionPatterns": {
          "type": "array"
        },
        "inclusionPrefixes": {
          "type": "array"
        },
        "exclusionPrefixes": {
          "type": "array"
        },
        "aclConfigurationFilePath": {
          "type": "string"
        },
        "metadataFilesPrefix": {
          "type": "string"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string"
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
          ]
        },
        "deletionProtectionThreshold": {
          "type": "string",
          "default": "15"
        }
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
  },
  "required": [
    "type",
    "syncMode",
    "connectionConfiguration",
    "repositoryConfigurations"
  ]
}
```

[Show moreShow less](# "#")

### Amazon S3 JSON schema example for using the configuration property with AWS CloudFormation

The following is the Amazon S3 JSON example for the Configuration property for
CloudFormation.

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "CloudFormation Amazon S3 Data Source Template",
  "Resources": {
    "DataSourceS3": {
      "Type": "AWS::QBusiness::DataSource",
      "Properties": {
        "ApplicationId": "app12345-1234-1234-1234-123456789012",
        "IndexId": "indx1234-1234-1234-1234-123456789012",
        "DisplayName": "MyS3DataSource",
        "RoleArn": "arn:aws:iam::123456789012:role/qbusiness-data-source-role",
        "Configuration": {
          "type": "S3",
          "syncMode": "FULL_CRAWL",
          "connectionConfiguration": {
            "repositoryEndpointMetadata": {
              "BucketName": "my-company-data-bucket"
            }
          },
          "repositoryConfigurations": {
            "document": {
              "fieldMappings": [
                {
                  "dataSourceFieldName": "content",
                  "indexFieldName": "document_content",
                  "indexFieldType": "STRING"
                }
              ]
            }
          },
          "additionalProperties": {
            "inclusionPatterns": ["*.pdf", "*.docx"],
            "exclusionPatterns": ["*.tmp"],
            "inclusionPrefixes": ["/important-docs/"],
            "exclusionPrefixes": ["/temporary/"],
            "aclConfigurationFilePath": "/configs/acl.json",
            "metadataFilesPrefix": "/metadata/",
            "maxFileSizeInMegaBytes": "50"
          }
        }
      }
    }
  }
}
```

[Show moreShow less](# "#")

## Amazon S3 YAML schema for using the configuration property with AWS CloudFormation

The following is the Amazon S3 YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Amazon S3 YAML schema for using the configuration property with AWS CloudFormation](#s3-cfn-yaml-schema "#s3-cfn-yaml-schema")
- [Amazon S3 YAML schema example for using the configuration property with AWS CloudFormation](#s3-cfn-yaml-example "#s3-cfn-yaml-example")

### Amazon S3 YAML schema for using the configuration property with AWS CloudFormation

The following is the Amazon S3 YAML schema for the configuration property for
CloudFormation.

```
type: object
properties:
  type:
    type: string
    pattern: S3
  syncMode:
    type: string
    enum:
      - FULL_CRAWL
      - FORCED_FULL_CRAWL
  connectionConfiguration:
    type: object
    properties:
      repositoryEndpointMetadata:
        type: object
        properties:
          BucketName:
            type: string
        required:
          - BucketName
    required:
      - repositoryEndpointMetadata
  repositoryConfigurations:
    type: object
    properties:
      document:
        type: object
        properties:
          fieldMappings:
            type: array
            items:
              - type: object
                properties:
                  indexFieldName:
                    type: string
                  indexFieldType:
                    type: string
                    enum:
                      - STRING
                  dataSourceFieldName:
                    type: string
                required:
                  - indexFieldName
                  - indexFieldType
                  - dataSourceFieldName
        required:
          - fieldMappings
    required:
      - document
  additionalProperties:
    type: object
    properties:
      inclusionPatterns:
        type: array
      exclusionPatterns:
        type: array
      inclusionPrefixes:
        type: array
      exclusionPrefixes:
        type: array
      aclConfigurationFilePath:
        type: string
      metadataFilesPrefix:
        type: string
      maxFileSizeInMegaBytes:
        type: string
      enableDeletionProtection:
        anyOf:
          - type: boolean
          - type: string
            enum:
              - "true"
              - "false"
      deletionProtectionThreshold:
        type: string
        default: "15"
version:
  type: string
  anyOf:
    - pattern: 1.0.0
required:
  - type
  - syncMode
  - connectionConfiguration
  - repositoryConfigurations
```

[Show moreShow less](# "#")

### Amazon S3 YAML schema example for using the configuration property with AWS CloudFormation

The following is the Amazon S3 YAML example for the Configuration property for
CloudFormation:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: "CloudFormation Amazon S3 Data Source Template"
Resources:
  DataSourceS3:
    Type: "AWS::QBusiness::DataSource"
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MyS3DataSource
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: S3
        syncMode: FULL_CRAWL
        connectionConfiguration:
          repositoryEndpointMetadata:
            BucketName: my-company-data-bucket
        repositoryConfigurations:
          document:
            fieldMappings:
              - dataSourceFieldName: content
                indexFieldName: document_content
                indexFieldType: STRING
        additionalProperties:
          inclusionPatterns:
            - "*.pdf"
            - "*.docx"
          exclusionPatterns:
            - "*.tmp"
          inclusionPrefixes:
            - "/important-docs/"
          exclusionPrefixes:
            - "/temporary/"
          aclConfigurationFilePath: "/configs/acl.json"
          metadataFilesPrefix: "/metadata/"
          maxFileSizeInMegaBytes: "50"
```

[Show moreShow less](# "#")
