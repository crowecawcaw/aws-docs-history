

# MAP constructor function
<a name="map_function"></a>

The MAP constructor function creates a map with the given key/value pairs.

Constructor functions like MAP are useful when you need to create new data structures programmatically within your SQL queries. They allow you to build complex data structures that can be used in further data processing or analysis. 

## Syntax
<a name="map_function-syntax"></a>

```
map(key0, value0, key1, value1, ...)
```

## Arguments
<a name="map_function-arguments"></a>

 *key0*   
An expression of any comparable type. All *key0* must share a least common type.

 *value0*   
An expression of any type. All *valueN* must share a least common type.

## Returns
<a name="map_function-returns"></a>

The MAP function returns a MAP with keys typed as the least common type of *key0* and values typed as the least common type of *value0*.

## Examples
<a name="map_function-examples"></a>

The following example creates a new map with two key-value pairs: The key `1.0` is associated with the value `'2'`. The key `3.0` is associated with the value `'4'`. The resulting map is then returned as the output of the SQL statement. 

```
SELECT map(1.0, '2', 3.0, '4');
 {1.0:"2",3.0:"4"}
```