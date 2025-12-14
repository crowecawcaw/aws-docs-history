**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Web ACL management for AWS WAF policies

Firewall Manager creates and manages web ACLs for in-scope resources according to your configuration settings and general policy management.

###### Note

If a resource that's configured with [advanced automatic application layer DDoS mitigation](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") comes into scope of an AWS WAF policy, Firewall Manager will be unable to apply the policy protections to the resource and will mark the resource noncompliant.

###### Manage unassociated web ACLs configuration

Policy configuration setting that specifies
how Firewall Manager manages web ACLs for accounts when the web ACLs won't be used by any resource. If you enable
management of unassociated web ACLs, Firewall Manager creates web ACLs in accounts that are within policy scope
only if the web ACLs will be used by at least one resource. If you don't enable this option, Firewall Manager
automatically ensures that each account has a web ACL regardless of whether the web ACL will be used.

When this is enabled, when an account comes into policy scope, Firewall Manager automatically creates a web ACL
in the account only if at least one resource will use the web ACL.

Additionally, when you enable management of unassociated web ACLs, at policy creation, Firewall Manager performs a one-time cleanup of unassociated web ACLs in your account. During this cleanup, Firewall Manager skips any web ACLs that you've modified after their creation, for example, if you added a rule group to the web ACL or modified its settings. The cleanup process can take several hours. If a resource leaves policy scope after Firewall Manager creates a web ACL, Firewall Manager disassociates the resource from the web ACL, but won't clean up the unassociated web ACL. Firewall Manager only cleans up unassociated web ACLs when you first enable management of unassociated web ACLs in a policy.

In the API, this setting is `optimizeUnassociatedWebACL` in the [SecurityServicePolicyData](../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md "../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md") data type. Example: `\"optimizeUnassociatedWebACL\":false`

###### Web ACL source configuration: Create all new or retrofit existing?

Policy configuration setting that specifies what Firewall Manager does with existing web ACLs that are associated with in-scope resources.

By default, Firewall Manager creates all new web ACLs for in-scope resources. With retrofitting,
Firewall Manager uses any existing web ACLs that are already in use, and only creates new web ACLs for
resources that don't already have one associated.

When a policy is configured for retrofitting, all web ACLs that are associated with in-scope resources are retrofitted or marked noncompliant.

Firewall Manager only retrofits a web ACL if it satisfies the following requirements:

- The web ACL is owned by a customer account.
- The web ACL is only associated with in-scope resources.

###### Tip

Before you configure an AWS WAF policy for retrofitting, make sure that the web ACLs that are associated with
the policy's in-scope resources aren't associated with any out-of-scope resources.

###### Tip

If you want to delete an associated resource, first disassociate it from the web ACL.
If a web ACL is noncompliant due to an association with an out-of-scope resource, deleting the out-of-scope resource
without first disassociating it from the web ACL can bring the web ACL into compliance, and Firewall Manager can then retrofit the web ACL through
remediation, but the remediation in this situation can be delayed by up to 24 hours.
For information about accessing compliance violation details, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md").

If a web ACL can be retrofitted, Firewall Manager modifies it as follows:

- Firewall Manager inserts the AWS WAF policy's first rule groups in front of the web ACL's existing rules
  and appends the AWS WAF policy's last rule groups at the end. For information about rule group management, see
  [Rule group management for AWS WAF policies](waf-policies-rule-groups.md "waf-policies-rule-groups.md").
- If the policy has a logging configuration, then Firewall Manager adds it to the web ACL only if the web ACL
  isn't already configured for logging. If the web ACL has logging configured by the account,
  Firewall Manager leaves it in place both during the retrofitting and for any subsequent updates to the policy's logging configuration.
- Firewall Manager doesn't verify or configure any other web ACL properties.
  For example, Firewall Manager doesn't modify the web ACL's default action, custom request headers, CAPTCHA or Challenge
  configurations, or token domain lists. Firewall Manager only configures these other properties on web ACLs that Firewall Manager creates.
  After Firewall Manager retrofits all existing associated web ACLs, for any in-scope resource that doesn't have a web ACL, Firewall Manager
  handles the resource following the default policy behavior. If it's a resource that AWS WAF can protect, then Firewall Manager creates and associates a Firewall Manager
  web ACL with that resource.

In the API, the web ACL source setting is `webACLSource` in the [SecurityServicePolicyData](../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md "../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md") data type. Example: `\"webACLSource\":\"RETROFIT_EXISTING\"`

###### Sampling and CloudWatch metrics

AWS Firewall Manager enables sampling and Amazon CloudWatch metrics for the web ACLs and rule groups that it
creates for an AWS WAF policy.

###### Web ACL naming

A web ACL that Firewall Manager creates is named after the AWS WAF policy as follows:
`FMManagedWebACLV2-`policy
name`-`timestamp``. The timestamp is
 in UTC milliseconds. For example,
 `FMManagedWebACLV2-MyWAFPolicyName-1621880374078`.

A web ACL that Firewall Manager retrofits has the name that the customer account specified at creation. A web ACL name can't be changed after creation.

###### Note

If a resource configured with [advanced automatic application layer DDoS mitigation](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md")
comes into scope of a AWS WAF policy, Firewall Manager will be unable to associate the web ACL created by the AWS WAF policy to the resource.
