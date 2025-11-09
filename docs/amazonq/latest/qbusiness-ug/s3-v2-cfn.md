# Connecting Amazon Q Business to Amazon S3 using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _AWS CloudFormation User Guide_.

###### Topics

- [Amazon S3 configuration properties](#s3-v2-configuration-keys "#s3-v2-configuration-keys")
- [Amazon S3 JSON schema for using the configuration
  property with AWS CloudFormation](#s3-v2-cfn-json "#s3-v2-cfn-json")
- [Amazon S3 YAML schema for using the configuration
  property with AWS CloudFormation](#s3-v2-cfn-yaml "#s3-v2-cfn-yaml")

## Amazon S3 configuration properties

The following provides information about important configuration properties required in the schema.

| Configuration                     | Description                                                                                                                                                                                              | Type                                                                                                  | Required |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `type`                            | The type of data source. Specify `S3V2` as your data source<br>type.                                                                                                                                     | `string`<br>The only allowed value is `S3V2`.                                                         | Yes      |
| `connectionConfiguration`         | Configuration information for the endpoint for the data<br>source.                                                                                                                                       | `object`<br>This property has sub-properties: `bucketName` and `bucketOwnerAccountId`.                | Yes      |
| `bucketName`                      | The name of your Amazon S3 bucket. This is a sub-property for the<br>`connectionConfiguration`.                                                                                                          | `string`                                                                                              | Yes      |
| `bucketOwnerAccountId`            | The 12-digit AWS account ID that owns the S3 bucket. This is a sub-property for the<br>`connectionConfiguration`.                                                                                        | `string`<br>Must match pattern: `^\d{12}$`                                                            | Yes      |
| `filterConfiguration`             | Configuration for filtering which files to include or exclude from indexing.                                                                                                                             | `object`<br>This property has sub-properties for patterns, prefixes, and file size limits.            | No       |
| `inclusionPatterns`               | File patterns to include during indexing . This is a sub-property for the<br>`filterConfiguration`.                                                                                                      | `array` of `string`                                                                                   | No       |
| `exclusionPatterns`               | File patterns to exclude during indexing. This is a sub-property for the<br>`filterConfiguration`.                                                                                                       | `array` of `string`                                                                                   | No       |
| `inclusionPrefixes`               | S3 key prefixes to include during indexing (e.g., documents/, reports/). This is a sub-property for the<br>`filterConfiguration`.                                                                        | `array` of `string`                                                                                   | No       |
| `exclusionPrefixes`               | S3 key prefixes to exclude during indexing (e.g., temp/, cache/). This is a sub-property for the<br>`filterConfiguration`.                                                                               | `array` of `string`                                                                                   | No       |
| `maxFileSizeInMegaBytes`          | Maximum file size in megabytes to index. Files larger than this will be skipped. This is a sub-property for the<br>`filterConfiguration`.                                                                | `number`<br>Minimum: 0, Maximum: 10240                                                                | No       |
| `accessControlConfiguration`      | Configuration for access control and permissions.                                                                                                                                                        | `object`<br>This property has sub-properties for ACL configuration and default access type.           | No       |
| `aclConfigurationFilePath`        | Path to the ACL configuration file in your S3 bucket. This is a sub-property for the<br>`accessControlConfiguration`.                                                                                    | `string`<br>Length: 1-1024 characters                                                                 | No       |
| `deletionProtectionConfiguration` | Configuration for deletion protection to prevent accidental bulk deletions.                                                                                                                              | `object`<br>This property has sub-properties for enabling deletion protection and setting thresholds. | No       |
| `enableDeletionProtection`        | Whether to enable deletion protection. This is a sub-property for the<br>`deletionProtectionConfiguration`.                                                                                              | `boolean`                                                                                             | No       |
| `deletionProtectionThreshold`     | Percentage threshold for deletion protection. If more than this percentage of documents would be deleted, the sync will be blocked. This is a sub-property for the<br>`deletionProtectionConfiguration`. | `number`<br>Default: 15                                                                               | No       |
| `metadataFilesPrefix`             | S3 key prefix where metadata files are stored for enhanced document processing.                                                                                                                          | `string`<br>Length: 1-1024 characters                                                                 | No       |

## Amazon S3 JSON schema for using the configuration

property with AWS CloudFormation

The following is the Amazon S3 JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Amazon S3 JSON schema for using the
  configuration property with AWS CloudFormation](#s3-v2-cfn-json-schema "#s3-v2-cfn-json-schema")
- [Amazon S3 JSON schema example for using the
  configuration property with AWS CloudFormation](#s3-v2-cfn-json-example "#s3-v2-cfn-json-example")

### Amazon S3 JSON schema for using the

configuration property with AWS CloudFormation

The following is the Amazon S3 JSON schema for the configuration property for
AWS CloudFormation.

```
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "pattern": "S3V2"
    },
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "bucketName": {
          "type": "string"
        },
        "bucketOwnerAccountId": {
          "type": "string",
          "pattern": "^\\d{12}$"
        }
      },
      "required": ["bucketName", "bucketOwnerAccountId"]
    },
    "filterConfiguration": {
      "type": "object",
      "properties": {
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
        },
        "inclusionPrefixes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionPrefixes": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "maxFileSizeInMegaBytes": {
          "type": "number",
          "minimum": 0,
          "maximum": 10240
        }
      }
    },
    "accessControlConfiguration": {
      "type": "object",
      "properties": {
        "aclConfigurationFilePath": {
          "type": "string",
          "minLength": 1,
          "maxLength": 1024
        }
      }
    },
    "deletionProtectionConfiguration": {
      "type": "object",
      "properties": {
        "enableDeletionProtection": {
          "type": "boolean"
        },
        "deletionProtectionThreshold": {
          "type": "number",
          "default": 15
        }
      }
    },
    "metadataFilesPrefix": {
      "type": "string",
      "minLength": 1,
      "maxLength": 1024
    }
  },
  "required": [
    "type",
    "connectionConfiguration"
  ]
}
```

[Show moreShow less](# "#")

### Amazon S3 JSON schema example for using the

configuration property with AWS CloudFormation

The following is the Amazon S3 JSON example for the Configuration property for
AWS CloudFormation.

```
{
  "type": "S3V2",
  "connectionConfiguration": {
    "bucketName": "my-company-data-bucket",
    "bucketOwnerAccountId": "123456789012"
  },
  "filterConfiguration": {
    "inclusionPatterns": ["*.pdf", "*.docx", "*.txt"],
    "exclusionPatterns": ["*.tmp", "*.log"],
    "inclusionPrefixes": ["documents/", "reports/"],
    "exclusionPrefixes": ["temp/", "cache/"],
    "maxFileSizeInMegaBytes": 100
  },
  "accessControlConfiguration": {
    "aclConfigurationFilePath": "config/acl-config.json"
  },
  "deletionProtectionConfiguration": {
    "enableDeletionProtection": true,
    "deletionProtectionThreshold": 15
  },
  "metadataFilesPrefix": "metadata/"
}
```

[Show moreShow less](# "#")

## Amazon S3 YAML schema for using the configuration

property with AWS CloudFormation

The following is the Amazon S3 YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Amazon S3 YAML schema example for using the
  configuration property with AWS CloudFormation](#s3-v2-cfn-yaml-example "#s3-v2-cfn-yaml-example")

### Amazon S3 YAML schema example for using the

configuration property with AWS CloudFormation

The following is the Amazon S3 YAML example for the Configuration property for
AWS CloudFormation:

```
AWSTemplateFormatVersion: "2010-09-09"
Description: "CloudFormation Amazon S3 Data Source Template"
Resources:
  DataSourceS3V2:
    Type: "AWS::QBusiness::DataSource"
    Properties:
      ApplicationId: app12345-1234-1234-1234-123456789012
      IndexId: indx1234-1234-1234-1234-123456789012
      DisplayName: MyS3DataSourceV2
      RoleArn: arn:aws:iam::123456789012:role/qbusiness-data-source-role
      Configuration:
        type: S3V2
        connectionConfiguration:
          bucketName: my-company-data-bucket
          bucketOwnerAccountId: "123456789012"
        filterConfiguration:
          inclusionPatterns:
            - "*.pdf"
            - "*.docx"
            - "*.txt"
          exclusionPatterns:
            - "*.tmp"
            - "*.log"
          inclusionPrefixes:
            - "documents/"
            - "reports/"
          exclusionPrefixes:
            - "temp/"
            - "cache/"
          maxFileSizeInMegaBytes: 100
        accessControlConfiguration:
          aclConfigurationFilePath: "config/acl-config.json"
        deletionProtectionConfiguration:
          enableDeletionProtection: true
          deletionProtectionThreshold: 15
        metadataFilesPrefix: "metadata/"
```

[Show moreShow less](# "#")
