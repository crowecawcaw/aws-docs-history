

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# H3\_FromPoint
<a name="H3_FromPoint-function"></a>

H3\_FromPoint returns the corresponding H3 cell ID from an input geometry point and resolution. For information about H3 indexing, see [H3](spatial-terminology.md#spatial-terminology-h3).

## Syntax
<a name="H3_FromPoint-function-syntax"></a>

```
H3_FromPoint(geom, resolution)
```

## Arguments
<a name="H3_FromPoint-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type. The *geom* must be a `POINT`.

 *resolution*   
A value of data type `INTEGER` or an expression that evaluates to an `INTEGER` type. The value represents the resolution of the H3 grid system. The value must be an integer between 0–15, inclusive. With `0` being the coarsest and `15` being the finest. 

## Return type
<a name="H3_FromPoint-function-return"></a>

`BIGINT` – represents the H3 cell ID.

If *geom* is not a `POINT`, then an error is returned.

If *resolution* is out of bounds, then an error is returned.

If *geom* is empty, then NULL is returned.

## Examples
<a name="H3_FromPoint-function-examples"></a>

The following SQL returns the H3 cell ID from point `0,0`, and resolution `10`. 

```
SELECT H3_FromPoint(ST_GeomFromText('POINT(0 0)'), 10);
```

```
 h3_frompoint
-------------------
 623560421467684863
```