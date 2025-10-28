# Revoked device certificate still

active

A revoked device certificate is still active.

This check appears as `REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK` in
the CLI and API.

Severity: **Medium**

## Details

A device certificate is in its CA's [certificate
revocation list](https://en.wikipedia.org/wiki/Certificate_revocation_list "https://en.wikipedia.org/wiki/Certificate_revocation_list"), but it is still active in AWS IoT.

This check applies to device certificates that are ACTIVE or
PENDING_TRANSFER.

The following reason codes are returned when this check finds
noncompliance:

- CERTIFICATE_REVOKED_BY_ISSUER

## Why it

matters

A device certificate is usually revoked because it has been compromised. It is
possible that it has not yet been revoked in AWS IoT due to an error or
oversight.

## How to fix it

Verify that the device certificate has not been compromised. If it has, follow
your security best practices to mitigate the situation. You might want to:

1.  Provision a new certificate for the device.
2.  Verify that the new certificate is valid and the device is able to use it
    to connect.
3.  Use [UpdateCertificate](../../../iot/latest/apireference/API_UpdateCertificate.md "../../../iot/latest/apireference/API_UpdateCertificate.md") to mark the old certificate as REVOKED in
    AWS IoT. You can also use mitigation actions to:

        * Apply the `UPDATE_DEVICE_CERTIFICATE` mitigation action
         on your audit findings to make this change.
        * Apply the `ADD_THINGS_TO_THING_GROUP` mitigation action
         to add the device to a group where you can take action on it.
        * Apply the `PUBLISH_FINDINGS_TO_SNS` mitigation action
         if you want to implement a custom response in response to the Amazon SNS
         message.

    For more information, see [Mitigation actions](dd-mitigation-actions.md "dd-mitigation-actions.md").

4.  Detach the old certificate from the device. (See [DetachThingPrincipal](../../../iot/latest/apireference/API_DetachThingPrincipal.md "../../../iot/latest/apireference/API_DetachThingPrincipal.md").)
