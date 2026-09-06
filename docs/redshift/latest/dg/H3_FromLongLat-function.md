

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# H3\_FromLongLat
<a name="H3_FromLongLat-function"></a>

H3\_FromLongLat returns the corresponding H3 cell ID from an input longitude, latitude, and resolution. For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3).

## Syntax
<a name="H3_FromLongLat-function-syntax"></a>

```
H3_FromLongLat(longitude, latitude, resolution)
```

## Arguments
<a name="H3_FromLongLat-function-arguments"></a>

 *longitude*   
A value of data type `DOUBLE PRECISION` or an expression that evaluates to a `DOUBLE PRECISION` type.

 *latitude*   
A value of data type `DOUBLE PRECISION` or an expression that evaluates to a `DOUBLE PRECISION` type.

 *resolution*   
A value of data type `INTEGER` or an expression that evaluates to an `INTEGER` type. The value represents the resolution of the H3 grid system. The value must be an integer between 0–15, inclusive. With `0` being the coarsest and `15` being the finest. 

## Return type
<a name="H3_FromLongLat-function-return"></a>

`BIGINT` – represents the H3 cell ID.

If *resolution* is out of bounds, then an error is returned.

## Examples
<a name="H3_FromLongLat-function-examples"></a>

The following SQL returns the H3 cell ID from longitude `0`, latitude `0`, and resolution `10`. 

```
SELECT H3_FromLongLat(0, 0, 10);
```

```
 h3_fromlonglat
-------------------
 623560421467684863
```