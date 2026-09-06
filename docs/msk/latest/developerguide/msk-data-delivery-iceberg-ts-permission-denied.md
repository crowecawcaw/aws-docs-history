

# Permission denied errors in Amazon CloudWatch Logs
<a name="msk-data-delivery-iceberg-ts-permission-denied"></a>
+ **Symptom:** Logs show `AccessDenied` or 403 errors.
+ **Causes:** Service-role IAM policy modified; destination bucket policy or KMS key policy denying access; trust policy no longer allows the Kafka service to assume the role.
+ **Resolution:** Compare the current policy against the required policy; check recent bucket-policy changes via CloudTrail; verify the trust policy still includes `kafka.amazonaws.com`; if using KMS, verify the key policy grants the role access.