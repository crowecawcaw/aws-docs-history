

# ARRAY\_REMOVE function
<a name="array_remove"></a>

The ARRAY\_REMOVE function takes two arguments: The first argument is the input array from which the elements will be removed. The second argument is the value that will be removed from the array. This function is useful when you need to remove specific elements from an array. This can be helpful in scenarios where you need to perform data cleaning or preprocessing on an array of values.

## Syntax
<a name="array_remove-syntax"></a>

```
array_remove(array, element)
```

## Arguments
<a name="array_remove-arguments"></a>

 *array*  
An ARRAY.

 *element*  
An expression of a type sharing a least common type with the elements of array.

## Return type
<a name="array_remove-return-type"></a>

The ARRAY\_REMOVE function returns the result type matched the type of the array. If the element to be removed is `NULL`, the result is `NULL`.

## Examples
<a name="array_remove-example"></a>

In this example, the ARRAY\_REMOVE function takes the array `[1, 2, 3, null, 3]` and removes all occurrences of the value 3. The resulting output is the array `[1, 2, null]`. 

```
SELECT array_remove(array(1, 2, 3, null, 3), 3);
 [1,2,null]
```