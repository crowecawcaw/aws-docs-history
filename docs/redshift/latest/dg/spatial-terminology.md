Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Terminology for Amazon Redshift spatial data

The following terms are used to describe some Amazon Redshift spatial functions.

## Bounding box

A bounding box of a geometry or geography is defined as the cross product (across dimensions) of the extents of the coordinates of all points in the geometry or geography.
For two-dimensional geometries, the bounding box is a rectangle that completely includes all points in the geometry.
For example, a bounding box of the polygon `POLYGON((0 0,1 0,0 2,0 0))` is the rectangle that is defined by the points (0, 0) and (1, 2)
as its bottom-left and top-right corners.
Amazon Redshift precomputes and stores a bounding box inside a geometry to speed up geometric predicates and spatial joins.
For example if the bounding boxes of two geometries don't intersect, then these two geometries can't intersect,
and they can't be in the result set of a spatial join using the ST_Intersects predicate.

You can use spatial functions to add ([AddBBox](AddBBox-function.md "AddBBox-function.md")), drop ([DropBBox](DropBBox-function.md "DropBBox-function.md")), and determine support ([SupportsBBox](SupportsBBox-function.md "SupportsBBox-function.md")) for a
bounding box.
Amazon Redshift supports the precomputaton of bounding boxes for all geometry subtypes.

The following example shows how to update existing geometries in a table to store them with a bounding box.
If your cluster is at cluster version 1.0.26809 or later, then all new geometries are created with a precomputed bounding box by default.

```
UPDATE my_table SET geom = AddBBox(geom) WHERE SupportsBBox(geom) = false;
```

After you update existing geometries, we recommend you run the VACUUM command on the updated table. For more information, see
[VACUUM](r_VACUUM_command.md "r_VACUUM_command.md").

To set whether geometries are encoded with a bounding box during a session, see [default_geometry_encoding](r_default_geometry_encoding.md "r_default_geometry_encoding.md").

## Geometric validity

Geometric algorithms used by Amazon Redshift assume that the input geometry is a valid geometry. If
an input to an algorithm is not valid, then the result is undefined. The following
section describes the geometric validity definitions used by Amazon Redshift for each geometry
subtype.

Point

A point is considered to be valid if one of the following conditions is true:

- The point is the empty point.
- All point coordinates are finite floating point numbers.

A point can be the empty point.

Linestring

A linestring is considered to be valid if any of the following conditions are
true:

- The linestring is empty; that is, it contains no points.
- All points in a nonempty linestring have coordinates that are finite floating point numbers.
- The linestring, if not empty, must be one-dimensional; that is, it can't degenerate to a
  point.

A linestring can't contain empty points.

A linestring can have duplicate consecutive points.

A linestring can have self-intersections.

Polygon

A polygon is considered to be valid if any of the following conditions are true:

- The polygon is empty; that is, it contains no rings.
- If not empty, a polygon is valid if all of the following conditions are true:
  - All rings of the polygon are valid. A ring is considered to be valid if all the following
    conditions are true:
    - All points of the ring have coordinates that are finite floating point numbers.
    - The ring is closed; that is, its first point and its last point coincide.
    - The ring doesn't have any self-intersections.
    - The ring is two-dimensional.

  - The rings of the polygon must have consistent orientations. That is, if you traverse any ring, the
    interior of the polygon is either to your right or to your left.
  - All interior rings must be within the exterior ring of the polygon.
  - All interior rings must have the same orientation, and it must be the opposite orientation of the exterior ring.
  - Interior rings can't be nested; that is, an interior ring can't be within another interior
    ring.
  - Interior and exterior rings can only intersect at a finite number of points.
  - The interior of the polygon must be simply connected.

A polygon can't contain empty points.

Multipoint

A multipoint is considered to be valid if any of the following conditions are true:

- The multipoint is empty; that is, it contains no points.
- A multipoint is not empty, and all points are valid according to the point validity definition.

A multipoint can contain one or more empty points.

A multipoint can have duplicate points.

Multilinestring

A multilinestring is considered to be valid if any of the following conditions are true:

- The multilinestring is empty; that is, it contains no linestrings.
- All linestrings in a nonempty multilinestring are valid according to the linestring validity
  definition.

A nonempty multilinestring that consists of only empty linestrings is
considered to be valid.

An empty linestring in a multilinestring doesn't affect its validity.

A multilinestring can have linestrings with duplicate consecutive points.

