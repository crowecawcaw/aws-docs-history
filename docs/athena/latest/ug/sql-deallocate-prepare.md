

# DEALLOCATE PREPARE
<a name="sql-deallocate-prepare"></a>

Removes the prepared statement with the specified name from the prepared statements in the current workgroup.

## Synopsis
<a name="sql-deallocate-prepare-synopsis"></a>

```
DEALLOCATE PREPARE statement_name
```

## Examples
<a name="sql-deallocate-prepare-examples"></a>

The following example removes the `my_select1` prepared statement from the current workgroup.

```
DEALLOCATE PREPARE my_select1
```

## Additional resources
<a name="sql-deallocate-prepare-additional-resources"></a>

[Use prepared statements](querying-with-prepared-statements-querying.md)

[PREPARE](sql-prepare.md)