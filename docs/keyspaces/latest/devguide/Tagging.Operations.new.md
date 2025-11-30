# Add tags to a new stream for an existing table

You can add tags when you create a new stream for an existing table. You can either use the `PropagateTags` flag
to apply the table tags to the stream or specify new tags for the stream. You can use CQL or the AWS CLI to tag a new stream.

###### Note

Amazon Keyspaces CDC requires the presence of a service-linked role
(`AWSServiceRoleForAmazonKeyspacesCDC`) that publishes metric data
from Amazon Keyspaces CDC streams into the `"cloudwatch:namespace": "AWS/Cassandra"`
in your CloudWatch account on your behalf. This role is created automatically for you. For
more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").

Console

###### Add tags when creating a new stream using the (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**,
   and then choose the table you want to add a stream for.
3. Choose the **Streams** tab.
4. In the **Stream details** section, choose **Edit**.
5. Select **Turn on streams** .
6. Select the **View type** and continue to **Tags** to create tags for the stream.
7. You can select one of the following options:
   - **No tags** – Use this option if you don't want to create any tags for the stream.
   - **Copy tags from table** – Use this option if you want to copy the tags from the table
     to the stream. After copying the tags, you can edit them for the stream. Note that this option is only available if the table has tags.
   - **Add new tags** – You can add up to 50 tags for the stream by choosing
     **Add new tag**.

8. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Add tags when creating a new stream

1. To create a new stream for an existing table and apply the table's tags to the stream, you can use the
   `'propagate_tags': 'TABLE'` flag. The following statements is an example of this.

```
ALTER TABLE mytable WITH cdc = TRUE AND CUSTOM_PROPERTIES={ 'cdc_specification': { 'view_type': 'NEW_IMAGE', 'propagate_tags': 'TABLE' } };
```

2. To create a new stream for an existing table and specify new tags,
   you can use the following example.

```
ALTER TABLE mytable WITH cdc = TRUE AND CUSTOM_PROPERTIES={ 'cdc_specification': { 'view_type': 'NEW_IMAGE', 'tags': { 'key': 'string', 'value': 'string' }} };
```

CLI

###### Add tags when creating a new stream using the AWS CLI

1. To create a new stream with tags, you can use the `propagateTags=TABLE` flag to apply the table's tags
   automatically to the stream. The following code is an example of this.

```
aws keyspaces update-table \
--keyspace-name 'my_keyspace' \
--table-name 'my_table' \
--cdc-specification propagateTags=TABLE,status=ENABLED,viewType=NEW_IMAGE
```

2. To create a new stream for an existing table and specify new tags,
   you can use the following example.

```
aws keyspaces update-table \
--keyspace-name 'my_keyspace' \
--table-name 'my_table' \
--cdc-specification 'status=ENABLED,viewType=NEW_IMAGE,tags=[{key=tag_key, value=tag_value}]'
```
