End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Configuring spatial domains

For spatial domains, you must specify a `partitioning_strategy`. The value of this
property is the name that you gave to a partitioning strategy that you defined in
another part of the schema.

```

  MySpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-us-west-2/MySpatialApp.zip"
      launch_command: ["MySpatialApp"]
      required_resource_units:
        compute: 1

```

###### Note

SimSpace Weaver app SDK
version 1.12.x projects use separate buckets for the app .zip files
and the schema:

- weaver-`lowercase-project-name`-`account-number`-app-zips-`region`
- weaver-`lowercase-project-name`-`account-number`-schemas-`region`
  A partitioning strategy with a `Grid` topology (the only topology supported in this
  release) directs SimSpace Weaver to arrange spatial app partitions of this domain in a
  grid. The `grid_partition` property specifies the number rows and columns of the partition
  grid.

SimSpace Weaver will start 1 instance of the spatial app for each cell in the
partition grid. For example, if a spatial domain has `grid_partition` values
`x: 2` and `y: 2`, there are 2 \* 2 = 4 partitions in the
spatial domain. SimSpace Weaver will start 4 instances of the app configured in the
spatial domain and assign 1 partition to each app instance.

###### Topics

- [Resource
  requirements for spatial domains](#working-with_configuring-simulation_domains_spatial_resources "#working-with_configuring-simulation_domains_spatial_resources")
- [Multiple spatial domains](#working-with_configuring-simulation_domains_spatial_multiple "#working-with_configuring-simulation_domains_spatial_multiple")
- [Frequently asked
  questions about spatial domains](#working-with_configuring-simulation_domains_spatial_faq "#working-with_configuring-simulation_domains_spatial_faq")
- [Troubleshooting
  spatial domains](#working-with_configuring-simulation_domains_spatial_troubleshooting "#working-with_configuring-simulation_domains_spatial_troubleshooting")

## Resource

requirements for spatial domains

You can assign up to 17 compute resource units for each worker.
You specify the number of compute resource units that each spatial app uses in the `app_config`
section of your spatial domain.

###### Example schema snippet showing the compute resource units for a spatial app

```
  MySpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-artifacts-us-west-2/MySpatialApp.zip"
      launch_command: ["MySpatialApp"]
      required_resource_units:
        **compute: 1**

```

To calculate the number of compute resource units that a domain requires, multiply the
number of cells in your grid (in your `grid_partition`,
`x` \* `y`) by the number of compute resource units assigned
to the spatial apps.

For the previous example, the domain `MySpatialDomain` specifies:

- `x`: `2`
- `y`: `2`
- `compute`: `1`

The grid for `MySpatialDomain` has 2 \* 2 = 4 cells. The spatial
domain requires 4 \* 1 = 4 compute resource units.

The total number of compute resource units for all domains specified in your schema
must be less than or equal to the `desired` number of workers
multiplied by the maximum number of compute resource units for each worker (17).

## Multiple spatial domains

You can configure your simulation to use more than 1 spatial domain.
For example, you can use 1 spatial domain to control the main
actors in a simulation (such as people and cars) and a different
spatial domain to control the environment.

You can also use multiple spatial domains to assign different
resources to different parts of your simulation. For example,
if your simulation has a type of entity that has 10x more
entity instances than another type, you can create different
domains to handle each entity type and allocate more
resources for the domain with more entities.

###### Important

SimSpace Weaver versions before 1.14.0 don't support
multiple spatial domains.

###### Important

AWS SimSpace Weaver Local doesn't currently support multiple spatial domains.
For more information about SimSpace Weaver Local, see [Local development in SimSpace Weaver](working-with_local-development.md "working-with_local-development.md").

###### Important

SimSpace Weaver supports up to 5 domains for
each simulation. This includes all spatial, custom, and service domains.

### Configure

multiple spatial domains

To configure more than 1 spatial domain, add the other spatial domain
definitions as separate named sections in your schema. Each domain must
specify the `launch_apps_by_partitioning_strategy`
key. See the following example schema.

```
sdk_version: "1.14"
workers:
  MyComputeWorkers:
    type: "sim.c5.24xlarge"
    desired: 1
clock:
  tick_rate: "30"
partitioning_strategies:
  MyGridPartitioning:
    topology: Grid
    aabb_bounds:
      x: [0, 1000]
      y: [0, 1000]
domains:
  MySpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-artifacts-us-west-2/MySpatialApp.zip"
      launch_command: ["MySpatialApp"]
      required_resource_units:
        compute: 1
  MySecondSpatialDomain:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "MyGridPartitioning"
      grid_partition:
        x: 2
        y: 2
    app_config:
      package: "s3://weaver-myproject-111122223333-artifacts-us-west-2/MySpatialApp2.zip"
      launch_command: ["MySpatialApp2"]
      required_resource_units:
        compute: 1

```

### Placing

spatial domains together

In some scenarios, you might want to place partitions for a spatial domain
on workers next to partitions from another domain. This can improve performance
characteristics if those partitions create cross-domain subscriptions to each other.

Add the top level key `placement_constraints` to your schema to specify
which domains SimSpace Weaver should place together. The required `on_workers` key
must refer to a named `workers` configuration in the schema.

###### Example schema snippet showing spatial domains placed together

```
workers:
  MyComputeWorkers:
    type: "sim.c5.24xlarge"
    desired: 2
placement_constraints:
  - placed_together: ["MySpatialDomain", "MySecondSpatialDomain"]
    on_workers: ["MyComputeWorkers"]

```

###### Important

- If you use placement groups:
  - Make sure that x \* y is a multiple of the number of workers.
  - Make sure that the placement group values are common divisors for the
    grid dimensions of the domains you place together.

- If you **don't use** placement groups:

      + Make sure that 1 axis of your spatial domain grids has a common
       divisor that is equal to the number of workers.

  For more information about placement groups, see
  [Partitioning strategies](working-with_configuring-simulation_partitioning-strategies.md#working-with_configuring-simulation_partitioning-strategies_placement-groups "working-with_configuring-simulation_partitioning-strategies.md#working-with_configuring-simulation_partitioning-strategies_placement-groups").

## Frequently asked

questions about spatial domains

### Q1. How can I add

another spatial domain to an existing simulation?

- For a running simulation – You can't change the
  configuration for a running simulation. Change the domain configuration in the schema,
  upload the schema and app zips, and start a new simulation.
- For a new simulation – Add the domain
  configuration to the schema, upload the schema and app zips, and start the new
  simulation.

## Troubleshooting

spatial domains

The might get the following error when you try to start your simulation but your domain
configuration is invalid.

```
"StartError": "[{\"errorType\":\"SchemaFormatInvalid\",\"errorMessage\":
    \"We were unable to determine an arrangement of your domains that would fit
    within the provided set of workers. This can generally be resolved by
    increasing the number of workers if able, decreasing your domains\u0027
    [\u0027\u0027grid_partition\u0027\u0027] values, or adjusting the
    dimensions of your [\u0027\u0027grid_placement_groups\u0027\u0027].\"}]"
```

###### Potential causes

- The schema allocates more compute resource units for apps than are available on workers.
- SimSpace Weaver can't determine an arrangement to place domains together on workers.
  This happens when you specify multiple spatial domains but there isn't a common divisor or
  multiple between domain grids, such as between a 2x4 grid and a 3x5 grid).
