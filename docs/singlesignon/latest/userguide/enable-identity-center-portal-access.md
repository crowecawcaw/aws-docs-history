# Update firewalls and gateways to

allow access to the AWS access portal

The AWS access portal provides users with single sign-on access to all your AWS accounts and
most commonly used cloud applications such as Office 365, Concur, Salesforce, and many more.
You can quickly launch multiple applications simply by choosing the AWS account or
application icon in the portal.

###### Note

AWS managed applications integrate with IAM Identity Center and use it for authentication and
directory services, but might not use the AWS access portal for application access.

If you filter access to specific AWS domains or URL endpoints by using a web content
filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG),
you must allowlist the domains and URL endpoints associated with the AWS access portal.

The following list provides the IPv4 and dual-stack domains and URL endpoints to add to your web-content filtering solution allowlists.

###### IPv4 allow list

- ``[Directory ID or alias]`.awsapps.com`
- `*.aws.dev`
- `*.awsstatic.com`
- `*.console.aws.a2z.com`
- `oidc.`[Region]`.amazonaws.com`
- `*.sso.amazonaws.com`
- `*.sso.`[Region]`.amazonaws.com`
- `*.sso-portal.`[Region]`.amazonaws.com`
- ``[Region]`.prod.pr.panorama.console.api.aws/panoramaroute`
- ``[Region]`.signin.aws`
- ``[Region]`.signin.aws.amazon.com`
- `signin.aws.amazon.com`
- `*.cloudfront.net`
- `opfcaptcha-prod.s3.amazonaws.com`

###### Dual-stack allow list

- `ssoins-`[IdC Instance ID]`.portal.`[Region]`.app.aws`
- `*.aws.dev`
- `*.awsstatic.com`
- `*.console.aws.a2z.com`
- `oidc.`[Region]`.api.aws`
- `sso.`[Region]`.api.aws`
- `portal.sso.`[Region]`.api.aws`
- ``[Region]`.sso.signin.aws`
- ``[Region]`.signin.aws.amazon.com`
- `signin.aws.amazon.com`
- `*.cloudfront.net`
- `cdn.us-east-1.threat-mitigation.aws.amazon.com`
- `us-east-1.threat-mitigation.aws.amazon.com`
- `amcs-captcha-prod-us-east-1.s3.dualstack.us-east-1.amazonaws.com`

###### Combined allow list (IPv4 + Dual-stack with backward compatibility)

- ``[Directory ID or alias]`.awsapps.com`
- `ssoins-`[IdC Instance ID]`.portal.`[Region]`.app.aws`
- `*.aws.dev`
- `*.awsstatic.com`
- `*.console.aws.a2z.com`
- `oidc.`[Region]`.amazonaws.com`
- `oidc.`[Region]`.api.aws`
- `*.sso.amazonaws.com`
- `*.sso.`[Region]`.amazonaws.com`
- `sso.`[Region]`.api.aws`
- `*.sso-portal.`[Region]`.amazonaws.com`
- `portal.sso.`[Region]`.api.aws`
- ``[Region]`.prod.pr.panorama.console.api.aws/panoramaroute`
- ``[Region]`.signin.aws`
- ``[Region]`.sso.signin.aws`
- ``[Region]`.signin.aws.amazon.com`
- `signin.aws.amazon.com`
- `*.cloudfront.net`
- `opfcaptcha-prod.s3.amazonaws.com`
- `cdn.us-east-1.threat-mitigation.aws.amazon.com`
- `us-east-1.threat-mitigation.aws.amazon.com`
- `amcs-captcha-prod-us-east-1.s3.dualstack.us-east-1.amazonaws.com`

## Considerations for allowlisting domains and URL endpoints

In addition to the allowlist requirements for the AWS access portal, the other services and applications you use might require allowlisting of domains.

- To access AWS accounts, the AWS Management Console, and the IAM Identity Center console from your
  AWS access portal, you must allowlist additional domains. Refer to [Troubleshooting](../../../awsconsolehelpdocs/latest/gsg/troubleshooting.md "../../../awsconsolehelpdocs/latest/gsg/troubleshooting.md") in the _AWS Management Console Getting Started
  Guide_ for a list of AWS Management Console domains.
- To access AWS managed applications from your AWS access portal, you must allowlist
  their respective domains. Refer to the respective service documentation for
  guidance.
- If you use external software, such as
  external IdPs (for example, Okta and Microsoft Entra
  ID), you'll need to include their domains in your allowlists.
