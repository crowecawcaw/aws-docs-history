

# Troubleshooting inbound external links with custom domains
<a name="troubleshooting-custom-domain-ingress"></a>

Use this section to diagnose common issues with inbound external links with custom domains. Each entry describes the observed symptom, its likely cause, and the recommended resolution.

## TLS handshake fails with certificate error
<a name="tls-handshake-certificate-error-1"></a>

**Symptom:** The client receives an unknown or default certificate instead of the expected custom domain certificate.

**Cause:** The SNI hostname sent by the client does not match the CN or any SAN on your ACM certificate. The certificate resolver performs case-sensitive exact hostname matching.

**Resolution:** Verify that the hostname in the client's SNI extension exactly matches (including case) the CN or a SAN on your ACM certificate. Ensure the CN and SANs use lowercase characters. Use `openssl s_client -servername <hostname>` to test SNI resolution against the gateway.

## TLS handshake fails with certificate error
<a name="tls-handshake-certificate-error-2"></a>

**Symptom:** The TLS handshake fails and the client receives a certificate error.

**Cause:** The certificate association between your ACM certificate and RTB Fabric could not be established, or the certificate is not in a valid state.

**Resolution:** Confirm that the ACM certificate ARN is correct and the certificate is in ISSUED status. Disassociate and re-associate the certificate using the AssociateCertificate API. If the issue persists, contact your account team.

## All requests return 404 Not Found
<a name="all-requests-404"></a>

**Symptom:** Every request to the custom domain returns a 404 response.

**Cause:** No routing rules are configured on any link on the gateway. The gateway cannot resolve a link ID from the incoming request. The 404 response body contains "Link ID not specified in request".

**Resolution:** Verify that at least one routing rule has been created on a link using the CreateLinkRoutingRule API, and that the rule is in ACTIVE status. Confirm that the rule conditions match the request's host, path, or query parameters. See Configuring routing rules for configuration details.

## Requests are routed to the wrong link ID
<a name="wrong-link-routing"></a>

**Symptom:** Requests arrive at an unexpected link instead of the intended target.

**Cause:** Rule priority misconfiguration. A less-specific rule has a lower priority number (higher precedence) than a more-specific rule, causing the less-specific rule to match first.

**Resolution:** Review the priority values assigned to all routing rules across your links. Ensure that more-specific rules (exact host, exact path) have lower priority numbers than less-specific rules (wildcard host, prefix path). The data plane evaluates rules strictly by ascending priority — it does not infer specificity.

## Certificate not found for a configured hostname
<a name="certificate-not-found"></a>

**Symptom:** The certificate resolver does not serve the expected certificate, even though the ACM certificate appears to cover the correct hostnames.

**Cause:** Case mismatch between the certificate's CN/SANs and the SNI hostname. The certificate resolver's exact hostname lookup is case-sensitive. Alternatively, the certificate may not be associated with the gateway.

**Resolution:** Ensure the CN and SANs on your ACM certificate use lowercase characters. Verify the certificate is associated with the gateway using the GetCertificateAssociation API.

## DNS queries do not resolve to the RTB Fabric gateway
<a name="dns-not-resolving"></a>

**Symptom:** `dig` queries for the bid endpoint return the old origin instead of the RTB Fabric gateway endpoint.

**Cause:** The CNAME record update has not propagated, or the previous record's TTL has not expired in downstream DNS caches.

**Resolution:** Verify the CNAME record is correctly configured using `dig east-bid.example.com CNAME`. Wait for the previous TTL to expire. If you did not lower the TTL before migration, propagation may take up to the original TTL duration (commonly 300-3600 seconds).

## Partial traffic loss during migration
<a name="partial-traffic-loss"></a>

**Symptom:** Elevated error rates or traffic loss affecting only a fraction of requests during weighted routing migration.

**Cause:** Weighted routing records are misconfigured, or DNS caches are returning stale records. Some resolvers may cache the legacy record while others have the new record, creating an inconsistent traffic split.

