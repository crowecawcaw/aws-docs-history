# Monitoring IAM Roles Anywhere notifications with

AWS Health

You can monitor IAM Roles Anywhere health notifications in [AWS Health](../../../health/latest/ug.md "../../../health/latest/ug.md").
Notifications from IAM Roles Anywhere are delivered to AWS Health when certificates (both CA certificates in trust anchors and end-entity certificates) that are configured with IAM Roles Anywhere are nearing expiry. You can use these AWS Health notifications to take renewal actions on your certificates. For more information see [Monitoring AWS Health events with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md")

## Affected resources for trust anchor expiry notifications

IAM Roles Anywhere sends daily expiry notifications for each trust anchor that satisfies the [notification evaluation criteria](customize-notification-settings.md#notification-evaluation "customize-notification-settings.md#notification-evaluation"). For these notifications, the "Affected Resources" will each be trust anchors. If you have multiple certificates within a single trust anchor, it's possible that multiple are nearing expiry. IAM Roles Anywhere will determine whether a notification should be sent for a given trust anchor based on the certificate in the trust anchor that is expiring the soonest. Thus, you'll have to check each certificate in the trust anchor and take the necessary actions so as to not cause impact to your workloads that rely on IAM Roles Anywhere for temporary security credentials.

## Affected resources for end-entity certificate expiry notifications

IAM Roles Anywhere also sends daily expiry notifications for each end-entity certificate that was used to authenticate over the last day and satisfies the [notification evaluation criteria](customize-notification-settings.md#notification-evaluation "customize-notification-settings.md#notification-evaluation"). For these notifications, the "Affected Resources" will each be end-entity certificates. Each of these end-entity certificates will have a composite "Resource ID/ARN", of the form given below.

```
serialNumber=`SerialNumber`;certificateId=`CertificateId`
```

The `serialNumber` in the above resource identifier will contain the value of the serial number of the end-entity certificate that was used for authentication and will be expiring soon. And the `certificateId` in the above resource identifier will contain the value of the certificate ID for that certificate. The certificate ID is defined as `Hex(SHA256(`ASN.1 DER Certificate Bytes`))`, where the result is a lowercase hex-encoded string. If you have a PEM file that contains your certificate data, you can use OpenSSL to convert your certificate into its DER representation and then take the SHA256 hash of the resulting value.

```
openssl x509 -in `end-entity-certificate.pem` -inform PEM -outform DER | sha256sum
```
