Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ROLLBACK

Stops the current transaction and discards all updates made by that transaction.

This command performs the same function as the [ABORT](r_ABORT.md "r_ABORT.md") command.

## Syntax

```
ROLLBACK [ WORK | TRANSACTION ]
```

## Parameters

WORK

Optional keyword. This keyword isn't supported within a stored
procedure.

TRANSACTION

Optional keyword. WORK and TRANSACTION are synonyms. Neither is supported
within a stored procedure.

For information about using ROLLBACK within a stored procedure, see [Managing transactions](stored-procedure-transaction-management.md "stored-procedure-transaction-management.md").

## Example

The following example creates a table then starts a transaction where data is
inserted into the table. The ROLLBACK command then rolls back the data insertion to
leave the table empty.

The following command creates an example table called MOVIE_GROSS:

```
create table movie_gross( name varchar(30), gross bigint );
```

The next set of commands starts a transaction that inserts two data rows into the
table:

```
begin;

insert into movie_gross values ( 'Raiders of the Lost Ark', 23400000);

insert into movie_gross values ( 'Star Wars', 10000000 );
```

Next, the following command selects the data from the table to show that it was
successfully inserted:

```
select * from movie_gross;
```

The command output shows that both rows successfully inserted:

```
name           |  gross
-------------------------+----------
Raiders of the Lost Ark | 23400000
Star Wars               | 10000000
(2 rows)
```

This command now rolls back the data changes to where the transaction began:

```
rollback;
```

Selecting data from the table now shows an empty table:

```
select * from movie_gross;

name | gross
------+-------
(0 rows)
```
