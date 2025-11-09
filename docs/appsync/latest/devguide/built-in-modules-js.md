# Built-in modules

Modules are a part of the `APPSYNC_JS` runtime and provide utilities to help
write JavaScript resolvers and functions. For samples and examples, see the [aws-appsync-resolver-samples](https://github.com/aws-samples/aws-appsync-resolver-samples "https://github.com/aws-samples/aws-appsync-resolver-samples")
GitHub repository.

## DynamoDB module functions

DynamoDB module functions provide an enhanced experience when interacting with DynamoDB
data sources. You can make requests toward your DynamoDB data sources using the functions
and without adding type mapping.

Modules are imported using `@aws-appsync/utils/dynamodb`:

```
// Modules are imported using `@aws-appsync/utils/dynamodb`
import * as ddb from '@aws-appsync/utils/dynamodb';
```

### Functions

**`get<T>(payload: GetInput):
 DynamoDBGetItemRequest`**

###### Tip

See [Inputs](#built-in-ddb-modules-inputs "#built-in-ddb-modules-inputs") for
information about GetInput.

Generates a `DynamoDBGetItemRequest` object to make a
[GetItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-getitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-getitem") request to DynamoDB.

```
import { get } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	return get({ key: { id: ctx.args.id } });
}
```

**`put<T>(payload):
 DynamoDBPutItemRequest`**

Generates a `DynamoDBPutItemRequest` object to make a
[PutItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-putitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-putitem") request to DynamoDB.

```
import * as ddb from '@aws-appsync/utils/dynamodb'

export function request(ctx) {
	return ddb.put({ key: { id: util.autoId() }, item: ctx.args });
}
```

**`remove<T>(payload):
 DynamoDBDeleteItemRequest`**

Generates a `DynamoDBDeleteItemRequest` object to make a
[DeleteItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-deleteitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-deleteitem") request to DynamoDB.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	return ddb.remove({ key: { id: ctx.args.id } });
}
```

**`scan<T>(payload):
 DynamoDBScanRequest`**

Generates a `DynamoDBScanRequest` to make a [Scan](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-scan "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-scan") request to DynamoDB.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const { limit = 10, nextToken } = ctx.args;
	return ddb.scan({ limit, nextToken });
}
```

**`sync<T>(payload):
 DynamoDBSyncRequest`**

Generates a `DynamoDBSyncRequest` object to make a
[Sync](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-sync "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-sync") request. The request only receives the data altered
since the last query (delta updates). Requests can only be made to
versioned DynamoDB data sources.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const { limit = 10, nextToken, lastSync } = ctx.args;
	return ddb.sync({ limit, nextToken, lastSync });
}
```

**`update<T>(payload):
 DynamoDBUpdateItemRequest`**

Generates a `DynamoDBUpdateItemRequest` object to make
an [UpdateItem](js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-updateitem "js-resolver-reference-dynamodb.md#js-aws-appsync-resolver-reference-dynamodb-updateitem") request to DynamoDB.

### Operations

Operation helpers allow you to take specific actions on parts of your data during
updates. To get started, import `operations` from
`@aws-appsync/utils/dynamodb`:

```
// Modules are imported using operations
`import {operations} from '@aws-appsync/utils/dynamodb';`
```

**`add<T>(payload)`**

A helper function that adds a new attribute item when updating
DynamoDB.

**Example**

To add an address (street, city, and zip code) to an existing DynamoDB
item using the ID value:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const updateObj = {
		address: operations.add({
			street1: '123 Main St',
			city: 'New York',
			zip: '10001',
		}),
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`append
 <T>(payload)`**

A helper function that appends a payload to the existing list in
DynamoDB.

**Example**

To append newly added friend IDs (`newFriendIds`) to an
existing friends list (`friendsIds`) during an
update:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const newFriendIds = [101, 104, 111];
	const updateObj = {
		friendsIds: operations.append(newFriendIds),
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`decrement (by?)`**

A helper function that decrements the existing attribute value in
the item when updating DynamoDB.

**Example**

To decrement a friends counter (`friendsCount`) by
10:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const updateObj = {
		friendsCount: operations.decrement(10),
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`increment (by?)`**

A helper function that increments the existing attribute value in
the item when updating DynamoDB.

**Example**

To increment a friends counter (`friendsCount`) by
10:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const updateObj = {
		friendsCount: operations.increment(10),
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`prepend
 <T>(payload)`**

A helper function that prepends to the existing list in
DynamoDB.

**Example**

To prepend newly added friend IDs (`newFriendIds`) to an
existing friends list (`friendsIds`) during an
update:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const newFriendIds = [101, 104, 111];
	const updateObj = {
		friendsIds: operations.prepend(newFriendIds),
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`replace
 <T>(payload)`**

A helper function that replaces an existing attribute when updating
an item in DynamoDB. This is useful for when you want to update the
entire object or subobject in the attribute and not just the keys in
the payload.

**Example**

To replace an address (street, city, and zip code) in an
`info` object:

```
import { update, operations } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const updateObj = {
		info: {
			address: operations.replace({
				street1: '123 Main St',
				city: 'New York',
				zip: '10001',
			}),
		},
	};
	return update({ key: { id: 1 }, update: updateObj });
}
```

**`updateListItem <T>(payload,
 index)`**

A helper function that replaces an item in a list.

**Example**

In the scope of the update (`newFriendIds`), this
example used `updateListItem` to update the ID values of
the second item (index: `1`, new ID: `102`) and
third item (index: `2`, new ID: `112`) in a list
(`friendsIds`).

```
import { update, operations as ops } from '@aws-appsync/utils/dynamodb';

export function request(ctx) {
	const newFriendIds = [
		ops.updateListItem('102', 1), ops.updateListItem('112', 2)
	];
	const updateObj = { friendsIds: newFriendIds };
	return update({ key: { id: 1 }, update: updateObj });
}
```

### Inputs

**`Type GetInput<T>`**

```
GetInput<T>: {
    consistentRead?: boolean;
    key: DynamoDBKey<T>;
}
```

**Type Declaration**

- `consistentRead?: boolean` (optional)

An optional boolean to specify whether you want to perform a
strongly consistent read with DynamoDB.

- `key: DynamoDBKey<T>` (required)

A required parameter that specifies the key of the item in
DynamoDB. DynamoDB items may have a single hash key or hash and sort
keys.

**`Type
 PutInput<T>`**

```
PutInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T> | null;
    customPartitionKey?: string;
    item: Partial<T>;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
}
```

**Type Declaration**

- `_version?: number` (optional)
- `condition?: DynamoDBFilterObject<T> | null`
  (optional)

When you put an object in a DynamoDB table, you can optionally
specify a conditional expression that controls whether the
request should succeed or not based on the state of the object
already in DynamoDB before the operation is performed.

- `customPartitionKey?: string` (optional)

When enabled, this string value modifies the format of the
`ds_sk` and `ds_pk` records used by the
delta sync table when versioning has been enabled. When enabled,
the processing of the `populateIndexFields` entry is
also enabled.

- `item: Partial<T>` (required)

The rest of the attributes of the item to be placed into
DynamoDB.

- `key: DynamoDBKey<T>` (required)

A required parameter that specifies the key of the item in
DynamoDB on which the put will be performed. DynamoDB items may have a
single hash key or hash and sort keys.

- `populateIndexFields?: boolean` (optional)

A boolean value that, when enabled along with the
`customPartitionKey`, creates new entries for each
record in the delta sync table, specifically in the
`gsi_ds_pk` and `gsi_ds_sk` columns.
For more information, see [Conflict detection and sync](conflict-detection-and-sync.md "conflict-detection-and-sync.md") in the _AWS AppSync Developer Guide_.

**`Type
 QueryInput<T>`**

```
QueryInput<T>: ScanInput<T> & {
    query: DynamoDBKeyCondition<Required<T>>;
}
```

**Type Declaration**

- `query: DynamoDBKeyCondition<Required<T>>`
  (required)

Specifies a key condition that describes items to query. For
a given index, the condition for a partition key should be an
equality and the sort key a comparison or a
`beginsWith` (when it's a string). Only number and
string types are supported for partition and sort keys.

**Example**

Take the `User` type below:

```
type User = {
  id: string;
  name: string;
  age: number;
  isVerified: boolean;
  friendsIds: string[]
}
```

The query can only include the following fields:
`id`, `name`, and
`age`:

```
const query: QueryInput<User> = {
    name: { eq: 'John' },
    age: { gt: 20 },
}
```

**`Type
 RemoveInput<T>`**

```
RemoveInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T>;
    customPartitionKey?: string;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
}
```

**Type Declaration**

- `_version?: number` (optional)
- `condition?: DynamoDBFilterObject<T>`
  (optional)

When you remove an object in DynamoDB, you can optionally
specify a conditional expression that controls whether the
request should succeed or not based on the state of the object
already in DynamoDB before the operation is performed.

**Example**

The following example is a `DeleteItem` expression
containing a condition that allows the operation succeed only if
the owner of the document matches the user making the
request.

```
type Task = {
  id: string;
  title: string;
  description: string;
  owner: string;
  isComplete: boolean;
}
const condition: DynamoDBFilterObject<Task> = {
  owner: { eq: 'XXXXXXXXXXXXXXXX' },
}

