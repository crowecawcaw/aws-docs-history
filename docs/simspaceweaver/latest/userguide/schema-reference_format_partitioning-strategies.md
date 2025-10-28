End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Partitioning strategies

The `partitioning_strategies` section (required) specifies the organization of partitions for a spatial domain.

###### Note

SimSpace Weaver only supports 1 partitioning strategy.

To specify the properties for a partitioning strategy, replace
`partitioning-strategy-name` with a name of your
choice. The name must be 3-64 characters long and can contain the characters
**A** -**Z** ,
**a** -**z** ,
**0** -**9** , and
**\_ -** (hyphen). Specify the properties of the
partitioning strategy after the name.

```
partitioning_strategies:
  `partitioning-strategy-name`:
    topology: "Grid"
    aabb_bounds:
      x: [`aabb-min-x`, `aabb-max-x`]
      y: [`aabb-min-y`, `aabb-max-y`]
    grid_placement_groups:
      x: `number-of-placement-groups-along-x-axis`
      y: `number-of-placement-groups-along-y-axis`

```

**Properties**

`topology`

Specifies the topology (partition arrangement scheme) for this partitioning strategy.

_Required:_ Yes

_Type:_ String

_Valid values:_ `"Grid"`

`aabb_bounds`

Specifies the bounds of the main axis-aligned bounding box (AABB) for
your simulation. You specify the bounds as 2-element ordered arrays that
describe the minimum and maximum values (in that order) for each axis (x
and y).

_Required:_ Conditional. This property is required
(and can only be specified) if the topology is set to `"Grid"`.

_Type:_ `Float` array (for each axis)

_Valid values:_ `-3.4028235e38`-`3.4028235e38`

`grid_placement_groups`

Specifies the number of placement groups along each axis (x and y) in
a grid topology. A placement group is a collection of partitions (in the
same domain) that are spatially adjacent.

_Required:_ Conditional. This property is required
(and can only be specified) if the topology is set to `"Grid"`.
If you don't specify a placement groups configuration, SimSpace Weaver
will calculate one for you. Any domain that uses a partitioning strategy
without a placement groups configuration must specify a `grid_partition`
(see [Spatial domain partitioning strategy](schema-reference_format_domains_spatial.md#schema-reference_format_domains_spatial_partitioning-strategy "schema-reference_format_domains_spatial.md#schema-reference_format_domains_spatial_partitioning-strategy")).

_Type:_ Integer (for each axis)

_Valid values:_ `1`-`20`. We recommend
that x \* y is equal to the desired number of workers. Otherwise, SimSpace Weaver will
attempt to balance your placement groups across the available workers.
