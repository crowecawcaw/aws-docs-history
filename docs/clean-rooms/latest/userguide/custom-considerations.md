# Considerations and limitations

AWS Clean Rooms helps you and your partners analyze and collaborate on collective datasets to drive
new insights without revealing underlying data to one another. Verify that your data
collaboration configuration adheres to the privacy, security, legal, and compliance
requirements of your organization.

AWS Clean Rooms offers various privacy-enhancing controls for your data collaboration use
case:

- [Allowed analyses](custom-allowed-analyses.md "custom-allowed-analyses.md")
- [Disallowed output columns](disallowed-output-columns.md "disallowed-output-columns.md")
- [Minimum aggregation thresholds](custom-min-agg-thresholds.md "custom-min-agg-thresholds.md")
- [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md")
- [Differential privacy](custom-diff-privacy.md "custom-diff-privacy.md")
  Consider comparison controls when your table contains low-cardinality or
  quasi-identifying columns — such as postal code or age band — or when the query runner is
  not fully trusted. For more information, see [Comparison controls](custom-comparison-controls.md "custom-comparison-controls.md").

## Assumptions about potentially adversarial queries

To help you and your partners maintain the controls you need, AWS Clean Rooms makes the
following assumptions regarding privacy-enhanced data collaboration:

- Assume the query runner is trying to exfiltrate user level data
- Assume other data providers are trying to exfiltrate user level data
- Assume the query runner and other data providers are colluding to exfiltrate user
  level data

## Limitations

Note the following limitations:

- Data aggregation enforced by minimum aggregation thresholds on its own does not address
  other potential exfiltration risks such as differencing attacks. For more information, see
  [Differencing attacks](#custom-differencing-attacks "#custom-differencing-attacks").
- The SQL surface for queries using minimum aggregation thresholds is restricted. For a
  complete list of supported and unsupported SQL constructs, see [SQL capabilities for minimum aggregation and comparison controls](custom-sql-capabilities.md "custom-sql-capabilities.md").
- Minimum aggregation thresholds and comparison controls do not currently work with
  [differential privacy](custom-diff-privacy.md "custom-diff-privacy.md").
- The minimum aggregation threshold is not enforced on COUNT,
  COUNT(DISTINCT), or APPROX\_COUNT\_DISTINCT functions over a
  single table with no grouping or join.

## Differencing attacks

A differencing attack occurs when someone runs two queries that differ by a single
individual, then subtracts the results to isolate that person's data, even though each query
on its own only returns aggregates.

For example:

- Query A: SUM(salary) WHERE department = 'Sales' →
  1,000,000
- Query B: SUM(salary) WHERE department = 'Sales'
  AND name != 'Jane' → 950,000
- Difference: Jane earns 50,000.

Each query passes a minimum-group-size check (minimum aggregation threshold), but the
combination leaks one data subject's value by running multiple queries. A per-query threshold
does not address this differencing attack vector.

To reduce the risk of bulk attacks, adopt data access budgets and differential privacy
policies.
