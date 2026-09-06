

# Delete a user-defined type (UDT) in Amazon Keyspaces
<a name="keyspaces-delete-udt"></a>

To delete a UDT in a keyspace, you can use the `DROP TYPE` statement in CQL, the `delete-type` command with the AWS CLI, or the console.

------
#### [ Console ]

**Delete a user-defined type (UDT) with the Amazon Keyspaces console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Keyspaces**, and then choose a keyspace from the list.

1. Choose the **UDTs** tab.

1. Choose the UDT that you want to delete. On the **Used in** you can confirm that the type you want to delete isn't currently used by a table or other UDT.

1. Choose **Delete** above the **Summary**. 

1. Type `Delete` in the dialog that appears, and choose **Delete UDT**.

------
#### [ Cassandra Query Language (CQL) ]

**Delete a user-defined type (UDT) with CQL**
+ To delete a type, you can use the following statement.

  ```
  DROP TYPE my_keyspace.my_udt;
  ```

  For more information about CQL syntax, see [DROP TYPE](cql.ddl.type.md#cql.ddl.type.drop).

------
#### [ CLI ]

**Delete a user-defined type (UDT) with the AWS CLI**

1. To delete a type, you can use the following command.

   ```
   aws keyspaces delete-type
   --keyspace-name 'my_keyspace'
   --type-name 'my_udt'
   ```

1. The output of the command looks similar to this example.

   ```
   {
       "keyspaceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/",
       "typeName": "my_udt"
   }
   ```

------