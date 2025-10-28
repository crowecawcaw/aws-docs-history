End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Partitioning strategies

The `partitioning_strategies` section specifies configuration properties for the
partitions of spatial apps. You provide your own name for a partitioning strategy (a set of
properties in this section) and use it in your spatial app configuration.

```

partitioning_strategies:
  MyGridPartitioning:
    topology: "Grid"
    aabb_bounds:
      x: [0, 1000]
      y: [0, 1000]
    grid_placement_groups:
      x: 1
      y: 1

```

The `topology` property specifies the type of coordinate system that your simulation uses.
The value `Grid` specifies a 2-dimensional (2D) grid.

For a `Grid` topology, the simulation space is modeled as an axis-aligned bounding box (AABB).
You specify the coordinate bounds for each axis of your AABB in the `aabb_bounds` property.
All entities that exist spatially in your simulation must have a position inside the AABB.

## Grid placement groups

A **placement group** is a collection of spatial app
partitions that you want SimSpace Weaver to place on the same worker. You specify the
number and arrangement of placement groups (in a grid) in the `grid_placement_groups`
property. SimSpace Weaver will attempt to evenly distribute the partitions across the
placement groups. The ownership areas of spatial apps with partitions in the same
placement group will be spatially adjacent.

We recommend that x \* y is equal to your desired number of workers. If it isn't
equal, SimSpace Weaver will attempt to balance your placement groups across the
available workers.

If you don't specify a placement group configuration, SimSpace Weaver will calculate
one for you.
