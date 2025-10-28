# Limitations / Callouts

- ODP entities are not compatible with Record Based Partitioning since pagination is handled using skip token/delta token. Consequently, for Record Based Partitioning, the default value for maxConcurrency is set to "null" irrespective of the user input.
- When both limit and partition is applied, the limit takes precedence over partitioning.
