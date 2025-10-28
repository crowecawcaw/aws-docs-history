# Using the HBase shell

After you create an HBase cluster, the next step is to connect to HBase so you can begin
reading and writing data (data writes are not supported on a read-replica cluster). You can use the [HBase shell](https://hbase.apache.org/book.html#shell "https://hbase.apache.org/book.html#shell") to test
commands.

###### To open the HBase shell

1. Use SSH to connect to the main server in the HBase cluster. For information
   about how to connect to the Amazon EMR primary node using SSH, see [Connect to the primary node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the _Amazon EMR Management Guide_.
2. Run `hbase shell`. The HBase shell opens with a prompt similar to
   the following.

```
hbase(main):001:0>
```

You can issue HBase shell commands from the prompt. For more information about the shell
commands and how to call them, type help at the HBase prompt and press Enter.

## Create a table

The following command creates a table named 't1' that has a single column family named
'f1'.

```
hbase(main):001:0>create 't1', 'f1'
```

## Put a value

The following command puts value 'v1' for row 'r1' in table 't1' and column 'f1'.

```
hbase(main):001:0>put 't1', 'r1', 'f1:col1', 'v1'
```

## Get a value

The following command gets the values for row 'r1' in table 't1'.

```
hbase(main):001:0>get 't1', 'r1'
```

## Delete a table

The following command drops and deletes table 't1'.

```
hbase(main):001:0>drop 'ns1:t1',false
```

The boolean value corresponds to whether or not you want to archive your table, so you can
set it to `true` if you want to save it. You can also run `drop
 'ns1:t1'` with no boolean to archive the table.
