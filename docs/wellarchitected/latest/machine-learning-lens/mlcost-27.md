# MLCOST-27: Monitor usage and cost by ML activity

Use cloud resource tagging to manage, identify, organize,
search for, and filter resources. Tags help categorize
resources by purpose, owner, environment, or other criteria.
Associate costs with resources using ML activity categories,
such as re-training and hosting, by using tagging to manage
and optimize cost in deployment phases. Tagging can be useful
for generating billing reports with breakdown of cost by
associated resources.

## Implementation plan

- **Use AWS tagging** -A
  [tag](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
  is a label that you or AWS assigns to an AWS resource.
  Each tag consists of a key and a value. For each
  resource, each tag key must be unique, and each tag key
  can have only one value. You can use tags to organize
  your resources, and cost allocation tags to track your
  AWS costs on a detailed level. AWS uses the cost
  allocation tags to organize your resource costs on your
  cost allocation report. This will make it easier for you
  to categorize and track your AWS costs. AWS provides two
  types of cost allocation tags, an AWS-generated tag and
  user-defined tags.
- **Use AWS Budgets to keep track of
  cost** - AWS Budgets helps you track your
  Amazon SageMaker AI cost, including development, training,
  and hosting. You can also set alerts and get a
  notification when your cost or usage exceeds (or is
  forecasted to exceed) your budgeted amount. After you
  create your budget, you can track the progress on the
  AWS Budgets console.

## Documents

- [Tagging
  AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
- [Use
  Tags to Track and Allocate Amazon SageMaker AI Studio
  Notebooks Costs](https://aws.amazon.com/about-aws/whats-new/2021/04/now-use-tags-track-allocate-amazon-sagemaker-studio-notebooks-costs/ "https://aws.amazon.com/about-aws/whats-new/2021/04/now-use-tags-track-allocate-amazon-sagemaker-studio-notebooks-costs/")
- [Tagging
  best practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md")
- [Managing
  your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md")

## Blogs

- [Optimizing
  costs for machine learning with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/")

## Videos

- [How
  can I tag my AWS resources to divide up my bill by cost
  center or project?](https://www.youtube.com/watch?v=HmXkLtSYHtk "https://www.youtube.com/watch?v=HmXkLtSYHtk")
