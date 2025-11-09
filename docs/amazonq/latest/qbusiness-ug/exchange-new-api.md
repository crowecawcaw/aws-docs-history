# Connecting Amazon Q Business to Microsoft Exchange (New connector)

using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Microsoft Exchange new connector JSON schema

The following shows the Microsoft Exchange new connector JSON schema:

```
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": ["MSEXCHANGEV2"]
        },
        "connectionConfiguration": {
            "type": "object",
            "properties": {
                "secretArn": {
                    "type": "string",
                    "pattern": "^arn:[a-z0-9-\\.]{1,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[^/].{0,1023}$"
                },
                "tenantId": {
                    "type": "string",
                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
                    "minLength": 36,
                    "maxLength": 36
                }
            },
            "required": ["tenantId", "secretArn"]
        },
        "dataEntityConfiguration": {
            "type": "object",
            "properties": {
            }
        },
        "filterConfiguration": {
            "type": "object",
            "properties": {
                "startDateFilter": {
                    "type": "string",
                    "format": "date-time"
                },
                "endDateFilter": {
                    "type": "string",
                    "format": "date-time"
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
                    "type": "string",
                    "pattern": "^(100|[1-9][0-9]?)$"
                }
            },
            "required": ["enableDeletionProtection", "deletionProtectionThreshold"]
        }
    },
    "required": [
        "type",
        "connectionConfiguration",
        "dataEntityConfiguration"
    ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure for the new Microsoft Exchange connector.

| Configuration                     | Description                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                            | The type of data source. Specify `MSEXCHANGEV2` for the new Microsoft Exchange connector.                                                                                                                      |
| `connectionConfiguration`         | Configuration information for connecting to the Microsoft Exchange data source.                                                                                                                                |
| `secretArn`                       | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains<br>the key-value pairs required to connect to your Exchange data source. This includes your<br>client ID and your client secret. |
| `tenantId`                        | The Microsoft 365 tenant ID (UUID v4 format). You can find your tenant ID in the Properties of your<br>Azure Active Directory Portal.                                                                          |
| `dataEntityConfiguration`         | Configuration for the types of data entities to crawl from Microsoft Exchange.                                                                                                                                 |
| `filterConfiguration`             | Optional configuration for filtering content during the crawl process.                                                                                                                                         |
| `startDateFilter`                 | Specify the start date for filtering emails. Only emails created on or after this date will be crawled. Format: ISO 8601 date-time (e.g., `2025-06-01T00:00:00Z`).                                             |
| `endDateFilter`                   | Specify the end date for filtering emails. Only emails created on or before this date will be crawled. Format: ISO 8601 date-time (e.g., `2025-07-01T00:00:00Z`).                                              |
| `deletionProtectionConfiguration` | Optional configuration to protect against accidental deletion of large amounts of content.                                                                                                                     |
| `enableDeletionProtection`        | A Boolean value to enable deletion protection. When enabled, the connector will not delete more than the specified threshold of documents in a single sync.                                                    |
| `deletionProtectionThreshold`     | The maximum percentage of documents that can be deleted in a single sync when deletion protection is enabled. Must be a string representing a number from 1-100 (e.g., "10" for 10%).                          |

## Sample configuration for the new Microsoft Exchange connector

The following is a sample configuration for the new Microsoft Exchange connector:

```
{
    "displayName": "mail-0910-sample",
    "configuration": {
        "connectionConfiguration": {
            "secretArn": "arn:aws:secretsmanager:<region>:<account>:secret:<secret>",
            "tenantId": "<tenant_id>"
        },
        "dataEntityConfiguration": {
        },
        "filterConfiguration": {
            "startDateFilter": "2025-06-01T00:00:00Z",
            "endDateFilter": "2025-07-01T00:00:00Z"
        },
        "deletionProtectionConfiguration": {
            "enableDeletionProtection": true,
            "deletionProtectionThreshold": "10"
        },
        "type": "MSEXCHANGEV2",
        "version": "1.0.0"
    },
    "description": "Sample Config",
    "syncSchedule": "",
    "roleArn": "arn:aws:iam::<account>:role/service-role/<role_name>",
    "mediaExtractionConfiguration": {}
}
```

[Show moreShow less](# "#")