remove<Task>({
   key: {
     id: 'XXXXXXXXXXXXXXXX',
  },
  condition,
});
```

- `customPartitionKey?: string` (optional)

When enabled, the `customPartitionKey` value
modifies the format of the `ds_sk` and
`ds_pk` records used by the delta sync table when
versioning has been enabled. When enabled, the processing of the
`populateIndexFields` entry is also enabled.

- `key: DynamoDBKey<T>` (required)

A required parameter that specifies the key of the item in
DynamoDB that is being removed. DynamoDB items may have a single hash
key or hash and sort keys.

**Example**

If a `User` only has the hash key with a user
`id`, then the key would look like this:

```
type User = {
	id: number
	name: string
	age: number
	isVerified: boolean
}
const key: DynamoDBKey<User> = {
	id: 1,
}
```

If the table user has a hash key (`id`) and sort
key (`name`), then the key would look like
this:

```
type User = {
	id: number
	name: string
	age: number
	isVerified: boolean
	friendsIds: string[]
}

const key: DynamoDBKey<User> = {
	id: 1,
	name: 'XXXXXXXXXX',
}
```

- `populateIndexFields?: boolean` (optional)

A boolean value that, when enabled along with the
`customPartitionKey`, creates new entries for each
record in the delta sync table, specifically in the
`gsi_ds_pk` and `gsi_ds_sk`
columns.

**`Type
 ScanInput<T>`**

```
ScanInput<T>: {
    consistentRead?: boolean | null;
    filter?: DynamoDBFilterObject<T> | null;
    index?: string | null;
    limit?: number | null;
    nextToken?: string | null;
    scanIndexForward?: boolean | null;
    segment?: number;
    select?: DynamoDBSelectAttributes;
    totalSegments?: number;
}
```

**Type Declaration**

- `consistentRead?: boolean | null`
  (optional)

An optional boolean to indicate consistent reads when
querying DynamoDB. The default value is `false`.

- `filter?: DynamoDBFilterObject<T> | null`
  (optional)

An optional filter to apply to the results after retrieving
it from the table.

- `index?: string | null` (optional)

An optional name of the index to scan.

- `limit?: number | null` (optional)

An optional max number of results to return.

- `nextToken?: string | null` (optional)

An optional pagination token to continue a previous query.
This would have been obtained from a previous query.

- `scanIndexForward?: boolean | null`
  (optional)

An optional boolean to indicate whether the query is
performed in ascending or descending order. By default, this
value is set to `true`.

- `segment?: number` (optional)
- `select?: DynamoDBSelectAttributes`
  (optional)

Attributes to return from DynamoDB. By default, the AWS AppSync DynamoDB
resolver only returns attributes that are projected into the
index. The supported values are:

    + `ALL_ATTRIBUTES`


    Returns all the item attributes from the specified
     table or index. If you query a local secondary index,
     DynamoDB fetches the entire item from the parent table for
     each matching item in the index. If the index is
     configured to project all item attributes, all of the data
     can be obtained from the local secondary index and no
     fetching is required.
    + `ALL_PROJECTED_ATTRIBUTES`


    Returns all attributes that have been projected into
     the index. If the index is configured to project all
     attributes, this return value is equivalent to specifying
     `ALL_ATTRIBUTES`.
    + `SPECIFIC_ATTRIBUTES`


    Returns only the attributes listed in
     `ProjectionExpression`. This return value is
     equivalent to specifying `ProjectionExpression`
     without specifying any value for
     `AttributesToGet`.

- `totalSegments?: number` (optional)

**`Type
 DynamoDBSyncInput<T>`**

```
DynamoDBSyncInput<T>: {
    basePartitionKey?: string;
    deltaIndexName?: string;
    filter?: DynamoDBFilterObject<T> | null;
    lastSync?: number;
    limit?: number | null;
    nextToken?: string | null;
}
```

**Type Declaration**

- `basePartitionKey?: string` (optional)

The partition key of the base table to be used when
performing a Sync operation. This field allows a Sync operation
to be performed when the table utilizes a custom partition
key.

- `deltaIndexName?: string` (optional)

The index used for the Sync operation. This index is required
to enable a Sync operation on the whole delta store table when
the table uses a custom partition key. The Sync operation will
be performed on the GSI (created on `gsi_ds_pk` and
`gsi_ds_sk`).

- `filter?: DynamoDBFilterObject<T> | null`
  (optional)

An optional filter to apply to the results after retrieving
it from the table.

- `lastSync?: number` (optional)

The moment, in epoch milliseconds, at which the last
successful Sync operation started. If specified, only items that
have changed after `lastSync` are returned. This
field should only be populated after retrieving all pages from
an initial Sync operation. If omitted, results from the base
table will be returned. Otherwise, results from the delta table
will be returned.

- `limit?: number | null` (optional)

An optional maximum number of items to evaluate at a single
time. If omitted, the default limit will be set to
`100` items. The maximum value for this field is
`1000` items.

- `nextToken?: string | null` (optional)

**`Type
 DynamoDBUpdateInput<T>`**

```
DynamoDBUpdateInput<T>: {
    _version?: number;
    condition?: DynamoDBFilterObject<T>;
    customPartitionKey?: string;
    key: DynamoDBKey<T>;
    populateIndexFields?: boolean;
    update: DynamoDBUpdateObject<T>;
}
```

**Type Declaration**

- `_version?: number` (optional)
- `condition?: DynamoDBFilterObject<T>`
  (optional)

When you update an object in DynamoDB, you can optionally
specify a conditional expression that controls whether the
request should succeed or not based on the state of the object
already in DynamoDB before the operation is performed.

- `customPartitionKey?: string` (optional)

When enabled, the `customPartitionKey` value
modifies the format of the `ds_sk` and
`ds_pk` records used by the delta sync table when
versioning has been enabled. When enabled, the processing of the
`populateIndexFields` entry is also enabled.

- `key: DynamoDBKey<T>` (required)

A required parameter that specifies the key of the item in
DynamoDB that is being updated. DynamoDB items may have a single hash
key or hash and sort keys.

- `populateIndexFields?: boolean` (optional)

A boolean value that, when enabled along with the
`customPartitionKey`, creates new entries for each
record in the delta sync table, specifically in the
`gsi_ds_pk` and `gsi_ds_sk` columns.

- `update: DynamoDBUpdateObject<T>`

An object that specifies the attributes to be updated along
with the new values for them. The update object can be used with
`add`, `remove`, `replace`,
`increment`, `decrement`,
`append`, `prepend`,
`updateListItem`.

## Amazon RDS module functions

Amazon RDS module functions provide an enhanced experience when interacting with databases
configured with the Amazon RDS Data API. The module is imported using
`@aws-appsync/utils/rds`:

```
import * as rds from '@aws-appsync/utils/rds';
```

Functions can also be imported individually. For instance, the import below uses
`sql`:

```
import { sql } from '@aws-appsync/utils/rds';
```

### Functions

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

You can specify columns with the `columns` property. If this
isn't set to a value, it defaults to `*`:

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

You can apply `limit` and `offset` to the
query:

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
| --------------- | -------------------------------- | ----------------------- |
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
| size            | checks the length of the element | string                  |

The `insert` utility provides a straightforward way of inserting
single row items in your database with the `INSERT`
operation.

**Single item insertions**

To insert an item, specify the table and then pass in your object of values.
The object keys are mapped to your table columns. Columns names are
automatically escaped, and values are sent to the database using the variable
map:

```
import { insert, createMySQLStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({ table: 'persons', values });

    // Generates statement:
    // INSERT INTO `persons`(`name`)
    // VALUES(:NAME)
    return createMySQLStatement(insertStatement)
}
```

**MySQL use case**

You can combine an `insert` followed by a `select` to
retrieve your inserted row:

```
import { insert, select, createMySQLStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({  table: 'persons', values });
    const selectStatement = select({
        table: 'persons',
        columns: '*',
        where: { id: { eq: values.id } },
        limit: 1,
    });

    // Generates statement:
    // INSERT INTO `persons`(`name`)
    // VALUES(:NAME)
    // and
    // SELECT *
    // FROM `persons`
    // WHERE `id` = :ID
    return createMySQLStatement(insertStatement, selectStatement)
}
```

**Postgres use case**

With Postgres, you can use [`returning`](https://www.postgresql.org/docs/current/dml-returning.html "https://www.postgresql.org/docs/current/dml-returning.html") to obtain data from the row that you
inserted. It accepts `*` or an array of column names:

```
import { insert, createPgStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input: values } = ctx.args;
    const insertStatement = insert({
        table: 'persons',
        values,
        returning: '*'
    });

    // Generates statement:
    // INSERT INTO "persons"("name")
    // VALUES(:NAME)
    // RETURNING *
    return createPgStatement(insertStatement)
}
```

The `update` utility allows you to update existing rows. You can
use the condition object to apply changes to the specified columns in all the
rows that satisfy the condition. For example, let's say we have a schema that
allows us to make this mutation. We want to update the `name` of
`Person` with the `id` value of `3` but
only if we've known them (`known_since`) since the year
`2000`:

```
mutation Update {
    updatePerson(
        input: {id: 3, name: "Jon"},
        condition: {known_since: {ge: "2000"}}
    ) {
    id
    name
  }
}
```

Our update resolver looks like this:

```
import { update, createPgStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input: { id, ...values }, condition } = ctx.args;
    const where = {
        ...condition,
        id: { eq: id },
    };
    const updateStatement = update({
        table: 'persons',
        values,
        where,
        returning: ['id', 'name'],
    });

    // Generates statement:
    // UPDATE "persons"
    // SET "name" = :NAME, "birthday" = :BDAY, "country" = :COUNTRY
    // WHERE "id" = :ID
    // RETURNING "id", "name"
    return createPgStatement(updateStatement)
}
```

We can add a check to our condition to make sure that only the row that has
the primary key `id` equal to `3` is updated. Similarly,
for Postgres `inserts`, you can use `returning` to return
the modified data.

The `remove` utility allows you to delete existing rows. You can
use the condition object on all rows that satisfy the condition. Note that
`delete` is a reserved keyword in JavaScript. `remove`
should be used instead:

```
import { remove, createPgStatement } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const { input: { id }, condition } = ctx.args;
    const where = { ...condition, id: { eq: id } };
    const deleteStatement = remove({
        table: 'persons',
        where,
        returning: ['id', 'name'],
    });

    // Generates statement:
    // DELETE "persons"
    // WHERE "id" = :ID
    // RETURNING "id", "name"
    return createPgStatement(updateStatement)
}
```

### Casting

In some cases, you may want more specificity about the correct object type to use
in your statement. You can use the provided type hints to specify the type of your
parameters. AWS AppSync supports the [same type hints](../../../rdsdataservice/latest/APIReference/API_SqlParameter.md#rdsdtataservice-Type-SqlParameter-typeHint "../../../rdsdataservice/latest/APIReference/API_SqlParameter.md#rdsdtataservice-Type-SqlParameter-typeHint") as the Data API. You can cast your parameters by using
the `typeHint` functions from the AWS AppSync `rds` module.

The following example allows you to send an array as a value that is casted as a
JSON object. We use the `->` operator to retrieve the element at the
`index`
`2` in the JSON array:

```
import { sql, createPgStatement, toJsonObject, typeHint } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const arr = ctx.args.list_of_ids
    const statement = sql`select ${typeHint.JSON(arr)}->2 as value`
    return createPgStatement(statement)
}

