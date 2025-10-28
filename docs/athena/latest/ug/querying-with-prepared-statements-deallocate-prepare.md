# DEALLOCATE PREPARE

Removes the prepared statement with the specified name from the list of
prepared statements in the current workgroup.

## Syntax

```
DEALLOCATE PREPARE `statement_name`
```

`statement_name` is the name of the prepared
statement to be removed.

## Example

The following example removes the `my_select1` prepared
statement from the current workgroup.

```
DEALLOCATE PREPARE **my\_select1**
```
