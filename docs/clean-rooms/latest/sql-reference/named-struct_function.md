

# NAMED\_STRUCT constructor function
<a name="named-struct_function"></a>

The NAMED\_STRUCT constructor function creates a struct with the given field names and values.

Constructor functions like NAMED\_STRUCT are useful when you need to create new data structures programmatically within your SQL queries. They allow you to build complex data structures, such as structs or records, that can be used in further data processing or analysis.

## Syntax
<a name="named-struct_function-syntax"></a>

```
named_struct(name1, val1, name2, val2, ...)
```

## Arguments
<a name="snamed-truct_function-arguments"></a>

 *name1*   
A STRING literal naming field 1.

 *val1*   
An expression of any type specifying the value for field 1.

## Returns
<a name="named-struct_function-returns"></a>

The NAMED\_STRUCT function returns a struct with field 1 matching the type of *val1*. 

## Examples
<a name="named-struct_function-examples"></a>

The following example creates a new struct with three named fields: The field `"a"` is assigned the value `1`. The field `"b"` is assigned the value `2.` The field `"c"` is assigned the value `3`. The resulting struct is then returned as the output of the SQL statement. 

```
SELECT named_struct("a", 1, "b", 2, "c", 3);
 {"a":1,"b":2,"c":3}
```