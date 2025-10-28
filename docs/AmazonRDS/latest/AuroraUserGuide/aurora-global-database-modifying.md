# Modifying parameters for an Aurora global

database

You can configure the Aurora DB cluster parameter groups independently for each Aurora
cluster within the Aurora global database. Most parameters work the same as for other kinds
of Aurora clusters. We recommend that you keep settings consistent among all the clusters in
a global database. Doing this helps to avoid unexpected behavior changes if you promote a
secondary cluster to be the primary.

For example, use the same settings for time zones and character sets to avoid inconsistent
behavior if a different cluster takes over as the primary cluster.

The `aurora_enable_repl_bin_log_filtering` and
`aurora_enable_replica_log_compression` configuration settings have no effect.
