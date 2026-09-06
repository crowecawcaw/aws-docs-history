

# ST\_Contains
<a name="access-graph-opencypher-22-spatial-functions-st-contains"></a>

ST\_Contains returns true if the 2D projection of the first input geometry contains the 2D projection of the second input geometry. Geometry A contains geometry B if every point in B is a point in A, and their interiors have nonempty intersection. ST\_Contains(A, B) is equivalent to ST\_Within(B, A).

**Syntax**

```
ST_Contains(geom1, geom2)
```

**Arguments**
+ `geom1` - A value of type GEOMETRY or an expression that evaluates to a GEOMETRY type.
+ `geom2` - A value of type GEOMETRY or an expression that evaluates to a GEOMETRY type. This value is compared with geom1 to determine if it is contained within geom1.

**Return type**

BOOLEAN

If geom1 or geom2 is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

**Examples**

```
RETURN ST_Contains(
    ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'), 
    ST_GeomFromText('POLYGON((-1 3,2 1,0 -3,-1 3))'));
false
```