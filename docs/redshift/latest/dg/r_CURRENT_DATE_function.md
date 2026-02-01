Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CURRENT_DATE function

CURRENT_DATE returns a date in the current session time zone (UTC by default) in the
default format: YYYY-MM-DD.

###### Note

CURRENT_DATE returns the start date for the current transaction, not for the start of
the current statement. Consider the scenario where you start a transaction containing
multiple statements on 10/01/08 23:59, and the statement containing CURRENT_DATE runs at 10/02/08 00:00.
CURRENT_DATE returns `10/01/08`, not `10/02/08`.

## Syntax

```
CURRENT_DATE
```

## Return type

DATE

## Examples

The following example returns the current date (in the AWS Region where the function runs).

```
`select current_date;`
`date
------------
2008-10-01`
```

The following example creates a table, inserts a row where the default of column `todays_date` is CURRENT_DATE, and then selects all the rows in the table.

```

`CREATE TABLE insert_dates(
 label varchar(128) NOT NULL,
 todays_date DATE DEFAULT CURRENT_DATE);

INSERT INTO insert_dates(label)
VALUES('Date row inserted');

SELECT * FROM insert_dates;`

`label | todays_date
------------------+-------------
Date row inserted | 2023-05-10`
```
