# AWS AppSync JavaScript resolver function

reference for Amazon RDS

The AWS AppSync RDS function and resolver allows developers to send SQL queries
to an Amazon Aurora cluster database using the RDS Data API and get back the result of these
queries. You can write SQL statements that are sent to the Data API by using
AWS AppSync's `rds` module `sql`-tagged template or by using the
`rds` module's `select`, `insert`, `update`,
and `remove` helper functions. AWS AppSync utilizes the RDS Data Service's [`ExecuteStatement`](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md") action to run SQL statements against the
database.

###### Topics

- [SQL tagged template](#sql-tagged-templates "#sql-tagged-templates")
- [Creating statements](#creating-statements "#creating-statements")
- [Retrieving data](#retrieving-data "#retrieving-data")
- [Utility functions](#utility-functions "#utility-functions")
- [SQL Select](#utility-functions-select "#utility-functions-select")
- [SQL Insert](#utility-functions-insert "#utility-functions-insert")
- [SQL Update](#utility-functions-update "#utility-functions-update")
- [SQL Delete](#utility-functions-delete "#utility-functions-delete")
- [Casting](#casting "#casting")

## SQL tagged template

AWS AppSync's `sql` tagged template enables you to create a static statement
that can receive dynamic values at runtime by using template expressions. AWS AppSync builds
a variable map from the expression values to construct a [`SqlParameterized`](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md") query that is sent to the Amazon Aurora
Serverless Data API. With this method, it isn't possible for dynamic values passed at
run time to modify the original statement, which could cause unintented execution. All
dynamic values are passed as parameters, can't modify the original statement, and aren't
executed by the database. This makes your query less vulnerable to SQL
injection attacks.

###### Note

In all cases, when writing SQL statements, you should follow
security guidelines to properly handle data that you receive as input.

###### Note

The `sql` tagged template only supports passing variable values. You
can't use an expression to dynamically specify the column or table names. However,
you can use utility functions to build dynamic statements.

In the following example, we create a query that filters based on the value of the
`col` argument that is set dynamically in the GraphQL query at run time.
The value can only be added to the statement using the tag expression:

```
import { sql, createMySQLStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
  const query = sql`
SELECT * FROM table
WHERE column = ${ctx.args.col}`
  ;
  return createMySQLStatement(query);
}
```

By passing all dynamic values through the variable map, we rely on the database engine
to securely handle and sanitize values.

## Creating statements

Functions and resolvers can interact with MySQL and PostgreSQL databases. Use
`createMySQLStatement` and `createPgStatement` respectively to
build statements. For example, `createMySQLStatement` can create a MySQL
query. These functions accept up to two statements, useful when a request should
retrieve results immediately. With MySQL, you could do:

```
import { sql, createMySQLStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { id, text } = ctx.args;
    const s1 = sql`insert into Post(id, text) values(${id}, ${text})`;
    const s2 = sql`select * from Post where id = ${id}`;
    return createMySQLStatement(s1, s2);
}
```

###### Note

`createPgStatement` and `createMySQLStatement` does not
escape or quote statements built with the `sql` tagged template.

## Retrieving data

The result of your executed SQL statement is available in your response handler in the
`context.result` object. The result is a JSON string with the [response elements](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md#API_ExecuteStatement_ResponseElements "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md#API_ExecuteStatement_ResponseElements") from the `ExecuteStatement` action. When
parsed, the result has the following shape:

```
type SQLStatementResults = {
    sqlStatementResults: {
        records: any[];
        columnMetadata: any[];
        numberOfRecordsUpdated: number;
        generatedFields?: any[]
    }[]
}
```

You can use the `toJsonObject` utility to transform the result into a list
of JSON objects representing the returned rows. For example:

```
import { toJsonObject } from '@aws-appsync/utils/rds';

export function response(ctx) {
    const { error, result } = ctx;
    if (error) {
        return util.appendError(
            error.message,
            error.type,
            result
        )
    }
    return toJsonObject(result)[1][0]
}
```

Note that `toJsonObject` returns an array of statement results. If you
provided one statement, the array length is `1`. If you provided two
statements, the array length is `2`. Each result in the array contains
`0` or more rows. `toJsonObject` returns `null` if
the result value is invalid or unexpected.

## Utility functions

You can use the AWS AppSync RDS module's utility helpers to interact with your
database.

The `select` utility creates a `SELECT` statement to
query your relational database.

**Basic use**

In its basic form, you can specify the table you want to query:

```
import { select, createPgStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {

    // Generates statement:
    // "SELECT * FROM "persons"
    return createPgStatement(select({table: 'persons'}));
}
```

Note that you can also specify the schema in your table identifier:

```
import { select, createPgStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {

    // Generates statement:
    // SELECT * FROM "private"."persons"
    return createPgStatement(select({table: 'private.persons'}));
}
```

**Specifying columns**

You can specify columns with the `columns` property. If this isn't
set to a value, it defaults to `*`:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name']
    }));
}
```

You can specify a column's table as well:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "persons"."name"
    // FROM "persons"
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'persons.name']
    }));
}
```

**Limits and offsets**

You can apply `limit` and `offset` to the query:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // LIMIT :limit
    // OFFSET :offset
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        limit: 10,
        offset: 40
    }));
}
```

**Order By**

You can sort your results with the `orderBy` property. Provide an
array of objects specifying the column and an optional `dir`
property:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name" FROM "persons"
    // ORDER BY "name", "id" DESC
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        orderBy: [{column: 'name'}, {column: 'id', dir: 'DESC'}]
    }));
}
```

**Filters**

You can build filters by using the special condition object:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: {name: {eq: 'Stephane'}}
    }));
}
```

You can also combine filters:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME and "id" > :ID
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: {name: {eq: 'Stephane'}, id: {gt: 10}}
    }));
}
```

