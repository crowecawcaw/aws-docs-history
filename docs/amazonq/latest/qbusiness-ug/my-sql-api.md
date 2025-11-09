# Connecting Amazon Q Business to

MySQL using APIs

You use the [`CreateDataSource`](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data source to
your Amazon Q application.

Then, you use the `configuration` parameter to provide a JSON schema with all
other configuration information specific to your data source connector.

## MySQL JSON schema

The following is the MySQL JSON schema:

```
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
            "dbType": {
              "type": "string",
              "enum": [
                "mysql",
                "db2",
                "postgresql",
                "oracle",
                "sqlserver"
              ]
            },
            "dbHost": {
              "type": "string"
            },
            "dbPort": {
              "type": "string"
            },
            "dbInstance": {
              "type": "string"
            }
          },
          "required": [
            "dbType",
            "dbHost",
            "dbPort",
            "dbInstance"
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
                      "type": "string"
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
          "required": [
            "fieldMappings"
          ]
        }
      },
      "required": [
      ]
    },
    "additionalProperties": {
      "type": "object",
      "properties": {
        "primaryKey": {
          "type": "string"
        },
        "titleColumn": {
          "type": "string"
        },
        "bodyColumn": {
          "type": "string"
        },
        "sqlQuery": {
          "type": "string",
          "not": {
            "pattern": ";+"
          }
        },
        "timestampColumn": {
          "type": "string"
        },
        "timestampFormat": {
          "type": "string"
        },
        "timezone": {
          "type": "string"
        },
        "changeDetectingColumns": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "allowedUsersColumn": {
          "type": "string"
        },
        "allowedGroupsColumn": {
          "type": "string"
        },
        "sourceURIColumn": {
          "type": "string"
        },
        "serverlessAurora": {
          "type": "string",
          "enum": ["true", "false"]
        }
      },
      "required": ["primaryKey", "titleColumn", "bodyColumn", "sqlQuery"]
    },
    "type" : {
      "type" : "string",
      "pattern": "JDBC"
    },
    "syncMode": {
      "type": "string",
      "enum": [
        "FORCED_FULL_CRAWL",
        "FULL_CRAWL",
        "CHANGE_LOG"
      ]
    },
    "secretArn": {
      "type": "string",
      "minLength": 20,
      "maxLength": 2048
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
      "connectionConfiguration",
      "repositoryConfigurations",
      "syncMode",
      "additionalProperties",
      "secretArn",
      "type"
  ]
}
```

The following table provides information about important JSON keys to configure.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database you are using, whether<br>`mysql`, `db2`, `postgresql`,<br>`oracle`, or `sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                              |
| repositoryConfigurations   | Configuration information for the content of the data source. For example,<br>configuring specific types of content and field mappings. Specify the type of data<br>source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                        |
| document                   | A list of objects that map the attributes or field names of your database content<br>to Amazon Q index field names. For more information, see [Fiel](connector-concepts.md#connector-field-mappings "connector-concepts.md#connector-field-mappings").                                                                                                                                                                                                                                                                                                |
| additionalProperties       | Additional configuration options for your content in your data source. Use to<br>include or exclude specific content in your database data source.                                                                                                                                                                                                                                                                                                                                                                                                    |
| primaryKey                 | Provide the primary<br>key for the database table. This identifies the row in the table for which your SQL query is written. The<br>connector uses the primary key column value to identify rows, detect<br>changes, and crawl data.                                                                                                                                                                                                                                                                                                                  |
| titleColumn                | Provide the name of the<br>column in your database table that you want to designate as the column<br>with document titles.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| bodyColumn                 | Provide the name of the<br>column in your database table that you want to designate as the column<br>with document body text.<br>Your SQL query can include multiple columns in your table concatenated<br>into a single body column with an assigned alias.                                                                                                                                                                                                                                                                                          |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL queries must be<br>less than 1000 characters and not contain any semi-colons (;). Amazon Q will crawl all<br>database content that matches your query.                                                                                                                                                                                                                                                                                                                                |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Q uses time stamp<br>information to detect changes in your content and sync only changed content.                                                                                                                                                                                                                                                                                                                                                                                     |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use to detect<br>content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| timezone                   | Enter the name of the column which contains time zones for the content to be<br>crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| changeDetectingColumns     | Enter the names of the columns that Amazon Q will use to detect content changes.<br>Amazon Q will re-index content when there is a change in any of these columns                                                                                                                                                                                                                                                                                                                                                                                     |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed access to<br>content.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| isSslEnabled               | `true` to add a path to an SSL certificate file stored in an Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| type                       | The type of data source. Specify `JDBC` as your data source<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| syncMode                   | Specify whether Amazon Q should update your index by syncing all documents or only<br>new, modified, and deleted documents. You can choose<br>• `FORCED_FULL_CRAWL` to freshly re-crawl all content and replace<br>existing content each time your data source syncs with your index<br>• `FULL_CRAWL` to incrementally crawl only new, modified, and deleted<br>content each time your data source syncs with your index<br>• `CHANGE_LOG` to incrementally crawl only new and<br>modified content each time your data source syncs with your index. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains username and<br>password required to connect to your database. The secret must contain a JSON structure<br>with the following keys:<br>``<br>{<br>"username": "`database username`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                  |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
