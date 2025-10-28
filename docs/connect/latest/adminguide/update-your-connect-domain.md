# Update your Amazon Connect domain

Amazon Connect instances that were created before March 31, 2021, were given a domain that
looks like this:

- https://`your-instance-alias`.**awsapps.com/connect/**
  If you have one of these domains, we urge you to change it immediately. Change it
  to:

- https://`your-instance-alias`.**my.connect.aws/**
  In the near future we plan to automatically change any remaining old domains that
  appear in the AWS console—including the emergency access URL—to the new
  URL.

- If anyone tries to access a URL with the old domain, they will be redirected
  automatically to the new one.
- If you have any custom code, a connector, or a firewall, it is your
  responsibility to update all references to your Amazon Connect URL from your old domain
  to your new domain.
- Automatic redirection from the old domain to the new one is only for any
  references you may have accidentally missed, for example, users still clicking
  on old favorites.
  **Perform the steps in this topic to help you PREPARE for when we
  automatically change your old domain name** (that is, redirect traffic from
  your old domain to the new one).

For example, if your old link looks like this:

- https://`examplecorp`.**awsapps.com/connect/**
  **Change to:**

- https://`examplecorp`.**my.connect.aws/**
  Continue reading this topic if you use a firewall, SAML, or other connectors such as
  Salesforce. This topic provides information you need to consider when migrating to the
  new domain.

###### Contents

