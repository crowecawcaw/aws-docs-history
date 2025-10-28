# Troubleshoot AS2 issues

This section describes possible solutions for issues with AS2 transfers.

###### Topics

- [Troubleshoot AS2 issues](#as2-troubleshooting-issues "#as2-troubleshooting-issues")
- [AS2 certificate issues](#as2-certificate-issues "#as2-certificate-issues")
- [AS2 MDN receipt issues](#as2-mdn-issues "#as2-mdn-issues")
- [Certificate expiration
  monitoring issues](#certificate-expiration-troubleshooting "#certificate-expiration-troubleshooting")

## Troubleshoot AS2 issues

[AS2 error codes](as2-monitoring.md#as2-error-codes "as2-monitoring.md#as2-error-codes"), messages and
troubleshooting tips for Applicability Statement 2 (AS2)-enabled servers are described
in the AS2 failure codes section in this guide.

## AS2 certificate issues

Description

You're experiencing certificate-related errors with AS2 transfers.

Cause

Common causes include expired certificates, incorrect certificate formats, or
mismatched certificate chains.

Solution

Try the following solutions:

- Verify that your certificates are not expired
- Ensure certificates are in the correct format (PEM for AWS Transfer Family)
- Check that the certificate chain is complete and valid
- Confirm that the signing and encryption certificates match between trading
  partners
- Rotate certificates well before expiration to avoid interruptions

## AS2 MDN receipt issues

Description

You're not receiving expected Message Disposition Notifications (MDNs) for AS2
transfers.

Cause

MDN issues can occur due to network connectivity problems, incorrect endpoint
configurations, or MDN format mismatches.

Solution

Consider these solutions:

- Verify that the MDN URL is correctly configured and accessible
- Check network connectivity between the AS2 server and the MDN endpoint
- Ensure that both trading partners are configured for the same MDN type
  (synchronous or asynchronous)
- Review AS2 logs for any errors related to MDN processing
- If using synchronous MDNs, verify that timeouts are set appropriately

## Certificate expiration

monitoring issues

This section provides solutions for common issues related to certificate expiration
monitoring and the DaysUntilExpiry metric.

### DaysUntilExpiry metric not

appearing

**Problem:** The DaysUntilExpiry metric is not
visible in Amazon CloudWatch after importing a certificate.

**Solution:**

- Wait up to 24 hours after importing the certificate. It can take up to a
  full day for Transfer Family to emit the metric to your account.
- Ensure you're looking in the correct AWS region and under the
  `AWS/Transfer` namespace in CloudWatch.

### Certificate

expiration alarms not triggering

**Problem:** CloudWatch alarms for certificate expiration
are not triggering when expected.

**Solution:**

- Verify that the alarm is configured with the `Maximum`
  statistic and a period of 1 day.
- Check that the threshold comparison is set to `Less than or equal
to` the desired number of days.
- Ensure that `Treat missing data as good (not breaching)` is
  selected in the alarm configuration.
- Verify that the alarm dimensions match your certificate's CertificateId
  and Description (if provided).
- Check that the alarm actions (SNS topics, email notifications) are
  properly configured and active.
