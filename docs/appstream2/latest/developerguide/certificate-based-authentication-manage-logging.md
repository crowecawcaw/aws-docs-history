# Logging and Monitoring

You can use CloudTrail to record API calls to a private CA by WorkSpaces Applications. For more
information see [What Is
AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and [Using CloudTrail](../../../privateca/latest/userguide/PcaCtIntro.md "../../../privateca/latest/userguide/PcaCtIntro.md").
In CloudTrail Event history you can view **GetCertificate** and
**IssueCertificate** event names from
**acm-pca.amazonaws.com** event source made by the
WorkSpaces Applications**EcmAssumeRoleSession** user name. These events will
be recorded for every WorkSpaces Applications certificate-based authentication request. For more
information, see [Viewing
events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").
