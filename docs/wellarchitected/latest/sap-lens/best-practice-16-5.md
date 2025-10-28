# Best Practice 16.5 – Scale to meet

performance demands

One of the primary benefits of operating workloads in AWS is the ability to increase
or decrease the compute capacity and change the storage performance characteristics to
match the performance required for the use case. For SAP workloads, use dynamic scaling
where applicable to avoid performance bottlenecks. Scenarios where dynamic scaling is not
possible, such as scaling out an SAP HANA database cluster, use a manual deployment
process.

**Suggestion 16.5.1 – Reactively scale SAP workloads**

In response to dynamic changes in workload performance requirements, scale your SAP
resources accordingly. Where possible, use automation to scale in or out, but when that is
not an option (such as scaling up a database instance), have a process in place to do so
manually. Consider:

- Adding or removing application server capacity or changing instance sizes as
  required to meet demand
- Changing SAP parameters to redistribute virtual resources programmatically
- [Modifying storage type](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md") (for example, Amazon EBS `gp3` to
  `io2` or vice versa in AWS), where applicable, to optimize storage
  performance

- AWS Documentation: [Request modifications to your EBS volumes](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md")

**Suggestion 16.5.2 – Schedule scaling for predictable SAP
workloads**

Whether in an automated or manual fashion, scaling an SAP workload up or down based on
predictable performance patterns is advisable. For instance, when month-end financial
processing on an SAP ECC system leads to a predictable 20% increase in processing
requirements on application server instances, system administrators can proactively
increase the number or size of application servers, then scale-in the number of instances
when the usage predictably decreases.