A multilinestring can have self-intersections.

A multilinestring can't contain empty points.

Multipolygon

A multipolygon is considered to be valid if any of the following conditions are true:

- The multipolygon doesn't contain any polygons (it is empty).
- The multipolygon is not empty and all of the following are true:
  - All polygons in the multipolygon are valid.
  - No two polygons in the multipolygon can intersect at an infinite number of points. In
    particular, this implies that the interior of any two polygons
    can't intersect and that they can only touch at a finite number of
    points.

An empty polygon in a multipolygon doesn't invalidate a multipolygon.

A multipolygon can't contain empty points.

Geometry collection

A geometry collection is considered to be valid if any of the following conditions are true:

- The geometry collection is empty; that is, it doesn't contain any geometries.
- All geometries in a nonempty geometry collection are valid.

This definition still applies, although in a recursive manner, for nested geometry collections.

A geometry collection can contain empty points and multipoints with empty points.

## Geometric simplicity

Geometric algorithms used by Amazon Redshift assume that the input geometry is a valid geometry.
If an input to an algorithm is not valid, then the simplicity check is undefined. The
following section describes the geometric simplicity definitions used by Amazon Redshift for each
geometry subtype.

Point

A valid point is considered to be simple if any of the following conditions are true:

- A valid point is always considered to be simple.
- An empty point is considered to be simple.

Linestring

A valid linestring is considered to be simple if any of the following conditions are true:

- The linestring is empty.
- The linestring is not empty and all of the following conditions are true:
  - It has no duplicate consecutive points.
  - It has no self-intersections, except possibly for its first point and last point, which can
    coincide. In other words, the linestring can't have
    self-intersections except at boundary points.

Polygon

A valid polygon is considered to be simple if it doesn't contain any
duplicate consecutive points.

Multipoint

A valid multipoint is considered to be simple if any of the following conditions are true:

- The multipoint is empty; that is, it contains no points.
- No two nonempty points of the multipoint coincide.

Multilinestring

A valid multilinestring is considered to be simple if any of the following conditions are true:

- The multilinestring is empty.
- The multilinestring is nonempty and all of the following conditions are true:
  - All its linestrings are simple.
  - Any two linestrings of the multilinestring don't intersect, except at points that are boundary
    points of the two linestrings.

A nonempty multilinestring that consists of empty linestrings only is
considered to be empty.

An empty linestring in a multilinestring doesn't affect its simplicity.

A closed linestring in a multilinestring can't intersect with any other linestring in the multilinestring.

A multilinestring can't have linestrings with duplicate consecutive
points.

Multipolygon

A valid multipolygon is considered to be simple if it doesn't contain
any duplicate consecutive points.

Geometry collection

A valid geometry collection is considered to be simple if any of the following conditions are true:

- The geometry collection is empty; that is, it doesn't contain any geometries.
- All geometries in a nonempty geometry collection are simple.

This definition still applies, although in a recursive manner, for nested geometry collections.

## H3

H3 is a hierarchical geospatial indexing grid system, which offers a way to index spatial coordinates down to square meter resolution.
Indexed data can be joined across disparate datasets and aggregated at different levels of precision.
H3 enables a range of algorithms and optimizations based on the grid, including nearest neighbors, shortest path, gradient smoothing, and more.
H3 indexes refer to cells that can be either hexagons or pentagons.
The space is subdivided hierarchically given a resolution.
H3 supports 16 resolutions from 0–15, inclusive.
With `0` being the coarsest and `15` being the finest.

Amazon Redshift provides the following H3 spatial functions:

- [H3_Boundary](H3_Boundary-function.md "H3_Boundary-function.md")
- [H3_Center](H3_Center-function.md "H3_Center-function.md")
- [H3_FromLongLat](H3_FromLongLat-function.md "H3_FromLongLat-function.md")
- [H3_FromPoint](H3_FromPoint-function.md "H3_FromPoint-function.md")
- [H3_IsValid](H3_IsValid-function.md "H3_IsValid-function.md")
- [H3_Polyfill](H3_Polyfill-function.md "H3_Polyfill-function.md")
- [H3_Resolution](H3_Resolution-function.md "H3_Resolution-function.md")
- [H3_ToChildren](H3_ToChildren-function.md "H3_ToChildren-function.md")
- [H3_ToParent](H3_ToParent-function.md "H3_ToParent-function.md")
