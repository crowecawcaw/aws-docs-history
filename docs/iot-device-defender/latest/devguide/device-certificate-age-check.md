# Device certificate age check

This audit check alerts you when a device certificate has been active for a number of
days greater than or equal to the number you specify. This check helps you stay informed
about your certificates’ status, enabling timely action on a periodic basis, regardless
of when the certificate reaches the end of its lifespan, improving security by reducing
the risk of certificate compromise.

The certificate age check threshold can be configured between 30 days (minimum) and 3652 days (10 years, maximum), with a default value of 365 days.

This check appears as `DEVICE_CERTIFICATE_AGE_CHECK` in the CLI and API.
This check is disabled by default Severity: **Low**

## Details

This check applies to device certificates that are ACTIVE or PENDING_TRANSFER. The
following reason codes are returned when this check finds a noncompliant device
certificate:

- CERTIFICATE_PAST_AGE_THRESHOLD

## Configuring the device certificate age check

This configuration allows you to tailor certificate rotation alerts to the
specific needs of your fleet, helping you maintain a strong security posture across
all devices. You can configure this check using the
`UpdateAccountAuditConfiguration` API. For example, if you want to be
alerted when certificates have been active for more than 365 days, you can configure
the check as follows:

```

{
    "roleArn": "your-audit-role-arn",
    "auditCheckConfigurations": {
        "DEVICE_CERTIFICATE_AGE_CHECK": {
            "enabled": true,
            "configuration": {
                "CERT_AGE_THRESHOLD_IN_DAYS": "365"
            }
        }
    }
}

```
