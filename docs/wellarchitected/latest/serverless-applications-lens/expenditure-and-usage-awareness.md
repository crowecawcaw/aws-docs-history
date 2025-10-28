# Expenditure and usage awareness

As covered in the [AWS
Well-Architected Framework](../framework/welcome.md "../framework/welcome.md"), the increased flexibility and agility that the cloud
enables encourages innovation and fast-paced development and deployment. It eliminates the
manual processes and time associated with provisioning on-premises infrastructure, including
identifying hardware specifications, negotiating price quotations, managing purchase orders,
scheduling shipments, and then deploying the resources.

As your serverless architecture grows, the number of Lambda functions, APIs, stages, and
other assets will multiply. Most of these architectures need to be budgeted and forecasted in
terms of costs and resource management, so tagging can help you here. You can allocate costs
from your AWS bill to individual functions and APIs and obtain a granulated view of your
costs and usage per project in AWS Cost Explorer.

A good implementation is to share the same key-value tag for assets that belong to the
project programmatically, and create custom reports based on the tags that you have created.
This feature will help you not only allocate your costs, but also identify which resources
belong to which projects. To gain practical experience on this topic refer to the [Well Architected Labs](https://www.wellarchitectedlabs.com/ "https://www.wellarchitectedlabs.com/"). You can find many
cost optimization walkthroughs that include tagging as well.
