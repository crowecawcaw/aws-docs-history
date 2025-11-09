# Migrate

Cost optimization doesn't stop after you complete the migration to
Cloud. It's essential to seamlessly manage resources and optimize
costs on regular basis. Start by closely monitoring your resources
throughout both the migration and post-migration stages to ensure
smooth transitions. Develop a thoughtful metrics strategy to
demystify cloud economics, enabling informed decision-making.
Establish budgeting mechanisms to continually monitor cost and
usage, and construct user-friendly dashboards with pre-built
visualizations for enhanced visibility. Choose the right purchase
options and scalable architectures tailored to your specific
workloads, and consider a long-term modernization strategy that
embraces cost-effective cloud-native services.

| MIG-COST-04: What custom monitoring strategies you have put in place to monitor and manage ongoing cost and usage data as you migrate resources to AWS? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                         |

Monitoring is an important part of maintaining and managing the
cost and usage of AWS resources during and after
migration. Customers use different AWS services and tools to
successfully manage and optimize their AWS bill.

## MIG-COST-BP-4.1: Create a deliberate metrics strategy to help demystify cloud economics

This BP applies to the following best practice areas:
Expenditure and usage awareness

### Implementation guidance

**Suggestion
4.1.1:** Regularly evaluate cloud
metrics to ensure they meet current business needs.