export function response(ctx) {
    return toJsonObject(ctx.result)[0][0].value
}
```

Casting is also useful when handling and comparing `DATE`,
`TIME`, and `TIMESTAMP`:

```
import { select, createPgStatement, typeHint } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const when = ctx.args.when
    const statement = select({
        table: 'persons',
        where: { createdAt : { gt: typeHint.DATETIME(when) } }
    })
    return createPgStatement(statement)
}
```

Here's another example showing how you can send the current date and time:

```
import { sql, createPgStatement, typeHint } from '@aws-appsync/utils/rds';

export function request(ctx) {
    const now = util.time.nowFormatted('YYYY-MM-dd HH:mm:ss')
    return createPgStatement(sql`select ${typeHint.TIMESTAMP(now)}`)
}
```

**Available type hints**

- `typeHint.DATE` - The corresponding parameter is sent as an
  object of the `DATE` type to the database. The accepted format is
  `YYYY-MM-DD`.
- `typeHint.DECIMAL` - The corresponding parameter is sent as an
  object of the `DECIMAL` type to the database.
- `typeHint.JSON` - The corresponding parameter is sent as an
  object of the `JSON` type to the database.
- `typeHint.TIME` - The corresponding string parameter value is
  sent as an object of the `TIME` type to the database. The accepted
  format is `HH:MM:SS[.FFF]`.
- `typeHint.TIMESTAMP` - The corresponding string parameter value
  is sent as an object of the `TIMESTAMP` type to the database. The
  accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]`.
- `typeHint.UUID` - The corresponding string parameter value is
  sent as an object of the `UUID` type to the database.
