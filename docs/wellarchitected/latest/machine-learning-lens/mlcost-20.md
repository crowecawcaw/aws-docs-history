# MLCOST-20 - Setup budget and use resource tagging to track costs

If you need visibility of your ML cost, set up budgets and
consider tagging your notebook instances. Examples of tags
include the name of the project, the business unit, and
environment (such as development, testing, or production).

Tags are useful for cost optimization and can provide a clear
visibility into where money is being spent.

## Implementation plan

- **Use AWS Budgets to keep track of
  cost** - AWS Budgets helps you track your Amazon SageMaker AI cost, including development, training, and
  hosting. You can also set alerts and get a notification
  when your cost or usage exceeds (or is forecasted to
  exceed) your budgeted amount. After you create your
  budget, you can track the progress on the AWS Budgets
  console.
- **Use
  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")** - Visualize, understand,
  and manage your AWS costs and usage over time using AWS Cost Explorer.
- **Tagging the resources** -
  Consider tagging your Amazon SageMaker AI notebook instances
  and the hosting endpoints. Cost allocation tags can help
  track and categorize your cost of ML. It can answer
  questions such as “Can I delete this resource to save
  cost?”

## Documents

- [Managing
  your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md")
- [Using
  Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
- [Tagging
  Best Practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")

## Blogs

- [Optimizing
  costs for machine learning with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/")
- [Automate
  Cost Control using Service Catalog and AWS
  Budgets](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-control-blog-series-2-automate-cost-control-using-aws-service-catalog-aws-budgets/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-control-blog-series-2-automate-cost-control-using-aws-service-catalog-aws-budgets/")
