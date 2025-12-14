**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Using AWS Shield Advanced policies in Firewall Manager

This page explains how to use AWS Shield policies with Firewall Manager.
In a Firewall Manager AWS Shield policy, you choose the resources that you want to protect. When you apply the policy with auto remediation enabled, for each in-scope resource that's not already associated with a AWS WAF web ACL, Firewall Manager associates an empty AWS WAF web ACL. The empty web ACL is used for Shield monitoring purposes. If you then associate any other web ACL to the resource, Firewall Manager removes the empty web ACL association.

###### Note

When a resource that's in scope of an AWS WAF policy comes into the scope of a Shield Advanced policy configured with [automatic application layer DDoS mitigation](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md"), Firewall Manager applies the Shield Advanced protection only after associating the web ACL created by the AWS WAF policy.

## How AWS Firewall Manager manages unassociated web ACLs in Shield policies

You can configure whether Firewall Manager manages unassociated web ACLs for you through the **Manage unassociated web ACLs** setting in your policy, or the `optimizeUnassociatedWebACLs` setting in the [SecurityServicePolicyData](../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md "../../../fms/2018-01-01/APIReference/API_SecurityServicePolicyData.md") data type in the API. If you enable management of unassociated web ACLs in your policy, Firewall Manager creates web ACLs in the accounts within policy scope only if the web ACLs will be used by at least one resource. If at any time an account comes into policy scope, Firewall Manager automatically creates a web ACL in the account if at least one resource will use the web ACL.

When you enable management of unassociated web ACLs, Firewall Manager performs a one-time cleanup of unassociated web ACLs in your account. The cleanup process can take several hours. If a resource leaves policy scope after Firewall Manager creates a web ACL, Firewall Manager doesn't disassociate the resource from the web ACL. If you want Firewall Manager to clean up the web ACL, you must first manually disassociate the resources from the web ACL, and then enable the manage unassociated web ACLs option in your policy.

If you don't enable this option, Firewall Manager doesn't manage unassociated web ACLs, and Firewall Manager automatically creates a web ACL in each account that's within policy scope.

## How AWS Firewall Manager manages scope

changes in Shield policies

Accounts and resources can go out of scope of an AWS Firewall Manager Shield Advanced policy due to a number
of changes, such as changes to policy scope settings, changes to the tags on a
resource, and the removal of an account from an organization. For general
information about policy scope settings, see [Using the AWS Firewall Manager policy scope](policy-scope.md "policy-scope.md").

With an AWS Firewall Manager Shield Advanced policy, if an account or resource goes out of scope, Firewall Manager
stops monitoring the account or resource.

If an account goes out of scope by being removed from the organization, it will continue to be subscribed to Shield Advanced.
Because the account is no longer part of the consolidated billing family, the
account will incur a prorated Shield Advanced subscription fee. On the other hand, an account that goes
out of scope but remains in the organization doesn't incur additional fees.

If a resource goes out of scope, it continues to be protected by Shield Advanced and
continues to incur Shield Advanced data transfer charges.
