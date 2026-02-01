Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ABORT

Stops the currently running transaction and discards all updates made by that
transaction. ABORT has no effect on already completed transactions.

This command performs the same function as the ROLLBACK command. For information, see
[ROLLBACK](r_ROLLBACK.md "r_ROLLBACK.md").

## Syntax

```
ABORT [ WORK | TRANSACTION ]
```

## Parameters

WORK

Optional keyword.

TRANSACTION

Optional keyword; WORK and TRANSACTION are synonyms.

## Example

The following example creates a table then starts a transaction where data is
inserted into the table. The ABORT command then rolls back the data insertion to leave
the table empty.

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

The command output shows that both rows are successfully inserted:

```
         name           |  gross
------------------------+----------
Raiders of the Lost Ark | 23400000
Star Wars               | 10000000
(2 rows)
```

This command now rolls back the data changes to where the transaction began:

```
abort;
```

Selecting data from the table now shows an empty table:

```
select * from movie_gross;

 name | gross
------+-------
(0 rows)
```
