End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Interacting with the app SDK at the top level

###### Lifecycle

- The SimSpace Weaver app SDK manages app life cycle. You don't need to read or write the
  lifecycle state of an app.

###### Partitions

- Use `Result <PartitionSet> AssignedPartitions(Transaction& txn);`
  to get owned partitions.
- Use `Result <PartitionSet> AllPartitions(Transaction& txn);` to get
  all partitions in the simulation.
