# Domains to add to your allow list

If you filter access to specific AWS domains or URL endpoints by using a web content
filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG),
you must add the following domains or URL endpoints to your web-content filtering solution
allowlists.

## AWS Sign-In domains to allowlist

If you or your organization implement IP or domain filtering, you may need to
allowlist domains to use the AWS Management Console. The following domains must be
accessible on the network from which you are trying to access the AWS Management Console.

- ``[Region]`.signin.aws`
- ``[Region]`.signin.aws.amazon.com`
- `signin.aws.amazon.com`
- `*.cloudfront.net`
- `opfcaptcha-prod.s3.amazonaws.com`

## AWS access portal domains to

allowlist

If you filter access to specific AWS domains or URL endpoints by using a web content
filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways
(SWG), you must add the following domains or URL endpoints to your web-content filtering
solution allowlists. Doing so enables you to access your AWS access portal.

- ``[Directory ID or
alias]`.awsapps.com`
- `*.aws.dev`
- `*.awsstatic.com`
- `*.console.aws.a2z.com`
- `oidc.`[Region]`.amazonaws.com`
- `*.sso.amazonaws.com`
- `*.sso.`[Region]`.amazonaws.com`
- `*.sso-portal.`[Region]`.amazonaws.com`

## AWS Builder ID domains to allowlist

If you or your organization implement IP or domain filtering, you may need to
allowlist domains to create and use an AWS Builder ID. The following domains must be
accessible on the network from which you are trying to access AWS Builder ID.

- `view.awsapps.com/start`
- `*.aws.dev`
- `*.uis.awsstatic.com`
- `*.console.aws.a2z.com`
- `oidc.*.amazonaws.com`
- `*.sso.amazonaws.com`
- `*.sso.*.amazonaws.com`
- `*.sso-portal.*.amazonaws.com`
- `*.signin.aws`
- `*.cloudfront.net`
- `opfcaptcha-prod.s3.amazonaws.com`
- `profile.aws.amazon.com`
