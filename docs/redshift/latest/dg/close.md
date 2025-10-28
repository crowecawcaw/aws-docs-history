Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CLOSE

(Optional) Closes all of the free resources that are associated with an open cursor.
[COMMIT](r_COMMIT.md "r_COMMIT.md"), [END](r_END.md "r_END.md"), and [ROLLBACK](r_ROLLBACK.md "r_ROLLBACK.md")
automatically close the cursor, so it isn't necessary to use the CLOSE command to
explicitly close the cursor.

For more information, see [DECLARE](declare.md "declare.md"), [FETCH](fetch.md "fetch.md").

## Syntax

```
CLOSE *cursor*
```

## Parameters

_cursor_

Name of the cursor to close.

## CLOSE example

The following commands close the cursor and perform a commit, which ends the
transaction:

```
close movie_cursor;
commit;
```
