# Device certificate

expiring

A device certificate is expiring within the configured threshold period or has expired. The certificate expiration check threshold can be configured between 30 days (minimum) and 3652 days (10 years, maximum) with a default value of 30 days.

This check appears as `DEVICE_CERTIFICATE_EXPIRING_CHECK` in the CLI and
API.

Severity: **Medium**

## Details

This check applies to device certificates that are ACTIVE or
PENDING_TRANSFER.

The following reason codes are returned when this check finds a noncompliant
device certificate:

- CERTIFICATE_APPROACHING_EXPIRATION
- CERTIFICATE_PAST_EXPIRATION

## Why it

matters

A device certificate should not be used after it expires.

## Configuring the Device certificate

expiring check

This configuration enables you to monitor and receive alerts for certificates that are
approaching their expiration date across your device fleet. For example, if you want to be
notified when certificates are within 30 days of expiration, you can configure
the check as follows:

```

{
    "roleArn": "your-audit-role-arn",
    "auditCheckConfigurations": {
        "DEVICE_CERTIFICATE_EXPIRING_CHECK": {
            "enabled": true,
            "configuration": {
                "CERT_EXPIRATION_THRESHOLD_IN_DAYS": "30"
            }
        }
    }
}

```

## How to fix

it

Consult your security best practices for how to proceed. You might want to:

1.  Provision a new certificate and attach it to the device.
2.  Verify that the new certificate is valid and the device is able to use it
    to connect.
3.  Use [UpdateCertificate](../../../iot/latest/apireference/API_UpdateCertificate.md "../../../iot/latest/apireference/API_UpdateCertificate.md") to mark the old certificate as INACTIVE in
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
