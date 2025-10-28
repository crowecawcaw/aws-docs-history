# Nested type

AWS Clean Rooms supports queries involving data with nested data types, specifically the AWS Glue
STRUCT, ARRAY, and MAP column types. Only the custom analysis rule supports nested data
types.

Notably, nested data types don't conform to the rigid, tabular structure of the
relational data model of SQL databases.

Nested data types contains tags that reference distinct entities within the data. They
can contain complex values such as arrays, nested structures, and other complex structures
that are associated with serialization formats, such as JSON. Nested data types support up
to 1 MB of data for an individual nested data type field or object.

###### Topics

- [ARRAY type](array_type.md "array_type.md")
- [MAP type](map_type.md "map_type.md")
- [STRUCT type](struct_type.md "struct_type.md")
- [Examples of nested data types](s_nested-data-type-examples.md "s_nested-data-type-examples.md")
