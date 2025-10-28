# Best Practice 20.3 – Establish a

budget and mechanisms for cost allocation and tracking including anomaly
detection

There are [guidelines](../cost-optimization-pillar/expenditure-and-usage-awareness.md "../cost-optimization-pillar/expenditure-and-usage-awareness.md") in the Well-Architected Framework for implementing financial
management. Set expectations around cloud costs with annual, quarterly, monthly, or even
daily budgets depending on your business needs. Adjust forecasts regularly to align with
usage, and identify patterns and anomalies. Establish mechanisms for cost allocation using
account and tagging strategies.

**Suggestion 20.3.1 – Use cost and billing tools to gain spend
visibility**

SAP systems are often static in their usage patterns once established. If you use an
on-demand pricing model, either on a permanent basis or during project phases, you might
see a fluctuation in Amazon EC2 costs. If data volume management strategies are not put in
place, Amazon EBS and Amazon S3 costs might be higher than expected.

AWS provide a suite of [Cloud
Financial Management Services](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/") including the following:

- - [AWS Billing Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/ "https://aws.amazon.com/aws-cost-management/aws-billing-conductor/") allows you to construct a cost allocation strategy that aligns
    with your business logic.
  - [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") can be used to set custom budget based on your expected
    usage and notify you when a threshold is exceeded.
  - [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/ "https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/") uses advanced machine learning (ML) technologies to identify
    anomalous spend and root causes.
  - [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?track=costop_bottom "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?track=costop_bottom")
    provide tools for visibility and analysis.
    Further guidance can be found in the Well-Architected Framework [Cost Optimization]:
    [Expenditure and Usage Awareness](../cost-optimization-pillar/expenditure-and-usage-awareness.md "../cost-optimization-pillar/expenditure-and-usage-awareness.md").

**Suggestion 20.3.2 – Analyze and allocate spend using tags**

You can create [cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md#allocation-what "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md#allocation-what") that help identify pricing of AWS resources based on
individual accounts, resources, business units, and SAP environments. These tags are then
visible within the AWS billing reports and can be analyzed using Cost Explorer. You can
use cost allocation tags to determine the costs associated with individual SAP
environments. They help inform if action should be taken to reduce or remove costs
associated with specific environments, such as temporary environments or project
environments that are no longer required. You should have a process to identify resources
that do not have cost allocation tags attached. Implement the actions required to add cost
allocation tags to these resources.

- SAP on AWS Blog: [Tagging recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/")
