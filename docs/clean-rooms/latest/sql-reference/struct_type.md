# STRUCT type

Use the STRUCT type to represent values with the structure described by a sequence of
StructFields (fields).

```
struct(name, dataType, nullable)
```

StructField(name, dataType, nullable): Represents a field in a StructType.

`dataType`: the data type a field

`name`: the name of a field

Use `nullable` to indicate if values of these fields can have
`null` values.
