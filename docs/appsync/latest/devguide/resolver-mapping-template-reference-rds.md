# AWS AppSync resolver

mapping template reference for RDS

The AWS AppSync RDS resolver mapping templates allow developers to send SQL queries to a
Data API for Amazon Aurora Serverless and get back the result of these queries.

## Request mapping template

The RDS request mapping template is fairly simple:

```
{
    "version": "2018-05-29",
    "statements": [],
    "variableMap": {},
    "variableTypeHintMap": {}
}
```

Here is the JSON schema representation of the RDS request mapping template, once
resolved.

```
{
    "definitions": {},
    "$schema": "https://json-schema.org/draft-07/schema#",
    "$id": "https://example.com/root.json",
    "type": "object",
    "title": "The Root Schema",
    "required": [
        "version",
        "statements",
        "variableMap"
    ],
    "properties": {
        "version": {
            "$id": "#/properties/version",
            "type": "string",
            "title": "The Version Schema",
            "default": "",
            "examples": [
                "2018-05-29"
            ],
            "enum": [
                "2018-05-29"
            ],
            "pattern": "^(.*)$"
        },
        "statements": {
            "$id": "#/properties/statements",
            "type": "array",
            "title": "The Statements Schema",
            "items": {
                "$id": "#/properties/statements/items",
                "type": "string",
                "title": "The Items Schema",
                "default": "",
                "examples": [
                    "SELECT * from BOOKS"
                ],
                "pattern": "^(.*)$"
            }
        },
        "variableMap": {
            "$id": "#/properties/variableMap",
            "type": "object",
            "title": "The Variablemap Schema"
        },
        "variableTypeHintMap": {
            "$id": "#/properties/variableTypeHintMap",
            "type": "object",
            "title": "The variableTypeHintMap Schema"
        }
    }
}
```

The following is an example of the request mapping template with a static query:

```
{
    "version": "2018-05-29",
    "statements": [
        "select title, isbn13 from BOOKS where author = 'Mark Twain'"
    ]
}
```

## Version

Common to all request mapping templates, the version field defines the version that the template
uses. The version field is required. The value “2018-05-29” is the only version supported for the Amazon
RDS mapping templates.

```
"version": "2018-05-29"
```

## Statements and VariableMap

The statements array is a placeholder for the developer-provided queries. Currently, up to two queries per
request mapping template are supported. The `variableMap` is an optional field that contains
aliases that can be used to make the SQL statements shorter and more readable. For example, the following is
possible:

```
{
"version": "2018-05-29",
    "statements": [
        "insert into BOOKS VALUES (:AUTHOR, :TITLE, :ISBN13)",
        "select * from BOOKS WHERE isbn13 = :ISBN13"
    ],
    "variableMap": {
        ":AUTHOR": $util.toJson($ctx.args.newBook.author),
        ":TITLE": $util.toJson($ctx.args.newBook.title),
        ":ISBN13": $util.toJson($ctx.args.newBook.isbn13)
    }
}
```

AWS AppSync will use the variable map values to construct the **[SqlParameterized](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md")** queries that will be sent to the Amazon Aurora Serverless Data
API. The SQL statements are executed with parameters provided in the variable map, which eliminates the risk
of SQL injection.

## VariableTypeHintMap

The `variableTypeHintMap` is an optional field containing aliased types that can be used to
send [SQL
parameter](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md") type hints. These type hints avoid explicit casting in the SQL statements, making them
shorter. For example, the following is possible:

```
{
    "version": "2018-05-29",
    "statements": [
        "insert into LOGINDATA VALUES (:ID, :TIME)",
        "select * from LOGINDATA WHERE id = :ID"
     ],
     "variableMap": {
        ":ID": $util.toJson($ctx.args.id),
        ":TIME": $util.toJson($ctx.args.time)
     },
     "variableTypeHintMap": {
        ":id": "UUID",
        ":time": "TIME"
     }
}
```

AWS AppSync will use the variable map value to construct the queries that are sent to the Amazon Aurora
Serverless Data API. It also uses the `variableTypeHintMap` data and sends the type's information
to RDS. RDS-supported `typeHints` can be found [here](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md").
