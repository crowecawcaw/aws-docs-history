

# Logging and Monitoring
<a name="certificate-based-authentication-manage-logging"></a>

You can use CloudTrail to record API calls to a private CA by WorkSpaces Applications. For more information see [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Using CloudTrail](https://docs.aws.amazon.com/privateca/latest/userguide/PcaCtIntro.html). In CloudTrail Event history you can view **GetCertificate** and **IssueCertificate** event names from **acm-pca.amazonaws.com** event source made by the WorkSpaces Applications**EcmAssumeRoleSession** user name. These events will be recorded for every WorkSpaces Applications certificate-based authentication request. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).