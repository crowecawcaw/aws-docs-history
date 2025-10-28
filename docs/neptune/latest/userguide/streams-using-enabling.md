# Enabling Neptune Streams

You can enable or disable Neptune Streams at any time by setting the
[neptune_streams
DB cluster parameter](parameters.md#parameters-db-cluster-parameters-neptune_streams "parameters.md#parameters-db-cluster-parameters-neptune_streams"). Setting the parameter to `1`
enables Streams, and setting it to `0` disables Streams.

###### Note

After changing the `neptune_streams` DB cluster parameter,
you must reboot all DB instances in the cluster for the change to take effect.

You can set the [neptune_streams_expiry_days](parameters.md#parameters-db-cluster-parameters-neptune_streams_expiry_days "parameters.md#parameters-db-cluster-parameters-neptune_streams_expiry_days")
DB cluster parameter to control how many days, from 1 to 90, that stream records
remain on the server before being deleted. The default is 7.

Neptune Streams was initially introduced as an experimental feature that
you enabled or disabled in Lab Mode using the DB Cluster `neptune_lab_mode`
parameter (see [Neptune Lab Mode](features-lab-mode.md "features-lab-mode.md")).
Using Lab Mode to enable Streams is now deprecated and will be disabled in the future.
