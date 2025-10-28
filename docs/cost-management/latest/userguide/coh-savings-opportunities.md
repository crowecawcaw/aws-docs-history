# Viewing your savings opportunities

You can view details about your recommended actions on the **Savings
opportunities** page. Use filters to refine the list of savings opportunities, and
learn more about each recommendation by using a split-view panel. For deeper analysis of any
recommendation, select it and choose **Analyze with Amazon Q**.

You can also group related recommendations. Cost Optimization Hub identifies recommended actions that
interact with each other, and it reduces estimated aggregated savings based on the degree of
overlap.

Cost Optimization Hub deduplicates amongst resource optimization strategies and proposes the recommendation
with the highest savings. It also considers the reduction in usage by implementing the
recommendations.

For example, an EC2 instance can either be deleted or rightsized, but not both. When Cost Optimization Hub
estimates aggregated savings for the instance, it chooses the actions with the highest savings
(in this case, delete), and ignores the savings from rightsizing.

Cost Optimization Hub also deduplicates amongst Savings Plans and Reserved Instances recommendations. It defaults to
commitment options that offer the highest overall savings, prioritizing Compute Savings Plans for their
flexibility and broader resource coverage. These recommendations typically favor three-year all
upfront options. You can customize these in Cost Optimization Hub preferences. For more information, see [Commitment preferences](coh-preferences.md#coh-commitment-preferences "coh-preferences.md#coh-commitment-preferences").

###### Topics

- [Viewing recommended actions and estimated
  savings](coh-view-recommendations.md "coh-view-recommendations.md")
- [Grouping related recommendations](coh-group-recommendations.md "coh-group-recommendations.md")
