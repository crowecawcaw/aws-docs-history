

# ACME domain validation
<a name="acm-acme-domain-validation"></a>

ACME domain validation resources pre-authorize which domains an ACME endpoint can issue certificates for. Unlike standard ACM domain validation (which you set up as part of a certificate request), ACME domain validations are persistent resources that the PKI administrator configures in advance. This separation enables application owners to request certificates without having to perform domain validation themselves.

Each domain validation requires a CNAME record in DNS. This is the same type of CNAME record used for standard ACM DNS validation. However, ACME domain validations are specific to individual endpoints. Different endpoints require separate CNAME records, even for the same domain.

## How ACME domain validation relates to standard ACM validation
<a name="acm-acme-dv-comparison"></a>

Both mechanisms use the same CNAME record format and purpose: proving domain ownership by placing a specific record in DNS, as described in [AWS Certificate Manager DNS validation](dns-validation.md). In both cases, the CNAME delegates ongoing domain validation to ACM. Because the record points to a target that ACM manages, ACM can re-validate domain ownership over time without further action from you. This is what lets ACM renew certificates automatically. The following list describes the key differences:
+ With standard ACM validation, you establish the CNAME as part of a certificate request, such as a call to `RequestCertificate`.
+ ACME domain validation is a persistent ACM resource that an administrator configures in advance, independent of any individual certificate request.
+ ACME domain validation includes a configurable scope that lets you control whether the endpoint can issue certificates for the exact domain, its subdomains, or wildcard names. For more information, see [Domain validation scope](#acm-acme-dv-scope).

## Domain validation scope
<a name="acm-acme-dv-scope"></a>

When you create a domain validation, you configure a scope that controls what certificates can be issued using this validation. The scope has three independent settings. For definitions of *apex domain* and *subdomain*, see [Domain Names](acm-concepts.md#concept-dn).

`ExactDomain` (`ENABLED`/`DISABLED`)  
Allow certificates for the exact domain that you specify. For example, if you specify the apex domain `example.com`, this setting allows certificates for `example.com`.

`Subdomains` (`ENABLED`/`DISABLED`)  
Allow certificates for subdomains of the domain that you specify (for example, `www.example.com` or `api.example.com`).

`Wildcards` (`ENABLED`/`DISABLED`)  
Allow [wildcard certificates](acm-concepts.md#concept-wildcard) for the domain that you specify (for example, `*.example.com`).

You can combine these settings. The following table shows example scope combinations.


**Domain validation scope combinations**  

| DomainName | ExactDomain | Subdomains | Wildcards | Certificates allowed | 
| --- | --- | --- | --- | --- | 
| example.com | ENABLED | DISABLED | DISABLED | example.com only | 
| example.com | DISABLED | ENABLED | DISABLED | sub.example.com, api.example.com, and so on | 
| example.com | DISABLED | DISABLED | ENABLED | \*.example.com only | 
| example.com | ENABLED | ENABLED | ENABLED | example.com, any subdomain, and \*.example.com | 
| internal.example.com | ENABLED | ENABLED | DISABLED | internal.example.com and its subdomains | 

## Status lifecycle
<a name="acm-acme-dv-status"></a>

After you create a domain validation, ACM attempts to verify the CNAME record for up to 72 hours. If the record is not detected within this period, the domain validation transitions to `INVALID` status. Make sure you provision the CNAME record promptly after creating the domain validation.

An ACME domain validation transitions through the following statuses:

`VALIDATING`  
The CNAME record is being verified. ACM attempts to verify the record for up to 72 hours. If the record is not confirmed within this period, the status transitions to `INVALID` with a `TIMED_OUT` failure reason.

`VALID`  
The CNAME record is confirmed. The domain validation is active and can be used for issuance.

`INVALID`  
CNAME record verification failed. See the following failure reasons.

`DELETING`  
The domain validation is being removed.

**Failure reasons**

`ACCESS_DENIED`  
Insufficient permissions to verify the DNS record.

`DOMAIN_MISMATCH`  
The CNAME record does not match expected values.

`HOSTED_ZONE_NOT_FOUND`  
The specified hosted zone could not be found.

`INTERNAL_FAILURE`  
An internal error occurred. Try creating the domain validation again.

`DOMAIN_NOT_ALLOWED`  
The domain is not permitted for issuance. The domain may be on a restricted list or may not meet issuance requirements.

`CAA_ERROR`  
A Certification Authority Authorization (CAA) DNS record prevents ACM from issuing for this domain. Ensure your CAA records allow Amazon to issue certificates.

`TIMED_OUT`  
The CNAME record was not detected within 72 hours. Verify that the record has propagated in DNS and that it matches the expected name and value exactly.

## Creating a domain validation
<a name="acm-acme-dv-create"></a>

You can create an ACME domain validation by using the ACM console or the AWS CLI.

### To create a domain validation (console)
<a name="acm-acme-dv-create-console"></a>

1. Sign in to the AWS Management Console and open the ACM console.

1. In the left navigation pane, under **ACME**, choose **Endpoints**.

1. Select the endpoint to configure.

1. Choose the **Domains** tab.

1. Choose **Add domain**.

1. For **Domain name**, enter the domain name (for example, `example.com`).

1. Configure the scope settings for exact domain, subdomains, and wildcards.

1. (Optional) For **Hosted zone ID**, enter a Route 53 hosted zone ID for automatic CNAME provisioning.

1. (Optional) Under **Tags**, add one or more tags to the domain configuration.

1. Choose **Add domain configuration**.

1. If you are not using Route 53 automatic provisioning, provision the CNAME record in your DNS. The required CNAME name and value are shown in the domain configuration details.

1. Wait for the status to change to `VALID`.

### To create a domain validation (AWS CLI)
<a name="acm-acme-dv-create-cli"></a>

Run the following command to create an ACME domain validation:

```
aws acm create-acme-domain-validation \
    --acme-endpoint-arn arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}} \
    --domain-name {{example.com}} \
    --prevalidation-options '{
        "DnsPrevalidation": {
            "DomainScope": {
                "ExactDomain": "ENABLED",
                "Subdomains": "ENABLED",
                "Wildcards": "DISABLED"
            },
            "HostedZoneId": "{{Z1234567890}}"
        }
    }'
```

To check the status and get CNAME details, run the following command:

```
aws acm describe-acme-domain-validation \
    --acme-domain-validation-arn arn:aws:acm:{{region}}:{{111122223333}}:acme-endpoint/{{00000000-0000-0000-0000-000000000000}}/acme-domain-validation/{{11111111-1111-1111-1111-111111111111}}
```

## Managing domain validations
<a name="acm-acme-dv-manage"></a>

You can perform the following management operations on ACME domain validations:

Describe  
View status and CNAME record details.

List  
View all domain validations for an endpoint.

Update  
Modify the scope configuration.

Delete  
Remove a domain validation. Certificates already issued are not affected.