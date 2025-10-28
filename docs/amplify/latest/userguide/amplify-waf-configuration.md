# How Amplify integrates with AWS WAF

The following list provides specific details about how Firewall support is integrated with
AWS WAF and the constraints to consider when creating web ACLs and associating them with Amplify
apps.

- You can enable AWS WAF for any type of Amplify app. This includes any supported framework,
  server-side rendered (SSR) apps, and fully static sites. AWS WAF is supported for Amplify Gen 1
  and Gen 2 apps.
- You must create web ACLs that you want to associate with an Amplify app in the Global
  (CloudFront) Region. Regional web ACLs might already exist in your AWS account, but they are not
  compatible with Amplify.
- The web ACL and the Amplify app must be created in the same AWS account. You can use
  AWS Firewall Manager to replicate AWS WAF rules across AWS accounts, to simplify keeping organization
  rules centralized and distributed across multiple AWS accounts. For more information, see
  [AWS Firewall Manager](../../../waf/latest/developerguide/fms-chapter.md "../../../waf/latest/developerguide/fms-chapter.md")
  in the _AWS WAF Developer Guide_.
- You can share the same web ACL across multiple Amplify apps in the same AWS account.
  All of the apps must be in the same Region.
- When you associate a web ACL with an Amplify app, the web ACL attaches to every branch
  in the app by default. When you create new branches, they will have the web ACL.
- When you associate a web ACL to an Amplify app, it is automatically associated with all
  of the app’s domains. However, you can configure rules that apply to a single domain name using
  Host-header matching rules.
- You can't delete a web ACL that is associated with an Amplify app. Before you delete a
  web ACL in the AWS WAF console, you need to disassociate it from the app.

## Amplify web ACL resource policy

To allow Amplify to access your web ACL, a resource policy is attached to the web ACL
during association. Amplify constructs this resource policy automatically, but you can view it
using the AWS WAFV2 [GetPermissionPolicy](../../../waf/latest/APIReference/API_GetPermissionPolicy.md "../../../waf/latest/APIReference/API_GetPermissionPolicy.md") API. The
following IAM permissions are required for associating a web ACL to an Amplify app.

- amplify:AssociateWebACL
- wafv2:AssociateWebACL
- wafv2:PutPermissionPolicy
- wafv2:GetPermissionPolicy
