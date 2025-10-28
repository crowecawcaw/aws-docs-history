# SUPER type

Use the SUPER data type to store semistructured data or documents as values.

Semistructured data doesn't conform to the rigid and tabular structure of the
relational data model used in SQL databases. The SUPER data type contains tags that
reference distinct entities within the data. SUPER data types can contain complex values
such as arrays, nested structures, and other complex structures that are associated with
serialization formats, such as JSON. The SUPER data type is a set of schemaless array and
structure values that encompass all other scalar types of AWS Clean Rooms.

The SUPER data type supports up to 1 MB of data for an individual SUPER field or object.

The SUPER data type has the following properties:

- An AWS Clean Rooms scalar value:
  - A null
  - A boolean
  - A number, such as smallint, integer, bigint, decimal, or floating point
    (such as float4 or float8)
  - A string value, such as varchar or char

- A complex value:

      + An array of values, including scalar or complex
      + A structure, also known as tuple or object, that is a map of attribute names
       and values (scalar or complex)

  Any of the two types of complex values contain their own scalars or complex values
  without having any restrictions for regularity.

The SUPER data type supports the persistence of semistructured data in a schemaless
form. Although hierarchical data model can change, the old versions of data can coexist in
the same SUPER column.
