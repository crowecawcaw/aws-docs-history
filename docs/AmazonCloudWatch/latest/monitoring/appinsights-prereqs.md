# Prerequisites to configure an application for monitoring

You must complete the following prerequisites to configure an application with
CloudWatch Application Insights:

- **AWS Systems Manager enablement** – Install
  Systems Manager Agent (SSM Agent) on your Amazon EC2 instances, and enable the instances for SSM. For information about how to install the SSM Agent, see
  [Setting up AWS Systems Manager](../../../systems-manager/latest/userguide/systems-manager-setting-up.md "../../../systems-manager/latest/userguide/systems-manager-setting-up.md") in the _AWS Systems Manager User Guide_.
- **EC2 instance role** – You must attach the following Amazon EC2 instance roles to enable Systems Manager
  - You must attach the `AmazonSSMManagedInstanceCore` role to enable Systems Manager. For more information, see [AWS Systems Manager identity-based policy examples](../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md "../../../systems-manager/latest/userguide/auth-and-access-control-iam-identity-based-access-control.md").
  - You must attach the `CloudWatchAgentServerPolicy`
    policy to enable instance metrics and logs to be emitted through CloudWatch.
    For more information, see [Create IAM roles and users for use with CloudWatch agent](create-iam-roles-for-cloudwatch-agent.md "create-iam-roles-for-cloudwatch-agent.md").

- **AWS resource groups** – To onboard
  your applications to CloudWatch Application Insights, create a resource group that includes all of the
  associated AWS resources used by your application stack. This includes
  application load balancers, Amazon EC2 instances running IIS and web front‐end,
  .NET worker tiers, and SQL Server databases. For more information about
  application components and technology stacks supported by Application Insights, see
  [Supported application components](appinsights-what-is.md#appinsights-components "appinsights-what-is.md#appinsights-components"). CloudWatch Application Insights automatically includes
  Amazon EC2 Auto Scaling groups using the same tags or CloudFormation stacks as your resource group,
  because Amazon EC2 Auto Scaling groups are not supported by CloudFormation resource groups. For
  more information, see [Getting Started with
  AWS Resource Groups](../../../ARG/latest/userguide/gettingstarted.md "../../../ARG/latest/userguide/gettingstarted.md").
- **IAM permissions** – For users who
  don't have administrative access, you must create an AWS Identity and Access Management (IAM) policy
  that allows Application Insights to create a service-linked role and attach it to the
  user's identity. For more information about how to create the IAM policy, see
  [IAM policy for CloudWatch Application Insights](appinsights-iam.md "appinsights-iam.md").
- **Service-linked role** – Application Insights
  uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is created
  for you when you create your first Application Insights application in the Application Insights
  console. For more information, see [Using service-linked roles for
  CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").
- **Performance Counter metrics support for EC2 Windows
  instances** – To monitor Performance Counter metrics on your Amazon EC2
  Windows instances, Performance Counters must be installed on the instances.
  For Performance Counter metrics and corresponding Performance Counter set
  names, see [Performance Counter metrics](application-insights-performance-counter.md "application-insights-performance-counter.md"). For more information about
  Performance Counters, see [Performance Counters](https://docs.microsoft.com/en-us/windows/win32/perfctrs/performance-counters-portal "https://docs.microsoft.com/en-us/windows/win32/perfctrs/performance-counters-portal").
- **Amazon CloudWatch agent** – Application Insights
  installs and configures the CloudWatch agent. If you have CloudWatch agent installed,
  Application Insights retains your configuration. To avoid a merge conflict, remove the
  configuration of resources that you want to use in Application Insights from the
  existing CloudWatch agent configuration file. For more information, see [Manually create or edit the
  CloudWatch agent configuration file](CloudWatch-Agent-Configuration-File-Details.md "CloudWatch-Agent-Configuration-File-Details.md").
