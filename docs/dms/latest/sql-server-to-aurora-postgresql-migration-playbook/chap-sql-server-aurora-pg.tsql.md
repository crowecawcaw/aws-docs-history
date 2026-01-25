# Service Broker functionality for T-SQL

This topic provides reference information about migrating from Microsoft SQL Server 2019’s Service Broker functionality to Amazon Aurora PostgreSQL. You can understand the challenges and alternatives available when moving from SQL Server’s native messaging and queuing capabilities to Aurora PostgreSQL, which doesn’t offer a direct equivalent. The topic explores how you can achieve similar functionality using a combination of AWS services, including DB Links, AWS Lambda, and Amazon SQS.

| Feature compatibility | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                   | Key differences                              |
| --------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| No compatibility      | No automation                      | [Service Broker](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.servicebroker "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.servicebroker") | Use Amazon Lambda for similar functionality. |

## SQL Server Usage

SQL Server Service Broker provides native support for messaging and queuing applications. Developers use Server Broker to create complex applications that use the database engine components to communicate between several SQL Server databases. Developers can use Service Broker to easily build distributed and more reliable applications.

Benefits of using messaging queues:

- Decouple dependencies between applications by communicating through messages.
- Scale out your architecture by moving queues or message processors to separate servers as needed.
- Maintain individual parts with a minimal impact to the end users.
- Control when the messages are processed, for example, off-peak hours.
- Process queued messages on multiple servers or processes or threads.

The following sections describe the Service Broker commands.

### CREATE MESSAGE TYPE

The following example creates a message with name and structure.

```
CREATE MESSAGE TYPE message_type_name
  [ AUTHORIZATION owner_name ]
  [ VALIDATION = { NONE
    | EMPTY
    | WELL_FORMED_XML
    | VALID_XML WITH SCHEMA COLLECTION schema_collection_name
  } ]
[ ; ]
```

For more information, see [CREATE MESSAGE TYPE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-message-type-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-message-type-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

### CREATE QUEUE

The following example creates a queue to store messages.

```
CREATE QUEUE <object>
  [ WITH
    [ STATUS = { ON | OFF } [ , ] ]
    [ RETENTION = { ON | OFF } [ , ] ]
    [ ACTIVATION (
      [ STATUS = { ON | OFF } , ]
        PROCEDURE_NAME = <procedure> ,
        MAX_QUEUE_READERS = max_readers ,
        EXECUTE AS { SELF | 'user_name' | OWNER }
        ) [ , ] ]
    [ POISON_MESSAGE_HANDLING (
      [ STATUS = { ON | OFF } ] ) ]
    ]
      [ ON { filegroup | [ DEFAULT ] } ]
[ ; ]

<object> ::=
{
  [ database_name. [ schema_name ] . | schema_name. ]
    queue_name
}

<procedure> ::=
{
  [ database_name. [ schema_name ] . | schema_name. ]
    stored_procedure_name
}
```

For more information, see [CREATE QUEUE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-queue-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-queue-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

### CREATE CONTRACT

The following example specifies the role and what type of messages a service can handle.

```
CREATE CONTRACT contract_name
  [ AUTHORIZATION owner_name ]
    ( { { message_type_name | [ DEFAULT ] }
      SENT BY { INITIATOR | TARGET | ANY }
    } [ ,...n] )
[ ; ]
```

For more information, see [CREATE CONTRACT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-contract-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-contract-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

### CREATE SERVICE

The following example creates a named Service Broker for a specified task or set of tasks.

```
CREATE SERVICE service_name
  [ AUTHORIZATION owner_name ]
  ON QUEUE [ schema_name. ]queue_name
  [ ( contract_name | [DEFAULT][ ,...n ] ) ]
[ ; ]
```

For more information, see [CREATE SERVICE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-service-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-service-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

### BEGIN DIALOG CONVERSATION

The following example starts the interaction between Service Brokers.

```
BEGIN DIALOG [ CONVERSATION ] @dialog_handle
  FROM SERVICE initiator_service_name
  TO SERVICE 'target_service_name'
    [ , { 'service_broker_guid' | 'CURRENT DATABASE' }]
  [ ON CONTRACT contract_name ]
  [ WITH
  [ { RELATED_CONVERSATION = related_conversation_handle
    | RELATED_CONVERSATION_GROUP = related_conversation_group_id } ]
  [ [ , ] LIFETIME = dialog_lifetime ]
  [ [ , ] ENCRYPTION = { ON | OFF } ] ]
[ ; ]
```

For more information, see [BEGIN DIALOG CONVERSATION (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/begin-dialog-conversation-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/begin-dialog-conversation-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

### WAITFOR(RECEIVE TOP(1))

The following example specifies that a code block has to wait until one message is received.

```
[ WAITFOR ( ]
  RECEIVE [ TOP ( n ) ]
  <column_specifier> [ ,...n ]
  FROM <queue>
  [ INTO table_variable ]
  [ WHERE { conversation_handle = conversation_handle
    | conversation_group_id = conversation_group_id } ]
  [ ) ] [ , TIMEOUT timeout ]
[ ; ]

<column_specifier> ::=
{ *
  | { column_name | [ ] expression } [ [ AS ] column_alias ]
  | column_alias = expression
} [ ,...n ]

<queue> ::=
{
  [ database_name . [ schema_name ] . | schema_name . ]
    queue_name
}
```

For more information, see [RECEIVE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/receive-transact-sql?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/t-sql/statements/receive-transact-sql?view=sql-server-2017") in the _SQL Server documentation_.

You can combine all of the preceding commands to achieve your architecture goals.

For more information, see [Service Broker](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-service-broker?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-service-broker?view=sql-server-2017") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t provide a compatible solution to the SQL Server Service Broker. However, you can use DB Links and AWS Lambda to achieve similar functionality.

You can combine AWS Lambda with AWS SQS to reduce costs and remove some loads from the database into the AWS Lambda and Amazon Simple Queue Service (Amazon SQS). This will be much more efficient. For more information, see [Using Lambda with Amazon SQS](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md").

For example, you can create a table in each database and connect each database with a DB link to read the tables and process the data. For more information, see DB Links.

You can also use AWS Lambda to query a table from the database, process the data, and insert it to another database (even another database type). This approach is the best option for moving workloads out of the database to a less expensive instance type.

For even more decoupling and reducing workloads from the database, you can use Amazon SQS with Lambda.

For more information, see [Database Mail](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").
