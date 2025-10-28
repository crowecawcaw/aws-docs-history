# Versioning DynamoDB data sources in AWS AppSync

AWS AppSync currently supports versioning on DynamoDB data sources. Conflict Detection,
Conflict Resolution, and Sync operations require a `Versioned` data source. When
you enable versioning on a data source, AWS AppSync will automatically:

- Enhance items with object versioning metadata.
- Record changes made to items with AWS AppSync mutations to a _Delta_ table.
- Maintain deleted items in the _Base_
  table with a “tombstone” for a configurable amount of time.

## Versioned data source

configuration

When you enable versioning on a DynamoDB data source, you specify the following
fields:

**`BaseTableTTL`**

The number of minutes to retain deleted items in the _Base_ table with a “tombstone” - a metadata
field indicating that the item has been deleted. You can set this value to
_0_ if you want items to be
removed immediately when they are deleted. This field is required.

**`DeltaSyncTableName`**

The name of the table where changes made to items with AWS AppSync mutations
are stored. This field is required.

**`DeltaSyncTableTTL`**

The number of minutes to retain items in the _Delta_ table. This field is
required.

## Delta sync table logging

AWS AppSync currently supports Delta Sync Logging for mutations using
`PutItem`, `UpdateItem`, and `DeleteItem` DynamoDB
operations.

When an AWS AppSync mutation changes an item in a versioned data source, a record of
that change will be stored in a _Delta_ table
that is optimized for incremental updates. You can choose to use different _Delta_ tables (e.g. one per type, one per domain
area) for other versioned data sources or a single _Delta_ table for your API. AWS AppSync recommends against using a single
_Delta_ table for multiple APIs to avoid
the collision of primary keys.

The schema required for this table is as follows:

**`ds_pk`**

A string value that is used as the partition key. It is constructed by
concatenating the _Base_ data source
name and the ISO 8601 format of the date the change occurred (e.g.
`Comments:2019-01-01`).

When the `customPartitionKey` flag from the VTL mapping template
is set as the column name of the partition key (see [Resolver Mapping Template Reference for DynamoDB](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem") in the
_AWS AppSync Developer Guide_), the format of `ds_pk`
changes, and the string is constructed by appending it the value of the
partition key in the new record in the _Base_ table. For
example, if the record in the _Base_ table has a partition
key value of `1a` and a sort key value of `2b`, the new
value of the string will be: `Comments:2019-01-01:1a`.

**`ds_sk`**

A string value that is used as the sort key. It is constructed by
concatenating the ISO 8601 format of the time the change occurred, the primary
key of the item, and the version of the item. The combination of these fields
guarantees uniqueness for every entry in the _Delta_ table
(e.g. for a time of `09:30:00` and an ID of `1a` and
version of `2`, this would be `09:30:00:1a:2`).

When the `customPartitionKey` flag from the VTL mapping template
is set to the column name of the partition key (see [Resolver Mapping Template Reference for DynamoDB](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem") in the
_AWS AppSync Developer Guide_), the format of `ds_sk`
changes, and the string is constructed by replacing the value of the
combination key with the value of the sort key in the _Base_
table. Using the previous example above, if the record in the
_Base_ table has a partition key value of `1a`
and a sort key value of `2b`, the new value of the string will be:
`09:30:00:2b:3`.

**`_ttl`**

A numeric value that stores the timestamp, in epoch seconds, when an item
should be removed from the _Delta_
table. This value is determined by adding the `DeltaSyncTableTTL`
value configured on the data source to the moment when the change occurred.
This field should be configured as the DynamoDB TTL Attribute.

The IAM role configured for use with the _Base_ table must also contain permission to operate on the _Delta_ table. In this example, the permissions
policy for a _Base_ table called
`Comments` and a _Delta_ table
called `ChangeLog` is displayed:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:DeleteItem",
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:Query",
 "dynamodb:Scan",
 "dynamodb:UpdateItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:us-east-1:000000000000:table/Comments",
 "arn:aws:dynamodb:us-east-1:000000000000:table/Comments/*",
 "arn:aws:dynamodb:us-east-1:000000000000:table/ChangeLog",
 "arn:aws:dynamodb:us-east-1:000000000000:table/ChangeLog/*"
 ]
 }
 ]
}`

```

## Versioned data source metadata

AWS AppSync manages metadata fields on `Versioned` data sources on your
behalf. Modifying these fields yourself may cause errors in your application or data
loss. These fields include:

**`_version`**

A monotonically increasing counter that is updated any time that a change
occurs to an item.

**`_lastChangedAt`**

A numeric value that stores the timestamp, in epoch milliseconds, when an
item was last modified.

**`_deleted`**

A Boolean “tombstone” value that indicates that an item has been deleted.
This can be used by applications to evict deleted items from local data
stores.

**`_ttl`**

A numeric value that stores the timestamp, in epoch seconds, when an item
should be removed from the underlying data source.

**`ds_pk`**

A string value that is used as the partition key for _Delta_ tables.

**`ds_sk`**

A string value that is used as the sort key for _Delta_ tables.

**`gsi_ds_pk`**

A string value attribute that's generated to support a global secondary
index as a partition key. It will be included only if both the
`customPartitionKey` and `populateIndexFields` flags
are enabled in the VTL mapping template (see [Resolver Mapping Template Reference for DynamoDB](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem") in the
_AWS AppSync Developer Guide_). If enabled, the value will be
constructed by concatenating the _Base_ data source name and
the ISO 8601 format of the date at which the change occurred (e.g. if the
_Base_ table is named _Comments_, this
record will be set as `Comments:2019-01-01`).

**`gsi_ds_sk`**

A string value attribute that's generated to support a global secondary
index as a sort key. It will be included only if both the
`customPartitionKey` and `populateIndexFields` flags
are enabled in the VTL mapping template (see [Resolver Mapping Template Reference for DynamoDB](resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem "resolver-mapping-template-reference-dynamodb.md#aws-appsync-resolver-mapping-template-reference-dynamodb-updateitem") in the
_AWS AppSync Developer Guide_). If enabled, the value will be
constructed by concatenating the ISO 8601 format of the time at which the
change occurred, the partition key of the item in the _Base_
table, the sort key of the item in the _Base_ table, and the
version of the item (e.g. for a time of `09:30:00`, a partition key
value of `1a`, a sort key value of `2b`, and version of
`3`, this would be `09:30:00:1a#2b:3`).

These metadata fields will impact the overall size of items in the underlying data
source. AWS AppSync recommends reserving _500 bytes + Max
Primary Key Size_ of storage for versioned data source metadata when
designing your application. To use this metadata in client applications, include the
`_version`, `_lastChangedAt`, and `_deleted` fields
on your GraphQL types and in the selection set for mutations.
