# RAIRC04-BP02 Consider trade-offs between release

criteria

Consider trade-offs where meeting your criteria thresholds for one
potential harm may reduce your ability to meet the criteria for
another harm (for example, privacy as opposed to transparency).
Consider harm and benefit trade-offs where meeting the criteria for
your potential harms may also reduce your ability to meet the
criteria for your benefits. Reconsider your threshold choices to
appropriately balance the trade-offs given your use case priorities
and document trade-off decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Map competing metric relationships and potential conflicts.
   For example, create a matrix showing how stricter privacy
   requirements might limit model explainability, or how higher
   accuracy targets could impact latency performance.
2. In the context of the metric relationships you identified,
   consider the limits you would set on each competing metric.
   For example, when user privacy and model accuracy compete, you
   may opt for privacy requirements even if it means accepting
   lower accuracy within acceptable bounds.
3. Document threshold decisions and rationale. For example,
   record final thresholds, identified conflicts, and
   justification for trade-off decisions in release documentation
   for future reference and auditing.

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.9.3 Objectives for responsible use of AI
  system
