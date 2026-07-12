# Troubleshoot ACME certificate automation

This section describes common issues with ACME certificate automation and how to
resolve them.

###### Topics

- [ACME failures not appearing in the console Monitoring tab](#troubleshooting-acme-monitoring "#troubleshooting-acme-monitoring")
- [Domain validation does not become valid](#troubleshooting-acme-dv "#troubleshooting-acme-dv")
- [Certificate issuance or revocation fails with access denied](#troubleshooting-acme-access-denied "#troubleshooting-acme-access-denied")
- [Certificate request is rejected](#troubleshooting-acme-rejected "#troubleshooting-acme-rejected")
- [Certificate issuance fails with a DNS CNAME error after the domain validation was previously valid](#troubleshooting-acme-cname-deleted "#troubleshooting-acme-cname-deleted")
- [Account registration fails](#troubleshooting-acme-account "#troubleshooting-acme-account")
- [ACME client times out waiting for certificate](#troubleshooting-acme-timeout "#troubleshooting-acme-timeout")

## ACME failures not appearing in the console Monitoring tab

The **Monitoring** tab on the ACME endpoint details page in
the ACM console shows events for the final step of certificate issuance—when ACM
creates the certificate (see [Monitoring ACME endpoints](acm-acme-endpoints.md#acm-acme-endpoint-monitoring "acm-acme-endpoints.md#acm-acme-endpoint-monitoring")). If your request failed before that
step, it doesn't appear there.

Some failures happen earlier in the process—for example, invalid credentials, an
unvalidated domain, or a domain that the endpoint doesn't allow. Your ACME client
receives these failures directly.

To diagnose these failures, use one of the following options:

- **Check your ACME client logs**—Your
  ACME client logs the exact error the server returns. Consult your
  client's documentation for the location of its log files.
- **Enable CloudTrail data events**—To get a
  centralized view of all ACME activity in your AWS account for debugging or
  auditing, enable CloudTrail data event logging for ACM ACME endpoints.
  For more information about these events, see [Data events](acm-supported-actions-in-cloudtrail.md#ct-data-events "acm-supported-actions-in-cloudtrail.md#ct-data-events").

## Domain validation does not become valid

An ACME endpoint can issue certificates for a domain only after the domain's
validation reaches the `VALID` status. If a domain validation stays in
`VALIDATING` or becomes `INVALID`, check the following:

- Confirm that you provisioned the CNAME record exactly as shown in the domain
  validation details, including both the record name and value. To view the required
  record, use `DescribeAcmeDomainValidation` or the ACM console.
- If you provided a Route 53 hosted zone for automatic record management, confirm that
  the hosted zone ID is correct and that ACM has access to it.

`DescribeAcmeDomainValidation` reports a failure reason that indicates the
cause:

- **`ACCESS_DENIED`:** ACM could not
  access the hosted zone to verify or create the record.
- **`DOMAIN_MISMATCH`:** The CNAME record
  does not match the expected value.
- **`HOSTED_ZONE_NOT_FOUND`:** The specified
  hosted zone could not be found.
- **`TIMED_OUT`:** The record was not
  detected within the allowed time. Verify that the record has propagated in
  DNS.
- **`INTERNAL_FAILURE`:** An internal error
  occurred. Try again, and if the problem persists, contact AWS Support.

For more information, see [ACME domain validation](acm-acme-domain-validation.md "acm-acme-domain-validation.md").

## Certificate issuance or revocation fails with access denied

ACM uses the IAM role associated with the client's external account binding (EAB)
to authorize issuance and revocation. If these operations fail with an access denied error,
check the following:

- The role's trust policy allows the ACME service principal
  (`acm-acme.amazonaws.com`) to perform `sts:AssumeRole`,
  `sts:TagSession`, and `sts:SetSourceIdentity`. If you added an
  `sts:SourceIdentity` or `sts:RoleSessionName` condition, confirm
  that it allows the values ACM uses.
- The role grants `acm:RequestCertificate` for issuance, or
  `acm:RevokeCertificate` for revocation.
- No AWS Organizations service control policy (SCP) denies the operation. SCPs are
  enforced at issuance time.

For more information, see [IAM for ACME certificate automation](security-iam-acme.md "security-iam-acme.md").

## Certificate request is rejected

If an ACME client's certificate request is rejected, check the
following:

- The requested domain is covered by a domain validation in `VALID`
  status on the endpoint, and the validation's scope (exact domain, subdomains, or
  wildcards) permits the requested name. For more information, see [Domain validation scope](acm-acme-domain-validation.md#acm-acme-dv-scope "acm-acme-domain-validation.md#acm-acme-dv-scope").
- The certificate's key algorithm is one of the endpoint's allowed key algorithms.
  For more information, see [Endpoint configuration](acm-acme-endpoints.md#acm-acme-endpoint-configuration "acm-acme-endpoints.md#acm-acme-endpoint-configuration").

## Certificate issuance fails with a DNS CNAME error after the domain validation was previously valid

An ACME domain validation requires that its CNAME record remain in DNS for as
long as the validation is in use. If the CNAME is removed after the domain validation
reaches `VALID` status, certificate orders for that domain can fail at issuance
time, even though the domain validation resource itself was previously confirmed.

When this happens, the ACME client sees the order transition to
`invalid` status and the order's `error` field carries a
`type` of `urn:ietf:params:acme:error:dns` with a
`detail` that names the CNAME records that could not be resolved. For
example:

```
{
    "status": "invalid",
    "error": {
        "type": "urn:ietf:params:acme:error:dns",
        "detail": "DNS CNAME records not found: [`_a1b2c3d4e5f67890abcdef1234567890.example.com.`]"
    },
    "identifiers": [{ "type": "dns", "value": "`example.com`" }],
    "authorizations": ["https://acm-acme-enroll.`region`.api.aws/`00000000-0000-0000-0000-000000000000`/authz/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"],
    "finalize": "https://acm-acme-enroll.`region`.api.aws/`00000000-0000-0000-0000-000000000000`/order/`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`/finalize",
    "expires": "2026-06-18T13:49:02Z"
}
```

ACME clients surface the order's error in their own output. For example,
Certbot exits with the following error:

```
An unexpected error occurred:
DNS CNAME records not found: [`_a1b2c3d4e5f67890abcdef1234567890.example.com.`]
```

If you have configured an CloudTrail trail or event data store to record ACM data events,
the failure also appears on the `IssueCertificate` CloudTrail event under
`serviceEventDetails`, with the same `errorType` and
`errorMessage`. For more information, see [ACM API actions supported in CloudTrail logging](acm-supported-actions-in-cloudtrail.md "acm-supported-actions-in-cloudtrail.md").

To resolve the issue, restore the CNAME record listed in the error. To find the
expected CNAME for a domain validation, use `DescribeAcmeDomainValidation` or
view the domain validation in the ACM console.

## Account registration fails

When an ACME client registers an account with an endpoint, check the
following:

- The client provides external account binding (EAB) credentials (the key
  identifier and HMAC key) during registration. The endpoint requires these
  credentials.
- If the endpoint requires contact information, the client provides a contact email
  address during registration. For more information, see [External account bindings](acm-acme-eab.md "acm-acme-eab.md").

## ACME client times out waiting for certificate

Certificate issuance through the ACM ACME endpoint can take up to two minutes.
If your ACME client times out before receiving the certificate, increase the
client's issuance timeout to at least 120 seconds (2 minutes).

For Certbot, use the `--issuance-timeout` flag:

```
certbot certonly --issuance-timeout 120 ...
```

For other ACME clients, consult your client's documentation for the equivalent
timeout configuration.
