

# Intermediate CA revoked for active device certificates check
<a name="audit-chk-active-intermediary-device-revoked-CA"></a>

Use this check to identify all related device certificates that are still active despite revoking an intermediate CA.

This check appears as `INTERMEDIATE_CA_REVOKED_FOR_ACTIVE_DEVICE_CERTIFICATES_CHECK` in the CLI and API.

Severity: **Critical**

## Details
<a name="audit-chk-active-device-intermediary-revoked-CA-details"></a>

The following reason codes are returned when this check finds noncompliance:
+ INTERMEDIATE\_CA\_REVOKED\_BY\_ISSUER

## Why it matters
<a name="audit-chk-active-device-intermediary-revoked-CA-why-it-matters"></a>

The intermediate CA revoked for active device certificates check assess device identity and trust, by determining if there are active device certificates in AWS IoT Core where the intermediate issuing CAs have been revoked in the CA chain.

A revoked intermediate CA should no longer be used to sign any other CA or device certificates in CA chain. Newly added devices with certificates signed using this CA certificate after the intermediate CA is revoked will pose a security threat.

## How to fix it
<a name="audit-chk-active-device-intermediary-revoked-CA-how-to-fix"></a>

Review the device certificate registration activity for the time after the CA certificate was revoked. Follow your security best practices to mitigate the situation. You might want to:

1. Provision new certificates, that are signed by a different CA, for the affected devices.

1. Verify that the new certificates are valid, and that the devices can use them to connect.

1. Use [UpdateCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html) to mark the old certificate as REVOKED in AWS IoT. You can also use mitigation actions to:
   + Apply the `UPDATE_DEVICE_CERTIFICATE` mitigation action on your audit findings to make this change. 
   + Apply the `ADD_THINGS_TO_THING_GROUP` mitigation action to add the device to a group where you can take action on it.
   + Apply the `PUBLISH_FINDINGS_TO_SNS` mitigation action if you want to implement a custom response in response to the Amazon SNS message. 
   + Review the device certificate registration activity for the time after the intermediate CA certificate was revoked and consider revoking any device certificates that might have been issued with it during this time. You can use [ListRelatedResourcesForAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRelatedResourcesForAuditFinding.html) to list the device certificates signed by the CA certificate and [UpdateCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html) to revoke a device certificate.
   + Detach the old certificate from the device. (See [DetachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_DetachThingPrincipal.html).)

   For more information, see [Mitigation actions](dd-mitigation-actions.md).