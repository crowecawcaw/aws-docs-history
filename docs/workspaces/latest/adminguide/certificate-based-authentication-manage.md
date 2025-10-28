# Manage Certificate-based

Authentication

After you enable certificate-based authentication, review the following
tasks.

## Private CA

Certificate

In a typical configuration, the private CA certificate has a validity period
of 10 years. For more information about replacing a private CA with an expired
certificate, or reissuing the private CA with a new validity period, see [Managing the private CA lifecycle](../../../privateca/latest/userguide/ca-lifecycle.md "../../../privateca/latest/userguide/ca-lifecycle.md")

## End User

Certificates

End user certificates issued by AWS Private Certificate Authority for WorkSpaces Pools certificate-based
authentication don't require renewal or revocation. These certificates are
short-lived. WorkSpaces Pools automatically issues a new certificate for each new
session, or every 24 hours for sessions with a long duration. The WorkSpaces Pools
session governs the use of these end user certificates. If you end a session,
WorkSpaces Pools stops using that certificate. These end user certificates have a
shorter validity period than a typical AWS Private Certificate Authority CRL distribution. As a result,
end user certificates don't need to be revoked and won't appear in a CRL.

## Audit

Reports

You can create an audit report to list all of the certificates that your
private CA has issued or revoked. For more information, see [Using audit reports with your private CA](../../../privateca/latest/userguide/PcaAuditReport.md "../../../privateca/latest/userguide/PcaAuditReport.md").

## Logging and

Monitoring

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
