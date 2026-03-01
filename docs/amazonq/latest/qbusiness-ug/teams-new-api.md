# Connecting Amazon Q Business to Microsoft Teams (new connector) using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Microsoft Teams new connector JSON schema

The following is the Microsoft Teams new connector JSON schema:

```
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "$id": "https://amazonaws.com/plato/connector/configuration/msteams",
  "title": "Microsoft Teams Configuration Schema",
  "description": "JSON Schema for Microsoft Teams data connector configuration based on Smithy model",
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "MSTEAMSV2"
      ],
      "description": "The connector type identifier"
    },
    "connectionConfiguration": {
      "type": "object",
      "description": "Configuration for connecting to Microsoft Teams",
      "properties": {
        "tenantId": {
          "type": "string",
          "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
          "minLength": 36,
          "maxLength": 36,
          "description": "Microsoft Teams tenant ID in UUID v4 format"
        },
        "secretArn": {
          "type": "string",
          "pattern": "^arn:[a-z0-9-\\.]{1,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[^/].{0,1023}$",
          "description": "ARN of the AWS Secrets Manager secret containing authentication credentials"
        }
      },
      "required": ["tenantId", "secretArn"],
      "additionalProperties": false
    },
    "filterConfiguration": {
      "type": "object",
      "description": "Configuration for filtering data based on date ranges",
      "properties": {
        "startDateFilter": {
          "type": "string",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$",
          "description": "Start date for filtering data in ISO 8601 format"
        },
        "endDateFilter": {
          "type": "string",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$",
          "description": "End date for filtering data in ISO 8601 format"
        }
      },
      "additionalProperties": false
    },
    "dataEntityConfiguration": {
      "type": "object",
      "description": "Configuration for specifying which data entities to crawl",
      "properties": {
        "crawlChatMessages": {
          "type": "boolean",
          "description": "Whether to crawl chat messages from Microsoft Teams"
        },
        "crawlChannelPosts": {
          "type": "boolean",
          "description": "Whether to crawl channel posts from Microsoft Teams"
        }
      },
      "additionalProperties": false
    },
    "deletionProtectionConfiguration": {
      "type": "object",
      "description": "Configuration for deletion protection settings",
      "properties": {
        "enableDeletionProtection": {
          "type": "boolean",
          "description": "Whether to enable deletion protection"
        },
        "deletionProtectionThreshold": {
          "type": "string",
          "pattern": "^(100|[1-9][0-9]?)$",
          "description": "Deletion protection threshold as a percentage (1-100)"
        }
      },
      "additionalProperties": false
    }
  },
  "required": [
    "type",
    "connectionConfiguration",
    "dataEntityConfiguration"
  ],
  "additionalProperties": false,
  "examples": [
    {
      "type": "MSTEAMSV2",
      "connectionConfiguration": {
        "tenantId": "12345678-1234-4123-8123-123456789012",
        "secretArn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:msteams-credentials-AbCdEf"
      },
      "filterConfiguration": {
        "startDateFilter": "2024-01-01T00:00:00Z",
        "endDateFilter": "2024-12-31T23:59:59Z"
      },
      "dataEntityConfiguration": {
        "crawlChatMessages": true,
        "crawlChannelPosts": true
      },
      "deletionProtectionConfiguration": {
        "enableDeletionProtection": true,
        "deletionProtectionThreshold": "10"
      }
    }
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure for the new Microsoft Teams connector.

| Configuration                     | Description                                                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                            | The type of data source. Must be `MSTEAMSV2` for the new Teams connector.                                                                                            |
| `connectionConfiguration`         | Configuration information for connecting to the Teams data source.                                                                                                   |
| `tenantId`                        | The Microsoft Teams tenant ID in UUID v4 format.                                                                                                                     |
| `secretArn`                       | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs<br>required to connect to your Microsoft Teams.                         |
| `dataEntityConfiguration`         | Configuration for the types of data entities to crawl from Teams.                                                                                                    |
| `crawlChatMessages`               | A Boolean value to specify whether to crawl chat messages. Set to `true` to include chat messages in the crawl, or `false` to exclude them.                          |
| `crawlChannelPosts`               | A Boolean value to specify whether to crawl channel posts. Set to `true` to include channel posts in the crawl, or `false` to exclude them.                          |
| `filterConfiguration`             | Optional configuration for filtering content during the crawl process.                                                                                               |
| `startDateFilter`                 | Specify the start date for filtering content. Only content created on or after this date will be crawled. Format: ISO 8601 date-time format.                         |
| `endDateFilter`                   | Specify the end date for filtering content. Only content created on or before this date will be crawled. Format: ISO 8601 date-time format.                          |
| `deletionProtectionConfiguration` | Optional configuration to protect against accidental deletion of large amounts of content.                                                                           |
| `enableDeletionProtection`        | A Boolean value to enable deletion protection. When enabled, the connector will not delete more than the specified threshold of documents in a single sync.          |
| `deletionProtectionThreshold`     | The maximum percentage of documents that can be deleted in a single sync when deletion protection is enabled. Specify as a string containing a number from 1 to 100. |
