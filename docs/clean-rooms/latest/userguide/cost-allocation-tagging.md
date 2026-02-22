# Cost Allocation Tagging

AWS Clean Rooms supports using Cost Allocation Tags to track your AWS costs. You activate
these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs
and deliver a monthly cost allocation report to you. User-defined cost allocation
tags can be applied to AWS Clean Rooms resources to help track and allocate costs across your
collaboration.

## Taggable Resources for Cost Allocation

The following table lists the AWS Clean Rooms resources that incur charges and can be tagged
with user-defined cost allocation tags for tracking and organizing costs.

| Billed Resource           | Tagged resource   |
| ------------------------- | ----------------- |
| SQL Query                 | Membership        |
| PySpark Job               | Membership        |
| ML Training Job           | Membership        |
| ML Inference Job          | Membership        |
| Synthetic Data Generation | Membership        |
| Lookalike Model Training  | Lookalike Model   |
| Lookalike Segment Export  | Lookalike Segment |
