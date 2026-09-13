

# Update a fleet configuration
<a name="smf-update-config"></a>

You can change a fleet's configuration from the Deadline Cloud console. For example, you can change the fleet's instance types and worker capabilities. You can also use the [UpdateFleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html) API operation.

An update doesn't replace running workers. Workers that are already running when you update the fleet keep their original instance type and capabilities. They keep this configuration until they scale in, and idle workers scale in when the fleet is above its minimum worker count. Deadline Cloud can schedule jobs that you submit shortly after an update on these existing workers. As a result, the new configuration might not take effect immediately.

To make sure that all workers use the new configuration, drain the fleet first:

1. Set the fleet's maximum worker count to 0.

1. Use the `ListWorkers` API operation to confirm that the fleet has no workers.

1. Restore the fleet's maximum worker count. New workers launch with the updated configuration.