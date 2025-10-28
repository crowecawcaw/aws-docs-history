# Automate export of a renewed certificate

When you use AWS Private CA to create a CA, you can import that CA into AWS Certificate Manager and let
ACM manage certificate issuance and renewal. If a certificate being renewed is associated
with an [integrated service](../../../acm/latest/userguide/acm-services.md "../../../acm/latest/userguide/acm-services.md"), the service
seamlessly applies the new certificate. However, if the certificate was originally [exported](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md") for use elsewhere in your PKI
environment (for example, in an on-premises server or appliance), you need to export it
again after renewal.

For a sample solution that automates the ACM export process using Amazon EventBridge and AWS
Lambda, see [Automating
export of renewed certificates](../../../acm/latest/userguide/renew-private-cert.md#automating-export "../../../acm/latest/userguide/renew-private-cert.md#automating-export").
