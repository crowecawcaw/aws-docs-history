# AWS Cloud Financial Management services and tools

The following AWS services can be used to help you meet the
prescribed benefits of the M&G Guide:

The [AWS
Cost & Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/ "https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/") contains a comprehensive set of AWS cost and usage data,
including additional metadata about AWS services, pricing, Reserved Instances, and Savings Plans.
You should use this information to inform and create controls.

[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?track=costma "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/?track=costma") is a tool that enables you to view and
analyze your costs and usage. You can explore your usage and costs
using the main graph, the Cost Explorer cost and usage reports, or
the Cost Explorer RI reports. You can view data for up to the last
12 months, forecast how much you’re likely to spend for the next
12 months, and get recommendations for what Reserved Instances to
purchase. You can use Cost Explorer to identify areas that need
further inquiry and see trends that you can use to understand your
costs.

AWS uses
[cost
allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") to organize your resource costs on your
cost allocation report, which makes it easier for you to
categorize and track your AWS costs. AWS provides two types of
cost allocation tags: AWS-generated tags and user-defined tags.
AWS (or AWS Partners) defines, creates, and applies the
AWS-generated tags for you, and you define, create, and apply
user-defined tags.

[AWS Cost Anomaly Detection](../../../awsaccountbilling/latest/aboutv2/manage-ad.md "../../../awsaccountbilling/latest/aboutv2/manage-ad.md") is an AWS cost management feature
that uses machine learning to continually monitor your cost and
usage to detect unusual spends.

[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") allows you to set custom budgets to track your cost
and usage on a wide variety of use cases. With AWS Budgets, you
can choose to be alerted by email or Amazon SNS notification when
actual or forecasted cost and usage exceed your budget threshold,
or when your actual RI and Savings Plans utilization or coverage
drops below your desired threshold. With AWS Budgets actions, you
can also configure specific actions to respond to cost and usage
statuses in your accounts, so that if your cost or usage exceeds
or is forecasted to exceed your threshold, actions can be run
automatically or with your approval to reduce unintentional
over-spending. AWS Budgets integrates with multiple AWS services,
such as AWS Cost Explorer, so that you can easily view and analyze
your cost and usage drivers, AWS Chatbot, so you can receive
budget alerts in your designated Slack channel or Amazon Chime
room, and Service Catalog, so you can track costs on your
approved AWS portfolios and products.

[AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/ "https://aws.amazon.com/aws-cost-management/aws-cost-categories/") is an AWS cost management feature that
enables you to group cost and usage information into meaningful
categories based on your needs. You can create custom categories
and map your cost and usage information into these categories
based on the rules defined by you using various dimensions such as
account, tag, service, charge type, and even other cost
categories.

[Tag
policies](../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md "../../../organizations/latest/userguide/orgs_manage_policies_tag-policies.md") are a type of policy that can help you standardize
tags across resources in your organization's accounts. In a tag
policy, you specify tagging rules applicable to resources when
they are tagged.
[AWS Resource Groups Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") allows you to add tags to—or
edit or delete tags of—multiple AWS resources at once. With Tag
Editor, you can search for the resources that you want to tag, and
then manage tags for the resources in your search results.

[AWS License Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/") enables management of your software
licenses from vendors across AWS and on-premises environments. AWS License Manager lets administrators define and enforce licensing
rules that mirror the terms of their licensing agreements and
prevent breaches. Portfolio administrators gain control and
visibility of all their licenses with the AWS License Manager
dashboard integrated with AWS Organizations and reduce the risk of
non-compliance, misreporting, and additional costs due to
licensing overages. Independent software vendors (ISVs) can also
use AWS License Manager to easily distribute and track licenses.

[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/?nc2=type_a "https://aws.amazon.com/compute-optimizer/?nc2=type_a") recommends optimal AWS resources for your
workloads to reduce costs and improve performance by using machine
learning to analyze historical utilization metrics Compute Optimizer helps you choose optimal configurations for three types
of AWS resources: Amazon EC2 instances, Amazon EBS volumes, and
AWS Lambda functions, based on your utilization data.

[AWS Application Cost Profiler](https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/ "https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/") provides you the ability to track
the consumption of shared AWS resources used by software
applications and report granular cost breakdown across tenant
base.

[AWS Billing
Conductor](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/ "https://aws.amazon.com/aws-cost-management/aws-billing-conductor/") simplifies the show-back and charge-back workflows for AWS Solution
Providers and Enterprise customers. Using AWS Billing Conductor, you can customize your
AWS pricing and monthly billing report according to the billing relationship between you and
your end customers. A pro forma billing and cost and usage report is available for viewing and
cost allocation purposes.

If you would like support implementing this guidance, or assisting
you with building the foundational elements prescribed by the
M&G Guide, we recommend you review the offerings provided by
[AWS Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/") or the AWS Partners in the
[Built
on Control Tower program](https://aws.amazon.com/controltower/partners/ "https://aws.amazon.com/controltower/partners/").

If you are seeking help to operate your workloads in AWS following
this guidance,
[AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/") can augment your operational
capabilities as a short-term accelerator or a long-term solution,
letting you focus on transforming your applications and businesses
in the cloud.
