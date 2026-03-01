# Connecting Amazon Q Business to Google Calendar using APIs

You use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to your
Amazon Q application. You can also use the [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") action to modify an existing data source configuration.

Then, you use the
`configuration` parameter to provide a JSON blob that conforms the AWS-defined JSON schema.

For an example of the API request, see [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") and [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md") in the Amazon Q API Reference.

###### Topics

- [Google Calendar configuration properties](#gcal-configuration-keys "#gcal-configuration-keys")
- [Google Calendar JSON schema](#gcal-json "#gcal-json")
- [Google Calendar JSON schema example](#s3-api-json-example "#s3-api-json-example")

## Google Calendar configuration properties

The following table provides information about configuration properties required in the
schema.

| Configuration                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                        | Required |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `connectionConfiguration`                | Configuration information for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `object`<br>This property has the following sub-property:<br>`repositoryEndpointMetadata`.                                                                                                                                                                                                                                                                                                  | Yes      |
| `repositoryEndpointMetadata`             | The endpoint information for the data source. This data source doesn't specify an<br>endpoint. You choose your authentication type: `serviceAccount` and<br>`OAuth2`. The connection information is included in an AWS Secrets Manager secret that you provide the `secretArn`.                                                                                                                                                                                                                                                                                              | `object`<br>This property has the following sub-property:<br>`authType`.                                                                                                                                                                                                                                                                                                                    | Yes      |
| `authType`                               | Choose between `serviceAccount` and `OAuth2`, based on your<br>use case.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `string`                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `repositoryConfigurations`               | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings.                                                                                                                                                                                                                                                                                                                                                                                                                                      | `object`<br>This property has the following sub-properties: `file` and<br>`comment`.                                                                                                                                                                                                                                                                                                        | Yes      |
| • 1) Calendar<br>• 2) Event              | A list of objects that map the attributes or field names of your Google<br>calendar to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `object`<br>`object`<br>These properties have the following sub-properties.<br>• `indexFieldName`<br>• `indexFieldType`<br>• `dataSourceFieldName`<br>• `dateFieldFormat`                                                                                                                                                                                                                   | No       |
| `indexFieldName`                         | The field name of your Google Drive to Amazon Q index<br>field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `indexFieldType`                         | The field type of your Google Drive to Amazon Q index<br>field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `string`<br>The allowed values are `STRING`, `STRING_LIST`, and<br>`DATE`.                                                                                                                                                                                                                                                                                                                  | Yes      |
| `dataSourceFieldName`                    | The data source field name of your Google Calendar to Amazon Q index field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `string`                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `dateFieldFormat`                        | The date format of your Google Calendar to Amazon Q index<br>field names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `string`<br>Specify the date format in the form `yyyy-MM-dd'T'HH:mm:ss'Z'`                                                                                                                                                                                                                                                                                                                  | No       |
| `additionalProperties`                   | Additional configuration options for your content in your data source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `object`<br>This property has the following sub-properties.<br>• `isCrawlAcl`<br>• `fielForUserId`<br>• `InclusionUserList`<br>• `exclusionUserList`<br>• `enableDeletionProtection`<br>• `DeletionProtectionThreshold`                                                                                                                                                                     | Yes      |
| `isCrawlAcl`                             | Specify `true` to crawl access control information by default from<br>documents. NoteAmazon Q Business crawls ACL information to ensure responses are generated<br>only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details.                                                                                                                                                                                                                   | `boolean`                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `fieldForUserId`                         | Specify field to use for `UserId` for ACL crawling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`                                                                                                                                                                                                                                                                                                                                                                                    | No       |
| `inclusionUsersList exclusionUsersLists` | A list of email IDs to exclude specific users from your Google<br>Calendardata source. Users whose email IDs match these will be excluded from<br>the index, while users whose email IDs do not match will be included. If a file<br>matches both an exclusion and an inclusion, the exclusion takes precedence, and the<br>file will not be included in the index.                                                                                                                                                                                                          | `array`                                                                                                                                                                                                                                                                                                                                                                                     | No       |
| • `type`                                 | The type of source. We recommend GOOGLECALENDAR as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `string`<br>Valid values are GOOGLECALENDAR.                                                                                                                                                                                                                                                                                                                                                | No       |
| • `enableIdentityCrawler`                | `true` to activate identity crawler. Identity crawler is activated by<br>default. Crawling identity information on users and groups with access to certain<br>documents is useful for user context filtering. Search results are filtered based on the<br>user or their group access to documents. NoteAmazon Q Business crawls ACL information to ensure responses are generated<br>only from documents your end users have access to. See [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization") for more details. | `boolean`                                                                                                                                                                                                                                                                                                                                                                                   | Yes      |
| • `syncMode`                             | Specify whether Amazon Q should update your index by syncing all<br>documents or only new, modified, and deleted documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `string`<br>You can choose between the following options: Use `FORCED FULL CRAWL`<br>to freshly re-crawl all content and replace existing content each time your data<br>source syncs with your indexUse.Use `FULL CRAWL` to incrementally crawl<br>only new, modified, and deleted content each time your data source syncs with your<br>index                                             | Yes      |
| • `SecretARN`                            | The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that<br>contains the key-value pairs required to connect to your Google Drive.<br>.                                                                                                                                                                                                                                                                                                                                                                                                                          | `string`<br>The secret must contain a JSON structure with the following keys:<br>If using Google Service Account authentication: `{"clientEmail": "user<br>account email","adminAccountEmail": "service account email","privateKey": "private<br>key"}If using OAuth 2.0 authentication:{"clientID": "OAuth client<br>ID","clientSecret": "client secret","refreshToken": "refresh token"}` | No       |
| • `version`                              | The version of this template that's currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `string`                                                                                                                                                                                                                                                                                                                                                                                    | No       |

## Google Calendar JSON schema

The following is the Google Calendar JSON schema:

```
{

{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "connectionConfiguration": {
      "type": "object",
      "properties": {
        "repositoryEndpointMetadata": {
          "type": "object",
          "properties": {
            "authType": {
              "type": "string",
              "enum": [
                "OAuth2",
                "serviceAccount"
              ]
            }
          },
          "required": [
            "authType"
          ]
        }
      },
      "required": [
        "repositoryEndpointMetadata"
      ]
    },
    "repositoryConfigurations": {
      "type": "object",
      "properties": {
        "calendar": {
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
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST",
                        "LONG"
                      ]
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
          }
        },
        "event": {
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
                      "enum": [
                        "STRING",
                        "DATE",
                        "STRING_LIST"
                      ]
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
          }
        }
      }
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "fieldForUserId": {
          "type": "string"
        },
        "isCrawlAcl": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "string",
              "enum": [
                "true",
                "false"
              ]
            }
          ]
        },
        "inclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "exclusionUsersList": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "enableDeletionProtection": {
          "type": "boolean",
          "default": false
        },
        "deletionProtectionThreshold": {
          "type": "string",
          "default": "15"
        }
      }
    },
    "enableIdentityCrawler": {
      "type": "boolean"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FULL_CRAWL",
        "FORCED_FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
    },
    "type": {
      "type": "string",
      "pattern": "GOOGLECALENDAR"
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
    "connectionConfiguration",
    "repositoryConfigurations",
    "syncMode",
    "additionalProperties",
    "secretArn",
    "type"
  ]
}


