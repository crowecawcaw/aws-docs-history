# Rotate SSL/TLS certificates

When your SSL/TLS certificates are near expiration, you need to rotate them to ensure the
security for your distribution and avoid service disruption for your viewers. You
can rotate them in the following ways:

- For SSL/TLS certificates provided by AWS Certificate Manager (ACM), you don't need to rotate them.
  ACM _automatically_ manages certificate renewals for
  you. For more information, see [Managed certificate renewal](../../../acm/latest/userguide/acm-renewal.md "../../../acm/latest/userguide/acm-renewal.md") in the
  _AWS Certificate Manager User Guide_.
- If you're using a third-party certificate authority and you imported the
  certificates into ACM (recommended) or uploaded them to the IAM
  certificate store, you must occasionally replace one certificate with
  another.

###### Important

- ACM doesn't manage certificate renewals for certificates that you
  acquire from third-party certificate authorities and import into
  ACM.
- If you configured CloudFront to serve HTTPS requests by using dedicated IP
  addresses, you might incur an additional, pro-rated charge for using one
  or more additional certificates while you're rotating certificates. We
  recommend that you update your distributions to minimize the additional
  charge.

## Rotate SSL/TLS certificates

To rotate your certificates, perform the following procedure. Viewers can
continue to access your content while you rotate certificates as well as after
the process is complete.

###### To rotate SSL/TLS certificates

1. [Increase the quotas for SSL/TLS certificates](increasing-the-limit-for-ssl-tls-certificates.md "increasing-the-limit-for-ssl-tls-certificates.md") to
   determine whether you need permission to use more SSL certificates. If
   so, request permission and wait until permission is granted before you
   continue with step 2.
2. Import the new certificate into ACM or upload it to IAM. For more
   information, see [Importing an SSL/TLS Certificate](cnames-and-https-procedures.md#cnames-and-https-uploading-certificates "cnames-and-https-procedures.md#cnames-and-https-uploading-certificates") in the
   _Amazon CloudFront Developer Guide_.
3. (For IAM certificates only) Update your distributions one at a time
   to use the new certificate. For more information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
4. (Optional) Delete the previous certificate from ACM or IAM.

###### Important

Don't delete an SSL/TLS certificate until you remove it from all
distributions and until the status of the distributions that you
have updated has changed to `Deployed`.
