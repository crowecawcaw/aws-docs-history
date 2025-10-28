# Best practice 2.1 – Use version control for job and application changes

Version control systems support tracking changes and the
ability to revert to previous versions of an analytics
system should changes cause unintended consequences. Your
team should version control code repositories for both
analytics infrastructure as code (IaC) and analytics
applications logic.

## Suggestion 2.1.1 – Use infrastructure as code and version control systems so that a failed deployment can be rolled back to a previous good state

Follow software development best practices when building
analytics systems. For example, deploy resources using
code templates, such as AWS CloudFormation or Hashicorp
Terraform, so that all deployments occur exactly as
intended. Use version control systems (for example, code
repositories such as GitHub) to hold
current and previous versions of your code templates.
Using these tools, if a new change results in unwanted
outcomes, you can easily roll back to the previous code
template.

For more details, refer to the following information:

- AWS Whitepaper:
  [Introduction
  to DevOps on AWS](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- AWS Blog:
  [Automate
  building an integrated analytics solution with AWS
  Analytics Automation Toolkit](https://aws.amazon.com/blogs/big-data/automate-building-an-integrated-analytics-solution-with-aws-analytics-automation-toolkit/ "https://aws.amazon.com/blogs/big-data/automate-building-an-integrated-analytics-solution-with-aws-analytics-automation-toolkit/")
