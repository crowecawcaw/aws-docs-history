# ADVCOST01-BP01 Continually measure costs of different

real-time bidding workloads, and adjust resource allocation accordingly

With fluctuations in usage over time, the costs associated with real-time bidding
workloads can vary significantly. Continually monitoring costs is the best way to keep them
under control.

## Implementation guidance

- Set KPIs for each campaign to evaluate cost-to-revenue ratios, as this is key to
  measuring value generation.
- Set KPIs for billing metrics (for example, resource costs) as well as campaign
  metrics (for example, click-through rate or new subscribers).
- Implement cost allocation tags for resources relevant to campaign tracking.
- Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard as a way
  to quickly visualize information about RTB costs and performance.
- Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") for one-off visualizations of cost data.
- Generate [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") dashboards that
  are specific to each campaign or that comprise the business as a whole.
- Configure Quick Suite with user-configurable filters to allow users to focus on the data
  that matters most to them.
- Configure Quick Suite to email dashboard reports to users on a schedule to automate and
  simplify the process.
- Regularly evaluate the data and report findings back to the business.
- As campaigns progress, continually re-evaluate them, and adjust resource
  allocation to meet value generation goals.

## Key AWS services

- [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
- [AWS Data Exports](../../../cur/latest/userguide/what-is-data-exports.md "../../../cur/latest/userguide/what-is-data-exports.md")

## Resources

- [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/ "https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/")
- [Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics
  on AWS](https://aws.amazon.com/solutions/guidance/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/ "https://aws.amazon.com/solutions/guidance/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/")
- [Using CUDOS Dashboard visualizations for AWS Marketplace spend visibility and
  optimization](https://aws.amazon.com/blogs/awsmarketplace/using-cudos-dashboard-visualizations-aws-marketplace-spend-visibility-optimization/ "https://aws.amazon.com/blogs/awsmarketplace/using-cudos-dashboard-visualizations-aws-marketplace-spend-visibility-optimization/")
- [Additional dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/additional "https://catalog.workshops.aws/awscid/en-US/dashboards/additional")
- [Organizing costs
  using AWS Cost Categories](../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md "../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md")
