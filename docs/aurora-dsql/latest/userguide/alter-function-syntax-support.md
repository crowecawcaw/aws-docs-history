

# `ALTER FUNCTION`
<a name="alter-function-syntax-support"></a>

`ALTER FUNCTION` changes the definition of a function.

## Supported syntax
<a name="alter-function-supported-syntax"></a>

```
ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    RENAME TO new_name
ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    SET SCHEMA new_schema
```

## Description
<a name="alter-function-description"></a>

`ALTER FUNCTION` changes the definition of an existing function. 

 You must own the function to use `ALTER FUNCTION`. To change a function's schema, you must also have `CREATE` privilege on the new schema. To alter the owner, you must be a member of the new owning role, and that role must have `CREATE` privilege on the function's schema.

**`RENAME TO`**  
Changes the name of the function.

**`OWNER TO`**  
Changes the owner of the function to the specified user.

**`SET SCHEMA`**  
Moves the function into another schema.

## Parameters
<a name="alter-function-parameters"></a>

**{{name}}**  
The name (optionally schema-qualified) of an existing function to alter.

**{{argmode}}**  
The mode of an argument: `IN`, `OUT`, `INOUT`, or `VARIADIC`. If omitted, the default is `IN`. The function uses only the input arguments for identification, so list only the `IN`, `INOUT`, and `VARIADIC` arguments.

**{{argname}}**  
The name of an argument.

**{{argtype}}**  
The data type(s) of the function's arguments.

**{{new\_name}}**  
The new name for the function.

**{{new\_owner}}**  
The new owner of the function.

**{{new\_schema}}**  
The new schema for the function.

## Considerations
<a name="alter-function-considerations"></a>

To change other attributes than those listed above, use `CREATE OR REPLACE FUNCTION`. For more information, see [`CREATE FUNCTION`](create-function-syntax-support.md).

To add, change, or remove a comment on a function, use the separate `COMMENT ON FUNCTION` command.

## Examples
<a name="alter-function-examples"></a>

Rename the function `add` (which takes two `integer` arguments) to `sum_two`:

```
ALTER FUNCTION add(integer, integer) RENAME TO sum_two;
```

Change the owner of the function `add` to the current user:

```
ALTER FUNCTION add(integer, integer) OWNER TO CURRENT_USER;
```

Move the function `add` into the schema `utils`:

```
ALTER FUNCTION add(integer, integer) SET SCHEMA utils;
```

## Compatibility
<a name="alter-function-compatibility"></a>

Aurora DSQL supports the `RENAME TO`, `OWNER TO`, and `SET SCHEMA` forms of the PostgreSQL `ALTER FUNCTION` statement. The other forms available in PostgreSQL are not supported. 