# Using AWS Identity and Access Management Access Analyzer

AWS Identity and Access Management Access Analyzer provides the following capabilities:

- IAM Access Analyzer external access analyzers help [identify resources](#what-is-access-analyzer-resource-identification "#what-is-access-analyzer-resource-identification") in your
  organization and accounts that are shared with an external entity.
- IAM Access Analyzer internal access analyzers help [identify internal access to selected
  resources](#what-is-access-analyzer-internal-access-analysis "#what-is-access-analyzer-internal-access-analysis") in your organization and accounts.
- IAM Access Analyzer unused access analyzers help [identify unused access](#what-is-access-analyzer-unused-access-analysis "#what-is-access-analyzer-unused-access-analysis") in your
  organization and accounts.
- IAM Access Analyzer [validates IAM
  policies](#what-is-access-analyzer-policy-validation "#what-is-access-analyzer-policy-validation") against policy grammar and AWS best practices.
- IAM Access Analyzer custom policy checks help [validate IAM policies against your specified
  security standards](#what-is-access-analyzer-policy-checks "#what-is-access-analyzer-policy-checks").
- IAM Access Analyzer [generates IAM
  policies](#what-is-access-analyzer-policy-generation "#what-is-access-analyzer-policy-generation") based on access activity in your AWS CloudTrail logs.

## Identifying resources shared

with an external entity

IAM Access Analyzer helps you identify the resources in your organization and accounts, such as
Amazon S3 buckets or IAM roles, shared with an external entity. This lets you identify unintended
access to your resources and data, which is a security risk. IAM Access Analyzer identifies resources
shared with external principals by using logic-based reasoning to analyze the resource-based
policies in your AWS environment. For each instance of a resource shared outside of your
account, IAM Access Analyzer generates a finding. Findings include information about the access and the
external principal granted to it. You can review findings to determine if the access is intended
and safe or if the access is unintended and a security risk. In addition to helping you identify
resources shared with an external entity, you can use IAM Access Analyzer findings to preview how your
policy affects public and cross-account access to your resource before deploying resource
permissions. The findings are organized in a visual summary dashboard. The dashboard highlights
the split between public and cross-account access findings, and provides a breakdown of findings
by resource type. To learn more about the dashboard, see [View the IAM Access Analyzer findings
dashboard](access-analyzer-dashboard.md "access-analyzer-dashboard.md").

###### Note

An external entity can be another AWS account, a root user, an IAM user or role, a
federated user, an anonymous user, or another entity that you can use to create a filter. For
more information, see [AWS JSON Policy Elements: Principal](reference_policies_elements_principal.md "reference_policies_elements_principal.md").

When you enable IAM Access Analyzer, you create an analyzer for your entire organization or your
account. The organization or account you choose is known as the zone of trust for the analyzer.
The analyzer monitors all of the [supported
resources](access-analyzer-resources.md "access-analyzer-resources.md") within your zone of trust. Any access to resources by principals within your
zone of trust is considered trusted. Once enabled, IAM Access Analyzer analyzes the policies applied to
all of the supported resources in your zone of trust. After the first analysis, IAM Access Analyzer
analyzes these policies periodically. If you add a new policy or change an existing policy,
IAM Access Analyzer analyzes the new or updated policy within about 30 minutes.

When analyzing the policies, if IAM Access Analyzer identifies one that grants access to an
external principal that isn't within your zone of trust, it generates a finding. Each finding
includes details about the resource, the external entity with access to it, and the permissions
granted so that you can take appropriate action. You can view the details included in the finding
to determine whether the resource access is intentional or a potential risk that you should
resolve. When you add a policy to a resource, or update an existing policy, IAM Access Analyzer
analyzes the policy. IAM Access Analyzer also analyzes all resource-based policies periodically.

On rare occasions under certain conditions, IAM Access Analyzer does not receive notification of
an added or updated policy, which can cause delays in generated findings. IAM Access Analyzer can take
up to 6 hours to generate or resolve findings if you create or delete a multi-region access point
associated with an Amazon S3 bucket, or update the policy for the multi-region access point. Also, if
there is a delivery issue with AWS CloudTrail log delivery or resource control policy (RCP) restriction
changes, the policy change does not trigger a rescan of the resource reported in the finding.
When this happens, IAM Access Analyzer analyzes the new or updated policy during the next periodic
scan, which is within 24 hours. If you want to confirm a change you make to a policy resolves an
access issue reported in a finding, you can rescan the resource reported in a finding by using
the **Rescan** link in the **Findings** details page, or by
using the [`StartResourceScan`](../../../access-analyzer/latest/APIReference/API_StartResourceScan.md "../../../access-analyzer/latest/APIReference/API_StartResourceScan.md") operation of the IAM Access Analyzer API. To learn more, see
[Resolve IAM Access Analyzer findings](access-analyzer-findings-remediate.md "access-analyzer-findings-remediate.md").

###### Important

For external access, IAM Access Analyzer analyzes only policies applied to resources in the same
AWS Region where it's enabled. To monitor all resources in your AWS environment, you must
create an external access analyzer to enable IAM Access Analyzer in each Region where you're using
supported AWS resources.

For unused access, findings for the analyzer do not change based on Region. Creating an
unused access analyzer in each Region where you have resources is not required.

IAM Access Analyzer analyzes the following resource types for external access:

- [Amazon Simple Storage Service buckets](access-analyzer-resources.md#access-analyzer-s3 "access-analyzer-resources.md#access-analyzer-s3")
- [Amazon Simple Storage Service directory buckets](access-analyzer-resources.md#access-analyzer-s3-directory "access-analyzer-resources.md#access-analyzer-s3-directory")
- [AWS Identity and Access Management roles](access-analyzer-resources.md#access-analyzer-iam-role "access-analyzer-resources.md#access-analyzer-iam-role")
- [AWS Key Management Service keys](access-analyzer-resources.md#access-analyzer-kms-key "access-analyzer-resources.md#access-analyzer-kms-key")
- [AWS Lambda functions and layers](access-analyzer-resources.md#access-analyzer-lambda "access-analyzer-resources.md#access-analyzer-lambda")
- [Amazon Simple Queue Service queues](access-analyzer-resources.md#access-analyzer-sqs "access-analyzer-resources.md#access-analyzer-sqs")
- [AWS Secrets Manager secrets](access-analyzer-resources.md#access-analyzer-secrets-manager "access-analyzer-resources.md#access-analyzer-secrets-manager")
- [Amazon Simple Notification Service topics](access-analyzer-resources.md#access-analyzer-sns "access-analyzer-resources.md#access-analyzer-sns")
- [Amazon Elastic Block Store volume snapshots](access-analyzer-resources.md#access-analyzer-ebs "access-analyzer-resources.md#access-analyzer-ebs")
- [Amazon Relational Database Service DB snapshots](access-analyzer-resources.md#access-analyzer-rds-db "access-analyzer-resources.md#access-analyzer-rds-db")
- [Amazon Relational Database Service DB cluster snapshots](access-analyzer-resources.md#access-analyzer-rds-db-cluster "access-analyzer-resources.md#access-analyzer-rds-db-cluster")
- [Amazon Elastic Container Registry repositories](access-analyzer-resources.md#access-analyzer-ecr "access-analyzer-resources.md#access-analyzer-ecr")
- [Amazon Elastic File System file systems](access-analyzer-resources.md#access-analyzer-efs "access-analyzer-resources.md#access-analyzer-efs")
- [Amazon DynamoDB streams](access-analyzer-resources.md#access-analyzer-ddb-stream "access-analyzer-resources.md#access-analyzer-ddb-stream")
- [Amazon DynamoDB tables](access-analyzer-resources.md#access-analyzer-ddb-table "access-analyzer-resources.md#access-analyzer-ddb-table")

## Identifying internal access to

business-critical resources

For your selected business-critical resources, IAM Access Analyzer helps you identify which
principals within your organization or account have access to them. This analysis supports
implementing the principle of least privilege by ensuring that your specified resources can only
be accessed by the intended principals within your organization.

Internal access analysis helps you:

- Determine which IAM users or roles within your account or organization can access your
  specified resources
- Understand access paths between principals and resources within your AWS
  environment
- Verify that your access controls are working as intended
- Review findings to determine if the access is intended and safe or if the access is
  unintended and presents a security risk
- Identify and remediate unintended access within your organization

IAM Access Analyzer analyzes the following resource types for internal access:

- [Amazon Simple Storage Service buckets](access-analyzer-resources.md#access-analyzer-s3 "access-analyzer-resources.md#access-analyzer-s3")
- [Amazon Simple Storage Service directory buckets](access-analyzer-resources.md#access-analyzer-s3-directory "access-analyzer-resources.md#access-analyzer-s3-directory")
- [Amazon Relational Database Service DB snapshots](access-analyzer-resources.md#access-analyzer-rds-db "access-analyzer-resources.md#access-analyzer-rds-db")
- [Amazon Relational Database Service DB cluster snapshots](access-analyzer-resources.md#access-analyzer-rds-db-cluster "access-analyzer-resources.md#access-analyzer-rds-db-cluster")
- [Amazon DynamoDB streams](access-analyzer-resources.md#access-analyzer-ddb-stream "access-analyzer-resources.md#access-analyzer-ddb-stream")
- [Amazon DynamoDB tables](access-analyzer-resources.md#access-analyzer-ddb-table "access-analyzer-resources.md#access-analyzer-ddb-table")

## Identifying unused access

granted to IAM users and roles

IAM Access Analyzer helps you identify and review unused access in your AWS organization and
accounts. IAM Access Analyzer continuously monitors all IAM roles and users in your AWS
organization and accounts and generates findings for unused access. The findings highlight unused
roles, unused access keys for IAM users, and unused passwords for IAM users. For active IAM
roles and users, the findings provide visibility into unused services and actions.

IAM Access Analyzer reviews last accessed information for all roles in your AWS organization and
accounts to help you identify unused access. IAM action last accessed information helps you
identify unused actions for roles in your AWS accounts. For more information, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

The findings for external, internal, and unused access analyzers are organized into a visual
summary dashboard. The dashboard highlights your AWS resources and AWS accounts that have the
most findings and provides a breakdown of findings by type. For more information about the
dashboard, see [View the IAM Access Analyzer findings
dashboard](access-analyzer-dashboard.md "access-analyzer-dashboard.md").

## Validating policies against AWS

best practices

You can validate your policies against IAM [policy grammar](reference_policies_grammar.md "reference_policies_grammar.md") and [AWS best practices](best-practices.md "best-practices.md") using the
basic policy checks provided by IAM Access Analyzer policy validation. You can create or edit a policy
using the AWS CLI, AWS API, or JSON policy editor in the IAM console. You can view policy
validation check findings that include security warnings, errors, general warnings, and
suggestions for your policy. These findings provide actionable recommendations that help you
author policies that are functional and conform to AWS best practices. To learn more about
validating policies using policy validation, see [Validate policies with
IAM Access Analyzer](access-analyzer-policy-validation.md "access-analyzer-policy-validation.md").

## Validating policies against your

specified security standards

You can validate your policies against your specified security standards using the
IAM Access Analyzer custom policy checks. You can create or edit a policy using the AWS CLI, AWS API,
or JSON policy editor in the IAM console. Through the console, you can check whether your
updated policy grants new access compared to the existing version. Through AWS CLI and AWS API,
you can also check specific IAM actions that you consider critical are not allowed by a policy.
These checks highlight a policy statement that grants new access. You can update the policy
statement and re-run the checks until the policy conform to your security standard. To learn more
about validating policies using custom policy checks, see [Validate policies with IAM Access Analyzer custom policy
checks](access-analyzer-custom-policy-checks.md "access-analyzer-custom-policy-checks.md").

## Generating policies

IAM Access Analyzer analyzes your AWS CloudTrail logs to identify actions and services that have been
used by an IAM entity (user or role) within your specified date range. It then generates an
IAM policy that is based on that access activity. You can use the generated policy to refine an
entity's permissions by attaching it to an IAM user or role. To learn more about generating
policies using IAM Access Analyzer, see [IAM Access Analyzer policy generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").

## Pricing for IAM Access Analyzer

IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and
users analyzed per analyzer per month.

- You will be charged for each unused access analyzer that you create.
- Creating unused access analyzers across multiple Regions will result in you being charged
  for each analyzer.
- Service-linked roles aren't analyzed for unused access activity and they aren't included
  in the total number of IAM roles analyzed.

IAM Access Analyzer charges for internal access analysis based on the number of resources
monitored per internal access analyzer per month.

IAM Access Analyzer charges for custom policy checks based on the number of API requests made to
IAM Access Analyzer to check for new access.

For a complete list of charges and prices for IAM Access Analyzer, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

To see your bill, go to the **Billing and Cost Management Dashboard** in
the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/"). Your bill contains links
to usage reports that provide details about your bill. To learn more about AWS account billing,
see the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md")

If you have questions concerning AWS billing, accounts, and events, [contact Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
