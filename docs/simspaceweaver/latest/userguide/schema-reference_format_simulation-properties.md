End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Simulation properties

The `simulation_properties` section (required) specifies various properties of your
simulation. Use this section to configure logging and specify a default container image. This section
is required even if you don't configure logging or choose to specify a default container image.

```
simulation_properties:
  log_destination_resource_name: "`log-destination-resource-name`"
  log_destination_service: "`log-destination-service`"
  default_entity_index_key_type: "Vector3<f32>"
  default_image: "`ecr-repository-uri`"

```

**Properties**

`log_destination_resource_name`

Specifies the resource that SimSpace Weaver will write logs to.

_Required:_ No. If this property isn't included,
SimSpace Weaver won't write logs for the simulation.

_Type:_ String

_Valid values:_

- The name of an CloudWatch Logs log group (for example, `MySimulationLogs`)
- The Amazon Resource Name (ARN) of a CloudWatch Logs log group (for example,
  `arn:aws:logs:us-west-2:111122223333:log-group/MySimulationLogs`)

###### Note

SimSpace Weaver only supports a log destination in the same account and AWS Region as the simulation.

`log_destination_service`

Indicates the type of logging destination resource when you specify a
`logging_destination resource_name` that isn't an ARN.

_Required:_ You must specify this property if the
`log_destination_resource_name` is specified and isn't an ARN. You can't
specify this property if the `log_destination_resource_name` isn't
specified or is an ARN.

_Type:_ String

_Valid values:_

- `logs`: The log destination resource is a log group.

`default_entity_index_key_type`

Specifies the data type for the index key field of simulation entities.

_Required:_ Yes

_Type:_ String

_Valid values:_ `Vector3<f32>`

`default_image`

Specifies the default container image for your simulation (not supported
for version `1.13` and `1.12`). If this property is
specified, domains that don't specify an `image` use the
`default_image`.

_Required:_ No

_Type:_ String

_Valid values:_

- The URI of a repository in Amazon Elastic Container Registry (Amazon ECR) (for example,
  `111122223333.dkr.ecr.us-west-2.amazonaws.com/my-ecr-repository:latest`)
