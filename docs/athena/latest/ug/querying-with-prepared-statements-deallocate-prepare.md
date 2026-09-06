

# DEALLOCATE PREPARE
<a name="querying-with-prepared-statements-deallocate-prepare"></a>

Removes the prepared statement with the specified name from the list of prepared statements in the current workgroup.

## Syntax
<a name="querying-with-prepared-statements-deallocate-prepare-syntax"></a>

```
DEALLOCATE PREPARE {{statement_name}}
```

{{statement\_name}} is the name of the prepared statement to be removed.

## Example
<a name="querying-with-prepared-statements-deallocate-prepare-examples"></a>

The following example removes the `my_select1` prepared statement from the current workgroup.

```
DEALLOCATE PREPARE my_select1
```