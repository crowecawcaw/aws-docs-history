

# Managing web ACLs for AWS WAF
<a name="managing-waf"></a>

With AWS Network Security Manager, you centrally configure and deploy AWS WAF web access control lists (web ACLs) across accounts and resources in your organization. You can define AWS Network Security Manager rules for AWS WAF, group them into protection templates, and enforce them at scale through AWS Network Security Manager policies and deployments.

## AWS WAF concepts
<a name="concepts-waf"></a>

The following concepts are specific to using AWS Network Security Manager with AWS WAF. For more information about how AWS Network Security Manager works, see [How AWS Network Security Manager works](concepts.md).

### AWS WAF rule types
<a name="concepts-waf-rule-types"></a>

For AWS WAF, a rule is one of two types:
+ **INSPECTION** – Contains a rule group definition using `PreProcessFirewallManagerRuleGroups` (rules that run before customer-defined rules) or `PostProcessFirewallManagerRuleGroups` (rules that run after).
+ **CONFIGURATION** – Contains a single web ACL configuration setting. The configuration JSON must contain exactly one top-level key matching a supported setting (for example, `Description`, `DefaultAction`, `VisibilityConfig`, `LoggingConfiguration`, `CaptchaConfig`, `ChallengeConfig`, `CustomResponseBodies`, `DataProtectionConfig`, `AssociationConfig`, `OnSourceDDoSProtectionConfig`, `TokenDomains`, or `MonetizationConfig`).

Most web ACL configuration settings correspond to parameters of the AWS WAF `CreateWebACL` operation. For more information about these settings and their definitions, see [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html) in the *AWS WAF API Reference*.

The exception is `LoggingConfiguration`, which you configure separately. For more information, see [Logging web ACL traffic](#managing-waf-logging).

### AWS WAF policy merging
<a name="concepts-priority-waf"></a>

For AWS WAF, each configuration setting uses one of the following merge strategies:

SingleValue  
Settings that can have only one value. The highest-priority policy wins. Priority values are unique, so two policies cannot define different values at the same priority. For more information about how AWS Network Security Manager resolves priority, see [Priority-based policy merging](concepts.md#concepts-priority). The following settings use SingleValue: `DefaultAction`, `VisibilityConfig`, `CaptchaConfig`, `ChallengeConfig`, `OnSourceDDoSProtectionConfig`, `LoggingConfiguration`, `MonetizationConfig`, and `Description`.

Append (and AppendAndSort)  
Entries from all policies append to the list in priority order. `TokenDomains` and `DataProtectionConfig.DataProtections` use Append. `PreProcessFirewallManagerRuleGroups` and `PostProcessFirewallManagerRuleGroups` use AppendAndSort, which appends rule groups from all policies and sorts them by priority. Order matters because AWS WAF evaluates rule groups sequentially.

Merge  
Entries from all policies merge into a single set, regardless of priority. `CustomResponseBodies` and `AssociationConfig.RequestBody` use Merge.

The Append, AppendAndSort, and Merge strategies remove duplicate entries. When two policies contribute identical configuration, AWS Network Security Manager keeps the entry from the higher-priority policy. The effective configuration therefore contains one copy of that entry, not one copy per contributing policy.

### Existing web ACL resolution
<a name="concepts-waf-existing-webacl"></a>

Use the `existingCustomerWebACLResolution` setting on an AWS WAF policy to specify how AWS Network Security Manager handles resources that already have a customer-managed web ACL:
+ `RETROFIT` – Update your existing web ACL to align with the effective configuration.
+ `OVERRIDE_ASSOCIATION` – Associate a web ACL managed by AWS Network Security Manager with the resource instead.
+ `NO_REMEDIATION` – Do not remediate if your web ACL exists.

### Logging web ACL traffic
<a name="managing-waf-logging"></a>

You control web ACL logging with the `LoggingConfiguration` setting on a policy. AWS Network Security Manager applies this setting using the AWS WAF `PutLoggingConfiguration` operation. You can define one logging destination per web ACL. For more information, see [PutLoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutLoggingConfiguration.html) in the *AWS WAF API Reference*.

Every in-scope web ACL that the policy manages sends its logs to the destination that the policy specifies. This gives you centralized logging across the accounts in your organization. Use it to get detailed information about the traffic that your web ACLs analyze organization-wide.

For centralized logging across multiple accounts, you can send logs to an Amazon S3 bucket or an Amazon Data Firehose delivery stream. Each destination type requires additional configuration, which you must complete before AWS Network Security Manager can manage AWS WAF logging across your in-scope resources and accounts. The destination name must begin with `aws-waf-logs-`.

Amazon Data Firehose  
Create the delivery stream with the following characteristics:  
+ Created using your AWS Network Security Manager administrator account
+ A name that starts with `aws-waf-logs-`, for example `aws-waf-logs-network-security-manager-central`
+ A `PUT` source
+ Created in the Region where you operate, or in the US East (N. Virginia) Region if you capture logs for Amazon CloudFront
Before you use the delivery stream, test it to confirm that it has enough throughput for your organization's logs. For more information, see [Creating an Amazon Data Firehose delivery stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*.

Amazon S3  
Create the bucket following the Amazon S3 guidance in the *AWS WAF Developer Guide*. You must also configure the bucket with the permissions that allow log delivery to write to it. The following bucket policy grants those permissions.  

```
{
    "Version":"2012-10-17",
    "Id": "AWSLogDeliveryForNetworkSecurityManager",
    "Statement": [
        {
            "Sid": "AWSLogDeliveryAclCheckNetworkSecurityManager",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::aws-waf-logs-{{bucket-suffix}}"
        },
        {
            "Sid": "AWSLogDeliveryWriteNetworkSecurityManager",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::aws-waf-logs-{{bucket-suffix}}/{{policy-id}}/AWSLogs/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control"
                }
            }
        }
    ]
}
```
Replace {{bucket-suffix}} with your own bucket name suffix, and replace {{policy-id}} with the ID of your policy.

**CloudWatch Logs supports single-account use only**  
If you use AWS Network Security Manager across multiple accounts, you cannot use an Amazon CloudWatch Logs log group as the logging destination. The log group must be in the same AWS account and the same Region as the web ACL. For multi-account deployments, use an Amazon S3 bucket or an Amazon Data Firehose delivery stream instead.