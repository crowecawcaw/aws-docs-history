

# `DROP VIEW`
<a name="drop-view-overview"></a>

The `DROP VIEW` statement removes an existing view. Aurora DSQL supports the full PostgreSQL syntax for this command.

## Supported syntax
<a name="drop-view-supported-syntax"></a>

```
DROP VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description
<a name="drop-view-description"></a>

`DROP VIEW` drops an existing view. To execute this command you must be the owner of the view.

## Parameters
<a name="drop-view-parameters"></a>

**`IF EXISTS`**  
Don't throw an error if the view doesn't exist. A notice is issued in this case.

**`name`**  
The name (optionally schema-qualified) of the view to remove.

**`CASCADE`**  
Automatically drop objects that depend on the view (such as other views), and in turn all objects that depend on those objects.

**`RESTRICT`**  
Refuse to drop the view if any objects depend on it. This is the default.

## Examples
<a name="drop-view-examples"></a>

```
DROP VIEW kinds;
```

## Compatibility
<a name="drop-view-compatibility"></a>

This command conforms to the SQL standard, except that the standard only allows one view to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension that Aurora DSQL supports.