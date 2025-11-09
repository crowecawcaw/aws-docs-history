# Building GraphQL APIs with RDS introspection

AWS AppSync's introspection utility can discover models from database tables and propose GraphQL
types. The AWS AppSync console's Create API wizard can instantly generate an API from an Aurora
MySQL or PostgreSQL database. It automatically creates types and JavaScript resolvers to read
and write data.

AWS AppSync provides direct integration with Amazon Aurora databases through the Amazon RDS Data
API. Rather than requiring a persistent database connection, the Amazon RDS Data API offers a
secure HTTP endpoint that AWS AppSync connects to for running SQL statements. You
can use this to create a relational database API for your MySQL and PostgreSQL workloads on
Aurora.

Building an API for your relational database with AWS AppSync has several advantages:

- Your database is not directly exposed to clients, decoupling the access point from
  the database itself.
- You can build purpose-built APIs tailored to the needs of different applications,
  removing the need for custom business logic in frontends. This aligns with the
  Backend-For-Frontend (BFF) pattern.
- Authorization and access control can be implemented at the AWS AppSync layer using various
  authorization modes to control access. No additional compute resources are required to
  connect to the database, such as hosting a web server or proxying connections.
- Real-time capabilities can be added via subscriptions, with data mutations made
  through AppSync automatically pushed to connected clients.
- Clients can connect to the API over HTTPS using common ports like 443.
  AWS AppSync makes building APIs from existing relational databases easy. Its introspection
  utility can discover models from database tables and propose GraphQL types. The AWS AppSync
  console's _Create API_ wizard can instantly generate an API
  from an Aurora MySQL or PostgreSQL database. It automatically creates types and JavaScript
  resolvers to read and write data.

