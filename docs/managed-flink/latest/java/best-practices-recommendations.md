Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# General best practices and

recommendations for application upgrades

- Test the new job/runtime without state on a non-production environment before
  attempting a production upgrade.
- Consider testing the stateful upgrade with a non-production application
  first.
- Make sure that your new job graph has a compatible state with the snapshot
  you will be using to start your upgraded application.
  - Make sure that the types stored in operator states stay the same. If
    the type has changed, Apache Flink can't restore the operator
    state.
  - Make sure that the Operator IDs you set using the `uid`
    method remain the same. Apache Flink has a strong recommendation for
    assigning unique IDs to operators. For more information, see [Assigning Operator IDs](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#assigning-operator-ids "https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#assigning-operator-ids") in the Apache Flink
    documentation.

  If you don't assign IDs to your operators, Flink automatically
  generates them. In that case, they might depend on the program structure
  and, if changed, can cause compatibility issues. Flink uses Operator IDs
  to match state in snapshot to operator. Changing Operator IDs results in
  the application not starting, or state stored in the snapshot being
  dropped, and the new operator starting without state.
  - Don't change the key used to store the keyed state.
  - Don't modify the input type of stateful operators like window or join.
    This implicitly changes the type of the internal state of the operator,
    causing a state incompatibility.
