# Nested type

AWS Clean Rooms supports queries involving data with nested data types, specifically the AWS Glue
struct, array, and map column types. Only the custom analysis rule supports nested data
types.

Notably, nested data types don't conform to the rigid, tabular structure of the
relational data model of SQL databases.

Nested data types contains tags that reference distinct entities within the data. They
can contain complex values such as arrays, nested structures, and other complex structures
that are associated with serialization formats, such as JSON. Nested data types support up
to 1 MB of data for an individual nested data type field or object.

###### Topics

- [ARRAY type](r_array_type.md "r_array_type.md")
- [MAP type](r_map_type.md "r_map_type.md")
- [STRUCT type](r_struct_type.md "r_struct_type.md")
- [Examples of nested data types](nested-data-type-examples.md "nested-data-type-examples.md")
