# AWS Config Resource Compliance Dashboard

## Authors

- Luca Casarini, Senior Technical Account Manager, AWS

## Contributors

- Iakov Gan, Senior Solution Architect, AWS

## Feedback & Support

Follow [Feedback & Support](feedback-support.md "feedback-support.md") guide.

## Links

### Demo Dashboard

Get more familiar with the dashboard using the live, interactive demo dashboard following this [link](https://cid.workshops.aws.dev/demo/?dashboard=cid-crcd "https://cid.workshops.aws.dev/demo/?dashboard=cid-crcd").

### GitHub Project

See the source code and the changelog at our GitHub [project](https://github.com/aws-samples/config-resource-compliance-dashboard "https://github.com/aws-samples/config-resource-compliance-dashboard").

## Introduction

AWS Config is a fully managed service that provides you with resource inventory, configuration history, and configuration change notifications for security and governance.

The Amazon Web Services (AWS) Config Resource Compliance Dashboard (CRCD) shows the inventory of your AWS resources, along with their compliance status, across multiple AWS accounts and Regions by leveraging your AWS Config data.

![CRCD Dashboard](images/images/dashboards/crcd-compliance-1.png)

## Advantages

### Compliance tracking

Track compliance of your AWS Config rules and conformance packs per service, AWS Region, account, resource. Identify resources that require compliance remediation and establish a process for continuous compliance review. Verify that your tagging strategy is consistently applied across accounts and Regions.

### Democratize security and compliance visibility

The AWS Config Dashboard helps security teams establish a compliance practice and offers visibility over security compliance to field teams, without them accessing AWS Config service or dedicated security tooling accounts.

### Shift-left security and compliance practices

Field teams will see their non-compliant resources as quickly as security teams. This creates a short feedback loop that helps keep non-compliant resources to a minimum and helps organizations establish a consistent compliance review process with a shorter path to get to green compliance.

### A simplified Configuration Management Database (CMDB) experience in AWS

Avoid investment in a dedicated external CMDB system or third-party tools. Access the inventory of resources in a single pane of glass, without accessing the AWS Management Console on each account and Region. Filter resources by account, Region, and fields that are specific to the resource such as IP address. If you tag consistently your resources, for example to map them to the application, owning team and environment, specify those tags to the dashboard and they will be displayed alongside other resource-specific information, and used for filtering your configuration items. Manage and plan the upgrade of Amazon RDS DB engines and AWS Lambda runtimes.

## Dashboard features

### AWS Config compliance

- At-a-glance status of compliant and non-compliant resources and AWS
  Config rules.
- Month-by-month compliance trend for resources and AWS Config rules.
- Compliance breakdown by service, account, and Region.
- Compliance tracking for AWS Config rules and conformance packs.

### Resource inventory management

![CRCD Dashboard](images/images/dashboards/crcd-ec2-inventory.png)

Inventory of Amazon EC2, Amazon EBS, Amazon S3, Amazon Relational Database Service (RDS) and AWS Lambda resources with filtering on account, Region and resource-specific fields (e.g. IP addresses for EC2, Lambda runtime, RDS database engine). Furthermore, the dashboard supports filtering of these resources by the custom tags that you use to categorize workloads and resources, such as Application, Owner and Environment. The name of the tags will be provided by you during installation.

#### Resource inventory and EC2 Availability Zone dashboards

Graphs that report summarized insights about resource configuration data, including detailed information about EC2 and EBS. Evaluate your resilience to AZ-level events by checking the distribution of your EC2 instances across Availability Zones.

### Tag compliance

Visualize the results of AWS Config Managed Rule [required-tags](../../../config/latest/developerguide/required-tags.md "../../../config/latest/developerguide/required-tags.md"). You can deploy this rule to find resources in your accounts that were not launched with your desired tag configurations by specifying which resource types should have tags and the expected value for each tag. The rule can be deployed multiple times in AWS Config. To display data on the dashboard, the rules must have a name that starts with `required-tags`, `required-tag`, `requiredtags` or `requiredtag` (this is case insensitive).

![CRCD Dashboard](images/images/dashboards/crcd-tag-compliance-summary.png)

### Contributors to AWS Config costs

AWS Config cost is driven by the number of rule evaluations and configuration item changes being recorded. AWS Config cost are complex and calculating them precisely is outside the scope of this dashboard. To help you analyze AWS Config cost contributors and reduce operational costs while maintaining robust security and compliance monitoring, the dashboard reports the number of configuration items changes that are recorded and the number of AWS Config rule evaluations over time. The dashboard also covers other use cases that contribute to unnecessary AWS Config costs:

- **Conformance pack rules that cannot be evaluated.** Conformance pack rules that have a compliance status of INSUFFICIENT_DATA do not have AWS resources in scope. Since you are charged for each rule evaluation regardless of the outcome, rules that return INSUFFICIENT_DATA still incur costs without delivering any compliance information.
- **Redundant AWS Config rules.** While AWS Config provides multiple deployment options—including individual rules, conformance packs, Security Hub standards, and AWS Control Tower controls—many customers inadvertently implement duplicate rules across these services. This duplication leads to significant disadvantages: unnecessary costs from redundant evaluations, governance complexity that complicates compliance management, and potentially inconsistent remediation actions for the same compliance issues. To optimize compliance efforts and reduce costs, organizations should develop a strategic approach that eliminates rule duplication across their AWS environments. The dashboard will help you identify the rules that are deployed multiple times.

![CRCD Dashboard](/images/guidance/latest/cloud-intelligence-dashboards/images/images/dashboards/crcd-cost-drivers.png)

### Configuration Item events

The AWS Config Dashboards shows the timeline of your configuration changes. Find which resources were recently created, updated or deleted and see which accounts and Regions are delivering AWS Config data. Visualize the latest data imported into the dashboard and confirm that you are receiving data from all accounts and Regions.

![CRCD Dashboard](images/images/dashboards/crcd-ci-events.png)

## Steps

There are two possible ways to deploy the AWS Config dashboard on AWS Organizations. Read the [Perequisites](config-resource-prerequisites.md "config-resource-prerequisites.md") page to understand which deployment setup is better for you. If you install the dashboard on a standalone account that is not part of an AWS Organization, follow the installation instructions in the Log Archive account.

- [Prerequisites](config-resource-prerequisites.md "config-resource-prerequisites.md")
- [Deployment: Log Archive account](config-resource-log-archive.md "config-resource-log-archive.md")
- [Deployment: Dashboard account](config-resource-dashboard-account.md "config-resource-dashboard-account.md")
- [Optional post-deployment activities and FAQ](config-resource-post-deployment.md "config-resource-post-deployment.md")
- [Teardown](config-resource-teardown.md "config-resource-teardown.md")

###### Note

These dashboards and their content: (a) are for informational purposes only, (b) represent current AWS product offerings and practices, which are subject to change without notice, and (c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS content, products or services are provided "as is" without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers.

## Update instructions

If you already have installed the AWS Config Dasboard, you can check our [GitHub repository upgrade page](https://github.com/aws-samples/config-resource-compliance-dashboard/blob/main/documentation/upgrade.md "https://github.com/aws-samples/config-resource-compliance-dashboard/blob/main/documentation/upgrade.md") to see if there are instructions on how to upgrade to the latest version.