**Resolution:** Verify both weighted records exist and have the intended weights using `aws route53 list-resource-record-sets`. Confirm that both the legacy and RTB Fabric endpoints are healthy. Allow additional time for DNS cache convergence (at minimum, one full TTL cycle).

## Wildcard certificate does not match a multi-level subdomain
<a name="wildcard-multi-level"></a>

**Symptom:** A certificate configured with `*.example.com` does not match `a.b.example.com` in routing, but may match in certificate resolution.

**Cause:** Routing rule wildcard matching correctly implements RFC 6125 single-label subdomain matching. `*.example.com` matches `bid.example.com` but not `a.b.example.com`. However, certificate resolution uses suffix-based wildcard matching, which can match multi-level subdomains. This behavioral difference is a known limitation.

**Resolution:** For routing, use an exact host match rule for multi-level subdomains, or restructure your domain hierarchy. For certificate resolution, be aware that a wildcard certificate may be served for multi-level subdomains. Do not rely on this behavior.

## Query parameter routing rule does not match
<a name="query-parameter-no-match"></a>

**Symptom:** A `queryStringEquals` rule does not match requests that appear to have the correct query string.

**Cause:** URL encoding differences between the rule configuration and the actual request. The rule matcher URL-decodes both the configured value and the request query string before comparison. If the configured value contains percent-encoded characters that differ from the decoded form in the request (or vice versa), the match fails. Query parameter matching is also case-sensitive for both keys and values.

**Resolution:** Verify that the `queryStringEquals` key and value in the rule configuration match the decoded form of the query parameter as it appears in the request. For example, if the request contains `supplier%5Fid=7`, configure the rule with key `supplier_id` and value `7` (decoded form).

## Customer certificate served as fallback for non-custom-domain traffic
<a name="customer-cert-fallback"></a>

**Symptom:** Your custom domain certificate is presented to clients connecting via hostnames not associated with your custom domain.

**Cause:** The certificate was not associated with the gateway through the AssociateCertificate API. Without proper association, the certificate resolver may treat it as a service certificate and serve it as a general fallback for any request, regardless of hostname.

**Resolution:** Associate the certificate with the gateway using the AssociateCertificate API. This ensures the certificate is treated as a customer certificate and served only when the client's SNI hostname matches the certificate's CN or SANs.

## Path prefix rule matches unexpected paths
<a name="path-prefix-unexpected"></a>

**Symptom:** A rule with path prefix `/api` appears to match `/api2/endpoint`.

**Cause:** The path prefix matcher is segment-boundary aware: `/api` matches `/api`, `/api/`, and `/api/v1`, but does not match `/api2`. If `/api2` appears to match, the issue is likely a different rule with a lower priority number that also matches the request.

**Resolution:** Inspect all routing rules and their priorities. Use the request's full host, path, and query string to determine which rule is actually matching. A rule with a broader condition (for example, a host-only rule with no path condition) and a lower priority number would match before the path-specific rule is evaluated.

## Routing rules are not evaluated
<a name="routing-rules-not-evaluated"></a>

**Symptom:** Requests fall through to legacy link ID extraction even though routing rules have been created.

**Cause:** The routing rules may not have reached ACTIVE status, or the rules are on a different link than expected.

**Resolution:** Use the ListLinkRoutingRules API to verify that rules exist on the intended link and are in ACTIVE status. If a rule is in PENDING\_CREATION or FAILED status, wait for provisioning or investigate the failure. See Step 5: Configure routing rules for the correct setup.

## Multiple certificates for the same hostname
<a name="multiple-certificates-same-hostname"></a>

**Symptom:** Multiple certificates are configured for the same hostname, but only one is served.

**Cause:** The certificate resolver stores certificates in a list per hostname but only uses the first entry. If multiple certificates covering the same hostname are associated with the gateway, all certificates after the first are silently ignored.

**Resolution:** Ensure only one certificate covers each hostname. If you need to rotate certificates, disassociate the old certificate before associating the new one, or use ACM in-place renewal.

**Note**  
Rotation of ACM-managed certificates will be handled automatically by RTB Fabric with no action required from you.