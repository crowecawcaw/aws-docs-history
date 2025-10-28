**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Specifying token domains and domain lists in AWS WAF

This section explains how to configure the domains that AWS WAF uses in tokens and that it
accepts in tokens.

When AWS WAF creates a token for a client, it configures it with a token domain. When
AWS WAF inspects a token in a web request, it rejects the token as invalid if its domain
doesn't match any of the domains that are considered valid for the protection pack (web ACL).

By default, AWS WAF only accepts tokens whose domain setting exactly matches the host
domain of the resource that's associated with the protection pack (web ACL). This is the value of the
`Host` header in the web request. In a browser, you can find this domain
in the JavaScript `window.location.hostname` property and in the address that
your user sees in their address bar.

You can also specify acceptable token domains in your protection pack (web ACL) configuration, as described in the following section. In this case, AWS WAF accepts both exact matches with the host header and matches with domains in the token domain list.

You can specify token domains for AWS WAF to use when setting the domain and
when evaluating a token in a protection pack (web ACL). The domains that you specify can't be public
suffixes such as `gov.au`. For the domains that you can't use, see the list
[https://publicsuffix.org/list/public_suffix_list.dat](https://publicsuffix.org/list/public_suffix_list.dat "https://publicsuffix.org/list/public_suffix_list.dat") under [Public suffix list](https://publicsuffix.org/list/ "https://publicsuffix.org/list/").

## AWS WAF protection pack (web ACL) token domain list configuration

You can configure a protection pack (web ACL) to share tokens across multiple protected resources
by providing a token domain list with the additional domains that you want AWS WAF to
accept. With a token domain list, AWS WAF still accepts the resource's host domain.
Additionally, it accepts all domains in the token domain list, including their
prefixed subdomains.

For example, a domain specification `example.com` in your token domain list
matches `example.com` (from `http://example.com/`),
`api.example.com`, (from `http://api.example.com/`), and
`www.example.com` (from `http://www.example.com/`). It doesn't
match `example.api.com`, (from `http://example.api.com/`), or
`apiexample.com` (from `http://apiexample.com/`).

You can configure the token domain list in your protection pack (web ACL) when you create or edit it.
For general information about managing a protection pack (web ACL), see [Viewing web traffic metrics in AWS WAF](web-acl-working-with.md "web-acl-working-with.md").

## AWS WAF token domain settings

AWS WAF creates tokens at the request of the challenge scripts, which are run by the
application integration SDKs and the Challenge and CAPTCHA rule actions.

The domain that AWS WAF sets in a token is determined by the type of challenge script
that's requesting it and any additional token domain configuration that you provide. AWS WAF
sets the domain in the token to the shortest, most general setting that it can find in
the configuration.

- **JavaScript SDK** – You can configure the
  JavaScript SDK with a token domain specification, which can include one or more
  domains. The domains that you configure must be domains that AWS WAF will accept,
  based on the protected host domain and the protection pack (web ACL)'s token domain list.

When AWS WAF issues a token for the client, it sets the token domain to one that
matches the host domain and is the
shortest, from among the host domain and the domains in your configured list. For example,
if the host domain is `api.example.com` and the token domain list has
`example.com`, AWS WAF uses `example.com` in the token,
because it matches the host domain and is shorter. If you don't provide a token
domain list in the JavaScript API configuration, AWS WAF sets the domain to the
host domain of the protected resource.

For more information, see [Providing domains for use in the
tokens](waf-js-challenge-api-set-token-domain.md "waf-js-challenge-api-set-token-domain.md").

- **Mobile SDK** – In your application code, you must configure the
  mobile SDK with a token domain property. This property must be a domain that AWS WAF
  will accept, based on the protected host domain and the protection pack (web ACL)'s token domain list.

When AWS WAF issues a token for the client, it uses this property
as the token domain. AWS WAF doesn't use the host domain in the tokens that it issues for the mobile SDK client.

For more information, see the `WAFConfiguration`
`domainName` setting at [AWS WAF mobile SDK specification](waf-mobile-sdk-specification.md "waf-mobile-sdk-specification.md").

- **Challenge action** – If you
  specify a token domain list in the protection pack (web ACL), AWS WAF sets the token domain to one
  that matches the host domain and is the shortest, from among the host domain and
  the domains in the list. For example, if the host domain is
  `api.example.com` and the token domain list has
  `example.com`, AWS WAF uses `example.com` in the token,
  because it matches the host domain and is shorter. If you don't provide a token
  domain list in the protection pack (web ACL), AWS WAF sets the domain to the host domain of the
  protected resource.
