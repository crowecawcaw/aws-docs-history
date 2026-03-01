# Connecting Amazon Q Business to Microsoft OneDrive using AWS CloudFormation

You use the [`AWS::QBusiness::DataSource`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md") resource to connect a data source to
your Amazon Q application.

Use the [`configuration`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid "../../../AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.md#cfn-qbusiness-datasource-applicationid") property to provide a JSON or YAML schema with the necessary
configuration details specific to your data source connector.

To learn more about AWS CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
in the _CloudFormation User Guide_.

###### Topics

- [Microsoft OneDrive JSON schema for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-json "#onedrive-v2-cfn-json")
- [Microsoft OneDrive YAML schema for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-yaml "#onedrive-v2-cfn-yaml")

## Microsoft OneDrive JSON schema for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive JSON schema and examples for the configuration
property for AWS CloudFormation.

###### Topics

- [Microsoft OneDrive JSON schema for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-json-schema "#onedrive-v2-cfn-json-schema")
- [Microsoft OneDrive JSON schema example for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-json-example "#onedrive-v2-cfn-json-example")

### Microsoft OneDrive JSON schema for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive JSON schema for the configuration property for
CloudFormation.

```
{
    "type": "object",
    "properties": {
        "version": {
            "type": "string"
        },
        "type": {
            "type": "string",
            "enum": ["ONEDRIVEV3"]
        },
        "connectionConfiguration": {
            "type": "object",
            "properties": {
                "secretArn": {
                    "type": "string",
                    "minLength": 20,
                    "maxLength": 2048
                },
                "tenantId": {
                    "type": "string",
                    "minLength": 36,
                    "maxLength": 36
                },
                "authType": {
                    "type": "string",
                    "enum": ["OAUTH2"]
                }
            },
            "required": ["secretArn", "tenantId", "authType"]
        },
        "dataEntityConfiguration": {
            "type": "object",
            "properties": {
                "crawlPersonalDrives": {
                    "anyOf": [{
                            "type": "boolean"
                        },
                        {
                            "type": "string",
                            "enum": ["true", "false"]
                        }
                    ]
                }
            }
        },
        "filterConfiguration": {
            "type": "object",
            "properties": {
                "inclusionUserEmailAddresses": {
                    "type": "array",
                    "maxItems": 100,
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 1024
                    }
                },
                "userFilterPath": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 1024
                },
                "exclusionDriveItems": {
                    "type": "array",
                    "maxItems": 100,
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 1024
                    }
                },
                "inclusionDriveItems": {
                    "type": "array",
                    "maxItems": 100,
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 1024
                    }
                },
                "absoluteDateBefore": {
                    "type": "string",
                    "description": "ISO 8601 date-time format (e.g., 2024-12-31T23:59:59Z)"
                },
                "absoluteDateAfter": {
                    "type": "string",
                    "description": "ISO 8601 date-time format (e.g., 2024-12-31T23:59:59Z)"
                },
                "maxFileSizeInMegaBytes": {
                    "type": "string"
                }
            }
        },
        "deletionProtectionConfiguration": {
            "type": "object",
            "properties": {
                "enableDeletionProtection": {
                    "anyOf": [{
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
                    "description": "percentage value of range (0-100)"
                }
            }
        },
        "crawlIdentities": {
            "anyOf": [{
                    "type": "boolean"
                },
                {
                    "type": "string",
                    "enum": ["true", "false"]
                }
            ]
        },
        "accessControlConfiguration": {
            "type": "object",
            "properties": {
                "crawlAcl": {
                    "anyOf": [{
                            "type": "boolean"
                        },
                        {
                            "type": "string",
                            "enum": ["true", "false"]
                        }
                    ]
                }
            }
        },
        "identityLoggingStatus": {
            "type": "string",
            "enum": ["ENABLED", "DISABLED"]
        },
    },
    "required": ["connectionConfiguration", "dataEntityConfiguration", "type"]
}
```

[Show moreShow less](# "#")

### Microsoft OneDrive JSON schema example for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive JSON example for the Configuration property for
CloudFormation.

```
{
    "type": "ONEDRIVEV3",
    "crawlIdentities": false,
    "connectionConfiguration": {
      "secretArn": "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-one-drive-secret",
      "tenantId": "1234a12c-1234-1234-1abc-1234ab12a12a",
      "authType": "OAUTH2"
    },
    "dataEntityConfiguration": {
      "crawlPersonalDrives": true
    },
    "accessControlConfiguration": {
      "crawlAcl": false
    },
    "filterConfiguration": {
      "inclusionUserEmailAddresses": ["user123@amazon.com"],
      "maxFileSizeInMegaBytes": "50",
      "exclusionDriveItems": ["path/to/folder1","path/to/file1"],
       "inclusionDriveItems": ["path/to/folder2","path/to/file2"],
       "userFilterPath": "s3://bucket/prefix/object.txt",
       "absoluteDateBefore": "2025-08-02T00:00:00Z",
       "absoluteDateAfter": "2025-08-01T00:00:00Z"
    },
    "deletionProtectionConfiguration": {
      "enableDeletionProtection": true,
      "deletionProtectionThreshold": "10"
    },
    "version": "3.0.0",
    "identityLoggingStatus": "DISABLED"
}
```

[Show moreShow less](# "#")

## Microsoft OneDrive YAML schema for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive YAML schema and examples for the configuration
property for AWS CloudFormation:

###### Topics

- [Microsoft OneDrive YAML schema for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-yaml-schema "#onedrive-v2-cfn-yaml-schema")
- [Microsoft OneDrive YAML schema example for using the configuration property with AWS CloudFormation](#onedrive-v2-cfn-yaml-example "#onedrive-v2-cfn-yaml-example")

### Microsoft OneDrive YAML schema for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive YAML schema for the configuration property for
CloudFormation.

```
configuration:
  type: object
  properties:
    version:
      type: string
    type:
      type: string
      enum:
        - ONEDRIVEV3
    connectionConfiguration:
      type: object
      properties:
        secretArn:
          type: string
          minLength: 20
          maxLength: 2048
        tenantId:
          type: string
          minLength: 36
          maxLength: 36
        authType:
          type: string
          enum:
            - OAUTH2
      required:
        - secretArn
        - tenantId
        - authType
    dataEntityConfiguration:
      type: object
      properties:
        crawlPersonalDrives:
          anyOf:
            - type: boolean
            - type: string
              enum:
                - 'true'
                - 'false'
    filterConfiguration:
      type: object
      properties:
        inclusionUserEmailAddresses:
          type: array
          maxItems: 100
          items:
            type: string
            minLength: 1
            maxLength: 1024
        userFilterPath:
          type: string
          minLength: 1
          maxLength: 1024
        exclusionDriveItems:
          type: array
          maxItems: 100
          items:
            type: string
            minLength: 1
            maxLength: 1024
        inclusionDriveItems:
          type: array
          maxItems: 100
          items:
            type: string
            minLength: 1
            maxLength: 1024
        absoluteDateBefore:
          type: string
          description: 'ISO 8601 date-time format (e.g., 2024-12-31T23:59:59Z)'
        absoluteDateAfter:
          type: string
          description: 'ISO 8601 date-time format (e.g., 2024-12-31T23:59:59Z)'
        maxFileSizeInMegaBytes:
          type: string
    deletionProtectionConfiguration:
      type: object
      properties:
        enableDeletionProtection:
          anyOf:
            - type: boolean
            - type: string
              enum:
                - 'true'
                - 'false'
        deletionProtectionThreshold:
          type: string
          description: 'percentage value of range (0-100)'
    crawlIdentities:
      anyOf:
        - type: boolean
        - type: string
          enum:
            - 'true'
            - 'false'
    accessControlConfiguration:
      type: object
      properties:
        crawlAcl:
          anyOf:
            - type: boolean
            - type: string
              enum:
                - 'true'
                - 'false'
    identityLoggingStatus:
      type: string
      enum:
        - ENABLED
        - DISABLED
  required:
    - connectionConfiguration
    - dataEntityConfiguration
    - type
```

[Show moreShow less](# "#")

### Microsoft OneDrive YAML schema example for using the configuration property with AWS CloudFormation

The following is the Microsoft OneDrive YAML example for the Configuration property for
CloudFormation:

```
configuration:
  type: ONEDRIVEV3
  crawlIdentities: false
  connectionConfiguration:
    secretArn: 'arn:aws:secretsmanager:us-west-2:123456789012:secret:my-one-drive-secret'
    tenantId: '1234a12c-1234-1234-1abc-1234ab12a12a'
    authType: OAUTH2
  dataEntityConfiguration:
    crawlPersonalDrives: true
  accessControlConfiguration:
    crawlAcl: false
  filterConfiguration:
    inclusionUserEmailAddresses:
      - 'user123@amazon.com'
    maxFileSizeInMegaBytes: '50'
    exclusionDriveItems:
      - 'path/to/folder1'
      - 'path/to/file1'
    inclusionDriveItems:
      - 'path/to/folder2'
      - 'path/to/file2'
    userFilterPath: 's3://bucket/prefix/object.txt'
    absoluteDateBefore: '2025-08-02T00:00:00Z'
    absoluteDateAfter: '2025-08-01T00:00:00Z'
  deletionProtectionConfiguration:
    enableDeletionProtection: true
    deletionProtectionThreshold: '10'
  version: '3.0.0'
  identityLoggingStatus: DISABLED
```

[Show moreShow less](# "#")
