# Manage Certificate-based Authentication

After you enable certificate-based authentication, review the following
tasks.

## Private CA Certificate

In a typical configuration, the private CA certificate has a validity period
of 10 years. For more information about replacing a private CA with an expired
certificate, or reissuing the private CA with a new validity period, see [Managing the private CA lifecycle](../../../privateca/latest/userguide/ca-lifecycle.md "../../../privateca/latest/userguide/ca-lifecycle.md")

## End User Certificates

End user certificates issued by AWS Private Certificate Authority for WorkSpaces Pools certificate-based
authentication don't require renewal or revocation. These certificates are
short-lived. WorkSpaces Pools automatically issues a new certificate for each new
session, or every 24 hours for sessions with a long duration. The WorkSpaces Pools
session governs the use of these end user certificates. If you end a session,
WorkSpaces Pools stops using that certificate. These end user certificates have a
shorter validity period than a typical AWS Private Certificate Authority CRL distribution. As a result,
end user certificates don't need to be revoked and won't appear in a CRL.

## Audit Reports

You can create an audit report to list all of the certificates that your
private CA has issued or revoked. For more information, see [Using audit reports with your private CA](../../../privateca/latest/userguide/PcaAuditReport.md "../../../privateca/latest/userguide/PcaAuditReport.md").

## Logging and Monitoring

You can use CloudTrail to record API calls to a private CA by WorkSpaces Pools. For more
information see [What Is
AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") in the _AWS CloudTrail User Guide_, and
[Using CloudTrail](../../../privateca/latest/userguide/PcaCtIntro.md "../../../privateca/latest/userguide/PcaCtIntro.md") in the _AWS Private Certificate Authority User Guide_.
In CloudTrail Event history you can view **GetCertificate** and
**IssueCertificate** event names from
**acm-pca.amazonaws.com** event source made by the
WorkSpaces Pools **EcmAssumeRoleSession** user name. These events
will be recorded for every WorkSpaces Pools certificate-based authentication request.
For more information, see [Viewing
events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User
Guide_.

## Monitor and manage PCA certificate limits

When you use certificate-based authentication (CBA) with WorkSpaces Pools,
AWS Private Certificate Authority issues a short-lived certificate for each user session. PCA enforces
two limits that can block certificate issuance:

1. **CA issuance limit** — The total number
   of certificates a CA can issue over its lifetime. This is cumulative and
   does not decrease when certificates expire or are revoked.
2. **CRL capacity limit** — The maximum
   number of revoked, unexpired certificates that can appear on the CRL at
   any given time. When revoked certificates expire, they are removed from
   the CRL and free up capacity.

By default with complete CRLs, both limits are set to 1 million, so they
behave as a single constraint. However, if you request a CA issuance limit
increase, the two limits become independent — your CA can issue more certificates over its
lifetime, but the CRL can still only hold 1 million revoked, unexpired
certificates at once.

When either limit is reached, PCA stops issuing new certificates and
WorkSpaces Pools users cannot authenticate.

### Understand your risk

Because the CA issuance limit is cumulative, even short-lived WorkSpaces Pools
certificates (24 hours) count permanently against it. Each user session
issues one certificate, so your daily issuance rate equals your daily active
user count.

For example, a deployment with 10,000 daily active users exhausts the
default 1M CA issuance limit in 100 days (approximately 3 months).

If you share the same private CA with non-WorkSpaces workloads that
have longer-lived certificates, you face additional risk from the CRL capacity
limit, because revoked certificates from those workloads remain on the CRL until they expire.

### Check your current certificate usage

You can monitor your CA issuance usage in the following ways:

- **PCA Console** — Open the [AWS Private CA
  console](https://console.aws.amazon.com/acm-pca/ "https://console.aws.amazon.com/acm-pca/"), choose your CA, and view the certificate usage
  metrics on the **Monitoring**
  tab.
- **Amazon CloudWatch** — PCA publishes
  the `CertificatesPerCA` metric to CloudWatch. This metric
  tracks cumulative lifetime issuance and maps directly to the CA
  issuance limit. You can create an alarm to notify you when usage
  approaches your limit. For more information, see [Using
  CloudWatch metrics with AWS Private Certificate Authority](../../../privateca/latest/userguide/PcaCloudWatch.md "../../../privateca/latest/userguide/PcaCloudWatch.md").

Set a CloudWatch alarm on
`CertificatesPerCA` at 70–80% of your CA's configured issuance
limit to allow time to request an increase or plan a CA rotation.

### Request a limit increase

If your CA issuance usage is approaching the limit, you can request an
increase by opening a support case:

1. Open the [AWS Support
   Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").
2. Choose **Create case** and choose
   **Technical**.
3. For **Service**, choose **AWS Private Certificate Authority**.
4. For **Category**, choose **Certificate Limits**.
5. In the description, include your AWS account ID, the ARN of the
   affected private CA, your current certificate usage (from the PCA
   console or CloudWatch), and the new limit you are
   requesting.

There is no additional cost for a higher issuance limit.

###### Important

When your CA issuance limit is increased beyond the CRL capacity (1M
for complete CRLs), the two limits become independent constraints. Your
CA can issue more certificates over its lifetime, but the CRL can still
only hold 1 million revoked, unexpired certificates at any given
time.

If your workload revokes enough certificates to fill the CRL,
issuance is blocked until some of those revoked certificates expire.
For most WorkSpaces Pools-only deployments, this is unlikely to be an issue
because WorkSpaces Pools certificates are not revoked and do not appear on
the CRL.

### Best practices

- **Use a dedicated private CA for WorkSpaces Pools
  CBA.** Sharing a CA across multiple workloads with
  longer-lived certificates increases the risk of filling the CRL
  capacity limit.
- **Monitor
  `CertificatesPerCA` with CloudWatch
  alarms.** Set an alarm at 70–80% of your configured
  issuance limit so you can request an increase or rotate to a new CA
  before users are affected.
- **Plan for CA rotation.** Because the
  issuance limit is cumulative, high-volume deployments eventually need
  to rotate to a new CA or request periodic limit increases.
- **Consider partitioned CRLs with
  caution.** Partitioned CRLs support 100M certificates
  for both the issuance and CRL capacity limits. However, they have a
  known limitation: every time a new CRL partition is rotated,
  there can be up to a 15-minute window where the CRL file is absent,
  which might cause authentication failures.
