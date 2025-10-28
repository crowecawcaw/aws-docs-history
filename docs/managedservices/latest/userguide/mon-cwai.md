# Using CloudWatch Application Insights for .Net and SQL server in AMS

You can use Amazon CloudWatch Application Insights to set up the monitors for your AWS Managed Services (AMS) application resources to continuously analyze data for signs of problems with your
applications and reduce your mean time to repair (MTTR) when troubleshooting application issues. For details about CloudWatch Application Insights, see
[CloudWatch Application Insights for .NET and SQL Server](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md").

###### Important

AMS does not monitor problems from CloudWatch Application Insights because they are for application code controlled by you.

To use CloudWatch Application Insights, submit an RFC with the Deployment | Advanced stack components | Identity
and Access Management (IAM) | Create entity or policy (managed automation) change type
(ct-3dpd8mdd9jn1r) with a request to create an IAM role that provides you with
permission to configure CloudWatch Application Insights. There are two options to receive the problems identified:
through an SNS topic or with a target in CloudWatch Event rules. In the RFC, specify which you
want. If you plan to use CloudWatch Event rules, also specify the rule definition in the RFC.
After you're set up with CloudWatch Application Insights, you receive notice of potential problems including
insights that point to a possible root cause.

To learn how you can assume the role, see the AMS Onboarding Guide
[Federate your Active Directory with the AMS IAM Roles](../onboardingguide/federate-dir-with-sent-iam-roles.md "../onboardingguide/federate-dir-with-sent-iam-roles.md").
