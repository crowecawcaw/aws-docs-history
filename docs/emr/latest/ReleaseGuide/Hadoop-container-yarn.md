# YARN container bin packing

Starting with Amazon EMR version 7.9.0, container bin-packing policy is now available for the YARN capacity scheduler, which is built on top
of YARN's multi-node placement policy. Although the feature is disabled by default, when activated, YARN prioritizes filling up a single
node with containers before expanding to other cluster nodes, while respecting a predefined packing threshold defined by the
configuration `yarn.scheduler.capacity.multi-node-placement.container.bin-packing.percentage`.

The container bin-packing policy offers several benefits as compared to the default uniform container allocation strategy:

- It Reduces cluster resource fragmentation.
- It potentially accelerates cluster scale-down operations by launching containers on limited number of nodes when
  there is available resources on those nodes, hence leaving other nodes idle, which can then be scaled down – thus leading to better cost savings for dynamically scaling a cluster.

## Enable the feature

To enable the container bin-packing feature in Amazon EMR, you can add the following YARN site classification:

```
[
	{
		"Classification": "yarn-site",
		"Properties": {
		"yarn.scheduler.capacity.multi-node-placement.container.bin-packing.percentage": "`integer value from 1-100`"
		}
	}
]
```

## Considerations

- The feature is exclusively available for the YARN capacity-scheduler.
- Enabling the feature automatically activates YARN multi-node placement scheduling strategy.
- There can be potential performance degradation due to concentrated resource utilization on a limited number of nodes.
- With this feature, custom auto-scaling policies demonstrate better scale-down operations, compared to managed scaling policy.
