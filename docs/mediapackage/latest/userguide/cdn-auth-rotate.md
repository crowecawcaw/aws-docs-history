

# Rotate MediaPackage CDN authorization secrets

When you need to update your AWS Elemental MediaPackage CDN authorization credentials, you must rotate the stored secret value in AWS Secrets Manager to maintain synchronization with your CDN's custom HTTP header. This process ensures continuous content delivery while updating security credentials.

**To rotate the value**

1. Update the stored secret value in Secrets Manager as described in [Modifying a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html) in the *AWS Secrets Manager User Guide*.

   To ensure continued playback for active streams, MediaPackage authorizes requests that use either the current value in Secrets Manager or one version back.

1. Wait 5 minutes for MediaPackage to recognize that the value has changed in Secrets Manager.

1. In your CDN, update the value in `X-MediaPackageV2-CDNIdentifier` to the new secret value.

1. Wait for your CDN to update fully with the new value before you send any requests through it to MediaPackage.

**Emergency rotation details**  
In emergency situations where you need to immediately invalidate a secret, do one of the following:
+ Update the endpoint configuration to remove the compromised secret ARN and replace it with a new secret ARN. After 5 minutes, MediaPackage will no longer accept the compromised secret value.
+ Alternatively, rotate the secret twice in quick succession. After 5 minutes, MediaPackage will no longer accept the old secret values since the incoming header value would not match either the current or previous secret.

**Note**  
MediaPackage caches CDN authorization settings, including secret values and the secret ARNs configured on the endpoint, for up to 5 minutes. After you rotate a secret value, replace a secret ARN, or remove CDN authorization from an endpoint, it can take up to 5 minutes for the change to take effect. During this period, MediaPackage might still accept the previous secret value.