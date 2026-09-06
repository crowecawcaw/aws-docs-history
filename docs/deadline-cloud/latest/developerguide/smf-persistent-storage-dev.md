

# Persistent storage for service-managed fleets
<a name="smf-persistent-storage-dev"></a>

AWS Deadline Cloud (Deadline Cloud) persistent storage attaches dedicated Amazon Elastic Block Store (Amazon EBS) gp3 volumes to service-managed fleet workers. These volumes preserve data such as conda package installations, application caches, and version control workspaces across worker lifecycle events. To enable persistent storage, include the `persistentVolumeConfiguration` object in the `serviceManagedEc2FleetConfiguration` when you call `CreateFleet` or `UpdateFleet`, or configure it in the console when you create or edit a fleet.

For the full documentation – how persistent storage works, when to use it, configuration parameters and examples, runtime integration with the `DEADLINE_PERSISTENT_MOUNT` environment variable, volume states, and considerations – see [Persistent storage for service-managed fleets](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/volumes.html) in the *AWS Deadline Cloud User Guide*.

For the API reference, see [CreateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFleet.html) in the *Deadline Cloud API Reference*.