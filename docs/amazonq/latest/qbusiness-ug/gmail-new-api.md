# Connecting Amazon Q Business to Gmail

using the new connector (API)

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

## New Gmail connector JSON schema

The following is the new Gmail connector JSON schema:

```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": ["GMAILV2"]
    },
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "secretArn": {
          "type": "string",
          "pattern": "^arn:[a-z0-9-\\.]{1,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[^/].{0,1023}$"
        }
      },
      "required": ["secretArn"]
    },
    "dataEntityConfiguration": {
      "type": "object",
      "properties": {
        "crawlDraftEmails": {
          "type": "boolean"
        }
      }
    },
    "filterConfiguration": {
      "type": "object",
      "properties": {
        "maxFileSizeInMegaBytes": {
          "type": "string",
          "pattern": "^\\d+$"
        },
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
The following table provides information about important JSON keys to configure for the new Gmail connector.

| Configuration                     | Description                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                            | The type of data source. Specify `GMAILV2` for the new Gmail connector.                                                                                                                                                                                                                                                             |
| `connectionConfiguration`         | Configuration information for connecting to the Gmail data source.                                                                                                                                                                                                                                                                  |
| `secretArn`                       | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains the key-value pairs required to connect to your Gmail. The secret must contain a JSON structure with the following keys: ``{ "adminAccountEmailId": `"${adminAccountEmailId}"`, "clientEmailId": `"${clientEmailId}"`, "privateKey": `"${privateKey}"` }`` |
| `dataEntityConfiguration`         | Configuration for the types of data entities to crawl.                                                                                                                                                                                                                                                                              |
| `crawlDraftEmails`                | A Boolean value to choose whether you want to crawl draft messages. Default is `false`.                                                                                                                                                                                                                                             |
| `filterConfiguration`             | Optional filtering configuration for the data source.                                                                                                                                                                                                                                                                               |
| `maxFileSizeInMegaBytes`          | Specify the maximum single file size limit in MBs that Amazon Q will crawl. Amazon Q will crawl only the files within the size limit you define. The default file size is 50MB. The maximum file size should be greater than 0MB and less than or equal to 50MB.                                                                    |
| `startDateFilter`                 | Specify messages to be included from a certain start date onwards. Use ISO 8601 date-time format.                                                                                                                                                                                                                                   |
| `endDateFilter`                   | Specify messages to be included up to a certain end date. Use ISO 8601 date-time format.                                                                                                                                                                                                                                            |
| `deletionProtectionConfiguration` | Configuration for deletion protection to prevent accidental data loss.                                                                                                                                                                                                                                                              |
| `enableDeletionProtection`        | A Boolean value to enable deletion protection. When enabled, prevents deletion of more than the specified threshold percentage of documents.                                                                                                                                                                                        |
| `deletionProtectionThreshold`     | The maximum percentage (1-100) of documents that can be deleted in a single sync. Required when deletion protection is enabled.                                                                                                                                                                                                     |
