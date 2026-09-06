

# `ALTER STATISTICS`
<a name="alter-statistics-syntax-support"></a>

## Supported syntax
<a name="alter-statistics-supported-syntax"></a>

```
ALTER STATISTICS name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER STATISTICS name RENAME TO new_name
ALTER STATISTICS name SET SCHEMA new_schema
ALTER STATISTICS name SET STATISTICS { new_target | DEFAULT }
```

## Description
<a name="alter-statistics-description"></a>

`ALTER STATISTICS` changes the parameters of an existing extended statistics object. Any parameters not specifically set in the `ALTER STATISTICS` command retain their prior settings.

You must own the statistics object to use `ALTER STATISTICS`. To change a statistics object's schema, you must also have `CREATE` privilege on the new schema. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have `CREATE` privilege on the statistics object's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the statistics object. However, a superuser can alter ownership of any statistics object anyway.)

## Parameters
<a name="alter-statistics-parameters"></a>

**{{name}}**  
The name (optionally schema-qualified) of the statistics object to be altered.

**{{new\_owner}}**  
The user name of the new owner of the statistics object.

**{{new\_name}}**  
The new name for the statistics object.

**{{new\_schema}}**  
The new schema for the statistics object.

**{{new\_target}}**  
The statistic-gathering target for this statistics object for subsequent `ANALYZE` operations. In Aurora DSQL, the target can be set in the range `0` to `100`. Set it to `DEFAULT` to revert to using the system default statistics target (`default_statistics_target`). (Setting it to a value of `-1` is an obsolete spelling to get the same outcome.)  
If you set a target greater than `100`, Aurora DSQL returns the error `statistics target N exceeds maximum allowed value of 100`.