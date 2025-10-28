# Best Practice 17.5 – Consider using

on-demand capacity to improve cost efficiency

The on-demand pricing model is suitable for SAP workloads needing reduced operating
hours, short-term projects, experimentation, or expanded capacity for small periods of
time (for example, performance testing). Determine where you can use on-demand pricing in
your SAP architecture.

**Suggestion 17.5.1 – Evaluate the use of on-demand for SAP systems
needing less than 24/7 operating hours**

Based on the break-even point between the use of on-demand and other pricing models.
(See [Reliability]: [Best Practice 18.1 - Understand the
payment and commitment options available for Amazon EC2](best-practice-18-1.md "best-practice-18-1.md") ), evaluate if on-demand
will provide the lowest cost. As part of this evaluation, consider the overall Savings Plan
commitment.

Common use cases include non-production systems that are not needed outside of
extended business hours or short-term business experiments, such as trial upgrades and
proofs of concept (POCs).

- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
  Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/ "https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/")

**Suggestion 17.5.2 - Evaluate scheduled or dynamic scaling options
for peak loads**

On-demand capacity is commonly used in SAP workloads for peaks where capacity
requirements spike for a short period of time. Consider the following:

- Use schedule-based SAP application server scaling for known usage pattern peaks
  such as period, month-end, year-end, or seasonal peaks.
- Use dynamic scaling of the application tier where peaks are less certain and need
  to be scaled based on real-time user load. Explore mechanisms which are SAP-aware and
  provide the required governance and controls.

**Note:** When evaluating dynamic scaling of the application
tier, consider the impact on user connections and batch jobs if an SAP application server
is shut down due to the stateful nature of SAP components. AWS, SAP, and APN
partner-developed tools can help address this requirement.

- AWS Documentation: [Systems Manager Automation actions reference](../../../systems-manager/latest/userguide/automation-actions.md "../../../systems-manager/latest/userguide/automation-actions.md")
- SAP Documentation: [SAP Landscape
  Management](https://www.sap.com/products/landscape-management.html "https://www.sap.com/products/landscape-management.html")
- SAP on AWS Blog: [Using AWS to enable SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/ "https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/")
