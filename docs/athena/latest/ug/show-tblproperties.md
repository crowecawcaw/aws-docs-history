

# SHOW TBLPROPERTIES

Lists table properties for the named table.

## Synopsis
<a name="synopsis"></a>

```sql
SHOW TBLPROPERTIES table_name [('property_name')]
```

## Parameters
<a name="parameters"></a>

**[('property\_name')]**  
If included, only the value of the property named `property_name` is listed.

## Examples
<a name="examples"></a>

```sql
SHOW TBLPROPERTIES orders;
```

```sql
SHOW TBLPROPERTIES orders('comment');
```