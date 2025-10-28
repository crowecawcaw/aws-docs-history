# Taking manual snapshots

Snapshots are not instantaneous. They take time to complete and don't represent
perfect point-in-time views of the cluster. While a snapshot is in progress, you can
still index documents and make other requests to the cluster, but new documents and
updates to existing documents generally aren't included in the snapshot. The snapshot
includes primary shards as they existed when OpenSearch initiated the snapshot. Depending
on the size of your snapshot thread pool, different shards might be included in the
snapshot at slightly different times. For snapshot best practices, see [Improve snapshot performance](bp.md#bp-stability-snapshots "bp.md#bp-stability-snapshots").

## Snapshot storage and

performance

OpenSearch snapshots are incremental, meaning they only store data that changed
since the last successful snapshot. This incremental nature means the difference in
disk usage between frequent and infrequent snapshots is often minimal. In other
words, taking hourly snapshots for a week (for a total of 168 snapshots) might not
use much more disk space than taking a single snapshot at the end of the week. Also,
the more frequently you take snapshots, the less time they take to complete. For
example, daily snapshots can take 20-30 minutes to complete, whereas hourly
snapshots might complete within a few minutes. Some OpenSearch users take snapshots
as often as every half hour.

## Take a snapshot

You specify the following information when you create a snapshot:

- The name of your snapshot repository
- A name for the snapshot

The examples in this chapter use [curl](https://curl.haxx.se/ "https://curl.haxx.se/"),
a common HTTP client, for convenience and brevity. To pass a username and password
to your curl request, see the [Getting started
tutorial](gsg.md "gsg.md").

If your access policies specify users or roles, you must sign your snapshot
requests. For curl, you can use the [`--aws-sigv4`
option](https://curl.se/docs/manpage.html#--aws-sigv4 "https://curl.se/docs/manpage.html#--aws-sigv4") with version 7.75.0 or later. You can also use the commented-out
examples in the [sample Python
client](managedomains-snapshot-registerdirectory.md#managedomains-snapshot-client-python "managedomains-snapshot-registerdirectory.md#managedomains-snapshot-client-python") to make signed HTTP requests to the same endpoints that the curl
commands use.

To take a manual snapshot, perform the following steps:

1. You can't take a snapshot if one is currently in progress. To check, run
   the following command:

```
curl -XGET '`domain-endpoint`/_snapshot/_status'
```

2. Run the following command to take a manual snapshot:

```
curl -XPUT '`domain-endpoint`/_snapshot/`repository-name`/`snapshot-name`'
```

To include or exclude certain indexes and specify other settings, add a
request body. For the request structure, see [Take snapshots](https://opensearch.org/docs/1.1/opensearch/snapshot-restore/#take-snapshots "https://opensearch.org/docs/1.1/opensearch/snapshot-restore/#take-snapshots") in the OpenSearch documentation.

###### Note

The time required to take a snapshot increases with the size of the OpenSearch Service
domain. Long-running snapshot operations sometimes encounter the following
error: `504 GATEWAY_TIMEOUT`. You can typically ignore these errors
and wait for the operation to complete successfully. Run the following command
to verify the state of all snapshots of your domain:

```
curl -XGET '`domain-endpoint`/_snapshot/`repository-name`/_all?pretty'
```
