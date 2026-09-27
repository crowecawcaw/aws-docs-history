

# What is AWS Network Security Manager?
<a name="what-is"></a>

With AWS Network Security Manager, you can centrally define and deploy network security protections—such as AWS WAF and AWS Shield Advanced rules—across one or more accounts and resources in your organization. Instead of working with each resource individually, you define reusable policy objects (rules, templates, and policies) once and deploy them at scale, with continual monitoring to detect and remediate policy drift.

## How AWS Network Security Manager works at a glance
<a name="what-is-how-it-works"></a>

You define a set of hierarchical policy objects and apply them to targeted scopes. The lowest level of policy objects are *rules*. You can group rules into *templates*, which you can combine into *policies* with priority-based conflict resolution. You then select accounts and resources to protect with a *scope*, and enforce your policies by publishing a *deployment*.

After deployment, AWS Network Security Manager continually monitors the scoped environment and deployed policies to check whether they match the intended definitions. If not, AWS Network Security Manager can optionally remediate resources that drift from the intended configuration. For full details on the resource model, lifecycle, and architecture, see [How AWS Network Security Manager works](concepts.md).

## Features of AWS Network Security Manager
<a name="what-is-features"></a>
+ **Support for multiple firewall types** – AWS Network Security Manager supports AWS WAF for web ACL configurations and rule groups. Protected resource types include Amazon CloudFront distributions, Application Load Balancers, and Amazon API Gateway stages. AWS Network Security Manager also supports AWS Shield Advanced for DDoS protection of Amazon CloudFront distributions, Application Load Balancers, Classic Load Balancers, and Elastic IP addresses.
+ **Reusable security configurations** – Define policy objects once as rules, group them into templates, and create scopes to target resources. Reuse rules, templates, and scopes across multiple policies and deployments.
+ **Priority-based policy merging** – When multiple policies protect the same resource, AWS Network Security Manager merges their configurations based on policy priority, providing predictable conflict resolution.
+ **Single-account and multi-administrator support** – Use AWS Network Security Manager in a single account or designate multiple administrator accounts, each with a priority level. When administrators' policies overlap, AWS Network Security Manager resolves conflicts by administrator priority first, then by policy priority within each account.
+ **Draft and Active states** – Each AWS Network Security Manager resource, including rules, templates, policies, scopes, and deployments, supports Draft and Active states. Save resources as Draft without affecting live protections, then publish when ready to enforce them.
+ **Versioned snapshots** – Each AWS Network Security Manager resource, including rules, templates, policies, scopes, and deployments, supports immutable, version-numbered snapshots. Use versioning to preserve known-good AWS Network Security Manager resource configurations.
+ **Protected-resource synchronization diagnostics** – For each in-scope resource, see exactly which settings are out of sync and why, with expected settings compared to actual values for each configuration field.
+ **Automatic remediation** – Optionally enable AWS Network Security Manager to automatically remediate out-of-sync resources and align them with the intended configuration without manual intervention.
+ **Natural-language rule generation** – Use the `GenerateRuleConfiguration` operation to describe a rule in plain language and receive the corresponding configuration JSON, powered by Amazon Bedrock.

## Use cases
<a name="what-is-use-cases"></a>

The following are common use cases for AWS Network Security Manager:
+ **Enforce baseline AWS WAF rules across all accounts** – Define a set of AWS WAF rule groups that every internet-facing application must use, then deploy them across your entire organization. AWS Network Security Manager automatically applies the rules to new in-scope resources as they come into scope.
+ **Create specific custom or exception AWS WAF rules across specific resources** – Define a set of AWS WAF rules that apply only to a specific set of resources. This set can be a specific business unit or application that you identify by AWS account ID, OU, tag, or Amazon Resource Names (ARNs).
+ **Verify DDoS protection on internet-facing resources** – Create an AWS Shield Advanced policy scoped to public resource types and deploy it organization-wide so that critical resources have DDoS protection enabled.
+ **Detect and remediate configuration drift** – Use synchronization status monitoring to identify resources whose firewall configurations have drifted from the intended state, and optionally enable automatic remediation to bring them back into compliance.
+ **Delegate security management to multiple teams** – Designate multiple administrator accounts with different priority levels and scoped access to specific accounts, organizational units, or firewall types, allowing teams to manage their own security policies within defined boundaries.

## Related services
<a name="what-is-related-services"></a>
+ **AWS WAF** – Use AWS WAF to protect your web applications and APIs against common web exploits and bots that might affect availability, compromise security, or consume excessive resources. AWS Network Security Manager uses AWS WAF to create and manage web ACLs and rule groups for resources in a single account or across accounts in your organization.
+ **AWS Shield Advanced** – A managed DDoS protection service that provides expanded protections for your applications running on AWS. AWS Network Security Manager uses Shield Advanced to provide DDoS protections for resources in a single account or across accounts in your organization.
+ **AWS Organizations** – Helps you centrally manage and govern your environment as you grow and scale your AWS resources. AWS Network Security Manager requires AWS Organizations to manage protections across member accounts.
+ **AWS Config** – A service that enables you to assess, audit, and evaluate the configurations of your AWS resources. AWS Network Security Manager uses a service-linked AWS Config recorder to discover resources in your member accounts.

## Accessing AWS Network Security Manager
<a name="what-is-accessing"></a>

You can access AWS Network Security Manager through the following interfaces:

AWS Management Console  
A web-based interface for managing AWS Network Security Manager resources.   
Open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).

AWS Command Line Interface (AWS CLI)  
Provides commands for AWS Network Security Manager operations. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

AWS SDKs  
AWS provides SDKs that consist of libraries and sample code for various programming languages and platforms. The SDKs provide a convenient way to create programmatic access to AWS Network Security Manager. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/).

AWS Network Security Manager API  
A REST API that uses JSON over HTTPS. The API endpoint format is `network-security-manager.{{{region}}}.api.aws`. For more information, see the [AWS Network Security Manager API Reference](https://docs.aws.amazon.com/network-security-manager/latest/APIReference/).

To get started with AWS Network Security Manager, see [Setting up AWS Network Security Manager](setting-up.md) and [Deploy your first network security protection](getting-started.md).

## Pricing
<a name="what-is-pricing"></a>

You pay for each in-scope resource that AWS Network Security Manager monitors and protects. Additional charges apply for the underlying security services that you deploy, such as AWS WAF and AWS Shield Advanced. For detailed pricing information, see [AWS Network Security Manager pricing](https://aws.amazon.com/network-security-manager/pricing/) on the AWS website.

## Are you a first-time user?
<a name="what-is-first-time"></a>

If you are a first-time user of AWS Network Security Manager, we recommend that you read the following topics in order:

1. [How AWS Network Security Manager works](concepts.md) – Learn about the resource model, lifecycle states, policy merging, and synchronization.

1. [Setting up AWS Network Security Manager](setting-up.md) – Complete the prerequisites for using AWS Network Security Manager.

1. [Deploy your first network security protection](getting-started.md) – Walk through an end-to-end tutorial that creates your first deployment.