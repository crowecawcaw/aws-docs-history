

# Troubleshoot Connector for SCEP connector creation failures

When connector creation fails, the connector's status is `FAILED` and the status reason describes the cause. The following table describes status reasons and recommended steps for resolution.


| Status reason | Root cause | Remediation | 
| --- | --- | --- | 
| `PRIVATECA_ACCESS_DENIED` | Connector for SCEP is unable to issue certificates from your private CA. Your IAM policy doesn't allow `acm-pca:IssueCertificate`, or you haven't shared the private CA with Connector for SCEP using AWS Resource Access Manager. | For information about setting up Connector for SCEP, see [Set up Connector for SCEP](connector-for-scep-setting-up.md). Check that your IAM policy allows `acm-pca:IssueCertificate` and that you have shared the private CA with Connector for SCEP.<br />If your policies use X.509 certificate condition keys (`acm-pca:x509*`), see [Allow connector creation when you use X.509 certificate condition keys](pca-rbp.md#connector-permission-check-condition-keys).<br />After fixing the permissions, delete the failed connector and create a new one. | 