# Use fault isolation to protect

your workload

Fault isolation limits the impact of a component or system failure to a defined boundary. With proper isolation, components outside of the boundary are unaffected by the failure. Running your workload across multiple fault isolation boundaries can make it more resilient to failure.

###### Best practices

- [REL10-BP01 Deploy the workload to multiple locations](rel_fault_isolation_multiaz_region_system.md "rel_fault_isolation_multiaz_region_system.md")
- [REL10-BP02 Automate recovery for components constrained to a
  single location](rel_fault_isolation_single_az_system.md "rel_fault_isolation_single_az_system.md")
- [REL10-BP03 Use bulkhead architectures to limit scope of
  impact](rel_fault_isolation_use_bulkhead.md "rel_fault_isolation_use_bulkhead.md")
