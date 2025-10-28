# Certificates

## How can I use

Lightsail-provisioned certificates?

SSL/TLS certificates are used to establish the identity of your website or application
and secure connections between browsers and your website. Lightsail provides a signed
certificate to use with your load balancer, and the load balancer provides SSL/TLS
termination before routing verified traffic to your target instances over the secure AWS
network. Lightsail certificates can only be used with Lightsail load balancers, not with
individual Lightsail instances.

## How do I validate my

certificate?

Lightsail certificates are domain validated, meaning that you need to provide proof of
identity by validating that you own or have access to your website’s domain before the
certificate can be provisioned by the certificate authority. When you request a new
certificate, Lightsail will attempt to automatically validate the certificate. If the
certificate cannot be validated automatically, Lightsail will prompt you to add a CNAME
record to the DNS zone(s) of the domain or domains you are validating. You’ll have 72 hours
to add the CNAME record wherever you currently manage your DNS zones – either Lightsail
DNS management or an external DNS hosting provider.

## What happens if I cannot

validate my domain?

You must be able to validate that you own a domain for security purposes. This means if
you or someone in your organization can't add a DNS record to validate your certificate for
any reason, you will not be able to use an HTTPS-enabled load balancer with
Lightsail.

## How many domains and subdomains

can I add to my certificate?

You can add up to 10 domains or subdomains per certificate. Lightsail does not
currently support wild card domains.

## How can I change the domains

associated with my certificate?

To change the domains (add/delete) associated with your certificate, you will need to
resubmit the certificate and revalidate your ownership of the domain(s). Follow the steps in
the certificate management screens to regenerate your certificate and add or remove domains
when prompted.

## How do I renew my certificate?

Lightsail provides managed renewal for your SSL/TLS certificates. This means that
Lightsail tries to renew the certificates automatically before they expire with no action
required from you. Your Lightsail certificate must be actively associated with a load
balancer before it can be automatically renewed.

## What happens to my

certificate when I delete my load balancer?

If your load balancer is deleted, your certificate is deleted as well. If you need to
use a certificate for the same domain(s) in the future, you will need to request and
validate a new certificate.

## Can I download my

certificate provided by Lightsail?

No, Lightsail certificates are bound to your Lightsail account and cannot be removed
and used outside of Lightsail.
