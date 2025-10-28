# Property column headers

You can specify a column (`:`) for a property by using the following syntax. The type names are not case
sensitive. If a colon appears within a property name, it must be escaped by preceding it with a backslash: `\:`.

```
propertyname:type
```

###### Note

- Space, comma, carriage return and newline characters are not allowed in the column headers, so property names cannot
  include these characters.

You can specify a column for an array type by adding [] to the type:

```
propertyname:type[]
```

- Edge properties can only have a single value and will cause an error if an array type is specified or a second value
  is specified. The following example shows the column header for a property named age of type Int.

```
age:Int
```

Every row in the file would be required to have an integer in that position or be left empty. Arrays of strings are
allowed, but strings in an array cannot include the semicolon (`;`) character unless it is escaped using
a backslash (`\;`).
