# Using Aurora PostgreSQL with Data API in

AWS AppSync

Learn how to connect your GraphQL API to Aurora PostgreSQL databases using AWS AppSync.
This integration enables you to build scalable, data-driven applications by executing SQL
queries and mutations through GraphQL operations. AWS AppSync provides a data source for
executing SQL statements against Amazon Aurora clusters that are enabled with a Data API.
You can use AWS AppSync resolvers to run SQL statements against the data API with GraphQL
queries, mutations, and subscriptions.

Before starting this tutorial, you should have basic familiarity with AWS services
and GraphQL concepts.

###### Note

This tutorial uses the `US-EAST-1` Region.

###### Topics

- [Set up your Aurora PostgreSQL database](#creating-clusters "#creating-clusters")
- [Creating the database and table](#creating-db-table "#creating-db-table")
- [Creating a GraphQL schema](#rds-graphql-schema "#rds-graphql-schema")
- [Resolvers for RDS](#rds-resolvers "#rds-resolvers")
- [Deleting your cluster](#rds-delete-cluster "#rds-delete-cluster")

## Set up your Aurora PostgreSQL database

Before adding an Amazon RDS data source to AWS AppSync, do the following.

1. Enable a Data API on an Aurora Serverless v2 cluster.
2. Configure a secret using AWS Secrets Manager
3. Create the cluster using the following AWS CLI command.

```
aws rds create-db-cluster \
            --db-cluster-identifier appsync-tutorial \
            --engine aurora-postgresql \
            --engine-version 16.6 \
            --serverless-v2-scaling-configuration MinCapacity=0,MaxCapacity=1 \
            --master-username USERNAME \
            --master-user-password COMPLEX_PASSWORD \
            --enable-http-endpoint
```

This will return an ARN for the cluster. After creating a cluster,
you must add a Serverless v2 instance with the following AWS CLI command.

```
aws rds create-db-instance \
    --db-cluster-identifier appsync-tutorial \
    --db-instance-identifier appsync-tutorial-instance-1 \
    --db-instance-class db.serverless \
    --engine aurora-postgresql
```

###### Note

These endpoints take time to become activate. You can check their status in
the RDS console in the **Connectivity & security**
tab for the cluster.

Check the cluster status with the following AWS CLI command.

```
aws rds describe-db-clusters \
    --db-cluster-identifier appsync-tutorial \
    --query "DBClusters[0].Status"
```

Create a Secret via the AWS Secrets Manager Console or the AWS CLI with an input file such as the
following using the `USERNAME` and `COMPLEX_PASSWORD` from the
previous step:

```
{
    "username": "USERNAME",
    "password": "COMPLEX_PASSWORD"
}
```

Pass this as a parameter to the AWS CLI:

```
aws secretsmanager create-secret \
    --name appsync-tutorial-rds-secret \
    --secret-string file://creds.json
```

This will return an ARN for the secret. **Take note** of
the ARN of your Aurora Serverless v2 cluster and Secret for later when creating a data
source in the AWS AppSync console.

## Creating the database and table

First, create a database named `TESTDB`. In PostgreSQL, a database is a
container that holds tables and other SQL objects. Validate that your Aurora
Serverless v2 cluster is configured correctly before adding it to your AWS AppSync
API. First, create a _TESTDB_ database with
the `--sql` parameter as follows.

```
aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:111122223333 ISN:cluster:appsync-tutorial" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:111122223333 ISN:secret:appsync-tutorial-rds-secret" \
    --sql "create DATABASE \"testdb\"" \
    --database "postgres"
```

If this runs without any errors, add two tables with the `create table`
command:

```
 aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:111122223333 ISN:cluster:appsync-tutorial" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:111122223333 ISN:secret:appsync-tutorial-rds-secret" \
    --database "testdb" \
    --sql 'create table public.todos (id serial constraint todos_pk primary key, description text not null, due date not null, "createdAt" timestamp default now());'

aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:111122223333 ISN:cluster:appsync-tutorial" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:111122223333 ISN:secret:appsync-tutorial-rds-secret" \
    --database "testdb" \
    --sql 'create table public.tasks (id serial constraint tasks_pk primary key, description varchar, "todoId" integer not null constraint tasks_todos_id_fk references public.todos);'
```

If successful, add the cluster as a data source in your API.

## Creating a GraphQL schema

Now that your Aurora Serverless v2 Data API is running with configured tables, we'll
create a GraphQL schema. You can quickly create your API by importing table configurations
from an existing database using the API creation wizard.

To begin:

1. In the AWS AppSync console, choose **Create API**,
   then **Start with an Amazon Aurora cluster**.
2. Specify API details like **API name**, then
   select your database to generate the API.
3. Choose your database. If needed, update the Region, then choose your Aurora
   cluster and _TESTDB_ database.
4. Choose your Secret, then choose **Import**.
5. Once tables have been discovered, update the type names. Change
   `Todos` to `Todo` and `Tasks` to
   `Task`.
6. Preview the generated schema by choosing **Preview
   Schema**. Your schema will look something like this:

```
type Todo {
  id: Int!
  description: String!
  due: AWSDate!
  createdAt: String
}

type Task {
  id: Int!
  todoId: Int!
  description: String
}
```

7. For the role, you can either have AWS AppSync create a new role or create one with
   a policy similar to the one below:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "rds-data:ExecuteStatement"
 ],
 "Resource": [
 "arn:aws:rds:us-east-1:111122223333:cluster:appsync-tutorial",
 "arn:aws:rds:us-east-1:111122223333:cluster:appsync-tutorial:*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:appsync-tutorial-rds-secret",
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:appsync-tutorial-rds-secret:*"
 ]
 }
 ]
}`

```

Note that there are two statements in this policy to which you are granting
role access. The first resource is your Aurora cluster and the second is your
AWS Secrets Manager ARN.

Choose **Next**, review the configuration
details, then choose **Create API**. You now have a
fully operational API. You can review the full details of your API on the
**Schema** page.

## Resolvers for RDS

The API creation flow automatically created the resolvers to interact with our types.
If you look at **Schema** page, you will find resolvers
some of the follwoing resolvers.

- Create a `todo` via the `Mutation.createTodo`
  field.
- Update a `todo` via the `Mutation.updateTodo`
  field.
- Delete a `todo` via the `Mutation.deleteTodo`
  field.
- Get a single `todo` via the `Query.getTodo`
  field.
- List all `todos` via the `Query.listTodos` field.

You will find similar fields and resolvers attached for the `Task` type.
Let's take a closer look at some of the resolvers.

### Mutation.createTodo

From the schema editor in the AWS AppSync console, on the right side, choose
`testdb` next to `createTodo(...): Todo`. The resolver
code uses the `insert` function from the `rds` module to dynamically create an insert
statement that adds data to the `todos` table. Because we are working with Postgres,
we can leverage the `returning` statement to get the inserted data back.

Update the following resolver to properly specify the `DATE` type of the
`due` field.

```
import { util } from '@aws-appsync/utils';
import { insert, createPgStatement, toJsonObject, typeHint } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input } = ctx.args;
    // if a due date is provided, cast is as `DATE`
    if (input.due) {
        input.due = typeHint.DATE(input.due)
    }
    const insertStatement = insert({
        table: 'todos',
        values: input,
        returning: '*',
    });
    return createPgStatement(insertStatement)
}

export function response(ctx) {
    const { error, result } = ctx;
    if (error) {
        return util.appendError(
            error.message,
            error.type,
            result
        )
    }
    return toJsonObject(result)[0][0]
}
```

Save the resolver. The type hint marks the `due` properly in our input
object as a `DATE` type. This allows the Postgres engine to properly
interpret the value. Next, update your schema to remove the `id` from the
`CreateTodo` input. Because our Postgres database can return the
generated ID, you can rely on it for creation and returning the result as a single
request as follows.

```
input CreateTodoInput {
    due: AWSDate!
    createdAt: String
    description: String!
}
```

Make the change and update your schema. Head to the **Queries** editor to add an item to the database as follows.

```
mutation CreateTodo {
  createTodo(input: {description: "Hello World!", due: "2023-12-31"}) {
    id
    due
    description
    createdAt
  }
}
```

You get the following result.

```
{
  "data": {
    "createTodo": {
      "id": 1,
      "due": "2023-12-31",
      "description": "Hello World!",
      "createdAt": "2023-11-14 20:47:11.875428"
    }
  }
}
```

### Query.listTodos

From the schema editor in the console, on the right side, choose
`testdb` next to `listTodos(id: ID!): Todo`. The request
handler uses the select utility function to build a request dynamically at run
time.

```
export function request(ctx) {
    const { filter = {}, limit = 100, nextToken } = ctx.args;
    const offset = nextToken ? +util.base64Decode(nextToken) : 0;
    const statement = select({
        table: 'todos',
        columns: '*',
        limit,
        offset,
        where: filter,
    });
    return createPgStatement(statement)
}
```

We want to filter `todos` based on the `due` date. Let's
update the resolver to cast `due` values to `DATE`. Update the
list of imports and the request handler as follows.

```
import { util } from '@aws-appsync/utils';
import * as rds from '@aws-appsync/utils/rds';

export function request(ctx) {
  const { filter: where = {}, limit = 100, nextToken } = ctx.args;
  const offset = nextToken ? +util.base64Decode(nextToken) : 0;

  // if `due` is used in a filter, CAST the values to DATE.
  if (where.due) {
    Object.entries(where.due).forEach(([k, v]) => {
      if (k === 'between') {
        where.due[k] = v.map((d) => rds.typeHint.DATE(d));
      } else {
        where.due[k] = rds.typeHint.DATE(v);
      }
    });
  }

  const statement = rds.select({
    table: 'todos',
    columns: '*',
    limit,
    offset,
    where,
  });
  return rds.createPgStatement(statement);
}

export function response(ctx) {
  const {
    args: { limit = 100, nextToken },
    error,
    result,
  } = ctx;
  if (error) {
    return util.appendError(error.message, error.type, result);
  }
  const offset = nextToken ? +util.base64Decode(nextToken) : 0;
  const items = rds.toJsonObject(result)[0];
  const endOfResults = items?.length < limit;
  const token = endOfResults ? null : util.base64Encode(`${offset + limit}`);
  return { items, nextToken: token };
}
```

In the **Queries** editor do the following.

```
query LIST {
  listTodos(limit: 10, filter: {due: {between: ["2021-01-01", "2025-01-02"]}}) {
    items {
      id
      due
      description
    }
  }
}
```

### Mutation.updateTodo

You can also `update` a `Todo`. From the **Queries** editor, let's update our first `Todo`
item of `id`
`1`.

```
mutation UPDATE {
  updateTodo(input: {id: 1, description: "edits"}) {
    description
    due
    id
  }
}
```

Note that you must specify the `id` of the item you are updating. You
can also specify a condition to only update an item that meets specific conditions.
For example, we may only want to edit the item if the description starts with
`edits` as follows.

```
mutation UPDATE {
  updateTodo(input: {id: 1, description: "edits: make a change"}, condition: {description: {beginsWith: "edits"}}) {
    description
    due
    id
  }
}
```

Just like how we handled our `create` and `list` operations,
we can update our resolver to cast the `due` field to a
`DATE`. Save these changes to `updateTodo` as follows.

```
import { util } from '@aws-appsync/utils';
import * as rds from '@aws-appsync/utils/rds';

export function request(ctx) {
  const { input: { id, ...values }, condition = {}, } = ctx.args;
  const where = { ...condition, id: { eq: id } };

  // if `due` is used in a condition, CAST the values to DATE.
  if (condition.due) {
    Object.entries(condition.due).forEach(([k, v]) => {
      if (k === 'between') {
        condition.due[k] = v.map((d) => rds.typeHint.DATE(d));
      } else {
        condition.due[k] = rds.typeHint.DATE(v);
      }
    });
  }

  // if a due date is provided, cast is as `DATE`
  if (values.due) {
    values.due = rds.typeHint.DATE(values.due);
  }

  const updateStatement = rds.update({
    table: 'todos',
    values,
    where,
    returning: '*',
  });
  return rds.createPgStatement(updateStatement);
}

export function response(ctx) {
  const { error, result } = ctx;
  if (error) {
    return util.appendError(error.message, error.type, result);
  }
  return rds.toJsonObject(result)[0][0];
}
```

Now try an update with a condition:

```
mutation UPDATE {
  updateTodo(
    input: {
        id: 1, description: "edits: make a change", due: "2023-12-12"},
    condition: {
        description: {beginsWith: "edits"}, due: {ge: "2023-11-08"}})
    {
          description
          due
          id
        }
}
```

### Mutation.deleteTodo

You can `delete` a `Todo` with the `deleteTodo`
mutation. This works like the `updateTodo` mutation, and you must specify
the `id` of the item you want to delete as follows.

```
mutation DELETE {
  deleteTodo(input: {id: 1}) {
    description
    due
    id
  }
}
```

### Writing custom queries

We've used the `rds` module utilities to create our SQL statements. We
can also write our own custom static statement to interact with our database. First,
update the schema to remove the `id` field from the
`CreateTask` input.

```
input CreateTaskInput {
    todoId: Int!
    description: String
}
```

Next, create a couple of tasks. A task has a foreign key relationship with
`Todo`as follows.

```
mutation TASKS {
  a: createTask(input: {todoId: 2, description: "my first sub task"}) { id }
  b:createTask(input: {todoId: 2, description: "another sub task"}) { id }
  c: createTask(input: {todoId: 2, description: "a final sub task"}) { id }
}
```

Create a new field in your `Query` type called
`getTodoAndTasks`as follows.

```
getTodoAndTasks(id: Int!): Todo
```

Add a `tasks` field to the `Todo` type as follows.

```
type Todo {
    due: AWSDate!
    id: Int!
    createdAt: String
    description: String!
    tasks:TaskConnection
}
```

Save the schema. From the schema editor in the console, on the right side, choose
**Attach Resolver** for `getTodosAndTasks(id:
 Int!): Todo`. Choose your Amazon RDS data source. Update your resolver with the
following code.

```
import { sql, createPgStatement,toJsonObject } from '@aws-appsync/utils/rds';

export function request(ctx) {
    return createPgStatement(
        sql`SELECT * from todos where id = ${ctx.args.id}`,
        sql`SELECT * from tasks where "todoId" = ${ctx.args.id}`);
}

export function response(ctx) {
    const result = toJsonObject(ctx.result);
    const todo = result[0][0];
    if (!todo) {
        return null;
    }
    todo.tasks = { items: result[1] };
    return todo;
}
```

In this code, we use the `sql` tag template to write a SQL statement
that we can safely pass a dynamic value to at run time.
`createPgStatement` can take up to two SQL requests at a time. We use
that to send one query for our `todo` and another for our
`tasks`. You could have done this with a `JOIN` statement
or any other method for that matter. The idea is being able to write your own SQL
statement to implement your business logic. To use the query in the **Queries** editor, do the following.

```
query TodoAndTasks {
  getTodosAndTasks(id: 2) {
    id
    due
    description
    tasks {
      items {
        id
        description
      }
    }
  }
}
```

## Deleting your cluster

###### Important

Deleting a cluster is permanent. Review your project thoroughly before carrying
out this action.

To delete your cluster:

```
$ aws rds delete-db-cluster \
    --db-cluster-identifier appsync-tutorial \
    --skip-final-snapshot
```
