

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_Z
<a name="ST_Z-function"></a>

ST\_Z returns the `z` coordinate of an input point. 

## Syntax
<a name="ST_Z-function-syntax"></a>

```
ST_Z(point)
```

## Arguments
<a name="ST_Z-function-arguments"></a>

 *point*   
A `POINT` value of data type `GEOMETRY`. 

## Return type
<a name="ST_Z-function-return"></a>

`DOUBLE PRECISION` value of the `m` coordinate.

If *point* is null, then null is returned. 

If *point* is a 2D or 3DM point, then null is returned. 

If *point* is the empty point, then null is returned. 

If *point* is not a `POINT`, then an error is returned. 

## Examples
<a name="ST_Z-function-examples"></a>

The following SQL returns the `z` coordinate of a point in a 3DZ geometry. 

```
SELECT ST_Z(ST_GeomFromEWKT('POINT Z (1 2 3)'));
```

```
st_z
-----------
 3
```

The following SQL returns the `z` coordinate of a point in a 4D geometry. 

```
SELECT ST_Z(ST_GeomFromEWKT('POINT ZM (1 2 3 4)'));
```

```
st_z
-----------
 3
```