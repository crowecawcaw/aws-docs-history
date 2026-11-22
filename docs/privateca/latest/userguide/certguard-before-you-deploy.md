

# Before you deploy a policy

A `Deny` statement applies to every request that it matches, including requests that you don't make directly. Before you add X.509 certificate condition keys to an SCP, RCP, or widely used identity-based policy, check the following:
+ **Services and connectors that issue certificates for you.** AWS Certificate Manager (ACM), AWS Private CA Connector for Active Directory, Connector for SCEP, AWS Private CA Connector for Kubernetes, and your own automation call `IssueCertificate` with certificate contents that they choose. Some of them also send test requests to check that they have permission to use a CA. A policy that denies those requests can stop certificate issuance or renewal, or cause setup to fail. Scope your statements with conditions such as `aws:PrincipalArn`, `aws:PrincipalTag`, or `aws:ViaAWSService` so that they apply only to the requests you intend. For the values in the test requests that Connector for AD and Connector for SCEP send, see [Allow connector creation when you use X.509 certificate condition keys](pca-rbp.md#connector-permission-check-condition-keys).
+ **Certificate templates.** Your conditions must allow the extensions that the template adds. For example, a statement that denies CA certificates also denies requests that use a subordinate CA template. For more information, see [Use AWS Private CA certificate templates](UsingTemplates.md).
+ **Absent keys.** Check what each statement does for certificates that don't have the key, as described in [How condition key values are evaluated](certguard-evaluation.md).
+ **Testing.** Apply the policy in a non-production account or organizational unit, and issue certificates that represent each of your use cases before you apply it more widely.

To troubleshoot requests that are denied, see [AccessDeniedException with X.509 certificate condition keys](troubleshoot-certguard.md).