# View user-defined types (UDTs) in Amazon Keyspaces

To view or list all UDTs in a single-Region keyspace, you can query the table `system_schema_mcs.types` in the system keyspace
using a statement in CQL, or use the `get-type` and `list-type` commands with the AWS CLI, or the console.

For either option, the IAM principal needs read permissions to the system keyspace.
For more information, see [Configure permissions to work with user-defined types (UDTs) in Amazon Keyspaces](configure-udt-permissions.md "configure-udt-permissions.md").

Console

###### View user-defined types (UDT) with the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**, and then choose a keyspace from the list.
3. Choose the **UDTs** tab to review the list of all UDTs in the keyspace.
4. To review one UDT in detail, choose a **UDT** from the list.
5. On the **Schema**tab you can review the schema. On the **Used in** tab
   you can see if this UDT is used in tables or other UDTs. Note that you can only delete UDTs that are not in use
   by either tables or other UDTs.

Cassandra Query Language (CQL)

###### View the user-defined types (UDTs) of a single-Region keyspace with CQL

1. To see the types that are available in a given keyspace, you can use the following statement.

```
SELECT type_name
FROM system_schema_mcs.types
WHERE keyspace_name = 'my_keyspace';
```

2. To view the details about a specific type, you can use the following statement.

```
SELECT
    keyspace_name,
    type_name,
    field_names,
    field_types,
    max_nesting_depth,
    last_modified_timestamp,
    status,
    direct_referring_tables,
    direct_parent_types
FROM system_schema_mcs.types
WHERE keyspace_name = 'my_keyspace' AND type_name = 'my_udt';
```

3. You can list all UDTs that exist in the account using `DESC TYPE`.

```
`DESC TYPES;

 Keyspace my_keyspace
 ---------------------------
 my_udt1 my_udt2

 Keyspace my_keyspace2
 ---------------------------
 my_udt1`
```

4. You can list all UDTs in the current selected keyspace using `DESC TYPE`.

```
`USE my_keyspace;
my_keyspace DESC TYPES;

my_udt1 my_udt2`
```

5. To list all UDTs in a multi-Region keyspace, you can query the system table `types`
   in the `system_multiregion_info` keyspace. The following query is an example of this.

```
SELECT keyspace_name, type_name, region, status FROM system_multiregion_info.types WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

The output of this command looks similar to this.

```
`keyspace_name | table_name | region | status
mykeyspace | mytable | us-east-1 | ACTIVE
mykeyspace | mytable | ap-southeast-1 | ACTIVE
mykeyspace | mytable | eu-west-1 | ACTIVE`
```

CLI

###### View user-defined types (UDTs) with the AWS CLI

1. To list the types available in a keyspace, you can use the
   `list-types` command.

```
aws keyspaces list-types
--keyspace-name 'my_keyspace'
```

The output of that command looks similar to this example.

```
`{
 "types": [
 "my_udt",
 "parent_udt"
 ]
}`
```

2. To view the details about a given type you can use the `get-type` command.

```
aws keyspaces get-type
--type-name 'my_udt'
--keyspace-name 'my_keyspace'
```

The output of this command looks similar to this example.

```
`{
 "keyspaceName": "my_keyspace",
 "typeName": "my_udt",
 "fieldDefinitions": [
 {
 "name": "a",
 "type": "int"
 },
 {
 "name": "b",
 "type": "text"
 }
 ],
 "lastModifiedTimestamp": 1721328225776,
 "maxNestingDepth": 3
 "status": "ACTIVE",
 "directReferringTables": [],
 "directParentTypes": [
 "parent_udt"
 ],
 "keyspaceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/"
}`
```