- [Custom code and
  integrations](#new-domain-custom "#new-domain-custom")
- [Firewall allow
  list](#new-domain-allow-list "#new-domain-allow-list")
- [About the Amazon Connect access URL and
  emergency login](#about-access-url "#about-access-url")
- [Personal settings](#new-domain-settings "#new-domain-settings")
- [Transport Layer Security
  (TLS)](#new-domain-tls "#new-domain-tls")

## Custom code and integrations

If you have any customization that involves Amazon Connect, review its code and replace
hard-coded references to the previous domain with the new domain. For example, if
you have a custom Contact Control Panel (CCP) integration, it likely relies on
embedded URLs. Following are tips for updating other types of integration.

### Active Directory

If you use Active Directory to manage identity and have an [Amazon Connect managed or customer
managed](connect-identity-management.md "connect-identity-management.md") instance, then update [ccpUrl](https://github.com/amazon-connect/amazon-connect-streams#connectcoreinitccp "https://github.com/amazon-connect/amazon-connect-streams#connectcoreinitccp") to the new domain. The next time a user accesses the CCP
they will be prompted to login to the new domain (one time only).

### SAML 2.0

If you use SAML 2.0 to manage identity, then do the following steps:

- Update `ccpUrl` in your [Amazon Connect Streams](https://github.com/amazon-connect/amazon-connect-streams#connectcoreinitccp "https://github.com/amazon-connect/amazon-connect-streams#connectcoreinitccp") to the new domain
  ``your-instance-alias`.my.connect.aws/ccp-v2`.
- When you configure the relay state for your identity provider, update
  the `loginUrl` with `new_domain=true`.
- You must use [URL
  encoding](https://en.wikipedia.org/wiki/Percent-encoding "https://en.wikipedia.org/wiki/Percent-encoding") for the destination and new_domain in the
  URL.

If you have old instances that were set up with SAML, do the following
steps:

1. If `loginUrl` contains
   `destination=%2Fconnect%2F`your-destination-endpoint``,
remove the `%2Fconnect` endpoint prefix from the new domain
   destination.
2. Add `new_domain=true` before or after
   `destination=%2F`your-destination-endpoint``.
It should be separated by `&`.
3. If `loginUrl` does not contain destination or any other
   parameter, add `?new_domain=true` after the relay state
   URL.

Following are examples of valid relay state URLs:

- `https://us-east-1.console.aws.amazon.com/connect/federate/`your-instance-id`?destination=%2Fccp-v2%2Fchat&new_domain=true`
- `https://us-east-1.console.aws.amazon.com/connect/federate/`your-instance-id`?new_domain=true`

###### Note

If the RelayState is itself a parameter to another URL, then the whole
RelayState itself must be URL encoded, on top of any URL encoding previously
done on the `destination`. For example, if the derived RelayState
was
`https://us-east-1.console.aws.amazon.com/connect/federate/your-instance-id?destination=%2Fccp-v2%2Fchat&new_domain=true`,
and it needs to be inserted in
`https://my.idp.com/signin?RelayState=<here>`, then the
final URL should look like
`https://my.idp.com/signin?RelayState=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fconnect%2Ffederate%2Fyour-instance-id%3Fdestination%3D%252Fccp-v2%252Fchat%26new_domain%3Dtrue.`
The URL encoding is crucial to allow it to be parsed correctly in a [query string](https://en.wikipedia.org/wiki/Query_string "https://en.wikipedia.org/wiki/Query_string").

### Other connectors

If you use Salesforce, Zendesk, ServiceNow, or other connectors:

1. Upgrade to the latest version of your connector.
2. In your connector, go to the settings and update the Amazon Connect domain that
   is stored there. Follow the SAML tips if applicable.

## Firewall allowlist

Add the following new domains to your allowlist:

- `your-instance-alias`.my.connect.aws
- \*.static.connect.aws

###### Important

Do not remove the domains already in your allowlist, such as the following
domains:

- `your-instance-alias`.awsapps.com/connect/ccp-v2
- `your-instance-alias`.awsapps.com/connect/api
- \*.cloudfront.net
  Keeping these domains in your allow list will ensure a smooth transition. You
  can remove them later, after the migration is complete.

For more information about setting up your allowlist, see [Set up your network](ccp-networking.md "ccp-networking.md").

## About the Amazon Connect access URL and emergency

login

The Amazon Connect access URL and emergency login URLs will be updated in the AWS console
after we complete the domain migration. Until that time, they will reflect the old
domain.

The following image shows the location of the access URL on the **Amazon Connect
virtual contact center instances** page. Even if you have taken steps
to update your domain, this URL will continue to show the old domain. The URL on
this page will update automatically when old domain traffic starts to redirect to
the new domain. Please **do not use this URL to log
in**; rather, communicate to your team the new URL that they should be
using.

![The access URL on the Amazon Connect console.](images/access-url.png)

The following image shows the location of the emergency login URL on the
**Account overview** page. This URL will lead to the old domain
until traffic starts to automatically redirect to the new domain. Please **refrain from using this URL to log in unless it is an
emergency**. Instead, log in with your username and password from the
login page associated with your new domain.

![The emergency login link on the Account overview page.](images/emergency-login.png)

## Personal settings

Notify your team to the upcoming change so they can take steps to prevent
confusion and disruption. If you have internal documentation that includes links,
please review and update accordingly. Encourage team members to update their browser
bookmarks _for the login page_, and productivity apps, such as
Alfred.

To ensure a seamless transition for your team, we encourage you to take steps to
identify any URL references.

## Transport Layer Security (TLS)

If your agents are using [browsers that
Amazon Connect supports](connect-supported-browsers.md "connect-supported-browsers.md"), there is no action for you. For example, if you are using
the latest Chrome and Firefox versions, no action is needed.

If you are using TLS 1.1 and below, you need to upgrade your tools to support the
TLS 1.1+ protocols.

We require your TLS protocol to be TLS 1.2 and recommend TLS 1.3.
The new domain does not support TLS 1.1 and TLS 1.0.

We recommend that you review the new TLS policy: [ALB FS-1-2-Res-2019-08](../../../elasticloadbalancing/latest/application/create-https-listener.md#tls-security-policies "../../../elasticloadbalancing/latest/application/create-https-listener.md#tls-security-policies"). For reference, you can find the previous TLS
policy here: [CloudFront TLSv1](../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md#secure-connections-supported-ciphers "../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md#secure-connections-supported-ciphers").
