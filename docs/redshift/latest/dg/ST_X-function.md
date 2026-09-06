

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_X
<a name="ST_X-function"></a>

ST\_X returns the first coordinate of an input point. 

## Syntax
<a name="ST_X-function-syntax"></a>

```
ST_X(point)
```

## Arguments
<a name="ST_X-function-arguments"></a>

 *point*   
A `POINT` value of data type `GEOMETRY`. 

## Return type
<a name="ST_X-function-return"></a>

`DOUBLE PRECISION` value of the first coordinate.

If *point* is null, then null is returned. 

If *point* is the empty point, then null is returned. 

If *point* is not a `POINT`, then an error is returned. 

## Examples
<a name="ST_X-function-examples"></a>

The following SQL returns the first coordinate of a point. 

```
SELECT ST_X(ST_Point(1,2));
```

```
st_x
-----------
 1.0
```