Start by creating an effective metrics and reporting
strategy, then define a set of metrics to measure the
implementation of your strategy. See
[Crafting
a robust metrics strategy to quantify your benefits from the
cloud](https://aws.amazon.com/blogs/aws-cloud-financial-management/crafting-a-robust-metrics-strategy-to-quantify-your-benefits-from-the-cloud/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/crafting-a-robust-metrics-strategy-to-quantify-your-benefits-from-the-cloud/") for some proven metrics that follow our
_see, save, plan,_ and
_run_ framework, and can serve as a
starting point for any company

## MIG-COST-BP-4.2: Monitor spend and limit unintended or unnecessary costs with budgeting and forecasting tools

This BP applies to the following best practice areas:
Expenditure and usage awareness

### Implementation guidance

**Suggestion
4.2.1:** Migrating to AWS can likely
reduce your
[total
cost of ownership](https://aws.amazon.com/economics/ "https://aws.amazon.com/economics/") (TCO), but you still need an
effective cost control mechanism to make sure you only pay
for what you need.

Set up your cost control system, by focusing on the
following core principles:

- Budget your spend with custom thresholds.
- Monitor and analyze how your costs progress toward
  limits.
- Take action to reduce unintended costs.

[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") gives you the ability to set custom budgets
that alert you when your costs or usage (actual or
forecasted) exceed your budgeted amount. With the recent
launch of

[AWS Budget actions](https://aws.amazon.com/blogs/aws-cost-management/get-started-with-aws-budgets-actions/ "https://aws.amazon.com/blogs/aws-cost-management/get-started-with-aws-budgets-actions/"), you can now preconfigure actions that
can trigger the implementation of

[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) policies or

[service
control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") (SCPs). In addition, you can stop
target

[Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") (Amazon EC2) or

[Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") instances in your account.

In a multi-account AWS environment, there are two patterns
for managing the budget that you can choose from based on
your organization's governance structure:

- Centralized budget management, where the budget is set
  by the management account for all its member accounts
- Decentralized budget management, where the budget is set
  for individual member accounts by its owners

For more detail, see the following:

- [How to manage cost overruns in your AWS multi-account environment – Part 1](https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/ "https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/")
- [Control developer account costs with AWS CloudFormation and AWS Budgets](https://aws.amazon.com/blogs/mt/control-developer-account-costs-with-aws-cloudformation-and-aws-budgets/ "https://aws.amazon.com/blogs/mt/control-developer-account-costs-with-aws-cloudformation-and-aws-budgets/")
- [Smart
  Budgeting Using Lambda and Service Catalog](https://aws.amazon.com/blogs/mt/smart-budgeting-using-lambda-and-service-catalog "https://aws.amazon.com/blogs/mt/smart-budgeting-using-lambda-and-service-catalog")

## MIG-COST-BP-4.3: Use AWS Cost Anomaly Detection in Cost Explorer to quickly improve cost controls

This BP applies to the following best practice areas:
Expenditure and usage awareness

### Implementation guidance

**Suggestion
4.3.1:**
[Cost
Anomaly Detection](https://aws.amazon.com/blogs/aws-cloud-financial-management/new-aws-cost-explorer-users-can-now-automatically-detect-cost-anomalies/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/new-aws-cost-explorer-users-can-now-automatically-detect-cost-anomalies/") is an

[AWS Cost Management](https://aws.amazon.com/aws-cost-management/ "https://aws.amazon.com/aws-cost-management/") service that uses advanced machine
learning to detect anomalous spend and provide
contextualized alert notifications through email and

[Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/").

Each anomaly includes root cause analysis and direct links
to further investigate in Cost Explorer to understand the
unexpected usage and its drivers.

The default configuration includes the creation of an AWS
services monitor, which tracks charges of most AWS services
(see
[Quotas
and restrictions](../../../cost-management/latest/userguide/management-limits.md#limits-ad "../../../cost-management/latest/userguide/management-limits.md#limits-ad")) deployed now, or in the future, by
your management and member accounts. It also includes a
daily email subscription, which sends an email if any
anomaly is detected or ongoing during that specific day. By
default, the primary email address associated with the
account will receive a daily summary email for any service
anomaly detected that is above $100 and exceeds 40% of the
expected spend.

## MIG-COST-BP-4.4: Use dashboards that provide pre-built visualizations to help you get a detailed view of your AWS usage and costs as you move resources to AWS

This BP applies to the following best practice areas:
Expenditure and usage awareness

### Implementation guidance

**Suggestion
4.4.1:**AWS Cost Explorer provides a
high-level view of costs and usage, using the same dataset that
is used to generate the AWS Cost and Usage Reports. 

To extract resource-level granularity, you can use Amazon Athena
queries, which requires familiarity and previous experience to
build complex SQL queries.

Having dashboards that provide pre-built visualizations can help
you get a detailed view of your AWS usage and costs.

The
[Cloud
Intelligence Dashboards](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/ "https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/") are a collection of

[Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
[dashboards](https://aws.amazon.com/blogs/mt/visualize-and-gain-insights-into-your-aws-cost-and-usage-with-cloud-intelligence-dashboards-using-amazon-quicksight/ "https://aws.amazon.com/blogs/mt/visualize-and-gain-insights-into-your-aws-cost-and-usage-with-cloud-intelligence-dashboards-using-amazon-quicksight/").
They offer powerful visuals, in-depth insights, and intuitive
querying without having to build complex solutions or share your
cost data with third-party companies.

The
[Cost
Intelligence Dashboard](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/cost-usage-report-dashboards/dashboards/2a_cost_intelligence_dashboard/ "https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/cost-usage-report-dashboards/dashboards/2a_cost_intelligence_dashboard/"),

[CUDOS
Dashboard](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/#cudos-dashboard "https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/#cudos-dashboard"),

[Trusted
Advisor Organization (TAO) Dashboard](https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/#trusted-advisor-organizational-tao-dashboard "https://www.wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/#trusted-advisor-organizational-tao-dashboard"), and

[Trends
Dashboard](https://cudos.workshop.aws/workshop-trends.html "https://cudos.workshop.aws/workshop-trends.html") are built on native AWS services. They are
inherently secure because the data resides in the organization.
They inherit all the features of Quick Suite, including
integration with

[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/"), which makes them highly secure, and
Quick Suite being a serverless service allows you to pay
as you go and scale on demand.

You do not need coding or SQL skills to customize these
dashboards. The visualizations include Machine Learning (ML)
driven insights, live trends, actionable recommendations, links
to relevant blog posts and AWS service documentation that help
you make informed business decisions.

| MIG-COST-05: How are you ensuring your target infrastructure is optimized for your workloads? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

AWS has a lot of options for instance shapes and sizes, purchase
options, scaling options, and managed services. Consider how you
can leverage these capabilities during and after migration to
maximize cost benefits from your cloud infrastructure.

## MIG-COST-BP-5.1: Leverage the right purchase options and scalable architecture for your workloads

This BP applies to the following best practice areas:
Cost-effective resources

### Implementation guidance

**Suggestion
5.1.1:** Leverage the right purchase
model for your workload. 

Selecting the correct purchasing models can greatly reduce
the total cost of running a workload. Workloads with fairly
consistent resource requirements should consider reserved
instances or savings plans to save up to 72 percent on cost
compared to the same resources purchased on-demand. On the
other hand, some workloads, such as question and answer (QA)
environments, may be temporary or intermittent. This type of
workload may benefit from
[Spot
Instances](../../../whitepapers/latest/cost-optimization-leveraging-ec2-spot-instances/when-to-use-spot-instances.md "../../../whitepapers/latest/cost-optimization-leveraging-ec2-spot-instances/when-to-use-spot-instances.md"), which can be much more cost effective for
well-fit workloads compared to comparable on-demand
resources. 

In some cases, licensing may have an impact on purchasing
models. For instance, some licenses are bound to physical
cores and not transferable to an EC2 instance. In this case,
it may be more cost effective to purchase a
[dedicated
host](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md") to use for the duration of those licenses. For
more detail, see

[EC2
Reservation Models](../../../whitepapers/latest/cost-optimization-reservation-models/welcome.md "../../../whitepapers/latest/cost-optimization-reservation-models/welcome.md").

**Suggestion
5.1.2:** Use fine-grained data collected
in the assess phase to right-size your infrastructure as
you're migrating.

It is unlikely that the resources allocated to your source
infrastructure are exactly what your workload is using. The
cloud offers more flexibility when provisioning resources
and makes it easier to change the size and shape of the
provisioned resources. By sizing your target infrastructure
to the actual usage, you can see immediate cost savings by
migrating to the cloud. 

When selecting your target resources, consider
[burstable
performance instances](../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md"), which allow you to run a
workload at a fraction of the cost of comparable-sized
non-burstable instances. These instances are especially
cost-effective for non-production or other workloads that
are often near-idle. 

**Suggestion
5.1.3:** Enable autoscaling immediately
after migrating when your workload allows it.

Autoscaling can have a significant impact on infrastructure
costs, especially for applications that that have large
fluctuations in compute capacity needs over time. If you are
able to autoscale, consider that when sizing your target
infrastructure. Choose instances that are between your
minimum and average compute, memory, and disk usage, and
make sure your autoscaling rules allow you to scale up to at
least the maximum expected usage. 

## MIG-COST-BP-5.2: Identify resources during migration that are likely candidates for cost optimizations later

This BP applies to the following best practice areas:
Cost-effective resources

### Implementation guidance

**Suggestion
5.3.1:** Tag your resources as you're
migrating to make additional cost optimizations later.

It's often not feasible to make every cost optimization
during the initial migration. Tag resources as they're being
created to distinguish important categories that can help
with cost optimization later. For instance, tag production
and pre-production instances so you can use the tags later
to automate stopping pre-production instances at night.

| MIG-COST-06: What cost optimization tools are you leveraging to reduce your cloud spend? |
| ---------------------------------------------------------------------------------------- |
|                                                                                          |

Once you have successfully migrated workloads to AWS, it is
critical to choose the right set of AWS cost optimization tools
that provide ability to manage, monitor, and track your spend in
the cloud. Understanding your cost structure in comprehensive
manner and applying it across spectrum of AWS services allows
you to implement the right cost optimization solutions in order
to optimize your operational cost after migration or
modernization.

## MIG-COST-BP-6.1: Use automation to re-evaluate your compute usage periodically

This question applies to best practice area:  Optimize over
time

### Implementation guidance

**Suggestion
6.1.1:** Employ cost-optimization tools
built specifically for AWS infrastructure. 

AWS provides comprehensive cost management tools for cost
optimization. Most workloads continue to evolve over time.
Use combination of cost optimization tools to continue
cost-optimization post-migration such as Compute Optimizer,
Trusted Advisor, rightsizing recommendations, Savings Plans
(SP) and Reserve Instances (RI) reports, Amazon CloudWatch
alarms, and Amazon S3 Lens based on various services that
are part of your AWS environments. These tools analyze your
AWS usage and make simple, actionable suggestions to reduce
costs of running your workloads on AWS, while incorporating
the latest features and pricing. 

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/"): Provides
  recommendations that help you follow AWS best practices.
  Trusted Advisor evaluates your account by using checks.
  These checks identify ways to optimize your AWS
  infrastructure, improve security and performance, reduce
  costs, and monitor service quotas. You can then follow
  the recommendations to optimize your services and
  resources.
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/"): Identifies whether
  your AWS resources are optimal, and offers
  recommendations to improve cost and performance. It
  helps us with rightsizing recommendations by avoiding
  over provisioning and under provisioning.
- [Rightsizing
  recommendations](../../../cost-management/latest/userguide/ce-rightsizing.md "../../../cost-management/latest/userguide/ce-rightsizing.md"): This feature in AWS Cost Explorer helps you identify cost-saving
  opportunities by downsizing or terminating instances in
  Amazon Elastic Compute Cloud (Amazon EC2). Rightsizing
  recommendations analyze your Amazon EC2 resources and
  usage to show opportunities for how you can lower your
  spending.
- **SP and RI reports**: If
  you own

[Savings
Plan](../../../savingsplans/latest/userguide/sp-monitoring.md "../../../savingsplans/latest/userguide/sp-monitoring.md")s or

[Reserved
Instances](https://aws.amazon.com/aws-cost-management/reserved-instance-reporting/ "https://aws.amazon.com/aws-cost-management/reserved-instance-reporting/"), this helps to understand how much SP
or RI to purchase. Once you purchase, it also helps you
understand the coverage, which is a measure of how many
instances are covered out of all your EC2 and RDS
instances.

- [Amazon CloudWatch:](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
  Provides detailed monitoring of infrastructure
  components at a line item about different services being
  consumed and allows to set near real-time alarms for
  Cloud Watch.
- [Amazon S3 Lens:](https://aws.amazon.com/s3/storage-lens/ "https://aws.amazon.com/s3/storage-lens/") Allows customers to get
  visibility into their Amazon S3 usage. Amazon S3 Storage
  Lens is a single place to understand Amazon S3
  consumption and provides recommendations for objects
  that haven't been accessed for long time, different
  storage tiers, and other storage related metrics.

Follow rightsizing recommendations provided by combination
of different AWS native Cloud Financial Management tools.

| MIG-COST-07: How are you prioritizing your migrated AWS workloads and further driving cost optimization through modernization? |
| ------------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                |

Migrations don't end when a workload is in AWS. It's important
to continue to optimize costs post-migration to get the most
value from the cloud. There are various modernization pathways
that allow you to further optimize your cost profile on AWS
while delivering innovative solutions, reducing time-to-value
and improving customer experiences.

## MIG-COST-BP-7.1: Create a plan early to optimize after the initial migration

This question applies to best practice area:  Optimize over
time

### Implementation guidance

**Suggestion
7.1.1:**Depending on your specific AWS
architecture and services being deployed, there are a number
of techniques to further optimize cost both at the
infrastructure layer, including refactoring your application
to take advantage of modern, cloud-native services. 

- **Use newer, cost-efficient
  compute options available for your
  workloads:** There are three important ways to
  optimize compute costs, and AWS has tools to help you
  with all of them. It starts with choosing the right
  [Amazon EC2 purchase model](https://aws.amazon.com/ec2/cost-and-capacity/ "https://aws.amazon.com/ec2/cost-and-capacity/") for your workloads, then
  selecting the right instance to fine tune price and
  performance, and finally mapping usage to actual demand.
- **Use an optimal combination of
  AWS Managed Services:** Depending on your
  existing AWS architecture, you can re-platform
  applications to further save on operating costs in the
  cloud. If you are running a SQL database on Amazon EC2,
  modernizing to an Amazon RDS managed service can remove
  lot of undifferentiated heavy-lifting and lower overall
  total cost of ownership (TCO).
- **Modernization
  pathways**: The four most popular
  [modernization
  pathways](../../../prescriptive-guidance/latest/patterns/modernization-pattern-list.md "../../../prescriptive-guidance/latest/patterns/modernization-pattern-list.md") are as follows:
  - **Serverless:** Helps
    organizations to build and run applications without
    provisioning or managing infrastructure. These
    services, such as AWS Lambda and AWS Fargate, allow
    organizations to worry less about operational
    overhead and have a faster time to market. Features
    like automatic scaling and pay-for-use billing drive
    business agility and cost-efficiency.
  - **Containers**: Containers
    provide a standard way to package an application's
    code, configurations, and dependencies into a single
    object. Examples of container services include
    Amazon Elastic Container Service (ECS) and AWS
    Elastic Kubernetes Service (EKS).
  - **Managed data:** A
    fully managed, purpose-built database service,
    supporting diverse data models and applications.
  - **Managed
    analytics:** A range of services supporting
    analytics use cases like data lake initiatives, big
    data processing, real-time analytics, and
    operational analytics.
