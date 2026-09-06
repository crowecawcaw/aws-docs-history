

# Actions, resources, and condition keys for Database Query Metadata Service
<a name="list_dbqms"></a>

Database Query Metadata Service (service prefix: `dbqms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dbqms/dbqms.json) for this service.

**Topics**
+ [Actions defined by Database Query Metadata Service](#list_dbqms-actions-as-permissions)
+ [Resource types defined by Database Query Metadata Service](#list_dbqms-resources-for-iam-policies)
+ [Condition keys for Database Query Metadata Service](#list_dbqms-policy-keys)

## Actions defined by Database Query Metadata Service
<a name="list_dbqms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateFavoriteQuery](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#CreateFavoriteQuery)  | Grants permission to create a new favorite query |  |   | Write | 
|   [CreateQueryHistory](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#CreateQueryHistory)  | Grants permission to add a query to the history |  |   | Write | 
|   [CreateTab](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#CreateTab)  | Grants permission to create a new query tab |  |   | Write | 
|   [DeleteFavoriteQueries](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DeleteFavoriteQueries)  | Grants permission to delete saved queries |  |   | Write | 
|   [DeleteQueryHistory](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DeleteQueryHistory)  | Grants permission to delete a historical query |  |   | Write | 
|   [DeleteTab](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DeleteTab)  | Grants permission to delete query tab |  |   | Write | 
|   [DescribeFavoriteQueries](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DescribeFavoriteQueries)  | Grants permission to list saved queries and associated metadata |  |   | List | 
|   [DescribeQueryHistory](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DescribeQueryHistory)  | Grants permission to list history of queries that were run |  |   | List | 
|   [DescribeTabs](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#DescribeTabs)  | Grants permission to list query tabs and associated metadata |  |   | List | 
|   [GetQueryString](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#GetQueryString)  | Grants permission to retrieve favorite or history query string by id |  |   | Read | 
|   [UpdateFavoriteQuery](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#UpdateFavoriteQuery)  | Grants permission to update saved query and description |  |   | Write | 
|   [UpdateQueryHistory](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#UpdateQueryHistory)  | Grants permission to update the query history |  |   | Write | 
|   [UpdateTab](https://docs.aws.amazon.com/qldb/latest/developerguide/dbqms-api.html#UpdateTab)  | Grants permission to update query tab |  |   | Write | 

## Resource types defined by Database Query Metadata Service
<a name="list_dbqms-resources-for-iam-policies"></a>

Database Query Metadata Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Database Query Metadata Service
<a name="list_dbqms-policy-keys"></a>

Database Query Metadata Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.