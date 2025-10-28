End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Schema format

The following example shows the overall structure of a schema. The order of properties
at each level of the schema doesn't matter, as long as the parent-child relationships
are the same. The order matters for elements in an array.

```
sdk_version: "`sdk-version-number`"
simulation_properties:
  `simulation-properties`
workers:
  `worker-group-configurations`
clock:
  tick_rate: `tick-rate`
partitioning_strategies:
  `partitioning-strategy-configurations`
domains:
  `domain-configurations`
placement_constraints:
  `placement-constraints-configuration`

```

###### Sections

- [SDK version](schema-reference_format_sdk-version.md "schema-reference_format_sdk-version.md")
- [Simulation properties](schema-reference_format_simulation-properties.md "schema-reference_format_simulation-properties.md")
- [Workers](schema-reference_format_workers.md "schema-reference_format_workers.md")
- [Clock](schema-reference_format_clock.md "schema-reference_format_clock.md")
- [Partitioning strategies](schema-reference_format_partitioning-strategies.md "schema-reference_format_partitioning-strategies.md")
- [Domains](schema-reference_format_domains.md "schema-reference_format_domains.md")
- [Placement constraints](schema-reference_format_placement-constraints.md "schema-reference_format_placement-constraints.md")
