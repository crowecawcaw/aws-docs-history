# Persistent storage for service-managed fleets

AWS Deadline Cloud (Deadline Cloud) persistent storage attaches dedicated Amazon Elastic Block Store (Amazon EBS) gp3 volumes to
service-managed fleet workers. These volumes preserve data such as conda package installations,
application caches, and version control workspaces across worker lifecycle events. To enable
persistent storage, include the `persistentVolumeConfiguration` object in the
`serviceManagedEc2FleetConfiguration` when you call `CreateFleet` or
`UpdateFleet`, or configure it in the console when you create or edit a
fleet.

For the full documentation – how persistent storage works, when to use it,
configuration parameters and examples, runtime integration with the
`DEADLINE_PERSISTENT_MOUNT` environment variable, volume states, and
considerations – see [Persistent storage for service-managed
fleets](../userguide/volumes.md "../userguide/volumes.md") in the _AWS Deadline Cloud User Guide_.

For the API reference, see [CreateFleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md") in the
_Deadline Cloud API Reference_.
