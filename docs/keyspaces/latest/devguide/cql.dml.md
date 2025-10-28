# UPDATE

Use the `UPDATE` statement to modify a row in a table.

Syntax

````
**update\_statement** ::=  UPDATE table_name
                      [ USING update_parameter ( AND update_parameter )* ]
                      SET assignment ( ',' assignment )*
                      WHERE where_clause
                      [ IF ( EXISTS | condition ( AND condition )*) ]
**update\_parameter** ::=  ( integer | bind_marker )
**assignment**       ::=  simple_selection '=' term
| column_name '=' column_name ( '+' | '-' ) term
| column_name '=' list_literal '+' column_name **simple\_selection** ::=  column_name | column_name '[' term ']'
| column_name '.' `field_name **condition**        ::=  simple_selection operator term ``` Example ``` UPDATE "myGSGKeyspace".employees_tbl SET pay_scale = 5 WHERE id = '567-89-0123' AND division = 'Marketing' ; ``` To increment a `counter`, use the following syntax. For more information, see [Counters](cql.md#cql.data-types.numeric.counters "cql.md#cql.data-types.numeric.counters"). ``` UPDATE ActiveUsers SET counter = counter + 1  WHERE user = A70FE1C0-5408-4AE3-BE34-8733E5K09F14 AND action = 'click'; ``` Update parameters `UPDATE` supports the following values as `update_parameter`: <br>• `TTL` – A time value in seconds. The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years. <br>• `TIMESTAMP` – A `bigint` value representing the number of microseconds since the standard base time known as the epoch: January 1 1970 at 00:00:00 GMT. A timestamp in Amazon Keyspaces has to fall between the range of 2 days in the past and 5 minutes in the future. Example ``` UPDATE `my_table` (userid, time, subject, body, user) VALUES (B79CB3BA-745E-5D9A-8903-4A02327A7E09, 96a29100-5e25-11ec-90d7-b5d91eceda0a, 'Message', 'Hello again','205.212.123.123') USING TIMESTAMP '2022-11-03 13:30:54+0400'; ```
````