You can also create `OR` statements:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE "name" = :NAME OR "id" > :ID
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: { or: [
            { name: { eq: 'Stephane'} },
            { id: { gt: 10 } }
        ]}
    }));
}
```

You can also negate a condition with `not`:

```
export function request(ctx) {

    // Generates statement:
    // SELECT "id", "name"
    // FROM "persons"
    // WHERE NOT ("name" = :NAME AND "id" > :ID)
    return createPgStatement(select({
        table: 'persons',
        columns: ['id', 'name'],
        where: { not: [
            { name: { eq: 'Stephane'} },
            { id: { gt: 10 } }
        ]}
    }));
}
```

You can also use the following operators to compare values:

| Operator        | Description                      | Possible value types    |
| --------------- | -------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eq              | Equal                            | number, string, boolean |
| ne              | Not equal                        | number, string, boolean |
| le              | Less than or equal               | number, string          |
| lt              | Less than                        | number, string          |
| ge              | Greater than or equal            | number, string          |
| gt              | Greater than                     | number, string          |
| contains        | Like                             | string                  |
| notContains     | Not like                         | string                  |
| beginsWith      | Starts with prefix               | string                  |
| between         | Between two values               | number, string          |
| attributeExists | The attribute is not null        | number, string, boolean |
| size            | checks the length of the element | string                  | The `insert` utility provides a straightforward way of inserting single row items in your database with the `INSERT` operation. **Single item insertions** To insert an item, specify the table and then pass in your object of values. The object keys are mapped to your table columns. Columns names are automatically escaped, and values are sent to the database using the variable map: ``import { insert, createMySQLStatement } from '@aws-appsync/utils/rds'; export function request(ctx) { const { input: values } = ctx.args; const insertStatement = insert({ table: 'persons', values }); // Generates statement: // INSERT INTO `persons`(`name`) // VALUES(:NAME) return createMySQLStatement(insertStatement) }`` **MySQL use case** You can combine an `insert` followed by a `select` to retrieve your inserted row: ``import { insert, select, createMySQLStatement } from '@aws-appsync/utils/rds'; export function request(ctx) { const { input: values } = ctx.args; const insertStatement = insert({  table: 'persons', values }); const selectStatement = select({ table: 'persons', columns: '*', where: { id: { eq: values.id } }, limit: 1, }); // Generates statement: // INSERT INTO `persons`(`name`) // VALUES(:NAME) // and // SELECT * // FROM `persons` // WHERE `id` = :ID return createMySQLStatement(insertStatement, selectStatement) }`` **Postgres use case** With Postgres, you can use [`returning`](https://www.postgresql.org/docs/current/dml-returning.html "https://www.postgresql.org/docs/current/dml-returning.html") to obtain data from the row that you inserted. It accepts `*` or an array of column names: `import { insert, createPgStatement } from '@aws-appsync/utils/rds'; export function request(ctx) { const { input: values } = ctx.args; const insertStatement = insert({ table: 'persons', values, returning: '*' }); // Generates statement: // INSERT INTO "persons"("name") // VALUES(:NAME) // RETURNING * return createPgStatement(insertStatement) }` The `update` utility allows you to update existing rows. You can use the condition object to apply changes to the specified columns in all the rows that satisfy the condition. For example, let's say we have a schema that allows us to make this mutation. We want to update the `name` of `Person` with the `id` value of `3` but only if we've known them (`known_since`) since the year `2000`: `mutation Update { updatePerson( input: {id: 3, name: "Jon"}, condition: {known_since: {ge: "2000"}} ) { id name } }` Our update resolver looks like this: `import { update, createPgStatement } from '@aws-appsync/utils/rds'; export function request(ctx) { const { input: { id, ...values }, condition } = ctx.args; const where = { ...condition, id: { eq: id }, }; const updateStatement = update({ table: 'persons', values, where, returning: ['id', 'name'], }); // Generates statement: // UPDATE "persons" // SET "name" = :NAME, "birthday" = :BDAY, "country" = :COUNTRY // WHERE "id" = :ID // RETURNING "id", "name" return createPgStatement(updateStatement) }` We can add a check to our condition to make sure that only the row that has the primary key `id` equal to `3` is updated. Similarly, for Postgres `inserts`, you can use `returning` to return the modified data. The `remove` utility allows you to delete existing rows. You can use the condition object on all rows that satisfy the condition. Note that `delete` is a reserved keyword in JavaScript. `remove` should be used instead: `import { remove, createPgStatement } from '@aws-appsync/utils/rds'; export function request(ctx) { const { input: { id }, condition } = ctx.args; const where = { ...condition, id: { eq: id } }; const deleteStatement = remove({ table: 'persons', where, returning: ['id', 'name'], }); // Generates statement: // DELETE "persons" // WHERE "id" = :ID // RETURNING "id", "name" return createPgStatement(updateStatement) }` ## Casting In some cases, you may want more specificity about the correct object type to use in your statement. You can use the provided type hints to specify the type of your parameters. AWS AppSync supports the [same type hints](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md#rdsdtataservice-Type-SqlParameter-typeHint "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md#rdsdtataservice-Type-SqlParameter-typeHint") as the Data API. You can cast your parameters by using the `typeHint` functions from the AWS AppSync `rds` module. The following example allows you to send an array as a value that is casted as a JSON object. We use the `->` operator to retrieve the element at the `index` `2` in the JSON array: ``import { sql, createPgStatement, toJsonObject, typeHint } from '@aws-appsync/utils/rds'; export function request(ctx) { const arr = ctx.args.list_of_ids const statement = sql`select ${typeHint.JSON(arr)}->2 as value` return createPgStatement(statement) } export function response(ctx) { return toJsonObject(ctx.result)[0][0].value }`` Casting is also useful when handling and comparing `DATE`, `TIME`, and `TIMESTAMP`: `import { select, createPgStatement, typeHint } from '@aws-appsync/utils/rds'; export function request(ctx) { const when = ctx.args.when const statement = select({ table: 'persons', where: { createdAt : { gt: typeHint.DATETIME(when) } } }) return createPgStatement(statement) }` Here's another example showing how you can send the current date and time: ``import { sql, createPgStatement, typeHint } from '@aws-appsync/utils/rds'; export function request(ctx) { const now = util.time.nowFormatted('YYYY-MM-dd HH:mm:ss') return createPgStatement(sql`select ${typeHint.TIMESTAMP(now)}`) }`` **Available type hints** <br>• `typeHint.DATE` - The corresponding parameter is sent as an object of the `DATE` type to the database. The accepted format is `YYYY-MM-DD`. <br>• `typeHint.DECIMAL` - The corresponding parameter is sent as an object of the `DECIMAL` type to the database. <br>• `typeHint.JSON` - The corresponding parameter is sent as an object of the `JSON` type to the database. <br>• `typeHint.TIME` - The corresponding string parameter value is sent as an object of the `TIME` type to the database. The accepted format is `HH:MM:SS[.FFF]`. <br>• `typeHint.TIMESTAMP` - The corresponding string parameter value is sent as an object of the `TIMESTAMP` type to the database. The accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]`. <br>• `typeHint.UUID` - The corresponding string parameter value is sent as an object of the `UUID` type to the database. |
