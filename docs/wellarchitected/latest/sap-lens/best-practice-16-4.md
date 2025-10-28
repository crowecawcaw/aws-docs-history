# Best Practice 16.4 – Identify and

triage performance issues

When key metrics indicate performance is degrading, have a process in place to
remediate the underlying cause. Using automation (see the following best practice on
dynamic scaling) can reduce the need for manual intervention, but when that is not
possible, having an automated alerting process for administrators is vital.

**Suggestion 16.4.1 – Configure performance alerts
appropriately**

Follow the guidelines as mentioned in the Well-Architected Framework Performance
Efficiency pillar regarding monitoring and alerts, and make use of SAP alerting
capabilities where they provide additional capabilities. Additional details are also
available in [Operational Excellence] [1 - Design SAP
workload to allow understanding and reaction to its state](design-principle-1.md "design-principle-1.md").

- Well-Architected Framework [Performance Efficiency]: [Monitoring](../performance-efficiency-pillar/monitoring.md "../performance-efficiency-pillar/monitoring.md")
- SAP Documentation: [SAP NetWeaver Alert Monitor](https://help.sap.com/doc/7a827019728810148a4b1a83b0e91070/1610 001/en-US/frameset.htm?frameset.htm "https://help.sap.com/doc/7a827019728810148a4b1a83b0e91070/1610 001/en-US/frameset.htm?frameset.htm")

**Suggestion 16.4.2 – Automatic remediation of performance
incidents**

While the management of performance incidents involves the best practices on
operations detailed in the Well-Architected Framework Operational Excellence pillar, the
proactive detection and automated remediation of potential performance impairment can
prevent deepening a performance problem and can improve the end-user experience. When
automated processes for mitigating a performance issue are not possible, having a detailed
runbook in place on how the operational team should respond to a performance issue can
accelerate the response to a performance incident.

- SAP Lens [Operational Excellence]: [Best
  Practice 1.8 Use automated response and recovery techniques to react to monitoring
  alerts](best-practice-1-8.md "best-practice-1-8.md")
- Well-Architected Framework [Operational Excellence]: [Best Practices: Operate](../framework/oe-operate.md "../framework/oe-operate.md")
