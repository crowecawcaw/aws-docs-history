# Understanding DNS terminology

and concepts

If you are unfamiliar with the terms and concepts associated with Domain Name System
(DNS), the following topics can help you understand the procedures for adding custom
domains.

## DNS terminology

The following are a list of terms common to DNS. They can help you understand the
procedures for adding custom domains.

**CNAME**

A Canonical Record Name (CNAME) is a type of DNS record that masks the
domain for a set of webpages and makes them appear as though they are located
elsewhere. A CNAME points a subdomain to a fully qualified domain name (FQDN).
For example, you can create a new CNAME record to map the subdomain **www.example.com**, where **www** is the subdomain, to the FQDN domain **branch-name.d1m7bkiki6tdw1.cloudfront.net** assigned to your app
in the Amplify console.

**ANAME**

An ANAME record is like a CNAME record, but at the root level. An ANAME
points the root of your domain to an FQDN. That FQDN points to an IP
address.

**Name server**

A name server is a server on the internet that's specialized in handling
queries regarding the location of a domain name’s various services. If you set
up your domain in Amazon Route 53, a list of name servers are already assigned to
your domain.

**NS record**

An NS record points to name servers that look up your domain details.

## DNS verification

A Domain Name System (DNS) is like a phone book that translates human-readable domain
names into computer-friendly IP addresses. When you type
`https://google.com` into a browser, a lookup operation is
performed in the DNS provider to find the IP Address of the server that hosts the
website.

DNS providers contain records of domains and their corresponding IP Addresses. The
most commonly used DNS records are CNAME, ANAME, and NS records.

Amplify uses a CNAME record to verify that you own your custom domain. If you host
your domain with Route 53, verification is done automatically on your behalf. However, if
you host your domain with a third-party provider such as GoDaddy, you have to manually
update your domain’s DNS settings and add a new CNAME record provided by
Amplify.

## Custom domain activation

process

###### Warning

When initiating a DomainAssociation request for an Amplify app with a domain that is already or was previously associated with different Amplify App(s) in other AWS account(s) in the same region, this is considered a cross account domain association. Cross account domain association requests require manual verification. If you would like to proceed with a cross account domain association, please contact AWS support for assistance.

When you connect your Amplify app to a custom domain in the Amplify console,
there are several steps that Amplify must complete before you can view your app using
your custom domain. The following list describes each step in the domain set up and
activation process.

**SSL/TLS creation**

If you are using a managed certificate, AWS Amplify issues an SSL/TLS
certificate for setting up a secure custom domain.

**SSL/TLS configuration and verification**

Before issuing a managed certificate, Amplify verifies that you are the
owner of the domain. For domains managed by Amazon Route 53, Amplify automatically
updates the DNS verification record. For domains managed outside of Route 53, you
must manually add the DNS verification record provided in the Amplify console
into your domain with a third-party DNS provider.

If you are using a custom certificate, you are responsible for validating
domain ownership.

**Domain activation**

The domain is successfully verified. For domains managed outside of Route 53,
you need to manually add the CNAME records provided in the Amplify console
into your domain with a third-party DNS provider.
