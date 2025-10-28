# Best Practice 16.2 – Establish

baseline performance requirements

Every SAP application has unique performance requirements. Using historical monitoring
data helps SAP administration teams understand the baseline performance of these
applications, enabling them to identify and understand the extent of any performance
changes. Relevant alerts can be put in place to detect anomalies, such as unintended CPU
spikes, storage throughput deltas, memory consumption increases, and more complex
performance decrements. This monitoring data can be used to further fine-tune
performance.

**Suggestion 16.2.1 – Collect and evaluate data that reflects
SAP-specific KPIs**

This suggestion aligns closely with additional suggestions in the Well-Architected
Framework Performance Efficiency Pillar discussion regarding [resource monitoring](../performance-efficiency-pillar/monitor-your-resources-to-ensure-that-they-are-performing-as-expected.md "../performance-efficiency-pillar/monitor-your-resources-to-ensure-that-they-are-performing-as-expected.md").

In addition to this general guidance, SAP-specific KPIs include dialog response time,
buffer swaps, used memory. These KPIs might differ based on the type of SAP software and
version you are running on. Further detail on KPI and monitoring recommendations is
available in this document in the Operational Excellence pillar:

- SAP Lens [Operational Excellence]: [Best
  Practice 1.2 - Implement infrastructure monitoring for SAP](best-practice-1-2.md "best-practice-1-2.md")
- SAP Lens [Operational Excellence]: [Best
  Practice 1.3 - Implement application and database monitoring for SAP](best-practice-1-3.md "best-practice-1-3.md")
