

# Creating custom error messages for Amazon RDS for SQL Server
<a name="Appendix.SQLServer.CommonDBATasks.CustomMessage"></a>

Applications often define their own error messages in `sys.messages` so that they can raise them with `RAISERROR`. On an Amazon RDS DB instance, to add a custom message to `sys.messages`, use the `rds_create_custom_message` stored procedure. The procedure passes its parameters to `sp_addmessage`.

The `rds_create_custom_message` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `@msgnum` | int | NULL | required | The ID of the message. The value must be between 50001 and 2147483647. | 
| `@severity` | smallint | NULL | required | The severity level of the message. The value must be between 1 and 25. | 
| `@msgtext` | nvarchar(255) | NULL | required | The text of the message. The value can't be empty. | 
| `@lang` | SYSNAME | NULL | optional | The language of the message. The default is the default language of the session. | 
| `@with_log` | varchar(5) | NULL | optional | Specifies whether to write the message to the Windows application log when the message is raised. | 
| `@replace` | varchar(7) | NULL | optional | Specify `REPLACE` to overwrite an existing message that has the same ID and language. | 

The parameters have the same meaning as the parameters of `sp_addmessage`. For more information, see [sp\_addmessage](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addmessage-transact-sql) on the Microsoft Learn website.

The following example adds a message to `sys.messages` and logs it to the Windows application log when it's raised. In the example, replace the `@msgnum` value {{50002}}, the `@severity` value {{16}}, and the `@msgtext` value with your own message ID, severity, and text.

```
EXEC msdb.dbo.rds_create_custom_message
    @msgnum = {{50002}},
    @severity = {{16}},
    @msgtext = N'{{The order could not be processed.}}',
    @lang = 'us_english',
    @with_log = 'TRUE';
```

The following example replaces the text of an existing message. In the example, replace the `@msgnum` value {{50002}}, the `@severity` value {{16}}, and the `@msgtext` value with your own message ID, severity, and text.

```
EXEC msdb.dbo.rds_create_custom_message
    @msgnum = {{50002}},
    @severity = {{16}},
    @msgtext = N'{{The order could not be processed. Contact support.}}',
    @lang = 'us_english',
    @with_log = 'TRUE',
    @replace = 'REPLACE';
```

To confirm that the message was added, query `sys.messages`. In the example, replace the `message_id` value {{50002}} with your message ID.

```
SELECT * FROM sys.messages WHERE message_id = {{50002}};
```