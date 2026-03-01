# Connecting to Microsoft SQL Server using APIs

You use the [`CreateDataSource`](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") action to connect a data
source to your Amazon Q application.

Then, you use the `configuration` parameter to provide a JSON schema with
all other configuration information specific to your data source connector.

## Microsoft SQL Server JSON schema

The following is the Microsoft SQL Server JSON schema:

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
        "FULL_CRAWL"
      ]
    },
    "secretArn": {
      "type": "string"
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

[Show moreShow less](# "#")
The following table provides information about important JSON keys to
configure.

| Configuration              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectionConfiguration    | Configuration information for the endpoint for the data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| repositoryEndpointMetadata | Required configuration information for connecting your data source.<br>• dbType—The type of Java database you are using,<br>whether `mysql`, `db2`,<br>`postgresql`, `oracle`, or<br>`sqlserver`.<br>• dbHost—The database host name.<br>• dbPort—The database port.<br>• dbInstance—The database instance.                                                                                                                                                                                                                                                       |
| repositoryConfigurations   | Configuration information for the content of the data source. For<br>example, configuring specific types of content and field mappings.<br>Specify the type of data source and the secret ARN.                                                                                                                                                                                                                                                                                                                                                                    |
| document                   | A list of objects that map the attributes or field names of your<br>database content to Amazon Q index field names. For more<br>information, see [Mapping data source<br>fields](../../../kendra/latest/dg/field-mapping.md "../../../kendra/latest/dg/field-mapping.md").                                                                                                                                                                                                                                                                                        |
| additionalProperties       | Additional configuration options for your content in your data<br>source. Use to include or exclude specific content in your database data<br>source.                                                                                                                                                                                                                                                                                                                                                                                                             |
| primaryKey                 | Provide the primary key for the database table. This identifies a<br>table within your database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| titleColumn                | Provide the name of the document title column within your database<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| bodyColumn                 | Provide the name of the document title column within your database<br>table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| sqlQuery                   | Enter SQL query statements like SELECT and JOIN operations. SQL<br>queries must be less than 1000 characters and not contain any<br>semi-colons (;). Amazon Q will crawl all database content<br>that matches your query. If a table name has special characters, put it<br>in square brackets "[ ]" in the SQL query. For example: `select *<br>from [my-database-table]`.                                                                                                                                                                                       |
| timestampColumn            | Enter the name of the column which contains time stamps. Amazon Q uses time stamp information to detect changes in your<br>content and sync only changed content.                                                                                                                                                                                                                                                                                                                                                                                                 |
| timestampFormat            | Enter the name of the column which contains time stamp formats to use<br>to detect content changes and re-sync your content.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| timezone                   | Enter the name of the column which contains time zones for the<br>content to be crawled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| changeDetectingColumns     | Enter the names of the columns that Amazon Q will use to<br>detect content changes. Amazon Q will re-index content when<br>there is a change in any of these columns                                                                                                                                                                                                                                                                                                                                                                                              |
| allowedUsersColumns        | Enter the name of the column which contains User IDs to be allowed<br>access to content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| allowedGroupsColumn        | Enter the name of the column which contains User IDs to be allowed<br>access to content.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| sourceURIColumn            | Enter the name of the column which contains Source URLs to be<br>indexed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| isSslEnabled               | `true` to add a path to an SSL certificate file stored in<br>an Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| type                       | The type of data source. Specify `JDBC` as your data<br>source type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| syncMode                   | Specify whether Amazon Q should update your index by<br>syncing all documents or only new, modified, and deleted documents. You<br>can choose<br>• `FORCED_FULL_CRAWL` to freshly re-crawl all<br>content and replace existing content each time your data<br>source syncs with your index<br>• `FULL_CRAWL` to incrementally crawl only new,<br>modified, and deleted content each time your data source<br>syncs with your index<br>• `CHANGE_LOG` to incrementally<br>crawl only new and modified content each time your data<br>source syncs with your index. |
| secretArn                  | The Amazon Resource Name (ARN) of a Secrets Manager secret that contains user<br>name and password required to connect to your database. The secret must<br>contain a JSON structure with the following keys:<br>``<br>{<br>"username": "`database username`",<br>"password": "`password`"<br>}<br>``                                                                                                                                                                                                                                                             |
| version                    | The version of the template that is currently supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
