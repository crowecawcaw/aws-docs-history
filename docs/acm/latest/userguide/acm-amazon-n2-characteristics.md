

# Amazon N2 certificate characteristics

The following characteristics apply to Amazon N2 certificates. Where a characteristic differs from an ACM public certificate, this page describes the difference.

**Validity period**  <a name="amazon-n2-validity-term"></a>
The maximum validity of an Amazon N2 certificate depends on its root hierarchy.    
`N2_AMAZON_MANAGED`  
395 days  
`N2_SFG2_AMAZON_MANAGED`  
98 days. This hierarchy follows CA/Browser Forum validity requirements, so its maximum decreases as those requirements change.

**Certificate usage**  <a name="amazon-n2-usage-term"></a>
Every Amazon N2 certificate can authenticate a client. With `CLIENT_AND_SERVER_AUTH` (the default), the certificate can also authenticate a server. With `CLIENT_AUTH_ONLY`, available only with `N2_AMAZON_MANAGED`, it authenticates only a client. For the supported combinations, see [How Amazon N2 certificates work in ACM](acm-amazon-n2-certificates.md#acm-amazon-n2-how-it-works).

**Key algorithms**  <a name="amazon-n2-algorithms-term"></a>
ACM issues Amazon N2 certificates with the following key algorithms.  
+ RSA 2048 bit (`RSA_2048`)
+ ECDSA 256 bit (`EC_prime256v1`)
+ ECDSA 384 bit (`EC_secp384r1`)
[Imported certificates](import-certificate.md) also support RSA 3072 bit, RSA 4096 bit, and ECDSA 521 bit keys. For a comparison of RSA and ECDSA key sizes at equivalent security strengths, see [Key algorithms](acm-certificate-characteristics.md#algorithms).

**Domain validation**  <a name="amazon-n2-validation-term"></a>
Amazon N2 certificates support DNS validation only. Set `ValidationMethod` to `DNS` and create the CNAME record that ACM provides. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md).  
HTTP validation and email validation are not available for Amazon N2 certificates. The domain names in an Amazon N2 certificate must be public DNS names that ACM can resolve.  
The validation CNAME record for an Amazon N2 certificate is specific to the AWS Region and account, and it differs from the record for an ACM public certificate for the same domain. Create the record that ACM provides for your Amazon N2 certificate request, even if you already validated the domain for a public certificate.

**Certificate transparency logging**  <a name="amazon-n2-transparency-term"></a>
ACM does not record Amazon N2 certificates in certificate transparency (CT) logs, because they are not intended for browser clients. If your request includes a CT logging preference, ACM accepts the request and ignores the preference.

**Listing and finding**  <a name="amazon-n2-listing-term"></a>
By default, `ListCertificates` does not return Amazon N2 certificates. As a result, the certificate pickers in integrated service consoles might not show Amazon N2 certificates. To list Amazon N2 certificates, specify `N2_AMAZON_MANAGED`, `N2_SFG2_AMAZON_MANAGED`, or both in the `RootHierarchyTypes` filter. With the filter, `ListCertificates` returns only certificates from the hierarchies that you specify. To list all of your certificates, call it once without the filter and once with it. The following AWS CLI command lists Amazon N2 certificates from both hierarchies.  

```bash
aws acm list-certificates \
    --root-hierarchy-types N2_AMAZON_MANAGED N2_SFG2_AMAZON_MANAGED
```
`SearchCertificates` and `DescribeCertificate` return Amazon N2 certificates without a filter. To search for Amazon N2 certificates from one hierarchy, filter on `RootHierarchyType`:  

```bash
aws acm search-certificates \
    --filter-statement '{"Filter": {"AcmCertificateMetadataFilter": {"RootHierarchyType": "N2_AMAZON_MANAGED"}}}'
```

**AWS integrated services**  <a name="amazon-n2-integrated-term"></a>
You can associate an Amazon N2 certificate with the resource of an integrated service by specifying the certificate ARN. You do not need to export the certificate. For the list of integrated services, see [Managed automation with integrated services](acm-services.md).  
Associate an Amazon N2 certificate only with a resource whose clients include the root in their trust store. If you associate an Amazon N2 certificate with a resource that serves browser clients, such as a public CloudFront distribution or an internet-facing Elastic Load Balancing listener, browsers reject the connection.

**Quotas**  <a name="amazon-n2-quota-term"></a>
Amazon N2 certificates count toward the **Number of ACM certificates** quota, the same as other ACM-issued certificates. For more information, see [Quotas](acm-limits.md).

**Export and revocation**  <a name="amazon-n2-export-term"></a>
Amazon N2 certificates are exportable by default. If you omit the `Export` option from the request, ACM stores the export preference as `ENABLED`. To issue an Amazon N2 certificate that cannot be exported, set `Export` to `DISABLED` in the request. You cannot change the export setting after the certificate is issued. ACM public certificates, by contrast, are not exportable unless you request them with `Export` set to `ENABLED`. For more information, see [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md).  
You can revoke an exported Amazon N2 certificate with the console, the AWS CLI, or the `RevokeCertificate` API action. For more information, see [Revoke an AWS Certificate Manager public certificate](revoke-certificate.md).  
Amazon N2 certificates include certificate revocation list (CRL) and Online Certificate Status Protocol (OCSP) locations, so verifying peers that check revocation status detect a revoked certificate. For the certificate chain that ACM returns, see [Amazon N2 roots and trust](acm-amazon-n2-certificates.md#acm-amazon-n2-trust).

**Renewal**  <a name="amazon-n2-renewal-term"></a>
ACM renews Amazon N2 certificates automatically while the DNS validation records stay in place. Renewal starts 60 days before expiration for `N2_AMAZON_MANAGED` and 30 days before expiration for `N2_SFG2_AMAZON_MANAGED`. Integrated services that use the certificate use the renewed certificate. ACM does not update copies that you exported, so export the certificate and install it again after each renewal. For more information, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md).