```

[Show moreShow less](# "#")

## Google Calendar JSON schema example

The following is the Google Calendar JSON schema example:

```
{

{
  "connectionConfiguration": {
    "repositoryEndpointMetadata": {
      "authType": "serviceAccount"
    }
  },
  "repositoryConfigurations": {
    "calendar": {
      "fieldMappings": [
        {
          "indexFieldName": "_category",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "category"
        },
        {
          "indexFieldName": "_source_uri",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "sourceUrl"
        }
      ]
    },
    "event": {
      "fieldMappings": [
        {
          "indexFieldName": "_category",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "category"
        },
        {
          "indexFieldName": "gcal_location",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "location"
        },
        {
          "indexFieldName": "_created_at",
          "indexFieldType": "DATE",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'",
          "dataSourceFieldName": "created"
        },
        {
          "indexFieldName": "_last_updated_at",
          "indexFieldType": "DATE",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'",
          "dataSourceFieldName": "updated"
        },
        {
          "indexFieldName": "gcal_event_start_time",
          "indexFieldType": "DATE",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'",
          "dataSourceFieldName": "eventStartTime"
        },
        {
          "indexFieldName": "gcal_event_end_time",
          "indexFieldType": "DATE",
          "dateFieldFormat": "yyyy-MM-dd'T'HH:mm:ss'Z'",
          "dataSourceFieldName": "eventEndTime"
        },
        {
          "indexFieldName": "_source_uri",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "htmlLink"
        },
        {
          "indexFieldName": "gcal_organizer",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "organizer"
        },
        {
          "indexFieldName": "gcal_attendees",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "attendees"
        },
        {
          "indexFieldName": "gcal_recurrence",
          "indexFieldType": "STRING",
          "dataSourceFieldName": "recurrence"
        }
      ]
    }
  },
  "additionalProperties": {
    "fieldForUserId": "email",
    "isCrawlAcl": true,
    "inclusionUsersList": [
      "ABC"
    ],
    "exclusionUsersList": [
      "TEST"
    ],
    "enableDeletionProtection": true,
    "deletionProtectionThreshold": "2"
  },
  "type": "GOOGLECALENDAR",
  "syncMode": "FORCED_FULL_CRAWL",
  "enableIdentityCrawler": true,
  "secretArn": "arn:aws::secretsmanager:us-west-2:123:secret:AmazonKendra-GoogleCalendar",
  "version": "1.0.0"
}

```

[Show moreShow less](# "#")
