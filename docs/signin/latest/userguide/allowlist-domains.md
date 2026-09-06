

# Domains to add to your allow list
<a name="allowlist-domains"></a>

If you filter access to specific AWS domains or URL endpoints by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains or URL endpoints to your web-content filtering solution allowlists.

## AWS Sign-In domains to allowlist
<a name="allowlist-domains-sign-in"></a>

If you or your organization implement IP or domain filtering, you may need to allowlist domains to use the AWS Management Console. The following domains must be accessible on the network from which you are trying to access the AWS Management Console.
+ `{{[Region]}}.signin.aws`
+ `{{[Region]}}.signin.aws.amazon.com`
+ `signin.aws.amazon.com`
+ `*.cloudfront.net`
+ `opfcaptcha-prod.s3.amazonaws.com`

## AWS Sign-In administration domains to allowlist
<a name="allowlist-domains-admin"></a>

If you configure console access controls by using the AWS CLI, you must allowlist the AWS Sign-In control plane endpoint. This endpoint handles policy administration and is distinct from the console sign-in domains in the previous section.
+ `signin.{{[Region]}}.api.aws`

  Replace {{[Region]}} with the AWS Region you are calling. Available in all commercial Regions. Example: `signin.us-east-1.api.aws`.

## AWS access portal domains to allowlist
<a name="allowlist-domains-access-portal"></a>

If you filter access to specific AWS domains or URL endpoints by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains or URL endpoints to your web-content filtering solution allowlists. Doing so enables you to access your AWS access portal.

The following lists provide the IPv4 and dual-stack domains and URL endpoints to add to your web-content filtering solution allowlists. For more information about dual-stack endpoints, see [Update firewalls and gateways to allow access to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center-portal-access.html) in the *IAM Identity Center User Guide*.

**IPv4 allow list**
+ `{{[Directory ID or alias]}}.awsapps.com`
+ `{{[IAM Identity Center instance ID]}}.{{[Region]}}.portal.amazonaws.com`
+ `*.aws.dev`
+ `*.awsstatic.com`
+ `*.console.aws.a2z.com`
+ `oidc.{{[Region]}}.amazonaws.com`
+ `*.sso.amazonaws.com`
+ `*.sso.{{[Region]}}.amazonaws.com`
+ `*.sso-portal.{{[Region]}}.amazonaws.com`

**Dual-stack allow list**
+ `{{[IAM Identity Center instance ID]}}.portal.{{[Region]}}.app.aws`
+ `*.aws.dev`
+ `*.awsstatic.com`
+ `*.console.aws.a2z.com`
+ `oidc.{{[Region]}}.api.aws`
+ `sso.{{[Region]}}.api.aws`
+ `portal.sso.{{[Region]}}.api.aws`
+ `{{[Region]}}.sso.signin.aws`
+ `{{[Region]}}.signin.aws.amazon.com`
+ `signin.aws.amazon.com`
+ `*.cloudfront.net`
+ `cdn.us-east-1.threat-mitigation.aws.amazon.com`
+ `us-east-1.threat-mitigation.aws.amazon.com`
+ `amcs-captcha-prod-us-east-1.s3.dualstack.us-east-1.amazonaws.com`

## AWS Builder ID domains to allowlist
<a name="allowlist-domains-builder-id"></a>

If you or your organization implement IP or domain filtering, you may need to allowlist domains to create and use an AWS Builder ID. The following domains must be accessible on the network from which you are trying to access AWS Builder ID.
+ `view.awsapps.com/start`
+ `*.portal.*.app.aws`
+ `*.aws.dev`
+ `*.api.aws`
+ `*.uis.awsstatic.com`
+ `*.console.aws.a2z.com`
+ `oidc.*.amazonaws.com`
+ `oidc.*.api.aws`
+ `*.sso.amazonaws.com`
+ `*.sso.*.amazonaws.com`
+ `*.sso-portal.*.amazonaws.com`
+ `sso.*.api.aws`
+ `*.signin.aws`
+ `*.cloudfront.net`
+ `opfcaptcha-prod.s3.amazonaws.com`
+ `profile.aws.amazon.com`