# AWS.Compute.PlacementGroup

A PlacementGroup node supports different strategies to place Amazon EC2 instances.

When you launch a new Amazon EC2instance, the Amazon EC2 service attempts to place the instance in
such a way that all of your instances are spread out across underlying hardware to minimize
correlated failures. You can use placement groups to influence the placement of a group of
interdependent instances to meet the needs of your workload.

## Syntax

```
tosca.nodes.AWS.Compute.PlacementGroup
  properties:
    strategy: String
    partition_count: Integer
    tags: List
```

## Properties

`strategy`

The strategy to use to place Amazon EC2 instances.

Required: Yes

Type: String

Possible values: CLUSTER | PARTITION | SPREAD_HOST | SPREAD_RACK

- **CLUSTER** – packs instances close
  together inside an Availability Zone. This strategy enables workloads to
  achieve the low-latency network performance necessary for tightly-coupled
  node-to-node communication that is typical of high-performance computing
  (HPC) applications.
- **PARTITION** – spreads your instances
  across logical partitions such that groups of instances in one partition
  do not share the underlying hardware with groups of instances in
  different partitions. This strategy is typically used by large
  distributed and replicated workloads, such as Hadoop, Cassandra, and
  Kafka.
- **SPREAD_RACK** – places a small group of
  instances across distinct underlying hardware to reduce correlated
  failures.
- **SPREAD_HOST** – used only with Outpost
  placement groups. Places a small group of instances across distinct
  underlying hardware to reduce correlated failures.

`partition_count`

The number of partitions.

Required: Required only when `strategy` is set to
`PARTITION`.

Type: Integer

Possible values: 1 | 2 |3 | 4 | 5 | 6 | 7

`tags`

The tags that you can attach to the placement group resource.

Required: No

Type: List

## Example

```
ExamplePlacementGroup:
  type: tosca.nodes.AWS.Compute.PlacementGroup
  properties:
    strategy: `"PARTITION"`
    partition_count: `5`
    tags:
      - tag_key=`tag_value`
```
