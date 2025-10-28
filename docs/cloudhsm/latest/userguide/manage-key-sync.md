# Key synchronization and durability settings in AWS CloudHSM

AWS CloudHSM synchronizes every token key you create. Key synchronization is mostly an automatic
process, but you can use a minimum of two hardware security modules (HSM) in your cluster to
make keys more durable. This topic describes key synchronization settings, common issues
customers face working with keys on a cluster, and strategies for making keys more
durable.

This topic describes key synchronization settings in AWS CloudHSM, common issues customers face
working with keys on a cluster, and strategies for making keys more durable.

###### Topics

- [Concepts](concepts-key-sync.md "concepts-key-sync.md")
- [Understanding key
  synchronization](understand-key-sync.md "understand-key-sync.md")
- [Change client key durability
  settings](working-client-sync.md "working-client-sync.md")
- [Synchronizing keys across cloned clusters](cli-sync.md "cli-sync.md")
