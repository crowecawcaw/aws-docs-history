# Troubleshoot MediaPackage CDN authorization

errors

When AWS Elemental MediaPackage CDN authorization fails, you may encounter various error codes and
authorization issues. This section helps you identify and resolve common problems with
CDN authorization configuration, secret management, and IAM permissions.

| Common Error Scenarios and Resolutions | Scenario         | Error Type                                                                                                                                                                          | Resolution |
| -------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Secret validation failure              | 4XX error        | Verify that your secret is stored with the correct key name `MediaPackageV2CDNIdentifier` and the value is between 8-256 characters.                                                |
| IAM role access denied                 | 4XX error        | Check that the IAM role has the correct permissions and trust relationship as described in [Configure MediaPackage CDN authorization setup](cdn-auth-setup.md "cdn-auth-setup.md"). |
| Secret not found                       | 4XX error        | Verify that the secret ARN is correct and the secret exists in the same Region as your MediaPackage endpoint.                                                                       |
| Header value mismatch                  | 403 Unauthorized | Ensure that the value in the `X-MediaPackageV2-CDNIdentifier` header matches the value stored in Secrets Manager.                                                                   |
