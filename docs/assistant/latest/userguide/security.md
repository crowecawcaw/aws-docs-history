

# Security in the AWS assistant
<a name="security"></a>

## Security best practices
<a name="security-best-practices"></a>

### Detective
<a name="security-best-practices-detective"></a>
+ Review the source links and API details in responses before you act on the information.
+ Review AWS CloudTrail events for the compatibility-sensitive `q` service prefix and for downstream service operations that the AWS assistant performs on your behalf.
+ Review access-denied responses and the applicable identity, session, permissions boundary, and organization policies.

### Preventative
<a name="security-best-practices-preventative"></a>
+ Give users only the permissions that they need to access the AWS assistant and the downstream services and resources in their requests.
+ Use a customer managed AWS Key Management Service (AWS KMS) key when that option is available and required by your organization.
+ Don't include confidential or sensitive information in resource names, tags, or other free-form fields that can appear in a request or response.

## Identity and access management
<a name="security-iam"></a>

Use IAM policies to control who can use the AWS assistant and which capabilities are available. The existing `q` service prefix, IAM actions, managed policies, service principals, ARNs, and AWS CloudTrail event names are compatibility-sensitive technical identifiers. The product name is now AWS assistant, but these identifiers are unchanged.

Common access patterns include policies that:
+ Permit users to chat with the AWS assistant in the AWS Management Console.
+ Allow access through an Amazon Q Developer Pro subscription.
+ Allow the AWS assistant to access a customer managed AWS KMS key.
+ Permit users to diagnose supported console errors.
+ Allow resource retrieval through read, list, and describe operations.
+ Allow access to cost and optimization data from AWS Cost Explorer, Cost Optimization Hub, AWS Compute Optimizer, AWS Budgets, and AWS Free Tier.
+ Allow access to AWS Pricing, AWS Savings Plans, and reservation recommendation APIs.
+ Allow or deny selected actions that the AWS assistant calls on your behalf, including restrictions based on `aws:CalledVia` or `aws:RequestedRegion`.

The AWS assistant can access only the resources and perform only the operations that your identity is authorized to access or perform.

For policies that implement these patterns, see [Identity-based policy examples for the AWS assistant](security-iam-examples.md).

## Logging and incident response
<a name="incident-response"></a>

AWS CloudTrail records the AWS assistant API calls as events under the compatibility-sensitive `q` service prefix. Use the information that CloudTrail collects to find the request that was made, the IP address that it came from, who made it, and when. If you don't configure a trail, you can still view recent events in **Event history** in the CloudTrail console. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

The AWS assistant also makes API calls with a `dryRun` parameter to verify that you have the necessary permissions for an action, without making the request. These calls are recorded in a CloudTrail log with `"dryRun" : true` in the `requestParameters` field.

If you suspect a security issue, contact AWS Support. For information about reporting a vulnerability, see [Vulnerability reporting](https://aws.amazon.com/security/vulnerability-reporting/).

## Compliance validation
<a name="compliance-validation"></a>

Our new AWS sign-up experience is not designed for regulated workloads. If you're using our new AWS sign-up experience, but you want to use AWS for regulated workloads, you can [sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) or [activate advanced features](https://docs.aws.amazon.com/accounts/latest/reference/activate-advanced-features.html) for your AWS environment.

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

## Resilience
<a name="resilience"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. Regions provide multiple physically separated and isolated Availability Zones. These Availability Zones are connected with low-latency, high-throughput, and highly redundant networking. The AWS assistant also uses cross-Region inference to distribute traffic within a geography during periods of high demand. For more information, see [Cross-Region inference](cross-region-processing.md#cross-region-inference).

For more information about Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Don't make operational recovery depend only on an AWS assistant response. Verify source links and use the applicable service console, API, or support process if the AWS assistant is unavailable.

## Infrastructure security
<a name="infrastructure-security"></a>

As a managed service, the AWS assistant is protected by the AWS global network security procedures described in [Security and compliance](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/security-and-compliance.html). Connections to the AWS assistant use TLS 1.2 or later.

Chatting with the AWS assistant in the AWS Management Console isn't supported through interface VPC endpoints (AWS PrivateLink).

For services that the AWS assistant calls on your behalf, use the network, endpoint, and access controls that each service documents.

## Configuration and vulnerability analysis
<a name="configuration-vulnerability-analysis"></a>

Configuration and IT controls are a shared responsibility between AWS and you, our customer. AWS manages the underlying infrastructure for the AWS assistant. You are responsible for configuring IAM permissions, customer managed keys, and the services that the AWS assistant calls on your behalf. For more information, see the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

Review [AWS security bulletins](https://aws.amazon.com/security/security-bulletins/) and the security guidance for each downstream service that you use with the AWS assistant.

## Cross-service confused deputy prevention
<a name="cross-service-confused-deputy"></a>

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

The AWS assistant calls other services with the permissions of your IAM identity. It can't perform an action that you aren't allowed to perform. When the AWS assistant calls a service on your behalf, the request includes `q.amazonaws.com` in the `aws:CalledVia` condition key. You can use this key to restrict the actions that the AWS assistant performs. For examples, see [Deny the AWS assistant permission to perform specific actions](security-iam-examples.md#iam-example-deny-some-actions) and [Allow the AWS assistant permission to perform specific actions](security-iam-examples.md#iam-example-allow-some-actions).

For general guidance, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.