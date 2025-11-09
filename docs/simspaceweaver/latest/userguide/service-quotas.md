End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# SimSpace Weaver endpoints and quotas

The following tables describe the service endpoints and service quotas for SimSpace Weaver. Service quotas, also
referred to as _limits_, are the maximum number of service resources or operations for your
AWS account. For more information, see
[AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
in the _AWS General Reference_.

## Service endpoints

| Region name              | Region         | Endpoint                                    | Protocol |
| ------------------------ | -------------- | ------------------------------------------- | -------- |
| US East (N. Virginia)    | us-east-1      | simspaceweaver.us-east-1.amazonaws.com      | HTTPS    |
| US East (Ohio)           | us-east-2      | simspaceweaver.us-east-2.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | simspaceweaver.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | simspaceweaver.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | simspaceweaver.ap-southeast-2.amazonaws.com | HTTPS    |
| Europe (Stockholm)       | eu-north-1     | simspaceweaver.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | simspaceweaver.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | simspaceweaver.eu-west-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)   | us-gov-east-1  | simspaceweaver.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | simspaceweaver.us-gov-west-1.amazonaws.com  | HTTPS    |

## Service quotas

| Name                                                | Default                            | Adjustable                                                                                                                                                                                       | Description                                                                                                                                                                                                                                   |
| --------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compute resource units for each app                 | Each supported Region: 4           | No                                                                                                                                                                                               | The maximum number of compute resource units that you can allocate to each app.                                                                                                                                                               |
| Compute resource units for each worker              | Each supported Region: 17          | No                                                                                                                                                                                               | The number of compute resource units available for each worker.                                                                                                                                                                               |
| Data fields for each entity                         | Each supported Region: 7           | No                                                                                                                                                                                               | The maximum number of data (non-index) fields that an entity can have.                                                                                                                                                                        |
| Entities in a partition                             | Each supported Region: 8,192       | No                                                                                                                                                                                               | The maximum number of entities in 1 partition.                                                                                                                                                                                                |
| Entity data field size                              | Each supported Region: 1,024 Bytes | No                                                                                                                                                                                               | The maximum size of a data (non-index) field of an entity.                                                                                                                                                                                    |
| Entity transfers between workers                    | Each supported Region: 25          | No                                                                                                                                                                                               | The maximum number of entity transfers between workers, for each partition and each tick.                                                                                                                                                     |
| Entity transfers on the same worker                 | Each supported Region: 500         | No                                                                                                                                                                                               | The maximum number of entity transfers on the same worker, for each partition and each tick.                                                                                                                                                  |
| Index fields for each entity                        | Each supported Region: 1           | No                                                                                                                                                                                               | The maximum number of index fields that an entity can have.                                                                                                                                                                                   |
| Largest maximum duration (in days) for a simulation | Each supported Region: 14          | No                                                                                                                                                                                               | The largest number of days that you can specify as the maximum duration for a simulation. All simulations have a maximum duration, even if you dont specify the value. A simulation automatically stops when it reaches its maximum duration. |
| Memory for each compute resource unit               | Each supported Region: 1 Gigabytes | No                                                                                                                                                                                               | The amount of random-access memory (RAM) that an app gets for each compute resource unit.                                                                                                                                                     |
| Remote subscriptions for each worker                | Each supported Region: 24          | No                                                                                                                                                                                               | The maximum number of remote subscriptions for each worker.                                                                                                                                                                                   |
| Simulation count                                    | Each supported Region: 2           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/simspaceweaver/quotas/L-7688C21B "https://console.aws.amazon.com/servicequotas/home/services/simspaceweaver/quotas/L-7688C21B") | The maximum number of simulations with a target status of STARTED in your account. You can request a quota increase up to 10.                                                                                                                 |
| Workers for a simulation                            | Each supported Region: 2           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/simspaceweaver/quotas/L-A8C6832C "https://console.aws.amazon.com/servicequotas/home/services/simspaceweaver/quotas/L-A8C6832C") | The maximum number of workers that you can assign to 1 simulation. You can request a quota increase up to 10.                                                                                                                                 |
| vCPUs for each compute resource unit                | Each supported Region: 2           | No                                                                                                                                                                                               | The number of virtual central processing units (vCPUs) that an app gets for each compute resource unit.                                                                                                                                       |

## Messaging quotas

The following quotas apply to app to app messaging for
SimSpace Weaver Local and in the AWS Cloud.

| Name                      | Default                          | Adjustable | Description                                                     |
| ------------------------- | -------------------------------- | ---------- | --------------------------------------------------------------- |
| Maximum message size      | Each supported Region: 256 bytes | No         | The maximum size of a message payload.                          |
| Maximum message send rate | Each supported Region: 128       | No         | The maximum number of messages that each app can send per tick. |

## Clock rates

The simulation schema specifies the _clock rate_ (also called the
_tick rate_) for a simulation. The following table
specifies the valid clock rates that you can use.

| Name                                | Valid values                                         | Description                             |
| ----------------------------------- | ---------------------------------------------------- | --------------------------------------- |
| Clock rate                          | Each supported Region: "10", "15", "30", "unlimited" | The valid clock rates for a simulation. |
| Clock rate (versions 1.13 and 1.12) | Each supported Region: 10, 15, 30                    | The valid clock rates for a simulation. |

## Service quotas for SimSpace Weaver Local

The following service quotas apply to SimSpace Weaver Local only. All
other quotas also apply to SimSpace Weaver Local.

| Name                   | Default                           | Adjustable | Description                                                         |
| ---------------------- | --------------------------------- | ---------- | ------------------------------------------------------------------- |
| Maximum partitions     | SimSpace Weaver Local: 24         | No         | The maximum number of partitions for a simulation.                  |
| Maximum apps           | SimSpace Weaver Local: 24         | No         | The maximum total number of apps (of any type) for a simulation.    |
| Maximum domains        | SimSpace Weaver Local: 24         | No         | The maximum total number of domains (of any type) for a simulation. |
| Entities per partition | SimSpace Weaver Local: 4,096      | No         | The maximum number of entities in each partition.                   |
| Fields per entity      | SimSpace Weaver Local: 8          | No         | The maximum number of fields for each entity.                       |
| Field size             | SimSpace Weaver Local: 1024 bytes | No         | The maximum size of an entity field.                                |
