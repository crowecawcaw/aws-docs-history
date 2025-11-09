# Troubleshoot DNS validation

problems

Consult the following guidance if you are having trouble validating a certificate with
DNS.

The first step in DNS troubleshooting is to check the current status of your domain with
tools such as the following:

- **dig** — [Linux](https://linux.die.net/man/1/dig "https://linux.die.net/man/1/dig"), [Windows](https://help.dyn.com/how-to-use-binds-dig-tool/ "https://help.dyn.com/how-to-use-binds-dig-tool/")
- **nslookup** — [Linux](https://linux.die.net/man/1/nslookup "https://linux.die.net/man/1/nslookup"), [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup")

###### Topics

- [Underscores prohibited by DNS provider](#underscores-prohibited "#underscores-prohibited")
- [Default trailing period added by DNS
  provider](#troubleshooting-trailing-period "#troubleshooting-trailing-period")
- [DNS validation on GoDaddy fails](#troubleshooting-DNS-GoDaddy "#troubleshooting-DNS-GoDaddy")
- [ACM Console does not display "Create records
  in Route 53" button](#troubleshooting-route53-1 "#troubleshooting-route53-1")
- [Route 53 validation fails on private (untrusted)
  domains](#troubleshooting-route53-2 "#troubleshooting-route53-2")
- [Validation is successful but
  issuance or renewal fails](#troubleshooting-dns-pending-violation "#troubleshooting-dns-pending-violation")
- [Validation fails for DNS server on a VPN](#troubleshooting-vpn "#troubleshooting-vpn")

## Underscores prohibited by DNS provider

If your DNS provider prohibits leading underscores in CNAME values, you can remove the
underscore from the ACM-provided value and validate your domain without it. For example,
the CNAME value `_x2.acm-validations.aws` can be changed to
`x2.acm-validations.aws` for validation purposes. However, the CNAME name
parameter must always begin with a leading underscore.

You can use either of the values on the right side of the table below to validate a
domain.

| Name                           | Type  | Value                                  |
| ------------------------------ | ----- | -------------------------------------- |
| `_<random value>.example.com.` | CNAME | `_<random value>.acm-validations.aws.` |
| `_<random value>.example.com.` | CNAME | `<random value>.acm-validations.aws.`  |

## Default trailing period added by DNS

provider

Some DNS providers add by default a trailing period to the CNAME value that you
provide. As a result, adding the period yourself causes an error. For example,
"`<random_value>.acm-validations.aws.`" is rejected while
"`<random_value>.acm-validations.aws`" is accepted.

## DNS validation on GoDaddy fails

DNS validation for domains registered with Godaddy and other registries may fail
unless you modify the CNAME values provided by ACM. Taking example.com as the domain
name, the issued CNAME record has the following form:

```
NAME: _ho9hv39800vb3examplew3vnewoib3u.example.com. VALUE: _cjhwou20vhu2exampleuw20vuyb2ovb9.j9s73ucn9vy.acm-validations.aws.
```

You can create a CNAME record compatible with GoDaddy by truncating the apex domain
(including the period) at the end of the NAME field, as follows:

```
NAME: _ho9hv39800vb3examplew3vnewoib3u VALUE: _cjhwou20vhu2exampleuw20vuyb2ovb9.j9s73ucn9vy.acm-validations.aws.
```

## ACM Console does not display "Create records

in Route 53" button

If you select Amazon Route 53 as your DNS provider, AWS Certificate Manager can interact directly with it
to validate your domain ownership. Under some circumstances, the console's
**Create records in Route 53** button may not be available when you expect
it. If this happens, check for the following possible causes.

- You are not using Route 53 as your DNS provider.
- You are logged into ACM and Route 53 through different accounts.
- You lack IAM permissions to create records in a zone hosted by Route 53.
- You or someone else has already validated the domain.
- The domain is not publicly addressable.

## Route 53 validation fails on private (untrusted)

domains

During DNS validation, ACM searches for a CNAME in a publicly hosted zone. When it
doesn't find one, it times out after 72 hours with a status of **Validation timed
out**. You cannot use it to host DNS records for private domains, including
resources in an Amazon VPC [private hosted zone](../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones "../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones"), untrusted domains in your private PKI, and self-signed
certificates.

AWS does provide support for publicly untrusted domains through the [AWS Private CA](https://aws.amazon.com/certificate-manager/private-certificate-authority/ "https://aws.amazon.com/certificate-manager/private-certificate-authority/") service.

## Validation is successful but

issuance or renewal fails

If certificate issuance fails with "Pending validation" even though DNS is correct,
check that issuance is not being blocked by a Certification Authority Authorization (CAA)
record. For more information, see [(Optional) Configure a CAA record](setup.md#setup-caa "setup.md#setup-caa").

## Validation fails for DNS server on a VPN

If you locate a DNS server on a VPN and ACM fails to validate a certificate against
it, check if the server is publicly accessible. Public certificate issuance using ACM
DNS validation requires that the domain records be resolvable over the public
internet.
