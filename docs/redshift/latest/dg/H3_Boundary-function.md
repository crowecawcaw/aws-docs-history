

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# H3\_Boundary
<a name="H3_Boundary-function"></a>

H3\_Boundary returns the boundary of an H3 cell ID from an input index. For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3).

## Syntax
<a name="H3_Boundary-function-syntax"></a>

```
H3_Boundary(index)
```

## Arguments
<a name="H3_Boundary-function-arguments"></a>

 *index*   
A value of data type `BIGINT` or `VARCHAR` that represents the index of an H3 cell. Or, an expression that evaluates to one of these data types.

## Return type
<a name="H3_Boundary-function-return"></a>

`POLYGON` – represents the polygon with spatial reference system identifier (SRID) of `0`.

If *index* is not valid, then an error is returned.

## Examples
<a name="H3_Boundary-function-examples"></a>

The following SQL inputs a `VARCHAR` that represents the index of an H3 cell, and returns a POLYGON with SRID 0 that represents the boundary of the input H3 cell. The output of H3\_Boundary is input to ST\_AwEWKT to display in extended well-known text (EWKT) representation.

```
SELECT ST_AsEWKT(H3_Boundary('8025fffffffffff'));
```

```
 st_asewkt
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 POLYGON((87.7729641223953 52.6542030078627,86.7082098104731 40.3127667561966,98.2285042557705 33.6210697806835,110.694610548823 37.163896485796,116.212895637138 47.3094513028131,106.40349563788 56.210610737585,87.7729641223953 52.6542030078627))
```

The following SQL inputs a `BIGINT` that represents the index of an H3 cell, and returns a POLYGON with SRID 0 that represents the boundary of the input H3 cell. The output of H3\_Boundary is input to ST\_AwEWKT to display in extended well-known text (EWKT) representation.

```
SELECT ST_AsEWKT(H3_Boundary(577129255373111295)); 
```

```
 st_asewkt
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
POLYGON((87.7729641223953 52.6542030078627,86.7082098104731 40.3127667561966,98.2285042557705 33.6210697806835,110.694610548823 37.163896485796,116.212895637138 47.3094513028131,106.40349563788 56.210610737585,87.7729641223953 52.6542030078627))
```