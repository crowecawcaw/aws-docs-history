**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using Automatic application layer DDoS mitigation with Firewall Manager Shield Advanced policies

This page explains how Automatic application layer DDoS mitigation works with Firewall Manager.

When you apply a Shield Advanced policy to Amazon CloudFront distributions or Application Load Balancers, you have the option of configuring Shield Advanced automatic application layer DDoS mitigation in the policy.

For information about Shield Advanced automatic mitigation, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

Shield Advanced automatic application layer DDoS mitigation has the following requirements:

- Automatic application layer DDoS mitigation works only with Amazon CloudFront distributions and Application Load Balancers.

If applying your Shield Advanced policy to Amazon CloudFront distributions, you can choose this option for Shield Advanced policies that you create for the **Global** Region. If applying protections to Application Load Balancers, you can apply the policy to any Region that Firewall Manager supports.

- Automatic application layer DDoS mitigation works only with protection packs (web ACLs) that were created using the latest version of AWS WAF (v2).

Because of this, if you have a policy that uses AWS WAF Classic web ACLs,
you need to either replace the policy with a new policy, which will
automatically use the latest version of AWS WAF, or have Firewall Manager create new
version web ACLs for your existing policy and switch over to using them. For
more information about the options, see [Replace AWS WAF Classic
web ACLs with latest version web ACLs](#shield-policies-auto-app-layer-update-waf-version "#shield-policies-auto-app-layer-update-waf-version").

## Automatic mitigation configuration

The automatic application layer DDoS mitigation option for Firewall Manager Shield Advanced policies applies Shield Advanced
automatic mitigation functionality to your policy's in-scope accounts
and resources. For detailed information about this Shield Advanced feature, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

You can choose to have Firewall Manager enable or disable automatic mitigation for the CloudFront
distributions or Application Load Balancers that are in scope of the policy, or you can choose to have the
policy ignore Shield Advanced automatic mitigation settings:

- **Enable** – If you choose to enable automatic mitigation, you also specify whether mitigating Shield Advanced rules should
  count or block matching web requests. Firewall Manager will mark in-scope resources
  as noncompliant if they either don't have automatic mitigation enabled,
  or are using a rule action that doesn't match the one you specify for
  the policy. If you configure the policy for automatic remediation, Firewall Manager
  updates noncompliant resources as needed.
- **Disable** – If you choose to disable automatic
  mitigation, Firewall Manager will mark in-scope resources as noncompliant if they
  have automatic mitigation enabled. If you configure the policy for
  automatic remediation, Firewall Manager updates noncompliant resources as needed.
- **Ignore** – If you choose to ignore automatic mitigation, Firewall Manager won't consider any of the automatic mitigation settings in your Shield policy when it performs remediation activities for the policy. This setting allows you to control automatic mitigation through Shield Advanced, without having those settings overwritten by Firewall Manager. This setting doesn't apply to any Classic Load Balancers or Elastic IPs resources manged through Shield Advanced, because Shield Advanced doesn't currently support L7 automatic mitigation for those resources.

## Replace AWS WAF Classic

web ACLs with latest version web ACLs

Automatic application layer DDoS mitigation works only with protection packs (web ACLs) that were created using the latest version of AWS WAF (v2).

To determine the web ACL version for your Shield Advanced policy, see [Determining the version of AWS WAF that's
used by a Shield Advanced policy](shield-policies-identify-waf-version.md "shield-policies-identify-waf-version.md").

If you want to use automatic mitigation in your Shield Advanced policy, and your policy
currently uses AWS WAF Classic web ACLs, you can either create a new Shield Advanced
policy to replace your current one, or you can use the options described in this
section to replace earlier version web ACLs with new (v2) web ACLs inside your
current Shield Advanced policy. New policies always create web ACLs using the latest
version of AWS WAF. If you replace the entire policy, when you delete it, you can
have Firewall Manager delete all of the earlier version web ACLs as well. The rest of this
section describes your options for replacing the web ACLs inside your existing policy.

When you modify an existing Shield Advanced policy for Amazon CloudFront resources, Firewall Manager can
automatically create a new empty AWS WAF (v2) web ACL for the policy, in any
in-scope account that doesn't already have a v2 web ACL. When Firewall Manager creates a
new web ACL, if the policy already has an AWS WAF Classic web ACL in the same
account, Firewall Manager configures the new version web ACL with the same default action
setting as the existing web ACL. If there is no existing AWS WAF Classic web
ACL, Firewall Manager sets the default action to Allow in the new web ACL. After
Firewall Manager creates a new web ACL, you can customize it as needed through the AWS WAF
console.

When you choose any of the following policy configuration options, Firewall Manager
creates new (v2) web ACLs for in-scope accounts that don't already have them:

- When you enable or disable automatic application layer DDoS mitigation. This choice alone only causes
  Firewall Manager to create the new web ACLs, and not to replace any existing
  AWS WAF Classic web ACL associations on the policy's in-scope
  resources.
- When you choose the policy action of automatic remediation and you choose the option to
  replace AWS WAF Classic web ACLs with AWS WAF (v2) web ACLs. You can
  choose to replace earlier version web ACLs regardless of your
  configuration choices for automatic application layer DDoS mitigation.

When you choose the replacement option, Firewall Manager creates the new version web ACLs as needed
and then does the following for the policy's in-scope resources:

    + If a resource is associated with a web ACL from any other active Firewall Manager policy, Firewall Manager
     leaves the association alone.
    + For any other case, Firewall Manager removes any association with an AWS WAF Classic web ACL and
     associates the resource with the policy's AWS WAF (v2) web ACL.

You can choose to have Firewall Manager replace the earlier version web ACLs with the new version web
ACLs when you want to. If you've previously customized the policy's
AWS WAF Classic web ACLs, you can update new version web ACLs to comparable
settings before you choose to have Firewall Manager perform the replacement step.

You can access either version of web ACL for a policy through the same-version console for
AWS WAF or AWS WAF Classic.

Firewall Manager doesn't delete any replaced AWS WAF Classic web ACLs until you delete
the policy itself. After the AWS WAF Classic web ACLs are no longer used by the
policy, you can delete them if you want to.
