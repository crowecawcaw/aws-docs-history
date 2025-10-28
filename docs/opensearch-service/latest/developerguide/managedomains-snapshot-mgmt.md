# Automating snapshots with Snapshot

Management

You can set up a Snapshot Management (SM) policy in OpenSearch Dashboards to automate
periodic snapshot creation and deletion. SM can snapshot of a group of indices, whereas
[Index State Management](managedomains-snapshots.md#managedomains-snapshot-ism "managedomains-snapshots.md#managedomains-snapshot-ism") can only
take one snapshot per index. To use SM in OpenSearch Service, you need to register your own Amazon S3
repository. For instructions to register your repository, see [Registering a manual snapshot repository](managedomains-snapshots.md#managedomains-snapshot-registerdirectory "managedomains-snapshots.md#managedomains-snapshot-registerdirectory").

Prior to SM, OpenSearch Service offered a free, automated snapshot feature that's still turned on by
default. This feature sends snapshots into the service-maintained `cs-*`
repository. To deactivate the feature, reach out to Support.

For more information on the SM feature, see [Snapshot
management](https://opensearch.org/docs/latest/dashboards/sm-dashboards/ "https://opensearch.org/docs/latest/dashboards/sm-dashboards/") in the OpenSearch documentation.

SM doesn't currently support snapshot creation on multiple index types. For example,
if you try to create snapshot on multiple indices with `*` and some indices
are in the [warm tier](ultrawarm.md#ultrawarm-manual-snapshot "ultrawarm.md#ultrawarm-manual-snapshot"), the snapshot creation will fail. If you need your snapshot to
contain multiple index types, use the [ISM
snapshot action](https://opensearch.org/docs/latest/im-plugin/ism/policies/#snapshot "https://opensearch.org/docs/latest/im-plugin/ism/policies/#snapshot") until SM supports this option.

## Considerations

Consider the following when you configure snapshot management:

- One policy is allowed per repository.
- Up to 400 snapshots are allowed for one policy.
- This feature won't run if your domain has a red status, is under high JVM
  pressure (85% or above), or has a stuck snapshot function. When the overall
  indexing and searching performance of your cluster is impacted, SM may also
  be impacted.
- A snapshot operation only starts after the previous operation finishes, so
  that no concurrent snapshot operations are activated by one policy.
- Multiple policies with the same schedule can cause a resource spike. If
  the policies' snapshotted indices overlap, the shard-level snapshot
  operations can only run sequentially, which can cause a cascaded performance
  problem. If the policies share a repository, there will be spike of write
  operations to that repository.
- We recommend that you schedule your snapshot operations automation to no
  more than once per hour, unless you have a special use case.
