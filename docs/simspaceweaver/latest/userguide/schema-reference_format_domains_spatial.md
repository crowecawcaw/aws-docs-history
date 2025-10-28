End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Spatial domain configuration

To specify the properties for a spatial domain, replace `spatial-domain-name`
with a name of your choice. The name must be 3-64 characters long and can
contain the characters **A** -**Z** , **a** -**z** , **0** -**9** , and **\_ -** (hyphen). Specify
the properties of the spatial domain after the name.

```
  `spatial-domain-name`:
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "`partitioning-strategy-name`"
      grid_partition:
        x: `number-of-partitions-along-x-axis`
        y: `number-of-partitions-along-y-axis`
    app_config:
      package: "`app-package-s3-uri`"
      launch_command: ["`app-launch-command`"`, "parameter1", ...`]
      required_resource_units:
        compute: `app-resource-units`
    image: "`ecr-repository-uri`"

```

## Spatial domain partitioning strategy

The `launch_apps_by_partitioning_strategy` section (required) specifies the
partitioning strategy and dimensions (in number of partitions) of the
simulation space.

```
    launch_apps_by_partitioning_strategy:
      partitioning_strategy: "`partitioning-strategy-name`"
      grid_partition:
        x: `number-of-partitions-along-x-axis`
        y: `number-of-partitions-along-y-axis`

```

**Properties**

`partitioning_strategy`

Specifies the partitioning strategy for this spatial domain.

_Required:_ Yes

_Type:_ String

_Valid values:_
The value of this property must match the name of a
partitioning strategy defined in the `partitioning_strategies`
section. For more information, see [Partitioning strategies](schema-reference_format_partitioning-strategies.md "schema-reference_format_partitioning-strategies.md").

`grid_partition`

Specifies the number of partitions along each axis (x and y)
in a grid topology. These dimensions describe the total
simulation space for this domain.

_Required:_ Conditional. This property can
only be specified if the topology is set to `"Grid"`. This
property depends on the `grid_placement_groups` property of the
specified partitioning strategy for this domain:

- This property is required if this domain's partitioning strategy doesn't specify a
  `grid_placement_groups` configuration.
- If there is a `grid_placement_groups` configuration but you don't specify `grid_partition` , then
  SimSpace Weaver will use the same dimensions as the
  `grid_placment_groups` configuration.
- If you specify both `grid_placement_groups` and `grid_partition` , the dimensions of
  `grid_partition` must be multiples of the dimensions of
  `grid_placement_groups` (for example, if your
  `grid_placement_groups` dimensions are 2x2, then some
  valid dimensions for `grid_partition` are 2x2, 4x4, 6x6,
  8x8, 10x10).

_Type:_ Integer (for each axis)

_Valid values:_ `1`-`20`

## Spatial app configuration

The `app_config` section (required) specifies the package, launch
configuration, and resource requirements for apps in this domain.

```

    app_config:
      package: "`app-package-s3-uri`"
      launch_command: ["`app-launch-command`"`, "parameter1", ...`]
      required_resource_units:
        compute: `app-resource-units`

```

**Properties**

`package`

Specifies the package (zip file) that contains the app
executable/binary. The package must be stored in an Amazon S3 bucket.
Only zip file format is supported.

_Required:_ Yes

_Type:_ String

_Valid values:_ The Amazon S3 URI of the package in
an Amazon S3 bucket. For example, `s3://weaver-myproject-111122223333-app-zips-us-west-2/MySpatialApp.zip`.

`launch_command`

Specifies the executable/binary file name and command-line
parameters to launch the app. Each command-line string token is
an element in the array.

_Required:_ Yes

_Type:_ String array

`required_resource_units`

Specifies the number of resource units that
SimSpace Weaver should allocate to each instance of this app. A
_resource unit_ is a
fixed amount of virtual central processing units (vCPUs) and
random-access memory (RAM) on a worker. For more information
about resource units, see [Endpoints and service quotas](service-quotas.md "service-quotas.md").
The `compute` property specifies a resource unit allocation
for the `compute` family of workers, and is currently the only
valid type of allocation.

_Required:_ Yes

_Type:_ Integer

_Valid values:_ `1`-`4`

## Custom container image

The `image` property (optional) specifies the location of a container image
that SimSpace Weaver uses to run apps in this domain (not supported in versions `1.13` and
`1.12`). Provide the URI to a repository in
Amazon Elastic Container Registry (Amazon ECR) that contains the image. If this property isn't specified but
the `default_image` is specified in the top level `simulation_properties`
section, apps in this domain use the `default_image`. For more information, see
[Custom containers](working-with_custom-containers.md "working-with_custom-containers.md").

```
    image: "`ecr-repository-uri`"
```

**Properties**

`image`

Specifies the location of a container image to run apps in this domain.

_Required:_ No

_Type:_ String

_Valid values:_

- The URI of a repository in Amazon Elastic Container Registry (Amazon ECR) (for example,
  `111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest`)
