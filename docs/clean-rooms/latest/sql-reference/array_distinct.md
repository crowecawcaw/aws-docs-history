

# ARRAY\_DISTINCT function
<a name="array_distinct"></a>

The ARRAY\_DISTINCT function can be used to remove duplicate values from an array. The ARRAY\_DISTINCT function is useful when you need to remove duplicates from an array and work with only the unique elements. This can be helpful in scenarios where you want to perform operations or analyses on a dataset without the interference of repeated values.

## Syntax
<a name="array_distinct-syntax"></a>

```
array_distinct(array)
```

## Arguments
<a name="array_distinct-arguments"></a>

 *array*  
An ARRAY expression.

## Return type
<a name="array_distinct-return-type"></a>

The ARRAY\_DISTINCT function returns an ARRAY that contains only the unique elements from the input array. 

## Examples
<a name="array_distinct-example"></a>

In this example, the input array `[1, 2, 3, null, 3]` contains a duplicate value of `3`. The `array_distinct` function removes this duplicate value `3` and returns a new array with the unique elements: `[1, 2, 3, null]`.

```
SELECT array_distinct(array(1, 2, 3, null, 3));
 [1,2,3,null]
```

In this example, the input array `[1, 2, 2, 3, 3, 3]` contains duplicate values of `2` and `3`. The `array_distinct` function removes these duplicates and returns a new array with the unique elements: `[1, 2, 3]`.

```
SELECT array_distinct(array(1, 2, 2, 3, 3, 3))
  [1,2,3]
```