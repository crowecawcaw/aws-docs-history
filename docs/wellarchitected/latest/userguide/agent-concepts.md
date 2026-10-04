

AWS Well-Architected Agent is in preview release and is subject to change.

# AWS Well-Architected Agent Concepts and terminology
<a name="agent-concepts"></a>

This topic defines the key concepts you need to understand before using AWS Well-Architected Agent.

## Agent profiles
<a name="agent-concept-profiles"></a>

An agent profile is the primary entity in AWS WA Agent. It defines which AWS accounts and Regions the agent monitors, the goals it optimizes for, and details about your applications. AWS WA Agent uses the profile to scan your resources and generate recommendations.

**Note**  
AWS Well-Architected Tool also has a feature named profiles. AWS WA Tool profiles are questionnaires that you attach to workloads to prioritize review questions, and are unrelated to AWS WA Agent profiles. This section describes AWS WA Agent profiles only. For information about AWS WA Tool profiles, see [Tool profiles](tool-profiles.md).

When you create a profile, you can create an execution role during the setup process or select an existing one. You create access roles in your workload accounts before or after profile creation, then link them by updating the access role trust policies.

Each profile has the following attributes:
+ A unique name within an AWS account and AWS Region.
+ Business goals that direct the optimization focus.
+ Optimization pillars to analyze.
+ Accounts to scan for resources.

## Execution roles and access roles
<a name="agent-concept-roles"></a>

AWS WA Agent uses two types of IAM roles to discover and analyze resources across your accounts:
+ **Execution role:** An IAM role in the same account as your AWS WA Agent profile. You create this role during profile setup or select an existing one. AWS WA Agent assumes this role to orchestrate resource discovery across your configured accounts. The trust policy allows the `wellarchitected.amazonaws.com` service principal to assume the role.
+ **Access role:** An IAM role that you create in each account you want AWS WA Agent to analyze. The access role is encouraged to use the `WellArchitectedAgentResourceScanning` managed policy, which grants read-only access to resource metadata and configuration. Alternatively, you can scope the access role permissions to only the actions you want AWS WA Agent to perform on your behalf. You update the trust policy on each access role to allow the execution role to assume it.

Neither role grants AWS WA Agent permission to modify your resources. The execution role's only permission is to assume your access roles, and access roles grant read-only access to resource metadata and configuration.

You can use the same role name across all workload accounts (common name pattern) or use different names per account (per-account ARN). During profile creation, you specify which approach you are using.

## Goals and optimization pillars
<a name="agent-concept-goals"></a>

Business goals are plain-text statements that guide how AWS WA Agent prioritizes and ranks recommendations. You add goals during profile creation and can modify them at any time afterward. Each goal is associated with one optimization pillar.

AWS WA Agent analyzes your infrastructure across four optimization pillars:
+ Cost optimization
+ Security
+ Resilience
+ Performance

## Application context
<a name="agent-concept-app-context"></a>

Application context provides AWS WA Agent with additional information about your workloads so that it can generate more relevant, personalized recommendations. You add application context after your profile is created.

Application context includes the following:
+ Application overview
+ Accounts and Regions
+ Tags (key-value pairs to scope resource discovery)
+ Services and resource types. Some resource types are not supported. For more information, see [Unsupported resource types](agent-quotas.md#agent-unsupported-resources).
+ Industry
+ Application type (`SAS`, `DESKTOP_APPLICATION`, or `OTHER`)
+ Criticality level (`TEST_DEVELOPMENT`, `NON_CRITICAL`, `MISSION_CRITICAL`, or `BUSINESS_CRITICAL`)
+ Architecture overview (plain text)
+ Additional context (plain text)

## Recommendation types
<a name="agent-concept-rec-types"></a>

AWS WA Agent generates three types of recommendations:
+ **Resource:** Targets a specific resource such as an Amazon EC2 instance, Lambda function, or Amazon RDS database. Identifies optimization opportunities at the individual resource level.
+ **Application:** Spans multiple related resources within a discovered application. Considers how resources interact and provides guidance that accounts for relationships between components.
+ **Architecture:** Generated from IaC template analysis. Upload your CloudFormation, Terraform, or AWS CDK templates and receive recommendations aligned to AWS Well-Architected best practices, along with deployment-ready updated templates.

## Architecture reviews
<a name="agent-concept-arch-reviews"></a>

Architecture reviews are on-demand analyses of your Infrastructure as Code (IaC) projects against the AWS Well-Architected Framework. You provide an Amazon S3 URI pointing to your IaC files or upload a single document directly through the console. Select which pillars to review, and AWS WA Agent returns architecture-type recommendations with updated templates.

Architecture reviews differ from resource and application recommendations in that they target templates before deployment, enabling you to identify issues before they reach production.