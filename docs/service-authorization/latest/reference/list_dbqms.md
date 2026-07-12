# Actions, resources, and condition keys for Database Query Metadata Service

Database Query Metadata Service (service prefix: `dbqms`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../qldb/latest/developerguide/dbqms-api.md "../../../qldb/latest/developerguide/dbqms-api.md").
- View a list of the [API operations available for
  this service](../../../qldb/latest/developerguide/dbqms-api.md "../../../qldb/latest/developerguide/dbqms-api.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../qldb/latest/developerguide/dbqms-api.md "../../../qldb/latest/developerguide/dbqms-api.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/dbqms/dbqms.json "https://servicereference.us-east-1.amazonaws.com/v1/dbqms/dbqms.json") for this service.

###### Topics

- [Actions defined by Database Query Metadata Service](#list_dbqms-actions-as-permissions "#list_dbqms-actions-as-permissions")
- [Resource types defined by Database Query Metadata Service](#list_dbqms-resources-for-iam-policies "#list_dbqms-resources-for-iam-policies")
- [Condition keys for Database Query Metadata Service](#list_dbqms-policy-keys "#list_dbqms-policy-keys")

## Actions defined by Database Query Metadata Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                        | Description                                                          | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateFavoriteQuery](../../../qldb/latest/developerguide/dbqms-api.md#CreateFavoriteQuery "../../../qldb/latest/developerguide/dbqms-api.md#CreateFavoriteQuery")             | Grants permission to create a new favorite query                     |                             |                | Write        |
| [CreateQueryHistory](../../../qldb/latest/developerguide/dbqms-api.md#CreateQueryHistory "../../../qldb/latest/developerguide/dbqms-api.md#CreateQueryHistory")                | Grants permission to add a query to the history                      |                             |                | Write        |
| [CreateTab](../../../qldb/latest/developerguide/dbqms-api.md#CreateTab "../../../qldb/latest/developerguide/dbqms-api.md#CreateTab")                                           | Grants permission to create a new query tab                          |                             |                | Write        |
| [DeleteFavoriteQueries](../../../qldb/latest/developerguide/dbqms-api.md#DeleteFavoriteQueries "../../../qldb/latest/developerguide/dbqms-api.md#DeleteFavoriteQueries")       | Grants permission to delete saved queries                            |                             |                | Write        |
| [DeleteQueryHistory](../../../qldb/latest/developerguide/dbqms-api.md#DeleteQueryHistory "../../../qldb/latest/developerguide/dbqms-api.md#DeleteQueryHistory")                | Grants permission to delete a historical query                       |                             |                | Write        |
| [DeleteTab](../../../qldb/latest/developerguide/dbqms-api.md#DeleteTab "../../../qldb/latest/developerguide/dbqms-api.md#DeleteTab")                                           | Grants permission to delete query tab                                |                             |                | Write        |
| [DescribeFavoriteQueries](../../../qldb/latest/developerguide/dbqms-api.md#DescribeFavoriteQueries "../../../qldb/latest/developerguide/dbqms-api.md#DescribeFavoriteQueries") | Grants permission to list saved queries and associated metadata      |                             |                | List         |
| [DescribeQueryHistory](../../../qldb/latest/developerguide/dbqms-api.md#DescribeQueryHistory "../../../qldb/latest/developerguide/dbqms-api.md#DescribeQueryHistory")          | Grants permission to list history of queries that were run           |                             |                | List         |
| [DescribeTabs](../../../qldb/latest/developerguide/dbqms-api.md#DescribeTabs "../../../qldb/latest/developerguide/dbqms-api.md#DescribeTabs")                                  | Grants permission to list query tabs and associated metadata         |                             |                | List         |
| [GetQueryString](../../../qldb/latest/developerguide/dbqms-api.md#GetQueryString "../../../qldb/latest/developerguide/dbqms-api.md#GetQueryString")                            | Grants permission to retrieve favorite or history query string by id |                             |                | Read         |
| [UpdateFavoriteQuery](../../../qldb/latest/developerguide/dbqms-api.md#UpdateFavoriteQuery "../../../qldb/latest/developerguide/dbqms-api.md#UpdateFavoriteQuery")             | Grants permission to update saved query and description              |                             |                | Write        |
| [UpdateQueryHistory](../../../qldb/latest/developerguide/dbqms-api.md#UpdateQueryHistory "../../../qldb/latest/developerguide/dbqms-api.md#UpdateQueryHistory")                | Grants permission to update the query history                        |                             |                | Write        |
| [UpdateTab](../../../qldb/latest/developerguide/dbqms-api.md#UpdateTab "../../../qldb/latest/developerguide/dbqms-api.md#UpdateTab")                                           | Grants permission to update query tab                                |                             |                | Write        |

## Resource types defined by Database Query Metadata Service

Database Query Metadata Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Database Query Metadata Service

Database Query Metadata Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
