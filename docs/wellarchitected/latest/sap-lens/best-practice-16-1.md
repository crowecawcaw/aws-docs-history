# Best Practice 16.1 – Have data to

evaluate performance

To evaluate the performance of an SAP system and take action in the event performance
is suboptimal, monitoring data must be collected for compute, memory, storage, and
networking as described in the Well-Architected Framework Performance Excellence
guidelines concerning monitoring your resources. As stated in the Well-Architected
Framework Operational Excellence pillar, understanding the current state of the system,
putting in place key performance indicators, and collecting metrics in a timely manner for
diagnosis are crucial for investigating performance issues.

- Well-Architected Framework [Performance Efficiency]: [Monitor Your Resources to Ensure That They Are Performing as Expected](../performance-efficiency-pillar/monitor-your-resources-to-ensure-that-they-are-performing-as-expected.md "../performance-efficiency-pillar/monitor-your-resources-to-ensure-that-they-are-performing-as-expected.md")
- Well-Architected Framework [Operational Excellence]: [Understanding Workload Health](../operational-excellence-pillar/understanding-workload-health.md "../operational-excellence-pillar/understanding-workload-health.md")

**Suggestion 16.1.1 – Gather and store data relevant to performance
metrics**

To collect and view relevant SAP monitoring data, you should install and configure
the AWS Data Provider for SAP and set up metrics in your chosen monitoring tools that
support your SAP workload. Further details on monitoring and additional recommendations
are available in the Operational Excellence pillar.

- AWS Documentation: [AWS
  Data Provider for SAP](../../../sap/latest/general/aws-data-provider.md "../../../sap/latest/general/aws-data-provider.md")
- SAP Lens [Operational Excellence]: [Best
  Practice 1.1 - Implement prerequisites for monitoring SAP on AWS](best-practice-1-1.md "best-practice-1-1.md")
- SAP Lens [Operational Excellence]: [Best
  Practice 1.2 - Implement infrastructure monitoring for SAP](best-practice-1-2.md "best-practice-1-2.md")
- SAP Lens [Operational Excellence]: [Best
  Practice 1.3 - Implement application and database monitoring for SAP](best-practice-1-3.md "best-practice-1-3.md")
