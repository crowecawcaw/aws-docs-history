Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DEALLOCATE

Deallocates a prepared statement.

## Syntax

```
DEALLOCATE [PREPARE] *plan\_name*
```

## Parameters

PREPARE

This keyword is optional and is ignored.

_plan_name_

The name of the prepared statement to deallocate.

## Usage Notes

DEALLOCATE is used to deallocate a previously prepared SQL statement. If you
don't explicitly deallocate a prepared statement, it is deallocated when the
current session ends. For more information on prepared statements, see [PREPARE](r_PREPARE.md "r_PREPARE.md").

## See Also

[EXECUTE](r_EXECUTE.md "r_EXECUTE.md"), [PREPARE](r_PREPARE.md "r_PREPARE.md")
