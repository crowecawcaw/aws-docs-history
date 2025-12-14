**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Determining the version of AWS WAF that's

used by a Shield Advanced policy

This page explains how to determine which version of AWS WAF web ACL your Shield Advanced policy uses.

You can determine which version of AWS WAF your Firewall Manager Shield Advanced policy uses by looking at the
parameter keys in the policy's AWS Config service-linked rule. If the AWS WAF version
that's in use is the latest, the parameter keys include `policyId` and
`webAclArn`. If it's the earlier version, AWS WAF Classic, the
parameter keys include `webAclId` and `resourceTypes`.

The AWS Config rule only lists keys for the web ACLs that the policy is currently
using with in-scope resources.

###### To determine which version of AWS WAF your Firewall Manager Shield Advanced policy uses

1. Retrieve the policy ID for the Shield Advanced policy:
   1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2"). For information about setting up a Firewall Manager administrator account, see
      [AWS Firewall Manager prerequisites](fms-prereq.md "fms-prereq.md").
   2. In the navigation pane, choose **Security
      Policies**.
   3. Choose the Region for the policy. For CloudFront distributions, this is
      `Global`.
   4. Find the policy that you want and copy the value of its
      **Policy ID**.

   Example policy ID:
   `1111111-2222-3333-4444-a55aa5aaa555`.

2. Create the policy's AWS Config rule name by appending the policy ID to the
   string `FMManagedShieldConfigRule`.

Example AWS Config rule name:
`FMManagedShieldConfigRule1111111-2222-3333-4444-a55aa5aaa555`. 3. Search the parameters for the associated AWS Config rule for keys named
`policyId` and `webAclArn`:

    1. Open the AWS Config console at [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
    2. In the navigation pane, choose **Rules**.
    3. Find your Firewall Manager policy's AWS Config rule name in the list and select it.
     The rule's page opens.
    4. Under **Rule details**, in the **Parameters**
     section, look at the keys. If you find keys named
     `policyId` and `webAclArn`, the policy
     uses web ACLs that were created using the latest version of AWS WAF.
     If you find keys named `webAclId` and
     `resourceTypes`, the policy uses web ACLs that were
     created using the earlier version, AWS WAF Classic.
