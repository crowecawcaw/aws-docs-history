# Best Practice 21.3 - Implement sustainability

monitoring for infrastructure and SAP

Monitoring and reporting on the sustainability of SAP workloads in the AWS Cloud
provides a crucial feedback mechanism. Such monitors indicate how suggestions you’ve
implemented translate into quantifiable changes over time. This data also feeds into the
sustainability reporting that will be delivered to shareholders, regulators, and
sustainability-minded customers. Reports using the metrics discussed in [BP 21.1](best-practice-21.md "best-practice-21.md") (for example, cost and usage as proxy metrics)
can demonstrate improvements made in the operational sustainability of your SAP landscape.
This can demonstrate that you are successfully achieving the goals set by your overall
corporate sustainability strategy.

- Well-Architected Framework [Sustainability]: [Optimize areas of code that consume the most time or resources](../sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.md "../sustainability-pillar/optimize-areas-of-code-that-consume-the-most-time-or-resources.md")
  **Suggestion 21.3.1 - Develop sustainability-centric monitoring and
  reporting**

Monitoring is vital to understanding the impact of changes applied to your SAP
workloads to improve their overall sustainability. Establish a mechanism to monitor the
sustainability of your AWS Cloud consumption based on common, standardized metrics.
The [AWS Customer Carbon Footprint Tool](../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md "../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md") can be used to estimate the carbon emissions
of AWS products and services that underlie your SAP systems. Greenhouse gas emissions are
converted to the amount of carbon dioxide that would result in equivalent warming and are
denoted by the services to which they are associated. Given that this reporting is
AWS account-specific, separating your SAP systems into separate accounts from other
workloads might be necessary to achieve the maximum benefits of the tool. That being said, a
multi-account strategy is typically based on the security requirements of your organization,
so refer to the SAP Lens security pillar guidance on this topic.

SAP also provides their [SAP Sustainability
Control Tower](https://www.sap.com/products/sustainability-control-tower.html "https://www.sap.com/products/sustainability-control-tower.html") solution to expand reporting beyond the underlying SAP
infrastructure costs to infrastructure costs and ultimately the overall business’s
sustainability posture.

- AWS Documentation: [Understanding your customer
  carbon footprint tool](../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md "../../../awsaccountbilling/latest/aboutv2/what-is-ccft.md")
- Well-Architected Framework [Sustainability]: [Evaluate specific improvements](../sustainability-pillar/evaluate-specific-improvements.md "../sustainability-pillar/evaluate-specific-improvements.md")
- Well-Architected Framework [Security]: [Assess the
  need for specific security controls for your SAP workloads](best-practice-5-3.md "best-practice-5-3.md")
- SAP Documentation: [SAP
  Sustainability Control Tower](https://www.sap.com/products/sustainability-control-tower.html "https://www.sap.com/products/sustainability-control-tower.html")
  **Suggestion 21.3.2 - Periodically baseline and review reported
  results**

As described in Suggestion 21.1.1, progress of an organization’s sustainability
initiative over time should be based on an initial reference position. As part of setting up
the relevant sustainability monitoring tools, establish the baseline configuration data and
reporting, from which progress will be tracked. Baselining should include the following
considerations:

- Tagging of relevant SAP workloads to allow for more granular reporting.
- Current carbon dioxide-equivalent (CO2e) or other proxy metric for workloads running
  in AWS.
  To ensure your organization’s use of AWS services for SAP and their sustainability
  trajectory are monitored against established KPIs and overall business goals, establish a
  periodic reporting review as part of an improvement process. This review should include the
  following activities:

- Validate all relevant SAP workloads are being monitored appropriately, including new
  workloads added since data gathering was last baselined.
- Measure the results, look for gaps, and replicate areas of success.
  Aligning these activities with the best practices from the SAP Lens operational
  excellence pillar can help you perform standardized sustainability reviews with other
  periodic operational activities. For example, discovering and removing unused resources,
  such as orphaned storage volumes or low-utilization instances, should be standard
  operational review tasks that also reduce environmental impact.

- Well-Architected Framework [Sustainability]: [Improvement process](../sustainability-pillar/improvement-process.md "../sustainability-pillar/improvement-process.md")
- Well-Architected Framework [Sustainability]: [Measure results and replicate successes](../sustainability-pillar/measure-results-and-replicate-successes.md "../sustainability-pillar/measure-results-and-replicate-successes.md")
- Well-Architected Framework [Operational Excellence]: [Validate and improve your
  SAP workload regularly](best-practice-5-3.md "best-practice-5-3.md")