AWS AppSync provides integrated JavaScript utilities to simplify writing SQL statements in
resolvers. You can use AWS AppSync's `sql` tag templates for static statements with
dynamic values, or the `rds` module utilities to build statements programmatically.
See the [resolver function reference
for RDS](resolver-reference-rds-js.md "resolver-reference-rds-js.md") data sources and [built-in
modules](built-in-modules-js.md#built-in-rds-modules "built-in-modules-js.md#built-in-rds-modules") for more.

## Using the introspection feature

(console)

For a detailed tutorial and getting started guide, see [Tutorial: Aurora
PostgreSQL Serverless with Data API](aurora-serverless-tutorial-js.md "aurora-serverless-tutorial-js.md").

The AWS AppSync console allows you to create an AWS AppSync GraphQL API from your existing Aurora
database configured with the Data API in just a few minutes. This quickly generates an
operational schema based on your database configuration. You can use the API as-is or build
on it to add features.

1. Sign in to the AWS Management Console and open the [AppSync
   console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   1. In the **Dashboard**, choose **Create API**.

2. Under **API options**, choose **GraphQL APIs**, **Start with an Amazon Aurora
   cluster**, then **Next**.
   1. Enter an **API name**. This will be used as an
      identifier for the API in the console.
   2. For **contact details**, you can enter a point
      of contact to identify a manager for the API. This is an optional field.
   3. Under **Private API configuration**, you can
      enable private API features. A private API can only be accessed from a
      configured VPC endpoint (VPCE). For more information, see [Private APIs](using-private-apis.md "using-private-apis.md").

   We don't recommend enabling this feature for this example. Choose **Next** after reviewing your inputs.

3. In the **Database** page, choose **Select database**.
   1. You need to choose your database from your cluster. The first step is to
      choose the **Region** in which your cluster
      exists.
   2. Choose the **Aurora cluster** from the drop-down
      list. Note that you must have created and [enabled](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md#data-api.enabling "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md#data-api.enabling") a corresponding data API before using the resource.
   3. Next, you must add the credentials for your database to the service. This is
      primarily done using AWS Secrets Manager. Choose the **Region** in which your secret exists. For more
      information on how to retrieve secret information, see [Find
      secrets](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") or [Retrieve
      secrets](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md").
   4. Add your secret from the drop-down list. Note that the user must have [read permissions](../../../AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console "../../../AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console") for your database.

4. Choose **Import**.

AWS AppSync will start introspecting your database, discovering tables, columns,
primary keys, and indexes. It checks that the discovered tables can be supported in a
GraphQL API. Note that to support creating new rows, tables need a primary key, which
can use multiple columns. AWS AppSync maps table columns to type fields as follows:

| Data type  | Field type |
| ---------- | ---------- |
| VARCHAR    | String     |
| CHAR       | String     |
| BINARY     | String     |
| VARBINARY  | String     |
| TINYBLOB   | String     |
| TINYTEXT   | String     |
| TEXT       | String     |
| BLOB       | String     |
| MEDIUMTEXT | String     |
| MEDIUMBLOB | String     |
| LONGTEXT   | String     |
| LONGBLOB   | String     |
| BOOL       | Boolean    |
| BOOLEAN    | Boolean    |
| BIT        | Int        |
| TINYINT    | Int        |
| SMALLINT   | Int        |
| MEDIUMINT  | Int        |
| INT        | Int        |
| INTEGER    | Int        |
| BIGINT     | Int        |
| YEAR       | Int        |
| FLOAT      | Float      |
| DOUBLE     | Float      |
| DECIMAL    | Float      |
| DEC        | Float      |
| NUMERIC    | Float      |
| DATE       | AWSDate    |
| TIMESTAMP  | String     |
| DATETIME   | String     |
| TIME       | AWSTime    |
| JSON       | AWSJson    |
| ENUM       | ENUM       |

5. Once table discovery is complete, the **Database**
   section will be populated with your information. In the new **Database tables** section, the data from the table may already be
   populated and converted to a type for your schema. If you don't see some of the
   required data, you can check for it by choosing **Add
   tables**, clicking on the checkboxes for those types in the modal that
   appears, then choosing **Add**.

To remove a type from the **Database tables**
section, click on the checkbox next to the type you want to remove, then choose
**Remove**. The removed types will be placed in the
**Add tables** modal if you want to add them again
later.

Note that AWS AppSync uses the table names as type names, but you can rename them - for
example, changing a plural table name like `movies` to the
type name `Movie`. To rename a type in the **Database tables** section, click on the checkbox of the type
you want to rename, then click on the _pencil_ icon
in the **Type name** column.

To preview the content of the schema based on your selections, choose **Preview schema**. Note that this schema cannot be empty, so
you'll have to have at least one table converted to a type. Also, this schema cannot
exceed 1 MB in size.

    1. Under **Service role**, choose whether to
     create a new service role specifically for this import or use an existing
     role.

6. Choose **Next**.
7. Next, choose whether to create a read-only API (queries only) or an API for
   reading and writing data (with queries and mutations). The latter also supports
   real-time subscriptions triggered by mutations.
8. Choose **Next**.
9. Review your choices and then choose **Create API**.
   AWS AppSync will create the API and attach resolvers to queries and mutations. The
   generated API is fully operational and can be extended as needed.

## Using the introspection feature (API)

You can use the `StartDataSourceIntrospection` introspection API to discover
models in your database programmatically. For more details on the command, see using the
[`StartDataSourceIntrospection`](../APIReference/API_StartDataSourceIntrospection.md "../APIReference/API_StartDataSourceIntrospection.md") API.

To use `StartDataSourceIntrospection`, provide your Aurora cluster Amazon
Resource Name (ARN), database name, and AWS Secrets Manager secret ARN. The
command starts the introspection process. You can retrieve the results with the
`GetDataSourceIntrospection` command. You can specify whether the command
should return the Storage Definition Language (SDL) string for the discovered models. This
is useful for generating an SDL schema definition directly from the discovered
models.

For example, if you have the following Data definition language (DDL) statement for a
simple `Todos` table:

```
create table if not exists public.todos
(
id serial constraint todos_pk primary key,
description text,
due timestamp,
"createdAt" timestamp default now()
);
```

You start the introspection with the following.

```
aws appsync start-data-source-introspection \
  --rds-data-api-config resourceArn=<cluster-arn>,secretArn=<secret-arn>,databaseName=database
```

Next, use the `GetDataSourceIntrospection` command to retrieve the
result.

```
aws appsync get-data-source-introspection \
  --introspection-id a1234567-8910-abcd-efgh-identifier \
  --include-models-sdl

```

This returns the following result.

```
{
    "introspectionId": "a1234567-8910-abcd-efgh-identifier",
    "introspectionStatus": "SUCCESS",
    "introspectionStatusDetail": null,
    "introspectionResult": {
        "models": [
            {
                "name": "todos",
                "fields": [
                    {
                        "name": "description",
                        "type": {
                            "kind": "Scalar",
                            "name": "String",
                            "type": null,
                            "values": null
                        },
                        "length": 0
                    },
                    {
                        "name": "due",
                        "type": {
                            "kind": "Scalar",
                            "name": "AWSDateTime",
                            "type": null,
                            "values": null
                        },
                        "length": 0
                    },
                    {
                        "name": "id",
                        "type": {
                            "kind": "NonNull",
                            "name": null,
                            "type": {
                                "kind": "Scalar",
                                "name": "Int",
                                "type": null,
                                "values": null
                            },
                            "values": null
                        },
                        "length": 0
                    },
                    {
                        "name": "createdAt",
                        "type": {
                            "kind": "Scalar",
                            "name": "AWSDateTime",
                            "type": null,
                            "values": null
                        },
                        "length": 0
                    }
                ],
                "primaryKey": {
                    "name": "PRIMARY_KEY",
                    "fields": [
                        "id"
                    ]
                },
                "indexes": [],
                "sdl": "type todos\n{\ndescription: String\n\ndue: AWSDateTime\n\nid: Int!\n\ncreatedAt: AW
SDateTime\n}\n"
            }
        ],
        "nextToken": null
    }
}
```
