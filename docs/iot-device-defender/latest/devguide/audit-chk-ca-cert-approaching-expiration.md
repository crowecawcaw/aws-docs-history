# CA certificate

expiring

A CA certificate is expiring within 30 days or has expired.

This check appears as `CA_CERTIFICATE_EXPIRING_CHECK` in the CLI and
API.

Severity: **Medium**

## Details

This check applies to CA certificates that are ACTIVE or PENDING_TRANSFER.

The following reason codes are returned when this check finds a noncompliant CA
certificate:

- CERTIFICATE_APPROACHING_EXPIRATION
- CERTIFICATE_PAST_EXPIRATION

## Why it

matters

An expired CA certificate should not be used to sign new device
certificates.

## How to fix

it

Consult your security best practices for how to proceed. You might want to:

1.  Register a new CA certificate with AWS IoT.
2.  Verify that you are able to sign device certificates using the new CA
    certificate.
3.  Use [UpdateCACertificate](../../../iot/latest/apireference/API_UpdateCACertificate.md "../../../iot/latest/apireference/API_UpdateCACertificate.md") to mark the old CA certificate as INACTIVE
    in AWS IoT. You can also use mitigation actions to do the following:

        * Apply the `UPDATE_CA_CERTIFICATE` mitigation action on
         your audit findings to make this change.
        * Apply the `PUBLISH_FINDINGS_TO_SNS` mitigation action
         if you want to implement a custom response in response to the Amazon SNS
         message.

    For more information, see [Mitigation actions](dd-mitigation-actions.md "dd-mitigation-actions.md").
