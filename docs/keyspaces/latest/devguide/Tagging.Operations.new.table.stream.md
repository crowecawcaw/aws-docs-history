# Add tags to a new stream when creating a table

You can add tags to streams when you create a new table with a stream using CQL or the AWS CLI to tag a stream.

###### Note

Amazon Keyspaces CDC requires the presence of a service-linked role
(`AWSServiceRoleForAmazonKeyspacesCDC`) that publishes metric data
from Amazon Keyspaces CDC streams into the `"cloudwatch:namespace": "AWS/Cassandra"`
in your CloudWatch account on your behalf. This role is created automatically for you. For
more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").

Cassandra Query Language (CQL)

###### Add tags to a stream when creating a new table using CQL

1. To create a new table with a stream and apply the table tags
   automatically to the stream, you can use the `'propagate_tags': 'TABLE'` flag. The following
   statement is an example of this.

```
CREATE TABLE `mytable (pk int, ck text, PRIMARY KEY(pk))`
WITH TAGS=`{'key1':'val1', 'key2':'val2'}`
AND cdc = TRUE
AND CUSTOM_PROPERTIES={
    'cdc_specification': {
        'view_type': 'NEW_IMAGE',
        'propagate_tags': 'TABLE'
    }
};
```

2. To apply new tags to the stream, you can use the following example.

```
CREATE TABLE `mytable (pk int, ck text, PRIMARY KEY(pk))`
WITH TAGS=`{'key1':'val1', 'key2':'val2'}`
AND cdc = TRUE
AND CUSTOM_PROPERTIES={
    'cdc_specification': {
        'view_type': 'NEW_IMAGE',
        'tags': { 'key': 'string', 'value': 'string' },
    }
};
```

CLI

###### Add tags to a stream when creating a new table using the AWS CLI

1. To create a table with a stream and apply the table tags
   automatically to the stream, you can use the `propagateTags=Table` flag. The following code is an
   example of this.

```
aws keyspaces create-table \
--keyspace-name 'my_keyspace' \
--table-name 'my_table' \
--schema-definition 'allColumns=[{name=pk,type=int},{name=ck,type=text}],clusteringKeys=[{name=ck,orderBy=ASC}],partitionKeys=[{name=pk}]' \
--tags key=tag_key,value=tag_value
--cdc-specification propagateTags=TABLE,status=ENABLED,viewType=NEW_IMAGE
```

2. To apply different tags to the stream, you can use the following example.

```
aws keyspaces create-table \
--keyspace-name 'my_keyspace' \
--table-name 'my_table' \
--schema-definition 'allColumns=[{name=pk,type=int},{name=ck,type=text}],clusteringKeys=[{name=ck,orderBy=ASC}],partitionKeys=[{name=pk}]' \
--tags key=tag_key,value=tag_value
--cdc-specification 'status=ENABLED,viewType=NEW_IMAGE,tags=[{key=tag_key, value=tag_value}]'
```
