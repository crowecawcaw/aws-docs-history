# Connecting Amazon Q Business to Microsoft OneDrive using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## Microsoft OneDrive JSON schema

The following is the Microsoft OneDrive JSON schema for OneDrive:

```
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "pattern": "2.0.0"
    },
    "type": {
      "type": "string",
      "enum": [
        "ONEDRIVEV3"
      ]
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
          "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
          "minLength": 36,
          "maxLength": 36
        },
        "authType": {
          "type": "string",
          "enum": [
            "ENTRA_APP_ID",
            "OAUTH2"
          ]
        }
      },
      "required": [
        "secretArn",
        "tenantId",
        "authType"
      ]
    },
    "dataEntityConfiguration": {
      "type": "object",
      "properties": {
        "crawlPersonalDrives": {
          "type": "boolean"
        }
      }
    },
    "filterConfiguration": {
      "type": "object",
      "properties": {
        "exclusionUserEmailAddresses": {
          "type": "array",
          "maxItems": 100,
          "items": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
          }
        },
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
          "pattern": "^s3:\\/\\/[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]\\/.*$"
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
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
        },
        "absoluteDateAfter": {
          "type": "string",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:\\.\\d+)?(?:Z|[+-]\\d{2}:\\d{2})$"
        },
        "maxFileSizeInMegaBytes": {
          "type": "string",
          "pattern": "^\\d+$"
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
      }
    },
    "crawlIdentities": {
      "type": "boolean"
    },
    "accessControlConfiguration": {
      "type": "object",
      "properties": {
        "crawlAcls": {
          "type": "boolean"
        }
      }
    }
  },
  "required": [
    "connectionConfiguration",
    "dataEntityConfiguration",
    "type"
  ]
}
```

[Show moreShow less](# "#")
The following table provides information about important JSON keys to configure for OneDrive (New).

| Configuration                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accessControlConfiguration`      | Configuration for access control: `crawlAcls`: Boolean flag to enable/disable crawling of access control lists. Specify `true` to crawl access control information from documents. Amazon Q crawls ACL information by default to ensure responses are generated only from documents your end users have access to.                                                                                                                                                                                                                                                                                                                                                  |
| `crawlIdentities`                 | Boolean flag to enable/disable crawling of identity information. `true` to activate identity crawler. Identity crawler is activated by default. Crawling identity information on users and groups with access to specific documents is useful for user context filtering. Search results are filtered based on the user or their group access to documents.                                                                                                                                                                                                                                                                                                         |
| `deletionProtectionConfiguration` | Configuration for deletion protection: `enableDeletionProtection`: Boolean flag to enable/disable deletion protection. `deletionProtectionThreshold`: Threshold percentage (1-100) for deletion protection.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `filterConfiguration`             | Configuration for filtering content:<br>• `exclusionUserEmailAddresses`: List of user email addresses to<br>exclude from crawling.<br>• `inclusionUserEmailAddresses`: List of user email addresses to<br>include in crawling.<br>• `userFilterPath`: S3 path for user filter file.<br>• `exclusionDriveItems`: List of drive items to exclude.<br>• `inclusionDriveItems`: List of drive items to include.<br>• `absoluteDateBefore`: Filter for content modified before this<br>date.<br>• `absoluteDateAfter`: Filter for content modified after this<br>date.<br>• `maxFileSizeInMegaBytes`: Maximum single file size limit in MBs<br>that Amazon Q will crawl. |
| `dataEntityConfiguration`         | Configuration for what content to crawl: `crawlPersonalDrives`: Boolean flag to enable/disable crawling of personal drives.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `connectionConfiguration`         | Configuration information for connecting to OneDrive: `secretArn`: The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains authentication credentials. The secret must contain a JSON structure with the following keys: `{"clientID": "OAuth Client ID", "clientSecret": "client secret"}`. `tenantId`: The tenant ID in UUID format. `authType`: Authentication type, either "ENTRA_APP_ID" or "OAUTH2".                                                                                                                                                                                                                                    |
| `type`                            | The type of data source. Specify `ONEDRIVEV3` as your data source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `version`                         | The version of this template. Currently supported version is "2.0.0".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
